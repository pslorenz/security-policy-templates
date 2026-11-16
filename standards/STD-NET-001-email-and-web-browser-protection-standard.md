# STD-NET-001: Email and Web Browser Protection Standard

| | |
|---|---|
| **Document ID** | STD-NET-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This standard sets the technical requirements for protecting [ORGANIZATION_NAME]'s email and web browsing. Email and the browser are where most attacks against small organizations begin: a phishing link that steals a session, an attachment that runs code, a message from a lookalike domain asking finance to change a vendor's bank account. They are also the two places where users make security decisions dozens of times a day.

The standard implements the edge filtering in POL-NET-001 Sections 3.2 and 3.3 for traffic that never crosses the office network, the browser requirements of POL-EP-001, and the email rules users follow under POL-AUP-001 Section 3.4. It adds the controls those documents do not cover: email authentication for every domain the organization owns, inbound mail filtering, browser and extension management, and the payment-change verification that stops business email compromise when everything else fails.

## 2. Scope

This standard applies to:

Every domain [ORGANIZATION_NAME] owns, including domains that do not send email. The email platform, every service that sends email on [ORGANIZATION_NAME]'s behalf (marketing, billing, ticketing, and similar), and every mailbox. Web browsers and email clients on managed devices, and on personal devices where POL-IAM-002 permits browser access. Browser extensions. The finance processes that act on payment instructions received by email or phone.

## 3. Standard Requirements

### 3.1 Supported Browsers and Email Clients

Only browsers and email clients on the approved list are used for company work, and only versions still supported by their vendor. Approved browsers are [APPROVED_BROWSERS, e.g., one or two current mainstream browsers that support centralized management through the device management platform].

Browsers update automatically. A browser more than one major version behind its current stable release is treated as unpatched under POL-VM-001. Browsers on managed devices are configured centrally through the device management platform rather than by each user.

### 3.2 Browser Configuration

On managed devices, the browser configuration includes:

The browser's built-in protection against known malicious sites and downloads, turned on and not user-adjustable. Downloads of executable and script files from the internet blocked or warned, with exceptions approved by IT. Password saving handled under STD-IAM-001 Section 3.3. Signing in to the browser's sync feature allowed only with the company account, so that company bookmarks, history, and saved data do not sync to a personal account. Third-party cookies and pop-ups blocked by default.

### 3.3 Browser Extensions

Extensions can read and change everything a user sees in the browser, including pages in signed-in business applications. On managed devices, extensions are blocked by default and only extensions on the approved list can be installed. The list is maintained by the IT function under POL-AUP-001 Section 3.8.

An extension is approved only after review of the permissions it requests, its publisher, and how it handles data. Extensions that can read data on all sites get extra scrutiny. AI extensions also go through POL-AI-001 Section 3.3, because they usually send page content to an outside service. Installed extensions are reviewed quarterly, and extensions that are removed from the store, change ownership, or request new permissions are re-reviewed before they are allowed to update.

### 3.4 DNS and Web Filtering Everywhere

The DNS filtering and URL filtering in POL-NET-001 Sections 3.2 and 3.3 apply to managed devices wherever they are, not only in the office. Laptops use a filtering agent or a protective DNS client so that the same blocking applies on home networks, hotel networks, and phone hotspots. Categories blocked include known-malicious sites, newly registered domains where the service supports it, and the high-risk categories in POL-NET-001 Section 3.3.

### 3.5 Email Authentication for Every Domain

Every domain [ORGANIZATION_NAME] owns publishes email authentication records, because attackers spoof whichever domain is least protected.

**Sending domains.** SPF lists every service authorized to send for the domain and ends in a fail or softfail qualifier. DKIM signs mail from every sending service, with keys of at least 2048 bits where the service supports them. DMARC is published and moves through monitoring (p=none), then quarantine, to reject, with aggregate reports collected and reviewed at each stage. A reasonable target is reaching p=reject within [DMARC_ENFORCEMENT_TIMELINE, e.g., about six months] of adoption. That is a target, not a deadline. An organization with many sending services, or with services that cannot yet sign with DKIM, may need longer; the pace is set by how quickly the aggregate reports show every legitimate sender passing, not by the calendar, and moving to reject before then blocks the organization's own mail. Progress, and a revised target date where needed, is reviewed quarterly. Major mailbox providers now require DMARC from organizations that send in bulk, and an unauthenticated domain is easy for an attacker to impersonate.

**Domains that do not send email.** Parked and defensive domains publish an SPF record that authorizes nothing, a DMARC policy of reject, and a null MX record, so that nothing can be sent as them.

**Inbound transport.** MTA-STS and TLS reporting are published for receiving domains where the email platform supports them, so that other mail servers deliver to [ORGANIZATION_NAME] over encrypted connections that cannot be silently downgraded.

**Sender inventory.** The list of services authorized to send as each domain is kept with the SaaS inventory in STD-AM-001 Section 3.1. When a service is retired, its SPF include and DKIM keys are removed under STD-AM-001 Section 3.10.

### 3.6 Inbound Email Filtering

Inbound mail is filtered for:

Malware, by scanning attachments with an anti-malware engine and, where the platform offers it, detonating attachments in a sandbox before delivery. Malicious links, by checking URLs at delivery and again when the user clicks, where the platform offers time-of-click protection. Spoofing and impersonation, by honoring the sender's DMARC policy and by protecting the names of executives and finance staff against display-name impersonation. Lookalike domains, by flagging or quarantining mail from domains that closely resemble [ORGANIZATION_NAME]'s own or its key vendors'.

High-risk attachment types are blocked from external senders by default: executables and scripts, disk image and installer files, macro-enabled Office documents, and shortcut files. Encrypted archives that cannot be scanned are quarantined for review. Business needs for any of these types go through the exception process.

Mail from external senders is visibly marked as external in the message.

### 3.7 Mailbox Rules and Forwarding

Automatic forwarding of mail to external addresses is blocked at the platform level, consistent with POL-AUP-001 Section 3.4. Exceptions are approved per mailbox and recorded.

New inbox rules that forward, redirect, delete, or move mail to rarely used folders generate alerts under STD-LOG-001, because those rules are the most common sign of a compromised mailbox being used for fraud. Delegated mailbox access and new mailbox permissions are logged and reviewed in the access review under POL-IAM-001 Section 3.3.

### 3.8 Phishing Reporting

Users have a one-click way to report suspicious messages from the mail client. Reported messages go to a monitored queue that the Information Security function or the security service provider reviews within one business day, and within one hour during business hours for reports that match an active campaign. Reporters receive a reply saying whether the message was malicious. Confirmed campaigns are handled under RUN-IR-001 Section 3.2.5.

### 3.9 Payment and Bank Detail Changes

Technical controls catch most fraud attempts, but business email compromise succeeds by making a legitimate-looking request to a person with authority to act. The final control is a process.

Requests to change a vendor's, employee's, or customer's bank or payment details are verified before they take effect, by calling the requester at a phone number already on file, not one supplied in the request. A verified change is recorded with who verified it, how, and when.

Payments above [PAYMENT_APPROVAL_THRESHOLD] require approval from two people. Requests for urgent or confidential payments outside the normal process are verified the same way, regardless of who appears to be asking, including requests by voice or video under POL-AI-001 Section 3.7.

**When a missed verification becomes an incident.** Not every slip in this process is an incident; a change entered before the callback, then verified and found legitimate, is a process finding. A payment detail change that was not verified is handled as a security incident under POL-IR-001 when any of these is true: money above [PAYMENT_INCIDENT_THRESHOLD, e.g., the dual-approval threshold] was sent to the new details; the request came from a lookalike domain, a mailbox that may be compromised, or a channel the requester does not normally use; the requester cannot confirm the change when reached at the number on file; or the change affects payroll or many payees at once. Below those conditions, the change is reversed or verified the same day and recorded as a process finding for the finance function to correct.

Staff in finance, accounts payable, payroll, and executive support receive specific training on these patterns at least annually under POL-GOV-001 Section 3.8.

### 3.10 Exceptions

Exceptions follow the process in POL-GOV-001 Section 3.6.

## 4. Roles and Responsibilities

**Information Security function.** Owns this standard. Reviews DMARC reports, phishing reports, and forwarding and inbox-rule alerts. Approves extensions and exceptions.

**IT function (or IT service provider).** Configures the email platform, filtering, browser policies, extension allowlist, and DNS records.

**Finance function.** Operates the payment-change verification and dual approval in Section 3.9.

**Domain owners.** Know which services send as their domains, and notify IT before adding a new one.

**All users.** Use approved browsers. Install only approved extensions. Report suspicious messages with the report button.

## 5. Enforcement

Specific remediation timelines:

Domains without SPF, DKIM, and DMARC records: published within thirty days of identification. DMARC not at enforcement by the target date: reviewed with the executive sponsor, with the remaining blockers and a revised target date documented. External auto-forwarding found enabled without an exception: disabled the same day and investigated as a possible compromise. Unapproved browser extensions on managed devices: removed within seven days. Payment details changed without verification: reversed or verified the same day, and handled as a security incident when the conditions in Section 3.9 apply.

## 6. Related Documents

POL-NET-001: Network Security Policy (DNS and URL filtering, extended to off-network devices by Section 3.4)
POL-EP-001: Endpoint Protection Policy (managed device configuration)
POL-AUP-001: Acceptable Use Policy (user email rules and software installation)
STD-IAM-001: Password and Authentication Standard (browser password storage)
STD-AM-001: SaaS Asset Management Standard (sending services and their retirement)
POL-AI-001: AI and Agent Governance Policy (AI extensions and impersonation verification)
POL-VM-001: Vulnerability Management Policy (browser update timelines)
STD-LOG-001: Logging and Monitoring Standard (inbox rule and forwarding alerts)
RUN-IR-001: Incident Response Runbook (business email compromise and phishing campaign playbooks)
POL-GOV-001: Information Security Policy (role-specific training and exceptions)

## 7. Framework Alignment

This standard supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.PS-01 (Configuration management practices are established and applied). PR.PS-05 (Installation and execution of unauthorized software are prevented). PR.DS-02 (The confidentiality, integrity, and availability of data-in-transit are protected). DE.CM-09 (Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events). PR.AT-02 (Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind).

**CIS Controls v8.1:**

Control 9 Email and Web Browser Protections: Safeguards 9.1 (ensure use of only fully supported browsers and email clients), 9.2 (use DNS filtering services), 9.3 (maintain and enforce network-based URL filters), 9.4 (restrict unnecessary or unauthorized browser and email client extensions), 9.5 (implement DMARC), 9.6 (block unnecessary file types), 9.7 (deploy and maintain email server anti-malware protections).

Control 14 Security Awareness and Skills Training: Safeguard 14.2 (train workforce members to recognize social engineering attacks), for the role-specific training in Section 3.9.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This standard is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
