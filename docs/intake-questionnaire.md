# Intake Questionnaire

*The decisions needed to customize the library for one organization, in plain language.*

---

## How to use this questionnaire

Copy this file for each organization, fill in the Answer column, and turn it into a configuration file for the generator:

```bash
cp docs/intake-questionnaire.md clients/acme-intake.md
python3 scripts/intake.py clients/acme-intake.md --out clients/acme.toml
python3 scripts/generate.py clients/acme.toml
```

Each section says who usually answers it. Most organizations need about an hour with the owner and an hour with whoever runs IT.

**Answers go into the documents word for word.** The "How your answer is used" column shows a sentence from the library with ___ where the answer goes. Write an answer that completes that sentence naturally. The Example column shows the kind of answer that fits.

**Leave a question blank if you do not know yet.** The generator lists every unanswered question for the documents you are adopting, so nothing is missed. Questions in sections that do not apply to you, such as the CUI section, can stay blank.

This questionnaire is generated from `placeholders.toml`. To change a question, edit the registry and run `python3 scripts/generate.py --update-guide`.

---

## Part 1: Scope

These answers decide which documents apply. The adoption guide (`docs/adoption-guide.md`) explains each one.

| Key | Question | Choices | Answer |
|---|---|---|---|
| `scope.office_network` | Do you have an office network or on-premises servers? | yes / no | |
| `scope.self_hosted_internet_services` | Do you run anything reachable from the internet yourself, such as a VPN or remote desktop gateway, a file transfer server, or a hosted site with logins? | yes / no | |
| `scope.writes_code` | Does anyone write code for the organization, including scripts and automations? If so, what kind? | none / scripts / internal / internet-facing | |
| `scope.regulated_data` | Do you handle any of these regulated kinds of data? | none, or any of: cui, health, payment-card, nydfs | |
| `scope.it_provider` | Does an outside provider run your IT or security? | yes / no | |
| `documents` | Are there any documents you are not adopting yet, or not adopting at all? List each as ID: Planned or ID: Not adopted, separated by semicolons. | for example, STD-DC-001: Planned; TPL-LOG-002: Not adopted | |

## Part 2: Details

### 2.1 Your organization

*Usually answered by the owner or executive sponsor.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `ORGANIZATION_NAME` | What is your organization's legal or trading name, as it should appear in the documents? | This policy defines how ___ approves, connects, and oversees artificial intelligence tools, including AI features built into software the organization already uses and AI agents that take actions on someone's behalf. |  | |
| `EFFECTIVE_DATE` | On what date should the documents take effect? (YYYY-MM-DD) | Date the adopted documents take effect (YYYY-MM-DD) |  | |
| `APPLICABLE_OBLIGATIONS` | Which laws, regulations, contracts, or insurance requirements impose security obligations on you? List each one. | The current list of applicable obligations is ___. | state breach notification law, HIPAA, PCI DSS, client contractual requirements, cyber insurance requirements | |
| `RISK_APPETITE_STATEMENT` | In two or three sentences, how much risk is the organization willing to accept, and where is it least willing? | The executive sponsor's risk appetite statement | "your organization does not accept residual risks rated Critical. High residual risks are accepted only with a funded treatment plan and an expiration date." | |

### 2.2 Leadership and roles

*Usually answered by the owner or executive sponsor.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `EXECUTIVE_SPONSOR` | Which executive approves these documents and owns the security program? (Name and title.) | Executive who approves the documents and owns the program |  | |
| `POLICY_OWNER` | Who maintains these documents day to day? (Name or role.) | Person or role that owns the documents |  | |
| `CONTINUITY_LEAD` | Who declares and manages a business disruption, such as losing the office or a key system? (Name and title.) | The continuity lead, ___, declares a continuity event, activates the plan, and decides when normal operations resume. |  | |
| `CONTINUITY_DEPUTY` | Who acts for the continuity lead when they cannot be reached? (Name and title.) | The deputy, ___, acts when the lead is unavailable. |  | |
| `CONTINUITY_ESCALATION_TIME` | If neither the continuity lead nor the deputy can be reached, how long should staff wait before the most senior available manager takes over? | If neither can be reached within ___ of a disruption to a critical function, the most senior available manager acts. | two hours | |
| `INFORMATION_SECURITY_FUNCTION` | Who performs the Information Security function: an internal person or role, an outside provider, or both? | At your organization, this function is performed by ___. | a named internal role, or the designated security service provider | |
| `ORGANIZATION_GOVERNANCE_BODY` | Who does the executive sponsor report to on security: owners, a board, partners, or no one? | A violation by a senior leader is handled through the same process as any other violation, with escalation to the executive sponsor or, where the executive sponsor is involved, to ___. | ownership or board | |

### 2.3 People and policies

*Usually answered by operations or HR.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `AI_TOOL_REQUEST_CHANNEL` | How should staff ask for a new AI tool to be approved? | Users request new AI tools through ___. | the standard software request process | |
| `ANNUAL_ACKNOWLEDGMENT_MONTH` | In which month each year should everyone re-acknowledge the policies? | Before access is granted, every year by ___, and within thirty days after a material change to either policy. | January | |
| `CONTRACT_REVIEW_PROCESS` | How are contracts with vendors reviewed before signing? | ___: The organization's standard contract review process |  | |
| `MEETING_RECORD_RETENTION` | How long should meeting recordings, transcripts, and AI summaries be kept? | Transcripts and summaries are Confidential by default and are retained for ___ unless a business or legal need requires longer. | ninety days | |
| `REPORTING_CHANNEL` | Where should staff report a security problem, such as a suspicious email or a lost device? | Reporting goes to the IT or Information Security function through ___. | a dedicated email address, a helpdesk ticket, a dedicated chat channel | |
| `REPORT_PHISHING_PROCESS` | How do staff report a suspected phishing email? | The reporting process should be made simple (___). |  | |
| `SCREENING_PROCESS` | Where is your process for screening new hires before they get access documented? (Your HR provider can usually answer this.) | ...your organization defines its screening process with counsel or its HR provider, records it in ___, and applies the same process to contractors with comparable access, either directly or by contract with t... |  | |
| `VISITOR_LOG_RETENTION` | How long should you keep records of office visitors? | Visitor records are kept for ___. | one year | |

### 2.4 Finance and payments

*Usually answered by finance.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `PAYMENT_APPROVAL_THRESHOLD` | Above what payment amount should two people approve before money moves? | Payments above ___ require approval from two people. |  | |
| `PAYMENT_HANDLING_PROCESS` | Where is your process for handling card payments documented, if you take them? | your organization's payment handling approach is documented in ___. |  | |
| `PAYMENT_INCIDENT_THRESHOLD` | If a vendor's bank details are changed without the required callback, above what payment amount is that treated as a security incident? (Often the same as the approval threshold.) | ...at was not verified is handled as a security incident under POL-IR-001 when any of these is true: money above ___ was sent to the new details; the request came from a lookalike domain, a mailbox that may be compromised, ... | the dual-approval threshold | |

### 2.5 IT and security tools

*Usually answered by the IT lead or IT provider.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `APPROVED_AI_TOOLS` | Which AI tools are approved for company data, and for which kinds of data? | Approved AI tools are ___. | business or enterprise tiers of AI assistants covered by a data protection agreement, and AI features of the approved productivity platform | |
| `APPROVED_BROWSERS` | Which web browsers are approved? | Approved browsers are ___. | one or two current mainstream browsers that support centralized management through the device management platform | |
| `APPROVED_DNS_FILTERING` | Which service blocks known-malicious websites, on and off the office network? | Approved DNS filtering services include ___. | a protective DNS service that blocks known-malicious domains and logs queries per device | |
| `APPROVED_EDR_PLATFORMS` | Which endpoint detection and response (EDR) service protects your computers? | Approved EDR platforms for your organization are ___. | an EDR platform with behavioral detection, tamper protection, remote isolation, and telemetry export to the central logging platform | |
| `APPROVED_FIREWALL_VENDORS` | Which firewalls protect your office network, if you have one? | Approved firewalls for your organization are ___. | a business-class firewall with intrusion prevention, centralized management, and a published firmware support lifecycle | |
| `APPROVED_IDP` | Which service do people sign in with for email and business applications? | your organization's approved identity provider is ___. | the identity service of the organization's primary productivity platform, or a standalone identity provider that supports SAML 2.0, OpenID Connect, and SCIM | |
| `APPROVED_MDM_PLATFORMS` | Which service manages your laptops and phones? | Approved MDM platforms are ___. | the device management service of the approved productivity platform, or a dedicated MDM that supports the organization's device mix | |
| `APPROVED_PASSWORD_MANAGERS` | Which password manager do staff use? | Approved password managers for your organization are ___. | a business password manager with shared vaults, administrator recovery, and phishing-resistant sign-in | |
| `APPROVED_REMOTE_ACCESS_TOOLS` | How do people reach internal systems from outside the office, if there are any internal systems? | Approved tools for your organization are ___. | an identity-gated access service that integrates with the approved identity provider and enforces per-application access rules | |
| `APPROVED_SECRETS_PLATFORMS` | Where are passwords and keys for service accounts and integrations stored? | Approved platforms for your organization are ___. | a cloud platform's key vault, a dedicated secrets manager, or the secrets feature of the approved password manager | |
| `APPROVED_STORAGE_PLATFORMS` | Where may company files be stored? | Approved storage at your organization includes ___. | the file storage and collaboration services of the approved productivity platform, approved file servers, and approved SaaS applications | |
| `APPROVED_VENDOR_MONITORING` | How do you hear about security problems at your vendors? | Approved services are ___. | a security ratings or vendor breach monitoring service where the value justifies the cost; smaller environments may rely on news monitoring and direct vendor communication | |
| `APPROVED_VM_TOOLS` | Which tools find missing patches and vulnerabilities? | Approved vulnerability management tools for your organization are ___. | the EDR platform's vulnerability assessment, an authenticated internal scanner, and an external attack surface scanner | |
| `CHANGE_RECORD_RETENTION` | How long are change records kept? | Records are retained for at least ___. | two years | |
| `CHANGE_RECORD_SYSTEM` | Where are changes to systems recorded? | Every change, of every type, is recorded in ___. | the IT ticket system or a shared change log | |
| `CHANGE_WINDOW` | When are higher-risk changes scheduled? | Higher-risk normal changes are scheduled in ___, and affected users are told in advance. | an agreed after-hours window | |
| `DMARC_ENFORCEMENT_TIMELINE` | How long do you expect it to take to fully enforce email authentication (DMARC) on your domains? | A reasonable target is reaching p=reject within ___ of adoption. | about six months | |
| `TESTING_TIER` | Which security testing tier applies: Baseline, Standard, or Expanded? (The scope answers in Part 1 usually decide this; see STD-VM-001 Section 3.1.) | Active at tier ___ | Baseline | |
| `VULNERABILITY_DISCLOSURE_CHANNEL` | Where should outside researchers report security problems they find in your systems? | External vulnerability reports are received through ___. | a security@ address at the organization's domain, a dedicated form, a bug bounty platform if one is in place | |

### 2.6 Monitoring and logging

*Usually answered by the IT lead or IT provider.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `ARCHIVE_RESTORE_TIME` | How quickly can archived logs be restored for an investigation? | Logs older than ninety days may move to lower-cost archive storage, provided they can be restored for investigation within ___. | two business days | |
| `CENTRAL_LOGGING_PLATFORM` | Where are security logs collected and kept? | The approved central logging platform for your organization is ___. | a cloud-native SIEM, a managed SIEM service, or the SIEM operated by the designated security service provider | |
| `LOG_TIME_ZONE` | Which time zone should all log timestamps use? (UTC is recommended.) | The central logging platform normalizes timestamps to a single time zone, ___. | UTC | |
| `MONITORING_COVERAGE` | During which hours are alerts watched, and what happens outside those hours? | Monitoring is performed by ... with ___. | 24x7 coverage, or business-hours coverage with automated containment outside business hours | |
| `MONITORING_PROVIDER` | Who watches security alerts and responds to them? | Monitoring is performed by ___ with .... | the Information Security function, or the designated MDR/SOC provider | |
| `TIME_SOURCE` | Where do your systems get their time from? | On-premises systems synchronize to ___. | the domain hierarchy, with the PDC emulator synchronized to two or more public NTP sources | |
| `VALIDATION_PERIOD` | How long should a new log source be watched for gaps before it is relied on? | The policy is created unlocked, log delivery is verified for every source over at least ___, and the policy is then locked. | seven days | |

### 2.7 Backup, recovery, and continuity

*Usually answered by the owner, with the IT lead or IT provider.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `CRITICAL_RPO` | For your most critical systems, how much data, measured in time, could you afford to lose? | Default recovery point objective for Critical systems | 24 hours | |
| `CRITICAL_RTO` | For your most critical systems, how long could the business operate without them? | Default recovery time objective for Critical systems | 72 hours | |
| `DAILY_RETENTION` | How long should daily backups be kept? | How long daily backups are kept | 30 days | |
| `IMPORTANT_RPO` | For important but not critical systems, how much data, measured in time, could you afford to lose? | Default recovery point objective for Important systems | 24 hours | |
| `IMPORTANT_RTO` | For important but not critical systems, how long could the business operate without them? | Default recovery time objective for Important systems | 7 days | |
| `MONTHLY_RETENTION` | How long should monthly backups be kept? | How long monthly backups are kept | 12 months | |
| `STANDARD_RPO` | For everything else, how much data, measured in time, could you afford to lose? | Default recovery point objective for Standard systems | 7 days | |
| `WEEKLY_RETENTION` | How long should weekly backups be kept? | How long weekly backups are kept | 12 weeks | |

### 2.8 Incidents and outside help

*Usually answered by the owner or executive sponsor.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `CYBER_INSURANCE_DOCUMENTATION` | Where are your cyber insurance policy and the insurer's claims contact kept? | The current carrier and policy details are documented in ___. |  | |
| `INCIDENT_RESPONSE_RETAINER_FIRM` | Which incident response firm would you call for a serious incident? (Check your cyber insurance policy first; many require a firm from the insurer's panel.) | The current retainer is with ___. | an incident response firm on the cyber insurance carrier's approved panel, or a regional firm the carrier has pre-approved | |
| `SECURITY_LEGAL_COUNSEL` | Which lawyer or firm advises you on security incidents and breach notification? | The current legal counsel for security matters is ___. |  | |

### 2.9 Defense contracts with CUI (skip unless you handle CUI)

*Usually answered by the owner, with the IT lead.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `CUI_PASSWORD_COMPLEXITY` | What password complexity rule applies to accounts in the CUI environment? | For accounts in the CUI environment, passwords meet ___, and the last ... passwords cannot be reused. | at least one change of character type from the previous password and the fifteen-character minimum in STD-IAM-001 | |
| `CUI_PASSWORD_HISTORY` | How many previous passwords may not be reused in the CUI environment? | For accounts in the CUI environment, passwords meet ..., and the last ___ passwords cannot be reused. | twenty-four | |
| `CUI_SCOPE_DOCUMENT` | Where is the scope of your CUI environment documented? | The CUI environment defined in ___ |  | |
| `CUI_SCREENING_PROCESS` | What additional screening applies before someone gets access to CUI? | People are screened before they are given access to the CUI environment under POL-PPS-001 Section 3.6, using ___ where CUI access calls for more than the role's standard screening (3.9.1). |  | |

### 2.10 Business owner explainers (optional)

*Usually answered by whoever presents the program to leadership.*

| Key | Question | How your answer is used | Example | Answer |
|---|---|---|---|---|
| `ESTIMATED_PROGRAM_COST` | What is the estimated first-year cost of the program, for the business owner explainers? | Replace bracketed placeholders (___, ...) with values appropriate to the adopting environment. |  | |
| `TIMELINE_WEEKS` | How many weeks will initial setup take, for the business owner explainers? | Replace ___ with a value appropriate to the adopting environment. |  | |

---

*Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution 4.0.*
