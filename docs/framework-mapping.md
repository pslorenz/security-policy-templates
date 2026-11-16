# Framework Mapping

How this library's content aligns to CIS Controls v8.1 and NIST Cybersecurity Framework 2.0. The mapping serves three purposes: it lets adopters confirm coverage of the controls their organization needs, it provides the audit-defensibility of explicit framework references, and it documents the rationale for the library's structural choices.

The mapping reflects the library as prepared for the v0.2.0 release, including POL-GOV-001 and STD-LOG-001, and cites CIS Controls v8.1. As new content is added in subsequent releases, this document is updated to reflect the expanded coverage.

---

## The library's framework alignment philosophy

The library aligns to two frameworks by default: CIS Controls v8.1 and NIST Cybersecurity Framework 2.0. The reasoning behind these specific choices is worth stating explicitly.

CIS Controls v8.1 provides specific, prescriptive safeguards organized into implementation groups appropriate to organizations of different sizes. Implementation Group 1 (IG1) is the minimum baseline for any organization with basic IT capabilities. IG2 adds safeguards appropriate to organizations handling more sensitive data or operating in regulated environments. IG3 adds safeguards for organizations with significant risk exposure. The library targets IG1 and IG2 in its default content, which covers the majority of small and mid-market organizations and managed service provider client bases.

NIST CSF 2.0 provides a higher-level outcome framework organized into six functions: Govern, Identify, Protect, Detect, Respond, and Recover. CSF 2.0 is well-suited to executive communication and board reporting because the function structure maps naturally to how non-technical leadership thinks about security. The library uses CSF 2.0 as the conceptual scaffold for documents organized around how a program is structured.

The two frameworks work together: CIS provides the specific safeguards, and NIST provides the structure for organizing them. CIS Controls v8.1 tags each safeguard with a CSF 2.0 security function, which makes the pairing explicit. Documents in the library reference both.

Other frameworks (HIPAA Security Rule, PCI DSS, SOC 2 Trust Services Criteria, ISO 27001 Annex A, CMMC, NYDFS Cybersecurity Regulation, GDPR, and others) are not covered by the default library content. Where adopting organizations need alignment to these frameworks, additional content is required. The library will be supplemented with framework-specific addenda over time. Until then, organizations subject to these frameworks should treat the library as a strong foundation that requires augmentation, not as a complete solution.

## Library content map by document

The table below maps each document in the library to the primary CIS Controls v8.1 safeguards and NIST CSF 2.0 subcategories it supports. The mapping is not exhaustive; documents typically support additional controls beyond those listed, but the listed controls are the primary coverage.

For a safeguard-by-safeguard view of the 56 Implementation Group 1 safeguards, with evidence for each, see `docs/cis-ig1-checklist.md`.

The mapping is presented in document-ID order to make it easy to find a specific document and identify its framework support. Each entry cites specific safeguards and subcategories; where a document addresses only part of a control, the entry says so.

### POL-IAM-001: Access Control Policy

**CIS Controls v8.1 primary coverage:**
- Control 5: Account Management (5.1, 5.2, 5.3, 5.4, 5.6)
- Control 6: Access Control Management (6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 6.8)

**NIST CSF 2.0 primary coverage:**
- PR.AA-01: Identities and credentials are managed
- PR.AA-03: Users, services, and hardware are authenticated
- PR.AA-05: Access permissions, entitlements, and authorizations are managed

### POL-IAM-002: Remote Access Policy

**CIS Controls v8.1 primary coverage:**
- Control 6: Access Control Management (6.4, 6.5, 6.7)
- Control 12: Network Infrastructure Management (12.5, 12.6, 12.7, met through identity-gated access rather than a VPN)
- Control 13: Network Monitoring and Defense (13.5)

**NIST CSF 2.0 primary coverage:**
- PR.AA-01: Identities and credentials are managed
- PR.AA-03: Users, services, and hardware are authenticated
- PR.AA-05: Access permissions, entitlements, and authorizations are managed
- PR.IR-01: Networks and environments are protected from unauthorized logical access and usage
- DE.CM-03: Personnel activity and technology usage are monitored

### POL-IAM-003: Non-Human Identity Governance Policy

**CIS Controls v8.1 primary coverage:**
- Control 5: Account Management (5.1, 5.2, 5.3, 5.4, 5.5, 5.6)
- Control 6: Access Control Management (6.1, 6.2, 6.7, 6.8)
- Control 3: Data Protection (3.3)
- Control 8: Audit Log Management (8.2, 8.5)

**NIST CSF 2.0 primary coverage:**
- GV.RR-02: Roles, responsibilities, and authorities are established
- ID.AM-02, ID.AM-05: Software, services, and systems are inventoried and prioritized
- PR.AA-01, PR.AA-03, PR.AA-05: Identity, credential, and access management
- DE.CM-03, DE.CM-09: Personnel activity, technology usage, and computing environments are monitored

### STD-IAM-001: Password and Authentication Standard

**CIS Controls v8.1 primary coverage:**
- Control 5: Account Management (5.2)
- Control 6: Access Control Management (6.3, 6.4, 6.5)

**NIST CSF 2.0 primary coverage:**
- PR.AA-01: Identities and credentials are managed
- PR.AA-02: Identities are proofed and bound to credentials (account recovery verification)
- PR.AA-03: Users, services, and hardware are authenticated
- PR.AA-04: Identity assertions are protected, conveyed, and verified (session management)

**External standard alignment:**
- NIST SP 800-63B Revision 4: This standard reflects Revision 4, including the fifteen-character minimum for single-factor passwords, the prohibition on mandatory periodic rotation and composition rules, compromised-password screening, and the prioritization of phishing-resistant authentication.

### STD-IAM-002: Single Sign-On and Federation Standard

**CIS Controls v8.1 primary coverage:**
- Control 5: Account Management (5.6)
- Control 6: Access Control Management (6.3, 6.7, 6.8)

**NIST CSF 2.0 primary coverage:**
- PR.AA-01: Identities and credentials are managed
- PR.AA-03: Users, services, and hardware are authenticated
- PR.AA-04: Identity assertions are protected
- PR.AA-05: Access permissions, entitlements, and authorizations are managed

### POL-AUP-001: Acceptable Use Policy

**CIS Controls v8.1 primary coverage:**
- Control 14: Security Awareness and Skills Training (14.1, 14.2, 14.3, 14.4, 14.6), as the policy content the awareness program teaches; the program itself is established in POL-GOV-001 Section 3.8
- Control 2: Inventory and Control of Software Assets (2.3)
- Control 5: Account Management (5.2)

**NIST CSF 2.0 primary coverage:**
- GV.RR-04: Cybersecurity is included in human resources practices
- PR.AT-01: Personnel are provided with awareness and training
- PR.AT-02: Individuals in specialized roles are provided with awareness and training
- PR.PS-01: Configuration management practices are established and applied
- PR.DS-01: The confidentiality, integrity, and availability of data-at-rest are protected

### POL-AM-001: Asset Management Policy

**CIS Controls v8.1 primary coverage:**
- Control 1: Inventory and Control of Enterprise Assets (1.1, 1.2, 1.3, 1.4, 1.5)
- Control 2: Inventory and Control of Software Assets (2.1, 2.2, 2.3, 2.4)
- Control 15: Service Provider Management (15.1)

**NIST CSF 2.0 primary coverage:**
- ID.AM-01: Inventories of hardware managed by the organization are maintained
- ID.AM-02: Inventories of software, services, and systems are maintained
- ID.AM-04: Inventories of services provided by suppliers are maintained
- ID.AM-05: Assets are prioritized based on classification, criticality, resources, and impact
- ID.AM-08: Systems, hardware, software, services, and data are managed throughout their life cycles

### STD-AM-001: SaaS Asset Management Standard

**CIS Controls v8.1 primary coverage:**
- Control 2: Inventory and Control of Software Assets (2.1, 2.2, 2.3)
- Control 4: Secure Configuration of Enterprise Assets and Software (4.1)
- Control 5: Account Management (5.3, 5.4)
- Control 11: Data Recovery (11.2, 11.5, for Critical SaaS applications)
- Control 15: Service Provider Management (15.1, 15.7)

**NIST CSF 2.0 primary coverage:**
- ID.AM-02, ID.AM-04: Software, services, and supplier services are inventoried
- ID.AM-08: Assets are managed throughout their life cycles
- PR.AA-05: Access permissions are managed with least privilege
- PR.PS-01: Configuration management practices are established and applied
- PR.DS-11: Backups are created, protected, maintained, and tested (Critical SaaS applications)
- GV.SC-10: Provisions for activities after a service agreement ends

### POL-DC-001: Data Classification and Handling Policy

**CIS Controls v8.1 primary coverage:**
- Control 3: Data Protection (3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.10, 3.11)

**NIST CSF 2.0 primary coverage:**
- ID.AM-07: Inventories of data and corresponding metadata for designated data types are maintained (partial)
- PR.DS-01: The confidentiality, integrity, and availability of data-at-rest are protected
- PR.DS-02: The confidentiality, integrity, and availability of data-in-transit are protected
- PR.DS-10: The confidentiality, integrity, and availability of data-in-use are protected (AI tool inputs)

### POL-IR-001: Incident Response Policy

**CIS Controls v8.1 primary coverage:**
- Control 17: Incident Response Management (17.1, 17.2, 17.3, 17.4, 17.5, 17.6, 17.7, 17.8, 17.9)

**NIST CSF 2.0 primary coverage:**
- GV.RR-04: Cybersecurity is included in human resources practices
- DE.AE-02: Potentially adverse events are analyzed
- DE.AE-03: Information is correlated from multiple sources
- DE.AE-06: Information on adverse events is provided to authorized staff and tools
- DE.AE-08: Incidents are declared when adverse events meet the defined criteria
- RS.MA-01 through RS.MA-05: Incident response plan execution and triage
- RS.AN-03, RS.AN-06, RS.AN-07, RS.AN-08: Incident analysis, records, evidence, and magnitude
- RS.CO-02, RS.CO-03: Incident notification and information sharing
- RS.MI-01, RS.MI-02: Containment and eradication
- RC.RP-01, RC.RP-02, RC.RP-03, RC.RP-05: Recovery execution, backup integrity, and restoration
- RC.CO-03, RC.CO-04: Recovery communication

### POL-EP-001: Endpoint Protection Policy

**CIS Controls v8.1 primary coverage:**
- Control 2: Inventory and Control of Software Assets (2.5, 2.7)
- Control 3: Data Protection (3.6, 3.9)
- Control 4: Secure Configuration of Enterprise Assets and Software (4.1, 4.3, 4.4, 4.5, 4.6, 4.7)
- Control 7: Continuous Vulnerability Management (7.3, 7.4)
- Control 10: Malware Defenses (10.1, 10.2, 10.3, 10.7)
- Control 13: Network Monitoring and Defense (13.2, 13.7)

**NIST CSF 2.0 primary coverage:**
- PR.PS-01: Configuration management practices are established and applied
- PR.PS-02: Software is maintained, replaced, and removed commensurate with risk
- PR.PS-03: Hardware is maintained, replaced, and removed commensurate with risk
- PR.PS-05: Installation and execution of unauthorized software are prevented
- PR.DS-01: The confidentiality, integrity, and availability of data-at-rest are protected
- DE.CM-09: Computing hardware and software, runtime environments, and their data are monitored

### POL-VM-001: Vulnerability Management Policy

**CIS Controls v8.1 primary coverage:**
- Control 7: Continuous Vulnerability Management (7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7)

**NIST CSF 2.0 primary coverage:**
- ID.RA-01: Vulnerabilities in assets are identified, validated, and recorded
- ID.RA-02: Cyber threat intelligence is received from information sharing forums and sources
- ID.RA-05: Threats, vulnerabilities, likelihoods, and impacts are used to inform risk response prioritization
- ID.RA-08: Processes for receiving, analyzing, and responding to vulnerability disclosures are established
- PR.PS-02: Software is maintained, replaced, and removed commensurate with risk
- DE.CM-09: Computing hardware and software are monitored

### STD-VM-001: Security Testing Standard

**CIS Controls v8.1 primary coverage:**
- Control 18: Penetration Testing (18.1, 18.2, 18.3 at the Standard tier; 18.4, 18.5 at the Expanded tier)
- Control 7: Continuous Vulnerability Management (7.6)
- Control 4: Secure Configuration of Enterprise Assets and Software (4.1, through the tenant configuration review)

**NIST CSF 2.0 primary coverage:**
- ID.RA-01: Vulnerabilities are identified, validated, and recorded
- ID.IM-02: Improvements are identified from security tests and exercises
- DE.CM-09: Computing environments are monitored (control checks)

Control 18 has no Implementation Group 1 safeguards. The Baseline tier substitutes external exposure review, configuration review, and quarterly control checks, which suit organizations with little or no infrastructure of their own.

### POL-NET-001: Network Security Policy

**CIS Controls v8.1 primary coverage:**
- Control 4: Secure Configuration of Enterprise Assets and Software (4.2)
- Control 9: Email and Web Browser Protections (9.2, 9.3)
- Control 12: Network Infrastructure Management (12.1, 12.2, 12.3, 12.4, 12.5, 12.6)
- Control 13: Network Monitoring and Defense (13.1, 13.3, 13.4, 13.6)

**NIST CSF 2.0 primary coverage:**
- PR.IR-01: Networks and environments are protected from unauthorized logical access and usage
- PR.PS-01: Configuration management practices are established and applied
- DE.CM-01: Networks and network services are monitored
- DE.CM-06: External service provider activities and services are monitored

### STD-NET-001: Email and Web Browser Protection Standard

**CIS Controls v8.1 primary coverage:**
- Control 9: Email and Web Browser Protections (9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7)
- Control 14: Security Awareness and Skills Training (14.2, for finance and executive support staff)

**NIST CSF 2.0 primary coverage:**
- PR.PS-01, PR.PS-05: Configuration management and prevention of unauthorized software (browsers and extensions)
- PR.DS-02: Data-in-transit is protected (MTA-STS)
- DE.CM-09: Computing hardware and software are monitored
- PR.AT-02: Role-based training

### POL-TPRM-001: Third-Party Risk Management Policy

**CIS Controls v8.1 primary coverage:**
- Control 15: Service Provider Management (15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7)

**NIST CSF 2.0 primary coverage:**
- GV.SC-01 through GV.SC-10: Cybersecurity supply chain risk management

### POL-AI-001: AI and Agent Governance Policy

**CIS Controls v8.1 primary coverage:**
- Control 2: Inventory and Control of Software Assets (2.1, 2.3)
- Control 3: Data Protection (3.3)
- Control 5: Account Management (5.5)
- Control 15: Service Provider Management (15.1, 15.4)

**NIST CSF 2.0 primary coverage:**
- GV.PO-01: Policy is established and enforced
- GV.SC-07: Supplier risks are understood and monitored
- ID.AM-02: Inventories of software, services, and systems are maintained
- PR.AA-05: Access permissions are managed with least privilege
- PR.DS-01, PR.DS-10: Data at rest and in use are protected
- DE.CM-03: Personnel activity and technology usage are monitored

**External framework alignment:**
- CIS Controls AI Companion Guides (LLM, AI Agent, and MCP): mapped to Sections 3.1, 3.3, 3.4, and 3.8.
- OWASP Top 10 for Large Language Model Applications: reference for agent risks and the test basis for AI built in-house.
- NIST AI Risk Management Framework (AI 100-1) and Generative AI Profile (AI 600-1): a practical subset of the Govern function for organizations that mostly use AI rather than build it.

### STD-DC-001: Data Loss Prevention Standard

**CIS Controls v8.1 primary coverage:**
- Control 3: Data Protection (3.3, 3.7, 3.9, 3.13)

**NIST CSF 2.0 primary coverage:**
- PR.DS-01, PR.DS-02, PR.DS-10: Data at rest, in transit, and in use are protected
- DE.CM-03: Personnel activity and technology usage are monitored

### STD-DR-001: Data Backup and Recovery Standard

**CIS Controls v8.1 primary coverage:**
- Control 11: Data Recovery (11.1, 11.2, 11.3, 11.4, 11.5)

**NIST CSF 2.0 primary coverage:**
- PR.DS-11: Backups of data are created, protected, maintained, and tested
- PR.IR-03: Resilience mechanisms are implemented
- RC.RP-02, RC.RP-03, RC.RP-05: Recovery actions, backup integrity verification, and verification of restored assets
- ID.IM-02: Improvements are identified from security tests and exercises

### POL-DEV-001: Secure Development Policy

Applies only where the adopting organization develops software, at one of three levels set in Section 2: scripts and automations, internal applications, or internet-facing applications. The coverage below is for full adoption; the scripts-and-automations level covers Safeguard 16.1 in part, through source control, secrets handling, review, and outsourced development.

**CIS Controls v8.1 primary coverage:**
- Control 16: Application Software Security (16.1 through 16.6, 16.8 through 16.14)

**NIST CSF 2.0 primary coverage:**
- PR.PS-06: Secure software development practices are integrated
- ID.RA-01, ID.RA-08: Vulnerabilities identified and disclosures handled
- GV.SC-05: Security requirements in contracts with outsourced developers

**External framework alignment:**
- NIST SP 800-218 (Secure Software Development Framework): a small-team subset of the practice groups.

### STD-DC-002: Cryptography and Key Management Standard

**CIS Controls v8.1 primary coverage:**
- Control 3: Data Protection (3.6, 3.9, 3.10, 3.11)
- Control 12: Network Infrastructure Management (12.6)

**NIST CSF 2.0 primary coverage:**
- PR.DS-01, PR.DS-02: Data at rest and in transit are protected
- PR.AA-01: Keys and certificates are managed as credentials

### STD-OPS-001: Change Management Standard

**CIS Controls v8.1 primary coverage:**
- Control 4: Secure Configuration of Enterprise Assets and Software (4.1, 4.2)

**NIST CSF 2.0 primary coverage:**
- ID.RA-07: Changes and exceptions are managed, assessed for risk impact, recorded, and tracked
- PR.PS-01: Configuration management practices are established and applied
- DE.CM-09: Unrecorded changes are detected

**Other frameworks:** SOC 2 CC8.1; NIST SP 800-171 3.4.3 through 3.4.5.

### POL-BC-001: Business Continuity Policy

**NIST CSF 2.0 primary coverage:**
- GV.OC-04, GV.OC-05: Services others depend on, and dependencies the organization relies on
- PR.IR-03: Resilience mechanisms
- RC.RP-04: Post-incident operational norms
- RC.CO-03: Recovery progress is communicated

**CIS Controls v8.1:** No business continuity control; complements Control 11.

**Other frameworks:** NYDFS 500.16; SOC 2 A1.2 and A1.3.

### POL-PPS-001: Physical and Personnel Security Policy

**CIS Controls v8.1 primary coverage:**
- Control 6: Access Control Management (6.1, 6.2, through role changes and departures)
- Control 14: Security Awareness and Skills Training (14.1, through Section 3.11)

**NIST CSF 2.0 primary coverage:**
- PR.AA-06: Physical access is managed, monitored, and enforced
- GV.RR-04: Cybersecurity is included in human resources practices

**Other frameworks:** NIST SP 800-171 3.9.x and 3.10.x; HIPAA 164.310(a)(1), (b), (c) and 164.308(a)(1)(ii)(C); SOC 2 CC6.4.

### POL-GOV-001: Information Security Policy

**CIS Controls v8.1 primary coverage:**
- Control 14: Security Awareness and Skills Training (14.1)
- Control 15: Service Provider Management (15.1, 15.2, 15.4)

**NIST CSF 2.0 primary coverage:**
- GV.OC-01, GV.OC-03: Mission and legal, regulatory, and contractual requirements
- GV.RM-01, GV.RM-02, GV.RM-04, GV.RM-06: Risk management objectives, appetite, response options, and method
- GV.RR-01 through GV.RR-04: Leadership accountability, roles, resources, and HR practices
- GV.PO-01, GV.PO-02: Policy established and maintained
- GV.OV-01, GV.OV-03: Oversight of strategy and performance
- GV.SC-01, GV.SC-04, GV.SC-05, GV.SC-07, GV.SC-10: Program-level supply chain provisions
- ID.RA-03 through ID.RA-07, ID.RA-10: Risk assessment, response, exceptions, and supplier assessment
- ID.IM-01: Improvements are identified from evaluations
- PR.AT-01, PR.AT-02: Awareness and role-based training

### STD-LOG-001: Logging and Monitoring Standard

**CIS Controls v8.1 primary coverage:**
- Control 8: Audit Log Management (8.1 through 8.12)
- Control 13: Network Monitoring and Defense (13.1)

**NIST CSF 2.0 primary coverage:**
- PR.PS-04: Log records are generated and made available for continuous monitoring
- PR.DS-01: The confidentiality, integrity, and availability of data-at-rest are protected (log integrity)
- DE.CM-01, DE.CM-03, DE.CM-06, DE.CM-09: Continuous monitoring
- DE.AE-02, DE.AE-03, DE.AE-06: Adverse event analysis
- RS.AN-03: Incident analysis

### RUN-IAM-001: Non-Human Identity Discovery Runbook

Operational support for POL-IAM-003. Supports the same framework controls through procedural execution.

### RUN-IR-002: Tabletop Exercise Facilitation Runbook

Operational support for POL-IR-001 Section 3.10. Supports CIS Safeguard 17.7 (conduct routine incident response exercises) and NIST CSF ID.IM-02 and ID.IM-04 (improvements from exercises; incident response plans are established, communicated, maintained, and improved).

### ADD-CMMC-001: CMMC Level 2 Addendum

Maps the 110 requirements of NIST SP 800-171 Revision 2 to the library by family, adds provisions for the CUI environment, and records where those provisions override library defaults. See the CMMC entry under Frameworks beyond the default for program status.

### Templates

TPL-GOV-001 through TPL-GOV-004 support POL-GOV-001, TPL-LOG-001 and TPL-LOG-002 support STD-LOG-001, TPL-AI-001 supports POL-AI-001, TPL-IAM-001 supports POL-IAM-003 and RUN-IAM-001, and TPL-IAM-002 supports POL-IAM-001, and TPL-BC-001 is the plan required by POL-BC-001. Each supports the framework controls of its parent document by producing recurring control evidence; the specific safeguards are listed in each template's metadata table.

*Additional documents will be mapped here as they are added to the library in future releases.*

## CIS Controls v8.1 coverage by control area

The reverse view: which CIS Controls v8.1 control areas are covered by the library, and which documents provide the coverage.

The numbering follows CIS Controls v8.1's eighteen control areas. Coverage is rated as Strong (the control area is substantively covered), Partial (some safeguards are covered but additional content is needed for full coverage), or Not Covered (the control area is out of scope for the current library version).

| CIS Control | Title | Coverage | Primary Documents |
|-------------|-------|----------|-------------------|
| 1 | Inventory and Control of Enterprise Assets | Strong | POL-AM-001, POL-NET-001 (network visibility) |
| 2 | Inventory and Control of Software Assets | Strong | POL-AM-001, POL-EP-001 (application control) |
| 3 | Data Protection | Strong | POL-DC-001, STD-DC-001 (data loss prevention), POL-EP-001 (device and removable media encryption), POL-IAM-003 (access aspects) |
| 4 | Secure Configuration of Enterprise Assets and Software | Strong | POL-EP-001, POL-NET-001 (network infrastructure) |
| 5 | Account Management | Strong | POL-IAM-001, STD-IAM-001, STD-IAM-002, POL-IAM-003 |
| 6 | Access Control Management | Strong | POL-IAM-001, STD-IAM-001, POL-IAM-002, STD-IAM-002, POL-IAM-003, POL-AUP-001 |
| 7 | Continuous Vulnerability Management | Strong | POL-VM-001, POL-EP-001 (patching) |
| 8 | Audit Log Management | Strong | STD-LOG-001, POL-IAM-003 (NHI logging) |
| 9 | Email and Web Browser Protections | Strong | STD-NET-001, POL-NET-001 (DNS and URL filtering) |
| 10 | Malware Defenses | Strong | POL-EP-001 |
| 11 | Data Recovery | Strong | STD-DR-001, STD-AM-001 (SaaS data), POL-DC-001 (backup classification), POL-IR-001 (recovery phase) |
| 12 | Network Infrastructure Management | Strong | POL-NET-001, POL-IAM-002 (remote access) |
| 13 | Network Monitoring and Defense | Strong | POL-NET-001, POL-EP-001 (endpoint monitoring) |
| 14 | Security Awareness and Skills Training | Strong | POL-GOV-001 (awareness program), POL-AUP-001 (content) |
| 15 | Service Provider Management | Strong | POL-TPRM-001, POL-GOV-001, POL-AM-001 and STD-AM-001 (service inventory and decommissioning) |
| 16 | Application Software Security | Scaled | POL-DEV-001, at the level the organization adopts: not applicable where no code is written, Partial for scripts and automations, Strong for internal and internet-facing applications |
| 17 | Incident Response Management | Strong | POL-IR-001, RUN-IR-001, RUN-IR-002 (exercises) |
| 18 | Penetration Testing | Scaled | STD-VM-001: Strong at the Standard and Expanded tiers; at the Baseline tier, control checks and exposure review substitute for testing, since Control 18 has no IG1 safeguards |

Of the eighteen CIS Controls v8.1 control areas, sixteen are covered Strong for every adopter. The other two scale with the organization. Application Software Security (Control 16) depends on how much software the organization builds, and POL-DEV-001 sets three adoption levels. Penetration Testing (Control 18) has no Implementation Group 1 safeguards, so STD-VM-001 sets a Baseline tier that every organization meets with scanning, exposure review, configuration review, and control checks, and Standard and Expanded tiers, triggered by exposure and obligations rather than headcount, that add outside testing. Since v0.1.0, Audit Log Management, Email and Web Browser Protections, and Data Recovery moved to Strong with STD-LOG-001, STD-NET-001, and STD-DR-001.

## NIST CSF 2.0 coverage by function

The reverse view organized by NIST CSF 2.0 function. Each function contains categories, and each category contains subcategories. Coverage is rated by category.

### GOVERN (GV)

The Govern function addresses how the organization establishes, communicates, and monitors its cybersecurity risk management strategy.

**GV.OC (Organizational Context):** Strong coverage. POL-GOV-001 covers GV.OC-01 and GV.OC-03 (mission and obligations), and POL-BC-001 covers GV.OC-04 and GV.OC-05 (services others depend on, and dependencies the organization relies on). Stakeholder expectations (GV.OC-02) are documented through the adopting organization's own artifacts.

**GV.RM (Risk Management Strategy):** Strong coverage. POL-GOV-001 establishes risk objectives, risk appetite, response options, and a standard rating method, supported by the risk register template.

**GV.RR (Roles, Responsibilities, and Authorities):** Strong coverage. Every policy in the library establishes roles and responsibilities for its domain. POL-PPS-001 includes cybersecurity in human resources practices (GV.RR-04): screening, agreements, departures, and sanctions.

**GV.PO (Policy):** Strong coverage. The library itself contributes to this category by providing template policies. Adopting organizations establish their policy program by adopting and customizing the library's policies.

**GV.OV (Oversight):** Strong coverage. POL-GOV-001 consolidates oversight through the quarterly and annual program reviews and the metrics report.

**GV.SC (Cybersecurity Supply Chain Risk Management):** Strong coverage. POL-TPRM-001 addresses GV.SC-01 through GV.SC-10, and POL-GOV-001 ties the vendor program into overall governance.

### IDENTIFY (ID)

The Identify function addresses understanding the organization's assets, suppliers, and risks.

**ID.AM (Asset Management):** Strong coverage. POL-AM-001 covers hardware and software inventory; POL-IAM-003 covers identity assets; POL-DC-001 covers data assets.

**ID.RA (Risk Assessment):** Strong coverage. POL-VM-001 covers vulnerability identification, prioritization, threat intelligence, and disclosure (ID.RA-01, ID.RA-02, ID.RA-05, ID.RA-08). POL-GOV-001 covers threat identification, likelihood and impact rating, risk response, exceptions, and supplier assessment (ID.RA-03 through ID.RA-07, ID.RA-10). Hardware and software integrity assessment before acquisition (ID.RA-09) is not covered.

**ID.IM (Improvement):** Strong coverage. POL-GOV-001 covers ID.IM-01 through the program reviews and ID.IM-03 through the measurement and reporting of operational processes. RUN-IR-002 (tabletop exercises) and the restore testing in STD-DR-001 cover ID.IM-02 and ID.IM-04, and POL-IR-001 feeds post-incident lessons into the program.

### PROTECT (PR)

The Protect function addresses safeguards to limit or contain the impact of cybersecurity events.

**PR.AA (Identity Management, Authentication, and Access Control):** Strong coverage. POL-IAM-001, STD-IAM-001, POL-IAM-002, STD-IAM-002, and POL-IAM-003 cover PR.AA-01 through PR.AA-05, and POL-PPS-001 covers physical access (PR.AA-06).

**PR.AT (Awareness and Training):** Strong coverage. POL-GOV-001 Section 3.8 establishes the awareness and role-based training program (PR.AT-01, PR.AT-02), and POL-AUP-001 supplies the content users are trained on.

**PR.DS (Data Security):** Strong coverage. POL-DC-001 and STD-DC-001 cover data-at-rest, data-in-transit, and data-in-use. STD-DR-001 covers backup creation, protection, and testing (PR.DS-11).

**PR.PS (Platform Security):** Strong coverage for PR.PS-01 through PR.PS-05, through POL-EP-001 and STD-LOG-001 (PR.PS-04). Secure software development (PR.PS-06) is covered by POL-DEV-001 where it is adopted.

**PR.IR (Technology Infrastructure Resilience):** Partial coverage. POL-NET-001 and POL-IAM-002 cover PR.IR-01, and STD-DR-001 and POL-BC-001 cover PR.IR-03 (resilience mechanisms). Environmental protection of facilities (PR.IR-02) is covered only at the level of locked equipment areas in POL-PPS-001, and capacity planning (PR.IR-04) is not covered.

### DETECT (DE)

The Detect function addresses identifying cybersecurity events.

**DE.CM (Continuous Monitoring):** Strong coverage. STD-LOG-001 (log sources, monitoring, and alerting), POL-IAM-003 (identity monitoring), POL-EP-001 (endpoint monitoring), and POL-NET-001 (network monitoring) together address the category.

**DE.AE (Adverse Event Analysis):** Strong coverage. POL-IR-001 and STD-LOG-001 cover DE.AE-02, DE.AE-03, DE.AE-06, and DE.AE-08.

### RESPOND (RS)

The Respond function addresses actions taken when a cybersecurity event is detected.

**RS.MA (Incident Management):** Strong coverage. POL-IR-001 substantively covers RS.MA-01 through RS.MA-05.

**RS.AN (Incident Analysis):** Strong coverage. POL-IR-001 addresses RS.AN-03, RS.AN-06, RS.AN-07, and RS.AN-08 through the response phases, evidence handling, and post-incident review.

**RS.CO (Incident Response Reporting and Communication):** Strong coverage. POL-IR-001 covers RS.CO-02 and RS.CO-03 through internal, executive, and external communication.

**RS.MI (Incident Mitigation):** Strong coverage. POL-IR-001 covers RS.MI-01 and RS.MI-02 through containment, eradication, and the standing authority matrix.

### RECOVER (RC)

The Recover function addresses restoring normal operations after a cybersecurity event.

**RC.RP (Incident Recovery Plan Execution):** Strong coverage. POL-IR-001 and STD-DR-001 cover RC.RP-01, RC.RP-02, RC.RP-03, and RC.RP-05, and POL-BC-001 covers post-incident operational norms (RC.RP-04). Formal recovery closure criteria (RC.RP-06) are covered only through the Recovery phase in POL-IR-001 Section 3.4.

**RC.CO (Incident Recovery Communication):** Strong coverage. POL-IR-001 covers RC.CO-03 and RC.CO-04.

The Recover function will be further addressed in future library content focused on business continuity and disaster recovery.

## Frameworks beyond the default

Adopting organizations subject to frameworks beyond CIS Controls v8.1 and NIST CSF 2.0 should consider the following guidance.

**HIPAA Security Rule.** The Security Rule's administrative, physical, and technical safeguards have substantial overlap with CIS Controls v8.1 and NIST CSF 2.0, but specific HIPAA requirements (workforce security under §164.308(a)(3), information access management under §164.308(a)(4), audit controls under §164.312(b), and others) require explicit treatment in policy text. Healthcare organizations adopting this library should plan for additional content to address HIPAA-specific requirements. HHS published a proposed overhaul of the Security Rule in January 2025. The proposal has not been finalized: the 2026 Unified Agenda moved the projected final action from May 2026 to July 2027 and reclassified the rulemaking as a long-term action. The current Security Rule remains in force and enforceable. Some published sources describe the proposal as a final rule; it is not. Build any HIPAA work against the current rule, and validate the proposal's status before adopting any of its requirements. A HIPAA addendum is a planned future addition.

**PCI DSS.** Merchants and payment processors subject to PCI DSS (currently version 4.0.1) need policy and procedural content addressing the twelve PCI DSS requirements. The library's identity, access control, vulnerability management, network security, endpoint protection, and logging content provides substantial partial coverage of requirements 1, 2, 6, 7, 8, 10, and 11. Comprehensive PCI DSS alignment requires additional work, particularly around requirements 3 (cryptography for stored cardholder data), 4 (cryptography for transmitted cardholder data), and 12 (information security policy specific to PCI scope).

**SOC 2 Trust Services Criteria.** Service organizations seeking SOC 2 Type II reports need policy and operational evidence aligned to the relevant Trust Services Criteria. The library's content provides substantial coverage of several Common Criteria (CC) categories: CC1 (control environment), CC2 (communication and information), CC3 (risk assessment, through POL-GOV-001), CC5 (control activities), CC6 (logical and physical access controls), CC7 (system operations), CC8.1 (change management, through STD-OPS-001), and CC9.2 (vendor risk management, through POL-TPRM-001). Organizations reporting on the Availability criteria have support for A1.2 and A1.3 through STD-DR-001 and POL-BC-001. The library also provides partial coverage of the Confidentiality category. Service organizations should engage qualified SOC 2 advisory services for the gap analysis between the library's content and their specific TSC scope.

**ISO/IEC 27001 Annex A.** The Annex A control set in ISO/IEC 27001:2022 has significant overlap with CIS Controls v8.1. Organizations pursuing ISO 27001 certification can use the library as a starting point but will need to explicitly map their adopted policies to Annex A controls and produce the additional documentation required by ISO 27001 (Statement of Applicability, risk treatment plan, and others).

**CMMC.** Defense contractors subject to Cybersecurity Maturity Model Certification need policy and procedural content aligned to NIST SP 800-171 and the CMMC level appropriate to their contracts. Level 2 is assessed against the 110 requirements of NIST SP 800-171 Revision 2, which remains the baseline under DFARS 252.204-7012 even though Revision 3 has been published; DoD has signaled a future rule to transition to Revision 3. The rollout changed during 2026. DoD suspended the Phase 2 third-party certification requirement in July 2026, before its scheduled November 2026 start, and a September 2026 class deviation directed contracting officers to accept Level 1 and Level 2 self-assessments while the program is reviewed. The self-assessment obligations and the underlying 800-171 requirements were not suspended. The library's content provides substantial partial coverage of the relevant 800-171 requirements; comprehensive CMMC alignment requires additional content addressing the requirements not covered.

ADD-CMMC-001 maps the 800-171 requirements to the library and sets the additional provisions for a CUI environment.

The CMMC program has changed repeatedly and is expected to change again. Validate the current phase, the assessment type the contract requires, and the applicable 800-171 revision against current DoD guidance and the contract itself before relying on this paragraph.

**NYDFS Cybersecurity Regulation (23 NYCRR Part 500).** The amended regulation adopted in November 2023 phased in through November 1, 2025, and all of its requirements are now in effect for covered entities.

The library provides partial coverage of these sections: risk assessment (500.9) through POL-GOV-001; third-party service provider security (500.11) through POL-TPRM-001; access privileges and privileged access management (500.7) through POL-IAM-001; multi-factor authentication for any individual accessing information systems (500.12) through POL-IAM-001 and STD-IAM-001; asset inventory (500.13) through POL-AM-001; vulnerability management (500.5) through POL-VM-001; monitoring and training (500.14) through STD-LOG-001 and POL-GOV-001; and incident response and business continuity planning (500.16) through POL-IR-001, POL-BC-001, and STD-DR-001.

The library does not provide: a designated CISO with the governance and board reporting duties in 500.4; the annual certification of compliance or acknowledgment of noncompliance due to the Department by April 15 (500.17(b)); the seventy-two-hour notice to the Department of a cybersecurity event, and the twenty-four-hour notice and thirty-day written explanation of any extortion payment (500.17); the additional requirements for Class A companies, including independent audits, a privileged access management solution, and endpoint detection with centralized logging; and the limited exemption analysis in 500.19. Validate these against the current regulation and Department guidance before relying on them.

**CIRCIA.** The Cyber Incident Reporting for Critical Infrastructure Act of 2022 will require covered entities in critical infrastructure sectors to report covered cyber incidents to CISA within seventy-two hours and ransom payments within twenty-four hours. The requirements take effect on a date set by CISA's final rule, which was under White House review as of late 2026 and had not been published. Coverage, incident definitions, and reporting details may change in the final rule. POL-IR-001 Section 3.6 and RUN-IR-001 include placeholders for these obligations; validate them against the final rule once it is published.

**AI-specific frameworks and regulation.** POL-AI-001 aligns to a subset of the NIST AI Risk Management Framework. Organizations seeking ISO/IEC 42001 certification for an AI management system, building AI systems for others, or subject to AI-specific regulation (such as the EU AI Act or state laws on automated decision-making) need the AI RMF's Map, Measure, and Manage functions and additional documentation beyond this library.

**GDPR and other privacy regulations.** Privacy regulations introduce data subject rights, data processing lawfulness requirements, and data protection impact assessments that the library does not address. Organizations subject to privacy regulations should treat the library as security-only foundation and engage qualified privacy advisory services for the additional work required.

## How to use this mapping

For an internal IT lead or MSP using the library, the mapping serves three practical purposes.

**Adoption planning.** Before adopting the library, walk the framework mapping against the adopting organization's required frameworks. Confirm that the library's coverage is sufficient for the organization's needs, or identify the gaps that require additional content. The framework coverage table indicates where the library is strong and where it requires supplementation.

**Audit response.** When an auditor or assessor asks how the organization addresses a specific control, this document provides a quick reference to the policy or runbook in the library that demonstrates the control's implementation.

**Roadmap planning.** As the library expands in future releases, the framework mapping shows the trajectory of expanded coverage. Adopting organizations can plan their own program maturity in alignment with the library's growth, prioritizing internal work in areas where library coverage is forthcoming.

The mapping is a living document. As the library expands, the mapping is updated to reflect the new coverage. Adopting organizations should consult the latest version of this document when planning major program updates.

---

*Framework alignment is the language of audit-defensibility. State the alignment explicitly; do not leave it implicit when writing policies.*
