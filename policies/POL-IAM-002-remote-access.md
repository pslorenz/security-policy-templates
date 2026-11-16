# POL-IAM-002: Remote Access Policy

| | |
|---|---|
| **Document ID** | POL-IAM-002 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how people and systems connect to [ORGANIZATION_NAME] resources from outside our offices. It covers employees working from home, contractors connecting from their own networks, vendors needing temporary access, and administrators managing systems from anywhere.

The goal is to make remote access secure without making it painful. Remote work is normal, and the policy is built around that reality.

The traditional approach to remote access (a corporate VPN that puts everyone on a flat internal network) is no longer the right answer. This policy reflects that shift. We use identity-based access controls that grant access to specific resources, not to entire networks.

## 2. Scope

This policy covers all remote access to [ORGANIZATION_NAME] systems and data, including:

Employees and contractors connecting from home or while traveling. Vendor and partner access to specific systems. Administrative access to servers, cloud platforms, and network equipment. Mobile device access to company resources. Connections to systems on premises from cloud services or other partners.

It does not cover access to public-facing applications (a customer connecting to our website) or local network access from inside [ORGANIZATION_NAME] offices, both of which are addressed in other policies.

## 3. Policy Statements

### 3.1 Identity-Based Access Replaces Network-Based Access

Remote access is granted based on who the user is and what they need to do, not based on connecting to a corporate network. This approach is sometimes called Zero Trust Network Access or identity-gated access.

We use a tool that connects authorized users directly to authorized resources without putting them on an internal network. Approved tools for [ORGANIZATION_NAME] are [APPROVED_REMOTE_ACCESS_TOOLS, e.g., an identity-gated access service that integrates with the approved identity provider and enforces per-application access rules].

Traditional corporate VPNs that connect users to a flat internal network are not approved for new deployments. Existing VPN deployments are migrated to identity-gated access on a documented timeline, typically within twelve to eighteen months of the policy effective date.

The reason for this change is straightforward. A flat network gives an attacker who steals one set of credentials access to everything that user could reach. Identity-gated access limits the attacker to the specific resources the user was authorized for, which is usually a small fraction of the network.

### 3.2 Strong Authentication Is Required

Every remote access session requires multi-factor authentication that meets the requirements in STD-IAM-001 (Password and Authentication Standard).

For standard remote access, authenticator app with number matching or stronger is required. Push notifications without number matching are not acceptable for remote access because attackers exploit push fatigue.

For administrative remote access (anyone connecting to perform privileged tasks), phishing-resistant authentication is required. FIDO2 hardware keys, device-bound passkeys, or certificate-based authentication on a managed device, as defined in STD-IAM-001 Section 3.5.

Authentication is performed at the start of every session, and sessions are subject to the inactivity and overall timeouts in STD-IAM-001 Section 3.9. Long-lived sessions that bypass those limits are not permitted for remote access.

### 3.3 Conditional Access Policies Govern Remote Connections

Remote access decisions consider the full context of the connection, not just the credentials. The factors evaluated include:

The user's identity and group membership. The device the user is connecting from (managed or unmanaged, compliant or non-compliant). The location the connection is coming from (expected, unexpected, blocked country). The application or resource being accessed (sensitivity level). The risk signals associated with the user or session (recent password change, unusual sign-in pattern, known compromised credential).

Conditional access rules block, allow, or require additional authentication based on these factors. The specific rules are maintained by the IT or Information Security function and reviewed quarterly.

At minimum, the following conditional access rules are in place:

Sign-ins from countries where [ORGANIZATION_NAME] does not operate are blocked unless an explicit exception applies. Sign-ins from unmanaged devices are restricted to specific low-risk applications. Sign-ins flagged as high-risk by the identity provider trigger additional authentication or are blocked. Administrative actions require phishing-resistant authentication regardless of the device or location.

### 3.4 Devices Used for Remote Access Must Meet Minimum Standards

Devices that connect to [ORGANIZATION_NAME] systems remotely must meet baseline requirements. The requirements differ for managed and unmanaged devices.

**Managed devices** (laptops or workstations issued by [ORGANIZATION_NAME] or enrolled in our device management system) must:

Run a current, supported operating system with security patches applied. Have full-disk encryption enabled. Have endpoint protection software installed and active. Be configured to lock after a defined period of inactivity. Be enrolled in [ORGANIZATION_NAME]'s mobile device management or endpoint management system.

**Unmanaged devices** (personal computers, contractor-owned devices, kiosks) may access only a limited set of resources, typically through a web browser with no ability to download or sync data. Specific allowed applications are defined by conditional access policy.

The list of approved managed device types and configurations is maintained by the IT function.

### 3.5 Access Is Time-Bound and Reviewed

Remote access privileges are not permanent. They are tied to the user's role and continued employment.

When a user changes roles, their remote access is reviewed and adjusted to match the new role. When a user leaves [ORGANIZATION_NAME], their remote access is removed at the time of departure, alongside the rest of their access removal under POL-IAM-001 Section 3.4.

Vendor and contractor remote access has an explicit end date set at the time of provisioning. The end date matches the engagement duration. When the engagement ends, the access ends. Ongoing engagements have their remote access reviewed at least annually and renewed if still appropriate.

Privileged remote access (administrative access to servers, cloud platforms, or network equipment) is reviewed monthly and uses just-in-time elevation where the platform supports it.

### 3.6 Administrative Access Has Additional Controls

Administrative remote access carries higher risk than standard user access. The following additional controls apply:

Administrative remote access uses a separate identity from the user's standard account, consistent with POL-IAM-001 Section 3.5. Administrative remote access uses phishing-resistant authentication as described in Section 3.2. Administrative remote access uses just-in-time elevation where the platform supports it, through the identity provider's or cloud platform's privileged access features or a dedicated privileged access tool. Administrative sessions are recorded where the platform supports it, and the recordings are retained per STD-LOG-001. Administrative access from unmanaged devices is not permitted outside the break-glass procedure below. A managed device is required.

If an administrator is traveling without their managed device and an emergency requires administrative access, the break-glass procedure in POL-IAM-001 Section 3.7 is used. Use of the break-glass procedure is logged and reviewed within twenty-four hours.

### 3.7 Mobile Device Access

Mobile devices (smartphones, tablets) accessing [ORGANIZATION_NAME] resources follow these requirements:

Devices accessing email, calendar, or files require enrollment in mobile device management. The device management policy enforces a screen lock, encryption, and the ability to remotely wipe company data if the device is lost. Personal devices used for work are enrolled with separation between personal and company data. The company can wipe its data without affecting the user's personal data. Devices that have been jailbroken, rooted, or otherwise had their security controls bypassed are blocked.

Mobile device access does not require a separate VPN or remote access tool. Authentication and conditional access rules apply at the application level (Microsoft 365 mobile apps, Google Workspace mobile apps, approved business applications).

### 3.8 Vendor and Third-Party Remote Access

Vendors, contractors, and other third parties needing remote access follow the same requirements as employees, with three additions:

Vendor accounts are documented and tied to a specific engagement, project, or system. Vendor access is granted to the minimum scope needed for the work, with no broader network access. Vendor access has an explicit end date set at provisioning, and is removed at the end date without requiring action from the user.

Vendors performing administrative work follow the administrative remote access rules in Section 3.6, including the requirement for a managed device. Vendors who do not have a managed device may be issued one for the engagement, may use a [ORGANIZATION_NAME]-provided virtual desktop, or may have the engagement scope adjusted to work that does not require administrative access.

### 3.9 Remote Access Logging

All remote access events are logged. That includes:

Session establishment (successful and failed). Authentication events at session start. Resources accessed during the session. Session duration and termination. Any policy violations or unusual activity flagged during the session.

Logs are sent to the central logging platform within fifteen minutes of the event and kept for at least one year. Where regulations require longer retention, the longer requirement applies.

Logs are reviewed for anomalies. Examples include sessions established from impossible locations, sessions accessing resources unusual for the user, and sessions outside normal working hours combined with sensitive actions.

### 3.10 Public Wi-Fi and Untrusted Networks

Users accessing internal [ORGANIZATION_NAME] resources from public Wi-Fi (coffee shops, airports, hotels) or other untrusted networks do so through the approved identity-gated access tool, which encrypts the connection regardless of the underlying network. Cloud and SaaS applications reached directly over the internet rely on their own TLS encryption, as described in Section 3.7.

Users do not transmit sensitive information over an unencrypted connection. The identity-gated access tool for internal resources, and TLS for cloud applications, provide this encryption when used as intended.

Use of personal VPN services to mask remote access traffic is not permitted. Personal VPNs interfere with the identity-gated access tool and may bypass conditional access policies.

### 3.11 Exceptions

Remote access requirements have a small number of legitimate exception scenarios.

A user with a documented disability that prevents the use of a standard MFA method may use an alternate method approved by the Information Security function. The alternate method is at least as strong as the standard requirement.

A vendor system that does not support modern remote access protocols may require a temporary alternate connection method. The exception is time-bound, the alternate method is documented, and the vendor is required to update to a supported method within a defined timeline.

Emergency situations may require deviation from the standard process. Deviations are documented after the fact and reviewed within forty-eight hours.

All exceptions follow the exception process in POL-IAM-001 Section 3.10.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Maintains the conditional access rules. Investigates remote access anomalies. Approves exceptions.

**IT function (or IT service provider).** Implements the identity-gated access tool. Configures conditional access policies. Manages the device enrollment system. Provisions and deprovisions remote access.

**Managers.** Approve remote access requests for their team members. Notify IT promptly when team members change roles or leave.

**System owners.** Define what level of remote access is appropriate for their systems. Approve vendor or third-party access to their systems.

**All users.** Use the approved remote access tools. Keep their managed devices current and compliant. Report lost devices, suspected account compromise, or any unusual remote access activity immediately.

## 5. Enforcement

Violations of this policy may result in loss of remote access, escalation to the user's manager, and disciplinary action consistent with [ORGANIZATION_NAME]'s human resources policies. For contractors and vendors, violations may result in contract termination.

Specific remediation timelines:

Remote access without MFA: enabled within thirty days, or the access is disabled. Administrative remote access without phishing-resistant authentication: enabled within thirty days, or the user is restricted to non-administrative tasks, consistent with POL-IAM-001 Section 5. Remote access through a non-approved tool (personal VPN, unsanctioned remote access software): the access is blocked, and the user is migrated to the approved tool within fourteen days. Unmanaged device accessing restricted resources: device is enrolled or the access is removed within seven days. Vendor access without an end date: end date documented or access removed within thirty days.

## 6. Related Documents

POL-IAM-001: Access Control Policy (the parent policy this remote access policy supports)
STD-IAM-001: Password and Authentication Standard (specific authentication requirements)
STD-IAM-002: Single Sign-On and Federation Standard (how applications integrate with the identity provider)
POL-IAM-003: Non-Human Identity Governance Policy (service accounts and automation, including those used for remote integration)
POL-EP-001: Endpoint Protection Policy (managed device requirements)
POL-AUP-001: Acceptable Use Policy
POL-IR-001: Incident Response Policy

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.AA-01 (Identities and credentials for authorized users, services, and hardware are managed by the organization). PR.AA-03 (Users, services, and hardware are authenticated). PR.AA-05 (Access permissions, entitlements, and authorizations are defined and managed). PR.IR-01 (Networks and environments are protected from unauthorized logical access). DE.CM-03 (Personnel activity and technology usage are monitored to find potentially adverse events).

**CIS Controls v8.1:**

Control 6 Access Control Management: Safeguards 6.4 (require MFA for remote network access), 6.5 (require MFA for administrative access), 6.7 (centralize access control).

Control 12 Network Infrastructure Management: Safeguards 12.5 (centralize network authentication, authorization, and auditing), 12.6 (use of secure network management and communication protocols), 12.7 (ensure remote devices utilize a VPN and are connecting to an enterprise's AAA infrastructure; this policy meets the safeguard's intent through identity-gated access tied to the identity provider rather than a network VPN).

Control 13 Network Monitoring and Defense: Safeguards 13.5 (manage access control for remote assets).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
