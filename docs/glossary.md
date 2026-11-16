# Glossary

Definitions for terms used across the security policy templates library. The glossary exists to ensure consistent meaning across documents. When a term in this glossary is used in a policy, runbook, or template, it carries the meaning defined here unless explicitly redefined in the specific document.

Terms are organized alphabetically within categories. Cross-references between terms are noted where the relationship matters.

---

## Identity and Access

**Account.** An authentication principal in a specific system. An account belongs to either a human user or a non-human identity. Used interchangeably with "identity" in casual reference, though "account" implies the specific system instance and "identity" implies the broader principal.

**AI agent.** An AI tool that takes actions (sending messages, changing records, calling other systems) rather than only producing text for a person to act on. POL-AI-001 Section 3.4 sorts agents into assistive, supervised, and autonomous levels by how much they do without per-action human approval.

**Authentication.** The process of verifying that a presented set of credentials belongs to the claimed identity. Distinct from authorization, which determines what the authenticated identity is permitted to do.

**Authorization.** The process of determining what an authenticated identity is permitted to access or do within a system. Often expressed through role assignments, permissions, scopes, or access control lists.

**Conditional Access.** A policy framework in Microsoft Entra (and equivalent capabilities in other identity providers) that evaluates contextual signals (user, device, location, application, risk) to make access decisions. Used in this library to refer specifically to the Entra capability when the context is Microsoft 365 environments.

**Credential.** Any artifact used to prove an identity's authenticity to a system. Includes passwords, client secrets, API keys, certificates, hardware tokens, biometric templates, and OAuth tokens. Treated as the most sensitive class of data the organization handles.

**Federation.** A trust relationship between an identity provider and a service or application that allows users to authenticate once and access multiple resources. Federation is what makes single sign-on work across systems. See SAML 2.0 and OpenID Connect.

**FIDO2.** A set of specifications for phishing-resistant authentication using public-key cryptography, typically implemented through hardware security keys or authenticators built into the device's operating system. Resistant to adversary-in-the-middle attacks that defeat password-plus-OTP authentication.

**Human identity.** An authentication principal corresponding to a natural person. Distinct from a non-human identity. Each human identity should correspond to exactly one person.

**Identity.** The broader concept of an authentication principal that may have multiple accounts across multiple systems. A human identity may have an Active Directory account, an Entra account, a GitHub account, and a SaaS application account, all representing the same person. The unifying principal is the identity.

**Identity-gated access.** A pattern for granting access to specific resources based on user identity rather than network location. Replaces the traditional VPN model that put authenticated users on a flat internal network. Sometimes called Zero Trust Network Access (ZTNA).

**Just-in-Time access (JIT).** A pattern for granting privileged access only at the moment it is needed, for the minimum duration required, with automatic revocation when the need ends. Replaces standing privilege grants. Implemented in Microsoft Entra through Privileged Identity Management (PIM), in AWS through role-assumption patterns, and in dedicated privileged access tools.

**Least privilege.** The principle that an identity should have the minimum permissions necessary to perform its documented function. A foundational principle of access control. Tested in practice by asking "what is the smallest possible set of permissions that allows this identity to do its job," not "what permissions has it always had."

**Managed identity.** A non-human identity in Microsoft Azure that is provisioned, authenticated, and rotated automatically by the platform. Eliminates the need for stored credentials. Preferred over service principals with client secrets where the workload runs on Azure infrastructure that supports managed identities.

**Model Context Protocol (MCP).** An open protocol for connecting AI tools to data sources and systems through servers that expose tools and data to the model. Each MCP server that reaches company systems is a non-human identity under POL-IAM-003.

**Multi-factor authentication (MFA).** Authentication that requires the user to present two or more factors from different categories: something they know (password), something they have (phone, hardware key), or something they are (biometric). MFA strength varies substantially by mechanism. See phishing-resistant authentication.

**Non-human identity (NHI).** An authentication principal that is not a human user. Includes service accounts, service principals, managed identities, application registrations, API keys, OAuth grants, automation accounts, robotic process automation identities, and authentication tokens issued to AI agents or autonomous workflows. See POL-IAM-003 for full definition and governance requirements.

**OAuth grant.** An authorization an identity (typically a user) gives to a third-party application to access resources on the identity's behalf. Two scopes of grant exist: delegated permissions (the application acts as the user) and application permissions (the application acts on its own).

**OpenID Connect (OIDC).** An authentication protocol layered on top of OAuth 2.0, providing federated authentication for web and mobile applications. The current preferred federation protocol for new applications because it handles modern application patterns more cleanly than SAML 2.0.

**Passkey.** A FIDO2 credential used in place of a password. A device-bound passkey never leaves the device or security key it was created on; a synced passkey is copied between a user's devices by the platform's credential manager. Both are phishing-resistant. See STD-IAM-001 Section 3.5 for which are accepted for privileged access.

**Phishing-resistant authentication.** An authentication mechanism that cannot be defeated by an adversary who intercepts and replays the authentication exchange. FIDO2 (including passkeys) and certificate-based authentication are phishing-resistant; password plus SMS OTP is not. Required for privileged access in this library's policies.

**Privileged access.** Access that allows the identity to make changes that affect the security or operation of systems beyond its own resources. Privileged access is treated more strictly than standard access throughout the library.

**Privileged Identity Management (PIM).** Microsoft Entra's just-in-time access capability for administrative roles. Used in this library to refer specifically to the Entra implementation; other identity providers have equivalent capabilities under different names.

**SAML 2.0.** Security Assertion Markup Language 2.0. A mature federation protocol that exchanges authentication and authorization data between an identity provider and a service provider. Common across enterprise SaaS applications. The library prefers OpenID Connect for new applications but accepts SAML 2.0 where required.

**SCIM (System for Cross-domain Identity Management).** A protocol for automating the exchange of user identity information between identity providers and applications. Enables automatic provisioning, deprovisioning, and updates to user accounts across federated systems.

**Service account.** A non-human identity in Active Directory or another directory service, traditionally used to run applications, services, or scheduled tasks. The on-premises predecessor to cloud service principals and managed identities.

**Service principal.** A non-human identity in Microsoft Entra that represents an application or service. Contrast with a user principal, which represents a human. Service principals are the primary form of non-human identity in M365 and Azure environments.

**Single Sign-On (SSO).** A user experience in which authentication to one system grants access to multiple federated systems without separate logins. The technical mechanism underlying SSO is federation. Bringing applications into SSO is a primary objective of STD-IAM-002.

**Tier-zero, Tier-one, Tier-two.** A classification system for administrative privilege. Tier-zero is the most sensitive (domain controllers, identity provider roots, certificate authorities). Tier-one is server and application administration. Tier-two is workstation administration. Identities and devices used for higher-tier work should not also be used for lower-tier work, to prevent privilege escalation through credential theft. Microsoft's current guidance describes the same idea as the enterprise access model, with control, management, and data planes.

## Data and Assets

**Asset.** Any item of value to the organization that requires protection. Includes information assets (data), systems (servers, endpoints, cloud resources), software (applications, services), and identities. The asset inventory tracks all assets in scope of the security program.

**Asset inventory.** A current, queryable record of all assets in the organization's environment. Distinguished from a CMDB (which tracks procured items) by including all assets observed in runtime, regardless of procurement origin.

**BYOD (Bring Your Own Device).** An arrangement under which employees use personal devices to access company resources. The library's policies accommodate BYOD with specific requirements for separating company data from personal data and limiting company control to company assets on the device.

**CAASM (Cyber Asset Attack Surface Management).** A category of tooling that consolidates asset inventory data from multiple sources (EDR, identity provider, cloud platforms, network discovery) into a unified view. Useful for environments where asset visibility is fragmented across tools.

**CMDB (Configuration Management Database).** A traditional inventory system that tracks procured assets and their configurations. Distinguished from the asset inventory described in this library by typically being procurement-driven rather than runtime-driven. The library prefers runtime-truth approaches but recognizes that some organizations maintain a CMDB.

**Confidential data.** Data whose unauthorized disclosure would cause significant harm to the organization, its clients, or its employees. Includes financial records, employee personal information, client confidential information, and proprietary business information. The middle tier in the library's three-tier classification scheme. See POL-DC-001 for full handling requirements.

**Controlled Unclassified Information (CUI).** Information the U.S. government creates or possesses, or that a contractor handles for it, that requires safeguarding under law, regulation, or government-wide policy but is not classified. Defense contractors handling CUI follow NIST SP 800-171 and CMMC. See ADD-CMMC-001.

**Data classification.** The process of categorizing data by sensitivity to determine appropriate handling, storage, transmission, and access controls. The library uses a three-tier scheme by default (public, confidential, restricted) but accommodates organizations that use more or fewer tiers.

**Data loss prevention (DLP).** Technology that detects sensitive data in email, files, chat, and endpoint activity and warns, blocks, or records when it is about to leave approved locations. Most effective against accidental loss. See STD-DC-001.

**Immutable backup.** A backup copy that cannot be changed or deleted before its retention period ends, even by an administrator with full access to the backup system. The copy that survives a ransomware attack in which the attacker has administrator access. See STD-DR-001 Section 3.3.

**Public data.** Data that has been intentionally released for public consumption. Marketing materials, published research, regulatory filings, public website content. The lowest tier in the library's three-tier classification scheme.

**Recovery point objective (RPO) and recovery time objective (RTO).** The RPO is how much data, measured in time, the business can afford to lose; the RTO is how long it can operate without a system. Both are set by the business owner and drive backup frequency and recovery design. See STD-DR-001 Section 3.1.

**Restricted data.** Data whose unauthorized disclosure would cause severe harm to the organization or trigger regulatory consequences. Includes regulated data (where applicable to the adopting organization), authentication credentials, encryption keys, and the most sensitive client information. The highest tier in the library's three-tier classification scheme. Synonymous in some schemes with "highly confidential" or "secret."

**Sensitive data.** A general term for data that requires protection. Used in this library when the specific classification tier is not material to the discussion. Confidential and restricted data are both sensitive; public data is not.

**Sensitivity label.** A marking applied to documents or other content that identifies its data classification and may trigger automatic handling controls. Productivity platforms implement these as sensitivity or classification labels. Used to support but not replace classification decisions.

## Threat and Defense

**Adversary-in-the-Middle (AiTM).** A phishing technique in which the attacker positions a proxy between the user and the legitimate service, intercepting the authentication exchange and stealing the resulting session. Defeats password-plus-OTP MFA and most push-based MFA. Defeated by phishing-resistant authentication.

**Business Email Compromise (BEC).** A fraud scheme in which an attacker either compromises an executive's email account or impersonates an executive to redirect payments, change wire instructions, or extract sensitive information. Among the highest-cost incident types at SMB scale. See RUN-IR-001 Section 3.2.3 for response procedures.

**CIS Benchmarks.** Configuration baselines published by the Center for Internet Security for common operating systems, cloud platforms, and applications. Used as reference points for hardening configurations.

**CVE (Common Vulnerabilities and Exposures).** A standard identifier for publicly disclosed software vulnerabilities. Each CVE has a unique identifier (for example, CVE-2024-12345) and is referenced by vendors, security tools, and threat intelligence sources.

**CVSS (Common Vulnerability Scoring System).** A numerical score (typically 0 to 10) that rates the technical severity of a vulnerability. CVSS scores measure technical characteristics in isolation; they do not capture environmental context like exposure, exploitability in the wild, or compensating controls. The library treats CVSS as one input to prioritization rather than the deciding factor.

**Detection engineering.** The discipline of building, tuning, and maintaining detection logic that identifies adversary activity in the organization's telemetry. Distinct from detection content consumption (running vendor-provided rules) by emphasizing organization-specific tuning and proactive hypothesis testing.

**DMARC, DKIM, SPF.** Three email authentication standards used together to prevent email spoofing. SPF (Sender Policy Framework) declares which servers can send mail for a domain. DKIM (DomainKeys Identified Mail) cryptographically signs outgoing mail. DMARC (Domain-based Message Authentication, Reporting, and Conformance) tells receivers how to handle mail that fails SPF or DKIM checks. Proper configuration of all three is the foundation of email authentication.

**Egress filtering.** The practice of restricting outbound network traffic to known-permitted destinations. Egress filtering catches ransomware reaching command-and-control infrastructure, data exfiltration to attacker destinations, and malware downloading payloads. The library treats egress filtering as a primary network defense.

**Endpoint Detection and Response (EDR).** A category of security tooling that monitors endpoint activity for indicators of malicious behavior, provides telemetry to security operations, and supports response actions such as isolation.

**EPSS (Exploit Prediction Scoring System).** A probability score that predicts the likelihood a vulnerability will be exploited in the next thirty days. Maintained by FIRST.org. Used as an input to vulnerability prioritization alongside CVSS and KEV listing.

**Identity Threat Detection and Response (ITDR).** A category of security tooling that monitors identity-layer activity for indicators of credential compromise, account takeover, or privilege escalation. Often detects an attack earlier than endpoint detection, because identity misuse frequently precedes endpoint activity.

**Indicator of Compromise (IoC).** A specific artifact that indicates the presence of an adversary in an environment. Examples include known-bad IP addresses, file hashes of malware, registry keys created by specific malware families, and command lines characteristic of specific attack tools.

**KEV (Known Exploited Vulnerabilities catalog).** A list maintained by CISA of vulnerabilities with confirmed active exploitation. KEV listing is a strong signal that a vulnerability requires urgent remediation. The library uses KEV listing as a primary input to vulnerability prioritization.

**Kill chain.** A model describing the stages of an adversary's progression from initial reconnaissance through final impact. Used in detection design to ensure coverage across stages, with the principle that detection earlier in the kill chain is more valuable than detection later.

**Lateral movement.** An adversary's progression from an initial foothold to additional systems within the environment. Often achieved by credential theft, exploitation of trust relationships, or abuse of legitimate administrative tools.

**Mobile Device Management (MDM).** A platform that enforces security policies on mobile devices: encryption, screen lock, application restrictions, and the ability to remotely wipe company data.

**Network segmentation.** The practice of dividing a network into isolated zones with controlled traffic between them. Limits the blast radius of compromise: an attacker who reaches one segment cannot reach the rest without traversing controlled paths. The library treats segmentation as the primary network control that survives even when other controls fail.

**Prompt injection.** An attack in which instructions hidden in content an AI tool reads (an email, a web page, a document) cause the tool to act against the user's intent, such as revealing data or taking an unapproved action. No current model reliably prevents it, which is why POL-AI-001 limits what agents that read untrusted content may do. It is the first entry in the OWASP Top 10 for Large Language Model Applications.

**Ransomware.** Malware that encrypts files and demands payment for decryption. Ransomware response is one of the most consequential incident types covered in RUN-IR-001 Section 3.2.2.

**Secret scanning.** Automated detection of passwords, keys, and tokens in source code, repository history, and collaboration tools, ideally blocking them before they are committed. See STD-DC-001 Section 3.6.

**Security Information and Event Management (SIEM).** A platform that aggregates, indexes, and correlates security telemetry from across the environment. The role of the SIEM in this library's policies is primarily as a log retention and investigation platform; correlation rules are deemphasized in favor of detection engineering against the underlying telemetry.

**Security Orchestration, Automation, and Response (SOAR).** A category of tooling that executes pre-defined response actions in reaction to detection events. Used in this library's incident response policies for the automation of containment actions that have been pre-approved through a Standing Authority Matrix.

**Software bill of materials (SBOM).** A machine-readable list of the third-party components an application contains, generated from the build. Used to find affected applications quickly when a component vulnerability is disclosed. See POL-DEV-001 Section 3.4.

**Zero-day.** A vulnerability that is being exploited before a patch is available. Distinct from a known vulnerability with an available patch that has not yet been deployed. The window between disclosure and patch availability has compressed substantially in recent years, increasing the operational importance of compensating controls (segmentation, identity boundaries, detection) over patch cadence as the primary defense.

## Governance and Process

**Attorney-client privilege.** A legal protection that prevents disclosure of communications between an attorney and client. Some incident response activities are conducted under privilege to protect the organization's legal position. The decision to invoke privilege is made with legal counsel at the start of the response.

**Audit.** A systematic review of the organization's controls against a defined standard, conducted by an internal or external party. Audits produce evidence of control operation and identify gaps or deficiencies for remediation.

**Business continuity plan.** A short document describing how an organization keeps its critical business functions running when the office, a key system, a key person, or a key vendor is unavailable. Distinct from backup and recovery, which restores systems and data. See POL-BC-001 and TPL-BC-001.

**Compensating control.** A control that achieves the same security outcome as a primary control through a different mechanism. Used when the primary control cannot be implemented for technical, regulatory, or business reasons. Compensating controls require documentation justifying their equivalence to the primary control.

**Control.** A specific safeguard implemented to achieve a security objective. May be technical (an access control list, a firewall rule, an encryption requirement), administrative (a policy, a procedure, a training requirement), or physical (a locked door, a security camera).

**Exception.** A documented deviation from a policy requirement, approved by appropriate authority, with compensating controls and a defined expiration date. The library's policies require all exceptions to be tracked, reviewed, and renewed or expired at the documented date.

**Framework.** A structured set of controls and objectives published by a standards body or regulatory authority. The library aligns to CIS Controls v8.1 and NIST Cybersecurity Framework 2.0 by default. Other frameworks (HIPAA Security Rule, PCI DSS, SOC 2, ISO 27001, CMMC, NYDFS) are supported through addenda when produced.

**Fourth party.** A vendor of a vendor: a sub-processor that handles organizational data through a contractual chain rather than a direct relationship. Common in SaaS environments where the chosen vendor uses other services to deliver theirs. Active management of fourth parties is generally beyond SMB scale; awareness and concentration of attention on Tier 1 vendors is the practical scope. See POL-TPRM-001 Section 3.7.

**Incident.** An event that compromises or threatens to compromise the confidentiality, integrity, or availability of organizational systems, data, or operations. The threshold for declaring an incident is intentionally broad in this library; when in doubt, treat the situation as an incident and follow the process. See POL-IR-001 Section 3.1 for the full definition.

**Information Security function.** The role or team within the organization responsible for the security program. May be a dedicated team in larger organizations, a single named individual in smaller organizations, or an outsourced function delivered by an MSP or vCISO. Used as a generic role name throughout the library.

**Managed Service Provider (MSP).** A provider that delivers ongoing IT services to an organization under a recurring service contract. Used in this library to refer to the firm that may be adopting the policy library to deliver services to its clients.

**Maximum tolerable downtime.** How long a business function can stop before the harm to clients, revenue, legal standing, or reputation becomes unacceptable. Set by the function's owner; the recovery time objectives of the systems behind the function must fit inside it. See POL-BC-001 Section 3.1.

**Policy.** A controlled document that defines what the organization commits to doing in a specific area. Approved at the appropriate level of authority, reviewed on a defined cadence, and binding on the organization's personnel and systems.

**Risk acceptance.** A documented decision to accept a known risk rather than remediate it, made by an authority appropriate to the risk's magnitude. Distinct from an exception (which is a deviation from a control with compensating measures) and from risk avoidance (which eliminates the risk by not engaging in the activity).

**Runbook.** An operational document that describes how to execute a specific procedure. Distinct from a policy (which describes what the organization commits to doing) by focusing on the practical how rather than the prescriptive what.

**Standard.** A document that provides specific technical requirements supporting a policy. Where a policy might require strong authentication, a standard specifies the minimum password length, the accepted MFA methods, and the session lifetimes. Standards are typically more detailed and more frequently updated than the policies they support.

**Standard, normal, and emergency changes.** The three change types in STD-OPS-001. Standard changes are pre-approved and only logged; normal changes are approved before they are made; emergency changes are made to restore service or contain an incident and recorded afterward.

**Standing Authority Matrix.** A document that pre-authorizes specific automated containment actions, with defined triggers, scope limits, named approvers, and rollback paths. Allows the security operation to respond at machine speed without case-by-case authorization while maintaining governance. See POL-IR-001 Section 3.5.

**Sub-processor.** A vendor that processes data on behalf of another vendor. Common in SaaS arrangements where the vendor uses other services (cloud platforms, payment processors, AI services) to deliver theirs. See fourth party. Disclosure of critical sub-processors is a Tier 1 vendor expectation in POL-TPRM-001.

**Tabletop exercise.** A structured walkthrough of a hypothetical incident scenario with the response team, conducted as a training and gap-identification exercise rather than a live response. Distinct from a simulation (which executes some response actions) and a live drill (which executes most or all response actions in production).

**Vendor risk management.** The process of evaluating and managing the security risks introduced by third-party vendors who have access to the organization's data, systems, or operations. Often called Third-Party Risk Management (TPRM).

**Vendor tier.** A classification of vendors by the risk they pose to the organization. The library uses three tiers: Tier 1 (significant harm if compromised), Tier 2 (meaningful harm), Tier 3 (limited harm). Tier drives the diligence, contractual protections, and ongoing monitoring applied. See POL-TPRM-001 Section 3.1.

**Vulnerability.** A weakness in a system that could be exploited to cause harm. May be a software defect (a CVE), a configuration error, a process gap, or a human factor. The vulnerability management policy defines how vulnerabilities are identified, prioritized, and remediated.

## Frameworks and References

**CIS Controls v8.1.** The Center for Internet Security's catalog of security controls (version 8.1, released in 2024, which aligned the safeguards to NIST CSF 2.0 and added a Govern security function), organized into eighteen control areas with implementation groups (IG1, IG2, IG3) appropriate to organizations of different sizes and risk profiles. The library aligns to IG1 and IG2 by default.

**CISA (Cybersecurity and Infrastructure Security Agency).** A U.S. federal agency providing threat intelligence, advisories, and incident response guidance. The CISA Known Exploited Vulnerabilities catalog (KEV) is a primary input to the library's vulnerability prioritization approach.

**Implementation Group (IG).** CIS Controls v8.1's classification of safeguards by the size and complexity of the adopting organization. IG1 is the minimum baseline for any organization. IG2 adds safeguards appropriate to organizations with more sensitive data or operations. IG3 adds further safeguards for organizations with high-value assets or regulatory exposure.

**NIST Cybersecurity Framework (CSF) 2.0.** The U.S. National Institute of Standards and Technology's framework for cybersecurity risk management, released in 2024. Organized into six functions: Govern, Identify, Protect, Detect, Respond, and Recover. The library aligns to CSF 2.0 by default.

**NIST SP 800-61.** NIST Special Publication 800-61, the foundational U.S. reference for incident response. Revision 3 (April 2025) replaced the Computer Security Incident Handling Guide with recommendations organized around the NIST CSF 2.0 functions. POL-IR-001 and RUN-IR-001 are consistent with it.

**NIST SP 800-63B.** NIST Special Publication 800-63B, Digital Identity Guidelines: Authentication and Authenticator Management. Revision 4 (July 2025) is the current authoritative guidance on password and authentication practice. STD-IAM-001 reflects Revision 4, including the fifteen-character minimum for single-factor passwords and the prohibition on mandatory periodic rotation and composition rules.

**Subcategory.** A specific outcome statement within a NIST CSF function and category. Subcategories are referenced in policy documents using the standard NIST notation (for example, ID.AM-02, PR.AA-05, DE.CM-01) to indicate which framework outcomes the policy supports.

