# WM-ORG-014 selected primary-source preparation

Publication transport check: SRC-001 through SRC-005 returned HTTP 200 to HEAD;
SRC-006 direct HEAD was unavailable. Its earlier inspected text remains the
basis of the timestamp design; this probe is not a source-content revalidation.
All exact release/license/full-constraint holds remain open.

Inspected 2026-09-09 UTC (2026-09-10 local). Proposed Vercy structure, not a
universal vendor schema. Source release/license/complete constraint holds remain.

## SRC-001 TM Forum TMF629 Customer Management
https://raw.githubusercontent.com/tmforum-apis/TMF629_CustomerManagement/main/TMF629-Customer_Management-v5.0.1.oas.yaml

Header version 5.0.1; selected AccountRef, PartyRole, engagedParty, status/reason,
validFor and customer examples inspected. A role is contextual; account and
agreement are referenced. Mutable main must be pinned to a commit for executable
mapping. Full discriminator/required-field graph and normative conformance not
verified. Forum community opinions are discovery only, not admitted evidence.

## SRC-002 Microsoft Dynamics customer entities
https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/customer-entities-account-contact?view=op-9-1

On-premises 9.1 documentation. Selected account hierarchy clauses inspected:
one parent account and multiple children/contacts in this implementation. It is
not a universal legal hierarchy or a mandate to conflate party and CRM record.
Publication date and full contact mapping remain to verify.

## SRC-003 Microsoft Dataverse Account reference
https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/account

Selected DoNotEMail field inspected: boolean preference with permissive default.
Vercy design inference: source preference/default cannot itself establish lawful
authority or consent for communication. Full schema, lifecycle and license pins
remain pending; no legal advice or automatic outreach rule is asserted.

## SRC-004 Stripe Customer object
https://docs.stripe.com/api/customers/object

Selected public customer fields including nullable email and current discount
inspected. Billing platform customer object is a scoped integration record, not
a universal CRM party. API release is not pinned; only selected object fields
were inspected. Do not import payment instruments or infer customer identity
from email alone. Full billing, deletion and subscription rules unreviewed.

## SRC-005 W3C PROV-O
https://www.w3.org/TR/prov-o/

Provenance vocabulary clauses inspected earlier in this dialogue: attributed
record changes and derivation. Reuse as conceptual provenance alignment, not
proof of customer state or access permission. Exact dated pin remains pending.

## SRC-006 IETF RFC 3339
https://www.rfc-editor.org/rfc/rfc3339

July 2002, timestamp grammar/examples inspected earlier in this dialogue.
Seconds and explicit offset for observation/recording instants; preserve source
date precision and separate identity. Edge-case runtime fixtures remain pending.

## Former dossier

Read stream-06 codex-preflight.md as untrusted preparation only. Empty relation
ledger means proposed sibling links are not approved edges. Generic organization
sources were not adopted as customer-domain research. Scope follows registry:
CRM relationship lifecycle, not party identity. No provider attribution copied.

## Risks and remaining verification

Different sources overload account/customer differently. Keep kind, seller scope,
related-party roles, billing references and source definitions explicit. No
universal active/dormant/closed state machine, legal hierarchy, creditworthiness
or consent rule is claimed. Vendor evidence illustrates mappings and counter-
examples; it does not mandate every proposed field. Later synthesis needs
independent-review, runtime, license and source-version holds.
