# TPL-GOV-002: Exception Register

| | |
|---|---|
| **Document ID** | TPL-GOV-002 |
| **Version** | 1.0 |
| **Supports** | POL-GOV-001 Section 3.6, and the exception sections of every policy and standard in the suite |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

This register records every approved exception to a policy or standard in the suite. One register serves the whole suite, so the Information Security function and the executive sponsor can see all deviations in one place.

Section 1 is the request form. The requester completes it and sends it to the Information Security function. Section 2 is the register itself, where approved exceptions are recorded. Section 3 records emergency exceptions logged after the fact. Section 4 records the quarterly review.

Every exception has an expiration date no more than twelve months after approval. An expired exception is not automatically renewed; if it is still needed, it goes through the request process again.

Watch the register as a whole, not just individual entries. If the same requirement keeps generating exceptions, the requirement is probably wrong for the environment and should be revised at the next policy review (POL-GOV-001 Section 3.6).

---

## 1. Exception Request Form

| Field | Response |
|---|---|
| **Requester** | |
| **Date requested** | |
| **Policy or standard affected** | e.g., POL-EP-001 |
| **Section and requirement** | e.g., Section 3.2, EDR on every endpoint |
| **Systems, data, or people affected** | |
| **Reason the requirement cannot be met** | |
| **Business impact if the exception is denied** | |
| **Proposed duration** | Maximum twelve months |
| **Compensating controls** | What reduces the risk while the requirement is not met |
| **Plan to end the exception** | What would allow the requirement to be met, and when |

**For the Information Security function:**

| Field | Response |
|---|---|
| **Residual risk rating** | Low / Medium / High / Critical (using TPL-GOV-001 Section 1) |
| **Within risk appetite?** | Yes / No |
| **Approval authority** | Information Security function (Low, Medium) or executive sponsor (High, Critical) |
| **Decision** | Approved / Approved with conditions / Declined |
| **Conditions** | |
| **Approved by** | |
| **Approval date** | |
| **Expiration date** | |
| **Exception ID assigned** | |

---

## 2. Exception Register

| Exception ID | Policy / standard | Section | Requirement affected | Scope (systems, data, people) | Requester | Reason | Compensating controls | Residual rating | Approved by | Approval date | Expiration date | Plan to end | Linked risk ID | Status | Last reviewed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EX-001 | | | | | | | | | | | | | | | |

**Status values:** Active, Expiring (within thirty days), Expired (needs renewal or closure), Closed (requirement now met), Declined.

**Linked risk ID.** Exceptions rated High or Critical are also recorded in the risk register (TPL-GOV-001), so the risk is visible in quarterly reviews alongside other risks.

---

## 3. Emergency Exceptions

Deviations made before approval because of an immediate operational need (POL-GOV-001 Section 3.6). Each is logged when it occurs and submitted through Section 1 within five business days.

| Date and time | Logged by | Policy / standard | What was done | Why it could not wait | Submitted for approval | Exception ID | Outcome |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

## 4. Quarterly Review

Completed at each quarterly program review.

| Review date | Reviewers | Active exceptions | Expiring next quarter | Expired and unresolved | Closed this quarter | Requirements with repeated exceptions | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

## 5. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
