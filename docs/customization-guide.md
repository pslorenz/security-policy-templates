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

`[REVIEW_DATE]` is the date the document is next scheduled for review. Most policies in the library specify an annual review cycle; the review date should be set one year from the effective date.

`[VERSION]` is the version number of the adopting organization's instance of the document. Begin at 1.0 for the initial adoption.

Document-specific placeholders use descriptive names in the same format. Examples: `[QUARTER_YEAR]` in the recurring access review template, `[INCIDENT_RESPONSE_RETAINER]` in the incident response policy if the organization uses one. Each document lists its specific placeholders in a comment at the top of the file.

## The customization sequence

The recommended sequence for customizing the pack, from clean fork to deployed library.

**Step one: fork or clone.** Fork the repository to your own GitHub account (if you intend to publish your derivative under the share-alike license terms) or clone it to a private working location (if you will treat the customized library as an internal artifact). The licensing implications are described in the LICENSE file.

**Step two: replace standard placeholders.** Use a project-wide find-and-replace to substitute the standard placeholders ([ORGANIZATION_NAME], [POLICY_OWNER], [EXECUTIVE_SPONSOR], [EFFECTIVE_DATE], [REVIEW_DATE], [VERSION]) across every document in the pack. Most code editors and IDE tools support project-wide find-and-replace; on the command line, `find` and `sed` accomplish the same thing.

**Step three: review and adapt opinionated provisions.** Several policies make specific recommendations that may not fit every adopting organization. Examples include the ninety-day credential rotation cadence, the dormancy thresholds for non-human identities, the specific tools recommended for endpoint detection. Walk through each policy with the adopting organization's leadership and adapt these provisions where the organization's risk tolerance, regulatory environment, or operational reality requires different choices. Document the deviations in the revision history.

**Step four: review framework alignment.** The library aligns to CIS Controls v8 and NIST Cybersecurity Framework 2.0 by default. If the adopting organization is subject to additional frameworks (HIPAA Security Rule, PCI DSS, SOC 2, ISO 27001, CMMC, NYDFS, or others), the framework alignment section of each policy will need additional content. The `docs/framework-mapping.md` document indicates where the existing alignment provides partial coverage of other frameworks; gaps require additional control statements.

**Step five: review cross-references.** The `docs/cross-reference-matrix.md` document lists every cross-reference between documents in the pack. If the adopting organization is not adopting the full pack, references to documents outside the adopted set need to be updated to point to equivalent documents in the organization's existing library or removed if no equivalent exists.

**Step six: legal and stakeholder review.** Adopted policies should be reviewed by appropriate legal counsel and business stakeholders before publication. The library is a starting point, not a substitute for review by people who understand the adopting organization's specific environment.

**Step seven: approve and publish.** Each document is approved by its named executive sponsor before going into effect. The approval is recorded in the revision history. Once approved, the documents are published to the location the adopting organization uses for its policy library (SharePoint, Confluence, internal wiki, document management system).

**Step eight: schedule the operational cadences.** The policies establish operational cadences (quarterly access reviews, annual policy review, monthly metrics reporting). These need to be scheduled in the organization's operational calendar, with named owners and tracking, before the policies can be said to be operational.

## Reframing for internal adoption

The library's default phrasing assumes an MSP-client or consulting relationship. For organizations adopting the pack internally, three categories of language need light editing.

**The phrase "the organization" is the default subject.** It works in either context, so no editing is required for most of the policy text. Where the policy refers to "the security advisor" or "the security provider," internal adopters should substitute "the Information Security function" or the equivalent role name.

**Client-facing materials in the `client-facing/` directory are written for the MSP's client.** For internal adoption, these materials are written for the executive sponsor or business owner of the adopting organization. The framing translates with light editing: replace "we" (referring to the MSP) with the adopting organization's IT function name, and replace "your organization" with "our organization" or the organization name.

**The runbooks assume the executor is an external consultant or engineer.** For internal adoption, the executor is an internal staff member. The procedural content does not change, but the references to "the field engineer" or "the consultant" should be replaced with the appropriate internal role name.

The customization guide does not enumerate every instance of these reframings; the adopting organization's editor reads through and adapts as appropriate.

## Common adaptation decisions

Several places in the library make opinionated choices that adopting organizations frequently want to adjust.

**Credential rotation cadences.** The library defaults to ninety days for high-privilege credentials and annual for standard credentials. Some organizations operate on different cadences for valid reasons. The cadence is adjusted in the policy text and the inventory template; both should be updated together to remain consistent.

**Dormancy thresholds for non-human identities.** The library defaults to ninety days (flag), one hundred eighty days (disable pending), and three hundred sixty-five days (delete). Some organizations need shorter or longer thresholds. The thresholds appear in the policy and in the formulas in the access review template; both should be updated together.

**Specific tool recommendations.** Several runbooks reference specific tools (Microsoft Graph PowerShell SDK, Power Platform admin module, GitHub CLI). Adopting organizations using different tooling stacks should substitute their equivalent tools. The procedural intent is preserved; the specific commands change.

**Phishing-resistant MFA scope.** The library requires phishing-resistant authentication for all privileged accounts with no exceptions. Some organizations have legitimate technical limitations (legacy systems, vendor constraints) that require time-bound exceptions. These should be documented as exceptions per the policy's exception process, not adopted as permanent standing carve-outs in the policy text.

**Risk tolerance language.** Each policy includes implicit assumptions about the adopting organization's risk tolerance. Higher-risk-tolerance organizations may want to soften some "shall" provisions to "should" or add exception processes for them. Lower-risk-tolerance organizations may want to strengthen some provisions or add additional controls. The adapting organization's executive sponsor is the appropriate authority for these decisions.

## What not to change

Several characteristics of the library should be preserved through adoption to maintain the pack's internal consistency and framework alignment.

The document ID convention should be preserved as long as the document remains recognizably derived from the upstream source. An adopted POL-IAM-011 should remain POL-IAM-011. Substantial restructuring that produces a meaningfully different document warrants a new document ID, but minor customization does not.

The numbered section structure should be preserved. Cross-references throughout the library use specific section numbers (POL-IAM-011 Section 3.6, for example). Renumbering sections breaks every document that references the renumbered section.

The framework alignment section should be preserved at minimum, even if additional frameworks are added. Removing the CIS Controls v8 or NIST CSF 2.0 alignment in favor of a different framework would break the cross-document mapping documented in framework-mapping.md.

The closing attribution line, required by the Creative Commons Attribution-ShareAlike 4.0 license, must be preserved in derivative works. The line identifies the original author and the upstream library and is a license requirement, not a stylistic choice.

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
