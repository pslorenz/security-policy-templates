# STD-IAM-002: Single Sign-On and Federation Standard

| | |
|---|---|
| **Document ID** | STD-IAM-002 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This standard defines how applications integrate with [ORGANIZATION_NAME]'s identity provider so that users authenticate once and access multiple applications without separate logins. It is sometimes called single sign-on (SSO) or federation.

The goal is to bring every business application under a single identity that we control. When a user joins, leaves, or changes roles, we make the change once and it propagates everywhere. When an account is compromised, we can disable it everywhere from one place.

This standard supports POL-IAM-001 (Access Control Policy) and STD-IAM-001 (Password and Authentication Standard) by making sure the strong authentication and access controls in those documents reach every application, not just the ones our identity provider handles natively.

## 2. Scope

This standard applies to any application or service that authenticates users at [ORGANIZATION_NAME], including:

Software-as-a-Service applications (CRM, accounting, HR, project management, marketing tools, file sharing, document signing, anything else used for company work). Internally hosted applications. Cloud platforms (Azure, AWS, GCP) used for company resources. Vendor portals where employees log in to interact with suppliers or partners.

It does not apply to:

Public-facing applications where customers or the general public log in. Personal accounts that employees use for work-related but non-business activities (a personal LinkedIn account used for professional networking, for example). Applications used by fewer than three people for short-duration projects, where the integration cost outweighs the benefit (these are still subject to access control review per POL-IAM-001).

## 3. Standard Requirements

### 3.1 SSO Is the Default for All Business Applications

Every business application that supports SSO must be configured to use it. New applications brought into [ORGANIZATION_NAME] are evaluated for SSO support during procurement. Applications that do not support SSO are flagged as a gap and either replaced, isolated, or accepted as a documented exception per Section 3.10.

The reason is direct. Applications outside SSO require separate credentials. Separate credentials mean separate password resets, separate access reviews, and separate offboarding. Every additional credential increases the chance of credential reuse, weak passwords, or accounts that survive an employee's departure.

When evaluating a new application, the procurement process asks four questions:

Does it support SAML 2.0 or OpenID Connect federation? Does it support automated user provisioning through SCIM or a similar protocol? Does it support multi-factor authentication enforced through the identity provider? What does it cost to enable SSO (some vendors charge extra for this, sometimes called the "SSO tax")?

If the answer to the first question is no, the application is not approved for new deployment without an exception. Existing applications that fail this test are migrated or replaced on a documented timeline.

### 3.2 The Approved Identity Provider

[ORGANIZATION_NAME]'s approved identity provider is [APPROVED_IDP, e.g., the identity service of the organization's primary productivity platform, or a standalone identity provider that supports SAML 2.0, OpenID Connect, and SCIM]. All federated applications integrate with this identity provider.

Multiple identity providers are not used in parallel for the same population of users. If an application supports federation only with a different provider than ours, the application is either replaced or accessed through an identity bridge (such as the federation features of the approved IdP) that lets our users authenticate without managing a second set of credentials.

### 3.3 Federation Protocols

Applications federate using one of these protocols, ranked by preference:

**OpenID Connect (OIDC) with OAuth 2.0.** The current standard for new applications. Cleaner than SAML for modern applications, supports mobile and single-page applications well.

**SAML 2.0.** The mature standard for federation, especially common with established SaaS providers. Acceptable when OIDC is not supported.

**WS-Federation.** Older protocol. Acceptable only for legacy applications that do not support OIDC or SAML, with a plan to migrate.

**Header-based authentication or proprietary protocols.** Not approved for new deployments. Existing deployments using these protocols are migrated to a standard protocol or isolated behind an authenticating reverse proxy.

### 3.4 User Provisioning and Deprovisioning

Where the application supports it, user provisioning is automated through SCIM (System for Cross-domain Identity Management) or a similar protocol. The identity provider tells the application when to create, update, or disable user accounts.

Automated provisioning matters because manual provisioning fails. When a user is added, manually provisioning them across twelve applications takes hours. When a user leaves, manually disabling them across twelve applications takes hours that nobody has, and one or two accounts get missed.

For applications that do not support SCIM, manual provisioning and deprovisioning is documented in a runbook with named owners. The runbook is followed for every joiner, mover, and leaver, with verification by a second person within seven days of the event.

### 3.5 Multi-Factor Authentication Through the Identity Provider

The identity provider enforces MFA on the user's authentication, not the individual application. This is one of the main benefits of federation: the MFA requirement is set once and applies everywhere.

Applications that try to enforce their own MFA in addition to the identity provider's MFA are configured to defer to the identity provider. Multiple MFA prompts during a single sign-on flow create user confusion and do not improve security.

Applications that do not accept the identity provider's MFA (typically older applications that require their own authentication) are flagged for replacement or migration.

### 3.6 Conditional Access at the Identity Provider

Conditional access policies described in POL-IAM-002 (Remote Access Policy) apply to all federated applications. When a user authenticates through the identity provider to reach an application, the conditional access rules evaluate the request before granting access.

This means that the device requirements, location restrictions, and risk-based controls in POL-IAM-002 reach every federated application without per-application configuration.

For sensitive applications (financial systems, HR systems, customer data systems), additional conditional access rules may require phishing-resistant authentication, a managed device, or a known network. These additional rules are configured at the identity provider and apply specifically to the targeted applications.

### 3.7 Application-Specific Roles and Permissions

Federation tells an application who the user is. The application still decides what the user can do.

For each federated application, the access roles within the application are defined and tied to groups in the identity provider. When a user is added to a group, they get the corresponding access in the application. When they are removed from the group, they lose the access.

Group-based access is preferred over individual user-based access in applications. It scales better, reviews better, and survives staff turnover better.

Where the application supports it, role assignments are also automated through SCIM. The identity provider tells the application not just that the user exists but what role to assign them.

### 3.8 Discovery and Onboarding of New Applications

When an employee or department starts using a new application that has not gone through procurement, the Information Security function is notified. Shadow IT discovery features in the identity provider or endpoint platform, or a CASB (Cloud Access Security Broker) tool, can identify these applications by analyzing network traffic, browser activity, or OAuth consent grants.

Newly discovered applications are evaluated within thirty days of discovery. The evaluation determines:

Whether the application is sanctioned for company use. Whether it can be brought into SSO. Whether it should be replaced, isolated, or blocked.

Applications used in the discovery period without prior sanction are not automatically blocked, but they are escalated for review. Blocking too aggressively pushes users into shadow IT through personal accounts, which is worse than the original problem.

### 3.9 SAML and OIDC Configuration Hygiene

Federation configurations are reviewed annually to confirm they remain secure. The review covers:

Certificate expiration dates. SAML certificates and OIDC signing keys expire and must be renewed before they expire. Allowed redirect URIs and assertion consumer service URLs. Misconfigured URIs are a known attack vector for federation bypass. Token lifetime settings. Tokens that live too long give attackers a longer window to use stolen credentials. Audience and issuer restrictions. Each application accepts tokens only from the expected issuer and only when the audience matches. Logging configuration. Authentication events at the application are logged either by the application or by the identity provider, and the logs reach the central logging platform.

Federation configurations that have not been reviewed in twelve months are flagged for review and remediated within thirty days.

### 3.10 Exceptions

Some applications cannot be federated, and the exception process says so openly. It documents what cannot be federated, why, and what we are doing instead.

Acceptable reasons for an exception:

The application predates federation standards and cannot be retrofitted, with a documented replacement plan and timeline. The application is used by few users for a short engagement, where the integration cost outweighs the benefit. The application is operated by a vendor who does not offer federation in any tier, and switching vendors is not feasible at the moment.

For each exception, the compensating controls include:

A unique, strong password generated by the approved password manager and stored only in the password manager. MFA at the application where it is supported, even if the application's MFA is weaker than the identity provider's. An access list reviewed quarterly to confirm only authorized users have credentials. Logging of access events to the central logging platform where the application supports it.

Exceptions are reviewed quarterly to confirm the original reason still applies and the compensating controls remain in place. Exceptions that drift from their justification are remediated.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Approves new federated applications. Reviews federation configurations annually. Manages the discovery process for unsanctioned applications.

**IT function (or IT service provider).** Implements federation for approved applications. Configures SCIM provisioning. Maintains the identity provider. Renews certificates and keys before expiration.

**Procurement function (or whoever approves SaaS purchases).** Verifies that proposed applications meet the federation requirements before purchase. Coordinates with Information Security on any application that does not.

**Application owners (the business owner of each federated application).** Define the access roles and group mappings for their application. Review access on the cadence in POL-IAM-001 Section 3.3.

**All users.** Use the SSO authentication path for every business application. Do not create separate accounts for federated applications. Report any application that requires a separate login to the IT or Information Security function.

## 5. Enforcement

Violations of this standard may result in loss of access to the affected applications, escalation to the user's manager, and disciplinary action consistent with [ORGANIZATION_NAME]'s human resources policies.

Specific remediation timelines:

Federated applications without SCIM provisioning where it is available: configured within sixty days of identification. Federation certificates within thirty days of expiration: renewed before expiration; expired certificates are renewed within seven days. Newly discovered unsanctioned applications: evaluated within thirty days of discovery. Manual provisioning runbooks not maintained: updated within thirty days of identification. Exceptions without documented compensating controls: controls implemented or exception revoked within thirty days.

## 6. Related Documents

POL-IAM-001: Access Control Policy (the parent policy this standard supports)
STD-IAM-001: Password and Authentication Standard (authentication requirements that flow through federation)
POL-IAM-002: Remote Access Policy (conditional access rules apply to federated applications)
POL-IAM-003: Non-Human Identity Governance Policy (governs the service principals and application registrations created by federation)
POL-IR-001: Incident Response Policy (response to federation compromise)
STD-AM-001: SaaS Asset Management Standard (SaaS inventory, onboarding baseline, and retirement)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.AA-01 (Identities and credentials for authorized users, services, and hardware are managed by the organization). PR.AA-03 (Users, services, and hardware are authenticated). PR.AA-04 (Identity assertions are protected, conveyed, and verified). PR.AA-05 (Access permissions, entitlements, and authorizations are defined and managed).

**CIS Controls v8.1:**

Control 5 Account Management: Safeguards 5.6 (centralize account management).

Control 6 Access Control Management: Safeguards 6.3 (require MFA for externally-exposed applications, enforced at the identity provider), 6.7 (centralize access control), 6.8 (define and maintain role-based access control).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
