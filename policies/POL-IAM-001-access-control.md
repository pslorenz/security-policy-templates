# POL-IAM-001: Access Control Policy

| | |
|---|---|
| **Document ID** | POL-IAM-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] manages who can access what. It covers user accounts, the permissions those accounts have, how access is granted and removed, and how privileged access is handled.

The goal is simple. Every person and every system should have only the access they need to do their work. Nothing more.

## 2. Scope

This policy covers all accounts that access [ORGANIZATION_NAME] systems and data. That includes:

Employees, contractors, and temporary workers. Vendors and service providers with access to our environment. Service accounts and other non-human accounts (covered in detail by POL-IAM-011). Customer accounts that access systems we operate.

It applies to all systems we use. That includes Microsoft 365 or Google Workspace, cloud platforms like Azure or AWS, line-of-business applications, file storage, and any other system that holds company data or supports company operations.

## 3. Policy Statements

### 3.1 Every Account Has an Owner

Every account in our environment must be tied to a specific person. For employee accounts, that person is the employee. For service accounts and integrations, that person is whoever is responsible for the system or process that uses the account.

Shared accounts are not allowed. If two people need to access the same system, they each get their own account. The only exception is a documented break-glass account used for emergency access, which is covered in Section 3.7.

### 3.2 Access Is Granted Based on Job Need

People get access to what they need to do their job. They do not get access to everything.

When someone joins the company or changes roles, their access is set up based on their job. We use a documented set of access patterns (sometimes called roles or access profiles) so people in similar jobs get similar access. This makes it easier to set up new people correctly and easier to spot when someone has more access than they should.

Requests for access beyond the standard set for someone's role go through a documented approval process. The approver is the person's manager or the owner of the system being accessed. Approvals are recorded.

### 3.3 Access Is Reviewed Regularly

Every quarter, managers review who reports to them and confirm that each person still has the right access for their current job. Access that is no longer needed is removed.

For systems that hold sensitive data or support critical operations, the system owner also reviews access quarterly. They confirm that the people listed should still have access and that the access level is still appropriate.

The review is documented. Anyone who appears in the review and has changed roles, left the company, or no longer needs the access has their access removed within thirty days.

### 3.4 Access Is Removed Promptly When People Leave

When an employee or contractor leaves [ORGANIZATION_NAME], their access is removed on their last day. For voluntary departures, the access removal is scheduled in advance. For involuntary departures, the access removal happens at the time of termination.

Removal includes:

The user's primary identity (their Microsoft 365 or Google Workspace account, their Active Directory account if applicable). Any additional accounts they had on specific systems. Any shared credentials they knew (which means changing those credentials, since we cannot un-tell them what the password was). Physical access (badge, building keys, parking access) where applicable.

For roles with significant access, this removal is verified by a second person who confirms each step was completed.

### 3.5 Privileged Access Gets Extra Care

Some accounts have permissions to make changes that affect many people or systems. These are called privileged accounts. Examples include domain administrators, global administrators in Microsoft 365, root accounts in cloud platforms, and administrative access to financial or HR systems.

Privileged accounts follow stricter rules:

They are separate from the user's normal account. The same person who has a privileged account also has a regular account they use for email, web browsing, and routine work. The privileged account is used only for privileged tasks.

They use phishing-resistant authentication (FIDO2 hardware keys, platform passkeys, or certificate-based authentication). Text-message and push-notification multi-factor authentication are not acceptable for privileged accounts because attackers can defeat them.

They use just-in-time access where the platform supports it. Instead of having permanent administrator rights, the user requests elevated access when they need it, the access lasts for a defined window (typically one to eight hours), and it expires automatically.

Privileged access is reviewed monthly rather than quarterly.

### 3.6 Multi-Factor Authentication Is Required

Every account that accesses [ORGANIZATION_NAME] systems uses multi-factor authentication. There are no exceptions for executives, no exceptions for legacy systems, and no exceptions for "just for now."

For standard user accounts, push-notification or authenticator-app MFA is acceptable. For privileged accounts, phishing-resistant authentication is required as described in Section 3.5.

Where a system does not support MFA, we put it behind a system that does (such as a single sign-on portal, an identity provider, or a jump host). If that is not possible, we replace the system within a documented timeline or accept a documented risk.

### 3.7 Break-Glass Accounts Are Tightly Controlled

We maintain a small number of emergency-use accounts that allow access if normal authentication systems fail. These are called break-glass accounts.

Break-glass accounts follow these rules:

They are used only for emergencies. Routine administration uses normal accounts. The credentials are stored in a secure way that requires multiple people to retrieve them (split between trusted custodians, stored in a sealed envelope in a safe, or held in a privileged access management tool that logs retrieval).

Their use is logged and reviewed. If a break-glass account is used, the use triggers an alert to the security team, and the use is reviewed within twenty-four hours. The credentials are rotated after each use.

They are reviewed quarterly to confirm the accounts still exist, the credentials are still recoverable, and only the intended people have access to them.

### 3.8 Vendor and Third-Party Access Is Documented and Limited

When vendors, contractors, or other outside parties need access to our systems, the access is documented. The documentation includes who the access is for, what they need to do, what access they need, and when the access ends.

Vendor accounts have an end date. When the engagement ends, the access is removed. If the engagement is ongoing, the access is reviewed at least annually.

Vendors who need privileged access follow the same rules as our internal privileged users (Section 3.5). They are not given standing administrative rights.

### 3.9 Records and Logging

We log access events. That includes successful and failed login attempts, password changes, account creation and deletion, permission changes, and use of privileged access.

Logs are kept for at least one year. Where regulations require longer retention (some industries require seven years or more), we follow the longer requirement.

Logs are reviewed by the security team or the security service provider. Routine review looks for anomalies. Investigation in response to suspected incidents uses the logs as a primary source of evidence.

### 3.10 Exceptions

Sometimes business needs conflict with policy requirements. When that happens, the conflict is documented as an exception and approved by the executive sponsor.

Exceptions include:

The specific provision being excepted. The business reason for the exception. What we are doing instead to manage the risk. When the exception ends.

No exception lasts more than twelve months without renewal. All active exceptions are reviewed quarterly.

## 4. Roles and Responsibilities

**[ORGANIZATION_NAME] leadership.** Approves the policy. Sets the executive sponsor. Funds the work needed to implement and maintain the policy.

**Information Security function (which may be an internal team, an MSP, or a vCISO).** Owns the policy. Maintains the access patterns. Reviews privileged access monthly. Investigates anomalies. Approves exceptions.

**IT function (or IT service provider).** Implements access controls in the systems we use. Provisions and deprovisions accounts. Maintains the logging. Supports the access review process.

**Managers.** Review their team members' access quarterly. Approve access requests for their team members. Notify IT when team members change roles or leave.

**System owners.** Review access to their systems quarterly. Approve access requests to their systems. Maintain the documented access patterns for their systems.

**All employees, contractors, and vendors.** Use their accounts in accordance with this policy and the Acceptable Use Policy. Do not share credentials. Report suspected account compromise immediately.

## 5. Enforcement

Violations of this policy may result in remediation action, including loss of access, escalation to the user's manager, and disciplinary action consistent with [ORGANIZATION_NAME]'s human resources policies. For contractors and vendors, violations may result in contract termination.

Specific remediation timelines:

Account ownership not assigned: documented and assigned within thirty days, or the account is disabled. Access not aligned with job role: corrected within thirty days of identification. Privileged accounts without phishing-resistant authentication: enabled within thirty days, or the account is converted to a standard account. Shared credentials in use: rotated and replaced with individual accounts within sixty days. Vendor access without documented end date: documented or removed within thirty days.

## 6. Related Documents

POL-IAM-002: Password and Authentication Standard (specific technical requirements for credentials)
POL-IAM-011: Non-Human Identity Governance Policy (service accounts and automation identities)
POL-AUP-001: Acceptable Use Policy (how users are expected to behave)
POL-IR-001: Incident Response Policy (what we do when something goes wrong)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.AA-01 (Identities and credentials are managed). PR.AA-02 (Identities are proofed and bound to credentials). PR.AA-03 (Users, services, and hardware are authenticated). PR.AA-04 (Identity assertions are protected). PR.AA-05 (Access permissions, entitlements, and authorizations are defined and managed).

**CIS Controls v8:**

Control 5 Account Management: Safeguards 5.1 (inventory of accounts), 5.2 (use unique passwords), 5.3 (disable dormant accounts), 5.4 (restrict administrator privileges), 5.6 (centralize account management).

Control 6 Access Control Management: Safeguards 6.1 (access granting process), 6.2 (access revoking process), 6.3 (require MFA for externally-exposed applications), 6.4 (require MFA for remote network access), 6.5 (require MFA for administrative access), 6.7 (centralize access control), 6.8 (role-based access control).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above. Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution-ShareAlike 4.0.*
