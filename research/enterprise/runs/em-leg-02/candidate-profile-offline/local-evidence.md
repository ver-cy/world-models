# EM-LEG-02 local synthesis

## Disposition

- Reuse WM-POL-001 as the master for external legal instruments, provisions and normalized norms. ExternalRequirement and NormVersion are profile concepts inside that boundary.
- Profile WM-ACT-034 for Applicability Assessment. The assessment has its own record identity, but its semantics and lifecycle do not justify a new model identifier.
- Reference jurisdiction from the enterprise place/polity/authority master. A bare jurisdiction code is insufficient; no identifier is allocated here.
- Reuse WM-KNW-012 for attributable internal interpretations or operational rules derived from a pinned legal source, and WM-XCT-029 for instantiated duties. Neither replaces the external norm.
- Allocate no new runtime/model identifier.

## Identity and mastership

WM-POL-001 keeps five distinct identities: legal work, language/version expression, manifestation or official source copy, addressable provision, and normalized norm identity across amendments. Citation text, title, URL and file hash are locators or evidence, never identity.

An enterprise interpretation is a separate WM-KNW-012 statement that pins the source work, expression and provision and records author, fidelity and limitations. It must never overwrite or masquerade as source text. Consolidations and translations retain their derivation, cutoff, authentication and authority class.

## Time and change

Publication or promulgation, commencement, applicability or efficacy, transitional/compliance deadline, repeal/supersession and record/knowledge time are separate axes. Commencement can be provision-specific or conditional. A deadline belongs to a derived obligation and retains its event basis, offset, timezone and business-day convention.

Amendment, correction, substitution and renumbering preserve historic addressability. A future expression can be published while the prior expression remains in force. Historic versions remain citable.

## Exceptions, derogations and transitions

A source-authored exception is a provision with a typed edge to the provision it qualifies. A derogation is grounded in enabling authority. A granted exemption identifies beneficiary, scope, authority, validity interval and any compensating obligation. A transitional period constrains applicability and may create a separate obligation deadline.

Boolean exemption flags and free-text applicability basis are rejected. Expiry changes the exemption or transition, never the norm version. Non-derogable floors remain explicit.

## Applicability Assessment profile

The WM-ACT-034 profile requires: assessment identity and status; pinned norm expression and provision set; named subject, activity, product and market with state pins; jurisdiction; facts-as-of; assessor identity, role, competence and impartiality; separate deciding authority where applicable; per-provision reasoning and evidence; conclusion of applies, does-not-apply, conditional, indeterminate or disputed; confidence and limitations; review/expiry and surveillance duties.

The norm owns declared territorial, personal, material and procedural scope. The assessment owns the attributable conclusion for a named context. It cannot edit the norm.

Conflicting assessments coexist as distinct records. Supersession is valid only within the same accountable series and pinned context. Different authority, market, facts-as-of or norm version creates another assessment. Divergence records the alternatives, contradiction, resolution owner and deciding authority; no majority or implicit current answer is computed.

## Jurisdiction, obligations and compliance

Jurisdiction is a time-qualified reference that can express territorial hierarchy, subject-matter competence, extraterritorial connecting factors and overlapping rules. A single code cannot represent these semantics.

Citation, applicability and compliance are separate claims. A WM-XCT-029 obligation pins its legal basis, obligor, required action, conditions, due basis, fulfilment criteria and evidence. Applicability can justify deriving an obligation, but only obligation-level evidence and an authorized assessment can support a compliance conclusion.

## Acceptance scenario

A regulation has E1 in force and amendment E2 published with future partial commencement. E2 contains a 24-month transition for one provision. Market A concludes that the provision applies conditionally; Market B concludes that its activity is outside material scope. Both assessments pin E2, their provision sets, facts-as-of, evidence, assessors and limitations and remain visible. Obligations derived for Market A compute deadlines from the actual commencement event plus the transition. E2 does not alter E1 obligations before commencement, and neither assessment proves compliance.

## Invariants

1. Every norm resolves to verifiable work, expression, provision and source-copy evidence.
2. Citation text, URL, title, date and hash do not identify a norm.
3. Source text and enterprise interpretation are distinct attributable objects.
4. Publication, commencement, applicability, deadline, repeal and knowledge time remain distinct.
5. Assessments pin norm version, provisions, subject context, jurisdiction and facts-as-of.
6. Indeterminate and disputed conclusions remain first-class outcomes.
7. Conflicting assessments coexist and are never silently merged.
8. Supersession requires the same accountable series and equivalent pinned inputs.
9. Exceptions, derogations, exemptions and transitions remain distinct.
10. Exemptions are authority-backed, beneficiary-scoped and time-bounded.
11. Historic and superseded norm versions remain citable.
12. Applicability never proves compliance.

## Holds

WM-POL-001 and adjacent models remain non-canonical reviewable drafts with single-provider, relation-ledger, source-pin and fixture gaps. WM-ACT-034 has unresolved access, parent and assessment-series issues. Jurisdiction has no confirmed registry allocation. Jurisdiction-specific commencement, treaty, multilingual authenticity and applicability crosswalks require specialist review. This checkpoint makes no canonical completeness, installability or publication claim.
