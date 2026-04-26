# POL-IAM-011: Non-Human Identity Governance Policy

| | |
|---|---|
| **Document ID** | POL-IAM-011 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] manages non-human identities. A non-human identity is any account that an automated tool, integration, or service uses to log in. Examples include the account that runs your nightly backup, the connector that syncs HR data into Microsoft 365, the API key your CRM uses to talk to your accounting system, and the service account that keeps an application running on a server.

In most organizations, there are far more non-human accounts than human users. Industry research puts the ratio at roughly forty-five to one. A fifty-person company easily has over two thousand of them.

These accounts often have strong access. They are also often forgotten. An account with broad access and no named owner is a credential waiting to be used by someone who should not have it. This policy makes sure every non-human identity has a named owner, a documented purpose, the right level of access, and a defined lifecycle.

## 2. Scope

This policy covers every non-human identity used in [ORGANIZATION_NAME] systems. That includes:

Service accounts in Microsoft Entra ID and Active Directory. Service principals, managed identities, and application registrations in Microsoft 365 and Azure. AWS IAM roles, Google Cloud service accounts, and equivalent identities in other cloud platforms. API keys and OAuth grants connecting SaaS applications to each other. GitHub Actions tokens, personal access tokens, and deploy keys. Power Automate connections, Power Apps service principals, Zapier and Make automations. Backup software credentials, monitoring agent credentials, RMM agent credentials, and other operational tooling. AI agent identities and Model Context Protocol (MCP) server credentials.

It applies to every identity in this category regardless of who created it or where it lives. Identities created outside the standard process are still in scope, and their existence without governance is a violation.

## 3. Policy Statements

### 3.1 Every Non-Human Identity Has a Named Owner

Every non-human identity must have a named human owner. The owner is a current employee responsible for the identity's purpose, its access, and its eventual removal.

Group ownership is not enough. "The IT team" or "Engineering" is not an acceptable owner. A specific person must be on the hook.

When the owner leaves [ORGANIZATION_NAME] or changes roles, ownership is reassigned within thirty days. The reassignment is logged.

Identities without a current owner are treated as orphans. Orphan identities are disabled until ownership is assigned or the identity is removed.

### 3.2 Every Non-Human Identity Has a Documented Purpose

Every non-human identity must have a written purpose. The documentation explains what business function the identity supports, what systems it accesses, what kind of data it touches, and why it has the access it has.

The purpose is recorded in the inventory described in Section 3.6 and reviewed each quarter. Identities whose purpose cannot be documented or justified are removed.

### 3.3 Least Privilege

Non-human identities get only the access they need to do their documented job. Nothing more.

Specific rules:

Global administrator, tenant administrator, or equivalent top-level access is not granted to non-human identities except where there is no technical alternative. Where there is no alternative, the grant is documented, approved by the Information Security function, and reviewed quarterly.

A human user does not share their account with an automation. Automation gets its own service identity. The user's normal account is not used to run scheduled tasks or service connections.

Permissions are scoped to specific resources where the platform supports it. "Access to all mailboxes" or "read all SharePoint sites" is replaced with site-specific or mailbox-specific grants where possible. Microsoft 365 supports this through Application Access Policies and site-scoped permissions; most modern platforms have similar features.

Application permissions on API integrations (the kind that act on their own behalf rather than on behalf of a user) are used only when the automation truly does not need a user context. When an automation acts on behalf of a specific person, delegated permissions are preferred.

### 3.4 Credentials Live in a Secrets Vault

Service account passwords, client secrets, API keys, and similar credentials are stored in a secrets management platform. Approved platforms for [ORGANIZATION_NAME] are [APPROVED_SECRETS_PLATFORMS, e.g., Azure Key Vault, AWS Secrets Manager, HashiCorp Vault, 1Password, Bitwarden].

Storage in any of these places is prohibited:

Source code repositories or any file checked into version control. Configuration files on shared drives or shared servers. Email messages, chat platforms, or documentation wikis. Spreadsheets, even password-protected ones. Environment variables on shared systems. Scripts or scheduled tasks where the credential appears in plain text.

When platforms support better options, use them instead of stored secrets:

Managed identities in Azure (the platform handles credentials automatically; nothing to store or rotate). AWS IAM roles with instance profiles. GCP service accounts with workload identity federation. Certificate-based authentication with automatic rotation.

These options are preferred wherever a workload runs on cloud infrastructure that supports them. If managed identity is available, use it.

### 3.5 Credentials Get Rotated

Service account credentials that cannot be replaced with managed identities or certificates are rotated on a schedule.

High-privilege credentials (administrator, root, database owner, equivalent): every ninety days.

Standard service credentials: at least annually.

Credentials that have been exposed or are suspected of being exposed: immediately, regardless of the regular schedule.

Each rotation is logged. The log is checked during the quarterly access review.

Each non-human identity has its own credentials. Sharing credentials between identities or between environments (production reusing development credentials) is not allowed.

### 3.6 The Inventory

[ORGANIZATION_NAME] maintains a current inventory of every non-human identity in scope. The inventory tracks:

A unique identifier for each identity. The platform where the identity was created. The named owner. The documented purpose. The systems and data it accesses. The privilege level granted. The authentication method in use (managed identity, certificate, secret, key). The date of last credential rotation. The date of last access review. The scheduled date for the next access review or end-of-life.

The inventory is updated within seven days of any provisioning, change, or removal. It is reconciled against the actual platform state at least quarterly. Discrepancies are investigated and corrected within thirty days.

Where the platforms support automated discovery, automation is preferred over manual inventory maintenance. The companion runbook (RUN-IAM-011) describes how to perform the discovery.

### 3.7 Lifecycle

Every non-human identity follows a defined path: provisioning, operation, review, and removal.

**Provisioning.** Requests to create a new non-human identity go through a documented process. The request captures the named owner, purpose, required access, and authentication method. Approvals are recorded. Identities are not created outside this process except in documented emergencies, and emergency provisioning is reviewed retroactively within five business days.

**Operation.** While in service, the identity follows the credential, authentication, and privilege rules in this policy.

**Removal.** Identities are removed when their purpose ends, when the system they support is decommissioned, when the owner leaves and ownership is not reassigned, or when a quarterly access review determines the identity is no longer needed. Removed identities are disabled immediately and deleted thirty days later. The thirty-day disable-before-delete window catches the cases where the removal turns out to break something the team forgot about.

**Dormancy thresholds.** Identities that have not been used in a while are flagged automatically:

Ninety days unused: flagged for review by the owner.

One hundred eighty days unused: disabled, pending the owner justifying continued need.

Three hundred sixty-five days unused: deleted.

### 3.8 Activity Is Logged and Monitored

Authentication events and privileged actions performed by non-human identities are logged to the central logging platform. Logs are kept per the [LOGGING_AND_MONITORING_STANDARD] retention requirements.

At minimum, alerts fire on:

Creation of new credentials or certificates on existing high-privilege identities. Sign-in from a non-human identity from an unexpected location, time window, or source system. Unusual volumes of authentication or API activity. Privilege escalation, including new role assignments or consent grants. Reactivation of an identity that had been disabled. Use of an identity that had been flagged as dormant.

Alerts go through the security operations process and escalate to incident response when warranted.

### 3.9 Quarterly Access Review

Each quarter, the named owner of each non-human identity reviews the identity. The review confirms:

The identity is still needed for its documented purpose. The owner is still correct. The access level is still the minimum needed. The authentication method still meets current standards. Activity logs match what the identity is supposed to be doing.

Review outcomes are recorded in the inventory. Identities that fail review are fixed or removed within thirty days. Reviews not completed within thirty days of their scheduled date trigger automatic disablement of the identity until the review is done.

A summary report goes to the Information Security function each quarter, covering review completion rates, identities fixed, identities removed, and any open exceptions.

The companion template (REV-IAM-011) provides the worksheet for conducting the review.

### 3.10 Exceptions

Some legitimate situations require deviating from this policy. When that happens, the deviation is documented as an exception and approved by the executive sponsor listed in this document.

The exception specifies what control is being excepted, why, what compensating control is in place, and when the exception ends. No exception lasts longer than twelve months without renewal. All active exceptions are reviewed quarterly.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Maintains the inventory. Runs the quarterly access review process. Operates the detection rules for non-human identity activity. Approves exceptions.

**IT function (or IT service provider).** Provisions and removes non-human identities through the approved process. Maintains the authentication mechanisms. Manages the secrets vault. Supports the access reviews.

**Platform and system owners.** Identify the non-human identities their systems require. Submit provisioning requests. Serve as the named owner for identities tied to their platforms unless ownership is formally reassigned.

**Named identity owners.** Review the identities they own each quarter. Notify the Information Security function when ownership changes. Initiate removal when the identity is no longer needed.

**All employees and contractors.** Do not create non-human identities outside the approved process. Do not store credentials in prohibited locations. Report suspected misuse or compromise of a non-human identity immediately.

## 5. Enforcement

Violations of this policy may result in disabling the non-compliant identity, escalation to the named owner's management chain, and disciplinary action consistent with [ORGANIZATION_NAME]'s human resources policies. Repeated non-compliance may result in loss of administrative access privileges.

Specific remediation timelines:

Identities without a named owner: disabled within seven days of detection.

Identities without a documented purpose: documented or removed within thirty days of detection.

Identities with excessive privilege: scoped down or removed within sixty days of detection.

Credentials stored in prohibited locations: rotated and moved to the secrets vault within seven days of detection. The prohibited storage is sanitized.

## 6. Related Documents

POL-IAM-001: Access Control Policy (the parent access control framework)
POL-IAM-002: Password and Authentication Standard (credential strength requirements where shared secrets are unavoidable)
POL-IAM-005: Remote Access Policy (where non-human identities are used for remote integrations)
POL-IAM-006: Single Sign-On and Federation Standard (where federation creates service principals and application registrations)
RUN-IAM-011: Non-Human Identity Discovery Runbook (how to produce and maintain the inventory)
REV-IAM-011: Quarterly Non-Human Identity Access Review (the recurring control template)
[LOGGING_AND_MONITORING_STANDARD]: Logging and Monitoring Standard (log retention requirements)
POL-IR-001: Incident Response Policy (response to non-human identity compromise)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

GV.RR-01, GV.RR-02 (Roles, responsibilities, and authorities for cybersecurity are established). ID.AM-02 (Software, services, and systems are inventoried). ID.AM-05 (Resources are prioritized based on classification, criticality, and mission impact). PR.AA-01 through PR.AA-05 (Identity, credential, and access management). DE.CM-01, DE.CM-03 (Networks and personnel activity are monitored).

**CIS Controls v8:**

Control 5 Account Management: Safeguards 5.1 (inventory of accounts), 5.2 (use unique passwords), 5.3 (disable dormant accounts), 5.4 (restrict administrator privileges to dedicated administrator accounts), 5.5 (establish and maintain an inventory of service accounts), 5.6 (centralize account management).

Control 6 Access Control Management: Safeguards 6.1 (access granting process), 6.2 (access revoking process), 6.7 (centralize access control), 6.8 (role-based access control).

Control 3 Data Protection: Selected safeguards related to access to sensitive data.

Control 8 Audit Log Management: Supporting the logging requirements of this policy.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above. Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution-ShareAlike 4.0.*
