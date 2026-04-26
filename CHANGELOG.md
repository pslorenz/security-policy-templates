# Changelog

Notable changes to this library are documented in this file.

The format follows the [Keep a Changelog](https://keepachangelog.com/) convention. The library uses semantic versioning, where the major-minor-patch numbers indicate roughly the scope of change between releases. Major versions indicate substantial restructuring or breaking changes to existing content. Minor versions indicate new content or significant updates to existing content. Patch versions indicate corrections, clarifications, and other small improvements that do not change the substance of existing content.

---

## [0.1.0] - 4/26/2026

The initial public release of the security policy templates library. The release establishes the library's structure, voice, conventions, and the foundational policies for SMB security programs.

### Coverage summary

This release covers nine of the eleven planned policy families: Identity and Access Management (IAM), Acceptable Use (AUP), Asset Management (AM), Data Classification (DC), Incident Response (IR), Endpoint Protection (EP), Vulnerability Management (VM), Network Security (NET), and Third-Party Risk Management (TPRM). Two families are deferred to later releases: Governance, Risk, and Compliance (GRC) is deferred until the rest of the library is mature enough to govern, and AI and Agent Governance (AI) is deferred because the topic is moving fast enough that a 2026 policy could be substantially out of date by 2027. The acceptable use policy includes a substantive AI tools section that covers the most urgent rules for general AI tool use.

The release aligns to CIS Controls v8 and NIST Cybersecurity Framework 2.0 by default. Of the eighteen CIS Controls v8 control areas, fourteen are covered Strong, two are Partial, and two are Not Covered. The Not Covered items (Email and Web Browser Protections, Application Software Security) are explicit scope decisions documented in the framework mapping.

### Added: Repository scaffolding

- `README.md`: Project introduction, audience description, structure overview, and adoption guidance.
- `LICENSE`: Creative Commons Attribution-ShareAlike 4.0 International license header. The canonical legal code text is appended at publication from creativecommons.org/licenses/by-sa/4.0/legalcode.
- `CONTRIBUTING.md`: Contribution guidelines including expectations for response time, voice consistency requirements, and the contribution licensing model.

### Added: Documentation

- `docs/glossary.md`: Definitions for terms used across the library, organized into five categories: Identity and Access, Data and Assets, Threat and Defense, Governance and Process, and Frameworks and References. Approximately 70 defined terms.
- `docs/style-guide.md`: Voice and structural conventions for documents in the library. Establishes the constraints on em-dashes, sentence-starting "And" or "But," AI-assisted-writing tells, and corporate-speak.
- `docs/customization-guide.md`: Placeholder convention, adoption sequence, and tailoring guidance for organizations adopting the library.
- `docs/framework-mapping.md`: How library content aligns to CIS Controls v8 and NIST Cybersecurity Framework 2.0, plus high-level guidance for adopters subject to additional frameworks (HIPAA, PCI DSS, SOC 2, ISO 27001, CMMC, NYDFS, GDPR).
- `docs/cross-reference-matrix.md`: Living record of how documents reference each other. Includes a verification checklist for use during contribution review and pre-release passes.

### Added: Identity and Access Management family

- `policies/POL-IAM-001-access-control.md`: Access control policy covering account ownership, role-based access, quarterly access reviews, departure-driven access removal, privileged access standards, MFA requirements, break-glass account controls, and vendor access provisions.
- `policies/POL-IAM-002-password-authentication-standard.md`: Password and authentication standard reflecting current NIST SP 800-63B guidance, including the move away from mandatory periodic password rotation and complexity rules. Establishes phishing-resistant authentication as the standard for privileged access.
- `policies/POL-IAM-005-remote-access.md`: Remote access policy adopting the identity-gated access model with a documented twelve-to-eighteen-month migration timeline from traditional VPN.
- `policies/POL-IAM-006-sso-federation-standard.md`: Single sign-on and federation standard establishing SSO as the default for business applications, with OpenID Connect preferred over SAML 2.0 for new applications.
- `policies/POL-IAM-011-non-human-identity-governance.md`: Non-human identity governance policy covering service accounts, service principals, managed identities, application registrations, API keys, and other non-human authentication principals. Operationalized by RUN-IAM-011 and REV-IAM-011.
- `runbooks/RUN-IAM-011-nhi-discovery.md`: Seven-phase non-human identity discovery procedure across Microsoft Entra, Active Directory, GitHub, Power Platform, Azure RBAC, and Microsoft 365. Includes PowerShell code blocks for the technical steps.
- `templates/REV-IAM-001-Quarterly-User-Access-Review.xlsx`: Quarterly user access review template operationalizing POL-IAM-001 Section 3.3. Five sheets (Instructions, Access Review, Findings Log, Summary, Sign-Off) with 522 formulas, conditional formatting, and dropdown validations. Three example users seeded.
- `templates/REV-IAM-011-Quarterly-NHI-Access-Review.xlsx`: Quarterly non-human identity access review template operationalizing POL-IAM-011 Section 3.9. Five sheets matching the REV-IAM-001 pattern with 1,018 formulas adapted for non-human identity scope.
- `client-facing/nhi-business-owner-explainer.md`: Plain-language explainer of the non-human identity governance program for executive sponsors and business owners. Includes a usage note explaining that the "we" voice can be read as either an internal team or a service provider.

### Added: Acceptable Use Policy family

- `policies/POL-AUP-001-acceptable-use.md`: Acceptable use policy covering general use, account security, data handling, email and communications, internet use, generative AI tools (substantive 2026 treatment), personal devices, software installation, incident reporting, and departure obligations.

### Added: Asset Management family

- `policies/POL-AM-001-asset-management.md`: Asset management policy adopting the runtime-truth approach (inventory built from EDR, RMM, identity provider, and cloud platform APIs rather than maintained as a separate spreadsheet). Three-tier criticality classification (Critical, Important, Standard). Substantive cloud and SaaS coverage.

### Added: Data Classification family

- `policies/POL-DC-001-data-classification-handling.md`: Three-tier data classification policy (Public, Confidential, Restricted) with handling rules for each tier. Default classification for unclassified data is Confidential. Specific 2026 treatment of AI tool inputs as a data category.

### Added: Incident Response family

- `policies/POL-IR-001-incident-response.md`: Incident response policy with six-phase response model (Preparation, Detection and Analysis, Containment, Eradication, Recovery, Post-Incident Review), four-tier severity classification (Critical, High, Medium, Low), Standing Authority Matrix for pre-authorized containment actions, and quarterly tabletop exercise requirement.
- `runbooks/RUN-IR-001-incident-response.md`: Incident response runbook with playbooks for the five most common SMB incident types: account compromise, ransomware, business email compromise, lost or stolen device, and phishing campaign response. Includes communication templates, decision frameworks for ransom payment and law enforcement engagement, and post-incident activities.

### Added: Endpoint Protection family

- `policies/POL-EP-001-endpoint-protection.md`: Endpoint protection policy covering baseline configuration by operating system, EDR requirements (with explicit acknowledgment that signature-based anti-malware alone is insufficient), disk encryption, patching cadences (14/30/60 day tiers), application control, mobile device management, lost or stolen device response, and decommissioning. Explicit ChromeOS treatment.

### Added: Vulnerability Management family

- `policies/POL-VM-001-vulnerability-management.md`: Vulnerability management policy adopting the exploitability-and-context prioritization model (KEV, EPSS, CVSS together rather than CVSS alone). Four-tier priority (Critical, High, Medium, Low) with 7/14/30-day remediation cadences. Acknowledges the Day-Zero Reality that exploitation may begin within hours of disclosure for some vulnerabilities. Five-tier remediation method preference (patch, configure, compensate, accept risk, retire).

### Added: Network Security family

- `policies/POL-NET-001-network-security.md`: Network security policy treating segmentation as the primary network control. Substantive coverage of office networks, cloud platform networks (Azure, AWS, GCP), and wireless (corporate, guest, IoT). Egress filtering as a primary defense. Acknowledges the modern reality that network perimeter is no longer the primary line of defense while addressing what network security still does.

### Added: Third-Party Risk Management family

- `policies/POL-TPRM-001-third-party-risk-management.md`: Vendor risk management policy with three-tier vendor model (Tier 1, 2, 3) driving due diligence, contractual protections, and ongoing monitoring. Explicit treatment of AI usage by vendors as a 2026 risk category. Sub-processor and fourth-party guidance scoped to what SMB organizations can realistically manage.

### Editorial standards established

- All documents written in plain prose without em-dashes or en-dashes anywhere except in style guide examples and CONTRIBUTING grep commands.
- No sentence-starting "And" or "But."
- No corporate-speak or AI-assisted-writing tells (delve, rapidly evolving, navigating the complexities, leverage synergies, robust, seamless, in today's, it is important to note).
- No "shall" usage; replaced with "must" or simpler indicative phrasing.
- Numbers under one hundred spelled out in policy text.
- Average sentence length 12-16 words across all documents.
- American English spelling.
- Each document closes with the CC BY-SA 4.0 attribution line: "Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution-ShareAlike 4.0."

### Cross-reference state

All cross-references between documents resolve to existing artifacts within v0.1.0. Forthcoming references are limited to: the planned Logging and Monitoring Standard, the planned Data Loss Prevention Standard, the planned AI and Agent Governance Policy (deferred per the v0.1.0 scope decision), and the Secure Development Policy (where applicable to organizations that develop software).

### Known gaps documented for future releases

The framework mapping document explicitly identifies the gaps that remain after this release. The following content is planned for future releases:

- Logging and Monitoring Standard: a foundational standard that the data classification, incident response, and vulnerability management policies depend on. Planned for v0.2.0.
- Data Loss Prevention Standard: technical implementation of the data classification handling rules. Planned for v0.2.0 or later.
- Email and Web Browser Protections (CIS Control 9): not yet covered. Planned for v0.2.0.
- Standalone Data Recovery treatment (CIS Control 11): currently covered partially by data classification and incident response policies. A standalone treatment is planned for v0.2.0 or later.
- Incident Response Runbook expansions: additional incident types beyond the five included in v0.1.0 (insider threat, supply chain compromise, denial of service) will be added based on adopter feedback.
- POL-AI-001 (AI and Agent Governance): deferred per v0.1.0 scope decision. Will be drafted when the AI governance landscape is more settled.
- POL-GRC-001 (Governance, Risk, and Compliance): deferred per v0.1.0 scope decision. Will be drafted when the rest of the library is mature enough to govern.
- Framework-specific addenda (HIPAA, PCI DSS, SOC 2, ISO 27001, CMMC) where adopter need warrants the work.
- Additional templates and runbooks operationalizing v0.1.0 policies that currently lack a recurring control template.


