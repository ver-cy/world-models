**Verdict.** PROFILE over WM-ACT-005 and WM-ACT-029. No new catalogue or runtime ID. DeliveryLandscape is a read-only projection specification plus generated views. DeliveryScope stays with the owning 005 or 029 root. A tracker container is not a project unless it resolves to an authoritative 005 or 029 identity. Cost is asserted once on the project. This is standards alignment, not a second delivery ledger.

**Identity / lifecycle test.** Source facts: 005 owns project identity, authorized scope, immutable cost/schedule/scope baselines and time-phased cost facts. 029 owns program or portfolio identity, component membership without absorbing component masters, allocation decisions and benefit logic. EM-WRK-01 already states that a tracker container is not a project. ISO 21504 / PMI alignment: a portfolio is a collection of components grouped to meet strategy; a program coordinates related work for benefits not available from any one project; components keep their own identity. ISO 42010 alignment, as on EM-LND-01: a view is not a second system of interest.

- **DeliveryLandscape.** Identity: landscape-id + spec version + root set + view policy (membership roles included, fiscal period, cost dimension, currency, data-date, scenario class). Lifecycle versions the spec. Spec change does not rewrite 005/029 records. Writes: none. Fail-to-new-aggregate if the landscape authors membership, stores a second budget, assigns identity to a tracker folder, or is re-imported as a project or portfolio.

- **DeliveryScope.** On 005: authorized scope of that project. On 029: program or portfolio scope plus the membership set it governs. A view may display the union of scopes for a root; it does not own them. Fail-to-new-aggregate if DeliveryScope becomes a third record kind with its own lifecycle.

- **Tracker container.** A Jira, Azure DevOps or GitHub “project” is an adapter. It enters the landscape only after it binds to a 005 or 029 identity. Unresolved adapter IDs are omitted or flagged `unresolved-adapter`. They receive no cost fact, membership role or benefit claim.

**Membership / allocation semantics.** Design inference from 029 membership plus the card’s anti-double-count invariant, labelled as such.

A project may belong to several 029 roots. Each membership carries exactly one role:

1. `financial-consolidating` — roll-up parent for a named fiscal period and cost dimension. The project’s single cost fact is included once in that root’s financial view after any declared share.
2. `coordination-only` — dependency, sequencing or interface. Visible in the graph; contributes no money.
3. `reporting-only` — dashboard inclusion. No financial roll-up, no coordination authority.

Constraint: at most one financial-consolidating membership per project per fiscal period per cost dimension. A second consolidating edge in the same key is `unresolved`, not a silent double count. Different dimensions (statutory book versus management book) may each have one consolidating parent.

Typical but not hard-coded pattern: program membership consolidates delivery budget; portfolio consolidates the already-deduplicated program view; a direct portfolio→project edge in the same period and dimension is coordination- or reporting-only. The PROFILE enforces uniqueness and refuses naive nested sums; it does not freeze that topology.

Project–Product and Project–Team are M:N references, not containment and not cost ledgers. Allocation *shares* live on those edges. Product shares decompose the single project cost fact on the product axis. Team shares decompose capacity or effort. Shares on one axis should sum to ≤ 1; remainder stays explicit. Product totals and team totals must not be added.

**Cost and benefit rules.** Cost is asserted once on 005 for the pin `(project-id, baseline-id, period, currency, price-base, data-date)`. 029 and the landscape never mint a second cost fact.

Every view: collect membership edges; deduplicate source cost facts by project identity and pin; apply allocation shares only on financial-consolidating memberships for that period and dimension; leave coordination and reporting edges as topology.

Product allocation and team allocation are orthogonal decompositions of the same cost fact. Adding them double-counts. Unallocated remainder on either axis stays visible, in the same spirit as EM-LND-10.

Benefits distinguish two claim kinds that must not be mixed in one sum:

- **Exclusive attribution** — additive shares of one benefit identity; shares across claimants ≤ 1 for a period.
- **Contribution** — non-additive enabling claim; several projects may contribute to one outcome and must not be summed as if exclusive.

EM-STR-02 remains the benefit master. Planned or forecast benefit is not realized benefit.

**Scenario results.**

1. *Portfolio contains a project directly and through a program.* Identify the unique 005 cost fact. Deduplicate by project identity before any share. If both paths are financial-consolidating in the same period and dimension → unresolved, no total. If the program path consolidates and the direct edge is reporting- or coordination-only → include the project once via the program. A view that adds nested references fails the card negative case.

2. *One project, two products, four teams, one cost fact.* 005 holds one assertion. Two product edges carry product shares. Four team edges carry capacity or effort shares and do not split the cost ledger unless a named cost-to-team rule is declared. The view may present a product breakdown or a team breakdown, never their arithmetic sum. Neither product nor team absorbs the project.

3. *A team is overcommitted across projects.* Landscape surfaces a derived conflict: sum of pinned demand versus declared capacity for period and unit, after deduplicating the same commitment fact. Result: overcommit flag, residual (may be negative), contributing project-ids. Landscape does not rewrite 005 commitments or invent a team-level cost fact. Money and effort stay in their own units.

4. *A scenario view is mistaken for authoritative actuals.* Every view pins `scenario-class` ∈ {authoritative-actuals | baseline | forecast | scenario} plus data-date. A scenario or forecast projection cannot be read as actuals. Missing class → refuse or unknown, never default to actuals. Writing a scenario total back onto the 005 baseline or 029 aggregate actuals fails this test and the EM-STR-02 negative case.

**Missing relations / fields** (named constraints on existing models, not new IDs): membership.role; membership.fiscalPeriod and costDimension; allocation.share, allocation.dimension and unallocated remainder; 005 cost-fact pin; benefit claim class {exclusive-attribution | contribution}; view scenario-class and data-date; tracker-adapter binding to 005/029 or `unresolved`.

**Publication blockers.**
- 029 frozen relation ledger has no approved 005 edges; membership-role and uniqueness key are not yet on the published model.
- Financial-consolidating uniqueness is a PROFILE constraint, not an existing 029 invariant.
- No fixtures for the diamond path, product-share + team-share non-additivity, team overcommit, or scenario-class refusal.
- 005 and 029 remain reviewable drafts with source-pin, ISO-text and second-provider holds. 029 has no approved project relation rows.
- EM-WRK-04 stays the selection-subject neighbor; this landscape must not absorb prioritization.
- Alignments to PMI, ISO 21504 and ISO 42010 are alignments only.
- Do not invent a DeliveryLandscape or DeliveryScope runtime identifier.