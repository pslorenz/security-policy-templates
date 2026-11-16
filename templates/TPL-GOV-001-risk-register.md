# TPL-GOV-001: Risk Register

| | |
|---|---|
| **Document ID** | TPL-GOV-001 |
| **Version** | 1.0 |
| **Supports** | POL-GOV-001 Section 3.5 |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

The risk register records the information security risks [ORGANIZATION_NAME] has identified, how each is rated, what the organization has decided to do about it, and who decided. It is reviewed at every quarterly program review under POL-GOV-001 Section 3.3.

Populate it first from the annual risk assessment, then add risks as they surface: from incidents, post-incident reviews, vulnerability findings that cannot be remediated, vendor assessments, and changes to the business. A risk that only exists in someone's head has not been managed.

Write each risk as a sentence with a cause and a consequence: "Because [condition], [threat] could [result], causing [impact]." Vague entries such as "ransomware" or "phishing" cannot be rated or treated consistently.

Rate each risk twice. **Inherent risk** is the rating before considering existing controls. **Residual risk** is the rating after existing controls. Treatment decisions and acceptance authority are based on residual risk.

---

## 1. Rating Method

### 1.1 Likelihood

| Score | Rating | Description |
|---|---|---|
| 1 | Rare | Not expected to occur in the next three years |
| 2 | Unlikely | Could occur in the next three years |
| 3 | Possible | Could occur in the next year |
| 4 | Likely | Expected to occur in the next year |
| 5 | Almost certain | Occurring now or expected within months |

### 1.2 Impact

| Score | Rating | Description |
|---|---|---|
| 1 | Minimal | Negligible disruption or cost; no external visibility |
| 2 | Minor | Short disruption to a non-critical function; limited cost; no notification obligation |
| 3 | Moderate | Disruption to a critical function for up to a day; meaningful cost; possible notification to a small number of parties |
| 4 | Major | Disruption to critical functions for several days; significant cost; regulatory or client notification likely |
| 5 | Severe | Prolonged disruption threatening business viability; major regulatory, legal, or reputational consequences |

Tailor the impact descriptions to [ORGANIZATION_NAME], for example by stating dollar thresholds: Minor under [AMOUNT], Moderate under [AMOUNT], and so on.

### 1.3 Risk Rating

Find the rating where the likelihood column meets the impact row. Do not multiply the scores. Likelihood and impact are ordinal scales, and multiplying them treats a rare event that would end the business the same as a near-certain nuisance. The matrix weights impact more heavily than likelihood, so a risk rated Severe never falls below High and a risk rated Major never falls below Medium.

| Impact \ Likelihood | 1 Rare | 2 Unlikely | 3 Possible | 4 Likely | 5 Almost certain |
|---|---|---|---|---|---|
| **5 Severe** | High | High | Critical | Critical | Critical |
| **4 Major** | Medium | High | High | Critical | Critical |
| **3 Moderate** | Low | Medium | Medium | High | High |
| **2 Minor** | Low | Low | Medium | Medium | High |
| **1 Minimal** | Low | Low | Low | Medium | Medium |

| Rating | Who can accept (POL-GOV-001 Section 3.5) |
|---|---|
| Low | Information Security function |
| Medium | Information Security function |
| High | Executive sponsor only |
| Critical | Executive sponsor only |

Within a rating, sort risks by impact first and likelihood second when deciding what to treat first.

### 1.4 Risk Appetite

Record the executive sponsor's current risk appetite statement here so treatment decisions can be checked against it.

| | |
|---|---|
| **Risk appetite statement** | [RISK_APPETITE_STATEMENT, e.g., "[ORGANIZATION_NAME] does not accept residual risks rated Critical. High residual risks are accepted only with a funded treatment plan and an expiration date."] |
| **Approved by** | [EXECUTIVE_SPONSOR] |
| **Approved date** | |
| **Next review** | |

---

## 2. Register

| Risk ID | Date identified | Risk statement | Category | Source | Risk owner | Existing controls | Inherent L | Inherent I | Inherent rating | Residual L | Residual I | Residual rating | Treatment | Treatment plan | Target date | Accepted by | Acceptance date | Acceptance expires | Status | Last reviewed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-001 | | Because [condition], [threat] could [result], causing [impact]. | | | | | | | | | | | | | | | | | | |

**Column guidance:**

**Category.** Identity, endpoint, data, third party, operational, physical, people, compliance, or other. **Source.** Where the risk came from: annual assessment, incident (with ID), vulnerability (with ID), vendor assessment, or change. **Treatment.** Mitigate, Transfer, Avoid, or Accept. **Treatment plan.** For Mitigate, the specific actions and owner. For Transfer, the insurance policy or contract. For Avoid, the activity being changed or stopped. For Accept, the reasoning. **Accepted by / expires.** Required when Treatment is Accept. Acceptance expires no more than twelve months after the acceptance date. **Status.** Open, In treatment, Accepted, or Closed.

---

## 3. Closed Risks

Move risks here when they are fully treated, no longer apply, or the asset is retired. Keep them for at least one year so the history is available to auditors.

| Risk ID | Risk statement | Closed date | Reason closed | Closed by |
|---|---|---|---|---|
| | | | | |

---

## 4. Quarterly Review Log

| Review date | Reviewers | Risks added | Risks closed | Ratings changed | Acceptances expiring next quarter | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |

---

## 5. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
