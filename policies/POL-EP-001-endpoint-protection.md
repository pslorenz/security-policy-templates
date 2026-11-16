# POL-EP-001: Endpoint Protection Policy

| | |
|---|---|
| **Document ID** | POL-EP-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] protects the devices that connect to its systems and data. It covers laptops, desktops, servers, mobile devices, and any other device that touches company resources.

The reason endpoint protection matters is direct. Devices are where users do their work, and where attackers most often gain a foothold. A compromised endpoint is the typical starting point for ransomware, business email compromise, and data theft. Strong endpoint protection does not prevent every attack, but it raises the cost of compromise, catches attacks faster when they happen, and limits the damage when they succeed.

This policy works alongside POL-AM-001 (Asset Management Policy), which tracks what devices exist, and POL-IAM-002 (Remote Access Policy), which defines what devices can connect to company resources. The endpoint protection policy adds the security configuration and protection requirements those devices must meet.

## 2. Scope

This policy applies to all devices that store [ORGANIZATION_NAME] data, access [ORGANIZATION_NAME] systems, or are used to perform [ORGANIZATION_NAME] work. Specifically:

Laptops and desktops issued by [ORGANIZATION_NAME], whether running Windows, macOS, ChromeOS, or Linux. Servers operated by [ORGANIZATION_NAME], whether on-premises, in cloud platforms, or hosted by a service provider. Mobile devices accessing company email, files, or applications, whether company-issued or personal. Tablets used for company work. Embedded and specialized devices where applicable (point-of-sale terminals, kiosks, industrial equipment that connects to company networks).

For personal devices used to access company resources under BYOD arrangements, the requirements are documented in POL-IAM-002 and POL-AUP-001. The endpoint protection requirements in this policy apply where they are technically possible without compromising the personal nature of the device.

The policy does not cover network equipment (routers, switches, firewalls, access points), which is addressed in POL-NET-001.

## 3. Policy Statements

### 3.1 Baseline Configuration

Every endpoint runs a defined baseline configuration appropriate to its operating system and role. The baseline establishes the starting state for security controls and is verified through device management tooling.

Every baseline, on every platform, includes these common elements: automatic screen lock after no more than fifteen minutes of inactivity on laptops, desktops, and servers with interactive sessions; a host-based firewall, managed centrally, with a default-deny inbound rule that allows only the services the device needs; and default accounts disabled, or renamed with their credentials changed, before the device is placed in service.

For Windows endpoints, the baseline includes Group Policy or device management configuration profiles covering BitLocker encryption, the built-in anti-malware and attack surface reduction settings where the EDR platform relies on them, Windows Update configuration, autorun and autoplay disabled for removable media, and App Control for Business (formerly Windows Defender Application Control) or AppLocker where supported.

For macOS endpoints, the baseline is enforced through Mobile Device Management with a configuration profile that includes FileVault encryption, Gatekeeper enforcement, system integrity protection (which is enabled by default and not disabled), and approved security tooling.

For ChromeOS devices, the baseline is enforced through the Google Admin console with a configuration profile that includes verified boot, automatic updates, and approved policy settings. ChromeOS devices have a smaller baseline because the platform's architecture provides much of the protection automatically.

For Linux servers and Linux endpoints, the baseline includes a hardening standard (CIS Benchmarks for the relevant distribution where available), automatic security updates configured, host firewall enabled, and approved security tooling.

For mobile devices, the baseline is enforced through MDM with a configuration profile that includes screen lock with timeout, encryption (which is the default on current iOS and Android), application restrictions where appropriate, and the ability to remotely wipe company data.

The baseline is reviewed annually and updated as the platforms and threats change. Devices that drift from baseline are flagged by the device management tooling for remediation.

### 3.2 Anti-Malware and Endpoint Detection and Response

Every endpoint runs a current anti-malware and endpoint detection and response (EDR) capability appropriate to its operating system. Anti-malware alone (signature-based detection) is no longer sufficient against modern threats. EDR provides behavioral detection, telemetry collection, and response capability.

Approved EDR platforms for [ORGANIZATION_NAME] are [APPROVED_EDR_PLATFORMS, e.g., an EDR platform with behavioral detection, tamper protection, remote isolation, and telemetry export to the central logging platform]. The specific platform is documented in the asset management records for each device.

The EDR configuration:

Receives current threat intelligence and detection rules from the vendor. Runs in active protection mode, not just monitoring mode, on all endpoints. Reports telemetry to the central security operations console. Supports response actions (isolation, file quarantine, process termination) that can be invoked during incident response. Cannot be disabled by the user without administrative authorization.

For ChromeOS devices, the platform's architecture provides much of what traditional EDR provides on other platforms. The requirement is met by the verified boot and automatic update mechanisms inherent to the platform, supplemented by Google Workspace endpoint management visibility.

For servers, the EDR configuration may differ from user endpoints to accommodate server-specific operations. Server-specific configurations are documented and approved.

Anti-malware definitions and EDR detection rules are kept current. Devices that have not received updates in seven days are flagged for investigation.

### 3.3 Disk Encryption

Every endpoint that stores [ORGANIZATION_NAME] data has disk encryption enabled. The encryption is enforced through device management tooling and verified at regular intervals.

Specific implementations:

Windows endpoints use BitLocker with a strong protector (TPM plus PIN for sensitive devices, TPM alone is acceptable for standard devices). Recovery keys are escrowed in the device management system, not stored locally on the device or in user-accessible locations.

macOS endpoints use FileVault. Recovery keys are escrowed through the MDM system.

Linux endpoints use the encryption mechanism appropriate to the distribution and use case. Servers in the cloud use the platform's managed disk encryption, which the major platforms enable at rest by default; the configuration is confirmed rather than assumed, and host-based or customer-managed-key encryption is used where the data classification calls for it. Linux laptops and desktops use LUKS or equivalent.

ChromeOS devices have encryption enabled by default through the platform's design. No additional configuration is required.

Mobile devices use the platform's default encryption, which is enabled by default on current iOS and Android.

External storage media (USB drives, external hard drives) used to store company data are encrypted. The preferred path is to discourage use of external storage by providing adequate cloud storage for the work that would otherwise require it.

### 3.4 Patching and Software Updates

Every endpoint receives operating system and security updates promptly. The patching cadence is documented and enforced through automated tooling where possible.

Default cadences:

Security updates follow the priority tiers and remediation cadences in POL-VM-001 Section 3.3: Critical priority within seven days, High priority within fourteen days, and Medium priority within thirty days of identification. Updates addressing actively exploited vulnerabilities on internet-facing systems follow POL-VM-001 Section 3.5 and may require faster action.

Standard updates (operating system feature updates, application updates without specific security severity): applied within sixty days.

These cadences apply to operating systems and to applications installed on the endpoint. Browsers (which are a primary attack surface) are kept current with the latest stable release.

For servers and other systems where update windows are constrained by operational considerations (uptime requirements, change windows), Medium and Low priority security updates may extend to ninety days without documented exception. Critical and High priority updates that cannot meet the POL-VM-001 cadence get compensating controls within that cadence and a documented exception under Section 3.10.

Devices that cannot be patched (end-of-life operating systems, embedded systems with locked firmware, vendor-managed systems) are documented as exceptions and isolated from the rest of the environment to limit blast radius.

The vulnerability management policy (POL-VM-001) covers the broader process of identifying and prioritizing vulnerabilities. This policy covers the specific operational requirements for keeping endpoints current.

### 3.5 Application Control and Software Installation

Endpoints are configured so that only authorized software runs. The mechanisms vary by platform:

Windows endpoints use App Control for Business, AppLocker, or equivalent application control where the operating system edition supports it, including script rules where the platform supports them. For editions where application control is not available, software installation is restricted through standard user accounts (users do not have local administrator rights) and inventory monitoring through the EDR or device management platform.

macOS endpoints rely on Gatekeeper for code signing enforcement, supplemented by application allowlisting through MDM where the environment requires stricter control.

Linux endpoints rely on the package management system and elevated-privilege restrictions for software installation control.

ChromeOS devices restrict software to Chrome Web Store extensions and Android applications approved through the Google Admin console.

Mobile devices restrict software to the platform's official application stores. Sideloading and developer mode are not permitted on devices accessing company resources.

Standard users do not have administrative rights on their endpoints. Users who require administrative rights to perform their work (developers, IT staff, certain power users) have a separate administrative account, consistent with POL-IAM-001 Section 3.5. Day-to-day work is performed on the standard user account.

The list of approved software is maintained by the IT function, consistent with POL-AUP-001 Section 3.8. Requests for additional software follow the documented approval process.

### 3.6 Mobile Device Management

Mobile devices accessing [ORGANIZATION_NAME] resources are enrolled in the company's mobile device management system. Approved MDM platforms are [APPROVED_MDM_PLATFORMS, e.g., the device management service of the approved productivity platform, or a dedicated MDM that supports the organization's device mix].

MDM configuration enforces:

Screen lock after no more than two minutes of inactivity, consistent with CIS Safeguard 4.3 for mobile devices. Strong authentication on the device (biometric or PIN of sufficient length). Encryption (default on current iOS and Android). The ability to remotely wipe company data without affecting personal data on personal devices. Restrictions on application installation, where appropriate. Compliance verification (jailbroken or rooted devices are blocked from accessing company resources).

For company-issued mobile devices, the MDM may enforce additional restrictions appropriate to the device's role.

For personal devices used for work, MDM enrollment uses a profile that separates company data from personal data. The user retains full control of their personal data; the company has visibility and control only over company data and applications.

### 3.7 Endpoint Logging

Endpoints generate logs that support detection and incident response. Logs include:

Authentication events (sign-in attempts, account lockouts). Application execution events from the EDR or equivalent platform. Privileged action events (administrative logon, privilege escalation, security tool changes). System integrity events (boot integrity, security tool tampering attempts). Network connection events from the EDR where applicable.

Logs are sent to the central logging platform within fifteen minutes of the event. Local logs on the endpoint are retained for at least seven days as a backup. Centralized logs are retained per STD-LOG-001.

The EDR platform telemetry is the primary source of endpoint logging. Native operating system audit logs supplement the EDR telemetry where the EDR does not capture the relevant events.

### 3.8 Lost, Stolen, and Compromised Devices

Devices reported lost, stolen, or compromised receive immediate response.

For lost or stolen devices:

The device is locked or wiped through the MDM or EDR platform. Accounts that the device had cached are reviewed for suspicious activity. Authentication tokens are revoked and re-issued. The device is removed from the asset inventory if recovery is not expected. Where regulations or contracts require notification, the appropriate notifications are made consistent with POL-DC-001 and POL-IR-001.

For compromised devices (suspected malware, suspected unauthorized access, or other security concern):

The device is isolated through the EDR platform within the response timelines defined in POL-IR-001. The user is provided alternate access while the device is investigated. The device is investigated, cleaned, and re-imaged before return to service. Repeated reimaging without root cause identification is not acceptable; the cause is determined and addressed.

Reporting lost, stolen, or compromised devices is the user's responsibility, consistent with POL-AUP-001 Section 3.9.

### 3.9 End-of-Life and Decommissioning

Devices reach end of useful life when they no longer receive security updates, when they are physically failing, or when they are replaced with newer equipment.

When a device is decommissioned:

The device is removed from the asset inventory, the device management system, and any other systems where it is registered. The disk is wiped using a method appropriate to the data classification (per POL-DC-001 Section 3.5 and 3.6, with cryptographic wipe required for devices that stored Restricted data). Devices that cannot be wiped to the appropriate standard have their storage media physically destroyed before disposal. Devices are disposed of through approved channels (vendor return, certified recycling, secure destruction service).

Devices being transferred to another user are wiped and reimaged before transfer. The previous user does not retain access to the device.

For devices returning to a vendor (lease return, warranty replacement), the wipe is performed before return. The vendor's standard reset is not sufficient for Confidential or Restricted data.

### 3.10 Exceptions

Specific situations may require deviation from the standard requirements:

Specialized equipment that cannot run modern endpoint protection (industrial equipment, certain medical devices, legacy systems with specific software dependencies). The exception documents the specific limitation and the compensating controls.

Vendor-managed systems where [ORGANIZATION_NAME] does not control the endpoint configuration. The exception documents the vendor management arrangement and the residual risk.

Personal devices in BYOD arrangements where some endpoint controls cannot be enforced without compromising the personal nature of the device. The exception documents what controls are in place and what is accepted.

Exceptions follow the process in POL-IAM-001 Section 3.10. No exception runs longer than twelve months without renewal. All active exceptions are reviewed quarterly.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Maintains the baseline configurations. Reviews and approves exceptions. Investigates compromised devices.

**IT function (or IT service provider).** Implements the technical controls described in this policy. Maintains the device management and EDR platforms. Responds to lost or stolen device reports. Performs the wipes, reimaging, and decommissioning.

**Department leads and managers.** Ensure their team members comply with the policy. Notify IT promptly when team members leave or change roles. Approve requests for non-standard configurations affecting their teams.

**All users.** Use only [ORGANIZATION_NAME]-approved devices for company work, except as permitted by the BYOD provisions in POL-IAM-002 and POL-AUP-001. Do not disable or interfere with security controls on company devices. Report lost, stolen, or compromised devices immediately. Cooperate with patching and update activities.

## 5. Enforcement

Violations of this policy may result in loss of device access, escalation to the user's manager, and disciplinary action consistent with HR policies. For serious violations involving deliberate disabling of security controls or willful introduction of malware, the violations are treated as security incidents under POL-IR-001.

Specific remediation timelines:

Devices not in baseline configuration: remediated within thirty days of identification. Devices without active EDR: remediated within seven days of identification, or the device is removed from the network. Devices with disk encryption disabled: encryption enabled within seven days of identification. Critical priority security updates not applied within seven days: investigated for cause and escalated per POL-VM-001 Section 5. Lost or stolen devices not reported promptly: addressed through user training and management coaching for first occurrences.

## 6. Related Documents

POL-IAM-001: Access Control Policy
POL-IAM-002: Remote Access Policy (managed device requirements for remote access)
POL-IAM-003: Non-Human Identity Governance Policy (service accounts on endpoints)
POL-AUP-001: Acceptable Use Policy (user responsibilities for endpoints)
POL-AM-001: Asset Management Policy (endpoint inventory)
POL-DC-001: Data Classification and Handling Policy (data on endpoints)
POL-IR-001: Incident Response Policy (compromised endpoint response)
POL-VM-001: Vulnerability Management Policy (broader vulnerability process)
POL-NET-001: Network Security Policy (network-level controls)
STD-LOG-001: Logging and Monitoring Standard (log retention)
STD-NET-001: Email and Web Browser Protection Standard (browser and extension management)
STD-OPS-001: Change Management Standard (changes to baselines)
STD-DR-001: Data Backup and Recovery Standard (endpoints are rebuilt, data is synced)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.PS-01 (Configuration management practices are established and applied). PR.PS-02 (Software is maintained, replaced, and removed commensurate with risk). PR.PS-03 (Hardware is maintained, replaced, and removed commensurate with risk). PR.PS-05 (Installation and execution of unauthorized software are prevented). PR.DS-01 (The confidentiality, integrity, and availability of data-at-rest are protected). DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored).

**CIS Controls v8.1:**

Control 2 Inventory and Control of Software Assets: Safeguards 2.5 (allowlist authorized software) and 2.7 (allowlist authorized scripts), where the platform supports application control.

Control 3 Data Protection: Safeguards 3.6 (encrypt data on end-user devices) and 3.9 (encrypt data on removable media).

Control 4 Secure Configuration of Enterprise Assets and Software: Safeguards 4.1 (establish and maintain a secure configuration process), 4.3 (configure automatic session locking), 4.4 (implement and manage a firewall on servers), 4.5 (implement and manage a firewall on end-user devices), 4.6 (securely manage enterprise assets and software), 4.7 (manage default accounts on enterprise assets and software).

Control 7 Continuous Vulnerability Management: Safeguards 7.3 (perform automated operating system patch management), 7.4 (perform automated application patch management).

Control 10 Malware Defenses: Safeguards 10.1 (deploy and maintain anti-malware software), 10.2 (configure automatic anti-malware signature updates), 10.3 (disable autorun and autoplay for removable media), 10.7 (use behavior-based anti-malware software).

Control 13 Network Monitoring and Defense: Safeguards 13.2 (deploy a host-based intrusion detection solution) and 13.7 (deploy a host-based intrusion prevention solution), both met by the EDR platform in active protection mode.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
