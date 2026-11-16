# RUN-IAM-001: Non-Human Identity Discovery Runbook

| | |
|---|---|
| **Document ID** | RUN-IAM-001 |
| **Related Policy** | POL-IAM-003 (Non-Human Identity Governance) |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Semiannual |
| **Owner** | [POLICY_OWNER] |
| **Audience** | Identity engineer, vCISO, or MSP consultant performing the discovery |

---

## 1. Purpose and Scope

This runbook is the operational companion to POL-IAM-003 (Non-Human Identity Governance Policy). It walks through how to produce the non-human identity inventory the policy requires, how to refresh that inventory each quarter, and how to handle the common findings a first-pass discovery surfaces.

The runbook covers a typical small or mid-market environment running Microsoft 365 with optional on-premises Active Directory, Azure subscriptions, GitHub, Power Platform, and connected SaaS applications. Environments with significant AWS, GCP, or specialized automation tooling need additional steps beyond what is here.

For a typical environment under five hundred users, expect the first-pass discovery to take two to four engineer-days. The quarterly reconciliation that follows takes one to two engineer-days. Environments with heavy Power Platform or engineering tool adoption run longer.

## 2. Prerequisites

Before starting, confirm the following access and tooling are in place.

### 2.1 Access

Entra ID: Global Reader at minimum. Global Administrator is needed only for remediation actions, not for discovery.

Azure subscriptions: Reader role on every subscription in scope.

On-prem Active Directory (if present): Domain User with read access is enough for discovery. Domain Admin is needed only for remediation.

GitHub organizations: Owner, or an organization member with audit log read access.

Power Platform admin center: Power Platform Administrator or Global Administrator.

SaaS platforms (M365 connected apps, HR, finance, anything else holding company data): admin-level read access to the application registration and consent records.

### 2.2 Tooling

PowerShell 7 with the Microsoft.Graph, Microsoft.Graph.Beta.Reports, and Az modules installed and current.

Windows PowerShell 5.1 with the Microsoft.PowerApps.Administration.PowerShell module for Phase 5. That module does not support PowerShell 7.

The ActiveDirectory module (RSAT) for Phase 3, and the GitHub CLI (`gh`) for Phase 4.

Microsoft Entra admin center in a browser for the views that do not have a clean API equivalent yet.

A working directory on a trusted workstation for the output files. The CSV exports below land here.

Access to the organization's secrets vault, so you can compare what credentials are stored to what credentials actually exist in production.

A ticket queue or shared workspace for recording ownership assignments as you make them during the discovery.

### 2.3 Output Artifacts

The discovery produces these files. They feed the inventory required by POL-IAM-003 and the quarterly access review in POL-IAM-003 Section 3.9.

`entra-service-principals.csv` lists every service principal in the Entra tenant with its type, publisher tenant, and enabled state. Last sign-in comes from Phase 2 and granted permissions from `entra-consented-apps.csv`.

`entra-app-registrations.csv` lists every application registration owned by the tenant, including redirect URIs and credential expiration dates.

`entra-consented-apps.csv` lists every third-party enterprise application that has been granted consent, including the permissions granted.

`entra-signin-activity.csv` records the last sign-in for each service principal, from Phase 2.

`ad-service-accounts.csv` lists on-prem service accounts identified by naming convention, SPN presence, and password age.

`github-tokens.csv` covers personal access tokens, deploy keys, and GitHub App installations across in-scope repositories.

`power-platform-connections.csv` lists Power Automate connections and Power Apps connectors, grouped by environment.

`azure-rbac-nhi.csv` lists service principals and managed identities holding Azure RBAC assignments, from Phase 6.

`saas-integrations.csv` is the manual inventory of integrations into business-critical SaaS platforms.

`discovery-findings.md` is the human-readable summary: what you found, what needs remediation, and the priority order.

## 3. Discovery Procedure

The procedure runs in seven phases. Phases run in order because later phases depend on context established earlier.

### 3.1 Phase 1: Entra ID Service Principals and Application Registrations

This is the largest single source of non-human identity sprawl in most M365 environments and the right starting point.

**Enumerate all service principals.**

```powershell
Connect-MgGraph -Scopes "Application.Read.All","Directory.Read.All","AuditLog.Read.All"

$sps = Get-MgServicePrincipal -All -Property Id,DisplayName,AppId,ServicePrincipalType,AccountEnabled,CreatedDateTime,Tags,AppOwnerOrganizationId,SignInAudience

$sps | Select-Object DisplayName,AppId,ServicePrincipalType,AccountEnabled,CreatedDateTime,@{N='IsManagedIdentity';E={$_.ServicePrincipalType -eq 'ManagedIdentity'}},@{N='HomeTenant';E={$_.AppOwnerOrganizationId}} | Export-Csv entra-service-principals.csv -NoTypeInformation
```

The output contains three categories that need separating in analysis:

Managed identities created by Azure resources (`ServicePrincipalType` is `ManagedIdentity`). These are generally safer because they have no credentials to steal, but they still need an owner.

Applications owned by your tenant (`AppOwnerOrganizationId` matches the tenant ID). These are applications the organization registered and is responsible for.

Multi-tenant applications owned by other organizations (`AppOwnerOrganizationId` is different or null). These are third-party integrations the organization has consented to.

**Enumerate all application registrations.**

```powershell
$apps = Get-MgApplication -All -Property Id,DisplayName,AppId,CreatedDateTime,PasswordCredentials,KeyCredentials,RequiredResourceAccess,SignInAudience

$apps | ForEach-Object {
    $app = $_
    $pwCreds = @($app.PasswordCredentials | Select-Object -ExpandProperty EndDateTime -ErrorAction SilentlyContinue)
    $keyCreds = @($app.KeyCredentials | Select-Object -ExpandProperty EndDateTime -ErrorAction SilentlyContinue)
    [PSCustomObject]@{
        DisplayName = $app.DisplayName
        AppId = $app.AppId
        Created = $app.CreatedDateTime
        PasswordCredCount = $app.PasswordCredentials.Count
        KeyCredCount = $app.KeyCredentials.Count
        EarliestSecretExpiry = ($pwCreds + $keyCreds | Sort-Object | Select-Object -First 1)
        LatestSecretExpiry = ($pwCreds + $keyCreds | Sort-Object -Descending | Select-Object -First 1)
        SignInAudience = $app.SignInAudience
    }
} | Export-Csv entra-app-registrations.csv -NoTypeInformation
```

Three things to look for in the output:

Applications with client secrets (`PasswordCredCount` greater than zero) are candidates for conversion to certificates or managed identities.

Applications with expired secrets are candidates for cleanup or intentional rotation.

Applications configured for `SignInAudience` of `AzureADMultipleOrgs`, `AzureADandPersonalMicrosoftAccount`, or `PersonalMicrosoftAccount` without a documented business reason should have their scope reviewed.

**Enumerate consented third-party applications and their permissions.**

This is where most tenants have the largest unmanaged exposure. Every enterprise application a user has granted consent to lives here, along with what it can access.

```powershell
$enterpriseApps = Get-MgServicePrincipal -All -Filter "servicePrincipalType eq 'Application'" -Property Id,DisplayName,AppId,AppOwnerOrganizationId,Tags

$results = foreach ($app in $enterpriseApps) {
    $appRoleAssignments = Get-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $app.Id -All
    $oauth2Grants = Get-MgOauth2PermissionGrant -Filter "clientId eq '$($app.Id)'" -All
    [PSCustomObject]@{
        DisplayName = $app.DisplayName
        AppId = $app.AppId
        PublisherTenant = $app.AppOwnerOrganizationId
        AppRoleCount = $appRoleAssignments.Count
        AppRoles = ($appRoleAssignments.AppRoleId -join ';')
        DelegatedGrantCount = $oauth2Grants.Count
        DelegatedScopes = ($oauth2Grants.Scope -join ';')
    }
}

$results | Export-Csv entra-consented-apps.csv -NoTypeInformation
```

The query returns Microsoft first-party applications alongside third-party ones, and `AppRoles` holds role IDs rather than permission names. Filter out first-party applications by publisher tenant, and resolve role IDs against the resource service principal's `AppRoles` collection when a finding needs the permission name.

Flag any application that has these characteristics:

Application permissions to Graph (`AppRoleCount` greater than zero) without a documented owner.

Broad delegated scopes such as `Mail.ReadWrite`, `Files.ReadWrite.All`, `Sites.FullControl.All`, or `Directory.AccessAsUser.All`.

Publisher tenants that do not match known vendors.

Applications consented during time windows that do not match known procurement events. This often indicates user-level consent that should have required admin consent.

### 3.2 Phase 2: Sign-In Activity and Dormancy

Service principals and applications that have not signed in recently are strong candidates for removal. Entra keeps sign-in logs for thirty days with P1 or P2 licensing (seven days without), and the Graph API returns the same retained data as the portal, so querying raw sign-in logs cannot see further back than that. Use one of two sources instead.

**The service principal sign-in activity report.** Entra tracks the last sign-in for each application independently of log retention. The report is on the Graph beta endpoint and requires P1 or P2 licensing; confirm the cmdlet name against the current Microsoft.Graph.Beta.Reports module.

```powershell
Connect-MgGraph -Scopes "AuditLog.Read.All"

Get-MgBetaReportServicePrincipalSignInActivity -All |
    Select-Object AppId,
        @{N='LastSignIn';E={$_.LastSignInActivity.LastSignInDateTime}},
        @{N='LastDelegatedClientSignIn';E={$_.DelegatedClientSignInActivity.LastSignInDateTime}},
        @{N='LastAppClientSignIn';E={$_.ApplicationAuthenticationClientSignInActivity.LastSignInDateTime}} |
    Export-Csv entra-signin-activity.csv -NoTypeInformation
```

**Exported sign-in logs.** Where service principal and managed identity sign-in logs are exported to the central logging platform under STD-LOG-001, query the full retention period there. In a Log Analytics workspace:

```kusto
union AADServicePrincipalSignInLogs, AADManagedIdentitySignInLogs
| where TimeGenerated > ago(180d)
| summarize LastSignIn = max(TimeGenerated), SignIns = count() by AppId, ServicePrincipalName
```

Join this output against the service principal CSV from Phase 1. A service principal with no row in the output has no recorded sign-in at all. Per POL-IAM-003 Section 3.7, any service principal still enabled with no sign-in in the last ninety days is flagged for review. Anything past one hundred eighty days is flagged for disablement. Build the dormancy section of the discovery findings document from this view.

### 3.3 Phase 3: On-Premises Active Directory Service Accounts

Skip this phase if there is no on-prem AD. For hybrid environments, on-prem service accounts are typically discovered through three heuristics. None is reliable on its own; together they produce a workable inventory.

**Naming convention.** Most organizations use naming patterns for service accounts (`svc-`, `sa-`, `service-`, `_svc`, and similar). Query AD for accounts matching these patterns.

```powershell
Get-ADUser -Filter { (Name -like 'svc*') -or (Name -like 'sa-*') -or (Name -like '*-svc') -or (SamAccountName -like 'svc*') } -Properties Name,SamAccountName,Description,PasswordLastSet,LastLogonDate,Enabled,ServicePrincipalName,TrustedForDelegation |
    Select-Object Name,SamAccountName,Description,PasswordLastSet,LastLogonDate,Enabled,@{N='HasSPN';E={$_.ServicePrincipalName.Count -gt 0}},TrustedForDelegation |
    Export-Csv ad-service-accounts-naming.csv -NoTypeInformation
```

**SPN presence.** Accounts with registered Service Principal Names are almost always service accounts, regardless of naming convention.

```powershell
Get-ADUser -Filter { ServicePrincipalName -like '*' } -Properties Name,SamAccountName,Description,PasswordLastSet,PasswordNeverExpires,LastLogonDate,Enabled,ServicePrincipalName,TrustedForDelegation,AdminCount |
    Where-Object { $_.SamAccountName -ne 'krbtgt' } |
    Export-Csv ad-service-accounts-spn.csv -NoTypeInformation
```

User accounts with SPNs can be Kerberoasted: any domain user can request a service ticket and attempt to crack the account's password offline. Prioritize these accounts for gMSA migration or a long random password.

**Group Managed Service Accounts.** gMSAs are the modern answer to service account credential management. Enumerate them separately because their lifecycle is different.

```powershell
Get-ADServiceAccount -Filter * -Properties Name,SamAccountName,Description,PasswordLastSet,LastLogonDate,Enabled,ServicePrincipalName,PrincipalsAllowedToRetrieveManagedPassword |
    Export-Csv ad-gmsa.csv -NoTypeInformation
```

Consolidate the three CSVs into `ad-service-accounts.csv` with deduplication. Flag for remediation:

Any account with `TrustedForDelegation` set to true.

Any account with `AdminCount` set to 1 (indicating historical membership in a protected group).

Any account with `PasswordLastSet` older than one year that is not a gMSA.

Any account with `PasswordNeverExpires` set that is not a gMSA, since it is exempt from any rotation the domain enforces.

### 3.4 Phase 4: GitHub and Source Control Identities

For organizations using GitHub, the token and key surface is substantial. Personal Access Tokens, fine-grained PATs, deploy keys, GitHub App installations, and Actions secrets all count as non-human identity.

Classic personal access tokens are not enumerable at the organization level. Fine-grained tokens with access to the organization are listed in the organization settings, and organizations can require approval for them. The viable approach combines App inventory, fine-grained token review, deploy key enumeration, and audit log review where the plan includes it.

```bash
gh api /orgs/{org}/installations --paginate > github-app-installations.json

gh api /orgs/{org}/actions/secrets --paginate > github-org-secrets.json

# Deploy keys are per repository
gh repo list {org} --limit 1000 --json nameWithOwner -q '.[].nameWithOwner' |
  while read -r repo; do
    gh api "/repos/$repo/keys" --jq ".[] | {repo: \"$repo\", id, title, read_only, created_at}"
  done > github-deploy-keys.json

# Audit log API requires GitHub Enterprise Cloud. --method GET is required:
# gh api switches to POST when -f parameters are present.
gh api --method GET /orgs/{org}/audit-log --paginate -f phrase="action:personal_access_token" > github-pat-audit.json
```

Review the App installations for Apps that can write to repositories, create branches, merge pull requests, or access Actions. Review the audit log for PAT creation events in the last ninety days and cross-reference against known automation work. Review organization-level Actions secrets and confirm each has a documented owner.

For classic PATs, the compensating control is an organization policy that blocks classic tokens or requires SAML SSO authorization for them, plus a requirement that fine-grained tokens be scoped, time-limited, and approved. Organizations on plans without the audit log API review token activity in the organization settings instead.

### 3.5 Phase 5: Power Platform Connections

Power Automate, Power Apps, Copilot Studio agents, and Power Platform service principals are a growing source of automation identity that most security programs have not yet inventoried. Citizen developers often create connections under their own user identities, which then outlive their employment.

```powershell
# Windows PowerShell 5.1
Add-PowerAppsAccount

$environments = Get-AdminPowerAppEnvironment

foreach ($env in $environments) {
    $connections = Get-AdminPowerAppConnection -EnvironmentName $env.EnvironmentName
    $connections | Select-Object @{N='Environment';E={$env.DisplayName}},ConnectorName,DisplayName,CreatedBy,CreatedTime,LastModifiedTime,Statuses | Export-Csv "power-platform-connections-$($env.DisplayName).csv" -NoTypeInformation -Append
}
```

In the resulting CSVs, flag:

Connections owned by users who have left the organization.

Connections to external systems (social media, consumer file sharing, personal email) that do not match an approved business use case.

Connections with write access to critical systems (Dynamics 365, SQL databases, SharePoint sites marked confidential).

### 3.6 Phase 6: Azure Subscription RBAC

For environments running workloads in Azure, enumerate managed identities and service principals that hold RBAC assignments at the subscription, resource group, or resource level.

```powershell
Connect-AzAccount

Get-AzSubscription | ForEach-Object {
    $null = Set-AzContext -SubscriptionId $_.Id
    $subName = $_.Name
    Get-AzRoleAssignment | Where-Object { $_.ObjectType -eq 'ServicePrincipal' } |
        Select-Object @{N='Subscription';E={$subName}},DisplayName,ObjectId,RoleDefinitionName,Scope,ObjectType
} | Export-Csv azure-rbac-nhi.csv -NoTypeInformation
```

Managed identities report an `ObjectType` of `ServicePrincipal`; join `ObjectId` against the Phase 1 output to separate them from application service principals. Assigning `Set-AzContext` to `$null` keeps its output out of the CSV.

Flag:

Service principals with Owner or Contributor roles at subscription scope. These should be reduced to resource group or resource scope wherever possible.

Service principals with role assignments on production resources whose home application registration shows no recent activity.

Managed identities still assigned to resources that no longer exist (orphaned role assignments).

### 3.7 Phase 7: SaaS Application Inventory

The remaining category is SaaS platforms that authenticate their integrations outside the M365 identity boundary. Examples include HR systems, finance platforms, CRM tools, marketing automation, and any application that predates the move to SSO.

This phase is manual because there is no cross-vendor API for integration discovery. Produce a list of business-critical SaaS applications (from the asset inventory, the SaaS management platform if there is one, or procurement records). For each application, document the following in `saas-integrations.csv`:

Platform name and vendor.

Named owner inside the organization.

Authentication mechanism for integrations (API key, OAuth, service account, shared password).

Integration endpoints and receiving systems.

Last credential rotation date, if known.

Whether credentials are stored in the approved secrets vault.

Environments with more than twenty SaaS platforms benefit from a SaaS management platform to automate this. For smaller environments, an annual spreadsheet refresh is enough.

## 4. Analysis and Findings

With the phase outputs in hand, produce the discovery findings document. The findings document is the handoff to the inventory and the executive-facing summary.

### 4.1 Build the Inventory

For each identity identified across the seven phases, create a row in the inventory required by POL-IAM-003 Section 3.6. Each row includes:

A unique identifier (AppId, SID, key ID, or platform-specific equivalent).

Identity type (service principal, application registration, managed identity, AD service account, gMSA, GitHub App, Power Platform connection, SaaS integration, AI agent, other).

Platform.

Named owner (assigned during or right after discovery).

Documented purpose (drafted during discovery, refined at the first access review).

Privilege level granted.

Authentication mechanism in use.

Last credential rotation date, where applicable.

Last observed activity date.

Initial access review date.

Outstanding remediation items.

### 4.2 Common First-Pass Findings

Every first-pass discovery surfaces a predictable set of findings. Knowing what to expect helps with both the analysis and setting expectations with the business. The volumes below are field estimates from small and mid-market tenants, not survey data.

| Finding | Typical volume | Priority |
|---------|----------------|----------|
| Identities with no named owner | 20-40% of total | High |
| Dormant service principals (90+ days idle) | 15-30% of Entra SPs | Medium |
| Client secrets never rotated | Most password-credential apps | High |
| Broad Graph permissions without justification | 5-15 apps per tenant | Critical |
| AD service accounts with Domain Admin rights | 2-10 accounts typical | Critical |
| Power Platform connections owned by departed users | 10-30% of connections | High |
| GitHub Apps with write access not inventoried | Most organizations | Medium |
| User-consent OAuth grants to unverified publishers | 5-30 per tenant | High |
| Credentials stored outside the secrets vault | Common, varies widely | Critical |
| Managed identities on deleted resources | Small counts per subscription | Low |

### 4.3 Remediation Sequencing

Finding everything is the easy part. Remediation is where most programs stall. Sequence the work by risk, not by finding category, and set realistic timelines.

**Within fourteen days.** Focus on findings that represent active exposure. Disable accounts with Domain Admin rights and no named owner. Rotate credentials stored in prohibited locations and sanitize the prohibited storage. Revoke OAuth consent grants to unverified publishers that have broad Graph permissions. These are the items that cannot wait for the next quarterly cycle.

**Within sixty days.** Focus on the governance gaps. Assign named owners to every identity in the inventory. Document the purpose of every identity. Convert client secrets to certificates or managed identities where the platform allows. Disable dormant identities and schedule their deletion.

**Within one hundred eighty days.** Focus on the structural improvements. Implement automated credential rotation for identities that cannot move to certificates. Reduce over-privileged service principals to resource-scoped permissions. Migrate AD service accounts to gMSAs where possible. Establish the quarterly access review cadence as a recurring discipline.

## 5. Operational Cadence

The discovery procedure runs at two cadences.

The **initial discovery** produces the baseline inventory and drives the first remediation sprint. Two to four engineer-days for a typical environment.

The **quarterly reconciliation** refreshes the inventory against current platform state and feeds the quarterly access review. Re-run phases one through six (phase seven runs annually unless a SaaS Management Platform automates it). Compare each phase's output against the prior quarter's. Investigate additions that do not match an approved provisioning request, deletions that do not match an approved removal request, and unexpected changes in permission or credential state.

The reconciliation typically takes one to two engineer-days once the initial discovery is done and the tooling is in place. The output feeds the quarterly access review in POL-IAM-003 Section 3.9, recorded in TPL-IAM-001, whose Section 2 logs the changes this reconciliation finds.

## 6. Automation Opportunities

The first-pass discovery is mostly manual. The recurring discovery should become more automated over time. Targets, in priority order:

A scheduled runbook in Azure Automation or GitHub Actions that runs the PowerShell from phases one, two, and six weekly and writes the outputs to a monitored storage location. Changes against the prior week's output generate tickets for investigation.

Scheduled ingestion of the CSV outputs into the SIEM or central logging platform, with detection rules for the change patterns documented in POL-IAM-003 Section 3.8.

Integration of the inventory with the organization's access review platform (the identity provider's access review feature or an identity governance platform), so quarterly access reviews run against the inventory rather than as a separate artifact.

Automated removal workflows that disable identities meeting the dormancy thresholds in POL-IAM-003 Section 3.7, with notification to the named owner before disablement and a defined rollback path during the thirty-day deletion window.

## 7. References

### Related Documents in This Library

POL-IAM-003: Non-Human Identity Governance Policy (the parent policy this runbook operationalizes)

POL-IAM-001: Access Control Policy

STD-IAM-001: Password and Authentication Standard

TPL-IAM-001: Quarterly Non-Human Identity Access Review (the recurring review worksheet)

STD-LOG-001: Logging and Monitoring Standard (service principal and managed identity sign-in logs)

### External References

Microsoft Graph PowerShell SDK documentation at `learn.microsoft.com/graph/powershell`

Microsoft Entra service principal and application documentation

Power Platform administrative PowerShell documentation

### Tooling Worth Evaluating

Identity threat detection and response (ITDR) tooling that covers both the cloud identity provider and on-premises directory

Secret scanning across repositories, including history, not only the current branch

Cross-cloud identity enumeration tooling that queries several platforms' APIs from one place

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This runbook is issued under the authority of the executive sponsor named in POL-IAM-003.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
