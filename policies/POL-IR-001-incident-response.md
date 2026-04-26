# POL-IR-001: Incident Response Policy

| | |
|---|---|
| **Document ID** | POL-IR-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] responds to security incidents. It covers what counts as an incident, who declares one, how the response is run, and what happens afterward.

The goal is not to prevent every possible bad outcome from a security incident. That is not achievable. The goal is to make sure that when something goes wrong, [ORGANIZATION_NAME] responds in a way that limits the damage, restores normal operations, and produces lessons that strengthen the program.

Good incident response depends on two things. The first is preparation: the people, tools, processes, and decisions that exist before anything happens. The second is muscle memory: the team has rehearsed the response often enough that they do not have to invent it under pressure. This policy supports both.

The companion runbook (RUN-IR-001) provides the operational procedures for common incident types. This policy establishes the framework; the runbook is the playbook.

## 2. Scope

This policy applies to all security incidents affecting [ORGANIZATION_NAME] systems, data, people, or operations. Specifically:

Confirmed or suspected unauthorized access to [ORGANIZATION_NAME] systems or data. Compromise of user accounts, service accounts, or other identities. Malware infections, ransomware, or other malicious software activity. Data exposure, loss, or theft. Denial-of-service or significant operational disruption from suspected adversarial activity. Physical security incidents that affect digital systems (theft of devices, unauthorized facility access). Significant policy violations that have potential security impact. Suspected insider threat activity.

It also applies to incidents affecting third-party services [ORGANIZATION_NAME] depends on, where the third party's incident has direct consequences for [ORGANIZATION_NAME] data or operations.

The policy applies to all employees, contractors, vendors, and other parties who detect or are involved in responding to incidents.

## 3. Policy Statements

### 3.1 The Definition of an Incident

A security incident is an event that compromises or threatens to compromise the confidentiality, integrity, or availability of [ORGANIZATION_NAME] systems, data, or operations.

Not every alert is an incident. Most security alerts are events that turn out to be normal activity, false positives, or minor issues handled through routine operations. An incident is what the response team determines an event to be after analysis.

The threshold for declaring an incident is intentionally broad. When in doubt, treat the situation as an incident and follow the process. Incidents that turn out to be non-events get closed quickly. Real incidents that get handled as routine events become much worse.

### 3.2 Severity Classification

Every declared incident is assigned a severity level. The severity drives the response speed, the people activated, and the level of leadership involvement.

**Critical.** Incidents that pose immediate, severe risk to [ORGANIZATION_NAME] operations, data, or stakeholders. Examples include active ransomware encrypting production systems, confirmed compromise of administrative credentials with active adversary activity, confirmed exposure of large volumes of restricted data, and any incident likely to trigger regulatory notification or significant public attention.

Critical incidents activate the full response process within thirty minutes of declaration. The executive sponsor is notified immediately. External support (incident response retainer, legal counsel, cyber insurance) is engaged as appropriate.

**High.** Incidents that pose significant risk but are contained or limited in scope. Examples include compromise of a single user account with potential lateral movement, malware on a single endpoint without confirmed spread, suspicious activity from a non-human identity, and confirmed phishing campaign targeting [ORGANIZATION_NAME] users.

High incidents activate the response process within two hours. The executive sponsor is informed within four hours. External support is engaged if the situation escalates.

**Medium.** Incidents that warrant formal response but are limited in scope and impact. Examples include single confirmed phishing email click without credential compromise, lost device with company data and remote wipe completed, unauthorized access attempt that was blocked by existing controls, and policy violations with potential security impact.

Medium incidents are handled during business hours with response activities completing within twenty-four hours. The executive sponsor receives a summary in the next routine reporting cycle.

**Low.** Events that meet the technical definition of an incident but pose minimal risk. Examples include automated security alerts that turned out to be benign after investigation but warrant documentation, near-miss events that were caught by controls before harm occurred, and confirmed events that fall below the threshold for higher classification.

Low incidents are documented but do not require emergency response activities.

Severity is assigned at declaration and revisited as the response progresses. An incident can be reclassified upward if new information emerges, or downward if initial concerns prove unfounded.

### 3.3 Who Declares an Incident

Any employee or contractor who suspects a security incident reports it. The report goes through the channels documented in POL-AUP-001 Section 3.9 and the companion runbook.

The Information Security function (or the designated security service provider) reviews reports and declares formal incidents. The declaration assigns the initial severity, activates the appropriate response, and starts the incident timeline.

For clearly serious situations (active ransomware, confirmed compromise with active adversary activity), any employee with authority to do so can take immediate protective action (disconnecting a compromised device, blocking an external IP, disabling a compromised account) without waiting for formal declaration. The declaration follows the action; the urgent protective work does not wait for paperwork.

### 3.4 Response Phases

[ORGANIZATION_NAME]'s incident response follows six phases. The phases are not strictly sequential; some run in parallel and the response may move backward to an earlier phase as new information emerges.

**Preparation.** The work that happens before an incident: building the inventory, training the team, establishing communication channels, retaining external partners, running tabletop exercises, and maintaining the tools and documentation the response depends on. This phase is continuous; it does not start when an incident begins.

**Detection and Analysis.** Identifying that something is wrong, gathering enough information to understand what is happening, and determining whether the situation meets the threshold for incident declaration. The output of this phase is a declared incident with assigned severity, or a determination that no incident exists.

**Containment.** Limiting the immediate damage and preventing the situation from getting worse. Containment is often urgent and may require quick decisions with incomplete information. Common containment actions include isolating affected systems, disabling compromised accounts, blocking malicious network traffic, and preserving evidence for later analysis. Containment is not the same as resolution; it buys time for the work that follows.

**Eradication.** Removing the cause of the incident from the environment. Eradication may include removing malware, closing the vulnerability that was exploited, removing attacker access, and rotating compromised credentials. Eradication is complete when the incident's root cause has been addressed and there is reasonable confidence that the adversary or threat is no longer present.

**Recovery.** Returning systems and operations to normal, validated state. Recovery includes restoring services from clean backups where appropriate, monitoring for signs that the threat returns, and verifying that affected systems are functioning correctly. Recovery is complete when [ORGANIZATION_NAME] has confidence that operations are stable and the affected environment is no more vulnerable than before the incident.

**Post-Incident Review.** Examining what happened, what worked well, and what should change. The review produces specific recommendations for improving the security program based on what the incident revealed. This phase is not optional. Incidents that produce no learning produce no improvement.

### 3.5 The Standing Authority Matrix

For incidents that require fast action, [ORGANIZATION_NAME] maintains a standing authority matrix. The matrix documents specific containment actions that the response team is pre-authorized to take, with defined scope and rollback paths.

Pre-authorized actions typically include:

Blocking specific IP addresses at the network edge for a defined window. Isolating a single endpoint from the network through the device management or EDR platform. Disabling a single user account or service account. Revoking specific OAuth tokens or session tokens. Rolling back a recent deployment to a known-good state.

The matrix specifies for each action: the trigger conditions, the scope limit, the named approver, the audit cadence, and the rollback procedure. Actions that cannot be safely scoped and rolled back are not on the matrix; they remain in the human-decision queue.

The matrix is reviewed quarterly by the Information Security function and the executive sponsor. New actions are added when their scope and rollback can be defined. Actions are removed if their use causes problems that outweigh their value.

### 3.6 Communication During Incidents

Communication during incidents is structured to keep the right people informed without overwhelming the response team or creating new risks through premature disclosure.

**Internal communication** during the response uses dedicated channels: a defined incident channel in the company's chat platform, a defined incident email distribution list, and a defined conference bridge for verbal coordination. These channels are established as part of preparation; they do not get created during the incident.

The Information Security function maintains the running record of the incident: timeline, decisions made, actions taken, and outcomes observed. This record becomes the basis for the post-incident review and any required external reporting.

**Executive communication** for High and Critical incidents goes to the executive sponsor at declared intervals (typically every two hours during active response for Critical, daily for High). Communications include a current status, the actions taken since the last update, the actions planned, and any decisions the executive needs to make.

**External communication** is restricted during active response. Public statements, press communication, customer notification, and similar external communication go through a defined process that involves the executive sponsor and, where applicable, legal counsel. Premature external communication can compromise the response, expose the organization to legal risk, and create unnecessary alarm.

Specific external notifications may be required by:

Regulatory requirements applicable to the data involved (privacy regulations, sector-specific rules). Contractual obligations to clients, vendors, or partners. Cyber insurance policy requirements. Law enforcement or government reporting requirements.

The applicable obligations are assessed during the response with appropriate counsel. Notifications are made within the timelines required, which vary substantially by jurisdiction and data type.

### 3.7 External Support and Retainers

[ORGANIZATION_NAME] maintains relationships with external parties who can support incident response when internal capacity is insufficient or specialized expertise is needed.

**Incident response retainer.** A relationship with a qualified incident response firm, established before incidents occur. The retainer specifies the engagement model, response time commitment, and the conditions under which the firm is engaged. The current retainer is with [INCIDENT_RESPONSE_RETAINER_FIRM, e.g., Mandiant, Unit 42, CrowdStrike, Kroll, or local equivalent].

**Legal counsel.** Counsel familiar with breach notification, regulatory obligations, and cybersecurity matters. The current legal counsel for security matters is [SECURITY_LEGAL_COUNSEL]. Some incidents are conducted under attorney-client privilege; the conditions for invoking privilege are decided in consultation with counsel at the start of the response.

**Cyber insurance carrier.** The carrier is notified for incidents that may meet the policy's reporting threshold. The notification is required by the policy and is also the path to coverage for the costs of response, recovery, and any liability that emerges. The current carrier and policy details are documented in [CYBER_INSURANCE_DOCUMENTATION].

**Law enforcement.** Engagement with law enforcement (FBI, local police, sector-specific agencies) is considered for incidents involving criminal activity, regulated data, or threats that exceed [ORGANIZATION_NAME]'s ability to respond independently. The decision to engage law enforcement is made with the executive sponsor and legal counsel.

**Vendors and service providers.** Critical vendors are contacted when an incident affects their services or when their cooperation is needed for response. The contact information for critical vendor support is maintained with the incident response materials.

### 3.8 Evidence Handling

Incidents involving criminal activity, regulatory issues, or potential litigation may require evidence preservation. The response process preserves evidence by default and applies stricter handling when the situation warrants it.

Standard evidence preservation includes:

Logs from affected systems, identity providers, network equipment, and endpoint security tools. Disk images of affected systems where the situation calls for forensic analysis. Memory captures from affected systems where volatile evidence is needed. Records of all decisions made during the response, including the reasoning for each decision and the people involved. The chronological timeline of the incident.

For incidents likely to involve litigation or regulatory action, a chain of custody is maintained for evidence. Evidence is handled by named custodians with documented transfers. The handling specifics are determined in consultation with legal counsel.

Evidence is retained per the [LOGGING_AND_MONITORING_STANDARD] retention rules at minimum. Incidents under active legal or regulatory process may require longer retention; the period is determined with counsel.

### 3.9 Post-Incident Review

Every declared incident at Medium severity or higher concludes with a post-incident review. The review produces a written record of what happened, what worked, what did not, and what should change.

The review includes:

A factual timeline of the incident from initial detection through resolution. The classification and reclassification decisions made during the response, with reasoning. The actions taken during each phase, with reasoning. The outcomes observed at each step. An honest assessment of what worked well and what did not. Specific recommendations for improvements to the security program, with named owners and target dates.

The review is conducted by the Information Security function with input from everyone involved in the response. The output is provided to the executive sponsor. Lessons are incorporated into the security program through the standard governance processes.

For Critical incidents, the post-incident review is conducted within thirty days of closure. For High incidents, within sixty days. For Medium incidents, within ninety days. Reviews not conducted within these timelines are escalated.

The review is not a venue for assigning blame to individual response team members. It is a venue for understanding the system that produced the incident and improving that system. Honest discussion of mistakes is essential to that purpose.

### 3.10 Tabletop Exercises and Preparation Activities

[ORGANIZATION_NAME] runs tabletop exercises at least quarterly. The exercises test the incident response process against realistic scenarios appropriate to the organization's environment and threat exposure.

Quarterly exercises cycle through the most plausible incident types: account compromise, ransomware, business email compromise, lost device with sensitive data, supply chain or vendor incident, insider threat, and similar scenarios. The companion runbook (RUN-IR-001) describes the specific exercise scenarios and the facilitation guide.

Exercises involve the response team plus, on a rotating basis, the executive sponsor and other leadership. Annual exercises include the executive sponsor by default to maintain leadership engagement with the response process.

Exercise outcomes are documented with the same rigor as actual incidents. Gaps identified during exercises are remediated through the same process that handles post-incident review findings.

Other preparation activities include maintaining the incident response materials (contact lists, runbook content, authority matrix, evidence handling procedures), validating that backup and recovery processes work, and confirming that the relationships with external partners are current.

### 3.11 Exceptions

Specific situations may warrant deviation from the standard response process. Common situations:

A documented emergency that requires immediate action outside the normal authority structure, where the action is logged and reviewed retroactively within five business days.

A regulatory or contractual obligation that requires response in a specific way that differs from the standard process. The variation is documented and the response follows the regulatory or contractual requirement.

An exercise or simulation that intentionally tests the response under non-standard conditions. The exercise is documented as such and the response is conducted in the exercise frame.

Exceptions follow the same process described in POL-IAM-001 Section 3.10.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Declares incidents. Coordinates the response. Maintains the runbooks, the authority matrix, and the relationships with external partners. Conducts post-incident reviews. Runs the tabletop exercise program.

**Executive sponsor.** Receives notification and updates for High and Critical incidents. Makes decisions that exceed the Information Security function's authority. Approves engagement of external counsel and similar resources. Reviews post-incident reports. Funds remediation work that emerges from incidents.

**IT function (or IT service provider).** Implements containment and recovery actions on technical systems. Maintains the technical capabilities (logging, EDR, backups) the response depends on. Participates in the response and in tabletop exercises.

**Legal counsel.** Advises during incidents involving regulatory obligations, contractual issues, or potential litigation. Determines when attorney-client privilege applies. Reviews external communications.

**Department leads and managers.** Notify the Information Security function of unusual activity their teams observe. Cooperate with response activities affecting their systems. Participate in tabletop exercises when their area of responsibility is involved.

**All employees and contractors.** Report suspected incidents promptly through the documented channels. Do not investigate suspected incidents independently. Cooperate with response activities. Follow direction from the response team during active incidents.

## 5. Enforcement

Violations of this policy may result in disciplinary action consistent with HR policies. Specific situations:

Failure to report suspected incidents: addressed through training and management coaching for first occurrences; formal action for repeated failures.

Independent investigation that compromises an active response: addressed through training and management coaching; significant compromise may warrant formal action.

Premature external disclosure of incident details: formal action consistent with the severity of the disclosure.

Deliberate concealment of incidents or evidence: serious disciplinary action up to and including termination.

The enforcement framing reflects that effective incident response depends on prompt, candid reporting. Penalizing honest reports discourages the reporting that the program depends on.

## 6. Related Documents

POL-IAM-001: Access Control Policy
POL-IAM-002: Password and Authentication Standard
POL-IAM-005: Remote Access Policy
POL-IAM-011: Non-Human Identity Governance Policy
POL-AUP-001: Acceptable Use Policy
POL-AM-001: Asset Management Policy
POL-DC-001: Data Classification and Handling Policy
RUN-IR-001: Incident Response Runbook (the operational companion to this policy)
[LOGGING_AND_MONITORING_STANDARD]: Logging and Monitoring Standard (forthcoming, evidence retention)
POL-EP-001: Endpoint Protection Policy (forthcoming)
POL-AUP-001: Vulnerability Management Policy (forthcoming)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

GV.RR-04 (Cybersecurity is included in human resources practices). DE.AE-02 (Potentially adverse events are analyzed to better understand associated activities). DE.AE-03 (Information is correlated from multiple sources). DE.AE-06 (Information on adverse events is provided to authorized staff and tools). DE.AE-08 (Incidents are declared when adverse events meet the defined incident criteria). RS.MA-01 (The incident response plan is executed in coordination with relevant third parties once an incident is declared). RS.MA-02 (Incident reports are triaged and validated). RS.MA-03 (Incidents are categorized and prioritized). RS.MA-04 (Incidents are escalated or elevated as needed). RS.MA-05 (The criteria for initiating incident recovery are applied). RS.AN (Incident analysis). RS.CO (Incident response reporting and communication). RS.MI (Incident mitigation). RC.RP (Incident recovery plan execution). RC.CO (Incident recovery communication).

**CIS Controls v8:**

Control 17 Incident Response Management: Safeguards 17.1 (designate personnel to manage incident handling), 17.2 (establish and maintain contact information for reporting security incidents), 17.3 (establish and maintain an enterprise process for reporting incidents), 17.4 (establish and maintain an incident response process), 17.5 (assign key roles and responsibilities), 17.6 (define mechanisms for communicating during incident response), 17.7 (conduct routine incident response exercises), 17.8 (conduct post-incident reviews), 17.9 (establish and maintain security incident thresholds).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above. Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution-ShareAlike 4.0.*
