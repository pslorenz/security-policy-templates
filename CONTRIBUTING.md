# Contributing to Security Policy Templates

Thank you for considering a contribution to this library. This document explains how contributions work, what kinds of contributions are most useful, and what to expect from the review process.

---

## What this project is, in case it affects your decision to contribute

This is a personal project maintained on a best-effort basis. The author works on it in available time, alongside other professional work. That has implications worth being upfront about.

Pull requests will be reviewed, but not always quickly. Two weeks is a typical response time. Longer is possible during busy periods. If a contribution is time-sensitive on your end, that timeline may not work for you, and forking the library to maintain your own derivative is a reasonable choice.

The library is opinionated. Contributions that align with the existing voice, structure, and editorial choices have a clear path to merge. Contributions that propose substantial structural changes or that disagree with the library's opinions may not be accepted, even if the contribution itself is well-crafted. A declined contribution says nothing about the contributor. Keeping one coherent point of view across a library of related documents is part of what makes the library useful, and some good work does not fit that point of view.

The author makes no commitment to incorporate every suggestion. Issues are welcome, discussion is welcome, but there is no service-level agreement on response or merge timelines.

If those expectations are workable for you, please continue.

## Kinds of contributions that are especially welcome

**Corrections.** Factual errors, broken cross-references, outdated framework citations, typos, broken Markdown rendering, incorrect command syntax in runbooks, and similar errors are the most useful kind of contribution. They are specific, easy to review, and clearly improve the library.

**Adaptations of existing documents to additional regulatory frameworks.** The library aligns to CIS Controls v8.1 and NIST CSF 2.0 by default. Contributions that produce HIPAA, PCI DSS, SOC 2, ISO 27001, CMMC, or other framework addenda are useful for adopters in those sectors. Addenda should be additive (separate documents that supplement the existing policies) rather than replacing the existing alignment.

**Concrete example improvements.** The policies stay vendor-neutral: placeholders and examples describe a category of tool rather than naming products, and platform names appear only where a provision is specific to that platform. Suggestions that make an example clearer or more current within those limits are welcome, such as replacing a deprecated platform feature name with its current one.

**New documents that fill clear gaps in the library.** The framework mapping document and the cross-reference matrix identify documents that are planned but not yet started. Contributions that draft these documents in the existing voice and structure are welcome. Current examples include a HIPAA addendum once the Security Rule revision settles, runbooks for endpoint baseline deployment and vulnerability triage, a network segmentation runbook, and an asset reconciliation template. Before starting on a new document, please open an issue to discuss scope and approach.

## Kinds of contributions that face higher review barriers

**Structural changes to the library.** The directory layout, the document ID convention, the section structure within document types, and the framework alignment approach are stable. Changes to these are unlikely to be accepted unless there is a clear and substantial reason.

**Voice changes.** The voice and tone of the library is documented in `docs/style-guide.md`. Contributions that are well-meaning but in a different voice (more formal, more casual, more corporate, more academic) will likely be rewritten during review or returned for revision. Reading the style guide before contributing prose saves everyone time.

**Substantial new content categories.** Adding a new family code, a new document type prefix, or a new content category requires discussion before significant work goes into it. Open an issue first.

**Contributions that move the library toward commercial product positioning.** This library is a personal public-service contribution. Suggestions that would make it look like a vendor product (added marketing, contact-the-author calls to action, sales funnels, premium tier hints) will not be accepted.

## How to contribute

The standard GitHub workflow applies:

1. Fork the repository to your own account.
2. Create a branch for your contribution. Use a descriptive name.
3. Make your changes in the branch. Edit the Markdown source.
4. Verify that your changes meet the consistency requirements documented below.
5. Open a pull request against the main branch with a clear description of the change.
6. Respond to review feedback as it comes.

For small corrections (typos, broken links, minor errors), a pull request without a prior issue is fine. For larger contributions or new documents, please open an issue first to discuss scope and approach. This avoids the awkward situation where a contributor invests significant effort into something that does not align with the library's direction.

## Consistency requirements

Contributions should meet the consistency requirements documented across the library's scaffolding:

**Document structure:** New policies and runbooks follow the section structures documented in the style guide. New templates follow the patterns established by the existing templates.

**Cross-references:** Update `docs/cross-reference-matrix.md` to reflect any new relationships your contribution introduces or any existing relationships it changes.

**Framework alignment:** Where a contribution claims coverage of CIS Controls v8.1 or NIST CSF 2.0 controls, the document content must address those controls. Cite specific safeguards and subcategories rather than whole controls or categories. The framework mapping document is the canonical view of coverage.

**Glossary:** Define new terms in `docs/glossary.md` if your contribution introduces them. Use existing defined terms consistently.

**Placeholders:** Use the standard placeholder convention ([BRACKETED_UPPERCASE_WITH_UNDERSCORES]). Register every new placeholder in `placeholders.toml` with its phase (`adoption` if it is filled once when the library is customized, `use` if it is filled each time a template is used) and a description. Adoption-time placeholders also need a plain-language `question` and a `section` for the intake questionnaire, or a `default`, then run `python3 scripts/generate.py --update-guide` to refresh the customization guide's table. The automated check fails on unregistered placeholders, unused registrations, and an out-of-date table. Placeholder examples name a category of tool, never a product.

**Automated checks:** Every push and pull request runs `scripts/check_library.py` through GitHub Actions. It confirms that every referenced document ID exists, that every cited section exists in its target, that each document's filename, title, and metadata ID agree, that numbers run sequentially from 001 within each type and family, that every document carries the attribution line, and that the voice rules below hold. Run it locally before opening a pull request:

```bash
python3 scripts/check_library.py
```

A pull request that fails the check is not reviewed until it passes.

**Voice checks:** The individual searches the script performs, for running by hand.

```bash
# Em-dashes and en-dashes
grep -rnP '\x{2014}|\x{2013}' --include=*.md .
# Sentences that start with And or But
grep -rnE '(^|\. )(And|But) ' --include=*.md .
# Shall
grep -rnwi 'shall' --include=*.md .
# Hedging, intensifiers, and corporate-speak
grep -rniwE 'leverage|synergy|robust|seamless|best-in-class|world-class|delve|very|really|extremely|incredibly|it is important to note' --include=*.md .
# British spellings
grep -rniE 'organis|behaviour|programme|prioritis|licence' --include=*.md .
```

These should return no matches in policy, runbook, or scaffolding documents. They may appear in glossary definitions or style guide examples where the term is being defined or explicitly cited.

## Licensing of contributions

By submitting a contribution to this repository, you agree that it is licensed under the same terms as the part of the library it changes: documents, templates, and documentation under Creative Commons Attribution 4.0 International (`LICENSE`), and code in `scripts/` and `tests/` under the MIT License (`LICENSE-CODE`). Contributions come in under the same license the library goes out under.

New documents end with the standard closing attribution line, word for word:

```
*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
```

The automated check fails a document whose line is missing or worded differently, because the generator relies on the exact wording to remove it.

You retain copyright in your contribution. The license you grant is non-exclusive, meaning you can also share your contribution under other terms elsewhere if you choose.

If you are contributing on behalf of an employer or organization that holds rights to your work product, please confirm that you have authorization to license the contribution under CC BY 4.0 before submitting. Most employers permit this kind of public-domain or open-license contribution to security and policy resources, but confirming is the contributor's responsibility.

Significant contributors are acknowledged in the library's contributor list, maintained as part of the changelog or release notes. Acknowledgment is the form of recognition this project provides; there is no monetary compensation for contributions.

## Reporting security issues in the templates themselves

If you identify a security issue in the templates (a policy that recommends an insecure practice, a runbook that produces an insecure outcome, a configuration example that exposes data), please report it through a public issue or pull request. There is no security disclosure process beyond the standard GitHub workflow because the library is documentation rather than software, and the threats from a flawed policy template are addressed by correction in the public record.

If you identify a security issue in the GitHub repository infrastructure itself (compromised account, malicious commit, suspicious pull request), contact the author directly through the channels listed on the GitHub profile.

## Issues and discussion

The repository's issue tracker is the right place for:

Reporting errors, broken references, or outdated information.

Asking clarifying questions about a specific document or its intent.

Proposing new content or significant changes before starting work.

Discussing how the library might evolve.

The issue tracker is not the right place for:

Requests for individual consulting on adoption. The author cannot provide personalized advice on adopting the library to specific environments.

Generic security questions unrelated to the library.

Promotion of products, services, or unrelated content.

## A note on the voice

The library is written in a specific voice. The voice is part of what makes the documents useful: direct, declarative, opinionated where opinion serves the reader, candid about trade-offs, and free of corporate filler. Contributions that match this voice land smoothly. Contributions that drift from this voice generally need rewriting during review.

The rule exists because a library of related documents reads better when one voice runs through it. If you contribute and your contribution is rewritten substantially during review, the result is still your contribution. The thinking, structure, and substance came from you. The polish came from the editorial pass.

If you want to maintain a derivative library in your own voice, the license fully supports that. Forking is a respected outcome.

---

Thank you for being interested enough in this work to consider contributing.
