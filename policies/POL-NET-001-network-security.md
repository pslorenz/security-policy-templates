# POL-NET-001: Network Security Policy

| | |
|---|---|
| **Document ID** | POL-NET-001 |
| **Version** | 1.0 |
| **Effective Date** | [EFFECTIVE_DATE] |
| **Review Cycle** | Annual |
| **Owner** | [POLICY_OWNER] |
| **Approver** | [EXECUTIVE_SPONSOR] |
| **Classification** | Internal |

---

## 1. Purpose

This policy defines how [ORGANIZATION_NAME] secures its networks. It covers the office networks where employees work, the cloud networks where company resources are hosted, the wireless networks employees and guests use, and the connections between them.

The reason network security matters today is different from the reason it mattered ten years ago. The old model assumed a strong network perimeter with trusted internal networks behind it. That model has not held up. Modern SMB environments have employees working from home, cloud-hosted resources, SaaS applications outside any network the organization controls, and identity-based access patterns that do not depend on network location. The network perimeter is no longer the primary line of defense.

What network security still does in this world: it segments the environment so that a compromise in one place does not become a compromise everywhere. It controls the egress paths that ransomware and data exfiltration depend on. It provides visibility into what is talking to what. It protects the office and cloud networks where physical or platform-level access matters. These are real defensive controls, even though they are no longer the primary perimeter.

This policy works alongside POL-IAM-002 (Remote Access Policy), which addresses how users connect to company resources from outside, and POL-AM-001 (Asset Management Policy), which tracks the network equipment itself.

## 2. Scope

This policy applies to all networks operated by or used to access [ORGANIZATION_NAME] systems. Specifically:

Office networks at company locations, including wired and wireless segments. Cloud platform virtual networks (Azure VNets, AWS VPCs, GCP VPC networks, equivalent). Network equipment owned or operated by [ORGANIZATION_NAME] (firewalls, switches, routers, wireless access points, load balancers). Connections between [ORGANIZATION_NAME]'s networks and external networks, including internet egress and any direct connections to vendors or partners. Guest network segments where present.

It does not cover the remote access path from external networks to [ORGANIZATION_NAME] resources, which is addressed in POL-IAM-002. It does not cover endpoint-level network controls (host firewalls, EDR network telemetry), which are addressed in POL-EP-001.

## 3. Policy Statements

### 3.1 Segmentation Is the Primary Network Control

[ORGANIZATION_NAME] segments its networks so that a compromise in one segment does not become a compromise across the entire environment. Segmentation is the network control that most reliably limits damage when other controls fail.

For office networks, the minimum segmentation:

A user segment for employee devices. A guest segment for visitor and BYOD devices, with no access to internal resources. A separate segment for printers, conference room equipment, and other office infrastructure. A separate segment for any production servers, lab equipment, or specialized devices.

The segments are isolated from each other by default. Traffic between segments is permitted only when there is a documented reason, and the permitted paths are configured explicitly rather than allowed by default.

For cloud platform networks, segmentation follows the platform's native constructs. In Azure, this means separate virtual networks or subnets with network security groups controlling traffic between them. In AWS, this means separate VPCs or subnets with security groups and NACLs. In GCP, this means separate VPC networks or subnets with firewall rules. The default is deny; permitted paths are explicit.

For environments with sensitive workloads (production systems, systems holding Restricted data, financial systems), additional segmentation isolates those workloads from the general environment. The isolation includes both network controls and identity controls, consistent with POL-IAM-001 and POL-DC-001.

The IT function maintains network architecture diagrams for office and cloud networks, showing segments, the permitted paths between them, and connections to external parties. The diagrams are reviewed annually and after significant changes.

Flat networks where everything can reach everything are not acceptable. Existing flat networks are migrated to a segmented model on a documented timeline, typically twelve to eighteen months from policy adoption.

### 3.2 Edge Security

The connection between [ORGANIZATION_NAME] networks and the internet is protected by appropriate edge security controls.

For office networks, this means:

A firewall at the network edge, with deny-by-default ingress rules and explicit egress rules. The firewall is from a current, supported vendor and runs current firmware. Approved firewalls for [ORGANIZATION_NAME] are [APPROVED_FIREWALL_VENDORS, e.g., a business-class firewall with intrusion prevention, centralized management, and a published firmware support lifecycle]. Intrusion prevention or threat detection capabilities, where the firewall platform supports them, configured to inspect traffic for known threats. DNS filtering at the network level, blocking known-malicious domains and providing visibility into lookup patterns. Approved DNS filtering services include [APPROVED_DNS_FILTERING, e.g., a protective DNS service that blocks known-malicious domains and logs queries per device]. Geographic filtering where appropriate, blocking traffic from regions where [ORGANIZATION_NAME] does not operate or where threat patterns warrant restriction.

For cloud networks, edge security means:

The cloud platform's native firewall and DDoS protection capabilities are enabled. Public-facing cloud resources are minimized; resources that do not need to be public are not exposed to the internet. Where public access is required, the access is gated through application-layer controls (web application firewalls, API gateways) rather than direct exposure of underlying infrastructure.

The configurations are reviewed quarterly to confirm they remain appropriate. STD-NET-001 extends DNS and web filtering to managed devices off the office network and sets the email protection requirements.

### 3.3 Egress Filtering

Outbound network traffic is controlled, not just inbound. Many security incidents are detected or prevented at the egress point: ransomware reaching command-and-control infrastructure, data exfiltration to attacker-controlled destinations, malware downloading additional payloads.

Egress controls:

Default egress rules deny outbound traffic to known-malicious destinations. The malicious destination list is updated continuously through the firewall vendor's threat feed and any additional threat intelligence sources in use.

Egress to high-risk destination categories (file sharing services not approved for company use, anonymization services, peer-to-peer file sharing, cryptocurrency mining pools) is blocked unless there is a documented business reason.

Egress to specific destinations required for normal business operations (Microsoft 365 endpoints, approved SaaS platforms, cloud platforms) is explicitly permitted and monitored.

DNS egress is restricted to the organization's approved DNS resolvers. Endpoints attempting to use other DNS resolvers are flagged.

For workloads in cloud platforms, egress filtering applies the same principle: outbound traffic is restricted to known-required destinations, and egress to unexpected destinations is logged or blocked.

The first month of egress filtering implementation typically surfaces previously-unknown dependencies, which the operations team adjusts for. This is a known cost of the control and is worth the resulting protection.

### 3.4 Wireless Networks

Wireless networks at [ORGANIZATION_NAME] locations are configured to standards appropriate to their purpose.

**Corporate wireless** (the network employees use for work) requires:

WPA3 authentication where supported, with WPA2 with strong configuration as a fallback for older devices. Authentication tied to the corporate identity provider where possible, using 802.1X with EAP-TLS or equivalent. Otherwise, a strong shared key changed on a defined schedule and when employees with knowledge of the key leave the organization. Connection only by managed devices that meet the requirements in POL-EP-001. Visibility into connected devices through the wireless management platform.

**Guest wireless** (the network visitors use) requires:

Separation from the corporate network with no access to internal resources. Encryption and authentication appropriate to the visitor population: a shared key, Wi-Fi Enhanced Open (OWE) where supported, or sponsored access, optionally combined with a captive portal for terms acceptance. A click-through captive portal on its own does not encrypt traffic. Bandwidth limits to prevent guest use from affecting corporate operations.

**IoT wireless** (the network for cameras, smart equipment, conference room devices) requires:

Separation from both corporate and guest networks. Restrictive firewall rules limiting what IoT devices can reach. Inventory tracking through POL-AM-001.

Open wireless networks without encryption are not permitted on [ORGANIZATION_NAME] property, including guest networks.

### 3.5 Network Equipment Configuration

Network equipment (firewalls, switches, routers, access points) is configured according to the security baselines appropriate to the equipment type and vendor.

Specific requirements:

Default vendor credentials are changed before equipment is placed in service. Default credentials are not used in production under any circumstance.

Administrative access to network equipment requires authentication consistent with STD-IAM-001, including MFA for any access from networks other than the device's management network.

Management interfaces are not exposed to the internet. Management is performed from internal management networks or through the approved remote access tools described in POL-IAM-002.

Network equipment runs current firmware. Security updates are applied on the priority cadences in POL-VM-001 Section 3.3. Edge devices (firewalls, VPN gateways, and anything else reachable from the internet) are treated as internet-facing under POL-VM-001 Section 3.5, because they are among the most frequently exploited assets.

Configurations are backed up regularly. Backups are stored in a location accessible during incident response. Configuration changes are logged.

End-of-life network equipment is replaced rather than continuing in service without security updates. The replacement timeline is documented in the asset management records.

### 3.6 Network Logging and Monitoring

Network activity is logged to support detection and incident response. The logging covers:

Firewall traffic logs, including blocked and permitted connections. DNS query logs, including queries to malicious or suspicious domains. Wireless authentication and association events. Network equipment authentication and configuration change events. Egress traffic patterns sufficient to identify anomalies.

Logs are sent to the central logging platform within fifteen minutes of the event. Local logs on network equipment are retained for at least seven days as a backup. Centralized logs are retained per STD-LOG-001.

Monitoring focuses on patterns that indicate compromise:

Egress to known-malicious destinations or unusual destinations. Lateral movement patterns within the network. Authentication anomalies on wireless and management interfaces. Traffic patterns characteristic of data exfiltration (large transfers to unexpected destinations, transfers outside normal hours, transfers to anonymization services).

Alerts go through the security operations process documented in POL-IR-001.

### 3.7 Direct Connections to External Parties

[ORGANIZATION_NAME] occasionally maintains direct network connections to external parties (vendor management networks, partner integrations, dedicated connections to cloud providers). These connections require additional controls:

The connection is documented with the named owner, the business reason, the systems on each end, and the traffic permitted to flow.

The connection is restricted to the specific traffic required for the business reason. Broader access is not permitted by the connection itself.

The connection is reviewed annually. Connections that no longer serve a documented purpose are removed.

The connection is monitored consistent with the rest of the network. Suspicious activity through the connection is treated as it would be from any other source.

For SMB environments, direct connections of this kind are uncommon. Most external connectivity flows over the internet with appropriate authentication and encryption. When direct connections are warranted, they get explicit treatment.

### 3.8 Cloud Network Configuration

Cloud platform networks (Azure VNets, AWS VPCs, GCP VPC networks) follow security baselines appropriate to the platform.

Common requirements:

Resources are placed in the appropriate network segment based on their function and sensitivity. Production resources are not in the same segment as development or testing resources.

Network security groups, security groups, or firewall rules are configured with deny-by-default. Permitted traffic is explicit.

Public IP addresses are assigned only to resources that need them. Public-facing resources sit behind appropriate edge controls (load balancers, application gateways, web application firewalls).

Network flow logs are enabled and forwarded to the central logging platform.

Service endpoints, private endpoints, or private connectivity (Azure Private Link, AWS PrivateLink, GCP Private Service Connect) are used to keep traffic to platform services off the public internet where the platform supports it.

The cloud platform's native security recommendations are reviewed monthly and addressed consistent with POL-VM-001.

### 3.9 Wireless and Network Visibility

[ORGANIZATION_NAME] maintains visibility into devices connecting to its networks. The visibility supports both security operations and asset management.

Network visibility tools include:

The wireless management platform, which sees all wireless connections. The wired network management platform or switch infrastructure, which sees connected devices on wired ports. The cloud platform's resource inventory, which sees all resources in cloud networks. Network access control systems, where deployed.

Devices connecting to the network without authorization are flagged. Investigation determines whether the device is legitimate (in which case it is brought into the standard provisioning process) or unauthorized (in which case it is removed).

The asset inventory is updated based on the network visibility tools, consistent with POL-AM-001 Section 3.2's runtime-truth principle.

### 3.10 Exceptions

Specific situations may require deviation from the standard requirements:

Specialized equipment that requires non-standard network configuration (industrial control systems, certain medical devices, vendor-managed equipment). The exception documents the requirement and the compensating controls.

Legacy systems that cannot meet current segmentation or authentication requirements. The exception documents the planned remediation timeline.

Temporary configurations during migrations or implementations. The exception documents the expected duration.

Exceptions follow the process in POL-IAM-001 Section 3.10. No exception runs longer than twelve months without renewal. All active exceptions are reviewed quarterly.

## 4. Roles and Responsibilities

**Information Security function.** Owns this policy. Reviews network configurations against the requirements. Investigates network anomalies. Approves exceptions.

**IT function (or IT service provider).** Implements and maintains the network equipment. Configures the segmentation, firewall rules, and wireless networks. Performs the patching and updates. Maintains the logging configuration.

**Cloud platform owners.** Configure cloud network security consistent with this policy. Maintain the cloud network logging and monitoring. Address cloud platform security recommendations.

**System and asset owners.** Identify network requirements for their systems. Approve network changes affecting their systems. Cooperate with quarterly review activities.

**All employees and contractors.** Connect only authorized devices to [ORGANIZATION_NAME] networks. Do not attempt to bypass network controls. Report suspected network issues or unauthorized devices.

## 5. Enforcement

Violations of this policy may result in loss of network access, escalation to the responsible owner, and disciplinary action consistent with HR policies. For deliberate violations involving bypass of network controls or installation of unauthorized network equipment, the violations are treated as security incidents under POL-IR-001.

Specific remediation timelines:

Flat networks identified during review: migration plan documented within sixty days, migration completed within eighteen months.

Default credentials on network equipment: changed within seven days of identification.

Network equipment running outdated firmware: updated on the POL-VM-001 cadence for the vulnerability's priority.

Unauthorized devices on the network: investigated and either authorized through the standard process or removed within fourteen days.

Open wireless networks without authentication: secured within seven days of identification.

## 6. Related Documents

POL-IAM-001: Access Control Policy
POL-IAM-002: Remote Access Policy (the user remote access path this policy does not cover)
POL-AM-001: Asset Management Policy (network equipment inventory)
POL-DC-001: Data Classification and Handling Policy (data sensitivity informs segmentation)
POL-EP-001: Endpoint Protection Policy (host-level network controls)
POL-VM-001: Vulnerability Management Policy (network equipment patching)
POL-IR-001: Incident Response Policy (response to network compromise)
STD-LOG-001: Logging and Monitoring Standard (log retention)
STD-NET-001: Email and Web Browser Protection Standard (filtering off-network, email authentication, and browser controls)
STD-OPS-001: Change Management Standard (firewall and network configuration changes)

## 7. Framework Alignment

This policy supports the following controls.

**NIST Cybersecurity Framework 2.0:**

PR.IR-01 (Networks and environments are protected from unauthorized logical access and usage). PR.PS-01 (Configuration management practices are established and applied). DE.CM-01 (Networks and network services are monitored to find potentially adverse events). DE.CM-06 (External service provider activities and services are monitored to find potentially adverse events).

**CIS Controls v8.1:**

Control 4 Secure Configuration of Enterprise Assets and Software: Safeguard 4.2 (establish and maintain a secure configuration process for network infrastructure), through Section 3.5.

Control 9 Email and Web Browser Protections: Safeguards 9.2 (use DNS filtering services) and 9.3 (maintain and enforce network-based URL filters), through Sections 3.2 and 3.3.

Control 12 Network Infrastructure Management: Safeguards 12.1 (ensure network infrastructure is up-to-date), 12.2 (establish and maintain a secure network architecture), 12.3 (securely manage network infrastructure), 12.4 (establish and maintain architecture diagram(s)), 12.5 (centralize network authentication, authorization, and auditing), 12.6 (use of secure network management and communication protocols). Remote access (12.7) is covered by POL-IAM-002.

Control 13 Network Monitoring and Defense: Safeguards 13.1 (centralize security event alerting), 13.3 (deploy a network intrusion detection solution), 13.4 (perform traffic filtering between network segments), 13.6 (collect network traffic flow logs). Host-based detection (13.2) is covered by POL-EP-001, and remote asset access control (13.5) by POL-IAM-002.

## 8. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [POLICY_OWNER] | Initial publication. |

---

*This policy is issued under the authority of the executive sponsor listed above.*

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
