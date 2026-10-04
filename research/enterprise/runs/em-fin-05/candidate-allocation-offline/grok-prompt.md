# Exact unsent Grok prompt — EM-FIN-05

Independent enterprise metamodel review. Do not browse, invent identifiers or claim standards conformance.

EM-FIN-05 covers CostRecord, UsageRecord, AllocationRule and UnitCostObservation. Reserved WM-ECO-002 Price/Valuation excludes accounting recognition. Adjacent masters are WM-FLW-015 Resource Consumption, WM-MAT-008 Observation, WM-ECO-008 Invoice and WM-ECO-016 Journal Entry.

Assess this proposal: keep quoted price, invoice amount, recognized cost, usage, allocated cost and valuation distinct; reuse WM-FLW-015 for usage and WM-MAT-008 plus Metric Definition for unit-cost observations; create one identifier-unassigned Cost Allocation aggregate containing versioned Rule, immutable Run and Results; retain billed/recognized masters and use typed derived Cost Records. Each run has one axis and currency, allocated plus residual equals source amount, and parallel project/product views are non-additive. Unused reserved capacity and discounts have explicit treatments.

Test a shared cloud invoice with a discount, reserved capacity, project and product views and untagged usage. Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; allocation aggregate boundary; unit economics; currency/time; scenario; at least 10 invariants; minimum completion shape; blockers. Explicitly decide whether Rule, Run and Result need separate model identifiers and whether UnitCostObservation can profile existing observation/metric models.
