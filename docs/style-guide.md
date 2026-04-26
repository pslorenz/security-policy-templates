# Style Guide

The conventions every document in this library follows. This guide exists so that contributors and adopters can keep the pack internally consistent as it evolves.

---

## Formatting conventions

The library uses Markdown as the canonical format. Documents render in GitHub's default theme without custom styling. The formatting conventions below ensure that documents render predictably and convert cleanly to DOCX or PDF when consumers need traditional formats.

**Heading hierarchy.** Documents use H1 for the document title, H2 for major sections (numbered, e.g. "## 3. Policy Statements"), H3 for subsections within sections (numbered, e.g. "### 3.1 Named Ownership"), and H4 sparingly for further subdivision when needed. The numbering convention helps consumers cross-reference specific provisions.

**Tables.** Used for metadata at the top of policy documents, for cross-reference matrices, and for revision history. Not used as a substitute for prose where prose would serve better.

**Code blocks.** Used in runbooks for executable commands. Triple-backtick fenced code blocks with language identifiers (`powershell`, `bash`, `python`) for syntax highlighting in GitHub's renderer.

**Bullet lists.** Used for genuinely parallel enumerated content. Each bullet should stand on its own as a complete thought. Sub-bullets are allowed but discouraged beyond one level of nesting.

**Bold and italic emphasis.** Bold for term introduction within a paragraph (the first appearance of a defined term, the role name in a roles-and-responsibilities section). Italic for document titles when referenced inline, and for the closing attribution line at the end of each document. Neither used for emphasis within sentences; sentence construction should carry the emphasis.

**Blockquotes.** Used for direct quotation from external sources only, with full citation. Not used as a styling device for callouts.

## Specific writing rules

These rules are enforced consistently across every document in the library.

**No hedging filler.** Phrases like "it is important to note that," "it should be observed that," "as we will see," and "in many ways" add words without adding meaning. Cut them. The reader should note what is important without being told to note it.

**No empty intensifiers.** "Very," "really," "extremely," "incredibly," and similar add no information. Either the underlying claim is strong enough to stand without them or the underlying claim needs to be made stronger.

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

**Recurring control templates** (REV-xxx-nnn) are XLSX or DOCX files. They follow the structure documented in their accompanying explainer or in the customization guide.

**Client-facing materials** are short documents (typically under fifteen hundred words) with minimal internal structure. They are written for non-technical readers and use plainer language than the policies and runbooks. They do not follow the numbered-section convention.

## Document IDs

Document IDs follow the pattern `[TYPE]-[FAMILY]-[NUMBER]`, where:

**Type** is a three-letter code identifying the document category:
- POL: Policy
- RUN: Runbook
- STD: Standard (a policy-adjacent document with more specific technical detail)
- REV: Recurring review or control evidence template
- PLY: Incident response playbook
- GUI: Guide (longer-form explanatory content)

**Family** is a two-to-four-letter code identifying the topical area:
- IAM: Identity and Access Management
- AM: Asset Management
- DC: Data Classification
- IR: Incident Response
- VM: Vulnerability Management
- EP: Endpoint Protection
- NET: Network Security
- AUP: Acceptable Use
- GRC: Governance, Risk, and Compliance
- AI: Artificial Intelligence and Agent Governance
- TPRM: Third-Party Risk Management

**Number** is a sequential integer within the family, zero-padded to three digits.

Examples: POL-IAM-001, POL-IAM-002, POL-IAM-011, RUN-IAM-011, REV-IAM-011, POL-AI-001.

The number is sequential within the family, not sequential within the type. POL-IAM-011 and RUN-IAM-011 are paired (the runbook operationalizes the policy), so they share the trailing number even though they have different type prefixes.

## Placeholder convention

Every document contains placeholders that the adopter fills in for their environment. Placeholders use the `[BRACKETED_UPPERCASE_WITH_UNDERSCORES]` pattern.

Standard placeholders used across the library:

- `[ORGANIZATION_NAME]`: The adopting organization's legal or operating name
- `[EFFECTIVE_DATE]`: The date the document goes into effect after adoption
- `[POLICY_OWNER]`: The named individual or role accountable for the document
- `[EXECUTIVE_SPONSOR]`: The named individual at the executive level who approves the document
- `[REVIEW_DATE]`: The date the document is next scheduled for review
- `[VERSION]`: The version number of the adopting organization's instance of the document

Document-specific placeholders use a descriptive name in the same format. The `docs/customization-guide.md` document lists every placeholder used in every artifact in the pack.

## Cross-references

Documents reference one another by document ID. The reference format is consistent across the library: `POL-IAM-011 Section 3.6` or simply `POL-IAM-011` when referring to the document as a whole. The `docs/cross-reference-matrix.md` document tracks every cross-reference and provides the basis for ensuring consistency when document IDs or section numbers change.

When a referenced document does not exist in the adopting organization's library (because they have not adopted it, or because they use a different document for the same purpose), the consumer is expected to update the reference during customization. The customization guide describes the process.

## Revision history

Every document includes a revision history table at the bottom. The table tracks the version number, the date, the author of the revision, and a brief description of the change. The revision history is the consumer's record of how their adopted instance has evolved, separate from the upstream library's release history.

When a consumer adopts a document from this library, the recommended practice is to begin a fresh revision history starting at version 1.0 with the adoption date and a description noting the source ("Adopted from `github.com/pslorenz/security-policy-templates` v[X.Y]"). This preserves the upstream attribution while creating a clean local history.

## Voice violations to watch for

Contributors and consumers should self-check against this list before publishing. The voice is preserved by attention to small details, and small details accumulate quickly when not policed.

- Hedging phrases ("it is important to note," "it should be observed")
- Corporate-speak ("leverage," "synergy," "robust," "seamless," "best-in-class")
- Empty intensifiers ("very," "really," "extremely")
- Cross-references to documents that do not exist in the library or that use the wrong document ID
- Placeholders that have been filled in with example values rather than left as bracketed placeholders for the consumer

A consistent application of these rules is what makes the library feel like a professional product rather than a collection of documents.


