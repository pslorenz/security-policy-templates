# Adoption Guide

*What to adopt first, what to scale down, and what you may not need at all.*

---

## Start here

This library has forty documents. Almost no organization needs all of them on day one, and some organizations will never need a few of them. This guide provides basic advice as to which ones to adopt, in what order, and how far to take each one for an organization like yours. The end result however will be the policy that feeds your security program and should be modified to meet your organization's business needs and security goals. 

Read this entire document before you start customizing. It takes about fifteen minutes, and it will save you from spending a month on documents that matter less than the six that should have started with.

The guide assumes you have read the README and know the document types: policies (POL) state what the organization commits to, standards (STD) set the technical specifics, runbooks (RUN) describe how to do something, templates (TPL) produce the records that prove a control is running, and addenda (ADD) add requirements for a specific regulation. The client-facing explainers translate two of the policies for business owners.

## Step 1: Answer five questions

These five questions decide most of your scope. Answer them before choosing anything else.

| Question | If the answer is no | If the answer is yes |
|---|---|---|
| **1. Do you have an office network or on-premises servers?** | POL-NET-001 reduces to guest Wi-Fi and the filtering in STD-NET-001. Most of the physical sections of POL-PPS-001 fall away; keep clean desk, home office, and the personnel sections. | Adopt POL-NET-001 and POL-PPS-001 in full. Your directory and servers belong in STD-DR-001's recovery planning. |
| **2. Do you run anything reachable from the internet yourself?** (A VPN or remote desktop gateway, a file transfer server, a hosted site with logins, an exposed firewall management page.) | STD-VM-001 Baseline tier. | STD-VM-001 Standard tier at least. Close anything that does not need to be exposed before you schedule a penetration test. |
| **3. Do you write any code, including scripts and automations?** | Mark POL-DEV-001 "Not adopted." | Adopt POL-DEV-001 at the level that matches what you build (Section 2 of that policy). |
| **4. Do you handle regulated data?** (Health information, payment cards, Controlled Unclassified Information, NYDFS-covered financial data.) | Skip the addenda. | Adopt the matching addendum or framework notes, and move STD-DC-001 (DLP) and POL-PPS-001 earlier. |
| **5. Does an outside provider run your IT or security?** | Roles in each document map to internal staff. | Roles marked "IT function (or IT service provider)" map to the provider. Read the provider sections of POL-BC-001 Section 3.2, STD-OPS-001 Section 3.5, and POL-TPRM-001 early, because your dependence on that provider is a business risk in its own right. |

Write your answers down, or record them in Part 1 of the intake questionnaire (`docs/intake-questionnaire.md`), which collects them along with every other decision the documents need. They go in the scope notes of POL-GOV-001 and decide the testing tier in STD-VM-001 and the development level in POL-DEV-001.

## Step 2: Adopt in three waves

The waves are ordered by what reduces the most risk soonest and by what other documents depend on, not by document number. Each document lists what "adopted" means: the evidence that shows it is in place rather than just signed.

### Wave 1: Foundation (first 30 to 60 days)

These documents set up the program, establish what you have and what is happening to it, and cover the attacks most likely to hurt a small organization: stolen credentials, phishing and payment fraud, and ransomware.

Asset inventory and logging come first for a reason. Asset inventory is CIS Control 1 because everything else depends on it: you cannot enforce MFA on accounts you have not found, patch devices you do not know about, back up systems missing from the list, or monitor what was never connected to the logging platform. Logging is close behind because the native retention of many identity and email logs is days or weeks, and an incident discovered next month will need the logs from this month.

| Document | Adopted when |
|---|---|
| POL-GOV-001 Information Security Policy | Signed by the executive sponsor. The Information Security function is named. The suite table in Section 3.7 shows which documents are adopted, planned, or not adopted. |
| POL-AM-001 Asset Management Policy, with the SaaS inventory in STD-AM-001 Section 3.1 | A hardware, software, SaaS, and cloud inventory exists, built from automated sources (EDR, device management, the identity provider's device and application lists, network discovery, and expense records), and every asset has an owner. It will not be perfect yet; it needs to be good enough that the other Wave 1 documents know what they are protecting. |
| STD-LOG-001 Logging and Monitoring Standard, with TPL-LOG-001 | Identity provider, email, and EDR logs are exported to a store that keeps them for the required period, rather than relying on native retention. Alerts reach a person or provider who will act on them. The log source inventory lists what is collected and what is still missing. |
| POL-AUP-001 Acceptable Use Policy, with TPL-AUP-001 | Every user has acknowledged it and POL-GOV-001, recorded in the acknowledgment log, before receiving access. |
| POL-IAM-001 Access Control Policy | Every account has an owner. Administrators use separate accounts. Break-glass accounts exist and have been tested. |
| STD-IAM-001 Password and Authentication Standard | MFA is enforced for every user. Privileged accounts use phishing-resistant methods. |
| POL-IR-001 Incident Response Policy, with RUN-IR-001 | The contact list and out-of-band channel exist. The cyber insurance carrier's requirements are known. |
| STD-DR-001 Data Backup and Recovery Standard | Critical data has an immutable or offline copy. One restore has been tested. |
| STD-NET-001 Email and Web Browser Protection Standard | SPF, DKIM, and DMARC are published for every domain. External forwarding is blocked. Payment-change verification is in use by finance. |

If you do nothing else in the library, do these. The CIS IG1 checklist (`docs/cis-ig1-checklist.md`) shows which safeguards each wave meets. The asset inventory and the log sources will be incomplete at the end of Wave 1, and that is expected; Wave 2 closes the gaps through the quarterly reconciliation and the full log source list.

### Wave 2: Core program (first six months)

These documents turn the foundation into a program that runs on a schedule and can be shown to an auditor, insurer, or client.

| Document | Adopted when |
|---|---|
| POL-AM-001 and STD-AM-001, completed | The first quarterly reconciliation is done, unknown assets found in it are resolved, and Critical SaaS applications meet the STD-AM-001 onboarding and configuration baselines. |
| POL-EP-001 Endpoint Protection Policy | Every managed device has EDR, encryption, and the baseline. |
| POL-VM-001 Vulnerability Management Policy, with STD-VM-001 | Scanning is running. The testing tier is set and its first activities are scheduled. |
| POL-DC-001 Data Classification and Handling Policy | Data owners are named for the main data types. Users have been told the three levels. |
| POL-AI-001 AI and Agent Governance Policy, with TPL-AI-001 | The first AI inventory is done and the approved tools list is published. |
| POL-TPRM-001 Third-Party Risk Management Policy, with TPL-GOV-003 | Vendors are inventoried and tiered. Tier 1 vendors have been reviewed. |
| STD-LOG-001, completed | Every required log source in Section 3.1 is collected, the minimum alerts are configured, and the first monthly log review is done. |
| POL-IAM-003 Non-Human Identity Governance Policy, with RUN-IAM-001 and TPL-IAM-001 | The first discovery is done and every non-human identity has an owner. |
| TPL-IAM-002 Quarterly User Access Review | The first quarterly review is complete. |
| STD-OPS-001 Change Management Standard | Changes to identity, firewall, and security tools are recorded and approved. |
| POL-BC-001 Business Continuity Policy, with TPL-BC-001 | The plan exists, with an offline copy. |
| RUN-IR-002 Tabletop Exercise Facilitation Runbook | The first exercise has run and its findings have owners. |
| TPL-GOV-001, TPL-GOV-002, and TPL-GOV-004 | The risk register and exception register are in use, and the first quarterly metrics report has gone to the executive sponsor. |

### Wave 3: As applicable

Adopt these when the five questions or your obligations call for them.

| Document | Adopt when |
|---|---|
| POL-IAM-002 Remote Access Policy | Anyone reaches internal systems from outside the office. For an all-SaaS organization with no internal systems, a short version covering devices and conditional access is enough. |
| STD-IAM-002 Single Sign-On and Federation Standard | You use more than a handful of SaaS applications. This is most organizations, and it can move into Wave 2. |
| STD-DC-001 Data Loss Prevention Standard | You hold Restricted data. Start in monitoring mode. |
| STD-DC-002 Cryptography and Key Management Standard | Always worth adopting; the urgent parts are recovery key escrow and certificate automation. Required early where a contract demands validated cryptography. |
| POL-PPS-001 Physical and Personnel Security Policy | Always adopt the personnel sections. Adopt the physical sections in full if you have an office. |
| POL-DEV-001 Secure Development Policy | You write code, at the level in its Section 2. |
| STD-VM-001 Standard and Expanded tiers | Question 2 or your contracts call for them. |
| TPL-LOG-002 Immutable Archive Record | You use the immutable log archive pattern in STD-LOG-001. |
| ADD-CMMC-001 CMMC Level 2 Addendum | You handle CUI. In that case, it is Wave 1, and scoping comes first. |

## Step 3: Find your profile

These profiles describe common small-organization situations. Find the closest one and adjust. Where a profile says "scale down," the document still applies but only its relevant sections.

**Remote-first professional services firm, around 20 people, all SaaS.** No office network, no servers, nothing of its own on the internet, an outside IT provider. Adopt Waves 1 and 2. Scale down POL-NET-001 to filtering and POL-PPS-001 to home office, clean desk, and personnel. POL-IAM-002 can be short. STD-VM-001 Baseline tier. POL-DEV-001 at the scripts level only if anyone writes automations. The biggest risks are the identity provider and the email account of the person who that approves payments, so STD-IAM-001 and STD-NET-001 Section 3.9 deserve the most attention.

**Office-based firm, around 125 people, hybrid.** An on-premises LDAP, a file server, a remote access gateway, client financial records. Adopt everything except POL-DEV-001 (unless scripts are in use) and the addenda. STD-VM-001 Standard tier. STD-DR-001's directory recovery and the network segmentation in POL-NET-001 are where the effort goes. This is the profile the library fits most naturally.

**Healthcare-adjacent practice.** A clinic, dental or therapy practice, or a business associate handling health information. Follow the profile above that matches your size, and move STD-DC-001 and POL-PPS-001 into Wave 1, because health information is Restricted and physical access to records and workstations is a common gap. POL-PPS-001 includes the HIPAA sanction policy. The HIPAA Security Rule is under revision; build against the current rule, and check the framework mapping for its status. A HIPAA addendum is planned.

**Defense contractor handling CUI.** Start with ADD-CMMC-001 Section 2: define the CUI environment before adopting anything, because a smaller enclave is far cheaper to protect and assess. Then adopt Wave 1 and the documents the addendum's coverage table names for the enclave, with the addendum's overrides. Expect to need STD-DC-002 validated cryptography and POL-PPS-001 early. Validate the CMMC program status before relying on any date in the addendum.

**Financial services firm covered by NYDFS Part 500.** Adopt Waves 1 and 2 and STD-DC-001. The framework mapping lists the Part 500 requirements the library does not cover, including the CISO designation, annual certification, and Department notification timelines; build those around the library rather than inside it.

**Small software company.** Adopt POL-DEV-001 at the internet-facing level and STD-VM-001 at the Expanded tier, alongside Waves 1 and 2. Secrets in code and access to production are where small software companies are usually breached, so POL-DEV-001 Sections 3.2 and 3.7 belong in Wave 1.

**Nonprofit.** Usually the 20-person profile, with two additions: donor and beneficiary data deserve Confidential or Restricted classification under POL-DC-001, and grant agreements sometimes carry security terms that belong in the obligations listed in POL-GOV-001. Volunteers with system access are covered by the personnel sections of POL-PPS-001 and the access rules in POL-IAM-001 like anyone else.

**An MSP adopting the library for itself.** Adopt all of it. An MSP's breach quickly becomes every client's breach, so the Wave 3 documents are Wave 2 for you, and your clients' auditors and insurers will increasingly ask to see them. POL-IAM-003, STD-OPS-001, and the provider sections of POL-TPRM-001 and POL-BC-001 describe controls your clients will expect you to hold yourself to.

## Step 4: Customize

With your scope decided, follow the customization guide (`docs/customization-guide.md`) for the documents you are adopting. Mark the rest "Not adopted" or "Planned" in the POL-GOV-001 suite table rather than deleting them, so the decision is visible and revisited at the annual review.

When a document's requirement does not fit your organization, use the exception process in POL-GOV-001 Section 3.6 rather than editing the requirement out quietly. An exception with a reason and an expiration date is honest. A requirement that disappeared from the document is not.

## Maintaining the library across many organizations

For an MSP or vCISO adopting the library for many clients, the temptation is to fork a full copy per client. Resist it. Every fork has to be updated separately when the library changes, and they drift apart within a year.

Instead, keep one master copy customized to how you deliver services: your role mappings, your tools in the placeholders, your standard cadences. For each client, keep a short record of what differs: their answers to the five questions, their profile, their suite table, their testing tier and development level, and any client-specific values or exceptions. Generate the client's documents from the master and the record. `scripts/generate.py` does exactly this: the client record is its configuration file, and the customization guide describes it. When the library changes, update the master once and regenerate every client.

A client whose differences grow beyond a page probably needs its own copy. Most will not.

## When to revisit your scope

Revisit the five questions at each annual policy review, and whenever one of these happens: opening or closing an office; putting a new system on the internet; starting to write software or hiring a developer; winning a contract with security requirements, especially one involving CUI or health information; changing IT providers; or a significant incident. Each of these can move documents between waves or out of "Not adopted."

---

*Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution 4.0.*
