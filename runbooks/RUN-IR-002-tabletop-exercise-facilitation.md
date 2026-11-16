# RUN-IR-002: Tabletop Exercise Facilitation Runbook

| | |
|---|---|
| **Document ID** | RUN-IR-002 |
| **Related Policy** | POL-IR-001 (Incident Response), Section 3.10 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Semiannual |
| **Owner** | [POLICY_OWNER] |
| **Audience** | Whoever plans and runs the exercise: the Information Security function, an IT lead, a vCISO, or an MSP consultant |

---

## 1. Purpose and Scope

This runbook describes how to plan, run, and follow up on the tabletop exercises that POL-IR-001 Section 3.10 requires each quarter. It is written so that someone who has never facilitated a tabletop can run a useful one by following it.

A tabletop exercise is a structured conversation about an incident that has not happened. The team sits together, hears a scenario unfold in stages, and talks through what they would do, who would decide, and what they would need. Nothing is touched in production. The value is in finding the gaps while finding them is cheap: the phone number nobody has, the decision nobody knows they own, the backup nobody has tried to restore.

The exercises test the response process in POL-IR-001 and the playbooks in RUN-IR-001. This runbook does not replace either. Section 3.4 provides seven ready-to-run scenarios built on those playbooks.

## 2. Prerequisites

### 2.1 People

**Facilitator.** Runs the exercise, presents the scenario, keeps time, and asks the questions. The facilitator does not play a responder and does not answer the questions they ask. In a small organization this is often the outside security provider, which also keeps the facilitator from defending their own decisions.

**Note-taker.** Records decisions, gaps, and questions as they come up, using the template in Section 4.1. The facilitator cannot do both well.

**Participants.** The people who would respond to the scenario for real: the Information Security function, IT, and the business people the scenario touches. Finance belongs in any scenario involving payments. The executive sponsor participates at least once a year, as POL-IR-001 Section 3.10 requires, and in any scenario where an executive decision drives the outcome.

Six to ten participants works best. With more than twelve, most people stop talking.

### 2.2 Materials

The current versions of POL-IR-001, RUN-IR-001, the incident contact list (RUN-IR-001 Section 2.1), and the standing authority matrix (POL-IR-001 Section 3.5). A printed or shared copy of the scenario injects, revealed one at a time. The note-taking template in Section 4.1. A room or video call with no other agenda for the full time slot.

### 2.3 Time

Plan ninety minutes for a standard exercise: ten minutes of setup, sixty minutes of scenario, and twenty minutes of debrief. A focused exercise on a single decision can run in forty-five minutes. Do not cut the debrief to make up time; the debrief is where the findings come from.

### 2.4 Output Artifacts

Every exercise produces an exercise record (Section 4.1) and a findings list with named owners and target dates. Findings that cannot be closed by their target date go to the risk register under POL-GOV-001. The record is retained with the incident response materials and treated with the same rigor as a real post-incident review, as POL-IR-001 Section 3.10 requires.

## 3. Procedure

### 3.1 Phase 1: Plan the Exercise (Two to Three Weeks Before)

**Pick the scenario.** Use the rotation in Section 5 so that every playbook in RUN-IR-001 is exercised over time. Choose a scenario from Section 3.4 or adapt one to the organization's environment. A scenario that could plausibly happen next month engages people more than an exotic one.

**Set two or three objectives.** Objectives are specific questions the exercise should answer, not topics. "Can we reach our cyber insurance carrier and know what they require before we call an outside firm?" is an objective. "Ransomware" is not. Good objectives come from recent incidents, last exercise's findings, changes in the environment, and anything nobody has tested.

**Tailor the injects.** Replace generic details with real ones: the actual email platform, a real vendor, the actual payroll date. Leave the identity of the people involved generic. Naming a real employee as the one who clicked the link is unkind and distracts from the exercise.

**Invite participants.** Send the date, the length, and a one-line description of what the exercise is. Do not send the scenario. Ask participants to bring whatever they would actually reach for during an incident, including their phones, because the contact list is part of what gets tested.

**Agree on the ground rules with the executive sponsor in advance**, particularly that the exercise is not an evaluation of individuals (Section 3.2).

### 3.2 Phase 2: Open the Exercise (Ten Minutes)

State the ground rules plainly:

This is a conversation, not a test, and nobody is being graded. Answer with what you would actually do today, not what the policy says you should do; the gap between the two is what we are here to find. "I don't know" is a useful answer. Decisions made here are not commitments. We stay in the scenario; side issues go on the parking lot list and get time at the end.

State the objectives and the time. Confirm who is playing which role. If someone who would matter in a real incident is absent, name who stands in for them.

### 3.3 Phase 3: Run the Scenario (Sixty Minutes)

The scenario unfolds in injects: short updates that move the situation forward. Present each inject, then ask the questions attached to it, then let the group work.

**Keep the time compressed.** One inject can represent minutes or days. Say so when time jumps: "It is now Tuesday morning, eighteen hours later."

**Ask, do not tell.** The facilitator's job is to ask the next question, not to supply the answer. The most useful questions are about specifics: Who exactly makes that call? How would you reach them at 2 a.m.? Where is that written down? What happens if that person is on a plane?

**Make people show, not say.** When someone says "we'd check the backups," ask them to open the backup console and tell the room when the last successful job ran. When someone says "we'd call the insurer," ask them to find the claims number now. Real lookups surface real gaps.

**Watch the clock on decisions.** Note how long each decision takes and whether the group knew who had the authority to make it. Unclear authority is the most common finding and the most valuable.

**Handle the common problems.** If one person dominates, ask a specific question of someone else by role. If the group goes off track, note the topic on the parking lot list and return to the inject. If the group finds the "right" answer instantly, add a complication: the person they called does not answer, the backup they planned to restore from is also encrypted, the vendor's support line has a four-hour wait.

**Record as you go.** The note-taker captures every decision, every "we don't know," every missing contact or permission, and every point where the group disagreed about who owns something.

### 3.4 Scenario Library

Each scenario lists its injects and the questions to ask at each. Use them as written or adapt them. Severity levels refer to POL-IR-001 Section 3.2.

#### 3.4.1 Account Compromise Leading to Payment Fraud

Tests RUN-IR-001 Section 3.2.1 and Section 3.2.3.

**Inject 1.** A vendor calls accounts payable to ask why this month's invoice was paid to a new bank account. Nobody at [ORGANIZATION_NAME] remembers changing it. *Questions:* Who takes this call, and who do they tell? Is this an incident? What severity?

**Inject 2.** The bank change request came by email from the controller's real mailbox two weeks ago. The controller says they never sent it. *Questions:* What happens to the controller's account right now, and who is allowed to do it? How do you talk to the controller about this without using the compromised mailbox?

**Inject 3.** Review of the mailbox shows a forwarding rule sending anything containing "invoice" or "payment" to an outside address, created three weeks ago. Sign-ins came from another country. The controller's MFA method list includes an authenticator app on a phone the controller does not own. *Questions:* What else did the attacker see? What other accounts and vendors need to be checked? How long until the money is unrecoverable, and who calls the bank?

**Inject 4.** Two more vendors received payment-change requests from the same mailbox. *Questions:* Who notifies the affected vendors? What does the cyber insurance policy require, and has anyone called the carrier? Does anything here create a notification obligation?

#### 3.4.2 Ransomware on a Friday Evening

Tests RUN-IR-001 Section 3.2.2 and the decision framework in Section 3.4.1.

**Inject 1.** At 6:40 p.m. on a Friday, the EDR platform alerts on ransomware behavior on a file server. The on-call contact is at dinner. *Questions:* Who is notified, and how? What can they do from their phone? What does the standing authority matrix allow without waking anyone else?

**Inject 2.** By 8:00 p.m., three more servers and twelve workstations show encrypted files. A ransom note demands payment within seventy-two hours and claims data was copied out first. *Questions:* Is this Critical? Who calls the executive sponsor? Who calls the insurer, and do they call before or after the incident response firm? Which systems get disconnected, and who decides?

**Inject 3.** The most recent backup of the file server is twenty-six hours old. The backup server shares administrator credentials with the domain. *Questions:* Can the backups be trusted? How do you find out without risking them? What is the restore order, and who decided it? How long until the business can operate, and does leadership agree with that number?

**Inject 4.** Monday morning: staff arrive, payroll runs Wednesday, and a client emails asking whether their data was involved. *Questions:* What do employees hear, and from whom? What does the client hear, and who approves it? Is payment being considered, and who is in that conversation? What reporting obligations might apply?

#### 3.4.3 Lost Laptop at an Airport

Tests RUN-IR-001 Section 3.2.4. A good scenario for a shorter exercise.

**Inject 1.** A sales manager texts from an airport: their laptop bag was taken while they were in line. The laptop was signed in. *Questions:* Who do they contact, and how do they know? What happens in the next thirty minutes?

**Inject 2.** The device management console shows the laptop last checked in four hours ago. Encryption status shows enabled. The laptop had a synced copy of a client's financial files. *Questions:* Does a remote wipe still work if the device never comes back online? What does encryption actually protect here? Is a client notification needed, and who decides?

**Inject 3.** The manager's security key was in the same bag. *Questions:* How do they sign in to anything for the rest of the trip? What recovery path exists, and has anyone tested it?

#### 3.4.4 Phishing Campaign Against the Whole Company

Tests RUN-IR-001 Section 3.2.5.

**Inject 1.** Several employees forward a message that looks like a shared-document notification from a known vendor. *Questions:* Who sees these reports, and how quickly? How do you find everyone who received it?

**Inject 2.** Sign-in logs show four users entered credentials on the linked page within the first hour. One is an IT administrator. *Questions:* What happens to those four accounts, in what order? Does the administrator's involvement change the severity?

**Inject 3.** One of the four accounts has already sent the same message to two hundred external contacts. *Questions:* Who tells those contacts, and what do you say? What happens to the organization's email reputation?

#### 3.4.5 A Vendor Breach You Learn About in the News

Tests POL-TPRM-001 Section 3.9 and the vendor coordination in POL-IR-001.

**Inject 1.** A news article reports that a SaaS vendor [ORGANIZATION_NAME] uses for client records was breached. The vendor has not contacted you. *Questions:* Is this an incident for [ORGANIZATION_NAME]? Who owns the vendor relationship? Where is the vendor's contact and the contract?

**Inject 2.** The vendor's statement says customer data "may have been accessed" and API tokens should be rotated. *Questions:* Which integrations use that vendor's tokens, and where are they in the non-human identity inventory? Who rotates them, and what breaks when they do?

**Inject 3.** A client asks whether their data was in that system. *Questions:* Can you answer from the asset and data inventories? What does the client contract require you to tell them, and when?

#### 3.4.6 The Departing Administrator

Tests insider risk, POL-IAM-001 Section 3.4, and the non-human identity controls in POL-IAM-003.

**Inject 1.** A systems administrator resigns with two weeks' notice after a dispute with their manager. *Questions:* What access do they have, and where is that list? What changes today versus on their last day? Who decides?

**Inject 2.** A week later, monitoring shows a large download from the file server by the administrator's account at 11 p.m. *Questions:* Is this an incident? Who can look at the activity, and who must be told before anyone confronts the employee? When does HR or counsel get involved?

**Inject 3.** After the last day, a scheduled task the administrator created starts failing, and a service account in their name is still signing in. *Questions:* What else did they create? How would you find it? What is the plan if one of those accounts turns out to be holding up payroll?

#### 3.4.7 A Voice Call From the CEO

Tests the impersonation and verification controls in POL-AI-001 Section 3.7 and RUN-IR-001 Section 3.2.3.

**Inject 1.** The finance lead receives a call that sounds exactly like the CEO, who is traveling. The caller asks for an urgent wire to close a confidential acquisition and says the lawyers will send details by email. *Questions:* What does the finance lead do right now? Is there a written rule for this? Would people actually follow it with the CEO's voice on the phone?

**Inject 2.** An email follows from a domain one letter different from the organization's, attaching what looks like a signed letter of intent. *Questions:* What would have caught this? Who is notified now? Is this an incident if no money moved?

### 3.5 Phase 4: Debrief (Twenty Minutes)

Stop the scenario with enough time left for the debrief. Ask three questions, in this order, and give each real time:

What went well? Start here. It is true more often than people expect, and it makes the next two questions easier to answer honestly.

What did we not know, not have, or not agree on? This is the main output. Push for specifics: a missing phone number is a finding; "communication could be better" is not.

What would we change, and who will do it by when? Each change gets a named owner and a target date before the meeting ends. A finding without an owner is a finding that will appear again next quarter.

Read back the findings list before people leave so that everyone hears the same version.

## 4. Analysis and Findings

### 4.1 The Exercise Record

The note-taker completes the record within two business days.

| | |
|---|---|
| **Exercise date** | |
| **Scenario** | |
| **Objectives** | |
| **Facilitator** | |
| **Participants (name and role)** | |
| **Roles not represented** | |
| **Duration** | |

**Decisions log**

| Inject | Decision | Who decided | Time taken | Authority clear (Yes / No) | Notes |
|---|---|---|---|---|---|
| 1 | | | | | |

**Findings**

| Finding ID | Finding | Category (People / Process / Technology / Contacts / Authority) | Owner | Target date | Status | Risk register entry (if not closed by target) |
|---|---|---|---|---|---|---|
| TT-001 | | | | | | |

**Parking lot** (issues raised but out of scope for this exercise)

**Objectives met?** For each objective, record whether the exercise answered it and what the answer was.

### 4.2 Writing Good Findings

A good finding names something specific enough to fix and check. "The cyber insurance claims number was not in the contact list, and nobody knew it" is a good finding. "Improve vendor communication" is not.

Group related findings rather than listing every symptom. If three injects stalled because nobody knew who could approve disconnecting servers, that is one finding about authority, not three.

Separate what the team did not know from what the organization does not have. Not knowing where the restore procedure lives is a training finding. Not having a restore procedure is a program finding.

### 4.3 Following Up

Findings are tracked to closure through the same process as post-incident review findings, under POL-IR-001 Section 3.10. The next exercise opens by reviewing the previous exercise's findings: what closed, what did not, and why. A finding that appears in two consecutive exercises goes to the executive sponsor.

Changes to RUN-IR-001, the contact list, or the standing authority matrix that come out of an exercise are made within thirty days, consistent with RUN-IR-001 Section 5.

## 5. Operational Cadence

POL-IR-001 Section 3.10 requires an exercise at least quarterly. The default rotation runs through the seven scenarios in Section 3.4 over about two years, with ransomware and account compromise repeated more often because they are the most likely and most damaging:

| Quarter | Scenario |
|---|---|
| Q1, year 1 | Account compromise leading to payment fraud (3.4.1) |
| Q2, year 1 | Ransomware on a Friday evening (3.4.2), with the executive sponsor |
| Q3, year 1 | Vendor breach (3.4.5) |
| Q4, year 1 | Phishing campaign (3.4.4) |
| Q1, year 2 | Departing administrator (3.4.6) |
| Q2, year 2 | Ransomware (3.4.2), varied, with the executive sponsor |
| Q3, year 2 | Voice call from the CEO (3.4.7) |
| Q4, year 2 | Lost laptop (3.4.3) and account compromise (3.4.1), as two short exercises |

Replace a scheduled scenario when something more relevant comes up: a real incident in a peer organization, a major change in the environment, or a finding that needs to be retested.

This runbook is reviewed semiannually. Scenarios are refreshed when the threats or the environment they assume have changed.

## 6. Automation Opportunities

Tabletop exercises are a conversation and should stay one, but the work around them can be lighter:

A recurring calendar series for the quarterly exercises, created once a year with the rotation above, so scheduling is not a quarterly negotiation. A shared findings tracker, or the organization's existing ticket system, so that exercise findings sit alongside post-incident and audit findings rather than in a document nobody reopens. A short participant survey after each exercise asking what was most useful and what felt unrealistic, to improve the next one.

## 7. References

### Related Documents in This Library

POL-IR-001: Incident Response Policy (the requirement for quarterly exercises, Section 3.10)
RUN-IR-001: Incident Response Runbook (the playbooks the scenarios test)
POL-GOV-001: Information Security Policy (risk register for findings that cannot be closed)
POL-TPRM-001: Third-Party Risk Management Policy (vendor incident coordination)
POL-IAM-001: Access Control Policy (departure and access removal)
POL-IAM-003: Non-Human Identity Governance Policy (service accounts and integrations)
POL-AI-001: AI and Agent Governance Policy (impersonation and verification)

### External Resources

CISA publishes free Tabletop Exercise Packages (CTEPs) covering many incident types, with situation manuals and facilitator guides that can be adapted to this format.

The Homeland Security Exercise and Evaluation Program (HSEEP) describes the exercise design and evaluation practices that this runbook simplifies for small organizations.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This runbook is issued under the authority of the executive sponsor named in POL-IR-001.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
