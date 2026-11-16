# TPL-IAM-001: Quarterly Non-Human Identity Access Review

| | |
|---|---|
| **Document ID** | TPL-IAM-001 |
| **Version** | 1.0 |
| **Supports** | POL-IAM-003 Sections 3.5, 3.6, 3.7, and 3.9; RUN-IAM-001 Section 5; CIS Controls v8.1 Safeguards 5.1, 5.3, 5.5, 6.2 |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

This template is the quarterly access review required by POL-IAM-003 Section 3.9. Use one copy per quarter. The review has four steps, each with its own section.

**Step 1: refresh the inventory.** Run the quarterly reconciliation in RUN-IAM-001 Section 5 and record what changed since last quarter in Section 2. The review works from the refreshed inventory, not last quarter's.

**Step 2: owners review their identities.** Copy every in-scope identity from the inventory into Section 3. Each named owner completes the five confirmations for each identity they own and records an outcome. Most owners have a handful of identities, and the review takes under an hour.

**Step 3: log and track what failed.** Every identity with an outcome of Fix or Remove gets a row in the findings log in Section 4, with a due date no more than thirty days out.

**Step 4: summarize and sign off.** Complete Section 5 and send it to the Information Security function. The summary is the evidence that the control ran.

AI connectors and agent identities recorded in TPL-AI-001 are non-human identities and are reviewed here, in the same cycle, by the same owners. Review each identity once.

**Deadlines that run automatically.** Under POL-IAM-003 Section 3.9, an identity whose review is not completed within thirty days of the scheduled date is disabled until the review is done. Under Section 3.1, an identity with no current owner is disabled until an owner is assigned. Record both in Section 5.

**Dates** use ISO format (YYYY-MM-DD).

---

## 1. Review Details

| | |
|---|---|
| **Quarter** | [QUARTER_YEAR] |
| **Inventory refreshed (RUN-IAM-001 run date)** | |
| **Review opened** | |
| **Owner responses due** | |
| **Review closed** | |
| **Coordinated by** | |

---

## 2. Changes Since Last Quarter

From the RUN-IAM-001 reconciliation. Each change either matches an approved request or is investigated.

| Change ID | NHI ID | Change type (Added / Removed / Permission change / Credential change / Owner change) | Matches an approved request | Request or ticket reference | Investigation notes | Resolved |
|---|---|---|---|---|---|---|
| C-001 | | | Yes / No | | | Yes / No |

An identity added without a provisioning request, or a permission added without an approved change, is a finding in Section 4 even if the owner confirms it is needed. The process failure is what gets fixed.

---

## 3. Review Worksheet

One row per identity. Columns A through J come from the inventory; the owner completes columns K through Q.

**Rotation due** follows POL-IAM-003 Section 3.5: ninety days for high-privilege credentials, one year for standard credentials, and not applicable for managed identities and other credentials the platform rotates.

**Dormancy status** follows POL-IAM-003 Section 3.7, based on days since last activity: Active (under 90), Flag (90 to 179), Disable (180 to 364), Delete (365 or more).

| NHI ID (A) | Identity name (B) | Platform (C) | Type (D) | Named owner (E) | Documented purpose (F) | Access and privilege level (G) | Authentication method (H) | Last credential rotation (I) | Last activity (J) | Rotation due (K) | Dormancy status (L) | Still needed for its purpose (M) | Owner still correct (N) | Access is the minimum needed (O) | Authentication meets STD-IAM-001 Section 3.7 (P) | Activity matches purpose (Q) | Outcome (Pass / Fix / Remove) | Action required | Reviewed by | Review date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [NHI_ID] | | | | | | | | | | | | Yes / No | Yes / No | Yes / No | Yes / No | Yes / No | | | | |

**Outcome rules.** Pass requires Yes in columns M through Q, a rotation that is not overdue, and a dormancy status of Active. A No in column M, or a dormancy status of Delete, means Remove. Anything else means Fix. An owner who answers No in column N names the correct owner in "Action required," and ownership is reassigned within thirty days under POL-IAM-003 Section 3.1.

**Authentication (column P).** STD-IAM-001 Section 3.7 ranks the methods: platform-managed workload identities first, then certificates with automatic rotation, then secrets in the vault rotated on schedule. A stored secret where a managed identity is available for the platform is a Fix, not a Pass.

**Activity (column Q).** Compare the identity's recent sign-ins and actions with its documented purpose: the systems it reached, the times it ran, and the volume. A reporting integration that started writing data, or a nightly job that now runs at noon from a new address, is a No and a candidate for POL-IR-001 if nobody can explain it.

---

## 4. Findings Log

| Finding ID | NHI ID | Finding | Source (Section 2 or 3) | Owner | Due date (thirty days or less) | Status (Open / In progress / Closed / Excepted) | Closed date | Exception reference (TPL-GOV-002) |
|---|---|---|---|---|---|---|---|---|
| F-001 | | | | | | | | |

Findings still open at their due date are escalated to the Information Security function. A finding that cannot be fixed within thirty days goes through the exception process in POL-GOV-001 Section 3.6 rather than staying open.

---

## 5. Quarterly Summary

| Measure | This quarter | Last quarter |
|---|---|---|
| Identities in scope | | |
| Reviews completed on time | | |
| Review completion rate | | |
| Outcome: Pass | | |
| Outcome: Fix | | |
| Outcome: Remove | | |
| Identities disabled for overdue review | | |
| Identities disabled for no owner | | |
| Identities flagged dormant (90 days) | | |
| Identities disabled for dormancy (180 days) | | |
| Identities deleted (365 days or removal) | | |
| Credentials past rotation due | | |
| Stored secrets where a managed identity was available | | |
| Unexplained changes from Section 2 | | |
| Open findings carried to next quarter | | |
| Active exceptions | | |

**Sign-off**

| | |
|---|---|
| **Reviewed by (Information Security function)** | |
| **Date** | |
| **Findings carried to the risk register (TPL-GOV-001)** | |
| **Metrics reported in TPL-GOV-004** | Yes / No |

---

## 6. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
