# Customization Guide

How to adapt the templates in this library for your organization or your client. This guide is the first document a new adopter should read. Twenty minutes here saves hours of rework later.

---

## Before you start

Three decisions to make before touching any template.

**Decide who is adopting.** Is this for your own organization (you are the IT lead implementing internally) or for your client (you are an MSP delivering to a customer)? The templates are written with MSP-client framing as the default. The default reads naturally for the MSP case and requires light reframing for the internal case. Specific reframing guidance is below.

**Decide on the scope of adoption.** Are you adopting the entire library, a specific subset (for example, just the identity governance documents), or specific individual policies? Adopting the whole library is more efficient if the organization has time to do it; partial adoption is acceptable but requires care with the cross-references between documents.

**Decide on the authority model.** Each policy has an owner and an executive sponsor. Identify the named individuals who will fill those roles before customization begins. The owner is the person accountable for keeping the document current; the sponsor is the executive who approves it. In a small organization these may be the same person; in a larger one they should be different.

## The placeholder convention

Every template uses placeholders for the values that vary between adopting organizations. Placeholders follow the pattern `[BRACKETED_UPPERCASE_WITH_UNDERSCORES]`. A find-and-replace pass across the pack handles most of them.

The standard placeholders, used across multiple documents:

`[ORGANIZATION_NAME]` is the legal or operating name of the adopting organization. Used in policy headers, in references to "the organization," and occasionally in scope definitions where the organization is named explicitly.

`[EFFECTIVE_DATE]` is the date the document goes into effect after adoption. Use ISO date format (YYYY-MM-DD) for consistency, or the format your organization uses in other governance documents if it differs.

`[POLICY_OWNER]` is the named individual or role accountable for the document. May be a specific person (Jane Doe, Director of Information Security) or a role title (Information Security Manager). Roles are more durable than names; names are more accountable.

`[EXECUTIVE_SPONSOR]` is the named individual at the executive level who approves the document. Typical sponsors include the CIO, CISO, COO, CFO, CEO, or a board member with security responsibility.

`[REVIEW_DATE]` is the date the document is next scheduled for review. The metadata tables in the library show the review cycle rather than a date; adopters who track the next review date add a row for it. Most policies in the library specify an annual review cycle; the review date should be set one year from the effective date.

`[VERSION]` is the version number of the adopting organization's instance of the document. The library's metadata tables ship at 1.0, which is the recommended starting version for the initial adoption.

Document-specific placeholders use descriptive names in the same format. Every one in the library is listed below with the documents that use it. The table is generated from `placeholders.toml`, the registry of every placeholder and whether it is filled at adoption or each time a template is used; to change it, edit the registry and run `python3 scripts/generate.py --update-guide`. Placeholders whose examples describe a category of tool are deliberately vendor-neutral; substitute the specific product the adopting organization uses.

| Placeholder | Used in | What to supply |
|---|---|---|
| `[AI_TOOL_NAME_AND_TIER]`, `[ALTERNATE_LOCATION]`, `[BACKUP_PLATFORM]`, `[BACKUP_VENDOR]`, `[CRITICAL_SYSTEM]`, `[DEVICE_RETENTION]`, `[DNS_SERVICE]`, `[EDR_PLATFORM]`, `[EMAIL_SECURITY_GATEWAY]`, `[FIREWALL]`, `[FUNCTION]`, `[NHI_ID]`, `[PLATFORM]`, `[PRODUCTIVITY_PLATFORM]`, `[SAAS_APPLICATION]`, `[VENDOR]`, `[VENDOR_RETENTION]`, `[VM_PLATFORM]`, `[VPN_GATEWAY]`, `[WEB_GATEWAY]` | TPL-AI-001, TPL-BC-001, TPL-GOV-003, TPL-IAM-001, TPL-IAM-002, TPL-LOG-001 | Seed-row placeholders; replace with real entries during the first pass through the template |
| `[AI_TOOL_REQUEST_CHANNEL]` | POL-AI-001 | Where users request a new AI tool |
| `[AMOUNT]`, `[BRIEF_DESCRIPTION]`, `[CHANGES]`, `[CLASSIFICATION]`, `[CLIENT_EXPECTATIONS]`, `[CONTACT]`, `[DATE]`, `[INCIDENT_SUMMARIES]`, `[INSTRUCTIONS]`, `[METHOD]`, `[NAME]`, `[SERVICE]`, `[SUMMARY]`, `[TARGET]`, `[WHAT_HAPPENED]` | TPL-BC-001, TPL-GOV-001, TPL-GOV-003, TPL-GOV-004, TPL-LOG-001 | Template fill-in fields, completed each time the template is used |
| `[ANNUAL_ACKNOWLEDGMENT_MONTH]` | TPL-AUP-001 | When the annual policy acknowledgment is due |
| `[APPLICABLE_OBLIGATIONS]` | POL-GOV-001 | Laws, regulations, and contracts that impose security obligations |
| `[APPROVED_AI_TOOLS]` | POL-AI-001, POL-AUP-001 | AI tools approved for company data, with the classifications each is approved for |
| `[APPROVED_BROWSERS]` | STD-NET-001 | Browsers approved for company work |
| `[APPROVED_DNS_FILTERING]` | POL-NET-001 | Protective DNS service |
| `[APPROVED_EDR_PLATFORMS]` | POL-EP-001 | EDR platform in use |
| `[APPROVED_FIREWALL_VENDORS]` | POL-NET-001 | Edge firewall platforms |
| `[APPROVED_IDP]` | STD-IAM-002 | The single approved identity provider |
| `[APPROVED_MDM_PLATFORMS]` | POL-EP-001 | Mobile device management platform |
| `[APPROVED_PASSWORD_MANAGERS]` | STD-IAM-001 | Business password manager |
| `[APPROVED_REMOTE_ACCESS_TOOLS]` | POL-IAM-002 | Identity-gated access service |
| `[APPROVED_SECRETS_PLATFORMS]` | POL-IAM-003 | Secrets vaults for non-human credentials |
| `[APPROVED_STORAGE_PLATFORMS]` | POL-DC-001 | Approved storage for Confidential data |
| `[APPROVED_VENDOR_MONITORING]` | POL-TPRM-001 | Vendor breach or ratings monitoring, if any |
| `[APPROVED_VM_TOOLS]` | POL-VM-001 | Vulnerability discovery tools |
| `[ARCHIVE_RESTORE_TIME]` | STD-LOG-001 | How quickly archived logs can be restored for an investigation |
| `[AUP_VERSION]`, `[GOV_VERSION]` | TPL-AUP-001 | The policy versions being acknowledged, updated when either policy changes |
| `[CENTRAL_LOGGING_PLATFORM]` | STD-LOG-001, TPL-LOG-001 | The central logging or SIEM platform |
| `[CHANGE_RECORD_RETENTION]` | STD-OPS-001 | How long change records are retained |
| `[CHANGE_RECORD_SYSTEM]` | STD-OPS-001 | Where change records are kept |
| `[CHANGE_WINDOW]` | STD-OPS-001 | When higher-risk normal changes are made |
| `[CONTINUITY_DEPUTY]` | POL-BC-001, TPL-BC-001 | Who acts when the continuity lead is unavailable |
| `[CONTINUITY_ESCALATION_TIME]` | POL-BC-001, TPL-BC-001 | How long to wait for the lead or deputy before the senior manager acts |
| `[CONTINUITY_LEAD]` | POL-BC-001, TPL-BC-001 | Who declares and manages a continuity event |
| `[CONTRACT_REVIEW_PROCESS]` | POL-TPRM-001 | Reference to the organization's contract review process |
| `[CRITICAL_RPO]` | STD-DR-001 | Default recovery point objective for Critical systems |
| `[CRITICAL_RTO]` | STD-DR-001 | Default recovery time objective for Critical systems |
| `[CUI_PASSWORD_COMPLEXITY]` | ADD-CMMC-001 | Password complexity rule for CUI accounts |
| `[CUI_PASSWORD_HISTORY]` | ADD-CMMC-001 | Number of previous passwords that cannot be reused in the CUI environment |
| `[CUI_SCOPE_DOCUMENT]` | ADD-CMMC-001 | Where the CUI environment scope is recorded |
| `[CUI_SCREENING_PROCESS]` | ADD-CMMC-001 | Personnel screening process before CUI access |
| `[CYBER_INSURANCE_DOCUMENTATION]` | POL-IR-001 | Where the carrier and policy details are kept |
| `[DAILY_RETENTION]` | STD-DR-001 | How long daily backups are kept |
| `[DMARC_ENFORCEMENT_TIMELINE]` | STD-NET-001 | Target time to reach DMARC p=reject |
| `[ESTIMATED_PROGRAM_COST]`, `[TIMELINE_WEEKS]` | AI Governance Business Owner Explainer, NHI Business Owner Explainer | Program cost and duration for the adopting environment |
| `[IMPORTANT_RPO]` | STD-DR-001 | Default recovery point objective for Important systems |
| `[IMPORTANT_RTO]` | STD-DR-001 | Default recovery time objective for Important systems |
| `[INCIDENT_LEAD]`, `[INCIDENT_LEAD_NAME]`, `[IT_FUNCTION_NAME]`, `[IT_SUPPORT_CONTACT]`, `[PHONE]`, `[TIME]` | RUN-IR-001, TPL-BC-001 | Values filled in when a communication template is used, not at adoption |
| `[INCIDENT_RESPONSE_RETAINER_FIRM]` | POL-IR-001 | Retained incident response firm |
| `[INFORMATION_SECURITY_FUNCTION]` | POL-GOV-001, STD-LOG-001 | Who performs the Information Security function |
| `[LOG_TIME_ZONE]` | STD-LOG-001, TPL-LOG-001 | Time zone used for all log timestamps |
| `[MEETING_RECORD_RETENTION]` | POL-AI-001 | Retention period for meeting transcripts and AI summaries |
| `[MONITORING_COVERAGE]` | STD-LOG-001, TPL-LOG-001 | Hours of alert monitoring coverage |
| `[MONITORING_PROVIDER]` | STD-LOG-001, TPL-LOG-001 | Who monitors and triages alerts |
| `[MONTHLY_RETENTION]` | STD-DR-001 | How long monthly backups are kept |
| `[ORGANIZATION_GOVERNANCE_BODY]` | POL-GOV-001 | The body the executive sponsor reports to on security |
| `[PAYMENT_APPROVAL_THRESHOLD]` | STD-NET-001 | Payment amount above which two approvers are required |
| `[PAYMENT_HANDLING_PROCESS]` | POL-DC-001 | Where payment card handling is documented |
| `[PAYMENT_INCIDENT_THRESHOLD]` | STD-NET-001 | Payment amount above which an unverified payment-detail change is handled as an incident |
| `[QUARTER_YEAR]` | TPL-AI-001, TPL-GOV-004, TPL-IAM-001, TPL-IAM-002 | The quarter being reviewed or reported, filled in each quarter |
| `[REPORT_PHISHING_PROCESS]` | POL-AUP-001 | How users report suspected phishing |
| `[REPORTING_CHANNEL]` | POL-AUP-001, RUN-IR-001, TPL-AUP-001 | Where users report security problems |
| `[RISK_APPETITE_STATEMENT]` | TPL-GOV-001 | The executive sponsor's risk appetite statement |
| `[SCREENING_PROCESS]` | POL-PPS-001 | Where the pre-access screening process is documented |
| `[SECURITY_LEGAL_COUNSEL]` | POL-IR-001 | Counsel for security matters |
| `[STANDARD_RPO]` | STD-DR-001 | Default recovery point objective for Standard systems |
| `[TESTING_TIER]` | POL-GOV-001, STD-VM-001 | The security testing tier set under STD-VM-001 Section 3.1 |
| `[TIME_SOURCE]` | STD-LOG-001 | Authoritative time sources for logging systems |
| `[VALIDATION_PERIOD]` | STD-LOG-001, TPL-LOG-002 | How long new log sources are validated before being relied on |
| `[VISITOR_LOG_RETENTION]` | POL-PPS-001 | How long visitor records are kept |
| `[VULNERABILITY_DISCLOSURE_CHANNEL]` | POL-VM-001 | Address or form for external vulnerability reports |
| `[WEEKLY_RETENTION]` | STD-DR-001 | How long weekly backups are kept |

Every placeholder that once stood in for an unpublished document has been replaced with the document's ID. If a referenced document is not part of the adopting organization's library, update the reference during Step five of the customization sequence.

## Collecting the answers: the intake questionnaire

`docs/intake-questionnaire.md` asks every decision the generator needs in plain language, grouped by who usually answers: the owner, operations or HR, finance, and whoever runs IT. Part 1 is the five scoping questions from the adoption guide. Part 2 has one question for each adoption-time placeholder, the sentence from the library where the answer will appear (with ___ marking the spot), and an example answer.

For working with a client, export it to Excel: `python3 scripts/export.py --questionnaire intake.xlsx` produces a workbook with one row per question, dropdowns for the scope answers, and a shaded Answer column. Fill in either version with the client, then convert it:

```bash
python3 scripts/intake.py clients/acme-intake.xlsx --out clients/acme.toml   # or a filled-in copy of the Markdown file
```

The result is the configuration file described below. Review it, then run the generator. Questions left blank are simply omitted, and the generator reports any that an adopted document needs.

Because answers go into the documents word for word, the "How your answer is used" column matters: an answer that completes the sentence naturally reads well in the finished document. The questionnaire is generated from `placeholders.toml`, so it always matches the library.

## Generating a customized copy

`scripts/generate.py` fills in every adoption-time placeholder from a single configuration file and writes a customized copy of the library, so the values are decided once and applied consistently. It needs Python 3.11 or later and nothing else.

**The configuration file.** Usually produced from the intake questionnaire, or written by hand. A TOML file with four tables. `[scope]` records the five questions from the adoption guide. `[documents]` records the status of any document that is not simply adopted ("Planned", "Not adopted", or "Adopted" with a level, such as "Adopted at the scripts and automations level"). `[values]` holds one entry per adoption-time placeholder. `[generation]` holds options. `examples/clients/sample-remote-firm.toml` is a complete example for a twenty-person firm; copy it and change the values.

**Running it.**

```bash
python3 scripts/generate.py clients/acme.toml               # writes build/acme/
python3 scripts/generate.py clients/acme.toml --out deliver/acme
```

**What it does.** It rejects misspelled or unknown placeholder names, and it rejects attempts to set use-time placeholders, which are template fields filled each time a template is used and must survive into the customized copy. It replaces each adoption-time placeholder, including any example text after "e.g.," with the configured value. It sets the status column of the suite table in POL-GOV-001 Section 3.7 from `[documents]`, and marks documents that are planned or not adopted with a status line under the title. Documents that are not adopted are kept, because adopted documents refer to them. Addenda default to "Not adopted", and POL-DEV-001 defaults from the code question in `[scope]`.

**When it fails.** If an adopted document still has an unfilled adoption-time placeholder, the script lists each one and exits with an error. The output is written for review but is not ready to use. Gaps in planned documents and the client-facing explainers are reported as warnings.

**Drafting with example text.** Setting `use_examples = true` under `[generation]` fills any missing value with the library's example text, wherever in the library that example appears, and lists each one in the report. Every document in a draft is marked DRAFT under its title, and unfilled placeholders are reported as warnings instead of errors. This is useful for a first draft to walk through with a client. A real deployment sets every value deliberately and leaves this option off.

**Attribution.** The generator removes each document's closing attribution line, since an organization's own copy does not need it, and writes a NOTICE file in the output folder that credits the source once. Set `keep_attribution = true` under `[generation]` to keep the line, for example when building a collection that will be redistributed.

**The report.** Each run writes `GENERATION_REPORT.md` in the output folder: the configuration used, the library revision, every document's status, any example text used, and any warnings. When the library is updated, regenerating each client and comparing the output with the previous version shows exactly what changed for that client.

The generator does not remove sections that do not apply. Where a provision does not fit, record it through the exception process in POL-GOV-001 Section 3.6, so the decision stays visible.

## Exporting to Word and Excel

`scripts/export.py` turns a generated library into the files an organization receives. It needs Pandoc 3.x and the Python packages python-docx and openpyxl (`pip install python-docx openpyxl`); the generator itself needs none of these.

```bash
python3 scripts/export.py build/acme --config clients/acme.toml --out deliver/acme
```

**Policies, standards, runbooks, addenda, and explainers become Word documents**, each with a page header naming the organization and the document, a footer with the classification, version, and page numbers, and shaded table headers. Policies, standards, and addenda end with an approval block for the executive sponsor's signature, because auditors and insurers often ask for signed policies.

**Templates become Excel workbooks**, one sheet per table with frozen headers, filters, shaded entry cells, and dropdowns wherever the template defines the answers (Yes / No, Pass / Fix / Remove, and similar). Each template also gets a Word copy holding the instructions, checks, and forms; tables too wide for a page are replaced there by a pointer to their sheet.

**Documents marked "Not adopted" are left out** unless `include_not_adopted` is set. The output folder also carries the license and the generation report.

**PDFs are deliberately not produced.** Review the Word documents, make any final edits, and export to PDF from Word when they are ready to distribute.

**Branding** comes from an optional `[export]` table in the client configuration: `font`, `primary_color`, `prepared_by` (shown in every footer, for the consultant or provider delivering the documents), and `logo` (an image for the page header). With no `[export]` table, the documents use a neutral default style.

## The customization sequence

The recommended sequence for customizing the pack, from clean fork to deployed library.

**Step one: fork or clone.** Fork the repository to your own GitHub account (if you intend to publish your derivative) or clone it to a private working location (if you will treat the customized library as an internal artifact). Either way, the license requires attribution, which the closing line in each document provides. The details are in the LICENSE file.

**Step two: fill in the placeholders.** Write a configuration file with the organization's scope, document statuses, and placeholder values, and run `scripts/generate.py` as described in Generating a customized copy above. Organizations that prefer to edit by hand can use a project-wide find-and-replace instead, working from the placeholder table, but the generator catches misspellings and missed placeholders that a manual pass will not.

**Step three: review and adapt opinionated provisions.** Several policies make specific recommendations that may not fit every adopting organization. Examples include the ninety-day credential rotation cadence, the dormancy thresholds for non-human identities, and the remediation cadences in the vulnerability management policy. Walk through each policy with the adopting organization's leadership and adapt these provisions where the organization's risk tolerance, regulatory environment, or operational reality requires different choices. Document the deviations in the revision history.

**Step four: review framework alignment.** The library aligns to CIS Controls v8.1 and NIST Cybersecurity Framework 2.0 by default. If the adopting organization is subject to additional frameworks (HIPAA Security Rule, PCI DSS, SOC 2, ISO 27001, CMMC, NYDFS, or others), the framework alignment section of each policy will need additional content. The `docs/framework-mapping.md` document indicates where the existing alignment provides partial coverage of other frameworks; gaps require additional control statements.

**Step five: review cross-references.** The `docs/cross-reference-matrix.md` document lists every cross-reference between documents in the pack. If the adopting organization is not adopting the full pack, references to documents outside the adopted set need to be updated to point to equivalent documents in the organization's existing library or removed if no equivalent exists.

**Step six: legal and stakeholder review.** Adopted policies should be reviewed by appropriate legal counsel and business stakeholders before publication. The library is a starting point, not a substitute for review by people who understand the adopting organization's specific environment.

**Step seven: approve and publish.** Each document is approved by its named executive sponsor before going into effect. The approval is recorded in the revision history. Once approved, the documents are published to the location the adopting organization uses for its policy library (an intranet, a wiki, or a document management system).

**Step eight: schedule the operational cadences.** The policies establish operational cadences (quarterly access reviews, annual policy review, monthly vulnerability metrics, and the quarterly program metrics report). These need to be scheduled in the organization's operational calendar, with named owners and tracking, before the policies can be said to be operational.

## Reframing for internal adoption

The library's default phrasing assumes an MSP-client or consulting relationship. For organizations adopting the pack internally, three categories of language need light editing.

**The phrase "the organization" is the default subject.** It works in either context, so no editing is required for most of the policy text. Where the policy refers to "the security advisor" or "the security provider," internal adopters should substitute "the Information Security function" or the equivalent role name.

**Client-facing materials in the `client-facing/` directory are written for the MSP's client.** For internal adoption, these materials are written for the executive sponsor or business owner of the adopting organization. The framing translates with light editing: replace "we" (referring to the MSP) with the adopting organization's IT function name, and replace "your organization" with "our organization" or the organization name.

**The runbooks assume the executor is an external consultant or engineer.** For internal adoption, the executor is an internal staff member. The procedural content does not change, but the references to "the field engineer" or "the consultant" should be replaced with the appropriate internal role name.

The customization guide does not enumerate every instance of these reframings; the adopting organization's editor reads through and adapts as appropriate.

## Common adaptation decisions

Several places in the library make opinionated choices that adopting organizations likely want to adjust.

**Credential rotation cadences.** The library defaults to ninety days for high-privilege credentials and annual for standard credentials. Some organizations operate on different cadences for valid reasons. The cadence appears in STD-IAM-001 Section 3.7 and POL-IAM-003 Section 3.5; both should be updated together to remain consistent.

**Dormancy thresholds for non-human identities.** The library defaults to ninety days (flag), one hundred eighty days (disable pending), and three hundred sixty-five days (delete). Some organizations need shorter or longer thresholds. The thresholds appear in POL-IAM-003 Section 3.7 and in the dormancy analysis in RUN-IAM-001 Phase 2; both should be updated together.

**Specific tool recommendations.** Several runbooks reference specific tools (Microsoft Graph PowerShell SDK, Power Platform admin module, GitHub CLI). Adopting organizations using different tooling stacks should substitute their equivalent tools. The procedural intent is preserved; the specific commands change.

**Phishing-resistant MFA scope.** The library requires phishing-resistant authentication for all privileged accounts with no exceptions. Some organizations have legitimate technical limitations (legacy systems, vendor constraints) that require time-bound exceptions. These should be documented as exceptions per the policy's exception process, not adopted as permanent standing carve-outs in the policy text.

**Risk tolerance language.** Each policy includes implicit assumptions about the adopting organization's risk tolerance. Higher-risk-tolerance organizations may want to soften some "must" provisions to "should" or add exception processes for them. Lower-risk-tolerance organizations may want to strengthen some provisions or add additional controls. The adopting organization's executive sponsor is the appropriate authority for these decisions.

## What not to change

Several characteristics of the library should be preserved through adoption to maintain the pack's internal consistency and framework alignment.

The document ID convention should be preserved as long as the document remains recognizably derived from the upstream source. An adopted POL-IAM-003 should remain POL-IAM-003. Substantial restructuring that produces a meaningfully different document warrants a new document ID, but minor customization does not.

The numbered section structure should be preserved. Cross-references throughout the library use specific section numbers (POL-IAM-003 Section 3.6, for example). Renumbering sections breaks every document that references the renumbered section.

The framework alignment section should be preserved at minimum, even if additional frameworks are added. Removing the CIS Controls v8.1 or NIST CSF 2.0 alignment in favor of a different framework would break the cross-document mapping documented in framework-mapping.md.

The closing attribution line may be removed by an organization adopting the documents for its own use, and the generator removes it by default. An organization or provider redistributing the library, or a collection derived from it, to others gives credit once, for example with the NOTICE file the generator writes; see LICENSE. Set `keep_attribution = true` under `[generation]` to keep the line in every document when building a collection for redistribution.

## After adoption

Adoption is the beginning of the relationship with the policy library, not the end. Three ongoing practices keep the adopted library current.

**Watch the upstream releases.** This library is updated periodically with new content, refreshed framework references, and corrections to existing artifacts. Subscribing to the repository's releases ensures that adopters see significant changes when they happen. The `CHANGELOG.md` file documents what changed in each release.

**Maintain the local revision history.** Every customization, every adaptation, every responsive update should be recorded in the document's revision history. The history is the auditable record of how the adopted library has evolved.

**Re-review on the documented cadence.** Each policy specifies a review cycle (typically annual). The review confirms that the document still reflects the organization's intent, that the framework references are still current, and that any external changes (new regulations, new tools, new threats) are reflected in the document.

The library is a living artifact in both the upstream and downstream contexts. Treating it as a one-time download produces a library that goes stale within eighteen months. Treating it as an ongoing reference produces a security program that grows in capability over time.

## Questions and contributions

Questions about specific customizations are best directed to the adopting organization's qualified security advisors. The upstream library author is not in a position to provide individual consulting on adoption.

General questions about the library, suggestions for improvements, and pull requests are welcome through the repository's issue tracker. The `CONTRIBUTING.md` document describes the contribution process.

---

*Customization is the work that turns a generic template into a working policy. Do the work; the policy is only as good as the customization that fits it to the environment.*
