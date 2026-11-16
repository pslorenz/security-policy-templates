# POL-AI-001: AI and Agent Governance Policy

| | |
|---|---|
| **Document ID** | POL-AI-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Semiannual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] approves, connects, and oversees artificial intelligence tools, including AI features built into software the organization already uses and AI agents that take actions on someone's behalf.

AI tools are useful, and people will use them whether or not a policy exists. The risk sits in three places. Data goes into tools that keep it, train on it, or share it. Tools are connected to mailboxes, files, and business systems with access nobody reviewed. Agents act on instructions that came from an email or a web page rather than from the person who owns the agent. This policy addresses each of those directly.

POL-AUP-001 Section 3.6 tells users the basic rules for using AI tools. This policy is the governance behind those rules: what gets approved, how connections are controlled, what agents may do on their own, and who is accountable. The review cycle is semiannual because the tools change faster than an annual review can follow.

## 2. Scope

This policy covers every AI capability that touches [ORGANIZATION_NAME] data, systems, or work, including:

Standalone AI assistants and chat tools. AI features built into the productivity platform, line-of-business applications, and SaaS tools already in use, including features a vendor turns on by default. Coding assistants and AI features in development tools. AI meeting assistants, note-takers, and transcription services. Browser extensions and desktop applications with AI features. AI agents and automated workflows that use a model to decide what to do next. Connectors, plugins, and Model Context Protocol (MCP) servers that give an AI tool access to company systems. AI capabilities that [ORGANIZATION_NAME] builds into its own systems or products using a model provider's API.

It applies to employees, contractors, and vendors using AI on [ORGANIZATION_NAME]'s behalf, and to AI tools used on personal devices or personal accounts when company data or company work is involved.

## 3. Policy Statements

### 3.1 Data Classification Decides What AI Can Touch

The question for any AI use is what data goes in and where it ends up. The data classification in POL-DC-001 answers it.

**Public data** may be used with any AI tool, including consumer tools.

**Confidential data** may be used only with AI tools approved under Section 3.2.

**Restricted data** may be used only with AI tools that the Information Security function has approved specifically for the Restricted data category involved. Authentication credentials, encryption keys, and recovery codes are never entered into any AI tool.

Data entered into an AI tool is treated as stored in that tool, consistent with POL-DC-001 Section 3.9. Outputs inherit the classification of the inputs: a summary of a Confidential document is Confidential.

### 3.2 AI Tools Are Approved Before Company Data Goes In

[ORGANIZATION_NAME] maintains a list of approved AI tools and the data classifications each is approved for. Approved AI tools are [APPROVED_AI_TOOLS, e.g., business or enterprise tiers of AI assistants covered by a data protection agreement, and AI features of the approved productivity platform].

A tool is approved only when the review under POL-TPRM-001 Section 3.6 confirms:

A business agreement covers the tool, rather than consumer terms. The vendor does not use [ORGANIZATION_NAME] data to train or improve models, and the agreement says so. Retention of prompts, files, and outputs is defined and can be limited. Administrators can manage access, ideally through single sign-on under STD-IAM-002, and can see usage or audit records. The vendor discloses the model providers and sub-processors that handle the data.

A consumer or free tier of a tool is a different product from the business tier, even when it comes from the same vendor, and is not approved for company data.

Users request new AI tools through [AI_TOOL_REQUEST_CHANNEL, e.g., the standard software request process]. Most requests for tools that meet the criteria above are approved quickly. The purpose of the process is to know what is in use, not to discourage use.

**AI features in existing software.** When a vendor adds or enables an AI feature in a tool [ORGANIZATION_NAME] already uses, the feature is reviewed before it is used with Confidential or Restricted data. The review asks the same questions as a new tool. Where the platform lets administrators turn an AI feature off until it is reviewed, it is turned off.

### 3.3 Connecting AI to Company Systems Creates a Non-Human Identity

An AI tool that can read a mailbox, open files, query a database, or post to a chat channel is using an identity to do it. Every connector, plugin, OAuth grant, API key, or MCP server that gives an AI tool access to [ORGANIZATION_NAME] systems is a non-human identity under POL-IAM-003 and follows that policy: a named owner, a documented purpose, least privilege, credentials in the secrets vault, and quarterly review.

Specific rules:

Users do not connect AI tools, browser extensions, or agents to company accounts on their own authority. The identity provider is configured so that consent to third-party applications requires administrator approval, and connections go through the provisioning process in POL-IAM-003 Section 3.7.

Connections are scoped to the specific mailboxes, sites, folders, or records the use case needs. An assistant that summarizes one shared mailbox does not get read access to every mailbox in the tenant.

Delegated access, where the tool acts as the signed-in user and can reach only what that user can reach, is preferred over application access, where the tool acts on its own across the tenant.

MCP servers and similar connectors are approved individually. A connector from an unknown publisher, or one that runs code locally with the user's full permissions, is treated as software installation under POL-AUP-001 Section 3.8 as well as a non-human identity.

### 3.4 What Agents May Do on Their Own

An AI agent is an AI tool that takes actions, not just one that produces text. This policy sorts agents into three levels by how much they do without a person approving each action.

**Assistive.** The agent drafts, summarizes, or recommends, and a person takes every action. A drafted email that a person reviews and sends is assistive. Assistive use is permitted with any approved tool.

**Supervised.** The agent takes actions, but a person approves each consequential action before it happens. Supervised agents are permitted for approved use cases with a named owner.

**Autonomous.** The agent takes actions without per-action approval. Autonomous agents are permitted only for use cases the Information Security function has approved in writing, with a named owner, a dedicated identity scoped to the task, logging of every action, and a documented way to stop the agent immediately.

Whatever its level, no agent takes these actions without a person approving each one: sending money or changing payment details; sending external communications to recipients the agent has not been approved to contact; granting, changing, or removing access permissions; deleting data or disabling security controls; and signing, accepting, or agreeing to anything on [ORGANIZATION_NAME]'s behalf.

**Untrusted content.** Agents that read untrusted content (inbound email, web pages, shared documents, tickets submitted by outsiders) can be steered by instructions hidden in that content. This is called prompt injection, and no current model reliably prevents it. An agent that reads untrusted content, has access to Confidential or Restricted data, and can send information outside the organization has every ingredient for data theft. Agents are not given all three at once without human approval of outbound actions. Where a use case needs all three, the outbound step is supervised. The OWASP Top 10 for Large Language Model Applications lists prompt injection and excessive agency (an agent given more functionality, permissions, or autonomy than its task needs) among the leading risks for these systems; the levels and limits in this section are the controls for both.

### 3.5 Meeting Assistants and Recordings

AI meeting assistants record, transcribe, and summarize conversations, which makes them a data collection tool as well as a productivity tool.

Only approved meeting assistants join [ORGANIZATION_NAME] meetings. Participants are told at the start of the meeting when a recording or AI assistant is active. Some jurisdictions require consent from every party before a conversation is recorded; meetings with participants in those jurisdictions follow the stricter rule.

Meetings with clients, candidates, or other external parties use a meeting assistant only with the host's approval and notice to the external participants. Where a client contract restricts recording or AI processing, the contract governs.

Transcripts and summaries are Confidential by default and are retained for [MEETING_RECORD_RETENTION, e.g., ninety days] unless a business or legal need requires longer. Meeting assistants that external participants bring are not admitted to meetings where Confidential or Restricted information will be discussed.

### 3.6 People Stay Accountable for AI Output

The person who uses an AI tool is accountable for what they do with its output. AI output can be wrong, invented, or out of date, and it is reviewed before it is relied on, sent, or published.

Decisions with significant effects on individuals (hiring, firing, promotion, compensation, credit, discipline, access to services) are not made by an AI tool alone. A person makes the decision and can explain the basis for it.

AI-generated code is reviewed for security, correctness, and license compliance the same way as code written by hand, and passes the same tests before it reaches production.

### 3.7 Disclosure and Impersonation

[ORGANIZATION_NAME] discloses the use of AI in work delivered to clients when a contract requires it, when a client asks, or when the client would reasonably expect the work to be produced by a person.

AI tools are not used to impersonate a real person, to create synthetic audio, video, or images of a real person without their consent, or to present AI output as a person's statement in a context where authenticity matters.

Voice and video can now be convincingly faked. Requests to move money, change payment details, share credentials, or bypass a process are verified through a separate, known channel even when they arrive by voice or video from someone who looks and sounds right. RUN-IR-001 Section 3.2.3 covers the response when that verification fails.

### 3.8 Building AI Into [ORGANIZATION_NAME] Systems

When [ORGANIZATION_NAME] builds AI capabilities into its own systems, workflows, or products using a model provider's API:

The model provider goes through vendor review under POL-TPRM-001 as a Tier 1 or Tier 2 vendor, depending on the data involved. API keys are non-human identity credentials under POL-IAM-003 and live in the secrets vault. Prompts and outputs that contain Confidential or Restricted data are logged and retained under STD-LOG-001 only where the log store is approved for that classification. Systems that pass untrusted input to a model are designed on the assumption that the model can be manipulated, with the controls in Section 3.4 applied to whatever the system can do. The system is tested before it handles production data, and again after significant changes to the prompts, model, or connected tools. The test basis is the current OWASP Top 10 for Large Language Model Applications, with prompt injection, sensitive information disclosure, improper output handling, and excessive agency treated as the minimum scope for any system that accepts untrusted input or can take actions.

Organizations that develop software also follow POL-DEV-001 for AI features.

### 3.9 AI Inventory and Review

The Information Security function maintains an inventory of AI in use at [ORGANIZATION_NAME], using TPL-AI-001: approved AI tools and the classifications each is approved for, AI features enabled in existing software, connectors and integrations, agents with their level under Section 3.4 and their owners, and AI capabilities built in-house.

The inventory is reconciled quarterly. Connectors and agent identities are reviewed as part of the non-human identity review in POL-IAM-003 Section 3.9. Shadow AI discovered through consent logs, network or endpoint visibility, or expense records is brought into the approval process or removed, following the approach for unsanctioned applications in STD-IAM-002 Section 3.8.

### 3.10 AI-Related Incidents

These events are reported and handled under POL-IR-001:

Confidential or Restricted data entered into an unapproved AI tool. An agent taking an action outside its approved scope, or an action nobody can explain. Evidence of prompt injection against an agent or an in-house AI system. A connector or AI tool requesting or using access beyond what was approved. A deepfake or AI-assisted impersonation attempt against [ORGANIZATION_NAME] staff, clients, or vendors. A vendor's notification of an incident involving an AI service that processed [ORGANIZATION_NAME] data.

The first containment step for a misbehaving agent or connector is to revoke its access at the identity provider, using the non-human identity response in POL-IR-001 and the standing authority matrix. Users who report that they put data into the wrong tool are treated under the good-faith reporting provision in POL-AUP-001 Section 3.9.

### 3.11 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6. The restrictions in Section 3.4 on actions requiring human approval are not subject to exception for autonomous agents; a use case that needs one of those actions runs as a supervised agent instead.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Reviews and approves AI tools, connectors, and autonomous agent use cases. Maintains the AI inventory. Monitors consent and connection activity. Investigates AI-related incidents.

**IT function (or IT service provider).** Configures administrator consent requirements, single sign-on, and administrative controls for approved AI tools. Provisions and removes connector and agent identities. Turns off unreviewed AI features where the platform allows.

**Procurement function (or whoever approves software purchases).** Routes AI tool purchases and AI-related contract changes through the review in Section 3.2.

**Legal counsel.** Advises on recording consent, client contract restrictions, disclosure obligations, and regulatory requirements that apply to AI use.

**Agent and connector owners.** Serve as the named owner under POL-IAM-003. Confirm the use case, the level under Section 3.4, and the access each quarter. Stop the agent when it behaves unexpectedly.

**Managers.** Make sure their teams know which AI tools are approved. Route requests for new tools through the process.

**All users.** Use only approved AI tools with company data. Do not connect AI tools to company accounts outside the approved process. Review AI output before relying on it. Report AI-related incidents promptly.

## 5. Enforcement

Violations of this policy may result in loss of access to AI tools, removal of unapproved connections, escalation to the user's manager, and disciplinary action consistent with [ORGANIZATION_NAME]'s human resources policies. Honest mistakes reported promptly are handled as learning opportunities, not violations.

Specific remediation timelines:

Unapproved AI tool connected to company accounts: access revoked within one business day of discovery; the tool may then be submitted for approval. Confidential or Restricted data in an unapproved AI tool: reported under POL-IR-001 and deletion requested from the vendor where possible. AI feature enabled in existing software without review: turned off or reviewed within thirty days. Autonomous agent operating without written approval: stopped immediately and moved to supervised operation or approved within thirty days. Connector with broader access than approved: scoped down within seven days.

## 6. Related Documents

POL-GOV-001: Information Security Policy (exception process and program governance)
POL-AUP-001: Acceptable Use Policy (user-facing rules for AI use, Section 3.6)
POL-DC-001: Data Classification and Handling Policy (classification that governs AI inputs)
POL-IAM-003: Non-Human Identity Governance Policy (connector and agent identities)
STD-IAM-002: Single Sign-On and Federation Standard (SSO for AI tools, shadow application discovery)
POL-TPRM-001: Third-Party Risk Management Policy (AI vendor diligence, Section 3.6)
POL-IR-001: Incident Response Policy (AI-related incidents)
RUN-IR-001: Incident Response Runbook (impersonation and BEC response)
STD-LOG-001: Logging and Monitoring Standard (logging for agent actions and AI systems)
TPL-AI-001: AI Tool and Agent Inventory (the inventory and quarterly reconciliation in Section 3.9)
POL-DEV-001: Secure Development Policy (where applicable)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

GV.PO-01 (Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced). GV.SC-07 (The risks posed by a supplier, their products and services, and other third parties are understood, recorded, prioritized, assessed, responded to, and monitored over the course of the relationship). ID.AM-02 (Inventories of software, services, and systems managed by the organization are maintained). PR.AA-05 (Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties). PR.DS-01 (The confidentiality, integrity, and availability of data-at-rest are protected). PR.DS-10 (The confidentiality, integrity, and availability of data-in-use are protected). DE.CM-03 (Personnel activity and technology usage are monitored to find potentially adverse events).

**CIS Controls v8.1:**

Control 2 Inventory and Control of Software Assets: Safeguards 2.1 (establish and maintain a software inventory) and 2.3 (address unauthorized software), through Sections 3.2 and 3.9.

Control 3 Data Protection: Safeguard 3.3 (configure data access control lists), through the scoping rules in Section 3.3.

Control 5 Account Management: Safeguard 5.5 (establish and maintain an inventory of service accounts), through Section 3.3 and POL-IAM-003.

Control 15 Service Provider Management: Safeguards 15.1 (establish and maintain an inventory of service providers) and 15.4 (ensure service provider contracts include security requirements), through Section 3.2.

**CIS Controls AI Companion Guides:**

CIS has published companion guides that apply CIS Controls v8.1 to three layers of AI systems. This policy aligns to each as follows. The LLM Companion Guide (prompts, context handling, and sensitive data exposure) corresponds to Sections 3.1 and 3.8. The AI Agent Companion Guide (safe tool execution, governed autonomy, and access to enterprise systems) corresponds to Section 3.4. The MCP Companion Guide (secure tool access, non-human identity management, and auditable interactions) corresponds to Section 3.3 and to POL-IAM-003. Organizations implementing CIS Controls use the guides for safeguard-level detail beyond this policy.

**OWASP Top 10 for Large Language Model Applications:**

Sections 3.4 and 3.8 use the current OWASP list as the reference for agent risks and as the test basis for AI built in-house. Sections 3.1 and 3.6 address the list's sensitive information disclosure and misinformation risks for AI that [ORGANIZATION_NAME] uses rather than builds.

**NIST AI Risk Management Framework (AI 100-1) and Generative AI Profile (AI 600-1):**

This policy implements a practical subset of the AI RMF Govern function for an organization that mostly uses AI rather than builds it: accountability for AI use (Sections 3.6 and 4), an inventory of AI systems (Section 3.9), third-party AI risk (Section 3.2), and human oversight proportional to autonomy (Section 3.4). It addresses several risks the Generative AI Profile identifies, including confabulation, data privacy, information security, and information integrity. Organizations that build AI systems for others, or that face sector-specific AI regulation, need the Map, Measure, and Manage functions as well.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
