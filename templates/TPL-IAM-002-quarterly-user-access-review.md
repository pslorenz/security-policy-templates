# TPL-IAM-002: Quarterly User Access Review

| | |
|---|---|
| **Document ID** | TPL-IAM-002 |
| **Version** | 1.0 |
| **Supports** | POL-IAM-001 Sections 3.1, 3.3, 3.4, 3.5, and 3.8; STD-AM-001 Section 3.7; CIS Controls v8.1 Safeguards 5.1, 5.3, 5.4, 6.1, 6.2 |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

This template is the quarterly access review for people's accounts required by POL-IAM-001 Section 3.3. Its counterpart for non-human identities is TPL-IAM-001; the two run in the same quarter but cover different accounts. Use one copy per quarter. The review has five steps.

**Step 1: reconcile accounts against the roster (Section 2).** Before anyone reviews access, confirm that every account belongs to a current person. This step finds the accounts of people who left, which are the highest-risk finding in most reviews and need no manager judgment to fix.

**Step 2: managers review their people (Section 3).** Each manager confirms, for each person who reports to them, that the person still works here and that their access matches their current job.

**Step 3: system owners review sensitive systems (Section 4).** For systems that hold sensitive data or support critical operations, the system owner confirms who has access and at what level, as POL-IAM-001 Section 3.3 requires.

**Step 4: review privileged, vendor, and guest accounts (Sections 5 and 6).** Privileged access is reviewed monthly under POL-IAM-001 Section 3.5. Use Section 5 for each month's review and attach the three monthly copies to the quarterly record. Vendor and guest accounts are checked for end dates under POL-IAM-001 Section 3.8.

**Step 5: log, fix, and sign off (Sections 7 and 8).** Every Change or Remove outcome gets a row in the findings log. Access that is no longer needed is removed within thirty days under POL-IAM-001 Section 3.3.

**Sources to export before starting:** the current staff roster from HR, including contractors and recent departures; the account list from the identity provider, with last sign-in, MFA methods, and group memberships; administrator role assignments in the identity provider and each Critical system; account lists from applications not provisioned through SCIM (STD-AM-001 Section 3.7); and guest and external accounts.

**Dates** use ISO format (YYYY-MM-DD).

---

## 1. Review Details

| | |
|---|---|
| **Quarter** | [QUARTER_YEAR] |
| **Roster exported (date and source)** | |
| **Identity provider export date** | |
| **Review opened** | |
| **Manager responses due** | |
| **Review closed** | |
| **Coordinated by** | |

---

## 2. Roster Reconciliation

Compare the identity provider's enabled user accounts, and the user lists of applications without SCIM, against the roster. Record every account that does not match a current person.

| Item ID | Account | System | Finding (Departed user still enabled / No matching person / Name or role mismatch / Contractor past end date) | Last sign-in | Action | Done |
|---|---|---|---|---|---|---|
| R-001 | | | | | | Yes / No |

An enabled account belonging to someone who has left is disabled the day it is found and logged as a finding in Section 7, because POL-IAM-001 Section 3.4 requires removal on the last day. The finding is the gap in the departure process, not just the account.

---

## 3. Manager Review

One row per person. Columns A through H come from the exports; the manager completes columns I through L.

**Dormant** means no sign-in for forty-five days. Under POL-IAM-001 Section 3.3, dormant accounts are disabled automatically where the platform supports it; any that are still enabled are listed here.

**MFA method** is checked against STD-IAM-001 Section 3.4: an authenticator app with number matching, TOTP, or a phishing-resistant method for standard accounts. SMS, voice, and email codes do not meet the standard.

| Person (A) | Account (B) | Department and job title (C) | Manager (D) | Access pattern or role (E) | Access beyond the standard pattern (F) | Last sign-in (G) | MFA method (H) | Still employed or engaged (I) | Access matches current job (J) | Additional access still needed and approved (K) | MFA meets STD-IAM-001 (L) | Outcome (Keep / Change / Remove) | Change required | Reviewed by | Review date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | Yes / No | Yes / No | Yes / No / N/A | Yes / No | | | | |

**Outcome rules.** Keep requires Yes in I, J, and L, and Yes or N/A in K. A No in column I means Remove. Anything else means Change, with the change described. A Yes in column K requires the approval record from POL-IAM-001 Section 3.2; access beyond the standard pattern without a recorded approval is a Change even if the manager agrees it is needed.

---

## 4. System Owner Review

For each system that holds sensitive data or supports critical operations. Attach the system's user list.

| System | System owner | Users with access | Users with elevated or administrative access | All users still need access (Yes / No) | Access levels appropriate (Yes / No) | Accounts outside SSO or SCIM checked against roster (Yes / No / N/A) | Changes required | Reviewed by | Review date |
|---|---|---|---|---|---|---|---|---|---|
| [CRITICAL_SYSTEM] | | | | | | | | | |

---

## 5. Privileged Access Review (Monthly)

Complete each month under POL-IAM-001 Section 3.5. Include administrator roles in the identity provider, the productivity platform, cloud platforms, domain administrators, and administrator accounts in Critical applications.

| Month | Account | Person | Role or group | Separate from daily account (Yes / No) | Phishing-resistant authentication (Yes / No) | Standing or just-in-time | Last used | Still needed (Yes / No) | Outcome | Reviewed by |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

A privileged account without phishing-resistant authentication is converted or upgraded within thirty days under POL-IAM-001 Section 5. Standing administrator rights where the platform supports just-in-time elevation are a Change.

Break-glass accounts are listed here too, with confirmation that the credentials are still recoverable and that any use since the last review was alerted on and reviewed under POL-IAM-001 Section 3.7.

---

## 6. Vendor, Contractor, and Guest Accounts

| Account | Organization | Sponsor at [ORGANIZATION_NAME] | Purpose or engagement | End date recorded (Yes / No) | End date | Past end date (Yes / No) | Access is the minimum needed (Yes / No) | Privileged (Yes / No) | Outcome | Reviewed by |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

Accounts without an end date get one or are removed within thirty days under POL-IAM-001 Section 5. Accounts past their end date are disabled when found.

---

## 7. Findings Log

| Finding ID | Account | Finding | Source section | Owner | Due date (thirty days or less) | Status (Open / In progress / Closed / Excepted) | Closed date | Exception reference (TPL-GOV-002) |
|---|---|---|---|---|---|---|---|---|
| UA-001 | | | | | | | | |

Findings open at their due date are escalated to the Information Security function. A finding that cannot be closed within thirty days goes through the exception process in POL-GOV-001 Section 3.6.

---

## 8. Quarterly Summary and Sign-Off

| Measure | This quarter | Last quarter |
|---|---|---|
| Enabled user accounts | | |
| Departed users found still enabled | | |
| Accounts with no matching person | | |
| Dormant accounts still enabled | | |
| Manager reviews completed on time | | |
| Outcome: Keep | | |
| Outcome: Change | | |
| Outcome: Remove | | |
| Access beyond pattern without recorded approval | | |
| Accounts with MFA below the standard | | |
| Privileged accounts | | |
| Privileged accounts without phishing-resistant authentication | | |
| Vendor or guest accounts past end date | | |
| Open findings carried to next quarter | | |

**Sign-off**

| | |
|---|---|
| **Reviewed by (Information Security function)** | |
| **Date** | |
| **Monthly privileged reviews attached (three)** | Yes / No |
| **Findings carried to the risk register (TPL-GOV-001)** | |
| **Metrics reported in TPL-GOV-004** | Yes / No |

---

## 9. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
