# Changelog

Notable changes to this library are documented in this file.

The format follows the [Keep a Changelog](https://keepachangelog.com/) convention. The library uses semantic versioning, where the major-minor-patch numbers indicate roughly the scope of change between releases. Major versions indicate substantial restructuring or breaking changes to existing content. Minor versions indicate new content or significant updates to existing content. Patch versions indicate corrections, clarifications, and other small improvements that do not change the substance of existing content.

---

### Changed

- **Breaking: document IDs.** Standards now use the STD prefix and live in `standards/`, and numbers run sequentially from 001 within each type and family, with no reserved slots and no shared numbers between a policy and its companions. In the IAM family: POL-IAM-002 (Password and Authentication Standard) is now STD-IAM-001; POL-IAM-006 (Single Sign-On and Federation Standard) is now STD-IAM-002; POL-IAM-005 (Remote Access) is now POL-IAM-002; POL-IAM-011 (Non-Human Identity Governance) is now POL-IAM-003; RUN-IAM-011 is now RUN-IAM-001. Templates use the TPL prefix in place of REV. The governance family code is GOV instead of the planned GRC, matching the NIST CSF 2.0 Govern function. Adopters who reference the old IDs update them during their next review.
- STD-IAM-001 session limits now follow NIST SP 800-63B Revision 4 reauthentication guidance: one-hour inactivity and twenty-four-hour overall timeouts for standard users (AAL2), fifteen minutes and twelve hours for privileged access (AAL3). Previously eight hours and one hour of inactivity.
- RUN-IR-001 restructured to the runbook convention in the style guide. The playbooks moved from Section 4 to Section 3.2; communication templates and escalation decisions became Phases 3 and 4 of the procedure. Operational Cadence and Automation Opportunities sections added.
- Regulatory notes updated, each marked for validation because the underlying programs are still changing: the CMMC Phase 2 suspension and self-assessment class deviation (framework mapping); the HIPAA Security Rule overhaul's status as a proposal now projected for July 2027, with the current rule still in force (framework mapping); and the full set of amended NYDFS Part 500 requirements, split into what the library covers and what it does not (framework mapping).
- License changed from CC BY-SA 4.0 to CC BY 4.0. LICENSE, README, CONTRIBUTING, the customization guide, the cross-reference matrix, and every closing attribution line updated. Derivative works no longer have to use the same license. Organizations adopting documents for their own use need not credit the source in them: each document's closing line now says it may be removed, `generate.py` removes it by default and writes a NOTICE file instead (`keep_attribution` keeps it), and the check script enforces one exact wording so the line can be removed reliably. Redistributing the library or a derived collection requires credit once, not in each document.
- Tooling in `scripts/` and `tests/` is now licensed under the MIT License (`LICENSE-CODE`), with SPDX headers; Creative Commons licenses are not designed for software. Documents remain under CC BY 4.0.
- Framework alignment moved from CIS Controls v8 to v8.1 throughout.
- Placeholders and examples are vendor-neutral. Product names replaced with descriptions of the tool category; platform-native feature names kept only where a provision is platform-specific. The rule is now in the style guide.
- STD-IAM-001 aligned to NIST SP 800-63B Revision 4: fifteen-character minimum, sixty-four-character maximum support, TOTP classified, synced and device-bound passkeys distinguished, session termination corrected.
- POL-EP-001 and POL-NET-001 patching timelines now follow the POL-VM-001 priority cadences (7/14/30 days). Previously EP used 14/30/60 and NET used thirty days for critical firmware.
- Phishing-resistant MFA remediation set to thirty days in POL-IAM-001, STD-IAM-001, and POL-IAM-002.
- Logging references now point to STD-LOG-001 instead of a placeholder.
- Framework mapping recalculated: Audit Log Management to Strong, Email and Web Browser Protections to Partial, Penetration Testing to Not Covered. Vague "selected safeguards" and unnumbered CSF categories replaced with specific citations; several over-claims removed.

### Added

- `scripts/export.py`: exports a generated library to Word (policies, standards, runbooks, addenda, explainers, and template instructions) and Excel (one workbook per template, with a sheet per table, dropdowns for fixed answers, frozen headers, filters, and print setup), and exports the intake questionnaire to Excel. Word documents carry a header with the organization and document, a footer with classification, version, and page numbers, and, for policies, standards, and addenda, an approval block. Branding comes from an optional `[export]` table; the default is a neutral style. PDF output is left to the reader after review. `scripts/intake.py` now reads the Excel questionnaire as well as the Markdown one. CI exports the sample client and attaches the deliverables to each build.
- `docs/intake-questionnaire.md` and `scripts/intake.py`: a plain-language questionnaire covering the five scoping questions, document statuses, and every adoption-time decision, grouped by who usually answers, with the library sentence each answer completes and an example answer. `intake.py` converts a filled-in copy into a generator configuration file. The questionnaire is generated from `placeholders.toml` (now holding a question and section for each adoption-time placeholder, and defaults for the policy versions), and the automated check fails if it falls out of date.
- `scripts/generate.py`: generates an organization's customized copy of the library from one TOML configuration file holding the scoping answers, document statuses, and placeholder values. It rejects unknown and use-time keys, replaces adoption-time placeholders including example text (with bracket matching for placeholders nested in examples), sets the POL-GOV-001 suite table from the configuration, marks planned and not-adopted documents, fails on unfilled placeholders in adopted documents, offers an example-text drafting mode, and writes a generation report. `examples/clients/sample-remote-firm.toml` is a complete example.
- `placeholders.toml`: a registry of all 109 placeholders with their phase (adoption or use) and description. The customization guide's placeholder table is now generated from it, and `scripts/check_library.py` fails on unregistered placeholders, unused registrations, or an out-of-date table.
- `tests/test_generate.py`: parser and generator tests. CI now runs the tests and generates the sample client on every push.
- TPL-AUP-001 (Policy Acknowledgment Form and Log): a signature form covering POL-AUP-001 and POL-GOV-001, monitoring, confidentiality, and reporting; a log tracking initial, annual, and post-change acknowledgments; and quarterly checks for access granted before acknowledgment.
- `docs/cis-ig1-checklist.md`: all 56 CIS Controls v8.1 Implementation Group 1 safeguards mapped to the document and section that meets each, with the evidence to show. All 56 are met: POL-DC-001 Section 3.7 now has data owners record where Confidential and Restricted data is stored (3.2), and POL-AUP-001 Section 3.9 and POL-GOV-001 Section 3.8 now cover reporting devices that are missing security updates (14.7).
- `docs/adoption-guide.md`: five scoping questions, three adoption waves (with asset inventory and logging in the first wave, ahead of the controls that depend on them) and evidence of adoption for each document, profiles for eight common organization types, and guidance for MSPs and vCISOs maintaining the library across many clients. Linked as the first step in the README.
- `scripts/check_library.py` and a GitHub Actions workflow that run on every push and pull request. The check confirms that referenced document IDs exist, that cited sections exist in their targets, that filenames, titles, and metadata IDs agree, that numbers run sequentially from 001 within each type and family, that every document carries the attribution line, and that the voice rules hold (no dashes, "shall," sentence-starting And or But, banned words, British spellings, or product names in placeholders).
- RUN-IR-002 (Tabletop Exercise Facilitation Runbook): planning, ground rules, facilitation technique, seven scenarios built on the RUN-IR-001 playbooks, a debrief structure, an exercise record, and an eight-quarter rotation. Fulfills POL-IR-001 Section 3.10.
- STD-DR-001 (Data Backup and Recovery Standard): recovery objectives by criticality, with default timings presented as starting points that the business owners replace, coverage of identity and SaaS, three copies with one immutable or offline, a backup system isolated from production identity, retention, monitoring, quarterly and annual restore testing, recovery procedures, and incident recovery rules. New DR family.
- TPL-IAM-002 (Quarterly User Access Review): roster reconciliation, manager review, system owner review, monthly privileged access review, vendor and guest accounts, findings, and summary.
- STD-NET-001 (Email and Web Browser Protection Standard): supported browsers, browser and extension management, filtering off the office network, SPF, DKIM, and DMARC for every domain including parked ones, MTA-STS, inbound filtering, forwarding and inbox-rule controls, phishing reporting, and payment-change verification, with a DMARC enforcement target rather than a deadline and conditions that decide when an unverified payment-detail change is an incident.
- STD-DC-001 (Data Loss Prevention Standard): monitor-first rollout, detection rules for Restricted data types, sensitivity labels, rules by channel, user experience, secret scanning, alert handling, and privacy limits. Replaces the `[DLP_STANDARD]` placeholder.
- POL-DEV-001 (Secure Development Policy), adopted only by organizations that develop software: source control, secrets, review, dependencies and SBOM, secure design, testing, environment separation, vulnerability handling, outsourced development, and training. New DEV family. Replaces the `[SECURE_DEVELOPMENT_POLICY]` placeholder.
- ADD-CMMC-001 (CMMC Level 2 Addendum), the first framework addendum, with a validation note on the changing CMMC program: coverage of the fourteen NIST SP 800-171 Revision 2 families, additional provisions for the CUI environment, overrides of library defaults (password composition and reuse, FIPS-validated cryptography, DIBNet reporting, FedRAMP Moderate equivalency, allowlisting), and assessment readiness. New ADD document type and `addenda/` directory.
- AI Governance Business Owner Explainer (client-facing), following the NHI explainer pattern.
- Glossary: CUI, data loss prevention, immutable backup, RPO and RTO, secret scanning, and SBOM. Customization guide: every placeholder in the library is now listed.
- STD-OPS-001 (Change Management Standard): standard, normal, and emergency changes; approval by the system owner and IT, with Information Security for security controls; a minimum change record; service provider changes; post-change checks; monthly reconciliation of configuration alerts against change records; and baselines changed only through normal changes. New OPS family. Covers SOC 2 CC8.1 and NIST SP 800-171 3.4.3 through 3.4.5.
- POL-BC-001 (Business Continuity Policy) and TPL-BC-001 (Business Continuity Plan): critical business functions with maximum tolerable downtime, planning for five kinds of loss (office, system, people, vendor, power and internet), organization-held break-glass access and transition terms for the IT provider, decision authority, communications, and annual testing. New BC family. Covers NYDFS 500.16 and CSF GV.OC-04, GV.OC-05, and RC.RP-04.
- POL-PPS-001 (Physical and Personnel Security Policy): physical areas, access devices, visitors, clean desk, home and shared workspaces, screening routed through counsel, confidentiality agreements, role changes, departures, sanctions, and awareness. New PPS family. Closes the CMMC Physical Protection and Personnel Security gaps.
- STD-DC-002 (Cryptography and Key Management Standard): one table of where encryption is required, protocol and algorithm minimums, validated cryptography where required (with the FIPS 140-2 to 140-3 transition flagged for validation), key storage, recovery keys, customer-managed keys, compromise handling, certificate inventory and automated renewal for shrinking certificate lifetimes, and post-quantum preparation.
- ADD-CMMC-001 updated: Personnel Security and Physical Protection now Strong; change control and validated cryptography point to the new library documents. Maintenance (3.7) remains the only family with no library coverage.
- STD-VM-001 (Security Testing Standard): three testing tiers chosen by exposure and obligations rather than headcount. Baseline (every organization): monthly external scanning, an annual external exposure review, an annual identity and productivity tenant configuration review, quarterly control checks, phishing simulations, and tabletops. Standard: adds an annual external penetration test, testing after significant change, and periodic outside tenant and assumed-breach reviews. Expanded: adds annual internal and application testing, segmentation testing, and detection validation.
- POL-DEV-001 adoption levels: scripts and automations, internal applications, and internet-facing applications, each naming the sections that apply.
- Framework coverage: CIS Controls 9 and 11 now Strong; Controls 16 and 18 scale with the organization through POL-DEV-001 adoption levels and STD-VM-001 tiers; NIST CSF PR.DS and ID.IM now Strong.
- POL-AI-001 (AI and Agent Governance Policy): data classification as the gate for AI use, approval criteria for AI tools and for AI features vendors enable in existing software, AI connectors and MCP servers governed as non-human identities, assistive, supervised, and autonomous agent levels with actions that always require human approval, prompt injection limits for agents that read untrusted content, meeting assistants and recording consent, human accountability for AI output, disclosure and deepfake verification, AI built in-house, an AI inventory, and AI-related incidents. Reviewed semiannually. Aligned to CIS Controls v8.1, NIST CSF 2.0, and a subset of the NIST AI RMF Govern function. POL-AUP-001 Section 3.6 now points to it.
- TPL-AI-001 (AI Tool and Agent Inventory): approved tools, AI features in existing software, connectors, agents with the POL-AI-001 Section 3.4 checks built in, in-house AI systems, and a quarterly reconciliation against consent logs, admin settings, endpoint and extension inventory, network visibility, and expense records. Connector and agent rows link to the POL-IAM-003 inventory.
- CIRCIA added as a pending federal reporting requirement in POL-IR-001 Section 3.6, RUN-IR-001 (notification triggers and ransom payment reporting), and the framework mapping, with a note that it may change when the final rule is published.
- POL-AI-001 references the CIS Controls AI Companion Guides (LLM, AI Agent, and MCP) and uses the OWASP Top 10 for Large Language Model Applications as the reference for agent risks and the test basis for AI built in-house. TPL-AI-001 records the test date.
- STD-AM-001 (SaaS Asset Management Standard): implements POL-AM-001 Section 3.6 with a SaaS inventory, multi-source discovery including sign-ups with company email, an onboarding baseline, administrator rules (at least two, no more than three without approval, and a break-glass local administrator where SSO is enforced), a configuration baseline for Critical and Important applications, quarterly roster comparison for applications without SCIM, independent backup and annual restore testing for Critical SaaS data, and retirement steps that remove dangling DNS records and email sending authorizations.
- TPL-IAM-001 (Quarterly Non-Human Identity Access Review): change log from the RUN-IAM-001 reconciliation, a review worksheet with the five POL-IAM-003 Section 3.9 confirmations, rotation and dormancy status, outcome rules, a findings log, and a quarterly summary. AI connectors and agents from TPL-AI-001 are reviewed in the same worksheet.
- Glossary: AI agent, Model Context Protocol (MCP), and prompt injection.
- POL-IAM-001: account inventory and forty-five-day dormant account disablement; phishing-resistant MFA for break-glass accounts.
- POL-AM-001: network discovery for devices without agents; unsupported software flagging.
- POL-EP-001: common baseline elements (screen lock, host firewall, default accounts), autorun disabled, two-minute mobile lock.
- POL-NET-001: architecture diagrams; guest Wi-Fi encryption requirement.
- POL-IR-001: out-of-band communication channel; insurer panel requirement for retainers.
- POL-VM-001: monthly external scanning; security.txt for disclosure.
- RUN-IR-001: removal of attacker-registered MFA methods; access token lifetime after session revocation; insurer notification before outside engagement.
- Style guide: em-dash, declarative lead, And/But, shall, vendor neutrality, and sourcing rules. CONTRIBUTING: voice-check commands. Customization guide: placeholder reference table.

### Removed

- References that presented REV-IAM-001 and REV-IAM-011 as published. Those templates were never committed. TPL-IAM-001 now holds the quarterly non-human identity review that REV-IAM-011 described (see Added); the user access review is listed as planned, without a number until it is written.

### Fixed

- RUN-IAM-001: Phase 2 relied on raw sign-in logs that cannot see past their retention window; replaced with the sign-in activity report and a KQL query against exported logs. Fixed DateTime concatenation (Phase 1), missing `-All` paging, `gh api` sending POST with `-f`, `Set-AzContext` output in the CSV, and the PowerShell version required by the Power Platform module. Fine-grained PATs and deploy keys are now enumerated.
- Wrong document IDs in POL-AUP-001 Related Documents; stale "forthcoming" labels across five policies and the matrix.
- POL-IR-001 claimed RUN-IR-001 contained tabletop scenarios and a facilitation guide; it does not.
- README version (1.0.0 to 0.1.0) and the reference to a `tools/` directory that does not exist.
- Unsourced statistics in POL-IAM-003 and the NHI explainer softened or removed. Outdated references updated (SP 800-61 Revision 3, PCI DSS 4.0.1, App Control for Business, Exchange RBAC for Applications).

## Future Roadmap: The Path to Compliance as Code (CaC)

While v0.2.0 establishes a robust "Docs as Code" pipeline for automated deliverable generation, my long-term vision is to bridge the gap between written policy and technical enforcement. Future releases will focus on evolving this library into a true Compliance as Code (CaC) framework for MSPs:

* **v0.3.0 - Machine-Readable Control Metadata:** Transitioning monolithic policy requirements into structured data by injecting YAML frontmatter (Control IDs, required values, and framework mappings) into the Markdown source. This establishes a programmatic single source of truth.
* **v0.4.0 - Configuration as Code Translation:** Expanding the Python automation suite to translate the `placeholders.toml` client baseline into executable configuration scripts (e.g., PowerShell, Microsoft Graph API, or Terraform) to automatically provision Microsoft 365/Entra ID environments to match the written policy.
* **v0.5.0 - Continuous Compliance & Drift Detection:** Introducing read-only auditing scripts that query a client's live tenant, compare the actual technical configurations against the TOML baseline, and output pass/fail states to an MSP's ticketing system to catch configuration drift.
* **Incident Response Runbook Expansions:** Specific incident-type playbooks (Insider Threat, Supply Chain Compromise, DoS) deferred from v0.1.0 will be integrated alongside community feedback.

## [0.1.0] - 2026-04-26

The initial public release of the security policy templates library. The release establishes the library's structure, voice, conventions, and the foundational policies for SMB security programs.

### Coverage summary

This release covers nine of the eleven planned policy families: Identity and Access Management (IAM), Acceptable Use (AUP), Asset Management (AM), Data Classification (DC), Incident Response (IR), Endpoint Protection (EP), Vulnerability Management (VM), Network Security (NET), and Third-Party Risk Management (TPRM). Two families are deferred to later releases: Governance, Risk, and Compliance (GRC) is deferred until the rest of the library is mature enough to govern, and AI and Agent Governance (AI) is deferred because the topic is moving fast enough that a 2026 policy could be substantially out of date by 2027. The acceptable use policy includes a substantive AI tools section that covers the most urgent rules for general AI tool use.

The release aligns to CIS Controls v8.1 and NIST Cybersecurity Framework 2.0 by default. Of the eighteen CIS Controls v8.1 control areas, fourteen are covered Strong, two are Partial, and two are Not Covered. The Not Covered items (Email and Web Browser Protections, Application Software Security) are explicit scope decisions documented in the framework mapping.

### Added: Repository scaffolding

- `README.md`: Project introduction, audience description, structure overview, and adoption guidance.
- `LICENSE`: Creative Commons Attribution-ShareAlike 4.0 International license header. The canonical legal code text is appended at publication from creativecommons.org/licenses/by-sa/4.0/legalcode.
- `CONTRIBUTING.md`: Contribution guidelines including expectations for response time, voice consistency requirements, and the contribution licensing model.

### Added: Documentation

- `docs/glossary.md`: Definitions for terms used across the library, organized into five categories: Identity and Access, Data and Assets, Threat and Defense, Governance and Process, and Frameworks and References. Approximately 70 defined terms.
- `docs/style-guide.md`: Voice and structural conventions for documents in the library. Establishes the constraints on em-dashes, sentence-starting "And" or "But," AI-assisted-writing tells, and corporate-speak.
- `docs/customization-guide.md`: Placeholder convention, adoption sequence, and tailoring guidance for organizations adopting the library.
- `docs/framework-mapping.md`: How library content aligns to CIS Controls v8.1 and NIST Cybersecurity Framework 2.0, plus high-level guidance for adopters subject to additional frameworks (HIPAA, PCI DSS, SOC 2, ISO 27001, CMMC, NYDFS, GDPR).
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


