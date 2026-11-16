# POL-BC-001: Business Continuity Policy

| | |
|---|---|
| **Document ID** | POL-BC-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy establishes how [ORGANIZATION_NAME] keeps operating when something important stops working: the office, a key system, a key person, or a vendor the business depends on.

STD-DR-001 restores data and systems. That is necessary but not sufficient. A business with perfect backups can still stall for a week because nobody knows who decides to send staff home, the only person with the payroll login is in the hospital, or the internet connection to the office has been down since the storm. Continuity planning is about the business functions, the people who run them, and the workarounds that keep them going while the systems come back.

For a small organization, the plan fits in a few pages. The value is in having thought it through once, written down who decides, and checked that the obvious single points of failure have a fallback.

## 2. Scope

This policy applies to the business functions [ORGANIZATION_NAME] must keep performing, and to the people, systems, vendors, and facilities those functions depend on. It covers disruptions from any cause, including cyber incidents, power and internet outages, severe weather, loss of a facility, illness or departure of key people, and failure of a vendor.

When a disruption is caused by a security incident, POL-IR-001 governs the response to the incident and this policy governs keeping the business running while that response proceeds.

## 3. Policy Statements

### 3.1 Critical Business Functions

[ORGANIZATION_NAME] identifies the business functions it must keep performing, such as serving clients, billing, payroll, and any regulated or contractual obligations. For each, the business owner records:

The function and its owner. The maximum tolerable downtime: how long the function can stop before the harm to clients, revenue, legal standing, or reputation becomes unacceptable. The dependencies: the systems (from the asset inventory in POL-AM-001), people, vendors, and facilities it needs. The workaround: how the function continues, even in a reduced form, when a dependency is lost.

The recovery objectives in STD-DR-001 Section 3.1 are set so that the systems behind each function come back within its maximum tolerable downtime. Where they cannot, the gap is funded, covered by a workaround, or accepted as a risk under POL-GOV-001 Section 3.5.

The functions and their details are recorded in the continuity plan (TPL-BC-001) and reviewed annually.

### 3.2 Plan for the Loss, Not the Cause

The plan addresses five kinds of loss. The cause matters less than what is unavailable, and planning by loss keeps the plan short.

**Loss of the office.** Staff work from home or an alternate location. The plan records which functions can run remotely today, which need equipment or access that is only in the office, and how to close that gap.

**Loss of a key system or SaaS application.** The function falls back to its documented workaround while the system is restored under STD-DR-001. The plan records the manual process and any information needed to run it, such as a recent client list or schedule kept where it can be reached without the system.

**Loss of key people.** No business function, credential, or relationship depends on a single person. For each critical function, at least one other person can perform it, even slowly. Credentials held by one person are stored in the organization's vault with documented access for a named successor. The owner, the sole IT administrator, and the only person who runs payroll are the usual cases.

**Loss of a key vendor.** For each vendor a critical function depends on, the plan records what happens if that vendor is unavailable for a day, a week, or permanently. For the IT or security service provider in particular, [ORGANIZATION_NAME] holds its own break-glass credentials to its identity provider and core platforms under POL-IAM-001 Section 3.7, owns the documentation of its environment, and has contract terms that require the provider to support a transition to another provider.

**Loss of power or internet.** Any location that must keep operating has a second internet connection, which can be a cellular backup, and power protection for the network equipment that connection needs.

### 3.3 Who Decides

The continuity lead, [CONTINUITY_LEAD], declares a continuity event, activates the plan, and decides when normal operations resume. The deputy, [CONTINUITY_DEPUTY], acts when the lead is unavailable. If neither can be reached within [CONTINUITY_ESCALATION_TIME, e.g., two hours] of a disruption to a critical function, the most senior available manager acts.

Decisions that affect staff safety, such as closing an office or sending people home, are made immediately by whoever is present and reported to the continuity lead afterward. Safety comes before continuity.

### 3.4 Communications

Staff are reached through the out-of-band channel established under POL-IR-001 Section 3.6, which does not depend on the company's email or chat. The plan holds a current staff contact list, available offline.

Clients, vendors, and other outside parties are told what they need to know, when they need to know it, by the people named in the plan. Messages about a disruption caused by a security incident follow the external communication rules in POL-IR-001 Section 3.6. Short message templates for staff, clients, and vendors are kept in the plan so that the first message does not have to be written under pressure.

### 3.5 The Continuity Plan

The plan is written using TPL-BC-001. It is short enough to read in a crisis, with an offline copy kept alongside the incident response materials described in RUN-IR-001 Section 2.1, and a copy available to the continuity lead and deputy outside the office.

The plan is updated within thirty days after a significant change: a new office, a new critical system or vendor, a change of IT provider, or the departure of a person named in it.

### 3.6 Testing

The plan is tested at least annually. One quarterly tabletop exercise each year under RUN-IR-002 uses a continuity scenario rather than a cyber one, such as a loss of the office, a key vendor, or a key person. A walkthrough also confirms that contact lists, offline copies, break-glass credentials, and the backup internet connection still work.

Findings are tracked to closure with owners and target dates, like exercise findings under POL-IR-001 Section 3.10.

### 3.7 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6.

## 4. Roles and Responsibilities

**Executive sponsor.** Approves this policy and the continuity plan. Funds the fallbacks the plan requires, or accepts the risk.

**Continuity lead and deputy.** Maintain the plan. Declare and manage continuity events.

**Business function owners.** Identify their critical functions, maximum tolerable downtime, dependencies, and workarounds. Make sure someone else can perform their function.

**IT function (or IT service provider).** Maintains the technical fallbacks: backup internet, remote access, break-glass credentials. Supports transition if the provider relationship ends.

**All staff.** Know how they will be contacted in a disruption. Keep their contact details current.

## 5. Enforcement

Specific remediation timelines:

Critical function with no documented workaround: workaround documented within sixty days. Credential or function dependent on a single person: successor access or a trained backup in place within sixty days. Annual test missed: completed within ninety days. Plan not updated after a significant change: updated within thirty days.

## 6. Related Documents

TPL-BC-001: Business Continuity Plan (the plan this policy requires)
STD-DR-001: Data Backup and Recovery Standard (restoring systems and data)
POL-IR-001: Incident Response Policy (cyber incidents and communications)
RUN-IR-001: Incident Response Runbook (contact list and offline materials)
RUN-IR-002: Tabletop Exercise Facilitation Runbook (continuity exercises)
POL-AM-001: Asset Management Policy (systems and their criticality)
POL-IAM-001: Access Control Policy (break-glass accounts)
POL-TPRM-001: Third-Party Risk Management Policy (vendor dependencies and transition terms)
POL-GOV-001: Information Security Policy (risk acceptance and exceptions)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

GV.OC-04 (Critical objectives, capabilities, and services that external stakeholders depend on or expect from the organization are understood and communicated). GV.OC-05 (Outcomes, capabilities, and services that the organization depends on are understood and communicated). PR.IR-03 (Mechanisms are implemented to achieve resilience requirements in normal and adverse situations). RC.RP-04 (Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms). RC.CO-03 (Recovery activities and progress in restoring operational capabilities are communicated to designated internal and external stakeholders).

**CIS Controls v8.1:**

The CIS Controls do not include business continuity planning. This policy complements Control 11 (Data Recovery), covered by STD-DR-001.

**Other frameworks:**

NYDFS 23 NYCRR 500.16 (business continuity and disaster recovery planning). SOC 2 A1.2 and A1.3, for organizations reporting on the Availability criteria.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
