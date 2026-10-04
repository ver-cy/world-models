## Verdict
**ACCEPT WITH LIMITS** — the profile is internally coherent and safe *while held*. No contradiction defeats a held profile; nothing here is issuable in the scenario's full form.

## Critical findings
1. **Shadow-master risk in the projection (primary hidden-aggregate vector).** Clause 1 makes the projection immutable and reproducible from pins; clauses 7–8 make elimination and allocation products of a pinned Consolidation Run and allocation run. If the projection *recomputes* eliminated or allocated rows instead of citing run-produced derived rows, the Landscape becomes a de facto master of consolidated results and a standing aggregate under a declaration identity. Clause 9's citation duty implies but does not state citation-only.
2. **Scenario's affirmative paths depend on unallocated constructs.** Clauses 2/4/6/7/8 require pins on Responsibility Centre, Chart of Accounts/Mapping, Consolidation Scope/Run, Intercompany Match, Cost Allocation, Metric Definition and FX Rate Set — all unallocated holds under clause 11. With clause 10, the pinned plan/actual comparison and the pinned elimination narrated in the scenario cannot be issued today; only rehearsed unpublished.
3. **No governed variance is available.** Clause 4 requires an allocated Metric Definition; clause 11 withholds it. Plan/actual yields paired rows and a stated difference only, never a governed variance metric.
4. **Responsibility scope is currently unsatisfiable.** Clause 5 bars inferring Responsibility Centres from WM-ORG-012 units, and Responsibility Centre is unallocated, so "pinned responsibility scope" has no legitimate referent yet.
5. **Ledger-revision containment gap.** Clause 2 pins ledger revisions at policy level; clause 5 names one per row. No rule requires row-level revisions to be a subset of the policy-pinned set — a reproducibility leak.
6. **Conservation currency.** Clause 8's allocated-plus-residual identity holds only in source currency (clause 6); GBP presentation must never be used to test it.

Mastership is otherwise unambiguous: source facts read-only masters; policy masters rules by family+revision; Landscape masters nothing; derived rows master nothing and cite sources, policy revision and steps. Reproduction needs no remastering, given read-only sources, mandatory knowledge cut, and no write-back of variance, eliminations or allocations into ledgers.

## Required holds
- All clause 11 unallocated holds retained; add: projection is citation-only and may not recompute or restate run-produced derived rows.
- Explicit containment rule: row ledger revision ⊆ policy-pinned revisions.
- Conservation testable only in source currency; presentation currency non-authoritative.
- No governed variance, cross-book total, cross-currency total, elimination, allocation, disclosure or publication authority from registration (clause 10).
- Missing canonical pins and base-relation contradictions remain publication holds (clause 12) — held, not contradicting.

## Scenario result
The negative path is correct: the combined GBP total fails absent an authorized FX Rate Set and cross-book transformation, returning separate EUR (L-STAT) and USD (L-MGMT) subtotals, the missing-pin list and the visible unallocated residual. The affirmative paths — plan/actual comparison and intercompany elimination — are **held**, not accepted, pending allocation of their pinned constructs. Source currencies preserved; unmatched and unallocated items remain visible.

## Identifier decision
No new runtime or model identifier. `newRuntimeId=false` sustained: Landscape issues are keyed by governed profile plus complete pins; View Policy by family plus revision. Both are non-mastering. Sustained only with the citation-only hold; without it, an aggregate identity emerges and the decision must be reopened.
