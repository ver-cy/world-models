# EM-ORG-03 — Ownership, Control and Corporate Governance

## Verdict

Reuse with profiles, one new-model candidate, no identifiers allocated.

- **OwnershipInterest** — profile. Two masters, not one: WM-ECO-038 for the holder-side position; WM-ORG-012 for the qualified inter-organizational interest edge. No new ID.
- **ShareClass** — new-model candidate, identifier unassigned. Neither base masters it: WM-ECO-038 lists "share class" as an *external reference*, and WM-ORG-012 is a relationship. The class has identity and lifecycle (creation, amendment of rights, conversion, redemption, reclassification) independent of every holding and every holder.
- **ControlRelation** — profile of WM-ORG-012 (`control-interest` layer, `control_basis`, kind-qualified graph rules).
- **GovernanceBody** — reuse WM-ORG-018 with an enterprise profile.
- **Mandate** — reuse WM-ORG-007 as master of the constitutive instrument; WM-ORG-018's `body-mandate` layer holds only the body-scoped delegation binding by reference.
- **Resolution** — profile, not a subject. Decision content → WM-KNW-010; authentic fixed expression → WM-REC-010; sitting, quorum determination and division → WM-ACT-025. WM-ORG-018 retains references only.

## Evidence

All three targets are `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, single-provider-waiver (Codex; Claude and Grok waived), `evidence_depth: index-and-publication-metadata`. WM-ORG-018 declares no quorum calculator, no appointment verifier, no decision-validity fixtures. WM-ORG-012 declares no graph-rule engine and rejects "scope-free percentages or indirect graph-derived ownership." WM-ECO-038 carries fourteen publication holds including a capacity hold and a balance hold. Nothing below is an installability or completeness claim.

## Identity/mastership

Four independent identities, four lifecycles: the **class** (issuer-side, survives all holders), the **position** (WM-ECO-038: holder capacity + security + account/register context, source-qualified), the **relation** (WM-ORG-012: parallel scopes, own ID distinct from its endpoint tuple), the **body** (WM-ORG-018: persists across membership turnover and meetings). Registered holder, beneficial owner, economic-interest holder, nominee, custodian and manager remain separately asserted capacities (WM-ECO-038 capacity hold). Two registry seams must be resolved before publication: WM-ORG-012 carries `parent_ids: WM-ORG-001` against a specification that declares WM-ORG-001 a REFERENCE endpoint — a relationship cannot be owned by one endpoint (already flagged at EM-ORG-01); WM-ORG-018 carries `parent_ids: WM-ORG-003` (Team) against a specification that declares WM-ORG-003 a non-owning REFERENCE.

## Ownership and share class

Six separately typed assertions, never derivable from each other: economic interest (dividend/distribution participation, liquidation preference), capital rights (subscription, pre-emption, conversion), voting rights (per-class ratio, class-vote gates, suspended or capped votes), contractual control (shareholder agreement, veto, casting vote, board-nomination right), de facto control (asserted with basis and evidence), accounting consolidation (standard-, scope- and period-qualified). WM-ECO-038 already separates legal title, beneficial interest, economic interest, control and voting-right assertions and refuses to collapse settled/available/blocked/pledged/lent balances — the profile inherits that refusal. ShareClass carries the rights, the ratio, the denominator base and the amendment history; a position references a class at a version.

## Control and consolidation

`ControlRelation` is a WM-ORG-012 assertion with participants, direction, kind, scope, control basis, valid interval and evidence. Consolidation is a *different* kind with its own standard and reporting period and is never equated with equity, votes, affiliation or supply. Reporting exceptions are recorded rather than omitted. Non-disclosure is not proven non-existence.

## Indirect calculations

Every computed figure is a labelled, reproducible derivation carrying: right type (economic | voting), class scope, denominator base, `asOf` valid time, knowledge time, scenario, rule version and input references. Rules:

1. **Direct** — one class, one period, one denominator.
2. **Denominator** — declare issued, outstanding (issued − treasury), or voting-eligible (excluding non-voting classes, treasury, suspended/capped votes, recusals). Treasury holdings are excluded from both numerator and denominator for control purposes and never vote.
3. **Indirect** — multiply along a chain only within one right type; never multiply an economic share into a voting share; retain component edges (BODS-style) rather than collapsing them.
4. **Cross-holdings** — a simple product diverges. Either solve the reciprocal system iteratively to a declared tolerance, or apply a declared convention (e.g. eliminate reciprocal legs), and record which. Cycles are reported, not silently traversed.
5. **Aggregation** across classes requires a declared common basis (as-converted or vote-weighted) and is refused otherwise.
6. **No inference** — economic share never yields voting share, board seats, consolidation, or signing authority.

## Governance body and membership

WM-ORG-018 holds body identity, establishment, seats, officers and procedure references. Appointments are Membership assertions (WM-ORG-006 profile): party + seat + term, from an authoritative record, with the explicit prohibition on inferring appointment from attendance. Seat ≠ holder ≠ person. Membership confers no vote by itself; eligibility comes from the governing rule.

## Mandate/quorum/voting

Mandate (WM-ORG-007) supplies powers, reserved matters and limits; the body's delegation binding cites it at a version. Quorum threshold, majority rule, eligibility and recusal effects are properties of the rule, not of the sitting — WM-ORG-018 correctly refuses universal arithmetic. The *determination* is made at the sitting (WM-ACT-025 quorum-determination finding: counted base, exclusions, instant, outcome) and evaluated by WM-REC-010 `fn-evaluate-quorum-and-majority`, which returns a verdict and blocks transition to a decided state. Recusal adjusts the eligible denominator. Abstention, dissent and absence are not interchangeable.

## Resolution and authority

A resolution is the fixed expression (WM-REC-010) of a decision (WM-KNW-010) taken by a body (WM-ORG-018) under a mandate (WM-ORG-007), evidenced by a sitting or a written-consent path (WM-ACT-025; Delaware §141(f)-style consent has no meeting). Signing authority derives from mandate + official role + appointment in force, never from a shareholding. A resolution that authorises a transfer does not itself change a position; WM-ECO-038 records the resulting change from its own source event.

## Acceptance scenario

**Two classes.** A (1 vote), B (10 votes). 51% of A is recorded as a class-scoped economic and voting interest; aggregate voting power is computed only on a declared vote-weighted basis and may be a minority. The negative case fails as required.
**Cross-ownership.** A→B 60%, B→A 10%. Product-only chaining is rejected; the profile emits a labelled derivation naming the convention and tolerance, with treasury excluded.
**Board change.** A director is replaced: the membership term closes, a new membership opens, the seat and the body identity persist, and no prior resolution is altered.
**Resolution without quorum.** The decision content, the participation acts and the record all persist; the quorum attestation records a failure with counted and required figures; the record is retained in a contested/defective state pending a competent determination. It is neither discarded nor silently validated.

## Invariants

1. Interests compare only within one class, one denominator, one period.
2. Participation is not control; control requires a basis.
3. Economic share never yields voting, consolidation or signing authority.
4. Every percentage carries class, denominator, time and scenario.
5. Treasury holdings neither vote nor count in the control denominator.
6. Derived figures are labelled, dated, reproducible and never merged with asserted ones.
7. A resolution cites a mandate in force and a completed procedure.
8. Seat, term and holder are distinct; attendance is not appointment.
9. Registered holder ≠ beneficial owner.
10. Cycles and exceptions are reported, not inferred away.

## Minimal model set

WM-ORG-018, WM-ORG-012, WM-ECO-038, WM-ORG-007, WM-ORG-006, WM-ACT-025, WM-KNW-010, WM-REC-010, WM-ORG-001; plus ShareClass as an unallocated candidate.

## Holds

Single-provider waiver on all three targets; two registry parent conflicts unresolved; WM-ORG-018→WM-ACT-025 containment is candidate, not approved; no executable quorum, appointment or indirect-calculation fixtures exist; jurisdiction profiles for control, consolidation, beneficial ownership and signing authority are adopter-owned. This is a boundary decision, not a canonical or installable release.
