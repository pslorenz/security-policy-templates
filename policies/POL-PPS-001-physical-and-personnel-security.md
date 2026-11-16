# POL-PPS-001: Physical and Personnel Security Policy

| | |
|---|---|
| **Document ID** | POL-PPS-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy covers the two parts of security that technical controls cannot handle on their own: the physical spaces where people and equipment are, and the people themselves, from before they are hired until after they leave.

Most of the library assumes that the people with access are who they say they are and that the equipment is where it should be. This policy is what makes those assumptions reasonable. A locked network closet keeps someone from plugging a device into the core switch. A visitor escort keeps a stranger from walking out with a laptop. A confidentiality agreement signed on day one, and an orderly departure on the last day, keep a person's access and obligations matched to their role.

The policy scales with the organization. A firm that works entirely from home and runs on SaaS has little office to protect but still needs the home office, clean desk, and personnel sections. A firm with an office, a server room, and visitors needs all of it.

## 2. Scope

This policy applies to:

Offices, server rooms, network closets, and storage areas that [ORGANIZATION_NAME] occupies or controls. Home offices and other locations where staff work with [ORGANIZATION_NAME] data. Shared and co-working spaces used for [ORGANIZATION_NAME] work. Employees, contractors, interns, and temporary staff, from recruitment through departure.

Cloud services are protected physically by their providers; that protection is assessed through POL-TPRM-001, not this policy.

## 3. Policy Statements

### 3.1 Physical Areas

[ORGANIZATION_NAME]'s premises are divided into three kinds of area:

**Public areas**, such as a reception area, where visitors may be without an escort.

**Staff areas**, where only staff and escorted visitors may be.

**Restricted areas**, such as the server room, network closet, and any space where Restricted data is stored on paper, where only named people may enter.

Restricted areas are locked at all times. Network equipment, servers, and patch panels are in a restricted area or a locked cabinet, never in an open office. Entry to restricted areas is logged, by an electronic access system where one is in place or by a sign-in log where it is not.

### 3.2 Keys, Badges, and Access Devices

Keys, badges, door codes, and alarm codes are issued to named people against a register. The register records who holds what and since when. Access devices are returned on departure, and door and alarm codes known to a departing person are changed when the departure is involuntary or the person had access to restricted areas. The register is reviewed annually, and lost devices are reported and deactivated the same day.

### 3.3 Visitors

Visitors sign in, are told who their host is, and are escorted in staff and restricted areas. Visitor records are kept for [VISITOR_LOG_RETENTION, e.g., one year]. Visitors use the guest wireless network under POL-NET-001 Section 3.4 and do not connect to the corporate network. Contractors working unescorted, such as cleaning or maintenance staff, are named in advance, and their access is limited to the areas and hours their work requires.

Maintenance on IT equipment by outside technicians is supervised, and equipment leaving the premises for repair is wiped of company data first or covered by a contract that protects it.

### 3.4 Clean Desk and Clear Screen

Screens lock when people step away, and automatically under POL-EP-001 Section 3.1. Confidential and Restricted paper is not left on desks, printers, or meeting room tables when unattended, and is locked away at the end of the day. Printouts are collected immediately; where the printers support it, printing of Confidential documents uses secure release. Whiteboards are wiped after meetings that discussed Confidential or Restricted information.

Paper containing Confidential or Restricted information is shredded or placed in locked secure disposal bins, never in ordinary recycling. Devices and media are disposed of under POL-AM-001 Section 3.5.

### 3.5 Home Offices and Remote Work

Staff who work from home or elsewhere outside the office:

Work where Confidential conversations cannot be overheard, or use headphones and avoid naming clients and details in shared spaces. Lock devices when stepping away, including at home. Do not let family members or others use company devices. Keep Confidential and Restricted paper to a minimum, store it securely, and shred it rather than putting it in household recycling. Print at home only when necessary, and only on printers they control. Use secured home networks, with the router's default password changed and current firmware where they control it.

Shared and co-working spaces are treated as public areas: screens are positioned away from others or use privacy filters, devices are never left unattended, and Restricted data is not viewed there.

Organizations handling Controlled Unclassified Information also follow ADD-CMMC-001 Section 4.10 for alternate work sites.

### 3.6 Screening Before Access

People are screened before they are given access to [ORGANIZATION_NAME] systems or data, to a depth proportionate to the access the role involves and permitted by law where they work. At minimum, identity and right to work are verified and references are checked. Roles with privileged access, financial authority, or access to Restricted data receive additional screening appropriate to the role, such as criminal history, employment verification, or credit checks where relevant and lawful.

Screening laws vary by state and country, including rules on consent, timing, and what may be considered. [ORGANIZATION_NAME] defines its screening process with counsel or its HR provider, records it in [SCREENING_PROCESS], and applies the same process to contractors with comparable access, either directly or by contract with the contractor's employer.

### 3.7 Agreements Before Access

Before receiving access, each person signs a confidentiality agreement and acknowledges POL-AUP-001. Contractors and vendors with access to [ORGANIZATION_NAME] data are covered by confidentiality terms in their contracts under POL-TPRM-001 Section 3.3. The confidentiality obligation continues after the person leaves.

### 3.8 Changes in Role

When a person changes roles, their access is adjusted under POL-IAM-001 Section 3.4: access the new role needs is added through the normal process, and access the old role needed but the new one does not is removed. Physical access devices are adjusted at the same time.

### 3.9 Departures

Departures follow a checklist coordinated between HR, the manager, and IT:

Access to systems is removed on the last day, under POL-IAM-001 Section 3.4. Company devices, access devices, and paper records are returned. Accounts and data the person owned are transferred to a named owner. Credentials the person knew for shared or service accounts are rotated, under POL-IAM-003. The person is reminded of their continuing confidentiality obligations.

For involuntary departures, and departures of people with privileged access, HR and IT plan the timing together so that access is removed at the moment the person is told, not afterward. Unusual activity by a departing person, such as large downloads, is reported to the Information Security function and handled under POL-IR-001.

### 3.10 Sanctions

Violations of security policies are handled through a documented sanctions process, proportionate to the seriousness of the violation and whether it was deliberate. The process is applied consistently and recorded. Honest mistakes that are reported promptly are treated as opportunities to fix the process, consistent with POL-AUP-001 Section 3.9.

### 3.11 Awareness

Security awareness training under POL-GOV-001 Section 3.8 includes physical security, tailgating, and recognizing and reporting insider risk, including concerning behavior by colleagues.

### 3.12 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Reviews physical access to restricted areas. Receives reports of physical security incidents and insider concerns.

**HR function (or HR provider).** Defines and runs screening. Manages confidentiality agreements and the departure checklist. Runs the sanctions process.

**Office or facilities manager.** Maintains the access device register and visitor process. Arranges secure disposal.

**IT function (or IT service provider).** Secures equipment in restricted areas. Removes access on departure.

**Managers.** Start the departure checklist. Report concerns about their team members' conduct.

**All staff.** Follow the clean desk, visitor, and home office rules. Challenge or report unescorted strangers. Report lost access devices immediately.

## 5. Enforcement

Violations of this policy may result in disciplinary action under Section 3.10, consistent with [ORGANIZATION_NAME]'s human resources policies.

Specific remediation timelines:

Lost or unreturned access devices: deactivated the same day. Door or alarm codes not changed after a departure that requires it: changed within one business day. Access device register not reviewed in the last year: reviewed within thirty days. Network equipment found outside a locked area: secured within thirty days.

## 6. Related Documents

POL-IAM-001: Access Control Policy (role changes and departures)
POL-IAM-003: Non-Human Identity Governance Policy (shared credential rotation)
POL-AUP-001: Acceptable Use Policy (acknowledgment and reporting)
POL-AM-001: Asset Management Policy (device disposal)
POL-EP-001: Endpoint Protection Policy (screen lock)
POL-NET-001: Network Security Policy (guest network)
POL-DC-001: Data Classification and Handling Policy (paper handling)
POL-TPRM-001: Third-Party Risk Management Policy (contractor terms and cloud provider physical security)
POL-IR-001: Incident Response Policy (insider incidents)
POL-GOV-001: Information Security Policy (training and exceptions)
ADD-CMMC-001: CMMC Level 2 Addendum (CUI environments)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.AA-06 (Physical access to assets is managed, monitored, and enforced commensurate with risk). GV.RR-04 (Cybersecurity is included in human resources practices). PR.AT-01 (Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind), for Section 3.11.

**CIS Controls v8.1:**

The CIS Controls do not address physical or personnel security directly. Sections 3.8 and 3.9 support Safeguards 6.1 (establish an access granting process) and 6.2 (establish an access revoking process), and Section 3.11 supports Safeguard 14.1 (establish and maintain a security awareness program).

**Other frameworks:**

NIST SP 800-171 Revision 2 requirements 3.9.1 and 3.9.2 (personnel security) and 3.10.1 through 3.10.6 (physical protection), for organizations using ADD-CMMC-001. HIPAA Security Rule 45 CFR 164.310(a)(1) (facility access controls), 164.310(b) and (c) (workstation use and security), and 164.308(a)(1)(ii)(C) (sanction policy). SOC 2 CC6.4 (physical access) and CC1.4 (commitment to competence, including screening).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
