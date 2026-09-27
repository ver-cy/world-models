**Verdict.** Accept. Commercial Landscape is a read-only derived profile; Market Scope is its versioned parameter set; output is an immutable projection. Neither candidate requires independent business identity. Mastership stays on Party, WM-ORG-014 Customer Account Relationship, WM-ECO-020 Sales Order, and the declared group-boundary assertion.

**Strongest evidence.** The profile/lens/print split prevents dual-write and lets one Party be reused across customer, supplier and partner roles without extra masters. A concentration run stays reproducible under two perimeters only when it names one grouping boundary and one fact key, then set-unions facts. Unknown parents stay reason-coded singletons; disputed links stay attributed ranges; series stay unmixed; cross-controller facts stay gated.

**Strongest counterexample.** Give CL business identity. Party X is customer in P1 and P2 and supplier in P1. The landscape either splits X by role, inflating unique-customer counts and breaking set-union, or collapses X and nets customer receipts against supplier payments, poisoning intercompany elimination. Inventing a parent for uncertain member Y to keep one identity tree manufactures concentration. Treating an MS edition as a business subject double-counts the same WM-ORG-014 and WM-ECO-020 facts as two counterparties.

**Identity/mastership.** Commercial Landscape does not require independent business identity. Market Scope does not require independent business identity; versioning is a technical parameter edition. Projection: reproducibility handle only. Identity lives on Party and on source facts (account relationship, sales order, quote, subscription, campaign, measurement, declared group boundary).

**Market scope.** An edition declares participating perimeters; grouping-boundary type (ownership/control or consolidation); the single active fact key; time window and scenario; intercompany-elimination eligibility; coverage policy; access grant and disclosure shape. Any change yields a new edition. MS stores no revenue, orders or roles. The same facts may project differently under two editions.

**Roles/grouping.** One Party is reused across customer, supplier and partner. Role is a relationship facet, not an identity. Roles are not merged and amounts are not netted. Grouping uses one declared ownership/control or consolidation boundary per run, one fact key, and set-union rollups. Unknown parents remain reason-coded singletons. Disputed links produce attributed ranges.

**Concentration.** Numerator is the set-union of customer-role facts for the grouped subject at the chosen fact key. Denominator is the same fact key over the perimeter after only those eliminations the declared consolidation boundary permits. Dual-role Party X contributes only customer-role facts to customer concentration. Ownership/control alone does not auto-eliminate intercompany.

**Forecast versus fact.** Forecast, pipeline, quote, order, subscription and observed revenue/delivery stay separate and non-substitutable. A projection names exactly one fact key. Coverage is backed, partial, unbacked-open, unbacked-lapsed or unevaluable. Unsupported does not mean false; unevaluable is not a zero. Campaign and measurement may annotate a window; they are not the fact key.

**Time/scenario.** Every projection is as-of one point under one scenario, both pinned by the MS edition. Prior projections stay immutable; restatement is a new projection. Cross-period comparison is valid only when fact key, grouping boundary and elimination rule match or are remapped.

**Access/disclosure.** Cross-controller facts are excluded by default. Inclusion requires an explicit access grant for controller, perimeter, purpose and as-of, plus a disclosure shape (identified, masked, banded or suppressed). No grant means omit or unevaluable; do not infer presence or absence. Disclosure shape is part of the projection key.

**Scenario.** Two perimeters P1 and P2. Party X is customer in both and supplier in P1. Intercompany flow exists between P1 and P2. Group member Y has an uncertain or disputed parent. Evaluate each perimeter separately under the same MS edition. Eliminate P1–P2 only if the declared boundary is consolidation and the pair sits inside it. Keep Y as a reason-coded singleton; if disputed, emit an attributed range. Compute customer concentration from customer-role facts only; do not net X’s supplier amounts. Emit two immutable projections; set-union the group view without merging perimeters.

**Invariants.**
1. CL is read-only and derived; never a system of record.
2. MS is a parameter edition; it owns no parties, accounts or orders.
3. Neither CL nor MS nor the projection has independent business identity.
4. Projection is immutable; correction yields a new projection.
5. One Party may hold customer, supplier and partner roles concurrently; roles are not merged and amounts are not netted.
6. One concentration run uses exactly one grouping boundary and exactly one fact key.
7. Group rollup is set-union; no path double-count.
8. Unknown parent remains a reason-coded singleton; no synthetic parent.
9. Disputed group link yields an attributed range, not a presented point fact.
10. Forecast, pipeline, quote, order, subscription and observed revenue/delivery are non-substitutable series.
11. Coverage is backed, partial, unbacked-open, unbacked-lapsed or unevaluable; unsupported is not false.
12. Intercompany elimination applies only inside a declared consolidation boundary.
13. Other-controller facts require explicit access and disclosure shape, else omitted or unevaluable.
14. Dual-role Party X contributes to customer concentration only through customer-role facts.
15. Two perimeters produce two projections; they are not merged by party identity alone.

**Minimum profile shape.** Subject Party; role qualification; perimeter; declared boundary type; membership as member, singleton-unknown with reason, or disputed with range; fact key; measurement; series kind; coverage state when forecast is shown; access and disclosure stamp; MS edition handle; as-of; scenario; immutable projection stamp.

**Blockers.** Business identity on CL or MS; in-place projection edits; netting dual-role amounts; mixing fact keys; inventing parents; replacing a disputed range with a point; eliminating intercompany outside consolidation; substituting forecast or pipeline for order or observed revenue; other-controller facts without access and disclosure; treating unsupported as false.
