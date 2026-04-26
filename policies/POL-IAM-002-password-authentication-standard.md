# POL-IAM-002: Password and Authentication Standard

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

This standard sets the technical requirements for passwords, multi-factor authentication, and other ways people and systems prove who they are when logging in to [ORGANIZATION_NAME] systems.

It supports the Access Control Policy (POL-IAM-001) by spelling out the specific rules that policy refers to. Where the access control policy says "use strong authentication," this standard tells you what strong authentication looks like.

The guidance follows current best practice from NIST Special Publication 800-63B, the U.S. federal standard for digital identity. Some of the rules will be different from what people remember from older guidance. The differences are deliberate and based on what actually works against modern attacks.

## 2. Scope

This standard covers all passwords and authentication used at [ORGANIZATION_NAME], including:

User passwords for Microsoft 365, Google Workspace, Active Directory, and any other system. Service account passwords and API keys. Multi-factor authentication methods. Recovery codes and backup authentication. Authentication for remote access tools.

It applies to employees, contractors, vendors with access to our systems, and any service account or automated process.

## 3. Standard Requirements

### 3.1 Password Length and Composition

Passwords must be at least fourteen characters long. Longer is better. We recommend using a passphrase of three or four random words rather than a short password with special characters.

We do not require specific character types (uppercase, lowercase, numbers, special characters). Mandatory complexity rules push people toward predictable patterns like "Password1!" that are easier to guess than the rules suggest. Length matters more than complexity.

Passwords are checked against a list of known compromised passwords when they are set or changed. If the password appears on the list, it is rejected and the user picks a different one. Microsoft Entra ID and most modern identity systems do this automatically.

### 3.2 Password Rotation

Standard user passwords do not expire on a schedule. Forced rotation every 90 days makes passwords worse, not better, because people choose easier passwords or reuse them across systems.

Passwords must be changed in three situations:

When there is reason to believe the password has been exposed (a breach notification, suspicious activity on the account, a known phishing event involving the user). When the user is leaving the company or changing roles in a way that ends their need for a specific account. When the password violates this standard (for example, an old password shorter than fourteen characters that predates this policy).

Service account and privileged account credentials are handled differently and are covered in Section 3.7.

### 3.3 Password Storage

Passwords are stored in a password manager. Approved password managers for [ORGANIZATION_NAME] are [APPROVED_PASSWORD_MANAGERS, e.g., 1Password, Bitwarden, Keeper].

Storage in any of these places is prohibited:

Sticky notes, notebooks, or other paper. Spreadsheets or documents on shared drives. Email messages, chat platforms (Teams, Slack, SMS), or any communication tool. Code repositories, configuration files, or anywhere a credential might end up in source control. Browser-saved passwords on shared devices.

Browser-saved passwords on a personal, dedicated device are acceptable when the browser sync is protected by phishing-resistant authentication and the device is encrypted.

### 3.4 Multi-Factor Authentication Is Required

Every account uses multi-factor authentication. There are no exceptions for executives, no exceptions for legacy systems, no exceptions for service accounts that can support it.

Acceptable MFA methods, ranked from strongest to weakest:

**Phishing-resistant** (required for privileged accounts, recommended for everyone): FIDO2 hardware security keys (YubiKey, Google Titan, similar), platform passkeys (Windows Hello for Business, Apple Passkeys, Google Passkeys), certificate-based authentication on a trusted device.

**Acceptable for standard accounts**: Authenticator app with number matching (Microsoft Authenticator, Google Authenticator, Duo, similar), where the user types a number shown on the login screen into the app to confirm the request.

**Acceptable as a backup only**: Authenticator app with simple push approval, where the user just taps "approve." This works against most attacks but can be defeated by push fatigue (an attacker sends repeated push requests until the user taps approve to make them stop).

**Not acceptable**: SMS text messages, voice calls, email-based codes. These can be intercepted or redirected by an attacker who controls a user's phone number or email.

### 3.5 Phishing-Resistant Authentication for Privileged Access

Every privileged account uses phishing-resistant authentication. Privileged accounts include domain administrators, global administrators in Microsoft 365 or Google Workspace, root accounts in cloud platforms, and administrative accounts on financial, HR, or other sensitive systems.

The required methods for privileged access are FIDO2 hardware keys, platform passkeys with hardware-backed attestation, or certificate-based authentication on a managed device.

Push-notification MFA, SMS, and authenticator app codes are not acceptable for privileged access because attacker-in-the-middle phishing kits defeat them. These kits are widely available and inexpensive.

If a privileged system does not support phishing-resistant authentication, we put it behind a system that does (a single sign-on portal, a privileged access management tool, a jump host) within ninety days, or we replace the system within twelve months.

### 3.6 Recovery and Backup Authentication

Every account that has MFA also has a way to recover access if the primary MFA method is lost or broken. The backup must be at least as strong as the primary MFA method.

Acceptable recovery options:

A second FIDO2 key registered to the same account and stored separately from the primary key (in a desk drawer at home if the primary lives on a keychain, or in a small safe). One-time recovery codes generated at MFA enrollment, printed and stored securely (in a sealed envelope in a desk drawer, or in the user's password manager).

Recovery codes must be replaced after use. If a recovery code is used, the account is reviewed for suspicious activity and a new set of codes is generated.

Self-service recovery through SMS or email alone is not acceptable for any account because it bypasses MFA. Self-service recovery must require a strong second factor (a registered backup device, a help-desk identity verification process, or an in-person verification).

### 3.7 Service Account and Non-Human Authentication

Service accounts and automated systems authenticate using mechanisms that do not rely on passwords where the platform supports it. The preferred methods, in order:

**Best**: Managed identities (Azure managed identities, AWS IAM roles, GCP service accounts with workload identity federation). The platform handles credentials automatically; nothing for us to store or rotate.

**Good**: Certificates with automatic rotation through a secrets management platform.

**Acceptable when better options are not available**: API keys or client secrets stored in a secrets management platform (Azure Key Vault, AWS Secrets Manager, HashiCorp Vault, or the secrets feature of an approved password manager) and rotated on a schedule.

**Not acceptable**: Plaintext passwords or keys in source code, configuration files in version control, environment variables on shared systems, scripts or scheduled tasks where the credential is visible.

Service account credentials that cannot be replaced with managed identities or certificates must be rotated on this schedule:

High-privilege credentials (administrator, root, database owner, equivalent): every 90 days.
Standard service credentials: at least annually.
Credentials that have been exposed or are suspected of being exposed: immediately.

POL-IAM-011 (Non-Human Identity Governance Policy) covers the broader governance of service accounts and other non-human identities, including ownership, lifecycle, and access review.

### 3.8 Failed Login Handling

After ten consecutive failed login attempts in a short window, the account is temporarily locked. The lockout lasts thirty minutes, after which the user can try again. This protects against automated password-guessing while not creating help-desk burden from typo-induced lockouts.

For accounts under apparent attack (many failed attempts from many sources), the security team is alerted and may extend the lockout or require a password reset before the account is reactivated.

We do not lock accounts permanently after failed attempts. Permanent lockout creates an opportunity for an attacker to lock out a legitimate user as a denial-of-service attack.

### 3.9 Session Management

Active sessions on [ORGANIZATION_NAME] systems expire after a defined period of inactivity. The default is eight hours for normal user sessions and one hour for sessions with privileged access.

Sessions are terminated when the user signs out, when the device is locked or restarted, or when the session token expires. Sign-out from Microsoft 365 and Google Workspace must invalidate the session everywhere, not just on the current device.

Sessions on systems handling sensitive data (financial, HR, customer data) require re-authentication after thirty minutes of inactivity.

### 3.10 Authentication Logging

Every authentication event is logged. That includes successful logins, failed logins, MFA challenges (issued, satisfied, failed), password changes, MFA method changes, and account lockouts.

Logs are sent to the central logging platform within fifteen minutes of the event and kept for at least one year. Where regulations require longer retention, we follow the longer requirement.

Anomalies in authentication patterns trigger alerts. Examples include impossible travel (a user logging in from two distant locations within a short window), authentication from a country where the user does not normally work, repeated failed MFA challenges followed by a success, and successful authentication followed quickly by sensitive actions.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Reviews authentication logs and investigates anomalies. Approves exceptions. Maintains the list of approved password managers and MFA tools.

**IT function (or IT service provider).** Implements the technical controls that enforce this standard. Provisions FIDO2 keys for privileged users. Configures Conditional Access or equivalent policies. Maintains the secrets management platform.

**Managers.** Ensure their team members understand the requirements. Support team members through MFA enrollment and password manager adoption.

**All users.** Use the approved password manager. Enable MFA on their accounts. Report lost MFA devices or suspected account compromise immediately.

## 5. Enforcement

Violations of this standard may result in account suspension, escalation to the user's manager, and disciplinary action consistent with [ORGANIZATION_NAME]'s human resources policies.

Specific remediation timelines:

Accounts without MFA: enabled within thirty days, or the account is disabled. Privileged accounts using non-phishing-resistant MFA: upgraded within sixty days. Service account credentials in prohibited storage: moved to the secrets management platform within fourteen days; the prohibited storage is sanitized. Passwords below the minimum length: replaced at next login or within thirty days, whichever comes first. Shared credentials: replaced with individual accounts within sixty days.

## 6. Related Documents

POL-IAM-001: Access Control Policy (the parent policy this standard supports)
POL-IAM-011: Non-Human Identity Governance Policy (broader governance of service accounts and automation identities)
POL-AUP-001: Acceptable Use Policy (user behavior expectations)
POL-IR-001: Incident Response Policy (response to credential compromise)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.AA-01 (Identities and credentials are managed). PR.AA-02 (Identities are proofed and bound to credentials). PR.AA-03 (Users, services, and hardware are authenticated). PR.AA-04 (Identity assertions are protected).

**CIS Controls v8:**

Control 5 Account Management: Safeguards 5.2 (use unique passwords), 5.4 (restrict administrator privileges to dedicated administrator accounts).

Control 6 Access Control Management: Safeguards 6.3 (require MFA for externally-exposed applications), 6.4 (require MFA for remote network access), 6.5 (require MFA for administrative access).

**NIST Special Publication 800-63B (Digital Identity Guidelines, Authentication and Lifecycle Management):**

This standard reflects the current guidance in NIST 800-63B, including the move away from mandatory periodic password rotation, the move away from mandatory complexity rules, and the prioritization of phishing-resistant authentication for sensitive use cases.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above. Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution-ShareAlike 4.0.*
