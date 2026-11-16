# Style Guide

The conventions every document in this library follows. This guide exists so that contributors and adopters can keep the pack internally consistent as it evolves.

---

## Formatting conventions

The library uses Markdown as the canonical format. Documents render in GitHub's default theme without custom styling. The formatting conventions below ensure that documents render predictably and convert cleanly to DOCX or PDF when consumers need traditional formats.

**Heading hierarchy.** Documents use H1 for the document title, H2 for major sections (numbered, e.g. "## 3. Policy Statements"), H3 for subsections within sections (numbered, e.g. "### 3.1 Named Ownership"), and H4 sparingly for further subdivision when needed. The numbering convention helps consumers cross-reference specific provisions.

**Tables.** Used for metadata at the top of policy documents, for cross-reference matrices, and for revision history. Not used as a substitute for prose where prose would serve better.

**Code blocks.** Used in runbooks for executable commands. Triple-backtick fenced code blocks with language identifiers (`powershell`, `bash`, `python`) for syntax highlighting in GitHub's renderer.

**Bold and italic emphasis.** Bold for term introduction within a paragraph (the first appearance of a defined term, the role name in a roles-and-responsibilities section). Italic for document titles when referenced inline, and for the closing attribution line at the end of each document. Neither used for emphasis within sentences; sentence construction should carry the emphasis.

**Blockquotes.** Used for direct quotation from external sources only, with full citation. Not used as a styling device for callouts.

## Specific writing rules

These rules are enforced consistently across every document in the library.

**No "shall."** Requirements use "must" or plain indicative phrasing ("Privileged accounts use phishing-resistant authentication").

**Vendor neutrality.** Placeholders and examples name a category of tool ("[APPROVED_EDR_PLATFORMS, e.g., an EDR platform with behavioral detection and remote isolation]"), never products. Platform names (Microsoft 365, Google Workspace, Azure, AWS, GCP) and their native feature names appear only where a provision or procedure is specific to that platform.

**Claims carry their basis.** Statistics and threat claims are either sourced or phrased as practitioner observation. Unsourced figures presented as fact are removed.

**No corporate-speak.** "Leverage," "synergy," "best-in-class," "world-class," "robust," "seamless," and similar are flagged as voice violations. Use the plain word: use, work together, good, well-built, smooth.

**Numbers under one hundred are spelled out in policy text.** "Ninety days" rather than "90 days." "Three years" rather than "3 years." Exception: dates, version numbers, percentages, currency amounts, and specific technical values (port 443, RFC 1918, eight characters minimum) use numerals. Tables and code blocks use numerals throughout.

**Oxford comma.** Used consistently. "Phishing-resistant MFA, segmentation, and identity-layer detection," not "phishing-resistant MFA, segmentation and identity-layer detection."

**American English spelling.** "Authorization" not "authorisation," "behavior" not "behaviour," "organization" not "organisation."

## Document structure conventions

Each document type follows a consistent structure. The structure is documented here so that contributors producing new content can match the existing pattern, and so that consumers can find specific information across documents quickly.

**Policy documents** (POL-xxx-nnn) follow this structure:

1. Title and metadata table at the top
2. Section 1: Purpose
3. Section 2: Scope
4. Section 3: Policy Statements (with numbered subsections for each provision)
5. Section 4: Roles and Responsibilities
6. Section 5: Enforcement
7. Section 6: Related Documents
8. Section 7: Framework Alignment
9. Section 8: Revision History
10. Closing attribution line

**Closing lines.** Policies, standards, runbooks, and addenda end with an italic authority statement ("This policy is issued under the authority of the executive sponsor listed above.") followed, as a separate line, by the standard attribution line given in CONTRIBUTING.md. Templates and client-facing documents end with the attribution line alone. The attribution line tells adopters they may remove it, and the generator removes it by default, so it must be worded exactly as given and kept on its own line.

**Runbook documents** (RUN-xxx-nnn) follow this structure:

1. Title and metadata table at the top
2. Section 1: Purpose and Scope
3. Section 2: Prerequisites (access, tooling, output artifacts)
4. Section 3: Procedure (numbered phases)
5. Section 4: Analysis and Findings
6. Section 5: Operational Cadence
7. Section 6: Automation Opportunities
8. Section 7: References
9. Section 8: Revision History
10. Closing attribution line

**Standards** (STD-xxx-nnn) follow the policy structure, with Section 3 titled "Standard Requirements" instead of "Policy Statements." A standard carries the technical specifics a policy points to, such as password length, log retention, or federation protocols.

**Templates** (TPL-xxx-nnn) are Markdown forms, registers, inventories, and reports that produce evidence of a control running over time. Each opens with a metadata table naming the document it supports, then a "How to use this template" section, then the form itself. Tables carry the recorded data; prose explains how to fill them in.

**Framework addenda** (ADD-xxx-nnn) live in `addenda/`. They follow the standard structure with these sections: Purpose and Status (including a validation note when the framework is changing), How to Use, Coverage by family or category, Additional Provisions, Overrides of Library Defaults, Assessment Readiness, Related Documents, and Revision History. An addendum is additive: within its scope it governs where it differs from a library document, and outside its scope it has no effect.

**Client-facing materials** are short documents (typically under fifteen hundred words) with minimal internal structure. They are written for non-technical readers and use plainer language than the policies and runbooks. They do not follow the numbered-section convention.

## Document IDs

Document IDs follow the pattern `[TYPE]-[FAMILY]-[NUMBER]`, where:

**Type** is a three-letter code identifying the document category:
- POL: Policy
- RUN: Runbook
- STD: Standard (technical requirements that implement a policy; see Document structure conventions)
- TPL: Template (registers, inventories, review worksheets, and reports that produce control evidence)
- PLY: Incident response playbook
- GUI: Guide (longer-form explanatory content)
- ADD: Framework addendum (supplements the library for a specific regulation or framework; the family code names the framework)

**Family** is a two-to-four-letter code identifying the topical area:
- IAM: Identity and Access Management
- AM: Asset Management
- DC: Data Classification
- IR: Incident Response
- VM: Vulnerability Management
- EP: Endpoint Protection
- NET: Network Security
- AUP: Acceptable Use
- GOV: Governance (the program-level policy, risk management, exceptions, and metrics)
- AI: Artificial Intelligence and Agent Governance
- LOG: Logging and Monitoring
- DR: Data Backup and Recovery
- DEV: Secure Development
- OPS: Operations (change management and related operational standards)
- BC: Business Continuity
- PPS: Physical and Personnel Security
- Framework codes for addenda (ADD type only): CMMC, HIPAA, PCI, SOC2, and similar
- TPRM: Third-Party Risk Management

**Number** is a sequential integer, zero-padded to three digits, that runs from 001 within each combination of type and family. The policies in the IAM family are POL-IAM-001, POL-IAM-002, and POL-IAM-003; its standards are STD-IAM-001 and STD-IAM-002; the governance templates are TPL-GOV-001 through TPL-GOV-004.

Examples: POL-IAM-001, POL-IAM-003, STD-IAM-001, RUN-IAM-001, TPL-GOV-004, POL-AI-001.

A new document takes the next unused number for its type and family. Numbers are not reserved in advance for topics that may never be written, and a number retired after a release is not reused, so that an adopter's references never silently point at a different document.

Numbers do not encode relationships. A runbook or template names the document it supports in its metadata table (the Related Policy or Supports row), and the cross-reference matrix records the relationship. RUN-IAM-001 operationalizes POL-IAM-003, and TPL-GOV-002 supports POL-GOV-001, without either sharing its parent's number.

## Placeholder convention

Every document contains placeholders that the adopter fills in for their environment. Placeholders use the `[BRACKETED_UPPERCASE_WITH_UNDERSCORES]` pattern.

Standard placeholders used across the library:

- `[ORGANIZATION_NAME]`: The adopting organization's legal or operating name
- `[EFFECTIVE_DATE]`: The date the document goes into effect after adoption
- `[POLICY_OWNER]`: The named individual or role accountable for the document
- `[EXECUTIVE_SPONSOR]`: The named individual at the executive level who approves the document
- `[REVIEW_DATE]`: The date the document is next scheduled for review
- `[VERSION]`: The version number of the adopting organization's instance of the document

Document-specific placeholders use a descriptive name in the same format. The `docs/customization-guide.md` document lists every document-specific placeholder and the documents that use it.

## Cross-references

Documents reference one another by document ID. The reference format is consistent across the library: `POL-IAM-003 Section 3.6` or simply `POL-IAM-003` when referring to the document as a whole. The `docs/cross-reference-matrix.md` document tracks every cross-reference and provides the basis for ensuring consistency when document IDs or section numbers change.

When a referenced document does not exist in the adopting organization's library (because they have not adopted it, or because they use a different document for the same purpose), the consumer is expected to update the reference during customization. The customization guide describes the process.

## Revision history

Every document includes a revision history table at the bottom. The table tracks the version number, the date, the author of the revision, and a brief description of the change. The revision history is the consumer's record of how their adopted instance has evolved, separate from the upstream library's release history.

When a consumer adopts a document from this library, the recommended practice is to begin a fresh revision history starting at version 1.0 with the adoption date.

## Voice violations to watch for

Contributors and consumers should self-check against this list before publishing. The voice is preserved by attention to small details, and small details accumulate quickly when not policed.

- Hedging phrases ("it is important to note," "it should be observed")
- Corporate-speak ("leverage," "synergy," "robust," "seamless," "best-in-class")
- Empty intensifiers ("very," "really," "extremely")
- Cross-references to documents that do not exist in the library or that use the wrong document ID
- Placeholders that have been filled in with example values rather than left as bracketed placeholders for the consumer
- Product names in placeholders or examples
- Unsourced statistics

A consistent application of these rules is what makes the library feel like a professional product rather than a collection of documents.


