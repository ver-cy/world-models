Verdict: Conditional accept. Keep quoted price, invoice amount, recognized cost, usage, allocated cost, and valuation as distinct facts. Reuse WM-FLW-015 for usage and profile unit cost onto WM-MAT-008 plus Metric Definition. Reject an identifier-unassigned allocation aggregate. Rule, Run, and Result need separate model identifiers. UnitCostObservation can profile the existing observation and metric models and must not become a second observation master.

Strongest evidence: the six facts have different lifecycles and different masters. Quoted price is a commercial offer under WM-ECO-002 and is outside accounting recognition. Invoice amount is billed fact on WM-ECO-008 and can be disputed after usage is already recorded. Recognized cost posts only through WM-ECO-016 at period close. Usage quantity is operational and mastered by WM-FLW-015. Allocated cost is a derived view of a source amount. Valuation is not recognition. Collapsing any pair hides a dispute, a close, or a double count. The cloud case needs all six: a discount changes billed versus list, reserved capacity can be unused, and untagged usage must stay visible.

Strongest counterexample: one shared cloud invoice, list 1,200 in currency C for period T, invoice-level discount 120, billed 1,080. Reserved commitment 600, of which part is unused; on-demand covers the rest. Project A consumes part of the reserved pool and some on-demand. Product B attributes an overlapping slice of the same reserved pool by SKU. Ten percent of on-demand is untagged. If the project view and the product view are added, reserved cost is counted twice against the invoice and against WM-ECO-016. If unused reserved capacity is dropped, allocated plus residual no longer equals the source. If the discount is applied only to tagged usage, the untagged residual no longer reconciles to the billed net. A single run cannot be both axes at once.

Identity and mastership: do not mint masters for usage or unit cost. UsageRecord is a profile of WM-FLW-015 Resource Consumption; allocation never creates usage. UnitCostObservation profiles WM-MAT-008 Observation plus Metric Definition: subject, time, unit, and value stay with the observation; the profile adds cost numerator, usage denominator from WM-FLW-015, currency, window, and allocation-run context. It does not store allocation keys as a new identity. Billed amount stays on WM-ECO-008. Recognized amount stays on WM-ECO-016. WM-ECO-002 remains price and valuation only. Cost Records are typed derived facts pointing at a Result, not a new master and not a journal.

Allocation aggregate boundary: one Cost Allocation aggregate, root = Run. Rule is a versioned policy, referenced by version, reusable across runs, not exclusively owned. Run is the immutable execution identity that Cost Records and audit cite. Result lines are stable derived facts (target, amount, residual flag, source invoice reference, usage references) so a later explanation can point at a line. Leaving the aggregate identifier-unassigned blocks citation from derived Cost Records. Results never mutate Invoice or Journal Entry.

Unit economics: unit cost is computed, not mastered. Numerator is a stated cost basis (source slice, allocated amount, or recognized amount — named, not mixed). Denominator is usage from WM-FLW-015. A Metric Definition fixes the ratio. Discount timing is a versioned rule attribute: reduce the source before allocation, or carry discount as its own residual. Both are legal; silent netting is not. Unused reserved capacity is an explicit waste or residual result on the commitment, never omitted. Untagged usage stays in an unassigned residual. No implicit default tag.

Currency and time: each Run has one axis and one currency, equal to the source invoice slice. No implicit FX inside a run. Cross-currency lines are out of scope until a conversion rule exists. The run window is the source period. Rule version is pinned at run close. A closed run is immutable; a correction is a new run.

Scenario: source commitment 600 plus on-demand 400 = 1,000 list; discount 100; billed 900. Rule version: discount pro-rata on billed usage before allocation; unused reserved is residual waste; untagged is residual unallocated. Project-axis run allocates Project A and leaves residual for unused reserved and untagged. Product-axis run allocates Product B from the same source and leaves its own residual. Each run satisfies allocated plus residual equals source. The two runs are alternative partitions and must not be summed. Unit-cost observations profile WM-MAT-008 for each result basis. Neither run posts to WM-ECO-016.

Invariants:
1. Quoted price, invoice amount, recognized cost, usage quantity, allocated cost, and valuation are distinct facts.
2. Usage quantity is mastered only by WM-FLW-015.
3. Recognition posts only through WM-ECO-016; allocation does not post journals.
4. WM-ECO-002 does not perform accounting recognition.
5. Each Run has exactly one allocation axis and one currency.
6. Allocated amount plus residual amount equals source amount in the run currency.
7. Project-axis and product-axis results are alternative views and are non-additive.
8. Discount treatment is explicit on the pinned rule version.
9. Unused reserved capacity is an explicit residual or waste result.
10. Untagged usage remains residual or unassigned; no implicit tag.
11. Run is immutable after close; rule version is pinned on the run.
12. A Result never updates Invoice or Journal Entry masters.
13. Unit cost is a profiled observation over a Metric Definition, not a second usage record.
14. Cost Records are typed and derived; they cite a Result.

Minimum completion shape: aggregate specification with separate identifiers for Rule, Run, and Result; root = Run; rule referenced by version; conservation equation; non-additivity of parallel axes; explicit discount and unused-capacity result types; typed derived Cost Records; unit-cost profile on WM-MAT-008 plus Metric Definition; the shared-invoice scenario as the acceptance test.

Blockers: an identifier-unassigned aggregate cannot be cited by Cost Records. A new UnitCostObservation master would duplicate WM-MAT-008. Multi-currency source without a conversion rule breaks one-currency-per-run. Residual policy for discount versus unused capacity must be stated on the rule, not inferred. No model identifiers are assigned here.
