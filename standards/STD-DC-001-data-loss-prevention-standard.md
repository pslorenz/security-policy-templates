# STD-DC-001: Data Loss Prevention Standard

| | |
|---|---|
| **Document ID** | STD-DC-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This standard sets the technical requirements for data loss prevention (DLP) at [ORGANIZATION_NAME]: the labels, detection rules, and enforcement that back up the handling rules in POL-DC-001.

POL-DC-001 tells people how to handle each classification. DLP catches the moments when they don't: the spreadsheet of Social Security numbers attached to the wrong email, the client file shared with "anyone with the link," the API key pasted into a chat channel, the customer list uploaded to a personal cloud drive. Most data loss in small organizations is accidental, and accidental loss is what DLP is good at stopping.

DLP will not stop a determined insider, who can photograph a screen, and the standard does not pretend otherwise. Its job is to make the safe path the easy one, to stop the common mistakes before they leave the building, and to produce a record when something does.

## 2. Scope

This standard applies to [ORGANIZATION_NAME] data classified Confidential or Restricted under POL-DC-001, in these channels:

Outbound email. File sharing and collaboration in the productivity platform and approved SaaS applications. Chat and messaging platforms. Managed endpoints, including removable media, printing, and uploads to websites. Source code repositories. Generative AI tools, under POL-AI-001 Section 3.1.

Public data is out of scope. Personal devices are covered only through the application-level controls permitted under POL-IAM-002 Section 3.4.

## 3. Standard Requirements

### 3.1 Start Narrow and Monitor First

DLP rules that block too much get turned off. Every rule starts in monitoring mode, which records matches and shows users a warning but does not block, for at least thirty days. During that time the Information Security function reviews the matches, tunes out false positives, and confirms the rule catches what it is meant to catch. Only then does the rule move to enforcement.

The first rules deployed cover Restricted data, because a missed Restricted match costs the most and Restricted data types are the easiest to detect accurately. Confidential rules follow once the Restricted rules are stable.

### 3.2 What DLP Detects

Detection rules cover the Restricted data types in POL-DC-001 Section 3.3, using the platform's built-in detectors where they exist:

Payment card numbers, validated with a checksum to reduce false positives. Social Security numbers and other national identification numbers. Bank account and routing numbers. Authentication credentials: passwords in known formats, API keys, access tokens, private keys, and connection strings. Health information, where [ORGANIZATION_NAME] handles it. Client identifiers or account numbers that a contract designates as Restricted, using custom patterns.

A single match in a long document is often a false positive. Rules for most data types trigger on a minimum count (for example, five or more card numbers in one item) or on a match combined with a supporting keyword, and the thresholds are recorded with each rule.

### 3.3 Sensitivity Labels

Where the productivity platform supports sensitivity labels, labels implement the classification marking in POL-DC-001 Section 3.8:

New documents and messages are labeled Confidential by default where the platform supports a default label, matching the default classification in POL-DC-001 Section 3.2. The Restricted label applies encryption, blocks sharing outside [ORGANIZATION_NAME] unless the recipient is explicitly authorized, and blocks forwarding and printing where the platform supports it. Content containing Restricted data types is labeled Restricted automatically where the platform supports automatic labeling, or the user is prompted to label it. Lowering a label requires the user to give a reason, which is logged.

### 3.4 Rules by Channel

| Channel | Confidential data | Restricted data |
|---|---|---|
| Outbound email to external recipients | Warn the user; allow with a stated business reason | Block unless sent through the approved secure method; notify the Information Security function |
| File sharing outside [ORGANIZATION_NAME] | Allow to named recipients; block "anyone with the link" sharing | Block, except through an approved secure sharing method to an authorized recipient |
| Chat and messaging | Warn on external chats | Block credentials and Restricted data types in any chat; remove the message and notify the sender |
| Removable media | Allow only to encrypted, company-issued media | Block |
| Printing | Allow | Allow only where the business process requires it; log |
| Uploads to websites and personal cloud storage | Block uploads to unapproved cloud storage and personal email | Block |
| Generative AI tools | Allow only to tools approved under POL-AI-001 Section 3.2 | Block, except tools approved for the specific Restricted category |
| Source code repositories | Not applicable | Block commits containing credentials (Section 3.6) |

Endpoint rules require the DLP or device management agent on managed devices. Where the platform cannot enforce a rule in a channel, the gap is recorded and the handling rule in POL-DC-001 still applies to users.

### 3.5 What the User Sees

When a rule triggers, the user sees a message explaining what was detected and why the action is limited, in plain language, with a link to POL-DC-001. Where a rule allows an override, the user gives a business reason, and the reason is logged and reviewed. Overrides are for legitimate exceptions. A user who overrides the same rule repeatedly is a conversation for their manager, not an automatic violation.

### 3.6 Credentials in Code and Chat

Secret scanning runs on every repository [ORGANIZATION_NAME] controls, including commit history, and blocks pushes that contain credentials where the platform supports push protection. Credentials found in repositories, chat, email, tickets, or documents are treated as exposed: they are rotated within seven days under POL-IAM-003 Section 3.4, and the location is cleaned. Deleting the message or file does not make the credential safe, because copies and history remain.

### 3.7 Alert Handling

DLP alerts go to the Information Security function or the security service provider. Alerts on Restricted data are reviewed within one business day. An alert showing Restricted data actually sent or shared outside the organization without authorization is handled as a security incident under POL-IR-001, as POL-DC-001 Section 5 requires.

Each month, the Information Security function reviews alert volumes, false positives, and overrides, and tunes rules. A rule with mostly false positives is fixed or returned to monitoring mode, not left to train users to ignore it.

### 3.8 Privacy and Access to DLP Data

DLP inspects the content of messages and files. Users are told this through the monitoring notice in POL-AUP-001 Section 3.1. Access to DLP alert content and incident details is limited to named members of the Information Security function, and DLP data is not used for purposes other than protecting data and investigating incidents. Where local law or a works agreement requires notice or consultation before content inspection, [ORGANIZATION_NAME] follows it.

### 3.9 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6. A business process that needs to send Restricted data externally is approved as an exception with a defined secure method, rather than by turning off the rule.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Designs and tunes rules, reviews alerts and overrides, and moves rules from monitoring to enforcement.

**IT function (or IT service provider).** Deploys labels, DLP policies, endpoint agents, and secret scanning.

**Data owners.** Confirm which data types in their domain need detection rules, and approve exceptions for their business processes.

**Managers.** Address repeated overrides with their team members.

**All users.** Label data where prompted. Read DLP warnings before overriding them. Report data sent to the wrong place.

## 5. Enforcement

Specific remediation timelines:

Restricted data detection rules not in enforcement: moved to enforcement within ninety days of deployment, or the reason documented. Credentials found in repositories or chat: rotated within seven days. Restricted data shared externally without authorization: handled under POL-IR-001. Rules with persistent false positives: tuned or returned to monitoring mode within thirty days.

## 6. Related Documents

POL-DC-001: Data Classification and Handling Policy (the handling rules this standard enforces)
POL-AUP-001: Acceptable Use Policy (monitoring notice and user data handling)
POL-AI-001: AI and Agent Governance Policy (data allowed in AI tools)
POL-IAM-003: Non-Human Identity Governance Policy (credential rotation)
POL-IAM-002: Remote Access Policy (personal device access)
POL-DEV-001: Secure Development Policy (secrets in source code)
POL-IR-001: Incident Response Policy (data exposure incidents)
STD-LOG-001: Logging and Monitoring Standard (DLP alert logging)
POL-GOV-001: Information Security Policy (exceptions)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.DS-01 (The confidentiality, integrity, and availability of data-at-rest are protected). PR.DS-02 (The confidentiality, integrity, and availability of data-in-transit are protected). PR.DS-10 (The confidentiality, integrity, and availability of data-in-use are protected). DE.CM-03 (Personnel activity and technology usage are monitored to find potentially adverse events).

**CIS Controls v8.1:**

Control 3 Data Protection: Safeguards 3.3 (configure data access control lists), 3.7 (establish and maintain a data classification scheme), 3.9 (encrypt data on removable media), 3.13 (deploy a data loss prevention solution).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
