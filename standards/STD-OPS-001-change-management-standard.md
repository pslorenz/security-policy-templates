# STD-OPS-001: Change Management Standard

| | |
|---|---|
| **Document ID** | STD-OPS-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This standard sets how changes to [ORGANIZATION_NAME]'s systems are approved, carried out, and recorded. It exists for two reasons. The first is stability: most outages in small organizations are caused by a change someone made, and a short pause to think about rollback prevents many of them. The second is security: an attacker who gains administrative access makes changes too, and an organization that records its own changes can tell the difference.

The standard is deliberately light. Routine work is pre-approved and only logged. Approval is reserved for the changes that can lock people out, open the network, or weaken a security control. A twenty-person firm can meet it with a shared change log and a second set of eyes on identity and firewall changes; a larger organization uses its ticket system and a short weekly review.

## 2. Scope

This standard applies to changes to:

The identity provider, including conditional access rules, administrator roles, federation settings, and application registrations. Network equipment and firewall rules under POL-NET-001. Servers, cloud platforms, and cloud network configuration. Security tools, including EDR, email filtering, DNS filtering, logging, and backup. The configuration of Critical and Important SaaS applications under STD-AM-001. Software [ORGANIZATION_NAME] develops, where POL-DEV-001 governs code changes and this standard governs deployment to production.

It applies to changes made by staff and by service providers, including the MSP, acting on [ORGANIZATION_NAME]'s systems. Changes to individual user devices made through the device management platform's approved baselines are standard changes under Section 3.1.

## 3. Standard Requirements

### 3.1 Types of Change

Every change falls into one of three types.

**Standard changes** are low-risk, repeatable, and already approved in advance. They need no per-change approval, only a record. The list of standard changes is maintained by the IT function and approved by the Information Security function, and includes: applying security updates within the POL-VM-001 cadences; provisioning and removing user access through the approved process; adding devices to management under existing baselines; and configuration changes inside an approved SaaS or endpoint baseline that do not change the baseline itself. A change that fails or causes an incident is removed from the standard list until it has been reviewed.

**Normal changes** are everything that is not standard or emergency, and in particular any change to: conditional access rules, administrator roles, or federation settings; firewall rules or network segmentation; the configuration of security tools; the backup system; or a Critical or Important system. Normal changes are approved before they are made (Section 3.2).

**Emergency changes** are changes needed to restore a failed service or to contain an active security incident, where waiting for approval would cause more harm than the change. They are made under the standing authority matrix in POL-IR-001 Section 3.5 or by the on-call lead, and recorded afterward (Section 3.4).

### 3.2 Approving Normal Changes

A normal change is approved by the owner of the affected system and by the IT function before it is made. A normal change to a security control, or one that reduces a security setting, is also approved by the Information Security function. The person who approves a change is not the person who makes it, except where [ORGANIZATION_NAME] has only one person able to do either, in which case the Information Security function or the executive sponsor approves.

Approval considers what could go wrong and what the change does to security: whether it widens access, exposes a service, weakens authentication, or disables logging. Higher-risk normal changes are scheduled in [CHANGE_WINDOW, e.g., an agreed after-hours window], and affected users are told in advance.

### 3.3 The Change Record

Every change, of every type, is recorded in [CHANGE_RECORD_SYSTEM, e.g., the IT ticket system or a shared change log]. The record shows:

What is changing and on which systems. Why. Who requested, approved, and carried out the change. When it was made. How it will be rolled back if it fails. How success was checked afterward.

For standard changes, the record can be the ticket or the automated log of the action. Records are retained for at least [CHANGE_RECORD_RETENTION, e.g., two years].

### 3.4 Emergency Changes

An emergency change is recorded within one business day, with the reason it could not wait. The system owner and the IT function review it within five business days and either confirm it, reverse it, or turn it into a normal change with a proper rollback plan. Emergency changes made during a security incident are also captured in the incident's running record under RUN-IR-001 Section 3.1.2.

Frequent emergency changes are a finding. If the same kind of emergency keeps happening, the underlying problem is fixed rather than the process bypassed again.

### 3.5 Changes Made by Service Providers

Service providers, including the MSP, follow this standard for changes to [ORGANIZATION_NAME]'s systems. A provider may use its own change process if it meets Sections 3.1 through 3.4 and [ORGANIZATION_NAME] can see the records for its environment on request. Normal changes made by a provider are still approved by [ORGANIZATION_NAME]'s system owner, not only by the provider.

### 3.6 Checking After the Change

After a normal or emergency change, the person who made it confirms the system works as intended and that the security settings it touched are as expected. A change that fails is rolled back under its plan and recorded as failed, with the reason.

### 3.7 Detecting Unrecorded Changes

STD-LOG-001 alerts on changes to conditional access rules, administrator roles, federation settings, and application credentials. Each month, the Information Security function compares those alerts, and configuration changes visible in the security tools and cloud platforms, with the change records. A change with no record is investigated as a possible security incident until someone accounts for it. A change that was legitimate but unrecorded is a process finding.

### 3.8 Configuration Baselines

The approved baselines in POL-EP-001 Section 3.1, POL-NET-001 Section 3.5, and STD-AM-001 Section 3.5 are themselves changed only through a normal change, so that the baselines remain the reference for what "correct" looks like.

### 3.9 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Approves the standard change list and security-relevant normal changes. Runs the monthly reconciliation in Section 3.7.

**IT function (or IT service provider).** Maintains the standard change list and the change record. Plans, approves, and carries out changes.

**System owners.** Approve normal changes to their systems. Review emergency changes.

**Service providers.** Follow this standard or an equivalent process for changes they make.

## 5. Enforcement

Specific remediation timelines:

Unrecorded change found in reconciliation: investigated within two business days. Emergency change not recorded within one business day: recorded and reviewed as a finding. Normal change made without approval: reviewed with the person who made it and their manager, and reversed if the system owner does not confirm it.

## 6. Related Documents

POL-GOV-001: Information Security Policy (exceptions)
POL-EP-001: Endpoint Protection Policy (endpoint and server baselines)
POL-NET-001: Network Security Policy (network configuration)
STD-AM-001: SaaS Asset Management Standard (SaaS configuration baselines)
POL-VM-001: Vulnerability Management Policy (patching as a standard change)
POL-IR-001: Incident Response Policy (standing authority and incident records)
POL-DEV-001: Secure Development Policy (code changes)
STD-LOG-001: Logging and Monitoring Standard (alerts on configuration changes)
POL-TPRM-001: Third-Party Risk Management Policy (service provider obligations)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

ID.RA-07 (Changes and exceptions are managed, assessed for risk impact, recorded, and tracked). PR.PS-01 (Configuration management practices are established and applied). DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events), through Section 3.7.

**CIS Controls v8.1:**

Control 4 Secure Configuration of Enterprise Assets and Software: Safeguards 4.1 (establish and maintain a secure configuration process) and 4.2 (establish and maintain a secure configuration process for network infrastructure), through Section 3.8.

**Other frameworks:**

SOC 2 CC8.1 (changes to infrastructure, data, software, and procedures are authorized, designed, tested, approved, and implemented). NIST SP 800-171 Revision 2 requirements 3.4.3 (track, review, approve, and log changes), 3.4.4 (analyze the security impact of changes), and 3.4.5 (restrict who can make changes), for organizations using ADD-CMMC-001.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
