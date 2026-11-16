# TPL-BC-001: Business Continuity Plan

| | |
|---|---|
| **Document ID** | TPL-BC-001 |
| **Version** | 1.0 |
| **Supports** | POL-BC-001 Sections 3.1 through 3.6 |
| **Owner** | [CONTINUITY_LEAD] |
| **Organization** | [ORGANIZATION_NAME] |
| **Classification** | Confidential |

---

## How to use this template

This template is [ORGANIZATION_NAME]'s business continuity plan under POL-BC-001. Fill it in once, keep it current, and keep an offline copy where the continuity lead and deputy can reach it without the office or company systems: a printed copy, and an encrypted copy on a personal device or in storage outside the company tenant.

Keep it short. A plan nobody can read in a crisis does not help. If a section grows past a page, move the detail to a linked document and leave a summary here.

The plan is Confidential because it holds contact details and describes the organization's dependencies. It contains no passwords; Section 4 says where credentials are held, not what they are.

---

## 1. Activation

| | |
|---|---|
| **Continuity lead** | [CONTINUITY_LEAD] |
| **Deputy** | [CONTINUITY_DEPUTY] |
| **If neither is reachable within** | [CONTINUITY_ESCALATION_TIME], the most senior available manager acts |
| **Out-of-band staff channel** | |
| **Where offline copies of this plan are kept** | |

**Declare a continuity event when** a critical function in Section 2 has stopped, or will stop, for longer than half its maximum tolerable downtime, or when a loss in Section 3 has happened. When in doubt, declare. Standing down is easy.

**First steps after declaring:**

Confirm everyone is safe. Tell staff through the out-of-band channel what has happened and what to do now. Identify which critical functions are affected, and start their workarounds from Section 2. If the cause is or may be a security incident, start POL-IR-001 at the same time. Note the time and keep a short log of decisions.

---

## 2. Critical Business Functions

One row per function. The maximum tolerable downtime is the business owner's judgment of how long the function can stop before the harm becomes unacceptable.

| Function | Owner | Backup person | Maximum tolerable downtime | Systems it needs | People it needs | Vendors it needs | Facility it needs | Workaround while dependencies are down |
|---|---|---|---|---|---|---|---|---|
| [FUNCTION, e.g., client billing] | | | | | | | | |

**Check against STD-DR-001:** for each system listed, its recovery time objective is shorter than the maximum tolerable downtime of every function that needs it, or the workaround covers the difference.

---

## 3. Loss Scenarios

| Loss | Immediate actions | Who | Functions affected | How long the workarounds can last |
|---|---|---|---|---|
| Office unavailable | Staff work from home or [ALTERNATE_LOCATION]. Forward office phones. Retrieve equipment if safe. | | | |
| Key system or SaaS application down | Start the function workarounds in Section 2. Contact the vendor or IT provider. Restore under STD-DR-001 if data is affected. | | | |
| Key person unavailable | Backup person takes over the function. Successor access to credentials (Section 4). | | | |
| Key vendor unavailable | Use the fallback in Section 5. Contact the alternate vendor if one is pre-arranged. | | | |
| Power or internet down | Switch to the backup connection. Move work to locations with power if needed. | | | |

---

## 4. Credentials and Access

Where the organization's own access lives, so that the business is not locked out if a person or the IT provider is unavailable. Record locations and holders only, never the credentials themselves.

| Access | Held by | Where it is stored | Successor or second holder | Last confirmed working |
|---|---|---|---|---|
| Break-glass accounts for the identity provider (POL-IAM-001 Section 3.7) | | | | |
| Domain registrar and DNS | | | | |
| Bank and payroll | | | | |
| Productivity platform administrator | | | | |
| Backup system administrator (STD-DR-001 Section 3.4) | | | | |
| Key vendor portals | | | | |

---

## 5. Key Vendors

| Vendor | What they provide | Functions that depend on them | Support contact | Contract or account reference | Fallback if unavailable for a day | Fallback if unavailable for a week or more | Transition terms in contract |
|---|---|---|---|---|---|---|---|
| IT or security service provider | | | | | | | Yes / No |
| Internet service provider | | | | | | | |
| [VENDOR] | | | | | | | |

---

## 6. Contacts

| Name | Role in this plan | Mobile | Personal email | Alternate contact |
|---|---|---|---|---|
| | Continuity lead | | | |
| | Deputy | | | |
| | | | | |

Keep the full staff list with the offline copy. Personal contact details are used only for continuity and incident events.

---

## 7. Message Templates

**To staff (first message):**

```
[ORGANIZATION_NAME] update: [WHAT_HAPPENED, one sentence].
What to do now: [INSTRUCTIONS, e.g., work from home today; do not come to the office].
Next update by [TIME] through this channel.
Questions: [CONTACT].
```

**To clients:**

```
We are experiencing [BRIEF_DESCRIPTION] that may affect [SERVICE].
[CLIENT_EXPECTATIONS, e.g., responses may be slower than usual].
We will update you by [TIME]. For urgent matters, contact [CONTACT].
```

If the disruption is caused by a security incident, client messages follow POL-IR-001 Section 3.6 and are approved before sending.

**To vendors:**

```
[ORGANIZATION_NAME] is operating under its continuity plan because of [BRIEF_DESCRIPTION].
Please direct communications to [CONTACT] until further notice.
```

---

## 8. Single Points of Failure

Anything that would stop a critical function if one person, system, vendor, or connection were lost, and what is being done about it.

| Single point of failure | Functions affected | Fallback in place (Yes / No) | Planned fix | Owner | Target date |
|---|---|---|---|---|---|
| | | | | | |

---

## 9. Test Record

| Date | Type (tabletop / walkthrough / live) | Scenario | Participants | What worked | Findings | Owner and target date |
|---|---|---|---|---|---|---|
| | | | | | | |

---

## 10. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [EFFECTIVE_DATE] | [CONTINUITY_LEAD] | Initial plan. |

---

*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). Organizations adopting this document for their own use may remove this line.*
