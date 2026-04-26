# Security Policy Templates

A library of practical, framework-aligned security policy templates for managed service providers and small business IT teams. Distributed under Creative Commons Attribution-ShareAlike 4.0.

---

## What this is

This repository contains a curated set of security policy templates, supporting runbooks, recurring control templates, and client-facing materials. The artifacts are written to be lightly customized and put into service by an MSP delivering security advisory work to their clients, or by a small or mid-market organization implementing a security program internally.

The library is opinionated. The policies reflect choices about what works in real environments based on practitioner experience, not a survey of every possible control phrasing. The opinions are made explicit where they matter, so a consumer can see what to keep, what to adjust, and what to reject for their context.

## What it is not

This library is not a substitute for legal review, regulatory consultation, or qualified security advisory work for your specific environment. Policy text adopted from this repository should be reviewed by appropriate stakeholders within the adopting organization before publication. Where regulatory frameworks beyond CIS Controls v8 and NIST Cybersecurity Framework 2.0 apply (HIPAA, PCI DSS, SOX, NYDFS, CMMC, ISO 27001, SOC 2, and others), additional content and review will be required to meet those frameworks' specific requirements.

This library does not replace the work of building a security program. It provides the documents that support the work. The work itself, building the inventory, training the team, running the operational cadences, responding to incidents, remains the consumer's to do.

## Who this is for

The primary audience is the managed service provider building a security advisory practice and looking for a starting point that does not require licensing a commercial policy library. The artifacts assume an MSP-client relationship in their default phrasing, with adaptation guidance provided in the customization guide for organizations using the pack internally.

The secondary audience is the small or mid-market organization with an internal IT lead or security-curious operator who needs to stand up a credible security program without the budget for outside counsel. The pack is sized for this audience: simpler than a Fortune 500 program, more substantial than a checklist.

## What is in the library

The library is organized into four content categories, plus scaffolding documentation that establishes the conventions across the pack.

**Policies** define what the organization commits to doing. They are the controlled documents that go to leadership for approval and to auditors for inspection. Each policy is aligned to specific controls in CIS Controls v8 and NIST Cybersecurity Framework 2.0.

**Runbooks** operationalize the policies. They are the how-to documents that an engineer or consultant follows to execute the requirements the policy establishes. Where a policy says the organization shall maintain an inventory, the runbook describes how to produce the inventory.

**Templates** are recurring control artifacts. They are the spreadsheets and forms that produce evidence of the controls running over time. A quarterly access review template, an asset inventory template, a vendor risk assessment template. These are the artifacts an auditor asks to see.

**Client-facing materials** are the documents written for the business owner, the executive sponsor, or the prospect. They translate the technical content of the policies and runbooks into the language a non-technical stakeholder can understand and act on. They are short, plain, and editorially polished.

**Scaffolding documentation** in the `docs/` directory establishes the conventions: the glossary that defines terms used across the pack, the style guide that captures the voice and formatting rules, the customization guide that explains how to adapt the templates for use, the framework mapping that documents the CIS and NIST alignment, and the cross-reference matrix that shows how the documents connect to one another.

## How to use this library

The simplest path is to fork the repository, customize the documents for your environment, and put them into service. Three steps in detail:

First, read the `docs/customization-guide.md` document. It explains the placeholder convention used throughout the library, the cross-references between documents that need to remain consistent, and the editorial choices that shape the templates. Twenty minutes spent on this guide saves hours of rework later.

Second, work through the placeholders. Every document has bracketed uppercase placeholders ([EFFECTIVE_DATE], [EXECUTIVE_SPONSOR], [POLICY_OWNER], and others) that the consumer fills in. The customization guide lists every placeholder and where it appears. A find-and-replace pass across the pack handles most of them.

Third, review the framework mapping in `docs/framework-mapping.md` to confirm the controls covered by the pack match the controls your organization or your client needs to satisfy. The pack covers CIS Controls v8 implementation groups one and two and the substantive content of NIST CSF 2.0. Frameworks beyond these require additional work.

Documents are distributed as Markdown source files in this repository. For consumers who need polished Word documents or working Excel templates, the `tools/` directory contains scripts that generate DOCX and XLSX outputs from the Markdown sources. Most consumers will use the Markdown directly; the conversion scripts exist for those who need traditional document formats for client delivery or audit submission.

## Versioning and stability

The library uses semantic versioning. Major version increments indicate breaking changes to document IDs or structural conventions. Minor version increments add new content. Patch increments correct errors or refresh references.

The library is currently at version 1.0.0. The roadmap is documented in `CHANGELOG.md`. Major content additions are announced as tagged releases. Content adopted from a specific release tag remains stable; content pulled from the main branch reflects in-progress work and may change.

Consumers who require stability should fork from a release tag rather than from main.

## Contributing

Contributions are welcome. The `CONTRIBUTING.md` document describes the editorial standards, the framework alignment requirements, and the review process for pull requests. Contributions that maintain the voice and structural conventions documented in `docs/style-guide.md` will be reviewed promptly. Contributions that propose new content categories or significant restructuring are best discussed in an issue first.

The library is maintained as a personal project on a best-effort basis. Response times for issues and pull requests will not match a commercial product. Consumers who require commercial support are encouraged to fork and maintain their own derivative or to engage qualified security advisory services.

## Licensing

This work is licensed under Creative Commons Attribution-ShareAlike 4.0 International. The license permits commercial and non-commercial use, modification, and distribution, subject to two requirements. First, attribution to the original author must be preserved in derivative works (the author identification line that appears in each document). Second, derivative works must be distributed under the same Creative Commons Attribution-ShareAlike 4.0 license.

The full license text is in the `LICENSE` file in the repository root. Adopting organizations should consult their legal counsel regarding the implications of the license for their specific use case.

## Author

Steven Lorenz. The author maintains this library as a personal contribution to the security community. The library reflects the author's individual professional opinions and does not represent the views of any current or former employer.

Repository: `github.com/pslorenz/security-policy-templates`

---

*This library is a work of practitioner experience, not a substitute for legal advice or qualified security counsel. Adopt at your own discretion.*
