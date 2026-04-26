# The Accounts You Forgot You Had

*A short guide for business owners on why non-human identities matter, what a governance program does about them, and what is needed from leadership to make it work.*

---

## About this document

This is a client-facing explainer designed to introduce non-technical business owners to the concept and importance of non-human identity governance. It pairs with POL-IAM-011 (Non-Human Identity Governance Policy) and RUN-IAM-011 (Non-Human Identity Discovery Runbook), which are the operational documents.

The voice uses "we" throughout, intended to be read as the organization's security function, IT team, or external security service provider speaking to the executive sponsor or business owner. Adopters should leave this voice in place. It works whether the document is delivered by an internal team or by an external service provider. Replacing "we" with an organization name or a service provider name flattens the document.

Replace bracketed placeholders ([ESTIMATED_PROGRAM_COST], [TIMELINE_WEEKS]) with values appropriate to the adopting environment. Guidance for these values appears in the customization guide.

---

## The short version

Your organization has more accounts than you have employees. Many more. Every integration between systems, every automation that moves data from point A to point B, every cloud service that talks to another cloud service, every Power Automate flow that someone built to save time on a weekly report: all of these run on accounts that are not tied to a person. The industry calls them non-human identities.

In a typical organization, there are roughly forty-five non-human accounts for every human user. A fifty-person company likely has over two thousand of them. Most organizations have no list of what they are, who owns them, or what they can access.

> An account with broad access and no named owner is a credential waiting to be used by someone who should not have it. Attackers do not need to breach your email to cause damage. They can take over a forgotten service account and walk through the front door.

## Why this matters right now

Three changes in the threat environment make this problem urgent rather than theoretical.

First, the time from when a vulnerability is discovered to when it is actively exploited has dropped from months to hours. Attackers now use AI tools that find exploitable weaknesses faster than defenders can patch them. Non-human accounts are a favorite target because they often have strong permissions and weak oversight.

Second, cyber insurance carriers have rewritten their requirements around identity governance. Documented governance of non-human identities has moved from a nice-to-have item on the questionnaire to a bind-or-not-bind decision. Organizations without a program in place are seeing premium increases or coverage denials.

Third, AI agents and automation tools are creating new non-human identities faster than anyone is tracking them. Every Copilot integration, every coding assistant with access to a repository, every AI-powered workflow your team builds, creates another account that can act inside your environment. These are the next generation of non-human identities, and the pattern of forgetting about them is already repeating.

## What we are doing

We are establishing a governance program for non-human identities across your environment. The program has four parts, each sized to the scale of your organization.

### One: We are going to find them all

We are going to run a discovery across your Microsoft 365 tenant, your Active Directory (if you have one), your cloud subscriptions, your source control, your Power Platform environment, and the third-party SaaS applications connected to your data. This produces a complete inventory of non-human accounts for the first time. The inventory is how every other part of the program works.

### Two: We are going to give every account an owner

Every account in the inventory gets a named person who is accountable for it. Not a team, not a role, a specific person. That person confirms the account is necessary, confirms what it should be able to access, and is responsible for cleaning it up when the business reason for it ends. Accounts with no owner get disabled.

### Three: We are going to review them every quarter

Every ninety days, the named owner confirms the account is still needed and still correctly scoped. Accounts that have not been used in six months get disabled. Accounts that have not been used in a year get deleted. This becomes a recurring discipline, not a one-time cleanup.

### Four: We are going to watch the active ones

The accounts that remain get monitored. If a non-human account starts doing things outside of its normal pattern (signing in from an unexpected location, accessing systems it has not touched before, creating new permissions for itself), the security operation is alerted and investigates. This is how we catch an attacker who has taken over a legitimate account, which is the most common breach pattern against this class of identity.

## What we need from you

The program requires a small amount of executive support and a larger amount of cooperation from the team leaders who will be named as owners.

**Sponsorship.** Someone at the executive level needs to be the named sponsor of the program. This is typically the business owner, the CFO, or the COO. The sponsor does not do the work, but the sponsor signs off on the policy, approves exceptions, and makes the final call when there is tension between convenience and security.

**Named owners across the business.** Every department that uses automation (which is all of them) will have at least one person named as the owner for identities related to their work. This is usually the department lead or a senior operator. The ownership responsibility is modest: a quarterly review that takes under an hour for most departments.

**Willingness to decommission.** The discovery will find automations nobody remembers building, integrations nobody remembers approving, and accounts from vendors the organization no longer uses. The right answer in most cases is to disable them. We will catch a few real uses on the way through. Expect some temporary friction, followed by a cleaner and safer environment.

**Patience on the timeline.** Full implementation runs roughly [TIMELINE_WEEKS] weeks from start to operational steady state. The first portion is discovery and ownership assignment. The next is remediation of findings that require technical work. The final portion establishes the quarterly review rhythm. The urgent items (credentials in the wrong places, accounts with excessive access, accounts owned by departed employees) are addressed in the first two weeks.

## What it costs and what it returns

The program requires time from your team and a modest investment in tooling, most of which is already in your environment and simply not being used. For an organization in your size range, the direct cost is roughly [ESTIMATED_PROGRAM_COST] in internal time and, potentially, one additional tool license.

The returns show up in three places.

Your cyber insurance renewal goes better, either through avoided premium increases or through maintained coverage that would otherwise be denied.

Your incident exposure drops measurably. The majority of successful breaches at organizations your size involve compromised non-human identities, and a governed environment is a significantly harder target.

Your operational posture becomes explainable. When an auditor, a client, or a prospect asks how you manage access across your systems, you have a real answer.

> The accounts you forgot you had are the accounts an attacker will use. The program turns a forgotten problem into a managed one, and it does so in a way that scales with your business rather than adding to the friction of running it.

## Next steps

Proceed in three stages:

Confirm the executive sponsor and schedule a kickoff conversation with department leads.

Execute the discovery and produce the initial inventory.

Review the inventory together, assign ownership, and agree on the remediation work for any urgent findings.

From there, the program operates on the quarterly cadence documented in the non-human identity governance policy.

Questions regarding this document or the program can be directed to your security function or service provider.

---

*Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution-ShareAlike 4.0.*
