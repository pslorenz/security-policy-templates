# Framework Mapping

How this library's content aligns to CIS Controls v8 and NIST Cybersecurity Framework 2.0. The mapping serves three purposes: it lets adopters confirm coverage of the controls their organization needs, it provides the audit-defensibility of explicit framework references, and it documents the rationale for the library's structural choices.

The mapping is current as of library version 0.1.0. As new content is added in subsequent releases, this document is updated to reflect the expanded coverage.

---

## The library's framework alignment philosophy

The library aligns to two frameworks by default: CIS Controls v8 and NIST Cybersecurity Framework 2.0. The reasoning behind these specific choices is worth stating explicitly.

CIS Controls v8 provides specific, prescriptive safeguards organized into implementation groups appropriate to organizations of different sizes. Implementation Group 1 (IG1) is the minimum baseline for any organization with basic IT capabilities. IG2 adds safeguards appropriate to organizations handling more sensitive data or operating in regulated environments. IG3 adds safeguards for organizations with significant risk exposure. The library targets IG1 and IG2 in its default content, which covers the majority of small and mid-market organizations and managed service provider client bases.

NIST CSF 2.0 provides a higher-level outcome framework organized into six functions: Govern, Identify, Protect, Detect, Respond, and Recover. CSF 2.0 is well-suited to executive communication and board reporting because the function structure maps naturally to how non-technical leadership thinks about security. The library uses CSF 2.0 as the conceptual scaffold for documents organized around how a program is structured.

The two frameworks are complementary, not redundant. CIS provides the specific safeguards; NIST provides the structure for organizing them. Documents in the library reference both.

Other frameworks (HIPAA Security Rule, PCI DSS, SOC 2 Trust Services Criteria, ISO 27001 Annex A, CMMC, NYDFS Cybersecurity Regulation, GDPR, and others) are not covered by the default library content. Where adopting organizations need alignment to these frameworks, additional content is required. The library will be supplemented with framework-specific addenda over time. Until then, organizations subject to these frameworks should treat the library as a strong foundation that requires augmentation, not as a complete solution.

## Library content map by document

The table below maps each document in the library to the primary CIS Controls v8 safeguards and NIST CSF 2.0 subcategories it supports. The mapping is not exhaustive; documents typically support additional controls beyond those listed, but the listed controls are the primary coverage.

The mapping is presented in document-ID order to make it easy to find a specific document and identify its framework support.

### POL-IAM-001: Access Control Policy

**CIS Controls v8 primary coverage:**
- Control 5: Account Management (5.1, 5.2, 5.3, 5.4, 5.6)
- Control 6: Access Control Management (6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 6.8)

**NIST CSF 2.0 primary coverage:**
- PR.AA-01: Identities and credentials are managed
- PR.AA-02: Identities are proofed and bound to credentials
- PR.AA-03: Users, services, and hardware are authenticated
- PR.AA-04: Identity assertions are protected
- PR.AA-05: Access permissions, entitlements, and authorizations are managed

### POL-IAM-002: Password and Authentication Standard

**CIS Controls v8 primary coverage:**
- Control 5: Account Management (5.2)
- Control 6: Access Control Management (6.3, 6.4, 6.5)

**NIST CSF 2.0 primary coverage:**
- PR.AA-01: Identities and credentials are managed
- PR.AA-03: Users, services, and hardware are authenticated

**External standard alignment:**
- NIST SP 800-63B Digital Identity Guidelines: This standard reflects current 800-63B guidance, including the move away from mandatory periodic password rotation, the move away from mandatory complexity rules, and the prioritization of phishing-resistant authentication.

### POL-IAM-005: Remote Access Policy

**CIS Controls v8 primary coverage:**
- Control 6: Access Control Management (6.4, 6.5, 6.7)
- Control 12: Network Infrastructure Management (12.5, 12.6)
- Control 13: Network Monitoring and Defense (13.5)

**NIST CSF 2.0 primary coverage:**
- PR.AA-01: Identities and credentials are managed
- PR.AA-03: Users, services, and hardware are authenticated
- PR.AA-05: Access permissions, entitlements, and authorizations are managed
- PR.IR-01: Networks and environments are protected from unauthorized logical access
- DE.CM-01: Networks and personnel activity are monitored

### POL-IAM-006: Single Sign-On and Federation Standard

**CIS Controls v8 primary coverage:**
- Control 5: Account Management (5.6)
- Control 6: Access Control Management (6.7, 6.8)

**NIST CSF 2.0 primary coverage:**
- PR.AA-01: Identities and credentials are managed
- PR.AA-03: Users, services, and hardware are authenticated
- PR.AA-04: Identity assertions are protected
- PR.AA-05: Access permissions, entitlements, and authorizations are managed

### POL-IAM-011: Non-Human Identity Governance Policy

**CIS Controls v8 primary coverage:**
- Control 5: Account Management (5.1, 5.2, 5.3, 5.4, 5.5, 5.6)
- Control 6: Access Control Management (6.1, 6.2, 6.7, 6.8)
- Control 3: Data Protection (selected safeguards related to access)
- Control 8: Audit Log Management (supporting)

**NIST CSF 2.0 primary coverage:**
- GV.RR-01, GV.RR-02: Roles and responsibilities for cybersecurity are established
- ID.AM-02, ID.AM-05: Software, services, and systems are inventoried and prioritized
- PR.AA-01 through PR.AA-05: Identity, credential, and access management
- DE.CM-01, DE.CM-03: Networks and personnel activity are monitored

### POL-AUP-001: Acceptable Use Policy

**CIS Controls v8 primary coverage:**
- Control 14: Security Awareness and Skills Training (14.1, 14.2, 14.3, 14.4, 14.6)
- Control 4: Secure Configuration of Enterprise Assets and Software (selected safeguards related to user-installed software)
- Control 6: Access Control Management (selected safeguards related to user behavior)

**NIST CSF 2.0 primary coverage:**
- GV.RR-04: Cybersecurity is included in human resources practices
- PR.AT-01: Personnel are provided with awareness and training
- PR.AT-02: Individuals in specialized roles are provided with awareness and training
- PR.PS-01: Configuration management practices are established and applied
- PR.DS-01: The confidentiality, integrity, and availability of data-at-rest are protected

### POL-AM-001: Asset Management Policy

**CIS Controls v8 primary coverage:**
- Control 1: Inventory and Control of Enterprise Assets (1.1, 1.2, 1.3, 1.4, 1.5)
- Control 2: Inventory and Control of Software Assets (2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7)
- Control 15: Service Provider Management (selected safeguards related to inventorying third-party services)

**NIST CSF 2.0 primary coverage:**
- ID.AM-01: Inventories of hardware managed by the organization are maintained
- ID.AM-02: Inventories of software, services, and systems are maintained
- ID.AM-04: Inventories of services provided by suppliers are maintained
- ID.AM-05: Resources are prioritized based on classification, criticality, and impact
- ID.AM-08: Systems, hardware, software, services, and data are managed throughout their life cycles

### POL-DC-001: Data Classification and Handling Policy

**CIS Controls v8 primary coverage:**
- Control 3: Data Protection (3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.10, 3.11)

**NIST CSF 2.0 primary coverage:**
- ID.AM-07: Inventories of data and corresponding metadata for designated data types are maintained
- PR.DS-01: The confidentiality, integrity, and availability of data-at-rest are protected
- PR.DS-02: The confidentiality, integrity, and availability of data-in-transit are protected
- PR.DS-10: The confidentiality, integrity, and availability of data-in-use are protected
- PR.DS-11: Backups of data are created, protected, maintained, and tested

### POL-IR-001: Incident Response Policy

**CIS Controls v8 primary coverage:**
- Control 17: Incident Response Management (17.1, 17.2, 17.3, 17.4, 17.5, 17.6, 17.7, 17.8, 17.9)

**NIST CSF 2.0 primary coverage:**
- GV.RR-04: Cybersecurity is included in human resources practices
- DE.AE-02: Potentially adverse events are analyzed
- DE.AE-03: Information is correlated from multiple sources
- DE.AE-06: Information on adverse events is provided to authorized staff and tools
- DE.AE-08: Incidents are declared when adverse events meet the defined criteria
- RS.MA-01 through RS.MA-05: Incident response plan execution and triage
- RS.AN: Incident analysis
- RS.CO: Incident response reporting and communication
- RS.MI: Incident mitigation
- RC.RP: Incident recovery plan execution
- RC.CO: Incident recovery communication

### POL-EP-001: Endpoint Protection Policy

**CIS Controls v8 primary coverage:**
- Control 4: Secure Configuration of Enterprise Assets and Software (4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7)
- Control 7: Continuous Vulnerability Management (7.3, 7.4)
- Control 10: Malware Defenses (10.1, 10.2, 10.3, 10.7)
- Control 13: Network Monitoring and Defense (selected safeguards related to endpoint monitoring)

**NIST CSF 2.0 primary coverage:**
- PR.PS-01: Configuration management practices are established and applied
- PR.PS-02: Software is maintained, replaced, and removed commensurate with risk
- PR.PS-03: Hardware is maintained, replaced, and removed commensurate with risk
- PR.PS-05: Installation and execution of unauthorized software are prevented
- PR.DS-01: The confidentiality, integrity, and availability of data-at-rest are protected
- DE.CM-01: Networks and personnel activity are monitored
- DE.CM-09: Computing hardware and software are monitored

### POL-VM-001: Vulnerability Management Policy

**CIS Controls v8 primary coverage:**
- Control 7: Continuous Vulnerability Management (7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7)
- Control 18: Penetration Testing (selected safeguards, where applicable to the adopting organization)

**NIST CSF 2.0 primary coverage:**
- ID.RA-01: Vulnerabilities in assets are identified, validated, and recorded
- ID.RA-02: Cyber threat intelligence is received from information sharing forums and sources
- ID.RA-05: Threats, vulnerabilities, likelihoods, and impacts are used to inform risk response prioritization
- PR.PS-02: Software is maintained, replaced, and removed commensurate with risk
- DE.CM-09: Computing hardware and software are monitored

### POL-NET-001: Network Security Policy

**CIS Controls v8 primary coverage:**
- Control 12: Network Infrastructure Management (12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8)
- Control 13: Network Monitoring and Defense (13.1, 13.2, 13.3, 13.4, 13.5, 13.6)

**NIST CSF 2.0 primary coverage:**
- PR.IR-01: Networks and environments are protected from unauthorized logical access
- PR.IR-02: The organization's technology assets are protected from environmental threats
- PR.PS-01: Configuration management practices are established and applied
- DE.CM-01: Networks and personnel activity are monitored
- DE.CM-06: External service provider activities and services are monitored

### POL-TPRM-001: Third-Party Risk Management Policy

**CIS Controls v8 primary coverage:**
- Control 15: Service Provider Management (15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7)

**NIST CSF 2.0 primary coverage:**
- GV.SC-01 through GV.SC-10: Cybersecurity supply chain risk management

### RUN-IAM-011: Non-Human Identity Discovery Runbook

Operational support for POL-IAM-011. Supports the same framework controls through procedural execution.

### REV-IAM-011: Quarterly Non-Human Identity Access Review

Operational support for POL-IAM-011. Supports the same framework controls by producing recurring control evidence.

*Additional documents will be mapped here as they are added to the library in future releases.*

## CIS Controls v8 coverage by control area

The reverse view: which CIS Controls v8 control areas are covered by the library, and which documents provide the coverage.

The numbering follows CIS Controls v8's eighteen control areas. Coverage is rated as Strong (the control area is substantively covered), Partial (some safeguards are covered but additional content is needed for full coverage), or Not Covered (the control area is out of scope for the current library version).

| CIS Control | Title | Coverage | Primary Documents |
|-------------|-------|----------|-------------------|
| 1 | Inventory and Control of Enterprise Assets | Strong | POL-AM-001 |
| 2 | Inventory and Control of Software Assets | Strong | POL-AM-001 |
| 3 | Data Protection | Strong | POL-DC-001, POL-IAM-011 (access aspects) |
| 4 | Secure Configuration of Enterprise Assets and Software | Strong | POL-EP-001, POL-AUP-001 (user-installed software) |
| 5 | Account Management | Strong | POL-IAM-001, POL-IAM-002, POL-IAM-006, POL-IAM-011 |
| 6 | Access Control Management | Strong | POL-IAM-001, POL-IAM-002, POL-IAM-005, POL-IAM-006, POL-IAM-011, POL-AUP-001 |
| 7 | Continuous Vulnerability Management | Strong | POL-VM-001, POL-EP-001 (patching) |
| 8 | Audit Log Management | Partial | POL-IAM-011 (NHI logging); planned logging and monitoring standard for full coverage |
| 9 | Email and Web Browser Protections | Not Covered | Forthcoming in v0.2.0 or later |
| 10 | Malware Defenses | Strong | POL-EP-001 |
| 11 | Data Recovery | Partial | POL-DC-001 (backup classification), POL-IR-001 (recovery phase); standalone data recovery content forthcoming |
| 12 | Network Infrastructure Management | Strong | POL-NET-001, POL-IAM-005 (remote access) |
| 13 | Network Monitoring and Defense | Strong | POL-NET-001, POL-EP-001 (endpoint monitoring) |
| 14 | Security Awareness and Skills Training | Strong | POL-AUP-001 |
| 15 | Service Provider Management | Strong | POL-TPRM-001, POL-AM-001 (service inventory) |
| 16 | Application Software Security | Not Covered | Out of scope for v0.1.0 (relevant only to organizations developing software) |
| 17 | Incident Response Management | Strong | POL-IR-001 |
| 18 | Penetration Testing | Partial | POL-VM-001 (referenced where applicable); standalone treatment forthcoming where adopters need it |

The coverage table reflects the library at the v0.1.0 release. Of the eighteen CIS Controls v8 control areas, fourteen are now covered Strong, two are Partial (Audit Log Management, Data Recovery), and two are Not Covered (Email and Web Browser Protections, Application Software Security). The two Not Covered items are deliberate scope decisions: email and web browser protections are planned for v0.2.0 or later, and application software security is out of scope for organizations that do not develop software.

## NIST CSF 2.0 coverage by function

The reverse view organized by NIST CSF 2.0 function. Each function contains categories, and each category contains subcategories. Coverage is rated by category.

### GOVERN (GV)

The Govern function addresses how the organization establishes, communicates, and monitors its cybersecurity risk management strategy.

**GV.OC (Organizational Context):** Not yet covered. The library does not include organizational context establishment as a standalone topic. Adopting organizations document this through their own organizational artifacts.

**GV.RM (Risk Management Strategy):** Not yet covered as a standalone topic. Risk-based decisions appear throughout the library (vendor tiering, vulnerability prioritization, asset criticality) but a standalone risk management strategy is deferred to a future GRC policy.

**GV.RR (Roles, Responsibilities, and Authorities):** Strong coverage. Every policy in the library establishes roles and responsibilities for its domain. Cybersecurity is included in human resources practices through POL-AUP-001.

**GV.PO (Policy):** Strong coverage. The library itself contributes to this category by providing template policies. Adopting organizations establish their policy program by adopting and customizing the library's policies.

**GV.OV (Oversight):** Partial coverage. Each policy includes review cycles and reporting expectations. Comprehensive oversight is supported by, but not formally consolidated in, the v0.1.0 library; a future GRC policy would consolidate this.

**GV.SC (Cybersecurity Supply Chain Risk Management):** Strong coverage. POL-TPRM-001 substantively addresses GV.SC-01 through GV.SC-10.

### IDENTIFY (ID)

The Identify function addresses understanding the organization's assets, suppliers, and risks.

**ID.AM (Asset Management):** Strong coverage. POL-AM-001 covers hardware and software inventory; POL-IAM-011 covers identity assets; POL-DC-001 covers data assets.

**ID.RA (Risk Assessment):** Partial coverage. POL-VM-001 covers vulnerability identification, prioritization, and threat intelligence inputs. Comprehensive risk assessment is deferred to a future GRC policy.

**ID.IM (Improvement):** Partial coverage. Implicit in the library's revision history requirements, the post-incident review process in POL-IR-001, and the various review cadences across the policies. A standalone improvement program is deferred.

### PROTECT (PR)

The Protect function addresses safeguards to limit or contain the impact of cybersecurity events.

**PR.AA (Identity Management, Authentication, and Access Control):** Strong coverage. POL-IAM-001, POL-IAM-002, POL-IAM-005, POL-IAM-006, and POL-IAM-011 substantively cover this category.

**PR.AT (Awareness and Training):** Strong coverage. POL-AUP-001 covers PR.AT-01 and PR.AT-02 substantively.

**PR.DS (Data Security):** Strong coverage. POL-DC-001 covers data-at-rest, data-in-transit, data-in-use, and backups.

**PR.PS (Platform Security):** Strong coverage. POL-EP-001 covers platform security comprehensively.

**PR.IR (Technology Infrastructure Resilience):** Strong coverage. POL-NET-001 covers PR.IR-01 and PR.IR-02 substantively.

### DETECT (DE)

The Detect function addresses identifying cybersecurity events.

**DE.CM (Continuous Monitoring):** Strong coverage. POL-IAM-011 (identity monitoring), POL-EP-001 (endpoint monitoring), POL-NET-001 (network monitoring) collectively address the continuous monitoring category.

**DE.AE (Adverse Event Analysis):** Strong coverage. POL-IR-001 covers DE.AE-02, DE.AE-03, DE.AE-06, and DE.AE-08.

### RESPOND (RS)

The Respond function addresses actions taken when a cybersecurity event is detected.

**RS.MA (Incident Management):** Strong coverage. POL-IR-001 substantively covers RS.MA-01 through RS.MA-05.

**RS.AN (Incident Analysis):** Strong coverage. POL-IR-001 addresses incident analysis through the response phases and post-incident review.

**RS.CO (Incident Response Reporting and Communication):** Strong coverage. POL-IR-001 covers internal, executive, and external communication.

**RS.MI (Incident Mitigation):** Strong coverage. POL-IR-001 covers containment, eradication, and the standing authority matrix for fast mitigation.

### RECOVER (RC)

The Recover function addresses restoring normal operations after a cybersecurity event.

**RC.RP (Incident Recovery Plan Execution):** Strong coverage. POL-IR-001 Recovery phase addresses this substantively.

**RC.CO (Incident Recovery Communication):** Strong coverage. POL-IR-001 communication provisions extend through recovery.

The Recover function will be further addressed in future library content focused on business continuity and disaster recovery.

## Frameworks beyond the default

Adopting organizations subject to frameworks beyond CIS Controls v8 and NIST CSF 2.0 should consider the following guidance.

**HIPAA Security Rule.** The Security Rule's administrative, physical, and technical safeguards have substantial overlap with CIS Controls v8 and NIST CSF 2.0, but specific HIPAA requirements (workforce security under §164.308(a)(3), information access management under §164.308(a)(4), audit controls under §164.312(b), and others) require explicit treatment in policy text. Healthcare organizations adopting this library should plan for additional content to address HIPAA-specific requirements. A HIPAA addendum is a planned future addition.

**PCI DSS.** Merchants and payment processors subject to PCI DSS requirements (most recently version 4.0) need policy and procedural content addressing the twelve PCI DSS requirements. The library's identity, access control, vulnerability management, network security, endpoint protection, and logging content provides substantial partial coverage of requirements 1, 2, 6, 7, 8, 10, and 11. Comprehensive PCI DSS alignment requires additional work, particularly around requirements 3 (cryptography for stored cardholder data), 4 (cryptography for transmitted cardholder data), and 12 (information security policy specific to PCI scope).

**SOC 2 Trust Services Criteria.** Service organizations seeking SOC 2 Type II reports need policy and operational evidence aligned to the relevant Trust Services Criteria. The library's content provides substantial coverage of the Common Criteria (CC) categories: CC1 (control environment), CC2 (communication and information), CC5 (control activities), CC6 (logical and physical access controls), CC7 (system operations), and CC8 (change management). The library also provides partial coverage of the Confidentiality category. Service organizations should engage qualified SOC 2 advisory services for the gap analysis between the library's content and their specific TSC scope.

**ISO/IEC 27001 Annex A.** ISO 27001's Annex A control set has significant overlap with CIS Controls v8. Organizations pursuing ISO 27001 certification can use the library as a starting point but will need to explicitly map their adopted policies to Annex A controls and produce the additional documentation required by ISO 27001 (Statement of Applicability, risk treatment plan, and others).

**CMMC.** Defense contractors subject to Cybersecurity Maturity Model Certification need policy and procedural content aligned to NIST SP 800-171 and the CMMC level appropriate to their contracts. The library's content provides substantial partial coverage of the relevant NIST 800-171 controls. Comprehensive CMMC alignment requires additional content addressing the specific controls not covered.

**NYDFS Cybersecurity Regulation (23 NYCRR 500).** Financial services entities subject to NYDFS cybersecurity requirements need specific policy content addressing the regulation's risk assessment, third-party service provider, and incident notification provisions. The library's TPRM, incident response, and access control policies provide substantial partial coverage. Specific NYDFS requirements around CISO role and certification of compliance require additional content.

**GDPR and other privacy regulations.** Privacy regulations introduce data subject rights, data processing lawfulness requirements, and data protection impact assessments that the library does not address. Organizations subject to privacy regulations should treat the library as security-only foundation and engage qualified privacy advisory services for the additional work required.

## How to use this mapping

For an internal IT lead or MSP using the library, the mapping serves three practical purposes.

**Adoption planning.** Before adopting the library, walk the framework mapping against the adopting organization's required frameworks. Confirm that the library's coverage is sufficient for the organization's needs, or identify the gaps that require additional content. The framework coverage table indicates where the library is strong and where it requires supplementation.

**Audit response.** When an auditor or assessor asks how the organization addresses a specific control, this document provides a quick reference to the policy or runbook in the library that demonstrates the control's implementation.

**Roadmap planning.** As the library expands in future releases, the framework mapping shows the trajectory of expanded coverage. Adopting organizations can plan their own program maturity in alignment with the library's growth, prioritizing internal work in areas where library coverage is forthcoming.

The mapping is a living document. As the library expands, the mapping is updated to reflect the new coverage. Adopting organizations should consult the latest version of this document when planning major program updates.

---

*Framework alignment is the language of audit-defensibility. State the alignment explicitly; do not leave it implicit when writing policies.*
