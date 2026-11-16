# STD-AM-001: SaaS Asset Management Standard

| | |
|---|---|
| **Document ID** | STD-AM-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This standard sets the technical requirements for tracking, configuring, and retiring the software-as-a-service (SaaS) applications [ORGANIZATION_NAME] uses. It implements POL-AM-001 Section 3.6, which establishes that SaaS needs special attention, by specifying what that attention consists of.

SaaS is where most of a small organization's data now lives, and it is the asset class least visible to the tools that find hardware. Nobody plugs a SaaS subscription into the network. Someone signs up with a company email address and a credit card, invites a few colleagues, and the application holds customer data for three years before anyone in IT hears its name. When that person leaves, the account and the data stay behind.

This standard closes that gap in three places: finding the applications, setting a security baseline for the ones that hold company data, and retiring them cleanly when they are no longer needed.

## 2. Scope

This standard applies to every SaaS application that holds [ORGANIZATION_NAME] data, supports [ORGANIZATION_NAME] operations, or is accessed with a company identity, including:

Applications procured through the standard process. Applications adopted by a department or individual without procurement, including free tiers. Applications that users signed up for with a company email address. Vendor portals where staff hold accounts on [ORGANIZATION_NAME]'s behalf. The productivity platform itself, which is the most critical SaaS application in most environments.

Cloud infrastructure subscriptions (virtual machines, networks, and platform services) follow POL-AM-001 Section 3.6 and POL-NET-001 Section 3.8 rather than this standard. AI tools follow this standard for inventory and offboarding and POL-AI-001 for approval and connection.

## 3. Standard Requirements

### 3.1 The SaaS Inventory

The SaaS inventory is part of the asset inventory in POL-AM-001 Section 3.2. For each application, it records:

The application and vendor. The business owner, who is accountable for the application's use, and the technical owner, who administers it. The documented purpose. The asset criticality under POL-AM-001 Section 3.7. The highest data classification it holds under POL-DC-001. The vendor tier under POL-TPRM-001 Section 3.1. The authentication method (single sign-on or separate credentials). The provisioning method (automated through SCIM or manual through a documented runbook). The number of administrator accounts and the number of users. Integrations with other systems, linked to their entries in the non-human identity inventory under POL-IAM-003. AI features, linked to TPL-AI-001 where present. Whether audit logs are available and where they go. Whether data can be exported in a usable format. The contract renewal date. The status (Approved, Under review, Restricted, Remove, or Removed).

The inventory is updated within seven days of any onboarding, change, or retirement. Removed applications stay in the inventory, marked Removed, for one year.

### 3.2 Discovery

SaaS discovery uses several sources, because each one misses applications the others catch:

The identity provider's application list and sign-in logs, which show every federated application and every application a user consented to. OAuth consent grants, which show applications connected to company accounts without single sign-on. Expense reports, corporate card statements, and accounts payable records, which show what is being paid for. Inbound mail to company addresses from services the organization does not use, such as account verification and welcome messages, which show sign-ups with company email. Endpoint, browser, or CASB visibility, where available. Procurement records.

The automated sources (identity provider, consent grants, and CASB or endpoint visibility) are reviewed monthly. All sources are reconciled against the inventory quarterly, as part of the reconciliation in POL-AM-001 Section 3.3. Applications found during discovery are handled under Section 3.11.

### 3.3 Onboarding Baseline

Before a SaaS application holds Confidential or Restricted data, it meets this baseline:

The vendor has completed the diligence its tier requires under POL-TPRM-001 Section 3.2. The application is federated with the approved identity provider under STD-IAM-002, or has an approved exception under STD-IAM-002 Section 3.10. User provisioning is automated through SCIM, or a manual provisioning runbook with a named owner exists under STD-IAM-002 Section 3.4. Multi-factor authentication is enforced, through the identity provider where the application is federated. The administrator model in Section 3.4 is in place. Audit logging is enabled at the highest level the subscription offers. A data export path has been confirmed. AI features have been reviewed under POL-AI-001 Section 3.2. The inventory entry under Section 3.1 is complete.

Applications holding only Public data need an inventory entry, a named business owner, and the vendor review for their tier.

### 3.4 Administrative Access

Each application has at least two named administrators, so that one person's absence or departure does not lock [ORGANIZATION_NAME] out of its own data, and no more than three unless the Information Security function approves more. Administrators use individual accounts. Shared administrator accounts are not permitted.

Administrator accounts use phishing-resistant authentication under STD-IAM-001 Section 3.5 where the application or the identity provider supports it, and administrator access is reviewed monthly under POL-IAM-001 Section 3.5.

Where single sign-on is enforced and the application allows it, one local administrator account is kept outside single sign-on for use when the identity provider is unavailable. That account follows the break-glass rules in POL-IAM-001 Section 3.7.

Vendor support access to [ORGANIZATION_NAME]'s tenant is disabled by default where the application allows it, and granted for a defined window when a support case needs it.

### 3.5 Security Configuration Baseline

Applications classified Critical or Important under POL-AM-001 Section 3.7 meet this configuration baseline where the application supports each setting:

External sharing defaults to internal only. External sharing, where needed, uses named recipients rather than public links, and sharing links expire. Public links are disabled for Confidential and Restricted data. Third-party integrations and marketplace apps require administrator approval. Session timeouts follow STD-IAM-001 Section 3.9 where the application controls its own sessions. Device, network, or location restrictions are enforced through the identity provider's conditional access rules under POL-IAM-002 Section 3.3 rather than application by application. Retention settings match the retention determined by the data owner under POL-DC-001 Section 3.7. Audit logs for Critical applications are forwarded to the central logging platform under STD-LOG-001.

Where the vendor publishes a security configuration guide or baseline, it is used as the starting point. The configuration is checked at onboarding, annually, and after the vendor announces significant changes to security or sharing features.

### 3.6 Integrations Between Applications

Every integration that lets one SaaS application read or write another's data, through OAuth, an API key, a webhook secret, or an automation platform, is a non-human identity under POL-IAM-003. It has a named owner, is scoped to the data it needs, keeps its credentials in the secrets vault, and is reviewed quarterly. The SaaS inventory links each integration to its non-human identity entry.

### 3.7 Accounts and Licenses

User accounts in applications that are not provisioned through SCIM are removed on the user's last day, alongside the rest of their access under POL-IAM-001 Section 3.4.

For Critical and Important applications without SCIM, the user list is compared against the current staff roster each quarter, during the access review in POL-IAM-001 Section 3.3. Accounts with no matching current user are disabled. Accounts with no sign-in activity for forty-five days are disabled where the application supports it, consistent with POL-IAM-001 Section 3.3.

Licenses freed by these removals are reclaimed. A license count that keeps growing while headcount stays flat usually means accounts are not being removed.

### 3.8 Data Ownership and Recovery

The SaaS vendor is responsible for the platform. [ORGANIZATION_NAME] is responsible for its data in the platform, including recovery from accidental deletion, malicious deletion by a compromised account, and ransomware that reaches synced files. Most vendors' built-in retention does not cover all of those cases.

For Critical applications that hold data [ORGANIZATION_NAME] cannot recreate, and following STD-DR-001, an independent backup or a scheduled export to storage that [ORGANIZATION_NAME] controls is in place. A restore is tested at least annually, by recovering a sample of data and confirming it is complete and usable.

### 3.9 Annual Review

Each application is reviewed at least annually, ideally before renewal. The review confirms that the application is still used and still needed, the business and technical owners are current, the criticality, classification, and vendor tier are still accurate, the baseline in Sections 3.3 through 3.5 still holds, and no other approved application already does the same job. Applications that fail the review are retired under Section 3.10 rather than renewed.

### 3.10 Retiring an Application

When an application is retired:

Data the organization needs is exported and retained according to its classification and retention requirements. The vendor is asked to delete the remaining data, and confirmation is obtained for Tier 1 vendors, consistent with POL-TPRM-001 Section 3.10. The application is removed from the identity provider, including its single sign-on configuration and SCIM provisioning. Integrations, API keys, and OAuth grants connected to the application are revoked and removed from the non-human identity inventory. DNS records that point to the service (custom domains, verification records, and CNAMEs) are removed, because a record left pointing at a service the organization no longer controls can be claimed by someone else. Email sending authorizations for the service, such as SPF includes and DKIM keys, are removed. Billing is cancelled and the inventory entry is marked Removed.

### 3.11 Unapproved Applications

Applications found through discovery that were not approved are evaluated within thirty days under STD-IAM-002 Section 3.8. The evaluation either brings the application through the onboarding baseline in Section 3.3, replaces it with an approved application, or retires it under Section 3.10.

Users do not sign up for SaaS applications with a company email address outside the approval process, consistent with POL-AUP-001 Section 3.8. A sign-up with a company address creates an account that can receive password resets and company data, whether or not anyone approved it.

### 3.12 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Runs discovery and the quarterly reconciliation. Approves exceptions to the baseline. Approves additional administrator accounts beyond three.

**IT function (or IT service provider).** Configures single sign-on, SCIM, and the configuration baseline. Removes accounts and reclaims licenses. Carries out retirements.

**Procurement function (or whoever approves software purchases).** Routes new SaaS purchases through the onboarding baseline. Provides expense and payables data for discovery.

**Business owners.** Are accountable for each application's use and data. Complete the annual review. Initiate retirement when the application is no longer needed.

**Technical owners.** Administer the application. Maintain the configuration baseline and the manual provisioning runbook where one is needed.

**All users.** Use approved applications for company work. Do not sign up for applications with a company email address outside the approval process. Report applications in use that may not be approved.

## 5. Enforcement

Violations of this standard may result in loss of access to the affected application, retirement of an unapproved application, escalation to the business owner's manager, and disciplinary action consistent with [ORGANIZATION_NAME]'s human resources policies.

Specific remediation timelines:

Applications not in the inventory: inventoried or retired within thirty days of discovery. Applications holding Confidential or Restricted data without the onboarding baseline: baseline met or data removed within sixty days. Applications with fewer than two administrators: second administrator assigned within fourteen days. Shared administrator accounts: replaced with individual accounts within thirty days. Accounts belonging to departed users: removed within one business day of discovery. DNS records pointing to retired services: removed within seven days of discovery.

## 6. Related Documents

POL-AM-001: Asset Management Policy (the parent policy this standard implements)
POL-IAM-001: Access Control Policy (account removal, access review, administrator and break-glass rules)
POL-IAM-002: Remote Access Policy (conditional access rules)
POL-IAM-003: Non-Human Identity Governance Policy (integrations between applications)
STD-IAM-001: Password and Authentication Standard (administrator authentication, session limits)
STD-IAM-002: Single Sign-On and Federation Standard (federation, SCIM, unsanctioned application discovery)
POL-DC-001: Data Classification and Handling Policy (classification and retention)
POL-TPRM-001: Third-Party Risk Management Policy (vendor diligence and offboarding)
POL-AI-001: AI and Agent Governance Policy (AI features in SaaS applications)
POL-AUP-001: Acceptable Use Policy (user sign-ups and software installation)
STD-DR-001: Data Backup and Recovery Standard (SaaS backup and restore testing)
STD-LOG-001: Logging and Monitoring Standard (audit log forwarding)
POL-GOV-001: Information Security Policy (exception process)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

ID.AM-02 (Inventories of software, services, and systems managed by the organization are maintained). ID.AM-04 (Inventories of services provided by suppliers are maintained). ID.AM-08 (Systems, hardware, software, services, and data are managed throughout their life cycles). PR.AA-05 (Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties). PR.PS-01 (Configuration management practices are established and applied). PR.DS-11 (Backups of data are created, protected, maintained, and tested), for Critical SaaS applications. GV.SC-10 (Cybersecurity supply chain risk management plans include provisions for activities that occur after the conclusion of a partnership or service agreement).

**CIS Controls v8.1:**

Control 2 Inventory and Control of Software Assets: Safeguards 2.1 (establish and maintain a software inventory), 2.2 (ensure authorized software is currently supported), 2.3 (address unauthorized software).

Control 4 Secure Configuration of Enterprise Assets and Software: Safeguard 4.1 (establish and maintain a secure configuration process), through Section 3.5.

Control 5 Account Management: Safeguards 5.3 (disable dormant accounts) and 5.4 (restrict administrator privileges to dedicated administrator accounts).

Control 11 Data Recovery: Safeguards 11.2 (perform automated backups) and 11.5 (test data recovery), for Critical SaaS applications under Section 3.8.

Control 15 Service Provider Management: Safeguards 15.1 (establish and maintain an inventory of service providers) and 15.7 (securely decommission service providers).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
