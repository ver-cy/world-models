# Frozen no-tools semantic audit — EM-LND-10

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

The result is a PROFILE over WM-ECO-012/015/016/017/018, WM-ORG-012, WM-ECO-038 and WM-MAT-008. Finance Landscape is a governed declaration plus immutable reproducible projection. Finance View Policy is a pinned policy/rule revision. No new runtime/model identifier is proposed.

Reconciled boundary:
1. Landscape identity equals the governed profile plus complete pins. Identical pins reproduce the same projection; changed pins or policy revisions create a new immutable issue.
2. View Policy identity equals policy family plus revision. It pins books, ledger revisions, periods, scenarios, framework, chart mapping, responsibility scope, consolidation scope/run, rates, transformations, elimination, allocation, knowledge cut and residual policy.
3. Plans, forecasts, postings, balances, statements, holdings, observations and derived rows remain distinct. Source facts remain read-only masters.
4. Plan/actual comparison requires pinned period, mapping, responsibility scope and currency policy. Governed variance metrics require an allocated Metric Definition.
5. Every row names one book and ledger revision. WM-ORG-012 units are not inferred to be Responsibility Centres.
6. Cross-book totals require an authorized cross-book transformation. Cross-currency totals also require an authorized FX Rate Set and translation method. Source currency is preserved.
7. Elimination requires pinned Consolidation Scope, Consolidation Run, Intercompany Match, both legs and authorized transformation. Unmatched items remain visible.
8. Allocation creates derived rows only. Allocated plus residual equals source within one run, axis and currency. Parallel axes are non-additive.
9. Period, ledger revision and knowledge cut are mandatory. Derived rows cite source facts, policy revision and transformation steps.
10. Missing required pins block issue. Registration grants no authority to post, value, eliminate, allocate, disclose or publish.
11. Responsibility Centre, Consolidation Scope/Run, Chart of Accounts/Mapping, Cost Allocation, Metric Definition, FX Rate Set and Intercompany Match remain unallocated holds.
12. Base relation contradictions and missing canonical pins remain publication holds.

Scenario: L-STAT uses EUR, L-MGMT uses USD and presentation is GBP. A plan and actual are compared through pinned mappings and responsibility scope. An intercompany pair is eliminated only with both legs and pinned consolidation/match controls. One cost remains unallocated and visible. A request for a combined GBP total without an authorized rate set or cross-book transformation fails and returns separate subtotals plus missing pins and residuals.

Audit questions:
- Is there a hidden aggregate or identifier despite `newRuntimeId=false`?
- Are source, landscape, policy, projection and derived-row mastership unambiguous?
- Are plan/actual, cross-book, currency, consolidation, elimination and allocation semantics safe?
- Can the scenario be reproduced without remastering source facts?
- Identify any contradiction that makes even a held profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model publication blockers as holds unless they contradict the profile.
