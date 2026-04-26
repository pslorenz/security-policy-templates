# POL-AM-001: Asset Management Policy

| | |
|---|---|
| **Document ID** | POL-AM-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] tracks the things it owns, uses, and depends on. That includes computers, servers, network equipment, software, cloud platforms, SaaS applications, and the data that lives across all of them.

The reason this matters is straightforward. You cannot protect what you do not know you have. The vast majority of preventable security incidents start with an asset that nobody was actively managing. The forgotten server, the SaaS tool a department signed up for two years ago, the laptop that never got returned, the cloud subscription a former employee created. Each of these becomes a problem because nothing was tracking them.

The goal of asset management is not to maintain a perfect catalog. It is to make sure every asset has someone responsible for it, that the security program reaches every asset, and that nothing falls through the cracks.

## 2. Scope

This policy covers all assets that [ORGANIZATION_NAME] owns, leases, subscribes to, or depends on for business operations. Specifically:

**Hardware assets**: laptops, desktops, servers, mobile devices, tablets, network equipment (routers, switches, firewalls, access points), printers and multifunction devices, security cameras and physical security systems, and any other device connected to [ORGANIZATION_NAME] networks or storing [ORGANIZATION_NAME] data.

**Software assets**: operating systems, applications installed on company devices, browser extensions, command-line tools, software licenses, and software development kits.

**Cloud and SaaS assets**: Microsoft 365 or Google Workspace tenants, cloud platform subscriptions (Azure, AWS, GCP), SaaS applications used for company work (CRM, accounting, HR, project management, file sharing, anything else), and any service [ORGANIZATION_NAME] pays for or uses to operate the business.

**Data assets**: company data wherever it lives, including in cloud platforms, SaaS applications, on-premises servers, endpoints, and backup systems. The data classification policy ([DATA_CLASSIFICATION_POLICY], forthcoming) covers data handling requirements; this policy covers tracking where data lives.

**Identity assets**: user accounts and non-human identities. POL-IAM-001 (Access Control Policy) and POL-IAM-011 (Non-Human Identity Governance Policy) cover identity governance specifically; this policy ensures identities are part of the broader asset view.

The scope intentionally includes assets that [ORGANIZATION_NAME] does not own outright. A SaaS subscription is an asset even though the underlying software is not owned. A cloud-hosted server is an asset even though the hardware is not owned. The test is whether [ORGANIZATION_NAME] depends on it for business operations.

## 3. Policy Statements

### 3.1 Every Asset Has an Owner

Every asset in scope of this policy has a named owner. The owner is a current employee responsible for the asset's intended use, its security, and decisions about its lifecycle.

For hardware, the owner is typically the user the device is assigned to (for personal-use devices) or the department lead responsible for the system (for shared devices and infrastructure).

For software and cloud subscriptions, the owner is the person who requested or approved the procurement, or the department lead whose work depends on it.

For SaaS applications, the owner is the business sponsor of the tool, not the IT person who configured it.

For data, the owner is the department lead or business unit head responsible for the data's purpose. Specific implementation owners (the person who runs the system that stores the data) are tracked separately from the business owner of the data itself.

When the named owner leaves [ORGANIZATION_NAME] or changes roles, ownership is reassigned within thirty days. Assets without a named owner are flagged for review and either reassigned or decommissioned.

### 3.2 The Inventory Is Built From Runtime, Not Kept by Hand

[ORGANIZATION_NAME] maintains a current inventory of all assets in scope. The inventory is built from what the existing tools already see, not from a separately maintained spreadsheet.

For hardware, the sources of truth are:

The endpoint detection and response (EDR) platform, which sees every managed device. The remote management and monitoring (RMM) platform, where used. The Microsoft Entra device list, the Intune or equivalent device management system, and the network access control system if one is in place.

For software, the sources are:

The endpoint management platform's inventory of installed applications. The license management system, where one exists. The SaaS management platform, where one is in use.

For cloud and SaaS assets, the sources are:

The cloud platform's resource inventory APIs (Azure Resource Graph, AWS Config, GCP Asset Inventory). The Microsoft 365 admin centers and equivalent for other identity providers. The procurement records for SaaS subscriptions. The Cloud App Discovery feature in Microsoft Defender for Cloud Apps or equivalent CASB capability.

The inventory is consolidated into a single view that the IT or Information Security function can query. Smaller environments use a CSV-based approach combined with the platform-native inventory tools. Larger environments may invest in a Cyber Asset Attack Surface Management (CAASM) tool to consolidate the views automatically.

Manual entries (assets not picked up by any of the runtime sources) are minimized. When manual entries are necessary, they are documented with the reason the asset is not visible to runtime tools.

### 3.3 The Inventory Is Refreshed Continuously, Reconciled Quarterly

The inventory updates as the runtime tools update. The EDR platform sees a new device and the inventory reflects it within hours, not weeks.

Each quarter, the inventory is reconciled. The reconciliation looks for:

Assets that appear in the inventory but cannot be located or contacted (potentially lost or stolen, potentially decommissioned without proper process). Assets that exist in the environment but are not in the inventory (something was provisioned outside the standard process). Assets with no named owner. Assets owned by departed employees whose ownership was not reassigned. SaaS subscriptions that show up in expense reports or shadow IT discovery but are not in the formal inventory.

Findings from the quarterly reconciliation are remediated within thirty days. The reconciliation report is provided to the Information Security function each quarter.

### 3.4 New Assets Are Added Through a Defined Process

When new assets enter [ORGANIZATION_NAME]:

**Hardware** is provisioned through the IT or IT service provider process. Devices are enrolled in the device management system before being given to users. Pre-enrollment delivery (the IT team handing a user a laptop and asking them to enroll it later) is not the standard path because users forget and devices remain unmanaged.

**Software** is requested through the approved process described in POL-AUP-001 (Acceptable Use Policy) Section 3.8. Approved software is added to the software inventory at the time of approval.

**Cloud and SaaS subscriptions** go through procurement with security review. The security review confirms federation support, data handling practices, and integration patterns. New SaaS subscriptions are added to the inventory at the time of procurement, with the named business owner recorded.

**Identities** follow the provisioning process described in POL-IAM-001 and POL-IAM-011 for human and non-human identities respectively.

Assets that arrive outside the standard process (a department signs up for a SaaS tool, a contractor brings in their own equipment, a developer provisions cloud resources without going through procurement) are still in scope. When discovered, they are either brought into the standard process or removed.

### 3.5 Assets Are Removed Cleanly When No Longer Needed

When an asset reaches the end of its useful life, it is removed from service through a documented process. The process protects [ORGANIZATION_NAME] data and removes the asset's footprint from the environment.

For hardware:

Devices are wiped before disposal, recycling, or transfer. The wipe meets the standard appropriate to the data the device may have stored. Confidential and restricted data classifications require a cryptographic wipe or physical destruction of storage media. Devices that are returned to a vendor (lease return, warranty replacement) are wiped before return. Devices that are reassigned to another user are wiped and reimaged. Decommissioned devices are removed from the inventory, the device management system, and any other systems where they appear.

For software:

Removed software has its license deactivated where applicable. The software is uninstalled from any devices where it remains. Subscriptions are canceled. Renewal dates are reviewed before the subscription auto-renews.

For cloud and SaaS:

Subscriptions are canceled through proper channels, not just abandoned. Data is exported or deleted as appropriate to retention policies. Service accounts and API keys associated with the subscription are deactivated and rotated where they had access to other systems. The subscription is removed from the inventory.

For identities:

Removal follows POL-IAM-001 Section 3.4 (for human identities) and POL-IAM-011 Section 3.7 (for non-human identities).

### 3.6 Cloud Subscriptions and SaaS Receive Special Attention

Cloud and SaaS assets are the assets most often missed in SMB environments because they do not appear in the same inventory as hardware. They are also the assets most likely to hold the largest amount of sensitive data.

Specific requirements for cloud and SaaS:

The IT or Information Security function maintains a list of approved SaaS applications. Departments using applications outside the approved list are identified and either bring the application into approval or migrate to an approved alternative.

Each cloud subscription (Azure, AWS, GCP, others) has a named owner, a documented purpose, and a billing relationship that is tracked. Cloud subscriptions provisioned for short-term projects are decommissioned when the project ends.

SaaS subscriptions used for business-critical work are integrated with the identity provider per POL-IAM-006 (Single Sign-On and Federation Standard) where the platform supports it. SaaS subscriptions that cannot be federated are reviewed for replacement on a defined timeline.

The annual subscription review (often performed alongside budget planning) is the natural moment for the SaaS inventory to be refreshed. Renewals that no longer serve a clear purpose are not renewed.

### 3.7 Assets Are Classified by Criticality

Not all assets are equally important. The asset inventory tracks a criticality level for each asset to support risk-based decisions about protection, monitoring, and response.

Criticality levels for [ORGANIZATION_NAME]:

**Critical**: Assets whose compromise or loss would cause major disruption to business operations. Examples include the production identity provider, primary file storage, financial systems, and any system holding restricted data.

**Important**: Assets whose compromise or loss would cause meaningful disruption. Examples include departmental SaaS tools, secondary infrastructure, and any system holding confidential data.

**Standard**: Assets whose compromise or loss would cause limited disruption. Examples include endpoint devices for non-privileged users and SaaS tools with limited scope.

The classification is reviewed annually. The classification informs the security controls applied to the asset, the priority of patching and remediation, and the response priority during incidents.

### 3.8 Physical Asset Tracking

Hardware that is physically portable (laptops, tablets, hardware security keys, USB drives, external monitors with company data on them in some configurations) is tracked through the device assignment process. The user receiving the device acknowledges receipt at the time of assignment.

Lost or stolen devices are reported immediately to the IT or Information Security function. Reported losses trigger:

Remote wipe of the device through the device management system. Disabling of any accounts that the device had cached. Review of any data the device is known to have stored. Reporting to authorities where appropriate (theft, regulatory requirements, insurance claims).

Annual physical asset audits compare the inventory against actual locations for assets not visible to remote management. This is most relevant for assets that have been deployed to remote sites, given to contractors, or stored in inventory.

### 3.9 Documentation of Critical Assets

For assets classified as Critical (Section 3.7), additional documentation is maintained beyond what is in the standard inventory.

Critical assets have documented:

Configuration details and dependencies. Backup and recovery procedures. Vendor contacts and support arrangements. Disaster recovery considerations. The named technical owner (for technical execution) in addition to the business owner.

The documentation is stored in a location accessible to the IT and Information Security function during incidents. Documentation that lives only in the head of one person is fragile.

### 3.10 Exceptions

Some assets cannot be brought fully under this policy. Recognizing this is honest, not weak. The exception process documents what is excepted, why, and what compensating controls are in place.

Common situations requiring exceptions:

Specialized equipment that cannot be enrolled in the standard device management system (industrial control equipment, certain medical devices, some legacy hardware). Vendor-managed assets where [ORGANIZATION_NAME] does not control the device but depends on its operation. Personal devices used in BYOD arrangements where company control is limited by design.

For each exception, the compensating controls include a documented owner, explicit understanding of the residual risk, and any technical isolation that limits the asset's exposure. Exceptions are reviewed quarterly per POL-IAM-001 Section 3.10.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Conducts the quarterly inventory reconciliation. Reviews and approves exceptions. Sets the criticality classification standards.

**IT function (or IT service provider).** Maintains the technical inventory tools. Provisions and decommissions hardware and software. Implements the device management and endpoint security tooling that feeds the inventory.

**Procurement function (or whoever approves SaaS purchases).** Confirms that proposed cloud and SaaS subscriptions go through security review. Records the named owner at the time of procurement.

**Department leads and asset owners.** Serve as the named owner for assets in their area. Notify IT or Information Security when assets are no longer needed. Cooperate with quarterly reconciliation efforts.

**All users.** Cooperate with device enrollment processes. Return company-issued equipment promptly upon role change or departure. Report lost or stolen devices immediately. Do not provision SaaS or cloud subscriptions outside the approved process.

## 5. Enforcement

Violations of this policy may result in:

Loss of authority to provision new assets without review. Escalation to the responsible department lead. For repeated or willful violations, formal disciplinary action consistent with HR policies.

Specific remediation timelines:

Assets without a named owner: documented and assigned within thirty days of identification.

Assets in the environment but not in the inventory: investigated and either inventoried or removed within sixty days of discovery.

SaaS subscriptions outside the approved list: brought into approval or migrated to an approved alternative within ninety days.

Decommissioned devices found still active: investigated and either reactivated through proper process or fully decommissioned within fourteen days.

Lost or stolen devices: reported and remote-wiped immediately upon discovery.

## 6. Related Documents

POL-IAM-001: Access Control Policy
POL-IAM-006: Single Sign-On and Federation Standard
POL-IAM-011: Non-Human Identity Governance Policy
POL-AUP-001: Acceptable Use Policy
POL-DC-001: Data Classification and Handling Policy (forthcoming)
POL-VM-001: Vulnerability Management Policy (forthcoming, depends on the asset inventory)
POL-IR-001: Incident Response Policy (forthcoming)
POL-EP-001: Endpoint Protection Policy (forthcoming)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

ID.AM-01 (Inventories of hardware managed by the organization are maintained). ID.AM-02 (Inventories of software, services, and systems managed by the organization are maintained). ID.AM-04 (Inventories of services provided by suppliers are maintained). ID.AM-05 (Resources are prioritized based on classification, criticality, resources, and impact on the mission). ID.AM-08 (Systems, hardware, software, services, and data are managed throughout their life cycles).

**CIS Controls v8:**

Control 1 Inventory and Control of Enterprise Assets: Safeguards 1.1 (establish and maintain a detailed enterprise asset inventory), 1.2 (address unauthorized assets), 1.3 (utilize an active discovery tool), 1.4 (use DHCP logging to update enterprise asset inventory), 1.5 (use a passive asset discovery tool).

Control 2 Inventory and Control of Software Assets: Safeguards 2.1 (establish and maintain a software inventory), 2.2 (ensure authorized software is currently supported), 2.3 (address unauthorized software), 2.4 (utilize automated software inventory tools), 2.5 (allowlist authorized software), 2.6 (allowlist authorized libraries), 2.7 (allowlist authorized scripts).

Control 15 Service Provider Management: Selected safeguards related to inventorying third-party services.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above. Adopted from `github.com/pslorenz/security-policy-templates`, distributed under Creative Commons Attribution-ShareAlike 4.0.*
