# EM-FIN-05 local synthesis

## Disposition

- Reject WM-ECO-002 Price / Valuation as the master for costs or allocations. It remains a price/valuation comparator only.
- Reuse WM-FLW-015 for Usage Records under a FinOps profile; reuse WM-MAT-008 plus the EM-DAT-05 Metric Definition candidate for Unit Cost Observations.
- Keep billed cost in WM-ECO-008 and recognized cost in WM-ECO-016. Derived effective, amortized, accrued-unbilled and allocated cost use typed, run-scoped Cost Records and never replace their source masters.
- Create one identifier-unassigned **Cost Allocation** aggregate candidate owning versioned Allocation Rule, immutable Allocation Run and contained Allocation Results. Separate model identifiers for Rule/Run/Result are not justified before registry review.
- Reuse commercial-contract or commitment authorities for reserved-capacity instruments; do not allocate another identifier merely because the dossier lacks their binding.
- Allocate no runtime/model identifier.

## Price, cost and usage boundaries

Quoted/list price, invoice amount, ledger-recognized cost, measured usage, allocated cost and valuation are distinct facts. Invoice allowances remain invoice-owned; ledger postings remain ledger-owned; usage remains source-qualified physical or computational consumption. An allocation produces an analytical attribution and is never a posting unless an authorized journal entry is separately created.

## Allocation aggregate

Allocation Rule has stable identity, immutable versions and effective periods. It declares one allocation axis, source scope, base kind and source, weight computation, rounding/tolerance, residual policy, confidence policy and authority.

Allocation Run pins one rule version, source amount/currency, source records, base population/completeness, execution actor/time and reconciliation result. Contained Allocation Results name target, amount, weight, base value, confidence and attribution basis. Corrections create successor runs.

Conservation holds within one run, one axis and one currency: allocated results plus visible residual equal the source amount within tolerance, and total weights do not exceed one. Parallel project and product views are non-additive. A report must select one run per source amount.

Reserved capacity separates covered usage from unused commitment capacity. Unused capacity is charged to a declared shared pool, allocated by its own rule or left as residual. Discounts retain the invoice allowance identity and gain only a run-specific attribution basis.

## Unit economics, currency and time

A Unit Cost Observation is numerator over denominator: a named cost basis and allocation run divided by a versioned functional-unit definition and measured quantity. It states period, currency, target scope and excluded residual share. Changing the useful-result definition creates a new metric-definition version.

Allocation occurs in the source currency. Translation records rate, type, date and authority per result. Billing period, usage interval, posting/effective dates, commitment period, run time and observation time remain separate.

## Acceptance scenario

A cloud invoice contains gross cost, discount and reserved-capacity effects. One project-axis run allocates metered usage to projects, sends unused reservation to a shared pool and leaves untagged usage as residual. One product-axis run uses a service-to-product rule and has a different residual. Each run conserves independently and cannot be summed with the other. Product unit cost cites the selected run, functional-unit definition and residual share.

## Invariants

1. Every cost assertion declares basis, period and currency.
2. Price, invoice, recognized cost, usage, allocation and valuation are never substituted.
3. Every run pins one immutable rule version.
4. Allocated results plus residual equal source amount within one run/axis/currency.
5. Total weights never exceed one; residual is materialized.
6. Parallel allocation axes over the same source are non-additive.
7. Allocation base kind and completeness are explicit.
8. Unused reserved capacity has a declared treatment.
9. Discount attribution retains the source allowance identity.
10. Allocation occurs before any currency translation of results.
11. Allocated cost is not a ledger posting.
12. Corrections append successor runs and preserve prior metric vintages.
13. Confidence separates measurement uncertainty, representativeness and residual share.
14. Unit cost pins numerator basis, allocation run and denominator definition version.

## Holds

All relevant bases remain non-canonical reviewable drafts; WM-ECO-002 has no approved outgoing relations, and usage/measurement models retain single-provider and allocation/profile holds. Cost Allocation and Metric Definition lack registry allocation; the contract/commitment binding, FOCUS/FIBO/ERP crosswalks, immutable pins and fixtures remain incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
