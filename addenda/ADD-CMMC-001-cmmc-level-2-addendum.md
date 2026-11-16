# ADD-CMMC-001: CMMC Level 2 Addendum

| | |
|---|---|
| **Document ID** | ADD-CMMC-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Semiannual, and whenever DoD changes the CMMC program |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Applies to** | The CUI environment defined in [CUI_SCOPE_DOCUMENT] |
| **Framework baseline** | NIST SP 800-171 Revision 2 (110 requirements), as incorporated by 32 CFR Part 170 and DFARS 252.204-7012 |
| **Classification** | Internal |

---

## 1. Purpose and Status

This addendum supplements the library for organizations that handle Controlled Unclassified Information (CUI) under Department of Defense contracts and need to meet CMMC Level 2. It maps the 110 requirements of NIST SP 800-171 Revision 2 to the library, identifies what the library does not cover, and sets the provisions that override library defaults inside the CUI environment.

The addendum is additive. The library's policies still apply everywhere. Within the CUI environment, where this addendum and a library document differ, this addendum governs.

**Status and validation.** The CMMC program changed repeatedly during 2026 and is expected to change again. As of this version, Level 2 is assessed against NIST SP 800-171 Revision 2, which remains the baseline under DFARS 252.204-7012 even though Revision 3 has been published, and DoD has signaled a future rule to transition to Revision 3. DoD suspended the Phase 2 third-party certification requirement in July 2026, and a September 2026 class deviation directed contracting officers to accept Level 1 and Level 2 self-assessments while the program is reviewed. The self-assessment obligations and the 800-171 requirements themselves were not suspended. Validate the current phase, the assessment type each contract requires, and the applicable 800-171 revision against current DoD guidance and the contract before relying on this addendum.

## 2. How to Use This Addendum

**Scope first.** Define the CUI environment before anything else: the people, systems, and locations that store, process, or transmit CUI, and the systems that protect them. A smaller, well-defined enclave is far cheaper to assess than an entire organization. Record the scope in [CUI_SCOPE_DOCUMENT].

**Adopt the library documents in Section 3** for the CUI environment, then add the provisions in Sections 4 and 5.

**Produce the two documents the library does not.** A System Security Plan (SSP) describing how each of the 110 requirements is implemented in the CUI environment (requirement 3.12.4), and a Plan of Action and Milestones (POA&M) for requirements not yet met (3.12.2). The SSP cites the library documents as the policies behind each implementation. Neither the library nor this addendum replaces the SSP; the SSP describes your implementation, and the policies describe your commitments.

**Score honestly.** The DoD Assessment Methodology score, submitted to SPRS, starts at 110 and subtracts weighted points for each requirement not met. Inflated self-assessments carry legal risk under the False Claims Act, and DoD has pursued contractors for them.

## 3. Coverage by Family

| Family | 800-171 requirements | Library documents | Coverage | Main gaps (Section 4) |
|---|---|---|---|---|
| 3.1 Access Control | 22 | POL-IAM-001, POL-IAM-002, STD-IAM-001, STD-IAM-002, POL-EP-001, STD-DC-001 | Partial | Login banners, session lock and termination, CUI flow control, mobile and external system connections, public posting of CUI |
| 3.2 Awareness and Training | 3 | POL-GOV-001, POL-AUP-001 | Partial | Insider threat awareness |
| 3.3 Audit and Accountability | 9 | STD-LOG-001 | Strong | Restricting audit log management to a subset of privileged users |
| 3.4 Configuration Management | 9 | STD-OPS-001, POL-EP-001, POL-AM-001, POL-NET-001, POL-AUP-001 | Partial | Security impact analysis on every change, least functionality |
| 3.5 Identification and Authentication | 11 | POL-IAM-001, STD-IAM-001, POL-IAM-003 | Partial | Password complexity and reuse rules that conflict with library defaults |
| 3.6 Incident Response | 3 | POL-IR-001, RUN-IR-001, RUN-IR-002 | Partial | DoD incident reporting under DFARS 252.204-7012 |
| 3.7 Maintenance | 6 | None | Gap | All six requirements |
| 3.8 Media Protection | 9 | POL-DC-001, STD-DC-002, POL-AM-001, POL-EP-001, STD-DR-001, POL-PPS-001 | Partial | CUI marking, media transport tracking, portable storage ownership |
| 3.9 Personnel Security | 2 | POL-PPS-001, POL-IAM-001 | Strong | None material; record the screening process used for CUI access |
| 3.10 Physical Protection | 6 | POL-PPS-001 | Strong | Monitoring of facility support infrastructure (3.10.2) where the organization controls it |
| 3.11 Risk Assessment | 3 | POL-GOV-001, POL-VM-001 | Strong | None material |
| 3.12 Security Assessment | 4 | POL-GOV-001 | Partial | SSP, POA&M, periodic control assessment |
| 3.13 System and Communications Protection | 16 | POL-NET-001, POL-IAM-002, STD-NET-001, POL-DC-001, STD-DC-002 | Partial | Split tunneling, collaborative devices, mobile code, VoIP |
| 3.14 System and Information Integrity | 7 | POL-VM-001, POL-EP-001, STD-NET-001, STD-LOG-001 | Strong | None material |

Coverage ratings describe whether the library's policy commitments address the family. They say nothing about whether the controls are implemented. An assessor tests implementation.

## 4. Additional Provisions for the CUI Environment

These provisions apply within the CUI environment in addition to the library documents.

### 4.1 Access Control

Systems in the CUI environment display a system use notification before sign-in that states the system contains CUI and that use is monitored (3.1.9). Sessions lock after no more than fifteen minutes of inactivity with a display that hides prior content (3.1.10), and user sessions terminate after a defined condition such as the overall session limit in STD-IAM-001 Section 3.9 (3.1.11). The flow of CUI is controlled so that it moves only to authorized systems and recipients, using the DLP rules in STD-DC-001 for the CUI data type (3.1.3). Mobile devices connect to the CUI environment only when managed and compliant (3.1.18), and CUI on mobile devices is encrypted (3.1.19). Connections to external systems, and use of portable storage on them, are documented and limited (3.1.20, 3.1.21). CUI is never posted to publicly accessible systems, and the people who may post public content are named and trained (3.1.22).

### 4.2 Awareness and Training

Security awareness training for people with access to the CUI environment includes recognizing and reporting potential indicators of insider threat (3.2.3).

### 4.3 Audit and Accountability

Management of audit logging (changing what is logged, retention, and the log platform itself) is limited to a named subset of privileged users who do not administer the systems being logged, where staffing allows (3.3.9).

### 4.4 Configuration Management

Changes follow STD-OPS-001 (3.4.3, 3.4.5), with one addition: in the CUI environment, every normal and standard change records a security impact analysis, not only changes to security controls (3.4.4). Systems are configured to provide only essential capabilities, with unnecessary programs, functions, ports, protocols, and services disabled (3.4.6, 3.4.7). The application control in POL-EP-001 Section 3.5 is applied as allowlisting in the CUI environment (3.4.8).

### 4.5 Identification and Authentication

Revision 2 of 800-171 requires password complexity and a prohibition on reusing recent passwords (3.5.7, 3.5.8), which STD-IAM-001 does not impose because NIST SP 800-63B Revision 4 advises against complexity rules. For accounts in the CUI environment, passwords meet [CUI_PASSWORD_COMPLEXITY, e.g., at least one change of character type from the previous password and the fifteen-character minimum in STD-IAM-001], and the last [CUI_PASSWORD_HISTORY, e.g., twenty-four] passwords cannot be reused. Record the chosen values in the SSP. Temporary passwords require an immediate change at first use (3.5.9), and authenticators are protected with replay-resistant mechanisms for privileged and network access (3.5.4), which the phishing-resistant methods in STD-IAM-001 Section 3.5 satisfy. Multi-factor authentication covers local and network access to privileged accounts and network access to all accounts (3.5.3).

### 4.6 Incident Response

Cyber incidents that affect covered defense information, or the ability to perform operationally critical support, are reported to DoD through the DIBNet portal within seventy-two hours of discovery, as DFARS 252.204-7012 requires. Reporting requires a DoD-approved medium assurance certificate, which is obtained before it is needed. Images of affected systems and relevant monitoring data are preserved for at least ninety days after the report, and malicious software found is submitted to the DoD Cyber Crime Center. These obligations are added to the notification triggers in POL-IR-001 Section 3.6 for the CUI environment (3.6.2), and the incident response capability is tested through the exercises in RUN-IR-002 (3.6.3).

### 4.7 Maintenance

System maintenance in the CUI environment is performed and recorded under a documented process (3.7.1, 3.7.2). Equipment removed for off-site maintenance is sanitized of CUI first (3.7.3). Media containing diagnostic and test programs is checked for malicious code before use (3.7.4). Nonlocal maintenance sessions require multi-factor authentication and are terminated when complete (3.7.5). Maintenance personnel without authorized access are escorted and supervised (3.7.6).

### 4.8 Media Protection

Media containing CUI, paper and digital, is physically controlled and stored securely (3.8.1), access to it is limited to authorized users (3.8.2), and it is sanitized or destroyed before disposal or reuse under the NIST SP 800-88 guidance referenced in POL-AM-001 Section 3.5 (3.8.3). CUI media is marked with the required CUI markings and distribution limitations (3.8.4). Media transported outside controlled areas is tracked, and digital media is encrypted in transport (3.8.5, 3.8.6). Removable media use is controlled (3.8.7), and portable storage with no identifiable owner is prohibited (3.8.8). Backups containing CUI are encrypted and protected under STD-DR-001 Section 3.4 (3.8.9).

### 4.9 Personnel Security

People are screened before they are given access to the CUI environment under POL-PPS-001 Section 3.6, using [CUI_SCREENING_PROCESS] where CUI access calls for more than the role's standard screening (3.9.1). Access is removed on termination or transfer under POL-IAM-001 Section 3.4 (3.9.2).

### 4.10 Physical Protection

POL-PPS-001 Sections 3.1 through 3.5 meet most of this family; the requirements are restated here so the SSP can cite them. Physical access to systems, equipment, and operating environments in the CUI environment is limited to authorized people (3.10.1), and the facility and support infrastructure are protected and monitored (3.10.2). Visitors are escorted and their activity monitored (3.10.3). Physical access logs are kept (3.10.4), and keys, badges, and other physical access devices are controlled (3.10.5). Safeguarding measures apply at alternate work sites, including home offices where CUI is handled (3.10.6). For an organization whose CUI environment is entirely in a cloud service, much of this family is inherited from the provider and documented in the SSP as such; the alternate work site requirement is not.

### 4.11 Security Assessment

Security controls in the CUI environment are assessed at least annually (3.12.1) and monitored on an ongoing basis (3.12.3). The SSP is maintained and updated when the environment changes (3.12.4). Deficiencies go to the POA&M with owners and dates (3.12.2).

### 4.12 System and Communications Protection

Cryptography protecting the confidentiality of CUI uses validated modules under STD-DC-002 Section 3.3 (3.13.11), and keys are managed under STD-DC-002 Sections 3.4 through 3.8 (3.13.10). Most mainstream operating systems and cloud services offer validated modules, but they often must be configured to use them, and the configuration is recorded in the SSP. Remote devices are prevented from split tunneling, so that a device connected to the CUI environment cannot simultaneously reach other networks outside the managed path (3.13.7); where the identity-gated access in POL-IAM-002 is used, document how it meets this requirement. Publicly accessible components are on separate subnetworks (3.13.5). Network connections terminate after a defined period of inactivity (3.13.9). Collaborative computing devices such as cameras and microphones cannot be activated remotely, and users see when they are in use (3.13.12). Mobile code and Voice over IP are controlled and monitored (3.13.13, 3.13.14).

Cloud services that store, process, or transmit covered defense information meet the FedRAMP Moderate baseline or equivalent requirements, as DFARS 252.204-7012 requires. This is a vendor selection requirement under POL-TPRM-001 for any service in the CUI environment, including email, file storage, and backup.

## 5. Overrides of Library Defaults

Within the CUI environment:

| Library default | CUI environment requirement | 800-171 basis |
|---|---|---|
| No password composition rules (STD-IAM-001 Section 3.1) | Complexity and reuse rules in Section 4.5 | 3.5.7, 3.5.8 |
| Validated cryptography only where required (STD-DC-002 Section 3.3) | Validated modules, in validated mode, on every system in the CUI environment | 3.13.11 |
| Incident notification per POL-IR-001 Section 3.6 | Adds 72-hour DIBNet reporting, image preservation, and malware submission | 3.6.2 and DFARS 252.204-7012 |
| Vendor tiering per POL-TPRM-001 | Cloud services handling CUI meet FedRAMP Moderate or equivalent | DFARS 252.204-7012 |
| Application control where the edition supports it (POL-EP-001 Section 3.5) | Allowlisting on all CUI systems | 3.4.8 |

## 6. Assessment Readiness

Before a self-assessment or an assessment by a third party:

The SSP describes each requirement. The SPRS score is calculated with the DoD Assessment Methodology and supported by evidence. POA&M items meet the program's eligibility rules: under 32 CFR Part 170, a conditional Level 2 status requires a minimum score (88 of 110 as of this version), only some requirements may be on a POA&M, and POA&M items close within 180 days. Validate these rules against the current regulation, since they are among the provisions most likely to change.

Evidence comes from the templates in this library where they apply: TPL-IAM-001 and TPL-IAM-002 for access reviews, TPL-LOG-001 and TPL-LOG-002 for logging, TPL-GOV-001 for risk assessment, and the RUN-IR-002 exercise records for incident response testing.

## 7. Related Documents

POL-GOV-001: Information Security Policy (governance, risk assessment, and training)
POL-IAM-001: Access Control Policy
STD-IAM-001: Password and Authentication Standard
POL-IR-001: Incident Response Policy
RUN-IR-002: Tabletop Exercise Facilitation Runbook
STD-LOG-001: Logging and Monitoring Standard
STD-DC-001: Data Loss Prevention Standard
STD-DR-001: Data Backup and Recovery Standard
STD-DC-002: Cryptography and Key Management Standard
STD-OPS-001: Change Management Standard
POL-PPS-001: Physical and Personnel Security Policy
POL-TPRM-001: Third-Party Risk Management Policy
docs/framework-mapping.md: CMMC status summary

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This addendum is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
