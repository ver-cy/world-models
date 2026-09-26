# Independent Review — EM-LND-15 Risk and Compliance Landscape

## Verdict

**Reuse and profile; allocate no new subject-model identifier.** The landscape is a *governed view* over records mastered elsewhere, not a new semantic domain. Concretely: **RiskLandscape** = a governed view-definition record (scope/perimeter, as-of, criteria and taxonomy pins, membership rule, the three questions it answers) plus immutable serial snapshots — it needs **record identity for the view definition and each snapshot, but no independent model identity**. **AssuranceCoverageView** = a **projection of that landscape**, no independent identity beyond its snapshot serial and its declared denominator; it is a rendered answer to "where is there no coverage," not a second object. Both must be typed as views in the ISO 42010 sense (viewpoint → questions → construction rules), never as a register that owns membership.

This follows the frozen adjudications rather than contradicting them: WM-XCT-027 explicitly **rejected** a local coverage-matrix artifact because a many-to-many matrix spanning many risks, controls and hosts is cross-record state a host-scoped field group cannot own, and recorded that aggregation semantics are not modelled. WM-KNW-015 already makes register views, snapshots and extracts read-only projections that never recompute item values. EM-LND-15 is the correct home for that cross-record traversal — as a view, with the comparability gate imported, not as an aggregate that re-masters risk or control.

## Evidence

All three target models are `published` but `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`, single-provider waiver (Grok waived 2026-08-29), evidence depth `index-and-publication-metadata`. WM-XCT-027's boundary decision is **`split`, not accepted**: bundles 4–6 author control implementation assertions, assessment/evidence manifests and effectiveness conclusions that the same record's `scope_statement`, `out_of_scope` and boundary note 2 assign to a control assessment model. WM-KNW-015 is `accepted` as entity but holds an unratified WM-ACT-017 parent and an empty composition set. WM-ACT-033 is `accepted` as aggregate with an empty relationship contract and unverified artifact/access rules. WM-ACT-034 is a `candidate` reservation with an accepted aggregate root and a downgraded access dimension. Nothing here supports a conformance claim.

## Identity/mastership

- **Risk entity, register membership, lifecycle** → WM-KNW-015 (entity; item is root, register is artifact).
- **Risk assessment context, inherent/residual estimate, appetite comparison, comparability verdict** → WM-XCT-027 retained mixin (host-scoped, no independent identity).
- **Control identity, applicability, design/implementation/operation, ownership** → the **identifier-unassigned Control candidate from EM-RSK-01**. Accounted for without allocation: the landscape references it as *pending-master*, and **must not** read control state out of WM-XCT-027 bundles 4–6, which the split disclaims.
- **Assessment/evaluation of a control** → WM-ACT-034 profile (reserved candidate; no ID allocated here).
- **Review/inspection/audit engagement and its findings** → WM-ACT-033 (findings are engagement-owned; recurrence key is derived).
- **Requirement / norm / provision** → WM-POL-001 + WM-KNW-012; **applicability** → WM-ACT-034 profile per EM-LEG-02.
- **Obligation** (obligor, due basis, fulfilment, evidence) → WM-XCT-029.
- **Observation / measurement** → WM-MAT-008 (evidence, never a finding).

Landscape identity: master-system identifier first, else governed IRI, else Dimension UUID/ULID with recorded fallback. `assessment_date` and `risk_scope` from LND-15 v1 are **candidate-not-normative** and are never identifiers; `scale_ref` maps to the criteria pin, `assurance_policy` to the view's construction rules.

## Scope and requirements

The perimeter is explicit: in-scope subjects (entities, processes, systems, sites, markets), jurisdictions, requirement sources at pinned expression/provision versions, control catalogue revision, criteria set version, and as-of instant. **Requirement applicability is an assessment, not a flag**: a requirement is in the applicable population only where an Applicability Assessment pins the norm expression, provision set, subject state, jurisdiction and facts-as-of, and concludes applies or conditional. `indeterminate` and `disputed` remain first-class and are counted separately — never silently resolved to not-applicable. Requirement ≠ obligation ≠ control: applicability may justify deriving an obligation; only obligation-level evidence supports compliance.

## Risk/control boundary

WM-XCT-027 cites controls and effectiveness determinations by reference and never produces them. The landscape inherits that: it may traverse risk→control reliance edges and read *cited* determinations, but attribution of reduction requires a current determination; an untested, expired or adverse conclusion yields no reduction. Reliance-without-determination is an explicit state, not zero. Superseded risk or control revisions mark dependent assessment contexts stale.

## Coverage and effectiveness

Four separate quantities, four separate denominators, never one percentage:

1. **Coverage** — structural. Denominator = applicable requirements (per assessments in force at the cut-off) × in-scope subjects, or applicable controls per applicability statements. Numerator = those with ≥1 non-retired mapping. Excluded from the denominator: not-applicable with justification (reported separately); never excluded silently.
2. **Compliance** — obligation fulfilment, evidenced, authority-qualified.
3. **Assurance** — independent examination with declared assurance level, methods/objects, scope exclusions and carve-outs; bounds reliance, does not establish compliance.
4. **Residual risk** — WM-XCT-027 post-control estimate with cited current determinations and appetite comparison outcome.

Effectiveness is distinct from existence, design, implementation and operation: four independent status values, none derived from another, plus a separate conclusion on a named vocabulary with valid-until and invalidation triggers. A policy, procedure, crosswalk mapping, or an uneventful period sets no effectiveness field.

## Assessments/audits/findings

Chain: requirement → applicability → control (applicability, design, implementation, operation) → assessment (method examine/interview/test, depth, coverage, sample basis, period, assessor independence) → evidence (reference + digest + verification outcome) → finding (criteria/condition/cause/effect, determination, severity, engagement-owned) → conclusion (validity window) → residual attribution. Coverage counts edges; it never counts findings closed.

## Exceptions and validity

Exceptions/waivers carry granting authority, beneficiary, scope, validity interval and compensating obligation. Expiry changes the **exception**, not the requirement or the control: on expiry the implementation state reverts to deviation-without-exception, dependent effectiveness conclusions are flagged for revalidation, and any residual attribution resting on it is suspended. Conclusion validity is derived, not asserted: currency is recomputed against a **caller-supplied** cut-off instant; an expired conclusion stays readable, marked not current, and cannot ground a new acceptance.

## Time/scenario

Event time, as-of/observation time and record time stay distinct; all instants RFC 3339 with explicit offset. The cut-off is a view parameter, never defaulted to "now." Comparability is gated: differing criteria, method, expression mode, scope, horizon or taxonomy pins block aggregation and return the mismatched pins plus non-strippable caveats. Ordinal bands are not averaged or multiplied.

## Scenario

At cut-off T: **C-1** is applicable, design adequate, implemented, expected cadence monthly, observed occurrences 0 for the period → *control without execution*; operating status not-operating, no effectiveness conclusion possible, no reduction attributed. **R-7** is in the requirement set with no applicability assessment resolving for the perimeter subject → *requirement without applicability*; excluded from both numerator and denominator and reported as a scope gap, not as non-compliance. **X-3** waives a deviation with valid-until < T → *expired exception*; the dependent conclusion is revalidation-pending. Meanwhile every card in the register is 100% complete — that measures **register currency only** and proves no coverage, compliance, assurance or residual position.

## Invariants

1. Coverage ≠ compliance ≠ assurance ≠ residual risk; each declares its own denominator and exclusions.
2. Every assertion cites verified evidence; a completed card is not evidence.
3. Every exception retains authority, beneficiary, scope and expiry; expiry changes the exception only.
4. Documentation, crosswalk mapping or absence of incidents never sets effectiveness.
5. Design, implementation, operation and effectiveness are independent; none is derived from another.
6. Conclusions expire against a supplied cut-off; expired is readable, not current, not a basis.
7. Requirement applicability is an authority-qualified assessment; indeterminate and disputed are countable outcomes.
8. Aggregation requires a comparability verdict; caveats are non-strippable.
9. The landscape references masters and re-masters nothing; snapshots never recompute item values.
10. Control state is read from the pending Control master, never from WM-XCT-027 bundles 4–6.

## Minimal profile shape

`RiskLandscapeView`: view id; viewpoint + questions answered; perimeter (subjects, jurisdictions, requirement sources @version, control catalogue @revision); criteria/taxonomy pins @version; cut-off instant; membership rule; construction rules; comparability verdict + caveats; declared denominators (per quantity) with exclusion ledger; gap sets (uncovered-applicable, requirement-without-applicability, control-without-execution, expired-exception, expired-conclusion, reliance-without-determination); pending-master markers; owner + reviewer; snapshot serial + digest; access class; retention binding.
`AssuranceCoverageProjection`: parent view id; quantity; denominator reference; numerator rule; per-cell state; caveat set; serial + digest.

## Holds

All three targets are non-canonical single-provider reviewable drafts; WM-XCT-027's ownership split is unresolved; WM-ACT-034 is a reservation; relationship contracts are empty and composition claims unverified; source pins, crosswalks and fixtures are unverified. The Control candidate remains identifier-unassigned, so the coverage denominator is **provisional** until its applicability records have a master. No legal advice, no canonical completeness, no installability or publication-readiness claim.
