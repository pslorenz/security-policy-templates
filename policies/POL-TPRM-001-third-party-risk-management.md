# POL-TPRM-001: Third-Party Risk Management Policy

| | |
|---|---|
| **Document ID** | POL-TPRM-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] manages the security risks introduced by third-party vendors, suppliers, contractors, and other parties that have access to company data or systems. It covers what [ORGANIZATION_NAME] expects of vendors, how vendor relationships are evaluated, and how risks from those relationships are addressed.

The reason third-party risk matters is straightforward. Many of the most damaging security incidents at organizations of all sizes start with a third party rather than with the organization itself. A compromised SaaS vendor exposes the data the organization stored there. A breached service provider gives attackers a path into the customer's environment. A vendor that uses AI tools without disclosure exposes customer data to those tools. The blast radius of a third-party incident often extends well beyond what either party anticipated when the relationship began.

This policy does not pretend that [ORGANIZATION_NAME] can perfectly assess or control every third-party relationship. Realistic third-party risk management at organizations of [ORGANIZATION_NAME]'s scale is about doing the right amount of diligence on the right vendors, building reasonable contractual protections, and having a process that catches the situations that matter most.

This policy works alongside POL-AM-001 (Asset Management Policy), which tracks the SaaS and cloud subscriptions [ORGANIZATION_NAME] uses, and POL-DC-001 (Data Classification and Handling Policy), which establishes the data sharing rules this policy enforces.

## 2. Scope

This policy applies to relationships with any third party that has access to [ORGANIZATION_NAME] data, systems, or operations. Specifically:

SaaS providers and cloud platforms that store or process [ORGANIZATION_NAME] data. Managed service providers, including IT service providers, security service providers, and managed detection and response services. Vendors providing operational services that involve access to company systems (payroll providers, benefits administrators, accounting and tax providers, audit firms). Contractors and consultants with access to systems or sensitive data. Software vendors whose products run inside [ORGANIZATION_NAME] environments. Vendors that act as data processors or sub-processors for personal data subject to privacy regulations.

It applies to ongoing relationships with these parties as well as to one-time engagements that involve access to company data.

The policy does not address customer relationships, which involve a different set of considerations. It does not cover relationships where [ORGANIZATION_NAME] is the third party providing services to others, which is governed by [ORGANIZATION_NAME]'s own contractual obligations rather than this policy.

## 3. Policy Statements

### 3.1 Vendors Are Tiered by Risk

Not every vendor relationship carries the same risk. Trying to apply the same diligence to every vendor is impractical and dilutes attention from the vendors that matter. [ORGANIZATION_NAME] tiers vendors based on the risk they pose, and the diligence applied to each vendor matches the tier.

**Tier 1 vendors** are those whose compromise or failure would cause significant harm to [ORGANIZATION_NAME] or its stakeholders. Examples include the primary identity provider, the primary file storage platform, vendors holding Restricted data per POL-DC-001, vendors providing critical operational services (payroll, benefits, banking), the primary IT or security service provider, and vendors with privileged access to production systems.

**Tier 2 vendors** are those whose compromise would cause meaningful but contained harm. Examples include departmental SaaS tools holding Confidential data, marketing and sales tools holding customer contact information, vendors providing non-critical operational services, and consultants with access limited to specific projects.

**Tier 3 vendors** are those whose compromise would cause limited harm. Examples include tools holding only Public data, vendors providing services that do not involve company data access, and short-engagement contractors with limited access.

The tier is assigned at the start of the relationship and reviewed annually. A vendor's tier can increase or decrease as the relationship evolves. A vendor who was Tier 3 when [ORGANIZATION_NAME] started using their tool may become Tier 2 or Tier 1 as the relationship grows in scope.

### 3.2 Due Diligence Before the Relationship Begins

Before [ORGANIZATION_NAME] enters a relationship with a new vendor, the vendor is evaluated for security risk appropriate to their tier.

**Tier 1 vendor due diligence** includes:

A security questionnaire covering the vendor's security program, controls, certifications, and incident history. Standard questionnaires (SIG, CAIQ) are appropriate; many vendors maintain their answers in a public or gated trust portal that satisfies this need. A review of the vendor's third-party security audits or certifications (SOC 2 Type II report, ISO 27001 certification, or equivalent attestation appropriate to the vendor's services). Evidence that the vendor handles data per the requirements of POL-DC-001 for the classification of data they will hold. Evidence that the vendor has incident response and notification capabilities. A review of the vendor's known breach history, if any, and how the vendor responded.

**Tier 2 vendor due diligence** is lighter:

A review of the vendor's published security information (security page, trust portal, recent SOC 2 or equivalent if available). Confirmation of basic security practices through the vendor's published materials or a brief targeted questionnaire. Evidence of incident notification capabilities.

**Tier 3 vendor due diligence** is minimal:

A review of the vendor's published information for any obvious red flags. Confirmation that the vendor is established and reputable in their space.

The due diligence is documented and retained with the vendor's records. The documentation supports later analysis and provides a reference point if the relationship changes scope.

### 3.3 Contractual Protections

[ORGANIZATION_NAME] negotiates contractual protections appropriate to each vendor's tier. The protections are targets that are not always achievable, and deviations are documented.

**Tier 1 vendor contracts include:**

Specific security requirements, including the controls expected and the consequences of failure to maintain them. Data handling requirements, including the data classifications the vendor may receive and the rules for handling each. Incident notification requirements, with timelines that allow [ORGANIZATION_NAME] to meet its own regulatory and contractual obligations. Audit rights or, where audit rights are not practical, the right to receive third-party audit reports on a defined cadence. Termination rights, including the right to terminate for breach of security obligations and the procedures for data return or destruction at termination. Liability provisions appropriate to the data and services involved. Sub-processor and AI usage disclosure requirements where applicable.

**Tier 2 vendor contracts include:**

Standard security and data handling expectations. Incident notification requirements. Termination rights and data handling at termination. Reasonable liability provisions.

**Tier 3 vendor contracts include:**

Standard terms appropriate to the engagement. Specific security provisions are not always required for vendors at this tier.

For SaaS vendors that use click-through terms rather than negotiated contracts, [ORGANIZATION_NAME] reviews the published terms before commitment. Where the published terms are inadequate for the data the vendor will receive, the relationship is reconsidered.

### 3.4 Data Sharing Controls

When [ORGANIZATION_NAME] shares data with a vendor, the sharing follows the rules established in POL-DC-001 for the data classification involved.

Specific requirements:

Restricted data is shared with vendors only when there is a documented business reason, the vendor has been validated as appropriate for the data classification, and the contractual protections meet the requirements of Section 3.3.

Confidential data shared with Tier 1 or Tier 2 vendors is appropriate when the vendor's handling matches POL-DC-001 expectations.

The minimum necessary data is shared. Vendors do not receive data they do not need to perform their service.

Where data transfer is involved, the transfer uses appropriate encryption and authenticated channels. Bulk data transfers are documented and approved before they occur.

For ongoing data flows (vendor integration with company systems, regular data feeds, automated synchronization), the flow is documented in the asset inventory per POL-AM-001 and reviewed annually.

### 3.5 Vendor Access to [ORGANIZATION_NAME] Systems

When a vendor needs direct access to [ORGANIZATION_NAME] systems, the access is provisioned and managed consistent with POL-IAM-001 (Access Control Policy).

Specific requirements:

Vendor access is granted to specific named individuals at the vendor, not to a generic vendor account. POL-IAM-001 Section 3.1's requirement for individual accounts applies to vendor access.

Vendor access has an explicit end date set at provisioning. The end date matches the engagement duration. Ongoing engagements are reviewed annually.

Vendor access uses authentication consistent with STD-IAM-001. Vendors with privileged access use phishing-resistant authentication.

Vendor administrative access is treated as privileged access per POL-IAM-001 Section 3.5, including the requirements for separate administrative accounts and just-in-time elevation where the platform supports it.

When the engagement ends, vendor access is removed promptly per POL-IAM-001 Section 3.4. The removal is verified.

### 3.6 AI Usage by Vendors

Vendors that use AI tools to process [ORGANIZATION_NAME] data introduce a specific category of risk. The vendor's use of AI may involve sending data to AI service providers, may involve training models on the data, or may involve other handling that the original vendor relationship did not anticipate.

For new vendor relationships and at contract renewal for existing relationships, the diligence asks specifically:

Does the vendor use AI tools to process data the vendor receives from customers? Which AI service providers does the vendor use? Are these providers approved for the data classifications involved?

Is customer data used to train AI models, either the vendor's own or third-party models? Most reputable vendors say no; the question still gets asked.

What logging and oversight does the vendor maintain over AI processing of customer data? Where AI is used, what happens if a customer requests data deletion?

Vendors that use AI in ways that conflict with [ORGANIZATION_NAME]'s data handling expectations or that cannot answer these questions clearly are reconsidered. The reconsideration may be a contract amendment, a change in what data is shared, or termination of the relationship.

This section will expand as AI governance practice matures.

### 3.7 Sub-Processors and Fourth Parties

The vendors [ORGANIZATION_NAME] engages have their own vendors. These sub-processors or fourth parties may handle [ORGANIZATION_NAME] data even though [ORGANIZATION_NAME] has no direct relationship with them.

For Tier 1 vendors, [ORGANIZATION_NAME] expects:

Disclosure of critical sub-processors who handle [ORGANIZATION_NAME] data. Notification of changes to the sub-processor list. Contractual flow-down of security and data handling expectations to sub-processors.

For Tier 2 vendors, the expectation is general transparency about sub-processors when asked, without a formal disclosure obligation.

For Tier 3 vendors, sub-processor questions are not typically pursued.

The realistic scope of fourth-party management at [ORGANIZATION_NAME]'s scale is awareness rather than active control. The organization cannot audit every sub-processor of every vendor. What it can do is concentrate diligence on the relationships that matter most and accept the residual risk for the rest.

### 3.8 Ongoing Monitoring

Vendor relationships are monitored throughout their duration, not just at the start.

For Tier 1 vendors:

The vendor's published security information is reviewed annually for material changes. Updated SOC 2 reports or equivalent are reviewed when issued. Public breach disclosures or credible reports of vendor security incidents trigger immediate review and decision about the relationship. Contract renewals trigger refreshed due diligence.

For Tier 2 vendors:

Public breach disclosures or credible reports trigger review. Contract renewals trigger refreshed lighter diligence.

For Tier 3 vendors:

Material changes that would cause the vendor to be re-tiered (a change in scope, a significant breach, a change in services) trigger review.

[ORGANIZATION_NAME] uses third-party monitoring services where appropriate to receive notifications about vendor security events. Approved services are [APPROVED_VENDOR_MONITORING, e.g., a security ratings or vendor breach monitoring service where the value justifies the cost; smaller environments may rely on news monitoring and direct vendor communication].

### 3.9 Vendor Incident Coordination

When a vendor experiences a security incident affecting [ORGANIZATION_NAME] data or services, [ORGANIZATION_NAME] coordinates the response.

The coordination:

The vendor's incident notification is received and triaged through the security operations process. If the vendor incident affects [ORGANIZATION_NAME] data or systems, the situation is treated as an incident under POL-IR-001, with the vendor as the source of the incident rather than the response responsible party. The relevant terms of the vendor contract are applied. Investigation, communication, and remediation are coordinated with the vendor. The vendor relationship is reviewed after the incident, with consideration of whether the relationship should continue and on what terms.

For Tier 1 vendors, the incident may rise to the level requiring executive sponsor involvement. For Tier 2 and Tier 3 vendors, the response is typically handled by the Information Security function with executive notification at the standard cadence for the incident severity.

### 3.10 Termination and Offboarding

When a vendor relationship ends, the offboarding process protects [ORGANIZATION_NAME] data.

Offboarding includes:

Vendor access to [ORGANIZATION_NAME] systems is removed promptly. Vendor accounts and credentials are deactivated. Data held by the vendor is returned or destroyed per the contractual terms. The destruction or return is confirmed. Integration paths between the vendor's systems and [ORGANIZATION_NAME] systems are removed. The vendor is removed from the active vendor inventory and from any access lists, group memberships, or technical configurations referencing them. The relationship outcome is documented for future reference.

For Tier 1 vendors, the offboarding includes confirmation of data destruction or return through documented attestation.

### 3.11 Exceptions

Specific situations may require deviation from the standard process:

A vendor relationship that begins on an emergency basis may not have time for full diligence before commitment. The exception documents the situation and the diligence completed retroactively within thirty days.

A vendor with established trust through long relationship may have lighter diligence than their tier would otherwise require. The exception documents the basis for the deviation.

A vendor relationship that does not fit cleanly into the tier model (a vendor providing services where the data sensitivity is unusual, or a vendor whose role evolves over the relationship). The exception documents the specific situation.

Exceptions follow the process in POL-IAM-001 Section 3.10. No exception runs longer than twelve months without renewal. All active exceptions are reviewed quarterly.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Performs or coordinates vendor due diligence. Reviews contracts for security and data handling provisions. Coordinates response to vendor incidents. Maintains the vendor risk records.

**Procurement function (or whoever approves vendor purchases).** Ensures that proposed vendors go through the appropriate due diligence before commitment. Negotiates the contractual protections appropriate to the vendor's tier. Maintains the active vendor list.

**Legal counsel.** Reviews contracts with significant security or data handling implications. Advises on liability and notification provisions. Reviews vendor incident situations involving regulatory or litigation exposure.

**Vendor relationship owners.** Each vendor relationship has a named owner inside [ORGANIZATION_NAME]. The owner is the business sponsor of the vendor's services. The owner participates in due diligence, monitors the vendor relationship, and signals when changes warrant re-tiering or re-evaluation.

**Executive sponsor.** Reviews Tier 1 vendor relationships annually. Approves significant changes to the third-party risk program. Receives notification of material vendor incidents.

**All employees and contractors.** Use only approved vendors for company work. Do not commit [ORGANIZATION_NAME] to vendor relationships without going through the approved process. Report observed vendor security issues or unusual vendor behavior.

## 5. Enforcement

Violations of this policy may result in restrictions on vendor commitment authority, escalation to the responsible owner, and disciplinary action consistent with HR policies.

Specific situations:

Tier 1 vendors engaged without due diligence: due diligence completed retroactively within thirty days, with the executive sponsor notified.

Vendor access provisioned without going through the approved process: investigated and either authorized through retroactive review or removed within thirty days.

Vendor contract renewals without refreshed diligence at the appropriate tier: completed within sixty days, with the relationship in review pending completion.

Vendor incidents not escalated through the documented process: reviewed for cause and addressed through training or process improvement.

## 6. Related Documents

POL-IAM-001: Access Control Policy (vendor access provisioning)
STD-IAM-001: Password and Authentication Standard (vendor authentication requirements)
POL-AM-001: Asset Management Policy (vendor inventory and ongoing tracking)
POL-DC-001: Data Classification and Handling Policy (data sharing controls)
POL-IR-001: Incident Response Policy (vendor incident response)
POL-AI-001: AI and Agent Governance Policy (approval criteria for AI tools)
POL-AUP-001: Acceptable Use Policy (employee responsibilities for vendor relationships)
[CONTRACT_REVIEW_PROCESS]: The organization's standard contract review process
STD-LOG-001: Logging and Monitoring Standard

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

GV.SC-01 (A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders). GV.SC-02 (Cybersecurity roles and responsibilities for suppliers, customers, and partners are established). GV.SC-03 (Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management programs). GV.SC-04 (Suppliers are known and prioritized by criticality). GV.SC-05 (Requirements to address cybersecurity risks in supply chains are established). GV.SC-06 (Planning and due diligence are performed to reduce risks before entering into formal supplier or other third-party relationships). GV.SC-07 (The risks posed by suppliers, their products, and their services are understood, recorded, prioritized, assessed, responded to, and monitored). GV.SC-08 (Relevant suppliers and other third parties are included in incident planning, response, and recovery activities). GV.SC-09 (Supply chain security practices are integrated into cybersecurity and enterprise risk management programs). GV.SC-10 (Cybersecurity supply chain risk management plans include provisions for activities that occur after the conclusion of a partnership or service agreement).

**CIS Controls v8.1:**

Control 15 Service Provider Management: Safeguards 15.1 (establish and maintain an inventory of service providers), 15.2 (establish and maintain a service provider management policy), 15.3 (classify service providers), 15.4 (ensure service provider contracts include security requirements), 15.5 (assess service providers), 15.6 (monitor service providers), 15.7 (securely decommission service providers).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
