# STD-DC-002: Cryptography and Key Management Standard

| | |
|---|---|
| **Document ID** | STD-DC-002 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This standard sets the minimum cryptography [ORGANIZATION_NAME] uses and how it manages the keys and certificates that cryptography depends on. It brings together encryption requirements that are spread across the library and adds the parts none of them covered: algorithm minimums, key handling, certificate management, and validated cryptography where a contract requires it.

Encryption is only as strong as the handling of its keys. A laptop encrypted with a recovery key nobody can find is as lost as an unencrypted one, from the owner's side. A backup encrypted with a key stored on the same server is no protection at all. A certificate that expires on a Saturday takes down a client portal as reliably as an attack. Most cryptographic failures in small organizations are failures of key and certificate management, not of algorithms.

The standard sets floors rather than a full catalog of algorithms, because catalogs age. Where it is silent, current NIST guidance applies.

## 2. Scope

This standard applies to cryptography protecting [ORGANIZATION_NAME] data at rest and in transit, the keys and certificates used for that protection, and code signing and authentication keys. It applies to systems [ORGANIZATION_NAME] operates and, through vendor review under POL-TPRM-001, to services that hold its Confidential and Restricted data.

## 3. Standard Requirements

### 3.1 Where Encryption Is Required

Encryption requirements live in the documents that govern each area. This table is the single place to find them.

| Data or system | Requirement | Source |
|---|---|---|
| Laptops, desktops, and mobile devices | Full-disk or device encryption | POL-EP-001 Section 3.3 |
| Removable media | Encrypted, company-issued media only for Confidential data; blocked for Restricted | POL-EP-001 Section 3.3, STD-DC-001 Section 3.4 |
| Confidential and Restricted data at rest | Encrypted in approved storage | POL-DC-001 Sections 3.5 and 3.6 |
| Data in transit over networks | Encrypted with TLS or equivalent | POL-DC-001 Section 3.5, Section 3.2 of this standard |
| Email between organizations | Opportunistic TLS, enforced for regular recipients of Confidential data; MTA-STS for receiving | POL-DC-001 Section 3.5, STD-NET-001 Section 3.5 |
| Backups | Encrypted, with keys stored separately and recoverable | STD-DR-001 Section 3.4 |
| Logs in immutable archive | Encrypted at rest by the storage platform | STD-LOG-001 |
| Secrets and non-human credentials | Stored in the secrets vault | POL-IAM-003 Section 3.4 |
| Restricted data shared externally | Encrypted through an approved secure sharing method or label | STD-DC-001 Section 3.3 |

### 3.2 Minimum Algorithms and Protocols

**Transport.** TLS 1.2 is the minimum; TLS 1.3 is preferred wherever both ends support it. SSL, TLS 1.0, and TLS 1.1 are disabled. Cipher suites with known weaknesses, including those using RC4, 3DES, or export-grade keys, are disabled. Administrative protocols use encrypted versions only (SSH rather than Telnet, HTTPS rather than HTTP, SFTP rather than FTP).

**Symmetric encryption.** AES with keys of at least 128 bits, in an authenticated mode such as GCM where the implementation allows the choice. AES-256 is used where a contract or regulation calls for it.

**Public-key cryptography.** RSA keys of at least 2048 bits (3072 bits for keys expected to remain in use beyond 2030), or elliptic curve keys on P-256 or stronger curves, or Ed25519.

**Hashing.** SHA-256 or stronger for any security purpose. MD5 and SHA-1 are not used for signatures, certificates, integrity checks, or password storage.

**Password storage** in applications [ORGANIZATION_NAME] builds uses a purpose-built password hashing function (Argon2, scrypt, bcrypt, or PBKDF2 with a high iteration count), under POL-DEV-001.

Configurations that fall below these minimums are found by the vulnerability scanning in POL-VM-001 and remediated on its cadences.

### 3.3 Validated Cryptography

Where a contract, regulation, or framework requires validated cryptography, such as CUI under ADD-CMMC-001 or federal contracts, systems in scope use cryptographic modules validated by the NIST Cryptographic Module Validation Program, configured to operate in their validated mode. The modules relied on and their configuration are recorded in the system security plan or equivalent.

FIPS 140-2 validations moved to the historical list in September 2026, and new procurements and deployments rely on FIPS 140-3 validations. Modules with only historical validations are reviewed for replacement. Confirm the current CMVP guidance before relying on this paragraph, since the transition rules are set by NIST and the contracting agency.

Outside those requirements, [ORGANIZATION_NAME] uses the current, supported cryptography built into its operating systems and platforms, which in mainstream products is generally the same validated code running in its default mode.

### 3.4 Key Generation and Storage

Keys are generated by the platform's key management service, a hardware security module, or a well-established cryptographic library, never by hand or by custom code.

Keys are stored separately from the data they protect: in the platform's key management service, the secrets vault under POL-IAM-003 Section 3.4, or a hardware token. Private keys are never sent by email or chat, stored in source code, or kept in shared folders.

Access to keys is limited to the people and services that need them, follows POL-IAM-001, and is logged where the platform supports it.

### 3.5 Recovery Keys

Device encryption recovery keys are escrowed automatically to the identity provider or device management platform when encryption is enabled, so that IT can recover a device without the user. Access to recovery keys is limited to named IT staff and logged, and retrieving a recovery key is reviewed when it was not prompted by a user's request.

Keys needed to read backups are themselves recoverable when production systems are not, under STD-DR-001 Section 3.4.

### 3.6 Customer-Managed Keys

Most cloud services encrypt data at rest with keys the provider manages, which is appropriate for most organizations. Customer-managed keys, where [ORGANIZATION_NAME] controls the encryption keys inside a cloud service, are used only where a contract or regulation requires them, because losing or misconfiguring those keys can make data permanently unreadable. Where they are used, the key recovery procedure is documented and tested with the annual restore test under STD-DR-001 Section 3.7.

### 3.7 Rotation and Retirement

Keys are rotated on the schedule the platform recommends or the data owner requires, and immediately when compromise is suspected. Signing and encryption keys for long-lived data are retired rather than deleted while data protected by them still needs to be read.

### 3.8 Suspected Key Compromise

A suspected compromise of a private key, encryption key, or signing key is handled as a security incident under POL-IR-001. The key is revoked or disabled, a new key is issued, data and certificates depending on the old key are re-protected, and the systems that held the key are investigated.

### 3.9 Certificates

[ORGANIZATION_NAME] maintains an inventory of the TLS and other certificates it relies on, including those on websites, remote access gateways, email services, internal servers, and federation trust (STD-IAM-002), with each certificate's expiry date and owner. Expiry is monitored, with alerts at least thirty days ahead.

Public TLS certificate lifetimes are shrinking. Under the CA/Browser Forum's schedule, the maximum validity of public certificates fell to 200 days in March 2026 and will fall to 100 days in March 2027 and 47 days in March 2029. Manual renewal does not scale to those lifetimes. Public certificates are renewed automatically, using the ACME protocol or the hosting platform's managed certificates, wherever the system supports it. Systems that cannot automate renewal are listed in the inventory as exceptions, with a named owner and a replacement plan.

Certificates use the key minimums in Section 3.2 and are obtained only from approved certificate authorities. Wildcard certificates are used only where specific certificates are impractical, because one compromised wildcard key exposes every host it covers.

### 3.10 Preparing for Post-Quantum Cryptography

NIST has published post-quantum cryptography standards and plans to deprecate today's public-key algorithms over the coming decade. Small organizations mostly receive this transition through vendor updates rather than doing it themselves. [ORGANIZATION_NAME] prepares by knowing where it depends on public-key cryptography (the certificate inventory in Section 3.9 and the systems in Section 3.1), preferring vendors with published post-quantum roadmaps when making long-term commitments, and applying vendor updates that add post-quantum support. No other action is required by this standard at present.

### 3.11 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Approves certificate authorities, exceptions, and customer-managed key use. Leads response to key compromise.

**IT function (or IT service provider).** Configures encryption and protocols. Manages key services, recovery key escrow, and certificate automation. Maintains the certificate inventory.

**Data and system owners.** Identify contractual or regulatory requirements for validated cryptography or customer-managed keys.

**Developers.** Use established libraries and the minimums in Section 3.2, under POL-DEV-001.

## 5. Enforcement

Specific remediation timelines:

Deprecated protocols (SSL, TLS 1.0, TLS 1.1) enabled on internet-facing systems: disabled within thirty days. Private keys found in email, chat, source code, or shared folders: treated as compromised under Section 3.8. Certificates within fourteen days of expiry without a renewal in progress: escalated to the Information Security function. Device encryption without escrowed recovery keys: escrowed within thirty days.

## 6. Related Documents

POL-DC-001: Data Classification and Handling Policy (the parent policy)
STD-DC-001: Data Loss Prevention Standard (labels and secure sharing)
POL-EP-001: Endpoint Protection Policy (device encryption)
STD-NET-001: Email and Web Browser Protection Standard (email transport security)
STD-DR-001: Data Backup and Recovery Standard (backup encryption and key recovery)
POL-IAM-003: Non-Human Identity Governance Policy (secrets vault)
STD-IAM-002: Single Sign-On and Federation Standard (federation certificates)
POL-DEV-001: Secure Development Policy (cryptography in developed software)
POL-VM-001: Vulnerability Management Policy (detecting weak configurations)
POL-IR-001: Incident Response Policy (key compromise)
ADD-CMMC-001: CMMC Level 2 Addendum (validated cryptography for CUI)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.DS-01 (The confidentiality, integrity, and availability of data-at-rest are protected). PR.DS-02 (The confidentiality, integrity, and availability of data-in-transit are protected). PR.AA-01 (Identities and credentials for authorized users, services, and hardware are managed by the organization), for keys and certificates.

**CIS Controls v8.1:**

Control 3 Data Protection: Safeguards 3.6 (encrypt data on end-user devices), 3.9 (encrypt data on removable media), 3.10 (encrypt sensitive data in transit), 3.11 (encrypt sensitive data at rest).

Control 12 Network Infrastructure Management: Safeguard 12.6 (use of secure network management and communication protocols).

**Other frameworks:**

NIST SP 800-171 Revision 2 requirements 3.13.8 (cryptography for CUI in transit), 3.13.10 (key management), 3.13.11 (FIPS-validated cryptography), 3.13.16 (CUI at rest), and 3.8.6 (cryptography on digital media during transport), for organizations using ADD-CMMC-001. SOC 2 CC6.1 and CC6.7.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
