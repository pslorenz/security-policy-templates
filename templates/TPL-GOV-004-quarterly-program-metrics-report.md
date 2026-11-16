# TPL-GOV-004: Quarterly Program Metrics Report

| | |
|---|---|
| **Document ID** | TPL-GOV-004 |
| **Version** | 1.0 |
| **Supports** | POL-GOV-001 Sections 3.3 and 3.11; POL-VM-001 Section 3.7; STD-LOG-001 Section 3.10 |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

This report is prepared by the Information Security function for each quarterly program review with the executive sponsor. It is written for a business leader, not an engineer: each section leads with what changed and what it means, and the tables carry the detail.

Report every metric as a trend: last quarter, this quarter, and the target. A single number tells the executive sponsor little. A number moving in the right direction, or the wrong one, tells them whether the program is working.

Report unfavorable metrics as plainly as favorable ones (POL-GOV-001 Section 3.11). Use the status column consistently: **On target**, **Improving** (not at target but moving toward it), **Flat**, or **Declining**.

Not every metric applies to every organization. Delete rows that do not apply, and note why in the first report so the omission is deliberate.

---

## Report Details

| | |
|---|---|
| **Quarter** | [QUARTER_YEAR, e.g., Q1 2027] |
| **Prepared by** | |
| **Prepared date** | |
| **Review meeting date** | |
| **Attendees** | |

---

## 1. Summary

Three to five sentences for the executive sponsor: the overall state of the program, the most important change since last quarter, and the decisions needed from them today.

[SUMMARY]

---

## 2. Decisions Needed

List anything that requires executive sponsor action: risk acceptances for High or Critical risks, exception approvals, budget requests, or policy approvals.

| # | Decision needed | Background | Recommendation | Decision | Decided by |
|---|---|---|---|---|---|
| 1 | | | | | |

---

## 3. Metrics

### 3.1 Identity and Access

| Metric | Last quarter | This quarter | Target | Status |
|---|---|---|---|---|
| User accounts with MFA enforced | | | 100% | |
| Administrative accounts with phishing-resistant MFA | | | 100% | |
| Accounts with administrative roles | | | [TARGET] | |
| Dormant accounts (no sign-in for 90 days) | | | 0 | |

### 3.2 Endpoints

| Metric | Last quarter | This quarter | Target | Status |
|---|---|---|---|---|
| Endpoints with active EDR | | | 100% | |
| Endpoints with disk encryption enabled | | | 100% | |
| Endpoints in baseline configuration | | | [TARGET] | |
| Endpoints on unsupported operating systems | | | 0 | |

### 3.3 Vulnerability Management

| Metric | Last quarter | This quarter | Target | Status |
|---|---|---|---|---|
| Open Critical priority vulnerabilities | | | 0 | |
| Open High priority vulnerabilities | | | [TARGET] | |
| Critical vulnerabilities remediated within POL-VM-001 timeline | | | 100% | |
| Mean time to remediate, Critical (days) | | | 7 or less | |
| Mean time to remediate, High (days) | | | 14 or less | |
| Mean time to remediate, Medium (days) | | | 30 or less | |
| KEV-listed vulnerabilities in the environment, addressed this quarter | | | All | |
| Assets covered by vulnerability discovery tools | | | 100% | |

### 3.4 Logging and Monitoring

| Metric | Last quarter | This quarter | Target | Status |
|---|---|---|---|---|
| Required log sources collecting | | | 100% | |
| Required log sources meeting retention | | | 100% | |
| Silent-source alerts investigated | | | All | |
| Alerts by severity (Critical / High / Medium / Low) | | | n/a | |
| Critical alerts triaged within thirty minutes | | | 100% | |

### 3.5 People

| Metric | Last quarter | This quarter | Target | Status |
|---|---|---|---|---|
| Security awareness training completion | | | 100% | |
| Policy acknowledgments current | | | 100% | |
| Phishing simulation click rate | | | [TARGET] | |
| Phishing simulation report rate | | | [TARGET] | |

Report rate matters more than click rate. A rising report rate means people are recognizing and escalating threats, which is the behavior that limits real incidents.

### 3.6 Incidents

| Metric | Last quarter | This quarter | Notes |
|---|---|---|---|
| Incidents declared, Critical | | | |
| Incidents declared, High | | | |
| Incidents declared, Medium | | | |
| Incidents declared, Low | | | |
| Post-incident reviews completed on time | | | |
| Post-incident review actions open | | | |

Summarize each Critical or High incident in one or two sentences: what happened, impact, and status.

[INCIDENT_SUMMARIES]

### 3.7 Risk, Exceptions, and Vendors

| Metric | Last quarter | This quarter | Target | Status |
|---|---|---|---|---|
| Open risks, High and Critical | | | [TARGET] | |
| Risk acceptances expiring next quarter | | | n/a | |
| Active exceptions | | | [TARGET] | |
| Expired exceptions not yet resolved | | | 0 | |
| Oldest active exception or accepted risk (days) | | | 365 or less | |
| Tier 1 and Tier 2 vendors assessed within twelve months | | | 100% | |

### 3.8 Backup and Recovery

| Metric | Last quarter | This quarter | Target | Status |
|---|---|---|---|---|
| Critical systems with successful backups | | | 100% | |
| Restore tests performed this quarter | | | [TARGET] | |
| Restore tests successful | | | 100% | |

---

## 4. Remediation Progress

Track the actions from risk treatment plans, post-incident reviews, assessments, and tabletop exercises.

| Action | Source | Owner | Target date | Status | Notes |
|---|---|---|---|---|---|
| | | | | | |

---

## 5. Changes Since Last Quarter

Note significant changes to the environment, threats, policies, or service providers that affect the program.

[CHANGES]

---

## 6. Priorities for Next Quarter

| Priority | Owner | Target date |
|---|---|---|
| | | |

---

## 7. Review Record

| | |
|---|---|
| **Decisions recorded in Section 2** | Yes / No |
| **Action items assigned** | |
| **Next review date** | |
| **Executive sponsor acknowledgment** | Name: ______ Date: ______ |

---

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
