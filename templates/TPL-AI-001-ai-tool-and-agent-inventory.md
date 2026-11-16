# TPL-AI-001: AI Tool and Agent Inventory

| | |
|---|---|
| **Document ID** | TPL-AI-001 |
| **Version** | 1.0 |
| **Supports** | POL-AI-001 Sections 3.2, 3.3, 3.4, 3.8, and 3.9; POL-IAM-003 Section 3.9; CIS Controls v8.1 Safeguards 2.1, 2.3, 5.5, 15.1 |
| **Owner** | [POLICY_OWNER] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Internal |

---

## How to use this template

This template is the AI inventory required by POL-AI-001 Section 3.9. It records five kinds of AI in use at [ORGANIZATION_NAME], each in its own section: approved AI tools (Section 2), AI features inside software the organization already uses (Section 3), connectors that give AI tools access to company systems (Section 4), agents (Section 5), and AI capabilities built in-house (Section 6). Section 7 is the quarterly reconciliation that keeps the inventory honest.

**Start with what already exists.** The first pass usually finds more AI than anyone expected: features a vendor switched on, browser extensions, and assistants a user connected to a mailbox last year. Record everything found, including tools that will be removed. An entry with a status of "Remove" is better evidence than a tool nobody wrote down.

**Connectors and agents are also non-human identities.** Every row in Sections 4 and 5 has a matching entry in the POL-IAM-003 inventory, and the NHI ID column links the two. Review them together during the quarterly non-human identity review in TPL-IAM-001, so that each identity is reviewed once, by its named owner.

**Statuses.** Use one of: Approved, Under review, Restricted (approved with conditions, recorded in the Notes column), Remove, Removed. Keep removed entries for one year so the reconciliation can show what changed.

**Dates** use ISO format (YYYY-MM-DD). Classifications use the levels in POL-DC-001: Public, Confidential, Restricted.

---

## 1. Inventory Summary

| | |
|---|---|
| **Quarter** | [QUARTER_YEAR] |
| **Reconciled by** | |
| **Reconciliation date** | |
| **Approved AI tools** | |
| **AI features reviewed / enabled / turned off** | |
| **Connectors** | |
| **Agents (assistive / supervised / autonomous)** | |
| **In-house AI systems** | |
| **New since last quarter** | |
| **Removed since last quarter** | |
| **Unapproved AI found this quarter** | |
| **Open findings** | |

---

## 2. Approved AI Tools

Standalone AI tools approved under POL-AI-001 Section 3.2. A tool appears here only after the vendor review under POL-TPRM-001 Section 3.6. A consumer or free tier is a separate entry from the business tier of the same product, and is not approved for company data.

| Tool ID | Tool and tier | Vendor | Vendor tier (POL-TPRM-001) | Highest classification approved | Business agreement in place | No training on company data confirmed | Retention of prompts and outputs | SSO enforced | Admin audit records available | Model providers and sub-processors disclosed | Business owner | Approved date | Next review | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI-T-001 | [AI_TOOL_NAME_AND_TIER] | | | | Yes / No | Yes / No | | Yes / No | Yes / No | Yes / No | | | | | |

---

## 3. AI Features in Existing Software

AI features inside tools [ORGANIZATION_NAME] already uses, including features a vendor enabled by default. POL-AI-001 Section 3.2 requires review before a feature is used with Confidential or Restricted data, and turning it off until review where the platform allows.

| Feature ID | Platform or application | AI feature | Vendor default state | Current state (On / Off / Limited to group) | Admin can turn off | Reviewed | Highest classification approved | Covered by existing agreement | Reviewer | Review date | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI-F-001 | [PLATFORM] | | | | Yes / No | Yes / No | | Yes / No | | | | |

---

## 4. Connectors and Integrations

Every OAuth grant, plugin, API key, or MCP server that gives an AI tool access to [ORGANIZATION_NAME] systems. Each is a non-human identity under POL-IAM-003 and follows POL-AI-001 Section 3.3.

| Connector ID | Connector | Type (OAuth app / MCP server / plugin / API key / other) | AI tool it serves | Systems and data it reaches | Scope (specific resources, not tenant-wide) | Access type (Delegated / Application) | Admin-approved consent | Publisher verified | Runs code locally | NHI ID (POL-IAM-003) | Named owner | Last reviewed | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI-C-001 | | | AI-T-001 | | | | Yes / No | Yes / No | Yes / No | | | | | |

Flag for follow-up any connector with application access across the tenant, consent granted by a user rather than an administrator, an unverified publisher, or local code execution with the user's full permissions.

---

## 5. Agents

Every AI agent that takes actions, at the level assigned under POL-AI-001 Section 3.4.

| Agent ID | Name and purpose | Level (Assistive / Supervised / Autonomous) | Named owner | Identity used (NHI ID) | Tools and connectors (IDs) | Actions it takes without approval | Actions requiring per-action approval | Reads untrusted content | Has Confidential or Restricted data | Can send outside the organization | Outbound step supervised | Written approval reference (Autonomous only) | Actions logged to | Stop procedure | Last reviewed | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI-A-001 | | | | | | | | Yes / No | Yes / No | Yes / No | Yes / No / N/A | | | | | |

**Checks for each agent at every review:**

None of the always-approve actions in POL-AI-001 Section 3.4 appears in "Actions it takes without approval": sending money or changing payment details, contacting unapproved external recipients, changing access permissions, deleting data or disabling security controls, or agreeing to anything on [ORGANIZATION_NAME]'s behalf.

If "Reads untrusted content," "Has Confidential or Restricted data," and "Can send outside the organization" are all Yes, then "Outbound step supervised" is Yes. An agent with all three and no supervised outbound step is stopped until it is reconfigured.

Every Autonomous agent has a written approval reference, a dedicated identity, a log destination, and a stop procedure that the owner has tested.

---

## 6. In-House AI Systems

AI capabilities [ORGANIZATION_NAME] builds into its own systems, workflows, or products using a model provider's API, under POL-AI-001 Section 3.8.

| System ID | System and purpose | Model provider (Tool or vendor ID) | Highest classification processed | Passes untrusted input to the model | Tools or actions available to the model | API key location (NHI ID) | Prompt and output logging location | Log store approved for classification | Last OWASP LLM Top 10 test (POL-AI-001 Section 3.8) | Significant change since last test | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI-S-001 | | | | Yes / No | | | | Yes / No | | Yes / No | | |

A Yes in "Significant change since last test" means the system is retested before the next production release.

---

## 7. Quarterly Reconciliation

Compare the inventory against what the environment actually shows. Record what each source found and what was done about it.

| Discovery source | What to look for | Found this quarter | Action taken |
|---|---|---|---|
| Identity provider application consents and enterprise applications | AI tools and connectors not in Section 4, consents granted by users, new permission scopes | | |
| Productivity platform and SaaS admin settings | AI features newly available or enabled since the last review, not in Section 3 | | |
| Endpoint and browser extension inventory | AI desktop applications, browser extensions, and local MCP servers | | |
| Network or DNS visibility, or the CASB | Traffic to AI services not in Section 2 | | |
| Expense and procurement records | AI subscriptions bought outside the approval process | | |
| Non-human identity review (POL-IAM-003 Section 3.9) | Connector and agent identities whose owner, scope, or purpose changed | | |
| Incident and help desk records | AI-related incidents under POL-AI-001 Section 3.10 and their follow-up | | |

Unapproved AI found during reconciliation is either submitted for approval or removed, following POL-AI-001 Section 3.9. Unapproved connectors to company accounts have access revoked within one business day, per POL-AI-001 Section 5.

**Sign-off**

| | |
|---|---|
| **Reviewed by (Information Security function)** | |
| **Date** | |
| **Findings carried to the risk register (TPL-GOV-001)** | |
| **Exceptions requested (TPL-GOV-002)** | |

---

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
