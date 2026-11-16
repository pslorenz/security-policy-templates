# POL-DC-001: Data Classification and Handling Policy

| | |
|---|---|
| **Document ID** | POL-DC-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] classifies its data and how each classification level is handled. It tells employees what kind of information they are looking at and what they can and cannot do with it.

The reason classification matters is practical. Different data carries different consequences when it is exposed, lost, or stolen. Public information has none. A list of customer credit card numbers has severe consequences. Most of what an organization handles falls between those extremes. Treating all data the same either over-protects the trivial information or under-protects the sensitive information. Classification lets the organization match the level of protection to the actual stakes.

This policy works alongside POL-AUP-001 (Acceptable Use Policy), which establishes user behavior expectations, and POL-AM-001 (Asset Management Policy), which tracks where data lives. The data classification policy adds the rules for what kind of data goes where and what protection it gets.

## 2. Scope

This policy applies to all data created, collected, processed, stored, or transmitted by [ORGANIZATION_NAME]. That includes:

Information about employees, contractors, and other personnel. Information about customers, clients, members, or other external parties [ORGANIZATION_NAME] serves. Financial data, accounting records, billing information, and payment data. Proprietary business information including strategy, pricing, and intellectual property. Vendor and partner information. Authentication credentials, encryption keys, and other security-sensitive data. Operational data including logs, monitoring records, and configuration information. Data received from third parties under confidentiality obligations.

The policy applies regardless of where the data lives: in cloud platforms, in SaaS applications, on company devices, on personal devices used for work, in physical documents, or in conversations. The classification follows the data, not the location.

The policy applies to all employees, contractors, vendors, and other parties who handle [ORGANIZATION_NAME] data. The acceptable use policy makes the user-facing version of these rules clear; this policy provides the underlying framework.

## 3. Policy Statements

### 3.1 The Three Classification Levels

[ORGANIZATION_NAME] uses three data classification levels. Every piece of company data falls into one of them.

**Public.** Information that has been intentionally released for public consumption. Marketing materials, published case studies, regulatory filings, public website content, job postings. Public information has no confidentiality restrictions because the organization has decided to release it.

**Confidential.** Information that is not public and would cause some level of harm to [ORGANIZATION_NAME], its people, or its clients if disclosed without authorization. This is the default classification for most internal company information. Examples include internal communications, employee contact information, financial details that have not been disclosed publicly, strategic plans, customer lists, internal documentation, and most operational data.

**Restricted.** Information whose unauthorized disclosure would cause severe harm or trigger regulatory consequences. This is the smallest category by volume but the most consequential by impact. Examples include authentication credentials and encryption keys, payment card data, personal information protected by privacy regulations applicable to the organization, financial information of individuals (Social Security numbers, bank account numbers, tax records), the most sensitive customer information, and information received under specific confidentiality agreements that require this level of protection.

When a piece of data could plausibly fit two levels, classify it at the higher level. The cost of over-protection is small; the cost of under-protection can be substantial.

### 3.2 Default Classification

If data has not been classified, it is treated as Confidential by default. The default exists so that unclassified data is not accidentally treated as Public.

The Public classification requires affirmative action. Someone with authority to release the information has decided to do so. Marketing publishes the case study. Legal approves the regulatory filing. The communications team posts the announcement. Without that affirmative release, the information is not Public.

The Restricted classification typically also requires affirmative action. Specific data types are designated as Restricted in Section 3.3, and any other data that meets the harm threshold for Restricted is classified that way by the data owner.

### 3.3 What Goes in Each Classification

The classification of specific data types is documented here. The list is not exhaustive but covers the most common types [ORGANIZATION_NAME] handles. Data types not listed are classified by analogy or by the data owner's judgment.

**Public data**: marketing collateral that has been released, blog posts and social media content, published case studies (with client approval), job postings, regulatory filings that have been submitted, press releases, content already on the public website.

**Confidential data**: internal communications (email, chat, internal documents), employee directory information beyond what is public, employee performance information except as noted under Restricted, customer relationship management data, project plans and internal documentation, financial data that has not been disclosed publicly, vendor information, internal training materials, system configuration documentation that does not include credentials, log files in their normal operational state, and most other day-to-day company data.

**Restricted data**: authentication credentials of any kind (passwords, API keys, certificates, recovery codes, MFA backup codes), encryption keys and key material, payment card data subject to PCI DSS requirements, Social Security numbers and equivalent national identification numbers, bank account numbers and routing numbers, tax records and tax identification numbers, employee compensation details and benefits enrollment information, employee medical or disability information, customer data subject to specific regulatory protection (HIPAA-protected health information for organizations subject to HIPAA, regulated financial information, and similar), information shared under specific confidentiality agreements that require this level of protection, security incident details before public disclosure, and pre-public merger or acquisition information.

### 3.4 Handling Public Data

Public data can be shared and distributed without restriction. Specific notes:

Public does not mean unmonitored. Releasing accurate Public information is the goal; releasing inaccurate or out-of-date information can still cause reputational harm. The communications, marketing, or public relations function reviews public-facing content for accuracy through their own processes.

Public data does not require encryption in transit or at rest. Standard storage and transmission methods are acceptable.

Public data is not exempt from copyright, attribution, and other legal obligations. Information is Public from the perspective of confidentiality, not from the perspective of all legal protections.

### 3.5 Handling Confidential Data

Confidential data is the most common classification and the place where most operational care is needed.

**Storage.** Confidential data is stored only in approved systems. Approved storage at [ORGANIZATION_NAME] includes [APPROVED_STORAGE_PLATFORMS, e.g., the file storage and collaboration services of the approved productivity platform, approved file servers, and approved SaaS applications]. Confidential data is not stored in personal cloud accounts, personal email, personal devices outside the approved access mechanisms, or unapproved SaaS tools.

**Transmission.** Confidential data is transmitted using channels with encryption in transit. Email between major email providers is usually encrypted in transit with opportunistic TLS, which is sufficient for most Confidential transmission. Opportunistic TLS is not guaranteed: a receiving server that does not support it, or an attacker who strips it, results in an unencrypted delivery. Where a recipient regularly receives Confidential data, enforced TLS for that domain (through a forced-TLS connector or the recipient's MTA-STS policy) closes the gap. Otherwise, use a secure file sharing tool.

**Access.** Confidential data is accessible only to people with a legitimate business need. Sharing follows the access control principles in POL-IAM-001. Sharing externally requires an awareness of who the recipient is and what they will do with the information.

**Sharing externally.** Confidential data is shared with external parties (vendors, partners, clients) only when there is a business reason and ideally a confidentiality agreement in place. Specific kinds of sharing (sharing customer data with a vendor, sharing employee data with a service provider, sharing strategic information with a partner) follow the third-party risk management process.

**Disposal.** Confidential data is disposed of through deletion processes that are appropriate to the storage system. Files in approved storage systems can be deleted normally; the storage platforms handle the underlying secure deletion. Physical documents containing Confidential data are shredded.

### 3.6 Handling Restricted Data

Restricted data has additional requirements beyond what applies to Confidential data.

**Storage.** Restricted data is stored only in systems approved specifically for this classification. The approved systems vary by data type:

Authentication credentials live in the approved secrets management platforms described in STD-IAM-001 and POL-IAM-003. They do not live anywhere else.

Payment card data, where the organization handles it, lives in PCI-compliant payment processing systems. [ORGANIZATION_NAME]'s payment handling approach is documented in [PAYMENT_HANDLING_PROCESS].

Other Restricted data lives in systems that have been specifically approved for the data type. The Information Security function maintains the list of approved systems for each Restricted data category.

**Transmission.** Restricted data is encrypted in transit using strong, current encryption (TLS 1.2 or later for network transmission, modern encryption tools for file transmission). Email is generally not appropriate for Restricted data; secure file sharing or encrypted document tools are used instead.

**Access.** Access to Restricted data is granted to the smallest number of people necessary. Access reviews for Restricted data occur at least quarterly, more frequently for the most sensitive categories.

**Logging.** Access to Restricted data is logged where the storage system supports it. Logs are retained per the STD-LOG-001 retention requirements.

**Sharing externally.** Restricted data is shared externally only when there is a documented business reason, a confidentiality agreement is in place, and the receiving party has appropriate protections. Sharing Restricted data with a vendor that has not gone through security review is not permitted.

**Disposal.** Restricted data is disposed of through deletion processes that meet the standard appropriate to the data type. For digital data, this typically means cryptographic deletion or overwrite. For physical media, this means shredding for paper and physical destruction or certified wipe for storage media.

### 3.7 Data Owners

Each significant body of [ORGANIZATION_NAME] data has a named owner. The owner is a department lead, business unit head, or other accountable person responsible for the data's purpose and the rules governing its use.

The data owner is distinguished from the system owner. The system owner runs the technical platform; the data owner is responsible for the data itself. The same person can hold both roles, but they are different responsibilities.

Data owners:

Confirm or assign the classification of data in their domain. Approve who has access to the data. Approve external sharing of the data. Determine retention and disposal requirements within applicable legal and regulatory constraints. Communicate handling requirements to people who use the data. Record where Confidential and Restricted data in their domain is stored, including file servers, shared drives, and other on-premises locations as well as SaaS applications, and review that record annually.

The records kept by data owners, together with the classification recorded for each SaaS application under STD-AM-001 Section 3.1, form [ORGANIZATION_NAME]'s data inventory.

When a data owner leaves [ORGANIZATION_NAME] or changes roles, data ownership is reassigned within thirty days.

### 3.8 Classification Marking

Data is marked with its classification where the storage system supports marking. For documents in Microsoft 365 or Google Workspace, sensitivity labels are used to mark Confidential and Restricted data. The labels both communicate the classification to readers and trigger automatic handling controls (encryption, sharing restrictions, watermarks).

Data without marking is treated as Confidential per the default rule in Section 3.2.

Marking is helpful but not the only way classification is determined. The content of the data, the source of the data, and the context of the data all inform classification regardless of whether the marking is present. Removing or changing a classification marking does not change the underlying classification of the data.

### 3.9 Special Categories

Some data categories warrant specific mention because they are commonly mishandled.

**Personal data subject to privacy regulations.** Some jurisdictions and industries impose specific requirements on the handling of personal information beyond what general data classification provides. [ORGANIZATION_NAME] complies with applicable privacy regulations through specific procedures that supplement this policy. Where privacy regulations apply, the regulatory requirements are followed even when they are stricter than this policy.

**Data received from clients or third parties.** Data that [ORGANIZATION_NAME] receives from clients or third parties is classified at the level required by any applicable contract or, in the absence of a contract requirement, at the same level [ORGANIZATION_NAME] would apply to its own data of the same type. When in doubt, the data is treated as Confidential at minimum.

**AI tool inputs.** When employees use generative AI tools, the data they paste into the tool's input is treated as if it were stored in the tool. Confidential data goes only into approved AI tools (per POL-AUP-001 Section 3.6). Restricted data is not pasted into AI tools, including approved ones, unless the specific tool has been reviewed and approved for that purpose.

**Data backups and copies.** Backups of data carry the same classification as the original. A backup of Confidential data is Confidential. A backup of Restricted data is Restricted. Backup storage and access controls reflect the classification of the data being backed up. STD-DR-001 sets the backup and recovery requirements.

### 3.10 Exceptions

Specific situations may warrant deviation from the standard handling rules. The exception process documents the deviation, the business reason, the compensating control, and an end date.

Common situations:

A specific business workflow requires storing Restricted data temporarily in a system that is not on the approved list. The exception specifies the system, the duration, and the controls in place during the exception window.

A vendor relationship requires sharing data with limited contractual protection. The exception documents the residual risk and the offsetting controls.

A legacy system handles Confidential data without meeting current handling standards. The exception specifies the migration timeline and any compensating controls during the migration.

Exceptions follow the same process described in POL-IAM-001 Section 3.10. No exception runs longer than twelve months without renewal. All active exceptions are reviewed quarterly.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Maintains the lists of approved storage systems for each classification. Approves exceptions. Reviews classification disputes.

**Legal and Compliance function (or external counsel).** Advises on regulatory requirements that apply to specific data categories. Reviews handling rules where regulatory requirements supplement this policy.

**Data owners.** Confirm or assign classification for data in their domain. Approve access and sharing decisions. Communicate handling requirements to their teams.

**IT function (or IT service provider).** Implements the technical controls that support classification (sensitivity labels, encryption tools, access controls, secure file sharing). Maintains the secrets management platform.

**All employees and contractors.** Recognize the classification of data they handle. Apply the handling rules appropriate to the classification. Mark data with classification labels where the system supports marking. Report suspected misclassification or mishandling.

## 5. Enforcement

Violations of this policy may result in remediation action proportional to the violation, including:

Mandatory retraining. Loss of access to specific systems or data. For serious or repeated violations, formal disciplinary action consistent with HR policies. For violations that involve illegal activity or breach of regulatory requirements, referral to law enforcement or regulatory authorities as appropriate.

Specific situations:

Confidential data stored in unapproved systems: moved to approved storage within thirty days.

Restricted data stored in unapproved systems: moved to approved storage within seven days. The original storage is sanitized.

Confidential data shared externally without authorization: reviewed for impact, recovery actions where possible, retraining for the involved party.

Restricted data shared externally without authorization: treated as a security incident under the incident response process.

Honest mistakes reported promptly are handled differently from deliberate violations. The intent is to improve handling practice, not to punish lapses.

## 6. Related Documents

POL-IAM-001: Access Control Policy
STD-IAM-001: Password and Authentication Standard
POL-IAM-003: Non-Human Identity Governance Policy
POL-AUP-001: Acceptable Use Policy
POL-AM-001: Asset Management Policy
POL-IR-001: Incident Response Policy
STD-LOG-001: Logging and Monitoring Standard (retention requirements)
POL-TPRM-001: Third-Party Risk Management Policy (vendor data sharing)
POL-AI-001: AI and Agent Governance Policy (classification rules for AI inputs)
STD-DC-001: Data Loss Prevention Standard (technical enforcement of the handling rules)
STD-DC-002: Cryptography and Key Management Standard (encryption minimums, keys, and certificates)
STD-DR-001: Data Backup and Recovery Standard (backups)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

ID.AM-07 (Inventories of data and corresponding metadata for designated data types are maintained), partially, through the data owner and classification requirements. PR.DS-01 (The confidentiality, integrity, and availability of data-at-rest are protected). PR.DS-02 (The confidentiality, integrity, and availability of data-in-transit are protected). PR.DS-10 (The confidentiality, integrity, and availability of data-in-use are protected), for AI tool inputs under Section 3.9. Backup creation and testing (PR.DS-11) are outside this policy; Section 3.9 sets only the classification of backups.

**CIS Controls v8.1:**

Control 3 Data Protection: Safeguards 3.1 (establish and maintain a data management process), 3.2 (establish and maintain a data inventory), 3.3 (configure data access control lists), 3.4 (enforce data retention), 3.5 (securely dispose of data), 3.7 (establish and maintain a data classification scheme), 3.10 (encrypt sensitive data in transit), 3.11 (encrypt sensitive data at rest).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
