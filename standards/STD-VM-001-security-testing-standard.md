# STD-VM-001: Security Testing Standard

| | |
|---|---|
| **Document ID** | STD-VM-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This standard sets how much security testing [ORGANIZATION_NAME] does, scaled to its size and exposure. It extends POL-VM-001, which finds and fixes known vulnerabilities, with testing that checks whether the controls actually work and whether an attacker could get in.

Penetration testing is often treated as something every organization should buy every year. The CIS Controls disagree: Control 18 has no safeguards in Implementation Group 1, the baseline for small organizations with limited IT staff. A twenty-person firm that runs entirely on SaaS gets more from monthly scanning, an annual look at what it exposes to the internet, and a few simple checks that its controls fire than from a penetration test of infrastructure it does not have. A 125-person firm with servers, an on-premises directory, a remote access gateway, and client financial data is in a different position; an outside tester will find things its own staff cannot see.

This standard sets a baseline every organization does, and two higher tiers triggered by what the organization runs and what it is responsible for, rather than by headcount alone.

## 2. Scope

This standard applies to security testing of [ORGANIZATION_NAME]'s own systems, identity provider, cloud tenants, networks, and applications. It does not authorize testing of systems [ORGANIZATION_NAME] does not own; SaaS applications and cloud platforms are tested only within the limits their providers publish or approve.

## 3. Standard Requirements

### 3.1 Choosing the Testing Tier

[ORGANIZATION_NAME]'s testing tier is set by the first row whose conditions apply, and recorded here: [TESTING_TIER, e.g., Baseline].

| Tier | Applies when any of these is true | Typical example |
|---|---|---|
| Expanded | [ORGANIZATION_NAME] builds internet-facing applications that handle Confidential or Restricted data (POL-DEV-001). A framework or contract requires internal or segmentation testing. A significant incident occurred in the past year. The organization targets CIS Implementation Group 3. | A firm with a client portal it built and hosts, or one handling payment card data in its own environment |
| Standard | [ORGANIZATION_NAME] runs internet-facing systems of its own, such as a VPN or remote desktop gateway, a file transfer server, a hosted website with logins, or an exposed firewall management interface. It runs an on-premises directory or servers. It holds Confidential or Restricted data under regulation or client contract. A client contract, cyber insurer, or regulator requires penetration testing. The organization targets CIS Implementation Group 2. | A 125-person firm with an on-premises directory, a remote access gateway, and client financial records |
| Baseline | None of the above. | A twenty-person firm whose systems are SaaS applications and managed laptops, with nothing of its own reachable from the internet |

Headcount is a weak proxy, so the tier follows exposure. A ten-person firm with a remote desktop gateway open to the internet belongs at Standard. A two-hundred-person firm that has moved everything to SaaS and closed its last exposed service can sit at Baseline, though at that size the configuration of its identity provider and productivity tenant carries most of its risk, and an outside review of them (Section 3.3) is usually worth the cost.

The tier is reviewed annually and whenever the conditions change, such as opening a new internet-facing service or signing a contract that requires testing.

### 3.2 Baseline Testing (Every Organization)

**External vulnerability scanning**, at least monthly, under POL-VM-001 Section 3.1.

**An annual external exposure review.** List everything reachable from the internet under [ORGANIZATION_NAME]'s domains and network addresses: DNS records, open ports, login pages, administrative interfaces, and file shares. Compare the list with what is supposed to be exposed, and close or justify everything else. Dangling DNS records found here are removed under STD-AM-001 Section 3.10.

**An annual configuration review** of the identity provider and the productivity platform against the vendor's published security baseline or the relevant CIS Benchmark. For most small organizations this tenant is the most valuable target an attacker can reach, and its configuration matters more than any server.

**Quarterly control checks.** Simple, safe tests that confirm key controls still work, recorded with the date and result:

A harmless anti-malware test file on a managed endpoint generates an EDR alert, and the alert reaches the monitoring provider under STD-LOG-001. A sign-in attempt using a blocked legacy authentication protocol is refused. Automatic forwarding to an external address is blocked under STD-NET-001 Section 3.7. A sign-in from a blocked country or an unmanaged device is handled as POL-IAM-002 Section 3.3 requires. A file is restored from backup under STD-DR-001 Section 3.7.

**People and process testing**, through the phishing simulations in POL-GOV-001 Section 3.8 and the tabletop exercises in RUN-IR-002.

### 3.3 Standard Testing

Everything in the Baseline tier, plus:

**An annual external penetration test** by a qualified, independent tester. The scope covers every internet-facing system [ORGANIZATION_NAME] runs and the external attack surface of the identity provider: password spraying resistance, multi-factor authentication gaps, legacy protocols, and exposed administrative portals.

**A test after significant change** to internet-facing systems, such as a new remote access gateway or a newly exposed application, before or soon after it goes live.

**An identity and tenant configuration review by an outside reviewer** at least every other year, alternating with the annual internal review in Section 3.2.

**An internal or assumed-breach test at least every other year** where [ORGANIZATION_NAME] runs an on-premises directory. The tester starts as an ordinary user on a managed laptop and tries to reach administrative control, which tests segmentation, privileged access, and detection together.

### 3.4 Expanded Testing

Everything in the Standard tier, plus:

**An annual internal penetration test** in place of the every-other-year test in Section 3.3.

**Application penetration testing** for internet-facing applications that handle Confidential or Restricted data, before first release and at least annually, under POL-DEV-001 Section 3.6.

**Segmentation testing** where a framework or contract requires it, at the frequency it requires.

**Detection validation.** At least annually, techniques from a recent test are replayed with the monitoring provider watching, to confirm that the activity is detected and escalated, and detection gaps are fixed. This validates the security measures based on what testing found.

### 3.5 Running a Test

Every penetration test or outside review has a written scope and rules of engagement, approved by the executive sponsor before testing begins, covering the systems in and out of scope, the testing window, techniques that are not permitted (such as denial of service or social engineering, unless explicitly included), how sensitive data found during testing is handled, and an emergency contact on each side who can stop the test.

Testers are independent of the people who built and run the systems being tested. The monitoring provider and IT service provider are told a test is happening, but not every detail, so that the test also shows what monitoring catches. Where the cyber insurance policy or a client contract has notification requirements for testing, they are followed.

Testers are selected for demonstrated experience with environments like [ORGANIZATION_NAME]'s, recognized penetration testing qualifications, professional liability insurance, and references. Test reports and findings are classified Restricted under POL-DC-001.

### 3.6 Findings

Findings from any test or review are rated and remediated under the priority tiers and cadences in POL-VM-001 Sections 3.2 and 3.3. Critical and High findings are retested once fixed, by the original tester where possible. Findings that cannot be remediated within the cadence go through the exception process or to the risk register under POL-GOV-001.

The executive sponsor receives a summary of each test: what was tested, what was found, and what is being done about it. A finding that appears in two consecutive tests is escalated, because it means the first fix did not work.

### 3.7 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Sets the testing tier. Scopes tests, selects testers, and tracks findings.

**IT function (or IT service provider).** Runs the Baseline control checks. Supports testing. Remediates findings.

**Executive sponsor.** Approves the testing tier, the scope and rules of engagement for each test, and the budget. Receives test summaries.

**System owners.** Agree testing windows for their systems and accept the risk of findings they cannot remediate within the cadence.

## 5. Enforcement

Specific remediation timelines:

Testing tier not set or not reviewed in the last year: set within thirty days. Baseline control check failing: investigated within five business days and fixed on the POL-VM-001 cadence for its priority. Annual penetration test missed at the Standard or Expanded tier: completed within ninety days and reported to the executive sponsor. Exposed services found that are not supposed to be exposed: closed within seven days or approved as an exception.

## 6. Related Documents

POL-VM-001: Vulnerability Management Policy (the parent policy, scanning, and remediation cadences)
POL-DEV-001: Secure Development Policy (application testing)
STD-AM-001: SaaS Asset Management Standard (dangling DNS and retired services)
STD-DR-001: Data Backup and Recovery Standard (restore testing)
STD-NET-001: Email and Web Browser Protection Standard (forwarding controls)
POL-IAM-002: Remote Access Policy (conditional access rules)
STD-LOG-001: Logging and Monitoring Standard (detection and monitoring)
RUN-IR-002: Tabletop Exercise Facilitation Runbook (process testing)
POL-DC-001: Data Classification and Handling Policy (classification of test reports)
POL-GOV-001: Information Security Policy (phishing simulations, risk register, and exceptions)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

ID.RA-01 (Vulnerabilities in assets are identified, validated, and recorded). ID.IM-02 (Improvements are identified from security tests and exercises, including those done in coordination with suppliers and relevant third parties). DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events), through the control checks.

**CIS Controls v8.1:**

Control 18 Penetration Testing, by tier: Safeguards 18.1 (establish and maintain a penetration testing program), 18.2 (perform periodic external penetration tests), and 18.3 (remediate penetration test findings) at the Standard tier; 18.4 (validate security measures) and 18.5 (perform periodic internal penetration tests) at the Expanded tier. Control 18 has no Implementation Group 1 safeguards; the Baseline tier substitutes the control checks in Section 3.2.

Control 7 Continuous Vulnerability Management: Safeguard 7.6 (perform automated vulnerability scans of externally-exposed enterprise assets), through Section 3.2.

Control 4 Secure Configuration of Enterprise Assets and Software: Safeguard 4.1 (establish and maintain a secure configuration process), through the configuration review in Section 3.2.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
