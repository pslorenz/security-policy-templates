# TPL-GOV-003: Vendor Inventory and Risk Assessment

| | |
|---|---|
| **Document ID** | TPL-GOV-003 |
| **Version** | 1.0 |
| **Supports** | POL-TPRM-001 Sections 3.1, 3.2, and 3.8; POL-GOV-001 Section 3.9; CIS Controls v8.1 Safeguards 15.1, 15.3, 15.5, 15.6 |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

This template has two parts. Section 1 is the inventory of every service provider with access to [ORGANIZATION_NAME] information or systems. Section 2 is the assessment questionnaire, completed for each provider that meets the assessment threshold.

**Assessment depth.** Every vendor with access to [ORGANIZATION_NAME] information or systems is recorded in the inventory. How much assessment each one gets depends on its tier, below. AI tools are reviewed here under POL-TPRM-001 Section 3.6 and also recorded in TPL-AI-001.

**Tiering.** Each vendor is assigned a tier under POL-TPRM-001 Section 3.1, and the tier sets the depth of review under Sections 3.2 and 3.8:

| Tier | Criteria | Assessment |
|---|---|---|
| Tier 1 | Compromise or failure would cause significant harm: privileged access to [ORGANIZATION_NAME] systems, Restricted data, the identity provider or primary file storage, critical operational services, or the IT or security service provider | Full questionnaire (Section 2) and independent evidence such as a SOC 2 Type II report before onboarding. Published security information reviewed annually, new audit reports reviewed when issued, and diligence refreshed at renewal |
| Tier 2 | Compromise would cause meaningful but contained harm: Confidential data, customer contact information, or non-critical operational services | Published security information and a brief targeted questionnaire (Sections 2.2 and 2.4) before onboarding. Diligence refreshed at renewal and after any public breach |
| Tier 3 | Compromise would cause limited harm: Public data only or no data access, easily replaced | Review of published information for red flags before onboarding. Reviewed again only if scope changes or a breach is reported |

Managed IT and managed security providers are always Tier 1, because they hold administrative access to everything. That includes the MSP delivering this program.

Prefer independent evidence over questionnaire answers where it exists. A current SOC 2 Type II report or ISO 27001 certificate answers many of the questions in Section 2 more reliably than self-attestation. Record what evidence was reviewed and note any exceptions or qualified opinions in the report.

---

## 1. Vendor Inventory

| Vendor ID | Vendor | Service provided | Internal owner | Data handled | Highest data classification | Administrative access | Tier | Contract start | Contract renewal | Security terms in contract | Last assessed | Next assessment | Assessment result | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V-001 | [MSP / IT_SERVICE_PROVIDER] | Managed IT and security | | All | Restricted | Yes | Tier 1 | | | | | | | Active | |
| V-002 | [PRODUCTIVITY_PLATFORM] | Email, files, identity | | Email, files, identities | [CLASSIFICATION] | Platform | Tier 1 | | | | | | | Active | |
| V-003 | [BACKUP_VENDOR] | Backup and recovery | | Copies of all backed-up data | [CLASSIFICATION] | | Tier 1 | | | | | | | Active | |
| V-004 | | | | | | | | | | | | | | | |

**Column guidance:** **Security terms in contract** records whether the contract includes the terms required by POL-GOV-001 Section 3.9: security requirements, incident notification, the right to request evidence of controls, and data return or destruction at termination (Yes, Partial, or No). **Assessment result** is Acceptable, Acceptable with conditions, or Not acceptable. **Status** is Active, Onboarding, Offboarding, or Terminated.

For large providers such as Microsoft, Google, or AWS, a full questionnaire is rarely practical or answered. Review their published compliance reports (for example, through the Microsoft Service Trust Portal) and record the evidence reviewed in Section 2.6.

---

## 2. Vendor Risk Assessment

Complete one copy of this section per assessed vendor.

### 2.1 Assessment Details

| Field | Response |
|---|---|
| **Vendor** | |
| **Vendor ID** | |
| **Tier** | |
| **Assessment type** | Pre-onboarding / Annual / Contract renewal / Triggered by incident |
| **Assessed by** | |
| **Assessment date** | |
| **Vendor contact** | |

### 2.2 Data and Access

| Question | Response |
|---|---|
| What [ORGANIZATION_NAME] data will the vendor store, process, or access? | |
| What is the highest classification of that data? | |
| Where is the data stored (countries and hosting providers)? | |
| What access does the vendor have to [ORGANIZATION_NAME] systems? | |
| How is that access granted, and can [ORGANIZATION_NAME] see and revoke it? | |
| Does the vendor use subcontractors that will access [ORGANIZATION_NAME] data? Which ones? | |
| Will the vendor notify [ORGANIZATION_NAME] before adding or changing subcontractors that access its data? | |
| Does the vendor use [ORGANIZATION_NAME] data to train or improve AI models, or send it to third-party AI services? Can [ORGANIZATION_NAME] opt out? | |

### 2.3 Security Controls

| Question | Response | Evidence |
|---|---|---|
| Does the vendor require MFA for all staff access to systems holding customer data? Is it phishing-resistant for administrators? | | |
| Is the vendor's access to [ORGANIZATION_NAME] systems through named individual accounts scoped to least privilege (for Microsoft 365, granular delegated admin privileges rather than shared or tenant-wide admin accounts)? | | |
| Is customer data encrypted in transit and at rest? | | |
| Does the vendor run EDR on its endpoints and servers? | | |
| What is the vendor's patching timeline for critical vulnerabilities? | | |
| Does the vendor centralize and retain security logs? For how long? | | |
| Does the vendor perform background checks on staff with access to customer data? | | |
| Does the vendor provide security awareness training to staff? | | |
| Does the vendor conduct penetration testing at least annually? | | |
| Does the vendor maintain backups of customer data, and test restores? | | |
| How is customer data segregated from other customers' data? | | |

### 2.4 Incident Response

| Question | Response |
|---|---|
| Does the vendor have a documented incident response plan? | |
| Within what timeframe will the vendor notify [ORGANIZATION_NAME] of an incident affecting its data or services? | |
| Has the vendor had a security incident affecting customer data in the past three years? What happened? | |
| Will the vendor provide logs and cooperate with [ORGANIZATION_NAME]'s investigation? | |

### 2.5 Contract and Exit

| Question | Response |
|---|---|
| Does the contract include security requirements? | |
| Does the contract include incident notification obligations with a defined timeframe? | |
| Does the contract allow [ORGANIZATION_NAME] to request evidence of security controls? | |
| Does the contract require return or certified destruction of data at termination? | |
| Does the vendor carry cyber liability insurance? Limit: | |
| How would [ORGANIZATION_NAME] exit this vendor, and how long would it take? | |

### 2.6 Independent Evidence Reviewed

| Evidence | Period covered | Reviewed date | Findings, exceptions, or qualifications |
|---|---|---|---|
| e.g., SOC 2 Type II report | | | |
| e.g., ISO 27001 certificate | | | |
| e.g., penetration test summary | | | |

### 2.7 Result

| Field | Response |
|---|---|
| **Residual risk rating** | Low / Medium / High / Critical (using TPL-GOV-001 Section 1) |
| **Result** | Acceptable / Acceptable with conditions / Not acceptable |
| **Conditions or required remediation** | |
| **Risk register entry** | Risk ID if High or Critical |
| **Approved by** | Information Security function (Low, Medium) or executive sponsor (High, Critical) |
| **Approval date** | |
| **Next assessment due** | |

---

## 3. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
