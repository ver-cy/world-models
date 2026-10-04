# EM-FIN-05 — Independent review

## Verdict

Reserved **WM-ECO-002 Price / Valuation is not an acceptable target** for this contour. Disposition is partial reuse plus two new candidates (identifiers unassigned):

- **UsageRecord** — reuse **WM-FLW-015 Resource Consumption** under a thin EM-FIN-05 profile; mint no new identity.
- **CostRecord** — no new master for billed or ledger-recognized cost; typed assertion with a mandatory `cost_basis` discriminator. Identity is minted **only** for derived bases (effective, amortized, accrued-unbilled, allocated).
- **AllocationRule** — **new**, independently identified and versioned, with **AllocationRun** and **AllocationResult** as separate identities.
- **UnitCostObservation** — **new** derived-metric identity; ALIGN to WM-ECO-002's amount/unit/time/provenance/uncertainty pattern, not mastered inside it.

Boundary decision: **new + profile**, not reuse of the reserved entry.

## Evidence

WM-ECO-002 `out_of_scope` names "accounting recognition, tax rules"; its Invoice/Payment boundary note states invoiced and paid amounts "are external accounting or settlement events; they may evidence price but do not become appraisal or index conclusions." Its cost bundle is replacement/reproduction cost *for valuation*, not incurred cost. A unit cost whose numerator is allocated recognized cost therefore cannot be mastered there without breaching its own stated boundary.

WM-FLW-015 already owns assertion-kind typing (metered/derived/allocated/estimated/modeled), gross/return/recovery/export/loss/net components, `shared-resource-allocation-driver-rule-basis-and-residual`, `functional-unit…normalizing-variable-and-intensity`, `allocate-shared-use` (outputs allocated assertions **plus residual**), and `reconcile-sources` rejecting last-write-wins. That is the usage side, already source-grounded.

WM-ECO-008 owns allowance/charge entries with reason code and their own tax category at line and document level, prepaid amount, document and tax-accounting currency. WM-ECO-016 owns per-ledger balancing, immutability, correction linkage and parallel-ledger divergence. WM-MAT-008 owns the measurement act.

## Identity/mastership

Independent identity and lifecycle: **AllocationRule**, **AllocationRun**, **AllocationResult**, **UnitCostObservation**, **CommitmentInstrument** (reserved capacity / savings commitment, if no contract master is available).

Reuse current masters, reference only: invoice and its allowances (WM-ECO-008), postings and recognized amounts (WM-ECO-016), measured usage (WM-FLW-015), meter observations (WM-MAT-008), market/quoted price and valuation (WM-ECO-002), allocation targets (project, product, responsibility centre — externally mastered).

AllocationRule needs its own identity because it is authored, approved, effective-dated and retired independently of any execution; AllocationRun needs its own because residual, confidence and reconciliation attach to an execution, not to the rule.

## Price/cost/usage boundaries

Six distinct facts, never interchangeable:

1. **Quoted/list price** — WM-ECO-002 price observation (advertised, quoted, administered).
2. **Invoice amount** — WM-ECO-008 line/document totals net of invoiced allowances.
3. **Ledger-recognized cost** — WM-ECO-016 posting in a named ledger, under that ledger's recognition policy.
4. **Measured usage** — WM-FLW-015 quantity with quantity kind, unit and net-component treatment.
5. **Allocated cost** — AllocationResult; derived, run-scoped, never a posting.
6. **Valuation** — WM-ECO-002 appraisal conclusion.

A rate card is (1), not (2). An invoice is not (3): commitment amortization, credits landing in later periods and accruals make them legitimately unequal. Allocated cost (5) is never posted back as (3) unless an explicit allocation posting is authorized as its own journal entry.

## Allocation rule and execution

AllocationRule declares: version and effective interval; **allocation axis** (the target dimension set, e.g. project *or* product); source scope (invoice, invoice group, cost pool, posting set); **allocation base** (metered usage, derived usage, headcount, revenue, fixed key, equal split) with the base's own assertion kind; base source binding; weight computation; rounding rule and tolerance; **residual policy**; confidence policy; authority and approval.

AllocationRun is immutable and records rule version, source amount and currency, base population and its completeness, execution time, actor, results, residual and reconciliation outcome. AllocationResult carries target reference, amount, weight, base value, confidence and the run reference.

**Duplication control (the negative case).** Conservation holds *within one run and one axis*: `Σ allocated + residual = source amount`, and `Σ weights ≤ 1`. Project-axis and product-axis runs over the same source are parallel views, each independently conserving. Cross-axis results are declared **non-additive**: any report summing allocated cost must name exactly one run per source amount, and summing two runs of the same source is a rejected operation. This is what prevents 100% of a shared invoice appearing against every product.

**Shared/reserved capacity.** Reserved or committed capacity is allocated in two layers: (a) covered usage attracts the commitment rate; (b) **unused reserved capacity** is an explicit cost with no consuming target and is allocated by a declared rule (spread, charged to a shared pool, or left in residual) — never silently absorbed into consumers' unit cost.

**Discounts.** Invoiced discounts are mastered in WM-ECO-008 as allowance entries with reason codes; EM-FIN-05 owns only their **attribution**: whether a discount follows the line it was granted against, is spread across the axis on the same base, or is held in a shared pool. Attribution basis is recorded per result so gross and net allocated views are both reproducible.

## Unit economics

UnitCostObservation = numerator (a stated CostRecord basis, one run, one axis) ÷ denominator (a functional unit taken from WM-FLW-015's normalizing variable). It must state numerator basis, run reference, denominator definition and version, period, currency, target scope and the unallocated share excluded. "Unit of useful result" is a declared, versioned choice (request, transaction, active tenant, delivered item), not a discovered fact; changing it creates a new definition version, not a restated metric.

## Currency/time

Allocate in the **source amount's currency**, then translate results with rate, rate type, rate date and source recorded per result. Never allocate a translated amount and re-translate. Residual carries its own currency. Where the source is an invoice, transaction currency and any tax-accounting currency are read from WM-ECO-008 and not re-derived.

Separate: billing period (invoice), usage interval (WM-FLW-015), accounting effective and posting dates (WM-ECO-016), commitment amortization period, allocation run execution instant, and metric as-of. Every cost and usage assertion states period and currency explicitly; date-only periods are not widened to instants.

## Reconciliation/correction

Three independent ties, each recorded with variance and reason rather than forced to zero: allocated total ↔ source invoice total; allocated/amortized total ↔ ledger-recognized cost for the period; allocation base ↔ measured usage population completeness. Unallocated remainder is reported, never suppressed.

Corrections are append-only: a superseding AllocationRun referencing its predecessor with reason (restated usage, corrected invoice, credit note, rule defect, base completeness fix). Prior runs and prior UnitCostObservation vintages remain resolvable. Invoice corrections arrive as WM-ECO-008 credit/corrective documents; ledger corrections as WM-ECO-016 reversing entries. Neither rewrites a run.

**Confidence** stays decomposed: measurement uncertainty (from usage/observation), base representativeness, commitment-coverage certainty, and unallocated share. No single collapsed score.

## Lifecycle

AllocationRule: draft → approved → effective → superseded → retired. AllocationRun: executed → reconciled → superseded (immutable throughout). AllocationResult: immutable, lives and dies with its run. UnitCostObservation: issued → superseded/withdrawn, preserving vintages. CostRecord: basis-dependent — billed and recognized follow their masters; derived bases are revisioned locally.

## Scenario

One shared cloud invoice: gross 100,000 EUR, invoiced volume discount 10,000, billed 90,000; plus a reserved-capacity commitment whose period amortization is 20,000, of which 4,000 is unused reservation.

- Amortized cost basis for the period: 90,000 + 20,000 − (commitment prepayment already invoiced, per prepaid amount) = a stated effective pool, recorded as one derived CostRecord with its computation.
- **Project run** (axis = project), base = metered compute usage: Project A 48,000, Project B 31,000, unused reservation 4,000 to shared pool, **residual 7,000** (usage from untagged resources, base incomplete). Σ = pool. Confidence: metered for A and B, estimated for the untagged share.
- **Product run** (axis = product), same pool, base = derived usage mapped via service-to-product rule v2: Product X 55,000, Product Y 29,000, **residual 6,000**. Σ = pool.
- Both runs conserve independently. Neither is summed with the other. A cross-axis report must name one run; the project+product sum of 174,000 against a 90,000-billed invoice is a rejected operation, which is precisely the negative case.
- Unit cost: Product X effective cost 55,000 ÷ 11.0m billable requests, with residual share 6.7% declared and run reference pinned.

## Invariants

1. Every cost assertion states `cost_basis`, period and currency.
2. Quoted price, invoice amount, recognized cost, measured usage, allocated cost and valuation are separately typed and never substituted.
3. AllocationRule is versioned; every run pins one rule version.
4. `Σ allocated + residual = source amount` within one run, one axis, one currency, to a declared tolerance.
5. `Σ weights ≤ 1`; the unallocated remainder is materialized and visible, never zero by default.
6. Allocated results from different axes/runs over the same source are non-additive.
7. Allocation base assertion kind and completeness are recorded per run.
8. Unused reserved capacity is an explicit cost with a declared treatment.
9. Discount attribution basis is recorded per result; gross and net views are both reproducible.
10. Allocation occurs in source currency; translation records rate, type, date and source.
11. Allocated cost is not a ledger posting unless an authorized allocation journal entry is created in WM-ECO-016.
12. Runs and metric vintages are immutable; correction supersedes with reason and preserves predecessors.
13. Confidence remains decomposed, not collapsed.
14. Unit cost states numerator basis, run reference, denominator version and excluded unallocated share.

## Minimal completion shape

EM-FIN-05 profile over WM-FLW-015 (usage, with allocation-axis and base-completeness constraints) + new AllocationRule / AllocationRun / AllocationResult + new UnitCostObservation + new CommitmentInstrument + typed references to WM-ECO-008 (invoice, allowances, prepaid), WM-ECO-016 (recognized cost, allocation postings), WM-MAT-008 (measurement evidence), WM-ECO-002 (price comparator only). Target masters (project, product, responsibility centre) referenced, never governed here.

## Holds

All four adjacent specifications are non-canonical reviewable drafts. WM-ECO-002, WM-FLW-015 and WM-MAT-008 carry single-provider waivers with external review explicitly waived; WM-ECO-002 has no approved outgoing relation rows, so a WM-ECO-002 edge cannot be relied on. WM-FLW-015 holds allocation, profile, measurement and impact items open; WM-MAT-008 is `boundary-review-required` with unverified cardinalities and an entry-kind mismatch between its registry record plane and its subject kind. Semantic crosswalks, registry allocation for the new candidates, immutable source pins, comparison-track validation (FIBO, UBL/FOCUS, XBRL/ERP policy) and fixtures are all absent. Jurisdictional cost-allocation, transfer-pricing and tax treatment are out of scope and unreviewed. This review makes no claim of canonical completeness, publication readiness or installability.
