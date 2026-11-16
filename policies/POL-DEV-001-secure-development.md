# POL-DEV-001: Secure Development Policy

| | |
|---|---|
| **Document ID** | POL-DEV-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] builds software securely. It applies only where [ORGANIZATION_NAME] develops, customizes, or maintains software, and an organization that only buys and configures software can mark it "Not adopted" under POL-GOV-001 Section 3.7.

Many organizations that think they do not develop software do. A PowerShell script that runs nightly with administrator rights is software. So is an automation that moves data between two SaaS applications, the infrastructure templates that build a cloud environment, a customer portal a contractor built five years ago, and an internal tool that calls an AI model. Each of these can leak credentials, be exploited, or break in a way that takes data with it. This policy sets a baseline proportional to that risk, sized for a small team rather than a software company.

## 2. Scope

This policy applies to software that [ORGANIZATION_NAME] writes, has written for it, or maintains, including:

Applications and websites, internal or customer-facing. Scripts and scheduled tasks that run in production or with privileged access. Integrations and automations between systems, including low-code workflows that handle Confidential or Restricted data. Infrastructure as code and deployment pipelines. AI features built on a model provider's API, which also follow POL-AI-001 Section 3.8.

It applies to employees and to contractors and vendors developing software on [ORGANIZATION_NAME]'s behalf. One-off scripts run interactively by an administrator and not saved for reuse are out of scope, though their credential handling still follows STD-IAM-001.

**Scaling the policy.** Most small organizations do not run a development team, and applying every section of this policy to a handful of scripts would be overhead without benefit. Adopt the level that matches what [ORGANIZATION_NAME] actually builds, record the level in the suite table in POL-GOV-001 Section 3.7, and move up when the work changes:

| Level | Typical organization | Sections that apply |
|---|---|---|
| Scripts and automations | Builds scripts, scheduled tasks, and integrations between SaaS applications, but no applications of its own. Common in organizations of twenty to a few hundred people. | 3.1, 3.2, 3.3, 3.9, 3.11 |
| Internal applications | Builds or maintains applications used only by its own staff. | All sections, with the testing in Section 3.6 limited to the automated checks |
| Internet-facing applications | Builds or maintains applications that customers, clients, or the public reach, particularly those handling Confidential or Restricted data. | All sections, plus application testing at the Expanded tier of STD-VM-001 |

An organization that writes no code at all, including scripts, marks this policy "Not adopted" in POL-GOV-001 Section 3.7.

## 3. Policy Statements

### 3.1 All Code Lives in Source Control

Code in scope is kept in a source control system that [ORGANIZATION_NAME] controls, not on individual laptops or shared drives. Access to repositories follows POL-IAM-001: individual accounts, multi-factor authentication, phishing-resistant authentication for repository administrators, and removal on departure. Repositories are reviewed in the quarterly access review.

The branch that deploys to production is protected. Changes reach it through a reviewed pull request or merge request, not direct commits, and force-pushes are disabled.

### 3.2 Secrets Never Go in Code

Passwords, API keys, tokens, certificates, and connection strings are never stored in source code, configuration files in source control, build logs, or container images. Code reads secrets at runtime from the secrets vault, or uses a platform-managed identity under STD-IAM-001 Section 3.7.

Secret scanning runs on every repository under STD-DC-001 Section 3.6. A secret committed to a repository is treated as exposed and rotated within seven days, even if the commit is removed, because repository history and clones keep it.

### 3.3 Changes Are Reviewed

Every change to production code is reviewed by someone other than its author before it is merged. The reviewer checks that the change does what it says, handles input safely, does not add secrets or unnecessary permissions, and does not introduce dependencies without reason. Where the team has only one developer, the reviewer can be another technical person or the outside security provider, and changes touching authentication, authorization, or payment flows always get a second reviewer.

Code generated with AI assistance is reviewed the same way as code written by hand, consistent with POL-AI-001 Section 3.6. The developer who submits it is accountable for it.

### 3.4 Dependencies Are Known and Kept Current

Third-party libraries and components are part of the software and part of its attack surface. [ORGANIZATION_NAME] maintains an inventory of the third-party components each application uses, generated automatically from the build where possible, in a standard software bill of materials format.

Dependencies come from the official package registries for the language or from vendors' official channels. Versions are pinned so that builds are reproducible. Dependency scanning runs on every build and flags components with known vulnerabilities, which are prioritized and remediated under POL-VM-001 Section 3.3. Components that are abandoned, unmaintained, or from an unknown publisher are replaced. New dependencies are added deliberately, with the reason recorded in the change.

### 3.5 Security Is Designed In

Before building a new application, or making a significant change to one, that handles Confidential or Restricted data or is reachable from the internet, the team spends a short session on how it could be attacked: what it trusts, what an attacker would want from it, and where input from outside comes in. The answers are recorded with the design and drive the security tests in Section 3.6.

Applications use the approved identity provider for user authentication under STD-IAM-002 rather than building their own login. They follow least privilege for their own service identities under POL-IAM-003, validate all input from outside the application, encode output to prevent injection, use current, supported cryptography and transport encryption, and fail closed when a security check cannot complete.

### 3.6 Security Is Tested Before Release

Automated checks run in the build pipeline: static analysis for common coding flaws, dependency scanning, and secret scanning. Findings at High or Critical priority under POL-VM-001 Section 3.2 block the release until fixed or accepted as a risk.

Internet-facing applications that handle Confidential or Restricted data are tested by someone other than the developers before first release and at least annually, under the Expanded tier of STD-VM-001: a penetration test, or a dynamic application security test with manual review. The OWASP Top 10 and the OWASP Application Security Verification Standard are the reference for what the testing covers. AI features are also tested under POL-AI-001 Section 3.8.

### 3.7 Environments Are Separated

Development, test, and production are separate environments with separate credentials. Developers do not have standing administrator access to production; production changes go through the deployment pipeline. Restricted production data is not copied into development or test environments unless it is masked or synthetic. Infrastructure as code is reviewed like application code, and the deployed configuration follows the hardening baselines in POL-EP-001 Section 3.1 and POL-NET-001 Section 3.8.

### 3.8 Vulnerabilities Are Handled Like Any Other

Vulnerabilities found in [ORGANIZATION_NAME]'s own software, whether by scanning, testing, users, or outside researchers, are rated and remediated under the priority tiers and cadences in POL-VM-001 Sections 3.2 and 3.3. External reports arrive through the disclosure channel in POL-VM-001 Section 3.10. Critical vulnerabilities in [ORGANIZATION_NAME]'s own code get a root cause review, so that the class of flaw is fixed and not just the instance.

### 3.9 Outside Developers Follow the Same Rules

Contractors and vendors who build or maintain software for [ORGANIZATION_NAME] follow this policy. Their contracts require it, give [ORGANIZATION_NAME] ownership of or access to the source code, and require notification of security issues, consistent with POL-TPRM-001 Section 3.3. When the engagement ends, their access to repositories, pipelines, and environments is removed.

### 3.10 Developers Are Trained

People who write code for [ORGANIZATION_NAME] complete secure development training when they start and at least annually, covering the common vulnerability classes, secret handling, and this policy, as part of the role-specific training in POL-GOV-001 Section 3.8.

### 3.11 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Sets the pipeline security checks. Reviews threat models and test results for internet-facing applications. Approves exceptions.

**Development lead (or the senior developer, or the vendor's lead for outsourced work).** Ensures the team follows this policy. Maintains the pipelines, branch protection, and component inventory.

**Developers.** Write, review, and test code under this policy. Keep secrets out of code. Report vulnerabilities they find.

**Application owners.** Are accountable for each application's risk. Approve releases with known risk and fund remediation.

**Procurement function.** Includes the requirements in Section 3.9 in development contracts.

## 5. Enforcement

Violations of this policy may result in loss of repository or deployment access and disciplinary action consistent with [ORGANIZATION_NAME]'s human resources policies. For contractors and vendors, violations may result in contract termination.

Specific remediation timelines:

Secrets found in source control: rotated within seven days. Production branch without protection: protected within seven days. Applications without a component inventory: inventory produced within ninety days. Internet-facing applications handling Confidential or Restricted data without a test in the last twelve months: tested within ninety days.

## 6. Related Documents

POL-VM-001: Vulnerability Management Policy (rating, remediation cadences, and disclosure)
STD-VM-001: Security Testing Standard (application testing and test conduct)
POL-AI-001: AI and Agent Governance Policy (AI features and AI-assisted code)
STD-DC-001: Data Loss Prevention Standard (secret scanning)
POL-IAM-001: Access Control Policy (repository access)
POL-IAM-003: Non-Human Identity Governance Policy (service identities and pipeline credentials)
STD-IAM-001: Password and Authentication Standard (credential handling)
STD-IAM-002: Single Sign-On and Federation Standard (application authentication)
POL-EP-001: Endpoint Protection Policy (server baselines)
POL-NET-001: Network Security Policy (cloud network baselines)
POL-TPRM-001: Third-Party Risk Management Policy (outsourced development)
POL-GOV-001: Information Security Policy (adoption, training, and exceptions)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.PS-06 (Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle). ID.RA-01 (Vulnerabilities in assets are identified, validated, and recorded). ID.RA-08 (Processes for receiving, analyzing, and responding to vulnerability disclosures are established). GV.SC-05 (Requirements to address cybersecurity risks in supply chains are established, prioritized, and integrated into contracts and other types of agreements with suppliers and other relevant third parties).

**CIS Controls v8.1:**

Control 16 Application Software Security: Safeguards 16.1 (establish and maintain a secure application development process), 16.2 (establish and maintain a process to accept and address software vulnerabilities), 16.3 (perform root cause analysis on security vulnerabilities), 16.4 (establish and manage an inventory of third-party software components), 16.5 (use up-to-date and trusted third-party software components), 16.6 (establish and maintain a severity rating system and process for application vulnerabilities), 16.8 (separate production and non-production systems), 16.9 (train developers in application security concepts and secure coding), 16.10 (apply secure design principles in application architectures), 16.11 (use vetted modules or services for application security components), 16.12 (implement code-level security checks), 16.13 (conduct application penetration testing), 16.14 (conduct threat modeling).

**NIST SP 800-218 (Secure Software Development Framework):**

This policy implements a small-team subset of the SSDF practice groups: protecting the software (Sections 3.1 and 3.2), producing well-secured software (Sections 3.3 through 3.7), and responding to vulnerabilities (Section 3.8).

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
