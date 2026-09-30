# EM-ORG-03 local synthesis

## Disposition

- Profile **Ownership Interest** across WM-ECO-038 holder-side positions and WM-ORG-012 qualified inter-organizational relations.
- Raise **Share Class** as an identifier-unassigned new-model candidate. Its issuer-side rights and lifecycle survive every holder and holding.
- Profile **Control Relation** over WM-ORG-012 with explicit basis, scope, direction, evidence and period.
- Reuse/profile WM-ORG-018 for **Governance Body** and legacy WM-ORG-007 for **Mandate**.
- Profile **Resolution** as the composition of WM-KNW-010 decision content, WM-REC-010 authentic fixed expression and WM-ACT-025 procedure evidence. No new Resolution identity is minted.

## Ownership and control boundaries

Share class, security position, relationship and governance body are independent identities. Registered holder, beneficial owner, economic-interest holder, nominee, custodian and manager remain separate capacities.

Economic interest, capital rights, voting rights, contractual control, de facto control and accounting consolidation are distinct assertions. Each carries its own scope, basis, evidence and validity. A position references a pinned Share Class version; class rights and amendments are issuer-side facts.

Direct and indirect calculations always declare right type, class scope, denominator, valid time, knowledge time, scenario, rule version and inputs. Treasury and suspended holdings are handled by the declared denominator rule. Economic and voting shares never mix. Cross-holding cycles use a declared method and tolerance or remain unresolved; they are never silently flattened. Derived values stay labelled and separate from asserted facts.

## Governance and authority

The body persists across changes in members, seats and meetings. Appointments profile WM-ORG-006 with party, seat, term, authority and source record. Attendance never proves appointment, and membership alone does not establish voting eligibility.

The mandate owns powers, reserved matters and limits. The governance body references a pinned mandate/delegation. Quorum and voting rules belong to the governing procedure; the meeting or written-consent act records the counted base, exclusions, recusals and determination at the relevant instant.

A resolution preserves decision content, procedure evidence and authentic issued expression as separate masters. Signing authority derives from an effective mandate, role and appointment, never from ownership percentage. A resolution authorizing a transaction does not itself mutate holdings.

## Acceptance result

Two classes have different vote ratios. A 51% economic holding in one class cannot yield 51% aggregate votes without a declared vote-weighted calculation. Cross-ownership is calculated with a named cycle convention. When a director changes, the old membership closes and the new one opens while body and seat persist. A resolution passed without quorum remains recorded with its failed attestation and defective/contested status; history is not discarded or silently validated.

## Required invariants

1. Interests compare only within a common class, denominator and period.
2. Economic, voting, control and consolidation assertions never substitute for each other.
3. Ownership never implies signing authority.
4. Every derived percentage is labelled, reproducible and input-pinned.
5. Treasury holdings do not vote and follow explicit denominator rules.
6. Cycles and exceptions remain visible.
7. Seat, office, member and person are distinct.
8. Attendance does not prove appointment.
9. Every resolution cites a mandate in force and procedure evidence.
10. Failed quorum preserves the record and blocks a valid-decision claim.

## Provider reconciliation

Share Class is the only permitted new master and remains identifier-unassigned. Ownership Interest and Control Relation are distinct typed profiles over WM-ORG-012; typed-profile identity does not create a new WM identifier. Ownership profiles cannot carry a `controls=true` shortcut. WM-ORG-007 reuse is conditional on mandate, eligibility, quorum and authority remaining distinct.

Calculations walk by pinned Share Class version and declare right type, denominator, valid and knowledge times, scenario, rule version, complete inputs, cycle convention and tolerance. Reciprocal holdings remain separate positions. A missing convention makes a result non-authoritative, and different conventions inside one scenario make results incomparable.

Procedure evidence is mandatory in every Resolution composition. A no-quorum act preserves content, authentic expression and failed attestation but is not validly adopted, creates no Mandate and grants no signing power. Signing authority requires a live in-scope Mandate plus appointment or role.

## Frozen-audit remediation

Share Class lifecycle now keeps amendment exclusively in append-only ShareClassVersion records. Version pins include `(shareClassId, version, contentDigest)`, deterministic JSON canonicalization, SHA-256, valid and recorded times. Effective versions require structured rights, denominator policy, issued-quantity rule and an authority bundle referencing Mandate, decision, authentic record and procedure evidence.

The profile defines one normative Derived Claim contract for derived and externally asserted percentages, a closed versioned cycle-convention list, convergence evidence and an explicit hold for the unassigned calculation-context vocabulary. WM-ECO-038 exclusively masters quantity and class pins; WM-ORG-012 carries no duplicate quantity. Ownership Interest has addressable profile-instance identity, required holder capacity and a natural-person path that does not fabricate an inter-organizational relation.

WM-ORG-006 is included for appointment and body-scoped seat semantics. Membership intervals enforce seat uniqueness and authority containment. Body continuity versus succession, per-matter recusal, written consent and governing-procedure holds are explicit. WM-REC-010 is the Resolution anchor with adoption status; ratification creates a new Resolution. Signing authority is evaluated at the act instant in valid and knowledge time. Mandate reuse has a nine-field gate and explicit failure branch. Corporate-action execution remains unassigned.

Every invariant and constraint now has an ID. Forty-seven declarative fixtures carry trace links, concrete positive expectations and an explicit non-executable hold until unassigned vocabularies and boundaries are resolved.

## Holds

All target models remain non-canonical reviewable drafts with provider waivers. Share Class requires registry allocation and its own source/corporate-action boundary. WM-ORG-012 and WM-ORG-018 have registry parent conflicts; relation contracts are missing; quorum, appointment and indirect-calculation fixtures remain declarative and non-executable until their unassigned vocabularies and boundaries are resolved. Jurisdiction-specific control, consolidation, beneficial-ownership and authority profiles remain adopter-owned. No runtime identifier or installable release is created.
