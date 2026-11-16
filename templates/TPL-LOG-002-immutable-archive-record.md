# TPL-LOG-002: Immutable Archive Configuration Record

| | |
|---|---|
| **Document ID** | TPL-LOG-002 |
| **Version** | 1.0 |
| **Supports** | STD-LOG-001 Section 3.7 |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

This record documents the optional immutable archive for Microsoft cloud logs described in STD-LOG-001 Section 3.7. It serves three purposes: it is the build sheet for the IT function, the approval record for locking the immutability policy, and the evidence that the archive exists and works.

Complete Sections 1 through 5 while building the archive. Complete Section 6 during the validation period. Do not lock the immutability policy until every item in Section 6 is complete and Section 7 is signed. Locking is irreversible: a locked policy can be extended but never shortened or removed, and the storage account cannot be deleted while it holds protected data.

A note on container timing: diagnostic settings create their containers automatically on first log delivery (for example, `insights-logs-signinlogs`, `insights-logs-auditlogs`, and `insights-activity-logs`). A container-level immutability policy can only be applied once the container exists. Either wait for the first delivery and then apply container-level policies to each container, or configure an account-level default immutability policy that applies to new containers. An account-level default requires version-level immutability support on the account, which in turn requires blob versioning; confirm append delivery under that model during validation. Record the approach in Section 3.

---

## 1. Storage Account

| Setting | Value | Requirement (STD-LOG-001 Section 3.7) |
|---|---|---|
| Tenant | [TENANT_NAME / ID] | |
| Subscription | | Separate from production workloads where possible |
| Resource group | | Separate from production workloads |
| Storage account name | | |
| Account kind | General-purpose v2 | Required |
| Region | | Same region as regional monitored resources |
| Redundancy | [LRS / ZRS / GRS / GZRS] | Organization's choice; GRS or GZRS adds regional protection |
| Dedicated to log archiving | Yes | No other data in this account |
| Resource lock (CanNotDelete) | | Required |
| Shared key access | [Disabled / Enabled, with reason] | Disabled where delivery path supports it |
| Firewall | [Disabled / Enabled] | |
| Trusted Microsoft services allowed | | Required if firewall is enabled |
| Created by | | |
| Created date | | |

---

## 2. Log Sources Sent to the Archive

One row per diagnostic setting or export path. The archive is a second destination; each source must also reach the central logging platform.

| Source | Diagnostic setting or export name | Log categories | Container | First delivery verified | Verified by | Immutable-storage compatibility confirmed |
|---|---|---|---|---|---|---|
| Microsoft Entra ID | | SignInLogs, NonInteractiveUserSignInLogs, ServicePrincipalSignInLogs, ManagedIdentitySignInLogs | insights-logs-signinlogs, insights-logs-noninteractiveusersigninlogs, insights-logs-serviceprincipalsigninlogs, insights-logs-managedidentitysigninlogs | | | Yes (diagnostic settings) |
| Microsoft Entra ID | | AuditLogs | insights-logs-auditlogs | | | Yes (diagnostic settings) |
| Azure Activity log | | Administrative, Security, Policy | insights-activity-logs | | | Yes (diagnostic settings) |
| [OPTIONAL: Unified audit log] | | | | | | [Confirm before relying on this path] |
| [OPTIONAL: Defender XDR] | | | | | | [Confirm before relying on this path] |

Container names are as created by the service on first delivery; record the actual names observed.

---

## 3. Immutability Policy

| Setting | Value | Requirement |
|---|---|---|
| Policy scope | [Container-level / Account-level default] | |
| Retention period (days) | | At least STD-LOG-001 Section 3.5 total retention (365 by default) |
| Allow protected append writes | Enabled | Required; diagnostic settings write append blobs |
| Policy created date | | |
| Policy created by | | |
| Policy state | [Unlocked / Locked] | Unlocked until Section 7 is signed |
| Locked date | | |
| Locked by | | |

If container-level policies are used, record each container:

| Container | Policy applied date | Retention (days) | Protected append writes | State | Locked date |
|---|---|---|---|---|---|
| | | | | | |

---

## 4. Lifecycle Management

Diagnostic settings do not apply retention to logs sent to storage. A lifecycle rule removes blobs after the retention period.

| Setting | Value |
|---|---|
| Rule name | |
| Scope (containers or prefix) | |
| Delete blobs after (days since last modification) | [Retention period + buffer, e.g., 370] |
| Rule created date | |
| Rule created by | |

Set the deletion age at or after the immutability retention period. Deletion attempts before the period expires fail; they do not remove data.

---

## 5. Access Control

No user or application identity holds a data-plane write or delete role; log delivery is the only writer. Owner and Contributor assignments are limited to named administrators, because those roles can retrieve account keys while shared key access is enabled. Read access is limited to named individuals.

| Principal | Type (user, group, service) | Role | Scope | Justification | Granted date | Granted by |
|---|---|---|---|---|---|---|
| | | | | | | |

Access is reviewed at each annual review (Section 9) and under POL-IAM-001 access review cadences.

---

## 6. Validation Checklist (Before Locking)

Complete during the validation period of [VALIDATION_PERIOD, e.g., seven days].

| Check | Result | Date | Checked by |
|---|---|---|---|
| Every source in Section 2 has delivered logs to the archive | | | |
| Logs continue to arrive daily across the full validation period | | | |
| No delivery errors reported for diagnostic settings | | | |
| Each source also reaches the central logging platform | | | |
| A sample blob can be read by an authorized reader | | | |
| An attempt to delete a test blob fails as expected | | | |
| Protected append writes confirmed enabled on every policy | | | |
| Retention period matches STD-LOG-001 Section 3.5 | | | |
| Lifecycle rule is in place and scoped correctly | | | |
| Resource lock is in place | | | |
| Estimated monthly storage cost calculated | | | |

---

## 7. Approval to Lock

Locking the immutability policy is irreversible. Both approvals are required before locking.

| | |
|---|---|
| **Estimated monthly storage cost** | |
| **Estimated total cost over retention period** | |
| **Information Security function approval** | Name: ______ Date: ______ |
| **Executive sponsor cost approval** | Name: ______ Date: ______ |

---

## 8. Legal Holds

Applied when an incident under POL-IR-001 requires preservation beyond the standard retention period. Remove a hold only when legal counsel confirms it is no longer required.

| Hold tag | Containers | Incident ID | Applied date | Applied by | Counsel approval | Removed date | Removal approved by |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

## 9. Annual Verification

Completed at each annual review of STD-LOG-001.

| Review date | Reviewer | All sources still delivering | Policy locked and retention correct | Lifecycle rule correct | Access list reviewed | Resource lock present | Restore test performed | Notes |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

---

## 10. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
