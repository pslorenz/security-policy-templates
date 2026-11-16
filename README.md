# Security Policy Templates

Stop copy-pasting client names into bloated enterprise templates. This repository provides a pragmatic, automated governance framework designed specifically for SMBs and the MSPs that secure them. Define your client's parameters once in a TOML file, and compile a complete, right-sized compliance library (Policies, Standards, Runbooks, and Trackers) in seconds.

A library of practical, framework-aligned security policy templates for managed service providers and small business IT teams. Documents are distributed under Creative Commons Attribution 4.0; the tooling is MIT licensed.

---

## What this is

This repository contains a curated set of security policy templates, supporting runbooks, recurring control templates, and client-facing materials. The artifacts are written to be lightly customized and put into service by an MSP delivering security advisory work to their clients, or by a small or mid-market organization implementing a security program internally.

The library is somewhat opinionated. The policies reflect choices about what works in real environments based on practitioner experience, not a survey of every possible control phrasing. The opinions are made explicit where they matter, so a consumer can see what to keep, what to adjust, and what to reject for their context.

## What it is not

This library is not a substitute for legal review, regulatory consultation, or qualified security advisory work for your specific environment. Policy text adopted from this repository should be reviewed by appropriate stakeholders within the adopting organization before publication. Where regulatory frameworks beyond CIS Controls v8.1 and NIST Cybersecurity Framework 2.0 apply (HIPAA, PCI DSS, SOX, NYDFS, CMMC, ISO 27001, SOC 2, and others), additional content and review will be required to meet those frameworks' specific requirements.

This library does not replace the work of building a security program. It provides the documents that support the creation of a security program. The work itself, building the inventory, training the team, running the operational cadences, responding to incidents, remains the consumer's to do.

## Who this is for

The primary audience is the managed service provider looking for a starting point that does not require licensing a commercial policy library. The artifacts assume an MSP-client relationship in their default phrasing, with adaptation guidance provided in the customization guide for organizations using the pack internally.

The secondary audience is the small or mid-market organization with an internal IT lead or security-curious operator who needs to stand up a reasonable security program without the budget for outside counsel. The pack is sized for this audience: simpler than a Fortune 500 program, more substantial than a checklist.

## What is in the library

The library is organized into six content categories, plus scaffolding documentation that establishes the conventions across the pack.

**Policies** define what the organization commits to doing. They are the controlled documents that go to leadership for approval and to auditors for inspection. Each policy is aligned to specific controls in CIS Controls v8.1 and NIST Cybersecurity Framework 2.0.

**Runbooks** operationalize the policies. They are the how-to documents that an engineer or consultant follows to execute the requirements the policy establishes. Where a policy says the organization must maintain an inventory, the runbook describes how to produce the inventory.

**Standards** carry the technical specifics that policies point to: password length and MFA methods, federation protocols, log sources and retention. They change more often than the policies above them.

**Templates** are recurring control artifacts. They are the Markdown registers, inventories, and reports that produce evidence of the controls running over time: a risk register, an exception register, a vendor inventory, a log source inventory, a quarterly metrics report. These are the artifacts an auditor asks to see.

**Framework addenda** in `addenda/` supplement the library for a specific regulation. Each maps the framework's requirements to the library, lists what the library does not cover, and sets the provisions that override library defaults within the regulated scope. The first addendum covers CMMC Level 2.

**Client-facing materials** are the documents written for the business owner, the executive sponsor, or the prospect. They translate the technical content of the policies and runbooks into the language a non-technical stakeholder can understand and act on. They are short, plain, and editorially polished.

**Scaffolding documentation** in the `docs/` directory establishes the conventions: the adoption guide that sets what to adopt first and what to scale down, the CIS IG1 checklist that maps every Implementation Group 1 safeguard to the document that meets it, the intake questionnaire that collects an organization's decisions, the glossary that defines terms used across the pack, the style guide that captures the voice and formatting rules, the customization guide that explains how to adapt the templates for use, the framework mapping that documents the CIS and NIST alignment, and the cross-reference matrix that shows how the documents connect to one another.

## How to use this library

The simplest path is to fork the repository, decide which documents you need, customize them for your environment, and put them into service. Four steps in detail:

First, read `docs/adoption-guide.md`. Five questions about your organization decide which documents apply, and the guide sorts them into three waves (what to adopt first, what follows within six months, and what applies only in some situations) with profiles for common types of small organizations. Most organizations do not need every document, and none needs them all on day one.

Second, read the docs/customization-guide.md document. It explains the placeholder convention used throughout the library, the cross-references between documents that need to remain consistent, and the editorial choices that shape the templates. Twenty minutes spent on this guide saves hours of rework later.

Third, collect the organization’s decisions. Export the intake questionnaire to Excel with python3 scripts/export.py --questionnaire intake.xlsx, and work through it with the organization. Each row says who usually answers it and shows the sentence the answer will complete. (The Markdown version, docs/intake-questionnaire.md, works too.) Then convert the answers into a configuration file with python3 scripts/intake.py intake.xlsx --out clients/acme.toml. examples/clients/sample-remote-firm.toml shows a complete configuration.

Fourth, generate and review. Run python3 scripts/generate.py clients/acme.toml, then read GENERATION_REPORT.md in the output folder. Fill in anything it lists as missing, correct anything that reads poorly in context, and run the generator again until the report is clean.

Fifth, produce the deliverables. Run python3 scripts/export.py build/acme --config clients/acme.toml to create Word documents and Excel workbooks. Review and make final edits in Word, have the executive sponsor approve and sign the policies, and export to PDF from Word if you need it. Export requires Pandoc and the Python packages python-docx and openpyxl; the customization guide covers setup.

Organizations that prefer to work by hand can skip the scripts: every document uses bracketed uppercase placeholders ([EFFECTIVE_DATE], [EXECUTIVE_SPONSOR], [POLICY_OWNER], and others), and the customization guide lists every one and where it appears.

Documents are distributed as Markdown source files in this repository. Consumers who need Word or PDF output for client delivery or audit submission can convert the Markdown with a standard tool such as Pandoc; the formatting conventions in the style guide are chosen so that conversion stays clean.

## Versioning and stability

The library uses semantic versioning. Major version increments indicate breaking changes to document IDs or structural conventions. Minor version increments add new content. Patch increments correct errors or refresh references.

The library is currently at version 0.2.0. The roadmap is documented in `CHANGELOG.md`. Major content additions are announced as tagged releases. Content adopted from a specific release tag remains stable; content pulled from the main branch reflects in-progress work and may change.

Consumers who require stability should fork from a release tag rather than from main.

## Contributing

Contributions are welcome. The `CONTRIBUTING.md` document describes the editorial standards, the framework alignment requirements, and the review process for pull requests. Contributions that maintain the voice and structural conventions documented in `docs/style-guide.md` will be reviewed promptly. Contributions that propose new content categories or significant restructuring are best discussed in an issue first.

The library is maintained as a personal project on a best-effort basis. Response times for issues and pull requests will not match a commercial product. Consumers who require commercial support are encouraged to fork and maintain their own derivative or to engage qualified security advisory services.

## Licensing

The documents, templates, and documentation are licensed under Creative Commons Attribution 4.0 International (`LICENSE`). The software in `scripts/` and `tests/` is licensed under the MIT License (`LICENSE-CODE`).

**Adopting the documents for your own organization requires no credit in them.** Each document ends with a line naming the source, and that line says it may be removed. `scripts/generate.py` removes it by default and writes a single NOTICE file alongside the generated documents instead.

**Redistributing the library, or a collection derived from it, requires credit once.** If you publish or hand others a policy pack built from this library, credit the original author, link to the license, and note that changes were made. A README or NOTICE with the collection is enough; the credit does not need to appear in each document. The license permits commercial and non-commercial use, modification, and distribution, including in derivative works distributed under other terms.

The full license text is in the `LICENSE` file in the repository root. Adopting organizations should consult their legal counsel regarding the implications of the license for their specific use case.

## Author

Steven Lorenz. The author maintains this library as a personal contribution to the security community. The library reflects the author's individual professional opinions and does not represent the views of any current or former employer.

Repository: `github.com/pslorenz/security-policy-templates`

---

*This library is a work of practitioner experience, not a substitute for legal advice or qualified security counsel. Adopt at your own discretion.*
