# TPL-LOG-001: Log Source Inventory

| | |
|---|---|
| **Document ID** | TPL-LOG-001 |
| **Version** | 1.0 |
| **Supports** | STD-LOG-001 Sections 3.1, 3.3, 3.5, 3.6, 3.10 |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

This inventory records every security log source in scope of STD-LOG-001, where its logs go, how long they are kept, and whether collection is working. It is the evidence an auditor or insurer asks for when they ask "what do you log, and for how long?"

Start with the pre-filled rows in Section 2, which cover the required sources for a typical Microsoft 365 environment. Delete rows for systems [ORGANIZATION_NAME] does not have, mark them "Not present," and add rows for anything else in scope. Update the inventory whenever a system is added or retired under POL-AM-001.

Record the native retention for each source. It is the number that shows why export matters: a source with thirty days of native retention and no export to the central platform is a gap, even if logging is "on."

Section 3 is completed monthly during the log source health review. Section 4 is completed at each annual review.

**Column definitions:**

**ID.** A short identifier for the source (LS-01, LS-02, and so on). **Source.** The system or service generating logs. **Log type.** The specific log or category collected. **Tier.** Required or Recommended under STD-LOG-001 Section 3.1. **System owner.** The person or team responsible for the source system. **Collection method.** How logs reach the central platform (native connector, diagnostic settings, agent, syslog, API). **Native retention.** How long the source keeps logs itself. **Central platform.** Yes if forwarded to [CENTRAL_LOGGING_PLATFORM]. **Latency.** Measured delay from event to central platform; the target is fifteen minutes or less. **Searchable / total retention.** Retention in the central platform and archive; the minimums are ninety days and one year for required sources. **Immutable archive.** Yes if also sent to the archive in STD-LOG-001 Section 3.7. **Silence alert.** Yes if the central platform alerts when the source stops reporting. **Status.** Collecting, Partial, Not collecting, Not present, or Exception. **Last verified.** Date collection was last confirmed working.

---

## 1. Inventory Summary

| | |
|---|---|
| **Central logging platform** | [CENTRAL_LOGGING_PLATFORM] |
| **Monitoring provider** | [MONITORING_PROVIDER] |
| **Monitoring coverage** | [MONITORING_COVERAGE] |
| **Log time zone** | [LOG_TIME_ZONE] |
| **Immutable archive implemented** | [Yes / No] (if yes, see TPL-LOG-002) |
| **Entra ID licensing** | [Free / P1 / P2] |
| **Inventory last reviewed** | [DATE] |
| **Reviewed by** | [NAME] |

---

## 2. Log Sources

### 2.1 Required Sources

| ID | Source | Log type | Tier | System owner | Collection method | Native retention | Central platform | Latency | Searchable retention | Total retention | Immutable archive | Silence alert | Status | Last verified | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LS-01 | Microsoft Entra ID | Sign-in logs (interactive, non-interactive, service principal, managed identity) | Required | | Diagnostic settings | 7 days (Free) / 30 days (P1/P2) | | | | | | | | | Export requires P1 or P2 |
| LS-02 | Microsoft Entra ID | Audit logs | Required | | Diagnostic settings | 7 days (Free) / 30 days (P1/P2) | | | | | | | | | Export requires P1 or P2 |
| LS-03 | Microsoft 365 | Unified audit log | Required | | Platform connector | 180 days (Audit Standard) | | | | | | | | | Confirm audit logging enabled |
| LS-04 | Microsoft 365 | Mailbox audit | Required | | Included in unified audit log | 180 days (Audit Standard) | | | | | | | | | Confirm mailbox auditing active |
| LS-05 | [EDR_PLATFORM] | Alerts and telemetry | Required | | Platform connector | [VENDOR_RETENTION] | | | | | | | | | |
| LS-06 | [FIREWALL] | Allowed/denied traffic, admin changes | Required | | Syslog | [DEVICE_RETENTION] | | | | | | | | | |
| LS-07 | [VPN_GATEWAY] | Remote access sessions | Required | | Syslog | [DEVICE_RETENTION] | | | | | | | | | Omit if VPN is part of firewall |
| LS-08 | Windows servers | Security event log | Required | | Agent | Local log size | | | | | | | | | |
| LS-09 | Domain controllers | Security event log | Required | | Agent | Local log size | | | | | | | | | Omit if no on-premises AD |
| LS-10 | [BACKUP_PLATFORM] | Job results, retention changes, deletions | Required | | [METHOD] | [VENDOR_RETENTION] | | | | | | | | | |

### 2.2 Recommended Sources

| ID | Source | Log type | Tier | System owner | Collection method | Native retention | Central platform | Latency | Searchable retention | Total retention | Immutable archive | Silence alert | Status | Last verified | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LS-11 | [DNS_SERVICE] | DNS queries | Recommended | | [METHOD] | | | | | | | | | | |
| LS-12 | [WEB_GATEWAY] | URL requests | Recommended | | [METHOD] | | | | | | | | | | |
| LS-13 | Microsoft Azure | Activity log | Recommended | | Diagnostic settings | 90 days | | | | | | | | | Only if Azure subscriptions exist |
| LS-14 | Microsoft Defender XDR | Alerts and incidents | Recommended | | Platform connector | | | | | | | | | | |
| LS-15 | [EMAIL_SECURITY_GATEWAY] | Message and threat logs | Recommended | | [METHOD] | | | | | | | | | | |
| LS-16 | [SAAS_APPLICATION] | Admin audit log | Recommended | | [METHOD] | | | | | | | | | | Add one row per application |
| LS-17 | Windows servers | PowerShell and command-line logging | Recommended | | Agent | Local log size | | | | | | | | | |
| LS-18 | [VM_PLATFORM] | Vulnerability findings | Recommended | | [METHOD] | | | | | | | | | | |
| LS-19 | Microsoft Entra ID | Microsoft Graph activity logs | Recommended | | Diagnostic settings | None (export only) | | | | | | | | | Requires P1 or P2; high volume, size storage before enabling |

### 2.3 Sources Not Collected

Record any in-scope source that is not collected, with the reason and a reference to the exception under POL-GOV-001 Section 3.6.

| ID | Source | Reason not collected | Exception reference | Compensating control | Target date |
|---|---|---|---|---|---|
| | | | | | |

---

## 3. Monthly Log Source Health Review

Completed monthly under STD-LOG-001 Section 3.10. One row per review.

| Review date | Reviewer | Sources collecting | Sources with gaps | Silence alerts triggered | Sources over latency target | Actions raised | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

## 4. Annual Review Checklist

Completed at each annual review of STD-LOG-001.

| Check | Result | Date | Reviewer | Notes |
|---|---|---|---|---|
| All systems added under POL-AM-001 in the past year have a row in Section 2 | | | | |
| Retired systems are removed or marked "Not present" | | | | |
| Microsoft native retention periods rechecked against current documentation | | | | |
| Unified audit logging confirmed enabled for the tenant | | | | |
| Mailbox auditing confirmed active | | | | |
| Entra ID diagnostic settings confirmed exporting sign-in and audit logs | | | | |
| Every required source has a silence alert | | | | |
| Retention in the central platform meets 90 days searchable and 1 year total | | | | |
| A log restore from archive was tested within the restore time | | | | |
| Time synchronization confirmed on servers and network devices | | | | |
| Immutable archive verified (if implemented; see TPL-LOG-002) | | | | |
| Service provider log retention and access terms confirmed (STD-LOG-001 Section 3.11) | | | | |

---

## 5. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
