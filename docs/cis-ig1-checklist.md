# CIS Controls v8.1 Implementation Group 1 Checklist

*Every IG1 safeguard, the library document and section that meets it, and what to show as evidence.*

---

## How to use this checklist

Implementation Group 1 is the set of CIS safeguards the Center for Internet Security describes as essential cyber hygiene: the minimum every organization should have in place, regardless of size. It contains 56 of the 153 safeguards in CIS Controls v8.1.

This checklist answers the question an SMB, its insurer, or its auditor usually asks first: does the program cover IG1? Each row names the safeguard, the library document and section that meets it once adopted, and the evidence that shows it is working. The framework mapping (`docs/framework-mapping.md`) gives the wider view by document; this checklist goes safeguard by safeguard.

**Coverage** describes the library's policy commitments, not your implementation. "Met" means adopting the cited sections commits the organization to the safeguard. "Partial" means the library covers part of it, and the note says what to add. A safeguard is only satisfied in practice when the evidence exists.

To use it as a self-assessment, copy the table, add a column for your status (Implemented, In progress, Not started, or Not applicable with a reason), and fill it in from the evidence column. Most organizations reach IG1 by completing Waves 1 and 2 of the adoption guide (`docs/adoption-guide.md`).

Safeguard titles are paraphrased from CIS Controls v8.1. CIS publishes the authoritative text.

---

## Checklist

| Safeguard | Title | Library document and section | Coverage | Evidence |
|---|---|---|---|---|
| 1.1 | Establish and maintain a detailed enterprise asset inventory | POL-AM-001 Sections 3.1, 3.2, and 3.3 | Met | Current inventory export with owners |
| 1.2 | Address unauthorized assets | POL-AM-001 Sections 3.3 and 3.4 | Met | Reconciliation records showing unknown assets resolved. CIS expects unauthorized assets to be addressed at least weekly; set the review of unknown devices in the continuous refresh to that cadence. |
| 2.1 | Establish and maintain a software inventory | POL-AM-001 Sections 3.2 and 3.4; STD-AM-001 Section 3.1 | Met | Software and SaaS inventory |
| 2.2 | Ensure authorized software is currently supported | POL-AM-001 Section 3.4; POL-EP-001 Section 3.9 | Met | Inventory flags for unsupported software, with exceptions recorded |
| 2.3 | Address unauthorized software | POL-AUP-001 Section 3.8; POL-EP-001 Section 3.5; STD-AM-001 Section 3.11 | Met | Records of unauthorized software found and removed, reviewed at least monthly |
| 3.1 | Establish and maintain a data management process | POL-DC-001 Sections 3.1 through 3.9 | Met | Adopted policy with named data owners |
| 3.2 | Establish and maintain a data inventory | POL-DC-001 Section 3.7; STD-AM-001 Section 3.1 | Met | Data owners' records of where Confidential and Restricted data is stored, reviewed annually, plus the SaaS inventory's classification column |
| 3.3 | Configure data access control lists | POL-IAM-001 Section 3.2; POL-DC-001 Sections 3.5 and 3.6; STD-AM-001 Section 3.5 | Met | Access reviews (TPL-IAM-002) and sharing settings |
| 3.4 | Enforce data retention | POL-DC-001 Section 3.7; STD-DR-001 Section 3.5 | Met | Retention set by data owners and configured in storage and backup |
| 3.5 | Securely dispose of data | POL-AM-001 Section 3.5; POL-DC-001 Sections 3.5 and 3.6; POL-PPS-001 Section 3.4 | Met | Device wipe and disposal records; shredding arrangements |
| 3.6 | Encrypt data on end-user devices | POL-EP-001 Section 3.3; STD-DC-002 Section 3.5 | Met | Device management encryption report; escrowed recovery keys |
| 4.1 | Establish and maintain a secure configuration process | POL-EP-001 Section 3.1; STD-OPS-001 Section 3.8 | Met | Documented baselines and change records for baseline changes |
| 4.2 | Establish and maintain a secure configuration process for network infrastructure | POL-NET-001 Section 3.5 | Met | Network equipment configuration standards and review records |
| 4.3 | Configure automatic session locking on enterprise assets | POL-EP-001 Sections 3.1 and 3.6 | Met | Device management policy showing the lock timers |
| 4.4 | Implement and manage a firewall on servers | POL-EP-001 Section 3.1 | Met | Host firewall policy applied to servers |
| 4.5 | Implement and manage a firewall on end-user devices | POL-EP-001 Section 3.1 | Met | Host firewall policy applied to workstations |
| 4.6 | Securely manage enterprise assets and software | POL-NET-001 Section 3.5; POL-EP-001 Section 3.1; STD-DC-002 Section 3.2 | Met | Management interfaces not exposed; encrypted administrative protocols |
| 4.7 | Manage default accounts on enterprise assets and software | POL-EP-001 Section 3.1; POL-NET-001 Section 3.5 | Met | Default accounts disabled or renamed, and default credentials changed |
| 5.1 | Establish and maintain an inventory of accounts | POL-IAM-001 Section 3.1 | Met | Account inventory, validated in the quarterly review |
| 5.2 | Use unique passwords | STD-IAM-001 Sections 3.1 and 3.3 | Met | Password policy settings; password manager deployment |
| 5.3 | Disable dormant accounts | POL-IAM-001 Section 3.3 | Met | Automatic disablement at forty-five days, or review records |
| 5.4 | Restrict administrator privileges to dedicated administrator accounts | POL-IAM-001 Section 3.5 | Met | Separate administrator accounts; monthly privileged review (TPL-IAM-002 Section 5) |
| 6.1 | Establish an access granting process | POL-IAM-001 Section 3.2 | Met | Access requests with approvals |
| 6.2 | Establish an access revoking process | POL-IAM-001 Section 3.4; POL-PPS-001 Section 3.9 | Met | Departure records showing access removed on the last day |
| 6.3 | Require MFA for externally-exposed applications | STD-IAM-001 Section 3.4; STD-IAM-002 Section 3.5 | Met | Identity provider MFA enforcement report |
| 6.4 | Require MFA for remote network access | POL-IAM-002 Section 3.2 | Met | Remote access configuration requiring MFA |
| 6.5 | Require MFA for administrative access | POL-IAM-001 Section 3.5; STD-IAM-001 Section 3.5 | Met | Phishing-resistant methods on all administrator accounts |
| 7.1 | Establish and maintain a vulnerability management process | POL-VM-001 Sections 3.1 through 3.3 | Met | Adopted policy and scanning configuration |
| 7.2 | Establish and maintain a remediation process | POL-VM-001 Sections 3.3 and 3.4 | Met | Remediation records against the cadences |
| 7.3 | Perform automated operating system patch management | POL-EP-001 Section 3.4 | Met | Patch compliance report |
| 7.4 | Perform automated application patch management | POL-EP-001 Section 3.4 | Met | Application update compliance report |
| 8.1 | Establish and maintain an audit log management process | STD-LOG-001 Sections 3.1 through 3.10 | Met | Adopted standard and log source inventory (TPL-LOG-001) |
| 8.2 | Collect audit logs | STD-LOG-001 Section 3.1 | Met | Log source inventory showing required sources collected |
| 8.3 | Ensure adequate audit log storage | STD-LOG-001 Section 3.5 | Met | Retention settings and storage capacity monitoring |
| 9.1 | Ensure use of only fully supported browsers and email clients | STD-NET-001 Section 3.1 | Met | Approved browser list and version compliance report |
| 9.2 | Use DNS filtering services | POL-NET-001 Section 3.2; STD-NET-001 Section 3.4 | Met | Protective DNS on the network and on managed devices off-network |
| 10.1 | Deploy and maintain anti-malware software | POL-EP-001 Section 3.2 | Met | EDR deployment report covering all managed devices |
| 10.2 | Configure automatic anti-malware signature updates | POL-EP-001 Section 3.2 | Met | EDR update status; devices out of date flagged after seven days |
| 10.3 | Disable autorun and autoplay for removable media | POL-EP-001 Section 3.1 | Met | Device configuration policy |
| 11.1 | Establish and maintain a data recovery process | STD-DR-001 Sections 3.1 through 3.8 | Met | Adopted standard, recovery objectives, and recovery procedures |
| 11.2 | Perform automated backups | STD-DR-001 Section 3.2 | Met | Backup job reports |
| 11.3 | Protect recovery data | STD-DR-001 Section 3.4 | Met | Separate backup credentials, encryption, and deletion protection |
| 11.4 | Establish and maintain an isolated instance of recovery data | STD-DR-001 Section 3.3 | Met | Immutable or offline copy configuration |
| 12.1 | Ensure network infrastructure is up-to-date | POL-NET-001 Section 3.5 | Met | Firmware versions against the POL-VM-001 cadences |
| 14.1 | Establish and maintain a security awareness program | POL-GOV-001 Section 3.8 | Met | Training records and acknowledgment log (TPL-AUP-001) |
| 14.2 | Train workforce members to recognize social engineering attacks | POL-GOV-001 Section 3.8; POL-AUP-001 Section 3.4; STD-NET-001 Section 3.9 | Met | Training content and phishing simulation results |
| 14.3 | Train workforce members on authentication best practices | POL-GOV-001 Section 3.8; POL-AUP-001 Section 3.2 | Met | Training content covering MFA and password managers |
| 14.4 | Train workforce on data handling best practices | POL-GOV-001 Section 3.8; POL-AUP-001 Section 3.3 | Met | Training content covering classification and handling |
| 14.5 | Train workforce members on causes of unintentional data exposure | POL-GOV-001 Section 3.8; POL-AUP-001 Sections 3.3 and 3.4 | Met | Training content covering misdirected email and oversharing |
| 14.6 | Train workforce members on recognizing and reporting security incidents | POL-GOV-001 Section 3.8; POL-AUP-001 Section 3.9 | Met | Training content and the reporting channel |
| 14.7 | Train workforce on how to identify and report if their enterprise assets are missing security updates | POL-GOV-001 Section 3.8; POL-AUP-001 Section 3.9 | Met | Training content covering update prompts and failed updates; reports through the reporting channel |
| 14.8 | Train workforce on the dangers of connecting to and transmitting enterprise data over insecure networks | POL-GOV-001 Section 3.8; POL-IAM-002 Section 3.10; POL-PPS-001 Section 3.5 | Met | Training content covering public Wi-Fi and home networks |
| 15.1 | Establish and maintain an inventory of service providers | POL-TPRM-001 Section 3.1; STD-AM-001 Section 3.1 | Met | Vendor inventory (TPL-GOV-003) |
| 17.1 | Designate personnel to manage incident handling | POL-IR-001 Sections 3.3 and 4 | Met | Named incident lead and deputy |
| 17.2 | Establish and maintain contact information for reporting security incidents | RUN-IR-001 Section 2.1 | Met | Contact list, confirmed quarterly during tabletops (RUN-IR-002) |
| 17.3 | Establish and maintain an enterprise process for reporting incidents | POL-IR-001 Sections 3.1 through 3.3; POL-AUP-001 Section 3.9 | Met | Reporting channel known to users; incident records |

---

## Summary

All 56 IG1 safeguards are met by the library's commitments once the cited sections are adopted. Every one is met by documents in Waves 1 and 2 of the adoption guide except 6.4, which relies on POL-IAM-002 and applies only where staff reach internal systems remotely. Completing those two waves is the practical route to IG1.

---

*Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution 4.0.*
