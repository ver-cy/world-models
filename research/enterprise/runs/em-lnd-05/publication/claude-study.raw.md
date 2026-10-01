# Verdict

**PROFILE.** EM-LND-05 is admitted as a named, read-only **projection profile over WM-ACT-029**, resolving components through WM-ACT-005. No new registry ID. Neither `DeliveryLandscape` nor `DeliveryScope` is admitted as a subject-model type; both are view names, not masters.

The independent-identity test fails on all three limbs. (1) *Identity*: a landscape instance is keyed by view definition + `as_of` + `scenario` + knowledge time — a derived key over existing roots, not an independently mintable identifier. (2) *Lifecycle*: every state change a landscape could undergo is already an appended event in 029's `component-admission-removal-priority-change-successor-and-history` or `programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation`. A landscape has no authorization, no mandate, no closure of its own. (3) *Invariants*: the double-count rule lives in 029's `metric-definition…-and-aggregation` (aggregation and deduplication) and `benefit-owner…-and-attribution-limit`; cost single-source lives in WM-ACT-005's `a-cost-baseline` and `de-actual-cost-to-date`. A landscape enforcing them would duplicate, not add.

`DeliveryScope` fails an additional test: 029 owns `scope-inclusion-exclusion-assumption-constraint-context-and-success` and 005 owns `de-scope-statement` with exclusions and confirmation. A third scope holder creates a second authoritative scope statement inside the same graph.

# Boundary

The landscape owns **nothing**. It owns no membership assertion (029, parent-side, per 005's explicit "must not be duplicated as a child edge here"), no component master, no cost fact, no benefit master, no resource capacity.

It owns only a **viewpoint specification** in the ISO 42010 sense: stakeholder, concerns, admitted model kinds, correspondence rules, and the loss declaration for the projection. A viewpoint is a specification artifact, not an aggregate root. Under Vercy composition/whole-object, 029 already delegates to component masters; the landscape must delegate identically and terminate — it adds one level of read, zero levels of ownership.

Boundary against a tracker container: a Jira/ADO project, board or epic tree is a workspace of a tooling system. Under 005 `f-project-identity`, the master system issues the authoritative identifier; a tracker key is admissible only as `de-alternate-identifier` bound to its issuing system and resolution target. A tracker container that resolves to no WM-ACT-005 authoritative identifier is not a landscape node at all.

# Membership/allocation semantics

**M:N across management views.** 029 places no single-parent constraint on components: N roots may each assert membership over the same project identifier, each with its own admission basis, effective interval, status and authority. This is sufficient for one project sitting simultaneously in a funding portfolio, a coordination program, a product-line view and a geographic view. What 029 does *not* supply is a **membership role discriminator**, and its absence is exactly where duplicate budget enters. The profile must require, on each membership assertion, one of: `financial-consolidating`, `coordination-only`, `reporting-only`.

**Project–Product–Team.** All three edges are M:N and all resolve outward: products to the product master, teams to the resource/organization master via 005 `de-allocation-owner-ref`. The landscape never stores team composition or product definition.

**Shared resource conflict.** Contention is a property of the *resource owner's capacity*, not of any view. It surfaces through 029 `resource-capability-capacity-demand-allocation-utilization-gap-and-conflict` and is arbitrated through 005 `q-resource-contention`. A landscape may display a conflict; it may not declare or resolve one.

**Cost single source.** One cost fact per `(project, baseline version, period, currency, price base, data date)`, held by 005. Every view figure is an allocation share applied to that fact. No view stores a monetary value; no roll-up is persisted.

**Benefit attribution.** Two claim kinds, never mixed: `exclusive-attribution` (share-weighted, additive, shares sum ≤ 1.0 per benefit/period/measure across *all* claiming roots) and `contribution-claim` (non-additive by construction, bounded by 029's declared causal limit, never summed).

# Required profile

A **projection profile**, delivered through 029's existing `project-validate-correct-retain-and-audit` function. It must **not** be added as a value of 029's required program/portfolio discriminator: that discriminator sits inside the artifact identity tuple, and 029 already holds an unresolved supersession rule for profile-unsafe change — adding a third value would be breaking.

V1 candidate fields become **projection parameters**, retaining `candidate-not-normative`: `portfolio_scope` → 029 scope finding reference; `as_of` → the (effective time, knowledge time) pair, mandatory; `priority_policy` → pinned criteria-and-weights version reference; `scenario` → 029 balancing-function scenario code, required and non-null for any non-authoritative view.

Three view classes, mutually exclusive: **authoritative** (no scenario code; bitemporal current-state), **as-of replay** (knowledge time pinned; immutable), **scenario** (scenario code required; may never feed benefit realization, cost actuals or published reporting).

# Invariants

1. A landscape node resolves to an authoritative WM-ACT-005 or WM-ACT-029 identifier; a tracker container is not a project.
2. At most one `financial-consolidating` membership per `(project, fiscal period, cost dimension)` across all roots.
3. No monetary or benefit value is stored on a view; every figure is computed from a source fact plus a declared allocation share.
4. Roll-up deduplicates on the source fact key before summation; path multiplicity never multiplies value.
5. Allocation shares sum to ≤ 1.0 per `(fact, period, dimension)`; orthogonal decompositions (product view, team view) are never summed with each other.
6. Contribution claims are non-additive and carry 029's attribution limit; only exclusive-attribution claims aggregate.
7. Project↔Product and Project↔Team are M:N with no exclusivity; membership is asserted parent-side only.
8. Every published view declares its class, `as_of`, knowledge time and criteria version; a scenario view is never published as authoritative.
9. Resource conflict is recorded against owner capacity, not against the view.

# Scenario walkthrough

**Negative — duplicate budget.** Project P is a direct component of portfolio X and also of program G, itself a component of X; P also appears in a product-line view. Naive traversal returns P's budget three times. Three independent failures: traversal with no role filter (blocked by invariants 2 and 4), no allocation share (invariant 5), and reading budget from the view rather than from 005's cost baseline (invariant 3). With the profile applied, X's figure resolves to one cost fact; G's membership is `coordination-only`; the product-line view is `reporting-only`; the deduplicated roll-up equals one budget.

**Acceptance — one project, two products, four teams.** P delivers to products A and B; teams T1–T4 are allocated through 005 `de-resource-allocation` with quantity, unit, period and owning party. Cost: one fact at P's data date against a named baseline version. Product view allocates it 60/40 — summing to exactly one fact, not a re-measurement. Team view decomposes the same fact by effort share — a second, orthogonal decomposition that must not be added to the product view. Benefits: A's benefit is exclusive-attribution at 0.6; B's a contribution-claim, non-additive, reported separately. T3 is also committed 0.5 FTE to another project in the same period against 0.8 here: capacity exceeded, surfaced as a 029 conflict, arbitrated by the owning party, recorded against capacity. M:N holds throughout; the cost fact is asserted once.

# Gaps and publication holds

- **Inherited holds bind.** WM-ACT-029 is `reviewable-draft`, `publishableCanonical: false`, under a single-provider waiver with Claude and Grok waived; WM-ACT-005 is `reviewable-draft` with ~30 unverified URLs. EM-LND-05 cannot be published above reviewable-draft.
- **Relation rows held.** 029's registry Project parent link and all proposed component relations are on hold with no approved rows. The landscape's entire traversal contract is unverifiable until those rows exist. **This is the hard blocker.**
- **Membership role discriminator is unsourced.** Neither model supplies it, and no source in either pack governs cross-root financial consolidation. Deferred research, not an assertion.
- **Cross-root deduplication scope unconfirmed.** 029's aggregation-and-deduplication element may cover only intra-root aggregation. Confirm before invariant 4 is claimed as reuse rather than extension.
- **Crosswalk incomplete.** Both candidates are `conceptual-candidate`; `published` ≠ independent expertise. Full semantic crosswalk remains a precondition.
- **Spelling normalization.** 029's unresolved programme/program token conflict propagates to any landscape artifact naming; block artifact minting until normalized.
- **No independent review.** This review is a boundary opinion on a frozen dossier, not external provider adjudication.
