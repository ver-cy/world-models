## Verdict per type

- **Position — REUSE ONLY (WM-ORG-004).** The contour's position content is already owned: `position_code` → `de-position-code`, `job_family` → `de-job-ref`/`de-occupation-code`, `grade` → `de-grade-ref`, `authorized_fte` → `de-fte`. Nothing in EM-ORG-06 survives the vacancy test as new structure.
- **BusinessRole — COMPLETE RESERVED MODEL, not a new ORG type.** Both specs already delegate abstract roles outward: WM-ORG-004 `abstract-role-binding` holds only a reference plus a fallback label, and WM-XCT-023 declares a required REFERENCE to a "Role type vocabulary / concept scheme model" with no registry ID. That unassigned reference is the reserved slot; BusinessRole should complete it, not be minted in ORG.
- **Accountability — PROFILE.** Two existing owners already split it: seat-durable accountability is WM-ORG-004 `prescribed-regulatory-responsibilities`; party-scoped accountability is a WM-XCT-023 assertion with `authority-basis-kind` and `mandate-ref`. No residue needs independent identity.
- **DecisionRight — REUSE ONLY.** Seat-conferred rights are `de-decision-right` + `de-vacancy-authority-rule`; person-exercised limits are `representation-and-limits` (`representation-limit`, `quorum-requirement`, `constraint-expression`). The pair is complete; adding a third owner would create competing sources of truth on the same limit.
- **RaciAssignment — PROFILE of WM-XCT-023.** Every required facet has a home: subject/context → `host-kind`/`host-version-ref`; role type → `role-type-code` with `role-classification-axis` = functional; player → `player-ref` or `position-ref`; validity → `valid-from`/`valid-until` + `period-boundary-semantics`; conflict rules → `incompatible-role-pair`, `separation-mode`, `sod-exception-ref`.
- **HeadcountPlan — identifier-unassigned candidate, but identifier assignment held.** It is a separate planning fact, not intrinsic capacity (below). The frozen dossier contains no evidence for it in either spec, so independent identity is argued, not proven; it must not be minted under EM-ORG-06.

## Evidence state

Both specs are `published` yet `publishableCanonical: false` and `adjudicationStatus: reviewable-draft`. Registry status is `described-previous-version` (WM-ORG-004) and `candidate` (WM-XCT-023); both `mapping_status` entries are `conceptual-candidate` at `index-and-publication-metadata` depth. Only selected findings were projected from 257,622 and 279,743 source bytes. This review is a boundary opinion over pinned drafts: no canonical status, no approved relations, no installability.

## Identity/mastership

Position identity is master-system-assigned (`de-position-id`, HRIS/position control) and must never be a title or date; `de-position-iri` is the optional graph identity. Role assertions carry their own identity (`assertion-id` + `assertion-id-scheme` + `assertion-natural-key`), which is what makes RACI and accountability addressable without promoting them to entities. Neither model masters the person. The contour's `candidate_master_systems` (corporate registry, HRIS, legal-entity registries) is consistent, but the split must be recorded: HRIS masters seats and occupancies; the corporate registry masters statutory officer assertions; neither masters role-type vocabulary.

## Position/occupancy/capacity

The three-way split is already drawn and should be adopted verbatim: WM-ORG-004 owns the durable seat; WM-ORG-016 owns occupancy (relationship ledger `WM-ORG-004 COMPOSE WM-ORG-016`, `review_state: candidate`); WM-ORG-002 owns the unit. Capacity is intrinsic to the seat — `de-fte`, `de-headcount`, `de-position-type` (single/pooled), `de-overlap-outcome`. Vacancy is **derived**, never stored: `de-open-capacity` computed against `de-occupancy-links`, with `de-vacancy-since`. HeadcountPlan is external because it is an aggregate over units and fiscal periods with its own approval lifecycle, and it exists before any seat is established; `de-budgeted-flag`/`de-budget-amount`/`de-funding-window` are the seat's projection of that plan, not the plan itself.

## Business role and PartyRole

An abstract BusinessRole is a concept with its own versioning and deprecation lifecycle; a PartyRole is a time-bounded assertion that a player stands in that role toward a host. WM-XCT-023's `role-type-and-axes` requires the axis declaration (functional / structural / contractual / statutory) and `role-type-binding-strength` — that is the mechanism that keeps the concept out of the assertion. Roles without a position are native: `player-kind` admits organizations, collectives and automated agents, `position-ref` is `0..1`, and the host may be an object, activity, agreement or party. Occupation/job/grade classifiers stay external registries under all three models; the position holds coded references and `de-classification-decision` evidence only.

## Accountability/RACI/IAM boundary

The line is stated in WM-XCT-023's RBAC boundary note and out-of-scope list: an RBAC role bundles permissions evaluated by a policy decision point; a party role is a business or legal assertion that may be an *input* to authorization and never carries permissions. `representation-limit` binds the host in the world; an entitlement binds a system. Keep them in different models with a one-way flow (assertion → policy input), and keep `participation-vs-standing-role` `assignment-mode` mandatory so act participation is not merged into standing occupancy.

## Invariants

1. A position exists and is queryable while `de-open-capacity` equals authorized capacity (vacant is valid).
2. Position identity survives any change of occupant; occupancy changes create assignment records, not position records.
3. Vacancy is derived from occupancy, never asserted on the seat.
4. Budget and `de-fte` are attributes of the seat, terminated only by `de-abolition-date` under `de-transition-authority`.
5. A role assertion grants no technical permission.
6. RACI validity: for a given host and period, exactly one Accountable; at least one Responsible; `assertion-uniqueness-key` prevents duplicates; conflicts resolved by `separation-mode` with time-limited `sod-exception-ref`.
7. Role type must name scheme, version and axis.

## Scenario walkthrough

**Negative — deleting an employee deletes the position and budget.** Rejected. The person is out of scope for both models; the deletion path reaches only WM-ORG-016. Ending occupancy frees `de-open-capacity`, sets `de-vacancy-since`, and leaves `de-fte`, `de-headcount`, `de-budget-amount` and `de-funding-source` untouched. Any implementation whose cascade reaches the position violates invariants 1, 2 and 4.

**Acceptance.** (a) Occupant change: prior assignment ends, successor begins (`succeed-role-holder`), position identity and effective-dated history preserved; `de-vacancy-authority-rule` decides whether delegations lapse or escalate during the gap. (b) One person, two roles: two assertions with distinct hosts, both validated by `validate-role-assertion` against `incompatible-role-pair`. (c) Two fractional occupancies, one seat: `de-position-type` = pooled, `de-headcount` = 2, two 0.5 FTE assignments summing to `de-fte` = 1.0, `de-overlap-outcome` recording warn-versus-block.

## Profile shape

One profile over WM-XCT-023 covering Accountability, DecisionRight-as-held and RACI: axis pinned to functional or statutory; role-type scheme pinned to a governed RACI/accountability vocabulary; `host-kind` restricted to decision, deliverable, process or control; player restricted to party **or** `position-ref`; cardinality rule per host/period; `separation-mode` mandatory; an explicit non-grant clause. Plus a job-share profile over WM-ORG-004 fixing pooled capacity and fractional-sum validation.

## Gaps and publication holds

Both models' own holds remain open and block any canonical claim: source re-verification and SRC-id re-keying (WM-ORG-004), multi-profile validation, retention as a declared gap, ODRL over-citation and HL7 RoleClass re-verification (WM-XCT-023). Directly relevant deferred items: job-share fractions, dual-incumbency overlap and union slot exclusivity are unsupported by primary sources in either run — so the third acceptance case is a *declared local profile*, not an evidenced capability. Additional holds for EM-ORG-06: no registry ID exists for the role-type vocabulary or classifier models; WM-ORG-016 has no registry reservation in this dossier though two invariants depend on it; all three relationship-ledger rows are `candidate`; no published RACI role-type vocabulary or segregation matrix was found by either provider.
