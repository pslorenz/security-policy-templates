# RUN-IR-001: Incident Response Runbook

| | |
|---|---|
| **Document ID** | RUN-IR-001 |
| **Related Policy** | POL-IR-001 (Incident Response) |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Semiannual |
| **Owner** | [POLICY_OWNER] |
| **Audience** | Security operations, IT staff, vCISO, MSP consultant responding to incidents |

---

## 1. Purpose and Scope

This runbook operationalizes POL-IR-001 for the incident types most commonly faced by small and mid-market organizations. It provides step-by-step playbooks that the response team follows during active incidents, plus the communication templates and decision frameworks that support the response.

The runbook does not replace the policy. POL-IR-001 establishes the response framework: the six phases, the severity tiers, the standing authority matrix, the post-incident review requirements. This runbook is what the response team reaches for when an incident is happening and they need to remember what to do next.

The runbook covers five incident scenarios: account compromise, ransomware, business email compromise, lost or stolen device, and phishing campaign response. These scenarios cover the majority of incidents at SMB scale. Other incident types are addressed by adapting the patterns established here.

## 2. Prerequisites

The response works only if the foundation is in place before anything happens. The following items are confirmed during quarterly tabletop exercises and reviewed at the start of any active response.

### 2.1 Contact Information

The incident response contact list is current and accessible. The list includes:

The Information Security function lead and backup. The IT function lead and backup. The executive sponsor and backup. Legal counsel for security matters. The cyber insurance carrier and broker. The incident response retainer firm (if one is in place). Critical vendor support contacts (EDR provider, identity provider, cloud platform, primary SaaS vendors).

The contact list is stored in a location accessible during incidents, including when normal company systems may be unavailable. Acceptable storage: a printed copy in a secure location, a contact list in a separately-managed system, or both.

### 2.2 Communication Channels

The dedicated incident channels are established and tested:

A defined chat channel for incident coordination on the company's chat platform. A defined email distribution list for incident updates. A defined conference bridge or video meeting room for verbal coordination. A separately-managed channel that does not depend on the company's identity provider, email, or chat platform, for use when those systems are unavailable or may be compromised. Account compromise of an administrator, ransomware, and BEC all move to this channel by default.

### 2.3 Tools and Access

The response team has the access needed to execute the playbooks below:

EDR platform administrative access for endpoint isolation and investigation. Identity provider administrative access for account disabling and session revocation. Email platform administrative access for message search and inbox rule review. Cloud platform administrative access for resource isolation and log review. Logging platform access for investigation and evidence collection.

Access for the response team is reviewed quarterly to confirm it remains current and that just-in-time elevation paths work as expected.

### 2.4 Standing Authority Matrix

The standing authority matrix described in POL-IR-001 Section 3.5 is current. The matrix specifies pre-authorized actions, scope limits, named approvers, and rollback procedures. The response team references the matrix to determine which actions can be taken immediately versus which require approval.

### 2.5 Output Artifacts

Every declared incident produces the same set of records. The running record of decisions and actions, started when the incident is declared (Section 3.1.2). The evidence package, preserved under POL-IR-001 Section 3.8 and retained per STD-LOG-001. The communications sent, kept with the running record. The post-incident review (Section 4) for incidents at Medium severity or higher.

## 3. Procedure

The procedure runs in four phases. Phase 1 applies to every incident. Phase 2 runs the playbook that matches the incident type. Phases 3 and 4 cover the communication and escalation decisions that come up in every playbook, and run alongside Phase 2 rather than after it.

### 3.1 Phase 1: The First Fifteen Minutes

Regardless of incident type, the first fifteen minutes follow the same pattern.

#### 3.1.1 Triage the Report

The reported event is reviewed to determine whether it meets the threshold for incident declaration. The triage answers three questions:

What is the user or system reporting? Get the specifics: what was observed, when, on what system, by whom.

Is this likely a real incident or a false alarm? Some indicators that it is likely real: confirmed unauthorized access, ransomware-style behavior, credential exposure with active sign-in attempts, data found in unexpected places. Some indicators that it may be false: an alert from a tool with a known false positive history, a routine event misinterpreted by the reporter, expected administrative activity that surprised someone.

What severity tier likely applies? Initial severity assignment per POL-IR-001 Section 3.2. Severity can be revised as the response progresses.

If the situation does not meet the threshold for incident declaration, document the triage decision and close the report. If the situation does meet the threshold, declare the incident and proceed.

#### 3.1.2 Establish Coordination

Open the dedicated incident channel. Note the time of declaration. Begin a running record of decisions and actions; this becomes the basis for the post-incident review and any required external reporting.

For Critical incidents, notify the executive sponsor immediately. For High incidents, the notification can occur within the four-hour window per POL-IR-001 Section 3.2.

#### 3.1.3 Activate the Appropriate Playbook

Based on the initial assessment, activate the relevant playbook from Section 3.2. If the incident type does not cleanly match any of the playbooks, follow the closest match and adapt as needed.

#### 3.1.4 Begin Containment

Containment actions defined in the standing authority matrix can begin immediately without further approval. Containment actions outside the matrix require the appropriate approval per the matrix's documented authority structure.

The principle: do not let containment delay slow the response. The longer an attacker has access, the more damage results.

### 3.2 Phase 2: Run the Playbook

Each playbook below follows the response phases in POL-IR-001 Section 3.4: first hour, containment, eradication and recovery, and post-incident. Incidents that do not match a playbook follow the closest one and adapt.

#### 3.2.1 Account Compromise

Account compromise is the most common SMB incident. A user's credentials have been stolen or guessed, and an attacker has used them to access company systems. Common signs include sign-in alerts from unexpected locations, unauthorized inbox rules, unexpected emails sent from the account, financial fraud attempts, and unauthorized access to cloud applications.

**First hour:**

Disable the compromised account immediately. In Microsoft Entra: block sign-in and revoke all sessions. In Google Workspace: suspend the user and revoke all sessions. The account stays disabled until the response is complete; do not re-enable for the user's convenience.

Force password reset and require re-enrollment of all authentication factors when the account is later restored. The old password is treated as known to the attacker.

Review recent sign-in activity for the account: sign-in locations, IP addresses, applications accessed, devices used. The review identifies what the attacker reached.

Review inbox rules and forwarding configurations. Attackers commonly create rules that forward, hide, or delete email related to fraud or further attacks. Remove any unauthorized rules.

Review the authentication methods registered on the account. Attackers who complete an adversary-in-the-middle phishing attack commonly register their own MFA method to keep access after a password reset. Remove any method the user did not register.

Review delegations and OAuth grants on the account. Remove any that the user did not authorize.

Revoking sessions invalidates refresh tokens, but access tokens already issued can remain valid until they expire (typically up to an hour) unless the platform supports continuous access evaluation. Keep monitoring the account's sign-in and audit activity through that window.

Check whether the attacker accessed financial systems, HR systems, or other sensitive resources. Each accessed system requires its own review and any necessary further response.

Notify the user through an out-of-band channel (phone call, in-person, separate email account). Do not communicate through the compromised channel.

**Containment:**

Block the IP addresses or geographic regions associated with the unauthorized access at the firewall and conditional access level, where the standing authority matrix permits.

Isolate any endpoints the user signed in from during the compromise window. The endpoints may also be compromised.

If the user has privileged access, escalate severity. Privileged account compromise is Critical.

**Eradication and recovery:**

Determine how the credentials were stolen. Common vectors: phishing email, AiTM phishing kit, malware on a personal device, credential stuffing from a third-party breach, social engineering of a help-desk reset.

Address the root cause based on the vector. For phishing: review awareness training and phishing-resistant MFA enrollment. For credential stuffing: confirm the user's password was unique and review the password manager adoption. For social engineering: review the help-desk authentication procedures.

When the response is complete, restore the account with fresh credentials and re-enrollment of all authentication factors. Phishing-resistant authentication is enrolled if not already in place.

**Post-incident:**

Conduct the post-incident review per POL-IR-001 Section 3.9. Specific lessons to capture: how did the credentials get stolen, what controls would have prevented or caught the compromise sooner, what improvements should be made to authentication or monitoring.

#### 3.2.2 Ransomware

Ransomware encrypts company files and demands payment for decryption. Common signs include files renamed with ransomware extensions, ransom notes appearing on systems, EDR alerts for ransomware-family activity, users reporting that files cannot be opened.

This is a Critical incident. The response is immediate.

**First hour:**

Isolate affected systems immediately through the EDR platform. Isolation prevents further spread while preserving the system for investigation.

If multiple systems are affected and the spread is active, isolate broader segments. Network segmentation per POL-NET-001 should limit the blast radius; the response uses that segmentation to contain.

Notify the executive sponsor immediately. Notify the cyber insurance carrier before engaging outside firms: many policies cover response costs only when the carrier is told first and a panel firm is used. Then engage the incident response retainer, confirming it is a carrier-approved firm.

Notify legal counsel. Some ransomware response decisions (whether to pay, whether to engage with attackers, what to disclose) carry legal implications that warrant counsel from the start.

Preserve evidence. Disk images of affected systems, EDR telemetry, ransom notes, network logs from the time of detection. Evidence supports later analysis and any legal or regulatory action.

Confirm the backup status. The most important question early in ransomware response is: do clean backups exist for the affected data, and how recent are they.

**Do not restart, reboot, or shut down affected systems** unless the incident response team specifically directs it. Memory holds evidence and, for some ransomware variants, encryption keys, and shutdown destroys both. The exception is a system that cannot be isolated from the network: if isolation fails and encryption is spreading, powering the system down to stop the spread takes priority over preserving memory, consistent with CISA's ransomware response guidance.

**Containment:**

Identify the entry point. Common vectors: compromised remote access credentials, exploited vulnerability in internet-facing service, malicious email attachment, supply chain compromise through managed service provider.

Block the entry point. If credentials were used, disable the affected accounts and rotate. If a vulnerability was exploited, take the vulnerable service offline. If email was the vector, check for additional malicious messages and remove from mailboxes.

Identify any lateral movement. The attacker likely accessed multiple systems before deploying the ransomware. Each accessed system is a potential persistence point.

Consider whether to disclose the incident publicly or to specific parties. The decision is made with executive sponsor and legal counsel input, not by the response team alone.

**Eradication and recovery:**

Eradicate the attacker's presence. This typically means rebuilding affected systems from clean backups or fresh installations rather than attempting to clean malware in place. Cleaning ransomware is unreliable; rebuilding is the safer path.

Recover data from backups. Verify the backups are uninfected before restoration. Restore in a controlled order, prioritizing the systems and data most critical to operations.

If backups are not available or are also encrypted, the recovery options are limited. The decision about whether to pay ransom is made with executive sponsor, legal counsel, and cyber insurance carrier input. Payment carries legal and ethical risks beyond the immediate cost.

Validate restored systems before returning to production. The rebuilding process is not complete until the affected systems are functioning and clean.

**Post-incident:**

The post-incident review for ransomware is substantial and conducted within thirty days of closure per POL-IR-001 Section 3.9. Key lessons: how did the attacker get in, how did they reach the backup or the production data, what segmentation or detection would have caught the attack sooner, what backup hygiene improvements are needed.

Specific notification obligations may apply: regulatory notification for affected data, cyber insurance reporting, customer notification per contracts, and law enforcement reporting where appropriate. The notifications are coordinated with legal counsel.

#### 3.2.3 Business Email Compromise (BEC)

BEC is a fraud scheme where an attacker either compromises an executive's email account or impersonates an executive to redirect payments, change wire instructions, or extract sensitive information. Common signs include unusual payment requests from executives, last-minute changes to vendor banking information, urgent requests outside normal business processes, and emails that look subtly off (slightly different sender domain, unusual phrasing).

**First hour:**

If money has been transferred or is in transit, contact the bank immediately. Some transfers can be reversed if the bank is notified within hours; the window closes quickly.

Determine whether the email account in question is actually compromised (the attacker is operating from inside the legitimate account) or is being impersonated (the attacker is sending mail from a similar-looking external domain). The response differs.

If the account is compromised: follow the account compromise playbook (Section 3.2.1) and additionally investigate whether other accounts are compromised, whether financial systems were accessed, and whether other fraudulent communications were sent.

If the account is impersonated: identify the spoofing pattern (lookalike domain, display name spoofing, internal email address impersonation). Block the malicious sender at the email security platform. Search for and remove similar messages from other recipients' mailboxes.

Notify finance staff and executive assistants company-wide that a BEC attempt is in progress and to verify any unusual payment requests through out-of-band channels.

**Containment:**

For confirmed compromise: rotate credentials, revoke sessions, review and remove unauthorized inbox rules, review what financial systems were accessed.

For impersonation: implement additional email authentication (DMARC enforcement, anti-spoofing rules), block the lookalike domain, ensure the spoofed person's name and email patterns are protected by tenant-level rules.

Communicate with finance, accounts payable, and accounts receivable about the specific attack pattern. BEC often targets these teams; making them aware of the active attempt prevents further successful attempts.

**Eradication and recovery:**

For compromise: complete the account compromise eradication steps. Verify the attacker has been fully removed before restoring access.

For impersonation: confirm the email security controls are blocking similar attempts. Review the broader email security posture for gaps the attacker exploited.

If money was lost, work with the bank, cyber insurance, law enforcement, and counsel to pursue recovery. In the United States, file a complaint with the FBI's Internet Crime Complaint Center (IC3) as soon as possible; the FBI works with banks to freeze fraudulent domestic wires, and the chance of recovery drops quickly with each day.

**Post-incident:**

Review the financial controls that allowed the fraudulent transaction (or would have allowed it). Effective controls include out-of-band verification for any payment changes, dual approval for transactions above defined thresholds, and standardized verification procedures for vendor banking changes.

Review the email security configuration. DMARC enforcement, sender authentication, lookalike domain blocking, and impersonation detection all reduce BEC effectiveness. Gaps identified in any of these areas are addressed.

Conduct awareness training reinforcement on BEC patterns for finance and executive support staff specifically.

#### 3.2.4 Lost or Stolen Device

A company-issued laptop, tablet, phone, or hardware authentication key has been lost, stolen, or otherwise become unaccounted for. The risk depends on what the device contained and what it could access.

**First hour:**

Confirm the report. The user reports the device missing; the response begins immediately based on the user's word.

Determine what the device was: company-issued or BYOD, what data it stored, what authentication factors it held, whether it was encrypted.

Initiate remote wipe through the device management platform. The wipe destroys company data. For BYOD devices with separated company and personal data, the wipe affects only company data.

Disable the device's access to company resources. The device's certificate is revoked, the trust relationship is broken, and any cached credentials become unusable.

Disable any hardware authentication factors associated with the device (FIDO2 keys built into the device, platform passkeys synced to the device).

Review accounts the device had access to for unusual activity since the device was lost. Sign-in alerts, unusual application access, anomalous patterns suggest the device has been used by an unauthorized party.

**Containment:**

If the device was encrypted with a strong protector and the wipe was successful, the data exposure risk is limited. Encryption per POL-EP-001 Section 3.3 is the primary protection against device loss.

If the device was unencrypted (which should not occur per POL-EP-001 but happens in practice), treat the situation as data exposure and follow POL-DC-001 procedures for the data classifications involved.

If the device held authentication factors that are now potentially in attacker hands, revoke those factors and re-enroll. This may include FIDO2 keys, certificate-based authentication, and stored authentication tokens.

**Eradication and recovery:**

Issue replacement equipment to the user. The replacement follows the standard provisioning process and includes new authentication factors.

If the device is recovered later, do not return it to service without forensic examination. A device that has been outside company control may have been tampered with.

Update the asset inventory. If the device is presumed lost, mark it as such with the date and circumstances. If recovered, update accordingly.

**Post-incident:**

Review the circumstances of the loss. Some losses indicate process gaps (devices left in vehicles, devices not returned at offboarding, devices stored insecurely at home). Process improvements address recurring patterns.

For stolen devices, file a police report and document the theft for insurance and any legal action.

For lost authentication factors, review whether the affected user had appropriate backup authentication paths to avoid being locked out.

#### 3.2.5 Phishing Campaign Response

A phishing campaign targets [ORGANIZATION_NAME] users. Reports come in from multiple users, the email security platform has detected the campaign, or the security team is alerted by external sources. The response addresses both the immediate campaign and the protection of users who may have already responded.

**First hour:**

Identify the scope of the campaign. How many users received the malicious messages, what is the message content, what is the malicious payload (link to credential harvesting, malware attachment, BEC framing).

Search and remove the campaign from all affected mailboxes. The search uses sender, subject, and content patterns. Removal is performed through the email security platform's threat hunting capabilities.

Block the malicious sender at the email gateway and the malicious destination URLs at the web filtering layer.

Identify users who interacted with the campaign. Specifically: who clicked the link, who entered credentials, who downloaded an attachment, who replied to the sender. Each interaction has different consequences.

For users who entered credentials: treat as account compromise per Section 3.2.1, including immediate credential reset and session revocation. Even if the user reports they think they entered the wrong information, treat the credentials as exposed.

For users who downloaded an attachment: isolate the affected endpoint immediately through the EDR platform. Investigate for malware execution.

For users who replied or clicked but did not enter credentials: lower risk, but their email may now be the target of follow-on social engineering. Notify them and remain alert for subsequent attempts.

**Containment:**

Communicate to all users about the campaign. The communication identifies the pattern (without including the malicious payload) and reminds users of the reporting process.

If the campaign is using a recognizable sender or pattern, share that information internally so users can recognize related attempts.

Confirm that email authentication controls (DMARC, SPF, DKIM) are configured correctly. Phishing campaigns often exploit gaps in these controls.

**Eradication and recovery:**

Continue searching for and removing the campaign messages until no new instances are found in mailboxes.

Address compromised credentials and infected endpoints per the playbooks above.

Verify that email security controls are tuned to catch similar future attempts. Add specific patterns to threat detection rules where the platform supports it.

**Post-incident:**

Review the campaign's success rate. Successful campaigns reveal gaps in awareness, technical controls, or both. Effective metrics include: percentage of users who reported the message versus percentage who clicked, time from campaign arrival to first report, time from first report to response.

Reinforce awareness training with the specific patterns from this campaign as examples.

If the campaign exploited a specific vulnerability (lookalike domain, missing email authentication, weak sender verification), address that vulnerability.

### 3.3 Phase 3: Communicate

The templates below provide starting points for incident communications. Adapt to the specific situation; do not send the templates verbatim.

#### 3.3.1 Executive Notification, Critical Incident

```
Subject: Critical Incident Notification - [BRIEF DESCRIPTION]

A Critical security incident was declared at [TIME] today. Initial details:

- What happened: [BRIEF FACTUAL DESCRIPTION]
- Current status: [WHAT THE RESPONSE TEAM IS DOING]
- Known impact: [SPECIFIC SYSTEMS, USERS, OR DATA AFFECTED]
- Response status: [WHO IS ENGAGED]
- Next update: [TIME, TYPICALLY TWO HOURS]

[INCIDENT_LEAD] is leading the response. The standing authority matrix has been
activated. External support [HAS BEEN / HAS NOT YET BEEN] engaged.

Contact me directly at [PHONE] for any executive-level decisions needed.

[INCIDENT_LEAD_NAME]
```

#### 3.3.2 User Communication, Account Compromise

```
Subject: Important: Your account has been temporarily disabled

We have detected suspicious activity on your account and have temporarily disabled
it as a precaution. This is a precaution, not an accusation; the activity may be
unauthorized access by someone other than you.

To restore your access, please contact [IT_SUPPORT_CONTACT] using a means other
than email. We will verify your identity and walk through the account restoration
process.

If you receive this notice, do not click any links in any email claiming to come
from IT or HR until you have verified directly with [IT_SUPPORT_CONTACT].

Thank you for your patience.

[IT_FUNCTION_NAME]
```

#### 3.3.3 Internal Communication, Active Phishing Campaign

```
Subject: Active phishing campaign - please be aware

A phishing campaign is currently targeting [ORGANIZATION_NAME] employees. The
campaign uses messages that [BRIEF PATTERN DESCRIPTION].

If you receive a message matching this pattern:
1. Do not click any links or open any attachments.
2. Report the message through [REPORTING_CHANNEL].
3. Delete the message after reporting.

If you have already clicked or entered information into a suspicious site,
contact [IT_SUPPORT_CONTACT] immediately. Reporting an interaction is never a
problem; not reporting one creates problems we cannot help with.

We are actively removing these messages from mailboxes and blocking the source.
Additional updates will follow as the response progresses.

[IT_FUNCTION_NAME]
```

#### 3.3.4 External Notification Trigger

External notification is required in specific situations. Triggers include:

Confirmed compromise of personal data subject to privacy regulations. Confirmed compromise of payment card data. Confirmed compromise of health information protected by applicable regulations. Compromise of client data covered by contractual notification obligations. Incidents that may meet cyber insurance reporting thresholds. Incidents that may be reportable to CISA under CIRCIA once its final rule takes effect (see POL-IR-001 Section 3.6; requirements may change when the rule is finalized).

External notification is coordinated with legal counsel. The specific notification language is drafted with counsel and reviewed by the executive sponsor before sending.

### 3.4 Phase 4: Escalation Decisions

Three decisions recur across incident types and are never the response team's to make alone. The team's job is to bring accurate information to the people who make them.

#### 3.4.1 Whether to Pay Ransom

This decision is not the response team's to make alone. The decision is made with executive sponsor, legal counsel, cyber insurance carrier, and ideally the engaged incident response firm.

Factors that argue against payment: sanctions risk (in the United States, the Treasury Department's Office of Foreign Assets Control has warned that facilitating payments to sanctioned actors can violate sanctions law regardless of the victim's intent), no guarantee of decryption after payment, and the risk of marking the organization as one that pays.

Factors that argue for payment: critical operational impact when no clean backups exist, regulatory or contractual obligations that cannot be met any other way.

The response team's role is to provide accurate information to support the decision: backup status, decryption viability, business impact, attacker demands. The decision itself is escalated.

If payment is made, reporting obligations may follow. Once CIRCIA's final rule takes effect, covered critical infrastructure entities will need to report a ransom payment to CISA within twenty-four hours (see POL-IR-001 Section 3.6). Financial services entities regulated by NYDFS already owe the Department notice within twenty-four hours of an extortion payment. Confirm current obligations with counsel before payment, because both the CIRCIA requirements and their effective date may change when the final rule is published.

#### 3.4.2 Whether to Engage Law Enforcement

Engagement with law enforcement is considered for incidents involving:

Ransomware (FBI is interested in ransomware activity). Suspected nation-state activity. BEC with significant financial loss. Insider threat with potential criminal activity. Threats against employees or facilities.

The decision is made with executive sponsor and legal counsel. Engagement does not commit the organization to any specific response; law enforcement typically observes and gathers intelligence rather than directing the response.

Specific contact paths for law enforcement engagement are documented in the contact list referenced in Section 2.1.

#### 3.4.3 Whether to Disclose Publicly

Public disclosure is required by some regulations (state breach notification laws, industry-specific rules, contractual obligations). Public disclosure may also be the right choice even when not required, particularly for incidents where stakeholders are likely to discover the issue independently.

The decision and timing are made with executive sponsor, legal counsel, communications counsel, and any retained crisis communication firm.

Premature public disclosure can compromise the response, expose the organization to legal risk, and create unnecessary alarm. The response team does not make this decision unilaterally.

## 4. Analysis and Findings

After the immediate response concludes, the post-incident review is conducted per POL-IR-001 Section 3.9. The review timeline:

Critical incidents: review completed within thirty days of closure. High incidents: within sixty days. Medium incidents: within ninety days.

The review produces:

A factual timeline of the incident. The classification and reclassification decisions made, with reasoning. The actions taken at each phase. An honest assessment of what worked and what did not. Specific recommendations for program improvements, with named owners and target dates.

The review is a learning exercise, and assigning blame works against it. The post-incident review process described in POL-IR-001 Section 3.9 governs.

Improvement items from the review are tracked through the security program's standard governance processes until completion.

Findings that cannot be fixed within the review's target dates go to the risk register under POL-GOV-001, so they are tracked and owned rather than left in the review document. Findings that require a temporary deviation from policy go through the exception process.

## 5. Operational Cadence

The runbook is used during incidents, but it only works if it is maintained between them.

Each quarter, the tabletop exercise required by POL-IR-001 Section 3.10, run under RUN-IR-002, confirms the prerequisites in Section 2: the contact list is current, the out-of-band channel works, response access and just-in-time elevation paths work, and the standing authority matrix is current. Each exercise also runs one playbook from Section 3.2 end to end, rotating so that all five are exercised within about fifteen months.

Every six months, matching the review cycle in the metadata table, the Information Security function reviews the runbook against lessons from incidents and exercises, changes to the platforms it names (session revocation, message purge, and device wipe procedures change with vendor releases), and any updates to POL-IR-001.

After every incident at Medium severity or higher, the post-incident review in Section 4 checks whether the playbook used was accurate and complete. Corrections are made within thirty days.

## 6. Automation Opportunities

Most first-hour actions are repeatable and benefit from automation, provided each automated action appears in the standing authority matrix (POL-IR-001 Section 3.5) with its trigger, scope limit, and rollback path. Targets, in priority order:

Account containment on a high-confidence identity alert: block sign-in, revoke sessions, and list the MFA methods, inbox rules, and OAuth grants added during the suspected compromise window for an analyst to review.

Endpoint isolation when the EDR platform detects ransomware behavior, scoped to the affected device.

Phishing search-and-purge when a user-reported message matches a confirmed campaign, scoped to messages matching the confirmed sender and indicators.

Incident record creation on declaration: the incident channel, the running record, and the ticket, opened together with the declaration time stamped.

Evidence collection: export of the affected account's sign-in and audit logs for the compromise window into the evidence store, so the record exists before any log retention window closes.

Actions that cannot be scoped and rolled back stay manual, consistent with POL-IR-001 Section 3.5.

## 7. References

### Related Documents in This Library

POL-IR-001: Incident Response Policy (the parent policy this runbook operationalizes)

POL-IAM-001: Access Control Policy (account management)

STD-IAM-001: Password and Authentication Standard (credential rotation)

POL-IAM-003: Non-Human Identity Governance Policy (service account incidents)

POL-AM-001: Asset Management Policy (asset-aware response)

POL-DC-001: Data Classification and Handling Policy (data exposure response)

POL-EP-001: Endpoint Protection Policy (endpoint isolation and recovery)

POL-VM-001: Vulnerability Management Policy (response to actively-exploited vulnerabilities)

POL-NET-001: Network Security Policy (network containment)

POL-TPRM-001: Third-Party Risk Management Policy (vendor incident coordination)

RUN-IR-002: Tabletop Exercise Facilitation Runbook (exercises that test these playbooks)

STD-DR-001: Data Backup and Recovery Standard (ransomware recovery)

STD-NET-001: Email and Web Browser Protection Standard (phishing and BEC prevention)

STD-LOG-001: Logging and Monitoring Standard (evidence retention)

### External Resources

CISA (Cybersecurity and Infrastructure Security Agency) provides current threat intelligence, advisories on actively-exploited vulnerabilities, and incident response guidance at cisa.gov.

The FBI Internet Crime Complaint Center (IC3) at ic3.gov is the reporting path for BEC, ransomware, and other internet-based crimes in the United States.

NIST SP 800-61 Revision 3 (Incident Response Recommendations and Considerations for Cybersecurity Risk Management, April 2025) organizes incident response around the NIST CSF 2.0 functions. POL-IR-001 and this runbook are consistent with it; the six phases in POL-IR-001 expand the four-phase incident life cycle from the earlier Revision 2.

Industry-specific Information Sharing and Analysis Centers (ISACs) provide sector-specific threat intelligence and incident response support.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This runbook is issued under the authority of the executive sponsor named in POL-IR-001.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
