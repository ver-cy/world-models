**Verdict.** Conditionally accept. Profile Portfolio on WM-ACT-029 only as a selection-and-allocation container that disables Program delivery, exclusive child-set, relatedness, rollup and single-owner funding. Treat PortfolioComponent, Prioritization, InvestmentAllocation and PortfolioScenario as addressable portfolio-owned releases. Keep component mastership, budget authority, observations, accounting actuals and decision records external. Allocate no other identifier. This review is not a publication decision.

**Selection Criteria Set identity.** Released set instances need independent identity so two portfolios and successive cycles can pin the same set. Binding criteria as portfolio-owned releases would duplicate sets or block reuse. EM-WRK-04 allocates no new identifier; the root stays identifier-unassigned. SelectionCriterion belongs to the set, not to a portfolio.

**Double funding vs double counting.** Two portfolios may fund one initiative at 0.6 and 0.4. That is overlapping investment intent, in-model and allowed. Double counting of budget authority, commitments, accounting actuals, capacity, outcomes or benefits is out-of-model and forbidden. Shares need not sum to 1.0; other sponsors may exist. Share basis (capital, cost, capacity, headcount) is unspecified and must not default to “fraction of the initiative budget.”

**Strongest evidence.** The 0.6/0.4 fixture works only under this split: initiative mastership stays on WM-ACT-030; two PortfolioComponent memberships; two InvestmentAllocation intent shares; budget authority and actuals stay on WM-ECO-012; a selected PortfolioScenario pins a criteria-set version and decision-evidence references without absorbing those records. Profiling on WM-ACT-029 also avoids minting a new portfolio identifier.

**Strongest counterexample.** If WM-ACT-029 already binds exclusive Program ownership or funding, one portfolio becomes “the program” and 0.6+0.4 is illegal. Separately: two portfolios share one criteria set, apply different local observations, each claims 100% of initiative benefits, and finance also books the initiative budget — selection looks valid, enterprise totals lie. Evidence is also lost if a selected scenario mutates live criteria instead of pinning a released set.

**Identity / mastership.** Portfolio instances have their own identity as a WM-ACT-029 profile. Project mastership stays on WM-ACT-005; Initiative on WM-ACT-030; budget authority on WM-ECO-012; Goal/Objective on WM-KNW-011; decisions on the decision triad. PortfolioComponent does not transfer mastership. Prioritization, InvestmentAllocation and PortfolioScenario are cycle-scoped portfolio-owned releases.

**Boundaries.** Portfolio ≠ Program ≠ catalogue ≠ project ≠ initiative. Membership ≠ mastership. Criteria ≠ observations ≠ ranking. Rank ≠ intrinsic work properties. Portfolio allocation ≠ budget authority ≠ commitment ≠ actual ≠ component funding. Scenario ≠ approved baseline. Strategic alignment ≠ causal benefit claims.

**Components / membership.** PortfolioComponent is a directed, addressable membership release from one Portfolio to one external work item. Cardinality is many-to-many. Unrelated components are permitted; membership is not a catalogue and not a type gate. No WBS parentage, no implied Program child-set, no exclusive owner. The same initiative may sit in two portfolios at once.

**Criteria / scoring / prioritization.** Three layers: reusable Selection Criteria Set (definitions, weights, scales); external observations; Prioritization as a portfolio-owned application of a pinned set to current membership. Rank is not written back onto WM-ACT-005/030. Alignment scores are prioritization outputs, not realized-value arithmetic on WM-KNW-011.

**Allocation / funding.** InvestmentAllocation states this portfolio’s intended share or amount for a component in a scenario or cycle. It is not a ledger entry, authority instrument or actual. Oversubscription is a scenario condition to flag externally, not an implicit transfer of ownership or cash.

**Scenarios / decisions.** PortfolioScenario packs membership, pinned criteria-set version, Prioritization, InvestmentAllocation set, and references to external decision records. It does not ingest decision bodies. Approval lives on the decision triad. Baseline is a governance designation of a scenario, not a second type in this package.

**Governance.** Portfolio governs membership, criteria pin, ranking application, allocation intent and scenario choice only. It does not govern execution, budget authority, commitments, actuals, observations or decision issuance. Conflicting ranks of the same work item across portfolios are allowed and unreconciled here. Criteria-set stewardship is outside any one portfolio.

**Time / version / rebalance.** Portfolio-owned releases version per cycle. Criteria-set versions are independent of cycle; a portfolio pins a released set or snapshot rather than forking it. Rebalance emits new Prioritization, InvestmentAllocation and PortfolioScenario. Prior selected scenarios remain immutable evidence. Component-master versions are not portfolio versions.

**Scenario (0.6 / 0.4).** P1 and P2 each hold a PortfolioComponent to the same Initiative. Mastership stays on the initiative. P1 share 0.6, P2 share 0.4. Each selected scenario preserves its criteria-set pin and decision-evidence refs. Unrelated third components may exist in either portfolio. Neither portfolio becomes a Program. Outcomes and actuals are not derived by summing the shares.

**Invariants.**
1. WM-ACT-029 profile does not inherit Program delivery, rollup or exclusive-owner semantics.
2. PortfolioComponent never transfers mastership.
3. A work item may belong to multiple portfolios at once.
4. Membership admits unrelated components; no automatic Program set.
5. Rank is a Prioritization output, not an intrinsic work property.
6. Criteria ≠ observations ≠ ranking.
7. InvestmentAllocation ≠ budget authority ≠ commitment ≠ actual ≠ component funding.
8. Overlapping allocations (0.6+0.4) are permitted as co-funding intent.
9. Actuals, capacity, outcomes and benefits must not be double-counted from those allocations.
10. Selected scenario pins criteria-set version or snapshot and decision-evidence refs.
11. Scenario is not the approved baseline until an external decision says so.
12. Rebalance creates new releases; it does not rewrite prior selected scenarios.

**Minimum model set.** In-model: Portfolio (WM-ACT-029 profile); PortfolioComponent; Selection Criteria Set (unassigned reusable root) + SelectionCriterion; Prioritization; InvestmentAllocation; PortfolioScenario. External refs only: WM-ACT-005, WM-ACT-030, WM-ECO-012, WM-KNW-011, decision triad, observations, actuals, component mastership, budget authority, catalogue.

**Blockers.** (1) Profiling is unsafe if WM-ACT-029 already binds exclusive ownership, child rollup or coordination — write an explicit profile constraint or do not profile. (2) Released criteria-set identity must be stated even without allocating an identifier. (3) Allocation share basis unspecified. (4) No in-model hook to WM-ECO-012 for oversubscription. (5) Decision-triad attachment point unspecified (scenario vs cycle vs portfolio). (6) Strategic-alignment slot vs WM-KNW-011 unspecified; risk of encoding causal benefit claims. (7) Observation authority unspecified; shared sets plus local observations make scores incommensurable. (8) No lifecycle rule when the initiative is cancelled, split or re-mastered.