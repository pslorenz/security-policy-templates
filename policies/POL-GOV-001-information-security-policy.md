# POL-GOV-001: Information Security Policy

| | |
|---|---|
| **Document ID** | POL-GOV-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy establishes the information security program at [ORGANIZATION_NAME]. It states leadership's commitment to protecting the organization's systems, data, and operations, defines who is responsible for the program, and sets the structure that every other security policy operates within.

This is the umbrella document. It does not define specific technical controls; the topic policies listed in Section 3.7 do that. What this policy does is answer the questions that sit above any individual control: why the program exists, who owns it, how decisions about risk get made, how policies are created and maintained, and what happens when a requirement cannot be met.

The goal is a program proportionate to the risks [ORGANIZATION_NAME] actually faces, run consistently, measured honestly, and improved over time. No organization achieves perfect security, and a program that pretends otherwise spends its effort in the wrong places. A modest program that operates every quarter is worth more than an ambitious one that exists only on paper.

## 2. Scope

This policy applies to:

All information owned, processed, stored, or transmitted by [ORGANIZATION_NAME], in any form, including electronic data, paper records, and information held in third-party services. All systems used to handle that information, including company-owned devices, personal devices used for work under POL-IAM-002, cloud services, applications, and network infrastructure. All people who access [ORGANIZATION_NAME] information or systems, including employees, contractors, temporary staff, interns, and vendors with access.

It also applies to service providers who operate systems or handle information on [ORGANIZATION_NAME]'s behalf, through the contractual requirements described in Section 3.9.

Where a topic policy defines a narrower scope for its specific requirements, the topic policy's scope governs those requirements. This policy's scope governs the program as a whole.

## 3. Policy Statements

### 3.1 Leadership Commitment

[ORGANIZATION_NAME] leadership commits to maintaining an information security program that protects the confidentiality, integrity, and availability of the organization's information and systems.

Leadership designates an executive sponsor who is accountable for the program. Leadership provides the budget, staff time, and external support the program needs to meet the requirements in this policy suite. Leadership participates in the program's governance activities, including risk decisions, exception approvals, and periodic program reviews. Leadership follows the same policies as everyone else.

A security program without leadership engagement becomes a set of documents that nobody follows. The commitments in this section exist to prevent that.

### 3.2 Program Objectives

The information security program exists to:

Protect [ORGANIZATION_NAME] information from unauthorized access, disclosure, alteration, and destruction. Keep the systems the business depends on available when they are needed. Meet the legal, regulatory, and contractual obligations that apply to the organization's information. Detect and respond to security incidents in a way that limits damage and restores operations. Give leadership an accurate picture of the organization's security risks so that decisions about those risks are made deliberately.

The program is risk-based. Controls are applied in proportion to the value of what they protect and the likelihood and impact of the threats they address. Requirements that impose cost without reducing meaningful risk are candidates for removal at the next policy review.

### 3.3 Program Governance

The information security program is governed through three mechanisms.

**Executive sponsorship.** The executive sponsor is a member of [ORGANIZATION_NAME] leadership with the authority to approve policies, accept risks, fund remediation, and resolve conflicts between security requirements and business needs. The current executive sponsor is [EXECUTIVE_SPONSOR].

**The Information Security function.** The Information Security function runs the program day to day. At [ORGANIZATION_NAME], this function is performed by [INFORMATION_SECURITY_FUNCTION, e.g., a named internal role, or the designated security service provider]. Where a service provider performs this function, the division of responsibilities between [ORGANIZATION_NAME] and the provider is documented in the service agreement, and the agreement governs where it is more specific than this policy.

**The program review.** The executive sponsor and the Information Security function meet at least quarterly to review the state of the program. The review covers changes in the risk register, open exceptions, incidents and post-incident review findings since the last review, progress on remediation work, metrics described in Section 3.11, and any decisions that need executive input. The review is documented, and decisions made in it are recorded with owners and target dates.

Quarterly is the minimum. Organizations with higher risk exposure or active remediation programs may meet monthly.

### 3.4 Policy Framework and Document Hierarchy

The program is documented through four types of documents, each with a defined purpose and approval level.

**Policies** state what [ORGANIZATION_NAME] commits to doing. They are approved by the executive sponsor, reviewed at least annually, and change infrequently. Policy document IDs use the POL- prefix.

**Standards** define specific, measurable requirements that implement a policy, such as configuration baselines, minimum password lengths, or retention periods. They are approved by the Information Security function, reviewed at least annually, and may change more often than policies as technology changes. Standard document IDs use the STD- prefix.

**Runbooks** describe how to carry out the work a policy requires. They are maintained by the Information Security function and the IT function and updated whenever the procedure changes. Runbook document IDs use the RUN- prefix.

**Templates and records** are the forms, checklists, and logs that produce evidence that controls are operating. They are maintained by the owner of the control they support.

When documents conflict, the higher document governs: this policy over topic policies, policies over standards, and standards over runbooks. A conflict is a defect, and the Information Security function corrects it at the next opportunity rather than waiting for the annual review.

Every policy follows a consistent structure: document control header, purpose, scope, policy statements, roles and responsibilities, enforcement, related documents, framework alignment, and revision history. Consistency makes the suite easier to read, audit, and maintain.

### 3.5 Risk Management

[ORGANIZATION_NAME] manages information security risk through a documented, repeatable process.

**Risk assessment.** The Information Security function conducts a risk assessment at least annually and whenever a significant change occurs, such as a new critical system, a major vendor change, an acquisition, or a significant incident. The assessment identifies the threats most relevant to [ORGANIZATION_NAME], the assets and processes they affect, the existing controls, and the remaining risk.

**The risk register.** Identified risks are recorded in a risk register with a description, an owner, a likelihood and impact rating, the current treatment decision, and a review date. The register is reviewed at each quarterly program review.

**Risk treatment.** Each risk is treated in one of four ways: mitigated through additional controls, transferred through insurance or contract, avoided by changing or stopping the activity, or accepted. Treatment decisions are recorded in the register with the reasoning.

**Risk acceptance.** Only the executive sponsor can accept risks rated High or Critical. The Information Security function can accept risks rated Medium or Low. Every acceptance is documented, names the person who accepted the risk, and carries an expiration date no more than twelve months out. Accepted risks are reviewed at expiration rather than renewed automatically.

**Risk appetite.** The executive sponsor defines [ORGANIZATION_NAME]'s risk appetite: the level of risk the organization is willing to carry in pursuit of its objectives. The appetite statement is documented, reviewed annually, and used to guide treatment decisions. A risk that exceeds the appetite is not accepted at the Information Security function level.

### 3.6 Exceptions

Policy requirements will occasionally conflict with a legitimate business need, a technical limitation, or a transition period. The exception process exists so that these situations are handled openly rather than through quiet non-compliance.

This section defines the exception process for the entire policy suite. Topic policies that refer to an exception process refer to this one.

**Requesting an exception.** The person who needs the exception submits a request to the Information Security function stating the requirement affected, the reason the requirement cannot be met, the systems, data, or people involved, the proposed duration, and any compensating controls that reduce the resulting risk.

**Evaluating the request.** The Information Security function assesses the risk the exception creates. Requests are approved by the Information Security function where the resulting risk is Medium or Low, and by the executive sponsor where the resulting risk is High or Critical. Requests that would create risk beyond the organization's risk appetite are declined or escalated.

**Approved exceptions.** Every approved exception is recorded in an exception register with the requester, the approver, the requirement affected, the compensating controls, and the expiration date. Exceptions expire no later than twelve months after approval. An exception that is still needed at expiration goes through the request process again.

**Emergency exceptions.** Where an immediate business or operational need requires deviating from a policy before an exception can be approved, the deviation is logged at the time it occurs and submitted through the standard process within five business days.

A large or growing exception register is a signal. It usually means a requirement is wrong for the environment, and the requirement should be revised at the next policy review rather than excepted indefinitely.

### 3.7 The Policy Suite

The information security program is implemented through the following topic policies and standards. Each operates under the authority of this policy.

| Document ID | Title | Status |
|---|---|---|
| POL-GOV-001 | Information Security Policy (this document) | Active |
| POL-AUP-001 | Acceptable Use Policy | Active |
| POL-IAM-001 | Access Control Policy | Active |
| POL-IAM-002 | Remote Access Policy | Active |
| POL-IAM-003 | Non-Human Identity Governance Policy | Active |
| STD-IAM-001 | Password and Authentication Standard | Active |
| STD-IAM-002 | Single Sign-On and Federation Standard | Active |
| STD-AM-001 | SaaS Asset Management Standard | Active |
| STD-DC-001 | Data Loss Prevention Standard | Active |
| STD-DC-002 | Cryptography and Key Management Standard | Active |
| STD-DR-001 | Data Backup and Recovery Standard | Active |
| STD-NET-001 | Email and Web Browser Protection Standard | Active |
| STD-VM-001 | Security Testing Standard | Active at tier [TESTING_TIER] |
| STD-OPS-001 | Change Management Standard | Active |
| POL-BC-001 | Business Continuity Policy | Active |
| POL-PPS-001 | Physical and Personnel Security Policy | Active |
| POL-AM-001 | Asset Management Policy | Active |
| POL-DC-001 | Data Classification and Handling Policy | Active |
| POL-IR-001 | Incident Response Policy | Active |
| POL-EP-001 | Endpoint Protection Policy | Active |
| POL-VM-001 | Vulnerability Management Policy | Active |
| POL-NET-001 | Network Security Policy | Active |
| POL-TPRM-001 | Third-Party Risk Management Policy | Active |
| STD-LOG-001 | Logging and Monitoring Standard | Active |
| POL-AI-001 | AI and Agent Governance Policy | Active |
| POL-DEV-001 | Secure Development Policy | Active at the level recorded under POL-DEV-001 Section 2, or Not adopted |

[ORGANIZATION_NAME] adopts the policies in this table that apply to its environment. A policy that does not apply is marked "Not adopted" with a brief reason, so that the omission is visible and deliberate.

### 3.8 Awareness, Acknowledgment, and Training

Policies only work when the people they apply to know what they say.

All personnel acknowledge POL-AUP-001 and this policy at onboarding, before receiving access to [ORGANIZATION_NAME] systems, and annually thereafter. Acknowledgments are recorded with TPL-AUP-001 and retained as records.

All personnel complete security awareness training at onboarding and at least annually. Training covers the threats most relevant to [ORGANIZATION_NAME], how to report suspected incidents, and the personal responsibilities in POL-AUP-001, including how to recognize and report a device that is missing security updates. Personnel with elevated access or security responsibilities receive additional role-specific training.

[ORGANIZATION_NAME] runs simulated phishing exercises at least quarterly. Results are used to target training, not to punish individuals. Someone who clicks a simulated phish and reports it has done the most important part correctly.

### 3.9 Third Parties and Service Providers

Much of [ORGANIZATION_NAME]'s information lives in or passes through systems operated by others. The program extends to those relationships.

[ORGANIZATION_NAME] maintains an inventory of service providers with access to its information or systems, with the data they handle and the access they hold. POL-TPRM-001 governs the rest of the relationship: providers are tiered by risk, assessed before onboarding to the depth their tier requires, held to contract terms in proportion to that tier (security requirements, incident notification, evidence of controls, and data return or destruction at the end of the relationship), and monitored for as long as the relationship lasts.

Where a service provider performs part of the information security program itself, including managed IT or managed security services, the service agreement defines which responsibilities belong to the provider and which remain with [ORGANIZATION_NAME]. Responsibilities not clearly assigned to the provider remain with [ORGANIZATION_NAME]. Accountability for the program stays with [ORGANIZATION_NAME] leadership regardless of what is outsourced.

### 3.10 Legal, Regulatory, and Contractual Obligations

The Information Security function, with legal counsel where appropriate, maintains a list of the legal, regulatory, and contractual security obligations that apply to [ORGANIZATION_NAME]. The list includes applicable data protection and breach notification laws in the jurisdictions where [ORGANIZATION_NAME] operates or holds personal data, sector-specific regulations, security requirements in client contracts, and requirements of the organization's cyber insurance policy.

The current list of applicable obligations is [APPLICABLE_OBLIGATIONS, e.g., state breach notification law, HIPAA, PCI DSS, client contractual requirements, cyber insurance requirements].

This policy suite is aligned to CIS Controls v8.1 and NIST Cybersecurity Framework 2.0. Where an obligation requires controls beyond those frameworks, the additional requirements are documented in the relevant topic policy or in a supplemental standard. Alignment to a framework is not the same as compliance with a regulation, and the program does not claim otherwise.

### 3.11 Measurement and Reporting

The program is measured so that leadership can see whether it is working.

The Information Security function reports to the executive sponsor at each quarterly program review on a defined set of metrics. The metrics are chosen for [ORGANIZATION_NAME]'s environment and typically include: multi-factor authentication coverage across user and administrative accounts, patch compliance for critical vulnerabilities within the timelines in the vulnerability management policy, endpoint protection coverage, completion rates for awareness training and acknowledgments, phishing simulation report rates, the number and age of open exceptions and accepted risks, incidents by severity, and progress on remediation items from risk assessments and post-incident reviews.

Metrics are reported honestly, including when they are unfavorable. A metric that always looks good is either measuring the wrong thing or being measured wrong.

At least annually, the executive sponsor and the Information Security function conduct a full program review assessing whether the program's scope, objectives, and resourcing still fit [ORGANIZATION_NAME]'s risks, and documenting the program priorities for the coming year.

### 3.12 Policy Review and Maintenance

Every policy in the suite is reviewed at least annually by its owner. Reviews also occur when a significant change affects the policy, such as a new regulation, a significant incident, a major technology change, or a finding from an audit or assessment.

A review results in one of three outcomes: the policy is reaffirmed without change, the policy is revised, or the policy is retired. Each outcome is recorded in the policy's revision history. Revisions to policies are approved by the executive sponsor; revisions to standards and runbooks are approved by the Information Security function.

Material changes to policies are communicated to the personnel they affect before taking effect.

## 4. Roles and Responsibilities

**Executive sponsor.** Accountable for the information security program. Approves policies. Defines the risk appetite. Accepts High and Critical risks and approves exceptions at those levels. Provides resources for the program. Chairs the quarterly program review and the annual program review.

**Information Security function (or designated security service provider).** Owns this policy. Runs the program day to day. Maintains the policy suite, the risk register, and the exception register. Conducts risk assessments. Accepts Medium and Low risks and approves exceptions at those levels. Reports program metrics. Coordinates with service providers and legal counsel.

**IT function (or IT service provider).** Implements and operates the technical controls the policy suite requires. Produces the evidence that those controls are operating. Identifies technical limitations that may require exceptions and raises them through the exception process.

**Policy owners.** Maintain their assigned policies, conduct annual reviews, and propose revisions. Each policy names its owner in the document control header.

**Department leads and managers.** Ensure their teams complete acknowledgments and training. Identify business processes and systems that create security risk and bring them to the Information Security function. Request exceptions through the documented process rather than permitting informal deviations.

**Legal counsel.** Advises on legal, regulatory, and contractual obligations. Reviews contract security terms for service providers that handle sensitive data. Advises during incidents as described in POL-IR-001.

**All personnel.** Read and acknowledge the policies that apply to them. Complete required training. Protect the information and systems they use. Report suspected incidents and policy violations through the channels in POL-AUP-001.

## 5. Enforcement

Violations of this policy or any policy in the suite may result in disciplinary action consistent with HR policies, up to and including termination of employment or contract. Violations by service providers are addressed through the terms of the service agreement.

The program favors correction over punishment for honest mistakes. Someone who reports their own error promptly, such as a misdirected email or a clicked phishing link, is treated as having helped the program. Disciplinary action is reserved for deliberate violations, repeated violations after coaching, concealment, and negligence that causes significant harm.

Leadership is not exempt. A violation by a senior leader is handled through the same process as any other violation, with escalation to the executive sponsor or, where the executive sponsor is involved, to [ORGANIZATION_GOVERNANCE_BODY, e.g., ownership or board].

## 6. Related Documents

All policies and standards listed in Section 3.7.
RUN-IR-001: Incident Response Runbook
POL-TPRM-001: Third-Party Risk Management Policy (vendor tiering, diligence, contracts, and monitoring)
TPL-GOV-001: Risk Register
TPL-GOV-002: Exception Register
TPL-GOV-003: Vendor Inventory and Risk Assessment
TPL-GOV-004: Quarterly Program Metrics Report

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

GV.OC-01 (The organizational mission is understood and informs cybersecurity risk management). GV.OC-03 (Legal, regulatory, and contractual requirements regarding cybersecurity are understood and managed). GV.RM-01 (Risk management objectives are established and agreed to by organizational stakeholders). GV.RM-02 (Risk appetite and risk tolerance statements are established, communicated, and maintained). GV.RM-04 (Strategic direction that describes appropriate risk response options is established and communicated). GV.RM-06 (A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated). GV.RR-01 (Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving). GV.RR-02 (Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced). GV.RR-03 (Adequate resources are allocated commensurate with the cybersecurity risk strategy, roles, responsibilities, and policies). GV.RR-04 (Cybersecurity is included in human resources practices). GV.PO-01 (Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced). GV.PO-02 (Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission). GV.OV-01 (Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction). GV.OV-03 (Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed). GV.SC-01 (A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders). GV.SC-04 (Suppliers are known and prioritized by criticality). GV.SC-05 (Requirements to address cybersecurity risks in supply chains are established, prioritized, and integrated into contracts and other types of agreements with suppliers and other relevant third parties). GV.SC-07 (The risks posed by a supplier, their products and services, and other third parties are understood, recorded, prioritized, assessed, responded to, and monitored over the course of the relationship). GV.SC-10 (Cybersecurity supply chain risk management plans include provisions for activities that occur after the conclusion of a partnership or service agreement). ID.RA-03 (Internal and external threats to the organization are identified and recorded). ID.RA-04 (Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded). ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization). ID.RA-06 (Risk responses are chosen, prioritized, planned, tracked, and communicated). ID.RA-07 (Changes and exceptions are managed, assessed for risk impact, recorded, and tracked). ID.RA-10 (Critical suppliers are assessed prior to acquisition). ID.IM-01 (Improvements are identified from evaluations). PR.AT-01 (Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind). PR.AT-02 (Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind).

**CIS Controls v8.1:**

CIS Controls v8.1 tags safeguards with a Govern security function to align with NIST CSF 2.0, but it has no dedicated governance control. This policy establishes the program structure that the CIS-aligned topic policies operate within, and directly supports: Safeguard 14.1 (establish and maintain a security awareness program), Safeguard 15.1 (establish and maintain an inventory of service providers), Safeguard 15.2 (establish and maintain a service provider management policy), and Safeguard 15.4 (ensure service provider contracts include security requirements).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
