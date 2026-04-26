# Cross-Reference Matrix

A living record of how documents in this library reference one another. The matrix exists to maintain internal consistency as the library evolves. When a document ID changes, when a section is renumbered, or when a new document is added that supersedes existing references, this matrix is the basis for finding and updating every dependent document.

The matrix is updated as part of every release. Contributors adding or modifying documents are expected to update the relevant matrix entries.

---

## How to read this matrix

The matrix is organized by source document. For each document, it lists the other documents that the source references and the nature of the reference. The relationships are categorized as follows.

**Operationalized by:** When a policy points to a runbook or template that operationalizes its requirements. The runbook describes how to execute what the policy requires. Example: POL-IAM-011 is operationalized by RUN-IAM-011.

**Operationalizes:** The reverse direction. The runbook or template that operationalizes a parent policy. Example: RUN-IAM-011 operationalizes POL-IAM-011.

**Implements via:** When a policy depends on a separate standard for technical specifics. The policy makes a high-level requirement; the standard provides the specific technical parameters. Example: POL-IAM-001 implements its authentication requirements via POL-IAM-002.

**Required input:** When a document depends on the output of another document for its execution. Example: REV-IAM-011 requires the inventory produced by RUN-IAM-011.

**Related:** When a document addresses an adjacent topic and is referenced for context. The relationship is informational, not procedural.

**Future related:** When a planned future document will have a relationship with the current document once it is published. Documented now so the relationship is captured before the future document exists.

The matrix is followed by a verification checklist that contributors and adopters can use to confirm cross-reference consistency before publishing a release or completing a customization.

---

## Document relationships

### POL-IAM-001: Access Control Policy

Implements via POL-IAM-002 (Password and Authentication Standard) for specific authentication requirements.

Implements via POL-IAM-005 (Remote Access Policy) for remote access provisions.

Implements via POL-IAM-006 (Single Sign-On and Federation Standard) for application authentication integration.

Implements via POL-IAM-011 (Non-Human Identity Governance Policy) for non-human identity provisions.

Operationalized by REV-IAM-001 (Quarterly User Access Review Template) for the recurring access review described in Section 3.3.

Related to POL-AUP-001 (Acceptable Use Policy) for user behavior expectations.

Related to POL-AM-001 (Asset Management Policy) for asset-to-identity relationships.

Related to POL-DC-001 (Data Classification and Handling Policy) for access-to-data relationships.

Related to POL-IR-001 (Incident Response Policy) for the exception process and response to access compromise.

Related to POL-EP-001 (Endpoint Protection Policy) for the relationship between user access and managed devices.

Related to POL-VM-001 (Vulnerability Management Policy) for access permissions exposed by vulnerabilities.

Related to POL-NET-001 (Network Security Policy) for network access controls.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor access provisioning.

Future related to POL-AI-001 (AI and Agent Governance Policy, planned) for AI agent identity provisions.

### POL-IAM-002: Password and Authentication Standard

Implements the authentication requirements of POL-IAM-001 (Access Control Policy).

Implements the credential strength requirements of POL-IAM-011 (Non-Human Identity Governance Policy) where shared secrets are unavoidable.

Related to POL-IAM-005 (Remote Access Policy) for remote access authentication requirements.

Related to POL-IAM-006 (Single Sign-On and Federation Standard) for federation authentication.

Related to POL-AUP-001 (Acceptable Use Policy) for user account security expectations.

Related to POL-IR-001 (Incident Response Policy) for credential compromise scenarios.

Related to POL-NET-001 (Network Security Policy) for authentication on network equipment.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor authentication requirements.

### POL-IAM-005: Remote Access Policy

Implements the remote access provisions of POL-IAM-001 (Access Control Policy).

Implements via POL-IAM-002 (Password and Authentication Standard) for remote access authentication requirements.

Implements via POL-IAM-006 (Single Sign-On and Federation Standard) where federation handles authentication for remote-accessed applications.

Related to POL-IAM-011 (Non-Human Identity Governance Policy) where non-human identities are used for remote integration.

Related to POL-AUP-001 (Acceptable Use Policy) for personal device requirements.

Related to POL-AM-001 (Asset Management Policy) for managed device requirements.

Related to POL-EP-001 (Endpoint Protection Policy) for managed device security configuration.

Related to POL-NET-001 (Network Security Policy) which addresses the on-premises and cloud network controls that the remote access policy does not cover.

Related to POL-IR-001 (Incident Response Policy) for response to remote access compromise.

### POL-IAM-006: Single Sign-On and Federation Standard

Implements the federation requirements of POL-IAM-001 (Access Control Policy).

Implements via POL-IAM-002 (Password and Authentication Standard) for the authentication that flows through federation.

Related to POL-IAM-005 (Remote Access Policy): conditional access rules apply to all federated applications.

Related to POL-IAM-011 (Non-Human Identity Governance Policy): governs the service principals and application registrations created by federation.

Related to POL-AM-001 (Asset Management Policy): cloud and SaaS application inventory.

Related to POL-IR-001 (Incident Response Policy) for response to federation compromise.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor application federation requirements.

### POL-IAM-011: Non-Human Identity Governance Policy

Implements via POL-IAM-002 (Password and Authentication Standard) for credential strength of non-human identities where shared secrets are unavoidable.

Operationalized by RUN-IAM-011 (Non-Human Identity Discovery Runbook) for inventory production.

Operationalized by REV-IAM-011 (Quarterly Non-Human Identity Access Review) for ongoing access review.

Related to POL-IAM-001 (Access Control Policy) for general access provisions.

Related to POL-IAM-005 (Remote Access Policy) where non-human identities are used for remote integrations.

Related to POL-IAM-006 (Single Sign-On and Federation Standard) where federation creates service principals and application registrations.

Related to POL-AM-001 (Asset Management Policy) for non-human identity inventory.

Related to POL-IR-001 (Incident Response Policy) for response to compromised non-human identities.

Related to POL-EP-001 (Endpoint Protection Policy) for service accounts on endpoints.

Future related to POL-AI-001 (AI and Agent Governance Policy, planned) for AI agent identities specifically.

Future related to a planned logging and monitoring standard for the activity logging requirements.

### POL-AUP-001: Acceptable Use Policy

Related to POL-IAM-001 (Access Control Policy) for the access control framework user behavior depends on.

Related to POL-IAM-002 (Password and Authentication Standard) for credential security expectations.

Related to POL-IAM-005 (Remote Access Policy) for personal device and remote work expectations.

Related to POL-IAM-011 (Non-Human Identity Governance Policy) for the prohibition on creating non-human identities outside the approved process.

Related to POL-AM-001 (Asset Management Policy) for software installation and asset handling expectations.

Implements via POL-DC-001 (Data Classification and Handling Policy) for the data handling rules referenced in Section 3.3.

Related to POL-IR-001 (Incident Response Policy) for the reporting requirements in Section 3.9.

Related to POL-EP-001 (Endpoint Protection Policy) for user responsibilities for endpoint security.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for user behavior around vendor relationships.

Future related to a planned AI and Agent Governance Policy that will expand on Section 3.6.

### POL-AM-001: Asset Management Policy

Related to POL-IAM-001 (Access Control Policy) for asset-to-identity relationships.

Related to POL-IAM-006 (Single Sign-On and Federation Standard) for cloud and SaaS asset integration with the identity provider.

Related to POL-IAM-011 (Non-Human Identity Governance Policy) for non-human identity inventory.

Related to POL-AUP-001 (Acceptable Use Policy) for user behavior around asset handling.

Implements via POL-DC-001 (Data Classification and Handling Policy) for the data handling rules referenced in Section 2.

Required input to POL-VM-001 (Vulnerability Management Policy): the asset inventory is the foundation for vulnerability discovery.

Related to POL-EP-001 (Endpoint Protection Policy) for endpoint inventory.

Related to POL-NET-001 (Network Security Policy) for network equipment inventory.

Related to POL-IR-001 (Incident Response Policy) for asset-aware incident response.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor and SaaS asset tracking.

### POL-DC-001: Data Classification and Handling Policy

Related to POL-IAM-001 (Access Control Policy) for access-to-data relationships.

Related to POL-AM-001 (Asset Management Policy): data is one of the asset categories tracked.

Related to POL-AUP-001 (Acceptable Use Policy) for user behavior around data handling.

Related to POL-IR-001 (Incident Response Policy) for data exposure scenarios.

Related to POL-EP-001 (Endpoint Protection Policy) for data on endpoints.

Related to POL-VM-001 (Vulnerability Management Policy) for data sensitivity informing vulnerability prioritization.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for data sharing with vendors.

Future related to a planned data loss prevention standard.

### POL-IR-001: Incident Response Policy

Operationalized by RUN-IR-001 (Incident Response Runbook, forthcoming) for response to common SMB incident types.

Related to POL-IAM-001 (Access Control Policy) for the exception process model and access compromise response.

Related to POL-IAM-002 (Password and Authentication Standard) for credential compromise response.

Related to POL-IAM-005 (Remote Access Policy) for remote access compromise response.

Related to POL-IAM-011 (Non-Human Identity Governance Policy) for non-human identity compromise response.

Related to POL-AUP-001 (Acceptable Use Policy) for the reporting expectations.

Related to POL-AM-001 (Asset Management Policy) for asset-aware incident response.

Related to POL-DC-001 (Data Classification and Handling Policy) for data exposure scenarios.

Related to POL-EP-001 (Endpoint Protection Policy) for compromised endpoint response.

Related to POL-VM-001 (Vulnerability Management Policy) for response to actively-exploited vulnerabilities.

Related to POL-NET-001 (Network Security Policy) for response to network compromise.

Related to POL-TPRM-001 (Third-Party Risk Management Policy) for vendor incident coordination.

Future related to a planned logging and monitoring standard for evidence retention requirements.

### POL-EP-001: Endpoint Protection Policy

Implements via POL-VM-001 (Vulnerability Management Policy) for the vulnerability management process that informs endpoint patching.

Related to POL-IAM-001 (Access Control Policy) for the relationship between user access and managed devices.

Related to POL-IAM-005 (Remote Access Policy) for managed device requirements.

Related to POL-IAM-011 (Non-Human Identity Governance Policy) for service accounts on endpoints.

Related to POL-AUP-001 (Acceptable Use Policy) for user responsibilities for endpoints.

Related to POL-AM-001 (Asset Management Policy) for endpoint inventory.

Related to POL-DC-001 (Data Classification and Handling Policy) for data on endpoints.

Related to POL-IR-001 (Incident Response Policy) for compromised endpoint response.

Related to POL-NET-001 (Network Security Policy) for the host-level network controls this policy does not cover.

Future related to a planned logging and monitoring standard.

### POL-VM-001: Vulnerability Management Policy

Required input from POL-AM-001 (Asset Management Policy): the asset inventory is the foundation for vulnerability discovery.

Related to POL-EP-001 (Endpoint Protection Policy) for endpoint patching cadences.

Related to POL-IR-001 (Incident Response Policy) for response to actively-exploited vulnerabilities.

Related to POL-DC-001 (Data Classification and Handling Policy) for data sensitivity informing prioritization.

Related to POL-NET-001 (Network Security Policy) for network configuration vulnerabilities.

Related to POL-IAM-001 (Access Control Policy) for access permissions exposed by vulnerabilities.

Future related to a planned secure development policy.

### POL-NET-001: Network Security Policy

Related to POL-IAM-001 (Access Control Policy) for network access controls.

Related to POL-IAM-002 (Password and Authentication Standard) for authentication on network equipment.

Related to POL-IAM-005 (Remote Access Policy) which addresses the user remote access path this policy does not cover.

Related to POL-AM-001 (Asset Management Policy) for network equipment inventory.

Related to POL-DC-001 (Data Classification and Handling Policy) for data sensitivity informing segmentation.

Related to POL-EP-001 (Endpoint Protection Policy) for host-level network controls.

Related to POL-VM-001 (Vulnerability Management Policy) for network equipment patching.

Related to POL-IR-001 (Incident Response Policy) for response to network compromise.

Future related to a planned logging and monitoring standard.

### POL-TPRM-001: Third-Party Risk Management Policy

Related to POL-IAM-001 (Access Control Policy) for vendor access provisioning.

Related to POL-IAM-002 (Password and Authentication Standard) for vendor authentication requirements.

Related to POL-AM-001 (Asset Management Policy) for vendor inventory and ongoing tracking.

Related to POL-DC-001 (Data Classification and Handling Policy) for data sharing controls.

Related to POL-IR-001 (Incident Response Policy) for vendor incident response.

Related to POL-AUP-001 (Acceptable Use Policy) for employee responsibilities for vendor relationships.

Future related to a planned logging and monitoring standard.

### RUN-IAM-011: Non-Human Identity Discovery Runbook

Operationalizes POL-IAM-011 (Non-Human Identity Governance Policy).

Required input to REV-IAM-011 (Quarterly Non-Human Identity Access Review): the discovery output populates the access review worksheet.

Related to POL-IAM-001 (Access Control Policy) for the general access control framework.

Related to POL-IAM-002 (Password and Authentication Standard) for the credential evaluation criteria used during discovery.

Related to POL-AM-001 (Asset Management Policy) for the broader asset inventory context.

### REV-IAM-011: Quarterly Non-Human Identity Access Review

Operationalizes Section 3.9 of POL-IAM-011 (Non-Human Identity Governance Policy).

Requires input from RUN-IAM-011 (Non-Human Identity Discovery Runbook): the discovery output is the basis for the quarterly review.

Future related to a planned logging and monitoring standard for the activity data referenced in the review.

### NHI Business Owner Explainer (client-facing)

Related to POL-IAM-011 (Non-Human Identity Governance Policy): the explainer translates the policy for executive sponsors and business owners.

Related to RUN-IAM-011 (Non-Human Identity Discovery Runbook): the explainer references the discovery as part of the program rollout described to leadership.

---

## Family completeness summary

A quick view of which families have content in the library and at what level of completeness.

### IAM (Identity and Access Management): Substantively Complete for v0.1.0

Five policies: POL-IAM-001, POL-IAM-002, POL-IAM-005, POL-IAM-006, POL-IAM-011.

One runbook: RUN-IAM-011.

One template: REV-IAM-011.

One client-facing artifact: NHI Business Owner Explainer.

Reserved slots for future expansion: POL-IAM-003 (Identity Proofing and Provisioning), POL-IAM-004 (Privileged Access Management standalone), POL-IAM-007 (Identity Governance and Lifecycle), POL-IAM-008 (Customer or External Identity), POL-IAM-009, POL-IAM-010.

Planned but not started: REV-IAM-001 (Quarterly User Access Review Template), runbooks for the other IAM policies as needed.

### AUP (Acceptable Use): Foundational for v0.1.0

One policy: POL-AUP-001.

This family is typically a single comprehensive document at SMB scale. Additional documents in this family would be unusual.

### AM (Asset Management): Foundational for v0.1.0

One policy: POL-AM-001.

Planned but not started: A standalone POL-AM-002 (SaaS Asset Management Standard) if the cloud and SaaS coverage in POL-AM-001 needs to be split out for a particular adopter. I prefer this for completeness, but may not be something you want to implement. A REV-AM-001 (Annual Asset Reconciliation Template) to support the quarterly reconciliation described in Section 3.3.

### DC (Data Classification): Foundational for v0.1.0

One policy: POL-DC-001.

Planned but not started: An accompanying handling matrix template that operationalizes the classification levels into specific tooling and storage choices.

### IR (Incident Response): Foundational for v0.1.0

One policy: POL-IR-001.

Planned for v0.1.0: RUN-IR-001 (Incident Response Runbook) covering common SMB incident types.

### EP (Endpoint Protection): Foundational for v0.1.0

One policy: POL-EP-001.

Planned but not started: Companion runbooks for endpoint baseline implementation and EDR deployment, this exists in different forms on my repo, but I want to pull some of that together here. 

### VM (Vulnerability Management): Foundational for v0.1.0

One policy: POL-VM-001.

Planned but not started: A vulnerability management runbook for the discovery and prioritization workflow.

### NET (Network Security): Foundational for v0.1.0

One policy: POL-NET-001.

Planned but not started: A network segmentation runbook for environments migrating from flat networks.

### TPRM (Third-Party Risk Management): Foundational for v0.1.0

One policy: POL-TPRM-001.

Planned but not started: A vendor risk assessment template and a vendor inventory template.

### Deferred to v0.2.0 or Later

GRC (Governance, Risk, and Compliance). Deferred because much of the GRC content lives across the existing policies, and a standalone GRC policy is more useful in v1.0 once the rest of the library is mature.

AI (AI and Agent Governance). Deferred because the AI governance landscape is volatile and a 2026 policy could be substantially out of date by 2027. POL-AUP-001 Section 3.6 covers the most urgent rules for general AI tool use.

### Planned for v0.2.0 and Beyond

Logging and Monitoring Standard, Data Loss Prevention Standard, Secure Development Policy (where applicable), and additional runbooks and templates that operationalize the v0.1.0 policies.

---

## Consistency verification checklist

Use this checklist before publishing a new release of the library, before completing a customization, or after modifying any document that other documents reference.

### Document ID consistency

- [ ] Every document ID referenced in another document exists in the library or is documented as a planned future addition.
- [ ] Every document ID is referenced consistently (POL-IAM-011, not POL-IAM-11 or POL-IAM-0011).
- [ ] Cross-references that include section numbers reference sections that actually exist in the target document.
- [ ] When a document is renumbered, every cross-reference to it has been updated.

### Terminology consistency

- [ ] Defined terms in the glossary are used consistently across documents. A term defined as "non-human identity" is not also referred to as "service identity" or "machine identity" except where explicitly noted as a synonym.
- [ ] New terms introduced in a document have been added to the glossary.
- [ ] The capitalization of defined terms is consistent within each document. Non-Human Identity, non-human identity, and NHI: pick one and use it consistently.

### Framework alignment consistency

- [ ] Every CIS Controls v8 reference uses the v8 numbering and naming.
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
- [ ] Numbers under one hundred are spelled out in policy text.
- [ ] American English spelling throughout.

### Structural consistency

- [ ] Every policy follows the standard policy structure (eight numbered sections plus metadata header).
- [ ] Every runbook follows the standard runbook structure (eight numbered sections plus metadata header).
- [ ] Client-facing materials use descriptive filenames and headed sections appropriate to their non-technical audience, without strict numbered sections.
- [ ] Section numbering is consistent within document type.
- [ ] Each document has a complete metadata table at the top, except client-facing materials, which use lighter metadata.
- [ ] Each policy and runbook has a complete revision history at the bottom.
- [ ] Each document has the closing attribution line required by the CC BY-SA 4.0 license.

---

## When to update the matrix

The matrix is updated in three situations.

**When a new document is added to the library.** The new document's relationships to existing documents are recorded, and existing documents that reference the new one are updated to include the new relationship.

**When an existing document's ID or structure changes.** Every document that references the changed document is reviewed and updated. The verification checklist above is the basis for the review.

**When a new version of the library is released.** A pre-release pass through the matrix confirms that all relationships are accurate as of the release.

The matrix is intended to be a tool for maintaining consistency, not a comprehensive map of every possible relationship between documents. Relationships that are obvious from context (every policy in a library has some relationship to every other policy in some sense) are not enumerated. Relationships that materially affect how a document is used or maintained are enumerated.

---

*Cross-reference consistency is invisible when it works and immediately apparent when it does not. Must be maintain it.*
