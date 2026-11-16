# Cross-Reference Matrix

A living record of how documents in this library reference one another. The matrix exists to maintain internal consistency as the library evolves. When a document ID changes, when a section is renumbered, or when a new document is added that supersedes existing references, this matrix is the basis for finding and updating every dependent document.

The matrix is updated as part of every release. Contributors adding or modifying documents are expected to update the relevant matrix entries.

---

## How to read this matrix

The matrix is organized by source document. For each document, it lists the other documents that the source references and the nature of the reference. The relationships are categorized as follows.

**Operationalized by:** When a policy points to a runbook or template that operationalizes its requirements. The runbook describes how to execute what the policy requires. Example: POL-IAM-003 is operationalized by RUN-IAM-001.

**Operationalizes:** The reverse direction. The runbook or template that operationalizes a parent policy. Example: RUN-IAM-001 operationalizes POL-IAM-003.

**Implements via:** When a policy depends on a separate standard for technical specifics. The policy makes a high-level requirement; the standard provides the specific technical parameters. Example: POL-IAM-001 implements its authentication requirements via STD-IAM-001.

**Required input:** When a document depends on the output of another document for its execution. Example: TPL-LOG-001 requires the log sources defined in STD-LOG-001.

**Related:** When a document addresses an adjacent topic and is referenced for context. The relationship is informational, not procedural.

**Future related:** When a planned future document will have a relationship with the current document once it is published. Documented now so the relationship is captured before the future document exists.

The matrix is followed by a verification checklist that contributors and adopters can use to confirm cross-reference consistency before publishing a release or completing a customization.

---

## Document relationships

### POL-IAM-001: Access Control Policy

Implements via STD-IAM-001 (Password and Authentication Standard) for specific authentication requirements.

Implements via POL-IAM-002 (Remote Access Policy) for remote access provisions.

Implements via STD-IAM-002 (Single Sign-On and Federation Standard) for application authentication integration.

Implements via POL-IAM-003 (Non-Human Identity Governance Policy) for non-human identity provisions.

Operationalized by TPL-IAM-002 (Quarterly User Access Review) for the recurring access review described in Section 3.3 and the monthly privileged review in Section 3.5.

Related to POL-AUP-001 (Acceptable Use Policy) for user behavior expectations.

Related to POL-AM-001 (Asset Management Policy) for asset-to-identity relationships.

Related to POL-DC-001 (Data Classification and Handling Policy) for access-to-data relationships.

Related to POL-IR-001 (Incident Response Policy) for the exception process and response to access compromise.

Related to POL-EP-001 (Endpoint Protection Policy) for the relationship between user access and managed devices.

Related to POL-VM-001 (Vulnerability Management Policy) for access permissions exposed by vulnerabilities.

Related to POL-NET-001 (Network Security Policy) for network access controls.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor access provisioning.

Related to POL-AI-001 (AI and Agent Governance Policy) for AI agent identity provisions.

### POL-IAM-002: Remote Access Policy

Implements the remote access provisions of POL-IAM-001 (Access Control Policy).

Implements via STD-IAM-001 (Password and Authentication Standard) for remote access authentication requirements.

Implements via STD-IAM-002 (Single Sign-On and Federation Standard) where federation handles authentication for remote-accessed applications.

Related to POL-IAM-003 (Non-Human Identity Governance Policy) where non-human identities are used for remote integration.

Related to POL-AUP-001 (Acceptable Use Policy) for personal device requirements.

Related to POL-AM-001 (Asset Management Policy) for managed device requirements.

Related to POL-EP-001 (Endpoint Protection Policy) for managed device security configuration.

Related to POL-NET-001 (Network Security Policy) which addresses the on-premises and cloud network controls that the remote access policy does not cover.

Related to POL-IR-001 (Incident Response Policy) for response to remote access compromise.

### POL-IAM-003: Non-Human Identity Governance Policy

Implements via STD-IAM-001 (Password and Authentication Standard) for credential strength of non-human identities where shared secrets are unavoidable.

Operationalized by RUN-IAM-001 (Non-Human Identity Discovery Runbook) for inventory production.

Operationalized by TPL-IAM-001 (Quarterly Non-Human Identity Access Review) for the quarterly access review in Section 3.9.

Related to POL-IAM-001 (Access Control Policy) for general access provisions.

Related to POL-IAM-002 (Remote Access Policy) where non-human identities are used for remote integrations.

Related to STD-IAM-002 (Single Sign-On and Federation Standard) where federation creates service principals and application registrations.

Related to POL-AM-001 (Asset Management Policy) for non-human identity inventory.

Related to POL-IR-001 (Incident Response Policy) for response to compromised non-human identities.

Related to POL-EP-001 (Endpoint Protection Policy) for service accounts on endpoints.

Related to POL-AI-001 (AI and Agent Governance Policy): AI connectors and agent identities are governed as non-human identities.

Related to STD-LOG-001 (Logging and Monitoring Standard) for service principal and managed identity sign-in logs and their retention.

### STD-IAM-001: Password and Authentication Standard

Implements the authentication requirements of POL-IAM-001 (Access Control Policy).

Implements the credential strength requirements of POL-IAM-003 (Non-Human Identity Governance Policy) where shared secrets are unavoidable.

Related to POL-IAM-002 (Remote Access Policy) for remote access authentication requirements.

Related to STD-IAM-002 (Single Sign-On and Federation Standard) for federation authentication.

Related to POL-AUP-001 (Acceptable Use Policy) for user account security expectations.

Related to POL-IR-001 (Incident Response Policy) for credential compromise scenarios.

Related to POL-NET-001 (Network Security Policy) for authentication on network equipment.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor authentication requirements.

### STD-IAM-002: Single Sign-On and Federation Standard

Implements the federation requirements of POL-IAM-001 (Access Control Policy).

Implements via STD-IAM-001 (Password and Authentication Standard) for the authentication that flows through federation.

Related to POL-IAM-002 (Remote Access Policy): conditional access rules apply to all federated applications.

Related to POL-IAM-003 (Non-Human Identity Governance Policy): governs the service principals and application registrations created by federation.

Related to POL-AM-001 (Asset Management Policy): cloud and SaaS application inventory.

Related to POL-IR-001 (Incident Response Policy) for response to federation compromise.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor application federation requirements.

### POL-AUP-001: Acceptable Use Policy

Related to POL-IAM-001 (Access Control Policy) for the access control framework user behavior depends on.

Related to STD-IAM-001 (Password and Authentication Standard) for credential security expectations.

Related to POL-IAM-002 (Remote Access Policy) for personal device and remote work expectations.

Related to POL-IAM-003 (Non-Human Identity Governance Policy) for the prohibition on creating non-human identities outside the approved process.

Related to POL-AM-001 (Asset Management Policy) for software installation and asset handling expectations.

Implements via POL-DC-001 (Data Classification and Handling Policy) for the data handling rules referenced in Section 3.3.

Related to POL-IR-001 (Incident Response Policy) for the reporting requirements in Section 3.9.

Related to POL-EP-001 (Endpoint Protection Policy) for user responsibilities for endpoint security.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for user behavior around vendor relationships.

Implemented via POL-AI-001 (AI and Agent Governance Policy), the governance behind Section 3.6.

### TPL-AUP-001: Policy Acknowledgment Form and Log

Operationalizes the acknowledgment requirements in POL-GOV-001 Section 3.8 and POL-AUP-001.

Related to POL-PPS-001 (Physical and Personnel Security Policy), whose confidentiality agreement is signed alongside it, and TPL-GOV-004, which reports the acknowledgment rate.

### POL-AM-001: Asset Management Policy

Related to POL-IAM-001 (Access Control Policy) for asset-to-identity relationships.

Related to STD-IAM-002 (Single Sign-On and Federation Standard) for cloud and SaaS asset integration with the identity provider.

Related to POL-IAM-003 (Non-Human Identity Governance Policy) for non-human identity inventory.

Related to POL-AUP-001 (Acceptable Use Policy) for user behavior around asset handling.

Implements via POL-DC-001 (Data Classification and Handling Policy) for the data handling rules referenced in Section 2.

Required input to POL-VM-001 (Vulnerability Management Policy): the asset inventory is the foundation for vulnerability discovery.

Related to POL-EP-001 (Endpoint Protection Policy) for endpoint inventory.

Related to POL-NET-001 (Network Security Policy) for network equipment inventory.

Related to POL-IR-001 (Incident Response Policy) for asset-aware incident response.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor and SaaS asset tracking.

Implements via STD-AM-001 (SaaS Asset Management Standard) for the SaaS requirements in Section 3.6.

### STD-AM-001: SaaS Asset Management Standard

Implements Section 3.6 of POL-AM-001 (Asset Management Policy).

Implements via STD-IAM-002 (Single Sign-On and Federation Standard) for federation, SCIM, and unsanctioned application discovery.

Implements via POL-IAM-003 (Non-Human Identity Governance Policy) for integrations between applications.

Related to POL-IAM-001 (Access Control Policy) for account removal, access review, and administrator and break-glass rules.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor diligence before onboarding and data deletion at retirement.

Related to POL-DC-001 (Data Classification and Handling Policy) for classification and retention.

Related to POL-AI-001 (AI and Agent Governance Policy) for AI features inside SaaS applications.

Related to STD-LOG-001 (Logging and Monitoring Standard) for audit log forwarding from Critical applications.

### POL-DC-001: Data Classification and Handling Policy

Related to POL-IAM-001 (Access Control Policy) for access-to-data relationships.

Related to POL-AM-001 (Asset Management Policy): data is one of the asset categories tracked.

Related to POL-AUP-001 (Acceptable Use Policy) for user behavior around data handling.

Related to POL-IR-001 (Incident Response Policy) for data exposure scenarios.

Related to POL-EP-001 (Endpoint Protection Policy) for data on endpoints.

Related to POL-VM-001 (Vulnerability Management Policy) for data sensitivity informing vulnerability prioritization.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for data sharing with vendors.

Implements via STD-DC-001 (Data Loss Prevention Standard) for technical enforcement of the handling rules.

Implements via STD-DR-001 (Data Backup and Recovery Standard) for the backups governed by Section 3.9.

### STD-DC-001: Data Loss Prevention Standard

Implements the handling rules of POL-DC-001 (Data Classification and Handling Policy) through labels, detection rules, and channel enforcement.

Implements via POL-IAM-003 (Non-Human Identity Governance Policy) for rotation of credentials found by secret scanning.

Related to POL-AI-001 (AI and Agent Governance Policy) for the AI tool channel, POL-DEV-001 (Secure Development Policy) for secret scanning in repositories, POL-AUP-001 (Acceptable Use Policy) for the monitoring notice, and POL-IR-001 (Incident Response Policy) for data exposure incidents.

### POL-IR-001: Incident Response Policy

Operationalized by RUN-IR-002 (Tabletop Exercise Facilitation Runbook) for the quarterly exercises in Section 3.10.

Implements via STD-DR-001 (Data Backup and Recovery Standard) for recovery from backups.

Operationalized by RUN-IR-001 (Incident Response Runbook) for response to common SMB incident types.

Related to POL-IAM-001 (Access Control Policy) for the exception process model and access compromise response.

Related to STD-IAM-001 (Password and Authentication Standard) for credential compromise response.

Related to POL-IAM-002 (Remote Access Policy) for remote access compromise response.

Related to POL-IAM-003 (Non-Human Identity Governance Policy) for non-human identity compromise response.

Related to POL-AUP-001 (Acceptable Use Policy) for the reporting expectations.

Related to POL-AM-001 (Asset Management Policy) for asset-aware incident response.

Related to POL-DC-001 (Data Classification and Handling Policy) for data exposure scenarios.

Related to POL-EP-001 (Endpoint Protection Policy) for compromised endpoint response.

Related to POL-VM-001 (Vulnerability Management Policy) for response to actively-exploited vulnerabilities.

Related to POL-NET-001 (Network Security Policy) for response to network compromise.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor incident coordination.

Related to STD-LOG-001 (Logging and Monitoring Standard) for evidence retention and alert triage timelines.

### RUN-IR-002: Tabletop Exercise Facilitation Runbook

Operationalizes POL-IR-001 (Incident Response Policy) Section 3.10, the quarterly exercise requirement.

Required input from RUN-IR-001 (Incident Response Runbook): the scenarios test its playbooks, contact list, and authority matrix.

Related to POL-TPRM-001, POL-IAM-001, POL-IAM-003, and POL-AI-001, whose provisions individual scenarios test.

Related to POL-GOV-001 (Information Security Policy) for findings carried to the risk register.

### POL-EP-001: Endpoint Protection Policy

Implements via POL-VM-001 (Vulnerability Management Policy) for the vulnerability management process that informs endpoint patching.

Related to POL-IAM-001 (Access Control Policy) for the relationship between user access and managed devices.

Related to POL-IAM-002 (Remote Access Policy) for managed device requirements.

Related to POL-IAM-003 (Non-Human Identity Governance Policy) for service accounts on endpoints.

Related to POL-AUP-001 (Acceptable Use Policy) for user responsibilities for endpoints.

Related to POL-AM-001 (Asset Management Policy) for endpoint inventory.

Related to POL-DC-001 (Data Classification and Handling Policy) for data on endpoints.

Related to POL-IR-001 (Incident Response Policy) for compromised endpoint response.

Related to POL-NET-001 (Network Security Policy) for the host-level network controls this policy does not cover.

Related to STD-LOG-001 (Logging and Monitoring Standard) for log collection and retention.

### POL-VM-001: Vulnerability Management Policy

Required input from POL-AM-001 (Asset Management Policy): the asset inventory is the foundation for vulnerability discovery.

Related to POL-EP-001 (Endpoint Protection Policy) for endpoint patching cadences.

Related to POL-IR-001 (Incident Response Policy) for response to actively-exploited vulnerabilities.

Related to POL-DC-001 (Data Classification and Handling Policy) for data sensitivity informing prioritization.

Related to POL-NET-001 (Network Security Policy) for network configuration vulnerabilities.

Related to POL-IAM-001 (Access Control Policy) for access permissions exposed by vulnerabilities.

Related to POL-DEV-001 (Secure Development Policy) for vulnerabilities in software the organization develops.

Implements via STD-VM-001 (Security Testing Standard) for control checks and penetration testing.

### STD-VM-001: Security Testing Standard

Implements POL-VM-001 (Vulnerability Management Policy) for testing beyond scanning, scaled by tier.

Related to POL-DEV-001 (Secure Development Policy) for application testing at the Expanded tier.

Required input from STD-AM-001, STD-DR-001, STD-NET-001, POL-IAM-002, and STD-LOG-001, whose controls the quarterly control checks test.

Related to RUN-IR-002 (Tabletop Exercise Facilitation Runbook) and POL-GOV-001 (phishing simulations) for people and process testing.

### POL-NET-001: Network Security Policy

Implements via STD-NET-001 (Email and Web Browser Protection Standard) for filtering off the office network and email protections.

Related to POL-IAM-001 (Access Control Policy) for network access controls.

Related to STD-IAM-001 (Password and Authentication Standard) for authentication on network equipment.

Related to POL-IAM-002 (Remote Access Policy) which addresses the user remote access path this policy does not cover.

Related to POL-AM-001 (Asset Management Policy) for network equipment inventory.

Related to POL-DC-001 (Data Classification and Handling Policy) for data sensitivity informing segmentation.

Related to POL-EP-001 (Endpoint Protection Policy) for host-level network controls.

Related to POL-VM-001 (Vulnerability Management Policy) for network equipment patching.

Related to POL-IR-001 (Incident Response Policy) for response to network compromise.

Related to STD-LOG-001 (Logging and Monitoring Standard) for log collection and retention.

### STD-NET-001: Email and Web Browser Protection Standard

Implements POL-NET-001 (Network Security Policy) Sections 3.2 and 3.3 for devices off the office network, and adds email authentication and inbound filtering.

Implements the browser requirements of POL-EP-001 (Endpoint Protection Policy) and the user email rules of POL-AUP-001 (Acceptable Use Policy).

Related to STD-AM-001 (SaaS Asset Management Standard) for the inventory of services that send email as the organization's domains.

Related to POL-AI-001 (AI and Agent Governance Policy) for AI extensions and impersonation verification.

Related to RUN-IR-001 (Incident Response Runbook) for the business email compromise and phishing playbooks.

### POL-TPRM-001: Third-Party Risk Management Policy

Related to POL-IAM-001 (Access Control Policy) for vendor access provisioning.

Related to STD-IAM-001 (Password and Authentication Standard) for vendor authentication requirements.

Related to POL-AM-001 (Asset Management Policy) for vendor inventory and ongoing tracking.

Related to POL-DC-001 (Data Classification and Handling Policy) for data sharing controls.

Related to POL-IR-001 (Incident Response Policy) for vendor incident response.

Related to POL-AUP-001 (Acceptable Use Policy) for employee responsibilities for vendor relationships.

Related to STD-LOG-001 (Logging and Monitoring Standard) for log collection and retention.

### POL-AI-001: AI and Agent Governance Policy

Implements the AI provisions summarized for users in POL-AUP-001 Section 3.6.

Implements via POL-IAM-003 (Non-Human Identity Governance Policy) for connector and agent identities.

Implements via POL-DC-001 (Data Classification and Handling Policy) for what data may enter which AI tools.

Implements via POL-TPRM-001 (Third-Party Risk Management Policy) for AI vendor review.

Related to STD-IAM-002 (Single Sign-On and Federation Standard) for SSO and shadow application discovery.

Related to POL-IR-001 (Incident Response Policy) and RUN-IR-001 (Incident Response Runbook) for AI-related incidents and impersonation.

Related to STD-LOG-001 (Logging and Monitoring Standard) for agent action logging.

Operationalized by TPL-AI-001 (AI Tool and Agent Inventory) for the inventory and quarterly reconciliation in Section 3.9.

Exceptions follow POL-GOV-001 Section 3.6.

### TPL-AI-001: AI Tool and Agent Inventory

Operationalizes POL-AI-001 Section 3.9, and records the approvals required by Sections 3.2, 3.3, 3.4, and 3.8.

Related to POL-IAM-003 (Non-Human Identity Governance Policy): every connector and agent row links to a non-human identity inventory entry, and both are reviewed in the same quarterly cycle.

Related to TPL-GOV-001 (Risk Register) and TPL-GOV-002 (Exception Register) for findings and exceptions carried out of the reconciliation.

### STD-DR-001: Data Backup and Recovery Standard

Implements the backup provisions of POL-DC-001 (Section 3.9), POL-IR-001 (the recovery phase in Section 3.4), and STD-AM-001 (Section 3.8).

Required input from POL-AM-001 (Asset Management Policy): criticality drives recovery objectives, and the inventory drives backup coverage checks.

Related to RUN-IR-002 (Tabletop Exercise Facilitation Runbook) for exercising recovery decisions, STD-LOG-001 for backup system alerting and the immutable storage pattern, and POL-NET-001 for segmentation of backup infrastructure.

### POL-DEV-001: Secure Development Policy

Applies only where the organization develops software.

Implements via POL-VM-001 (Vulnerability Management Policy) for rating, remediation, and disclosure of vulnerabilities in the organization's own software.

Implements via STD-DC-001 (Data Loss Prevention Standard) for secret scanning.

Related to POL-AI-001 (AI and Agent Governance Policy) for AI features and AI-assisted code, POL-TPRM-001 for outsourced development, and STD-IAM-002 for application authentication.

### ADD-CMMC-001: CMMC Level 2 Addendum

Supplements the library for the CUI environment. Overrides STD-IAM-001 (password composition and reuse), POL-IR-001 (adds DoD incident reporting), POL-TPRM-001 (FedRAMP Moderate equivalency for cloud services), and POL-EP-001 (allowlisting) within that scope.

Required input from TPL-IAM-001, TPL-IAM-002, TPL-LOG-001, TPL-LOG-002, TPL-GOV-001, and RUN-IR-002 for assessment evidence.

Related to docs/framework-mapping.md for the current CMMC program status.

### STD-DC-002: Cryptography and Key Management Standard

Implements the encryption requirements of POL-DC-001 (Data Classification and Handling Policy), and collects those in POL-EP-001, STD-NET-001, and STD-DR-001 into one table.

Implements via POL-IAM-003 (Non-Human Identity Governance Policy) for keys stored in the secrets vault.

Related to STD-IAM-002 (federation certificates), POL-DEV-001 (cryptography in developed software), and ADD-CMMC-001 (validated cryptography for CUI).

### STD-OPS-001: Change Management Standard

Implements the configuration management provisions of POL-EP-001 (Section 3.1), POL-NET-001 (Section 3.5), and STD-AM-001 (Section 3.5): baselines change only through a normal change.

Required input from STD-LOG-001 (Logging and Monitoring Standard): configuration change alerts feed the monthly reconciliation.

Related to POL-IR-001 (Incident Response Policy) for emergency changes under the standing authority matrix, and POL-TPRM-001 for changes made by service providers.

### POL-BC-001: Business Continuity Policy

Operationalized by TPL-BC-001 (Business Continuity Plan).

Implements via STD-DR-001 (Data Backup and Recovery Standard): recovery objectives are set to fit each function's maximum tolerable downtime.

Related to POL-IR-001 (Incident Response Policy), which runs alongside continuity when the cause is a security incident and supplies the out-of-band channel; RUN-IR-002 for annual continuity exercises; and POL-IAM-001 for break-glass credentials held by the organization.

### TPL-BC-001: Business Continuity Plan

Operationalizes POL-BC-001. Related to STD-DR-001 for the system recovery objectives checked in Section 2.

### POL-PPS-001: Physical and Personnel Security Policy

Implements via POL-IAM-001 (Access Control Policy) for role changes and departures.

Related to POL-AUP-001 (acknowledgment and good-faith reporting), POL-IAM-003 (shared credential rotation on departure), POL-AM-001 (disposal), and ADD-CMMC-001 (CUI physical and personnel requirements).

### POL-GOV-001: Information Security Policy

Governs every other policy in the library: approval, review cycle, exception process, and risk acceptance authority.

Implements via POL-TPRM-001 (Third-Party Risk Management Policy) for vendor tiering, diligence, and monitoring.

Implements via STD-LOG-001 (Logging and Monitoring Standard) for the monitoring that program metrics depend on.

Operationalized by the GOV-family templates (risk register, exception register, vendor inventory, quarterly metrics report).

### STD-LOG-001: Logging and Monitoring Standard

Implements the logging requirements of POL-IAM-001, STD-IAM-001, POL-IAM-002, POL-IAM-003, POL-EP-001, and POL-NET-001.

Required input to POL-IR-001 (Incident Response Policy): alert triage timelines follow the POL-IR-001 severity levels, and log retention supports evidence handling.

Operationalized by the LOG-family templates (log source inventory, immutable archive record).

Related to RUN-IAM-001 (Non-Human Identity Discovery Runbook): exported service principal sign-in logs extend the Phase 2 dormancy lookback.

### RUN-IAM-001: Non-Human Identity Discovery Runbook

Operationalizes POL-IAM-003 (Non-Human Identity Governance Policy).

Required input to TPL-IAM-001 (Quarterly Non-Human Identity Access Review): the reconciliation output populates the review worksheet and its change log.

Related to POL-IAM-001 (Access Control Policy) for the general access control framework.

Related to STD-IAM-001 (Password and Authentication Standard) for the credential evaluation criteria used during discovery.

Related to POL-AM-001 (Asset Management Policy) for the broader asset inventory context.

### TPL-IAM-002: Quarterly User Access Review

Operationalizes POL-IAM-001 (Access Control Policy) Sections 3.3, 3.5, and 3.8.

Related to TPL-IAM-001 (Quarterly Non-Human Identity Access Review), which runs in the same quarter for non-human identities.

Related to STD-AM-001 (SaaS Asset Management Standard) for the roster comparison of applications without SCIM.

### TPL-IAM-001: Quarterly Non-Human Identity Access Review

Operationalizes Section 3.9 of POL-IAM-003 (Non-Human Identity Governance Policy), applying the rotation schedule in Section 3.5 and the dormancy thresholds in Section 3.7.

Requires input from RUN-IAM-001 (Non-Human Identity Discovery Runbook): the quarterly reconciliation is the basis for the review.

Related to TPL-AI-001 (AI Tool and Agent Inventory): AI connectors and agent identities are reviewed in this worksheet.

Related to TPL-GOV-001, TPL-GOV-002, and TPL-GOV-004 for findings, exceptions, and the metrics the summary feeds.

Related to STD-LOG-001 (Logging and Monitoring Standard) for the activity data referenced in the review.

### AI Governance Business Owner Explainer (client-facing)

Related to POL-AI-001 (AI and Agent Governance Policy): the explainer translates the policy for executive sponsors and business owners.

Related to TPL-AI-001 (AI Tool and Agent Inventory): the explainer describes the discovery and inventory as part of the program rollout.

### NHI Business Owner Explainer (client-facing)

Related to POL-IAM-003 (Non-Human Identity Governance Policy): the explainer translates the policy for executive sponsors and business owners.

Related to RUN-IAM-001 (Non-Human Identity Discovery Runbook): the explainer references the discovery as part of the program rollout described to leadership.

---

## Family completeness summary

A quick view of which families have content in the library and at what level of completeness.

### IAM (Identity and Access Management): Substantively Complete for v0.1.0

Three policies: POL-IAM-001, POL-IAM-002, POL-IAM-003.

Two standards: STD-IAM-001, STD-IAM-002.

One runbook: RUN-IAM-001.

Two templates: TPL-IAM-001 (Quarterly Non-Human Identity Access Review) and TPL-IAM-002 (Quarterly User Access Review).

One client-facing artifact: NHI Business Owner Explainer.

Candidate topics for future IAM documents, which take the next unused number when written: identity proofing and provisioning, standalone privileged access management, identity governance and lifecycle, and customer or external identity.

Planned but not started: runbooks for the other IAM policies as needed.

### AUP (Acceptable Use): Foundational for v0.1.0

One template: TPL-AUP-001 (Policy Acknowledgment Form and Log).

One policy: POL-AUP-001.

This family is typically a single comprehensive document at SMB scale. Additional documents in this family would be unusual.

### AM (Asset Management): Foundational for v0.1.0

One policy: POL-AM-001.

One standard: STD-AM-001 (SaaS Asset Management Standard).

Planned but not started: an asset reconciliation template to support the quarterly reconciliation described in Section 3.3.

### DC (Data Classification): Foundational for v0.1.0

One policy: POL-DC-001.

Two standards: STD-DC-001 (Data Loss Prevention Standard) and STD-DC-002 (Cryptography and Key Management Standard).

Planned but not started: An accompanying handling matrix template that operationalizes the classification levels into specific tooling and storage choices.

### IR (Incident Response): Foundational for v0.1.0

One policy: POL-IR-001.

Two runbooks: RUN-IR-001 (Incident Response Runbook) covering five common SMB incident types, and RUN-IR-002 (Tabletop Exercise Facilitation Runbook) with seven scenarios.

### EP (Endpoint Protection): Foundational for v0.1.0

One policy: POL-EP-001.

Planned but not started: Companion runbooks for endpoint baseline implementation and EDR deployment.

### VM (Vulnerability Management): Foundational for v0.1.0

One policy: POL-VM-001.

One standard: STD-VM-001 (Security Testing Standard).

Planned but not started: A vulnerability management runbook for the discovery and prioritization workflow.

### NET (Network Security): Foundational for v0.1.0

One policy: POL-NET-001.

One standard: STD-NET-001 (Email and Web Browser Protection Standard).

Planned but not started: A network segmentation runbook for environments migrating from flat networks.

### TPRM (Third-Party Risk Management): Foundational for v0.1.0

One policy: POL-TPRM-001.

The vendor inventory and risk assessment template is TPL-GOV-003, in the GOV family.

### Governance and Logging: Added in v0.2.0

POL-GOV-001 (Information Security Policy), STD-LOG-001 (Logging and Monitoring Standard), and their templates TPL-GOV-001 through TPL-GOV-004 and TPL-LOG-001 and TPL-LOG-002. GOV replaces the GRC family code planned in v0.1.0.

### AI (AI and Agent Governance): Added in v0.2.0

One policy: POL-AI-001. Reviewed semiannually because AI tools change faster than an annual cycle can follow.

One template: TPL-AI-001 (AI Tool and Agent Inventory).

One client-facing artifact: AI Governance Business Owner Explainer.

### DR (Data Backup and Recovery): Added in v0.2.0

One standard: STD-DR-001 (Data Backup and Recovery Standard).

### DEV (Secure Development): Added in v0.2.0

One policy: POL-DEV-001, adopted at one of three levels (scripts and automations, internal applications, internet-facing applications), or not adopted where no code is written.

### OPS (Operations): Added in v0.2.0

One standard: STD-OPS-001 (Change Management Standard).

### BC (Business Continuity): Added in v0.2.0

One policy and one template: POL-BC-001 and TPL-BC-001 (Business Continuity Plan).

### PPS (Physical and Personnel Security): Added in v0.2.0

One policy: POL-PPS-001.

### Framework Addenda: Added in v0.2.0

One addendum: ADD-CMMC-001 (CMMC Level 2). A HIPAA addendum is planned once the Security Rule revision is final.

### Planned Beyond v0.2.0

A HIPAA addendum, runbooks for endpoint baselines, vulnerability triage, and network segmentation, an asset reconciliation template, a data handling matrix template, and additional client-facing explainers.

---

## Consistency verification checklist

Use this checklist before publishing a new release of the library, before completing a customization, or after modifying any document that other documents reference.

### Document ID consistency

- [ ] Every document ID referenced in another document exists in the library or is documented as a planned future addition.
- [ ] Every document ID is referenced consistently (POL-IAM-003, not POL-IAM-11 or POL-IAM-0011).
- [ ] Cross-references that include section numbers reference sections that actually exist in the target document.
- [ ] When a document is renumbered, every cross-reference to it has been updated.

### Terminology consistency

- [ ] Defined terms in the glossary are used consistently across documents. A term defined as "non-human identity" is not also referred to as "service identity" or "machine identity" except where explicitly noted as a synonym.
- [ ] New terms introduced in a document have been added to the glossary.
- [ ] The capitalization of defined terms is consistent within each document. Non-Human Identity, non-human identity, and NHI: pick one and use it consistently.

### Framework alignment consistency

- [ ] Every CIS Controls v8.1 reference uses the v8.1 numbering and naming.
- [ ] Every NIST CSF 2.0 reference uses the 2.0 numbering and naming. The 2.0 release renumbered some categories from 1.1.
- [ ] The framework mapping document reflects the actual coverage of every document in the library.
- [ ] Where documents claim coverage of specific framework controls, the document content actually addresses those controls.

### Placeholder consistency

- [ ] Every document uses the standard placeholder convention ([BRACKETED_UPPERCASE_WITH_UNDERSCORES]).
- [ ] Standard placeholders ([ORGANIZATION_NAME], [POLICY_OWNER], [EXECUTIVE_SPONSOR], [EFFECTIVE_DATE], [REVIEW_DATE], [VERSION]) are used consistently and not replaced with example values.
- [ ] Document-specific placeholders are noted in the document and listed in the customization guide.
- [ ] No placeholder appears in the library with example data filled in. A customization that is later checked in to the public library should have the placeholders restored.

### Voice consistency

- [ ] No corporate-speak, no trying to sell your wares.
- [ ] No product names in placeholders or examples.
- [ ] Statistics are sourced or phrased as practitioner observation.
- [ ] The voice-check commands in CONTRIBUTING.md return no matches, weeding out AI derived rewrites.
- [ ] Numbers under one hundred are spelled out in policy text.
- [ ] American English spelling throughout.

### Structural consistency

- [ ] Every policy follows the standard policy structure (eight numbered sections plus metadata header).
- [ ] Every runbook follows the standard runbook structure (eight numbered sections plus metadata header).
- [ ] Client-facing materials use descriptive filenames and headed sections appropriate to their non-technical audience, without strict numbered sections.
- [ ] Section numbering is consistent within document type.
- [ ] Each document has a complete metadata table at the top, except client-facing materials, which use lighter metadata.
- [ ] Each policy and runbook has a complete revision history at the bottom.
- [ ] Each document ends with the standard closing attribution line, worded exactly as in CONTRIBUTING.md.

---

## When to update the matrix

The matrix is updated in three situations.

**When a new document is added to the library.** The new document's relationships to existing documents are recorded, and existing documents that reference the new one are updated to include the new relationship.

**When an existing document's ID or structure changes.** Every document that references the changed document is reviewed and updated. The verification checklist above is the basis for the review.

**When a new version of the library is released.** A pre-release pass through the matrix confirms that all relationships are accurate as of the release.

The matrix is intended to be a tool for maintaining consistency, not a comprehensive map of every possible relationship between documents. Relationships that are obvious from context (every policy in a library has some relationship to every other policy in some sense) are not enumerated. Relationships that materially affect how a document is used or maintained are enumerated.

---

*Cross-reference consistency is invisible when it works and immediately apparent when it does not. Maintain it.*
