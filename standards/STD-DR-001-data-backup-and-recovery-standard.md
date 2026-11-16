# STD-DR-001: Data Backup and Recovery Standard

| | |
|---|---|
| **Document ID** | STD-DR-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This standard sets the requirements for backing up [ORGANIZATION_NAME]'s data and systems and for proving that they can be recovered. It brings together backup provisions that were previously spread across POL-DC-001 (the classification of backups), POL-IR-001 (the recovery phase of incident response), and STD-AM-001 (SaaS data), and adds the requirements none of them covered.

Backups are the control that decides how a ransomware incident ends. An organization with clean, recent, tested backups restores and moves on. An organization without them negotiates. Attackers know this, and they look for the backups first: deleting them, encrypting them, or waiting until the retention window has rolled past the point of infection. A backup that shares credentials with the systems it protects is not a backup during a ransomware incident; it is another target.

The test of this standard is whether [ORGANIZATION_NAME] can restore the systems it depends on, within the time the business can tolerate, after an attacker with administrator access has tried to stop it. Successful backup jobs are where that test starts, not where it ends.

## 2. Scope

This standard covers the data and systems [ORGANIZATION_NAME] would need to recover after loss, corruption, or attack, including:

Servers and the data on them, on premises and in cloud platforms. Data in SaaS applications, including the productivity platform, under STD-AM-001 Section 3.8. Endpoint data, which is protected by syncing it to approved storage rather than backing up each device. The configuration of the identity provider, on-premises directory, and conditional access rules. Network equipment configurations, under POL-NET-001 Section 3.5. The secrets vault and the encryption keys needed to read the backups. The documentation, procedures, and contact lists needed to carry out a recovery.

## 3. Standard Requirements

### 3.1 Recovery Objectives

Each system classified Critical or Important under POL-AM-001 Section 3.7 has two documented recovery objectives, set by the business owner with the IT function:

**Recovery point objective (RPO).** How much data, measured in time, the business can afford to lose. An RPO of twenty-four hours means a daily backup is enough.

**Recovery time objective (RTO).** How long the business can operate without the system before the harm becomes unacceptable.

The right objectives depend on the business. A clinic that cannot see patients without its scheduling system may need that system back within hours; a firm that can run on email and phones for a week can live with longer. The starting points below suit many small organizations, but [ORGANIZATION_NAME] may need different timings for some or all of its systems, and the business owners' objectives replace them as soon as they are set:

| Criticality | Recovery point objective | Recovery time objective |
|---|---|---|
| Critical | [CRITICAL_RPO, e.g., 24 hours] | [CRITICAL_RTO, e.g., 72 hours] |
| Important | [IMPORTANT_RPO, e.g., 24 hours] | [IMPORTANT_RTO, e.g., 7 days] |
| Standard | [STANDARD_RPO, e.g., 7 days] | Best effort |

Objectives are recorded with the critical asset documentation in POL-AM-001 Section 3.9 and reviewed annually. An objective that the current backup design cannot meet is either funded or accepted as a risk under POL-GOV-001 Section 3.5. Leadership should not discover the real recovery time during an incident.

Shorter objectives cost more: more frequent backups, faster storage, standby systems. When a business owner asks for an objective shorter than the defaults, the IT function provides the cost of meeting it so the owner can decide with both numbers in front of them.

### 3.2 What Gets Backed Up

**Data.** All Confidential and Restricted data, on a schedule that meets the RPO of the system that holds it.

**Systems that cannot be rebuilt quickly.** Servers whose configuration is not reproducible from documentation or code are backed up as full system images. Systems that can be rebuilt from code or a documented build in less than their RTO may back up data only.

**Identity.** The on-premises directory is backed up with system state from at least two domain controllers, and a documented directory recovery procedure exists, because restoring identity comes before restoring almost everything else. The cloud identity provider's configuration (conditional access rules, application registrations, role assignments) is exported on a schedule, since most identity providers do not offer a point-in-time restore of their configuration.

**SaaS.** Critical SaaS applications follow STD-AM-001 Section 3.8. The productivity platform's mail, files, and collaboration data are backed up by a service independent of the platform's own retention features.

**Endpoints.** User data on laptops and desktops lives in approved synced storage under POL-DC-001 Section 3.5. Endpoints are rebuilt, not restored. Data kept only on a local device is not backed up and is the user's responsibility to move.

**Recovery dependencies.** The secrets vault, backup encryption keys, network configurations, and the recovery procedures in Section 3.8 are backed up or stored where they remain reachable when production systems are not.

### 3.3 Copies and Isolation

Critical and Important data meets these requirements:

At least three copies, including production. At least two different storage types or platforms. At least one copy offsite or in a different cloud region or account. At least one copy that is immutable or offline, meaning it cannot be changed or deleted before its retention period ends, even by an administrator with full access to the backup system.

The immutable or offline copy is the one that matters during ransomware. Immutable storage with a locked retention policy (the same approach STD-LOG-001 uses for logs), backup service features that prevent deletion during the retention period, or media physically disconnected from the network all qualify. A second copy on a network share does not.

### 3.4 Protecting the Backup System

The backup system is treated as a Tier-zero asset, because control of it decides whether recovery is possible.

Backup administration does not depend on the production directory or identity provider. Backup administrator accounts are separate from production administrator accounts, are not members of production domain groups, and do not share passwords with any other account.

Access to the backup console requires phishing-resistant authentication under STD-IAM-001 Section 3.5. Backup servers and storage are on a network segment that production systems cannot reach except through the paths backup traffic requires, under POL-NET-001 Section 3.1.

Where the backup platform supports it, deleting backups, shortening retention, or disabling immutability requires a second approver or a delay period. Backups are encrypted, and the encryption keys are stored separately from the backups and are themselves recoverable. A backup that cannot be decrypted is not a backup.

The backup system's logs go to the central logging platform under STD-LOG-001, and alerts fire on deleted backups, changed retention settings, disabled jobs, and new administrator accounts. Those events are early signs of an attack in progress.

### 3.5 Retention

Backups are retained long enough to restore from a point before an attacker arrived, which is often weeks before anyone noticed. Default retention:

| Backup | Retained for |
|---|---|
| Daily | [DAILY_RETENTION, e.g., 30 days] |
| Weekly | [WEEKLY_RETENTION, e.g., 12 weeks] |
| Monthly | [MONTHLY_RETENTION, e.g., 12 months] |

Retention is extended where the data owner, a regulation, or a contract requires it under POL-DC-001 Section 3.7, and shortened only where a legal obligation requires deletion. Backups keep the classification of the data they hold, under POL-DC-001 Section 3.9.

### 3.6 Monitoring Backups

Backup jobs are monitored daily. A failed job for a Critical or Important system is investigated by the next business day. Two consecutive failures for a Critical system are escalated to the Information Security function.

Each month, the list of systems being backed up is compared with the asset inventory in POL-AM-001 Section 3.2. A Critical or Important system that appears in the inventory but not in the backup configuration is a finding. New systems are the ones most often missed.

### 3.7 Restore Testing

A backup is only known to work once something has been restored from it.

**Quarterly.** A sample of files, mailboxes, or records is restored from each Critical system and checked for completeness. At least one quarterly test each year restores from the immutable or offline copy.

**Annually.** At least one Critical system is recovered end to end into an isolated environment, timed, and compared against its RTO. The test includes the dependencies a real recovery needs: identity, network access, and the application starting and serving data. The system tested rotates each year.

**After major changes.** A restore test follows any change to the backup platform, storage, or encryption.

Each test records the date, the system, the restore point used, the time taken, whether the objective was met, and any problems found. Problems are tracked to closure like any other finding. The ransomware scenario in RUN-IR-002 is a good place to test the decisions around a recovery; the restore test is where the technical steps get proven.

### 3.8 Recovery Procedures

Each Critical system has a written recovery procedure covering:

The restore order and the dependencies that drive it (identity and network before applications). Where the backups are, how to reach them without the production identity provider, and where the encryption keys are. How to build or obtain the clean environment the system will be restored into. How to verify the restored system before reconnecting it. Who performs the recovery and who approves returning it to service.

Procedures are stored with the incident response materials, in a location reachable when company systems are down, consistent with RUN-IR-001 Section 2.1. They are reviewed after each annual recovery test.

### 3.9 Recovery During an Incident

Recovery after an incident follows the recovery phase in POL-IR-001 Section 3.4, with these additional requirements:

The restore point is chosen to predate the attacker's first access, not just the visible damage, using the investigation's timeline. Backups are checked for malware and for the attacker's persistence mechanisms before use. Restored systems are brought up in an isolated environment, scanned, and patched before they are reconnected. Credentials that existed at the time of the compromise are reset, including the backup system's own, before restored systems return to production.

Where the integrity of a restore point cannot be established, systems are rebuilt from known-good installation media and only data is restored.

### 3.10 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6. A Critical system without an immutable or offline copy is a High risk at minimum.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Reviews backup security, alerting, and test results. Approves exceptions.

**IT function (or IT service provider).** Operates the backup system. Monitors jobs, runs restore tests, maintains recovery procedures, and carries out recoveries.

**Business owners.** Set the recovery objectives for their systems. Accept the risk where the current design cannot meet them. Participate in the annual recovery test for their system.

**Executive sponsor.** Funds the backup design needed to meet the agreed objectives, or accepts the risk in writing.

**All users.** Keep company data in approved synced storage rather than only on a local device.

## 5. Enforcement

Specific remediation timelines:

Critical or Important system with no backup: backed up within seven days of discovery. Critical system without an immutable or offline copy: copy in place within thirty days, or an exception approved. Backup administration that depends on the production directory or shares production credentials: separated within thirty days. Restore test missed: completed within thirty days, and escalated to the executive sponsor if missed twice. Backup job failing for more than seven days on a Critical system: escalated to the executive sponsor.

## 6. Related Documents

POL-AM-001: Asset Management Policy (criticality and critical asset documentation)
STD-AM-001: SaaS Asset Management Standard (SaaS data backup)
POL-BC-001: Business Continuity Policy (business functions and maximum tolerable downtime)
POL-DC-001: Data Classification and Handling Policy (classification and retention of backups)
POL-IR-001: Incident Response Policy (the recovery phase)
RUN-IR-001: Incident Response Runbook (ransomware playbook and contact list)
RUN-IR-002: Tabletop Exercise Facilitation Runbook (ransomware recovery decisions)
STD-IAM-001: Password and Authentication Standard (backup console authentication)
POL-NET-001: Network Security Policy (segmentation of backup infrastructure)
STD-LOG-001: Logging and Monitoring Standard (backup system logging and immutable storage pattern)
POL-GOV-001: Information Security Policy (risk acceptance and exceptions)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.DS-11 (Backups of data are created, protected, maintained, and tested). RC.RP-02 (Recovery actions are selected, scoped, prioritized, and performed). RC.RP-03 (The integrity of backups and other restoration assets is verified before using them for restoration). RC.RP-05 (The integrity of restored assets is verified, systems and services are restored, and normal operating status is confirmed). ID.IM-02 (Improvements are identified from security tests and exercises, including those done in coordination with suppliers and relevant third parties). PR.IR-03 (Mechanisms are implemented to achieve resilience requirements in normal and adverse situations).

**CIS Controls v8.1:**

Control 11 Data Recovery: Safeguards 11.1 (establish and maintain a data recovery process), 11.2 (perform automated backups), 11.3 (protect recovery data), 11.4 (establish and maintain an isolated instance of recovery data), 11.5 (test data recovery).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
