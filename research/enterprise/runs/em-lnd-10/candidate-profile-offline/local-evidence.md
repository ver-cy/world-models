# EM-LND-10 local synthesis

## Disposition

- Treat **Finance Landscape** as a governed profile declaration plus reproducible projection over existing plan, posting, balance and statement masters.
- Treat **Finance View Policy** as a pinned policy/rule revision, not an aggregate.
- Reuse WM-ECO-012/015/016/017/018, WM-ORG-012, WM-ECO-038 and WM-MAT-008.
- Require the unallocated Responsibility Centre, Consolidation Scope/Run, Chart of Accounts/Mapping, Cost Allocation, Metric Definition, FX Rate Set and Intercompany Match boundaries from prior research.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Plans remain mastered by WM-ECO-012, accounts by WM-ECO-015, postings by WM-ECO-016, balances by WM-ECO-017 and statement issues by WM-ECO-018. Organizational relations, holdings and observations retain their own masters.

The landscape stores only scope revisions, input pins, derived rows and a gap/conflict register. Its output is an immutable digest-addressed artifact, not a subject root and never reimported as source fact. Corrections go to the source master.

Finance View Policy revisions pin book set, ledger revisions, period/cutoff, scenario, responsibility scope, framework, chart/mapping, consolidation scope/run, currency/rates, transformations, elimination and allocation rules, knowledge cut, comparability and residual disclosure. Missing required pins block the view.

## Plans, actuals and responsibility

Plan, ceiling, allocation, availability, commitment, forecast, actual posting and cash remain parallel states with distinct authority. A plan/actual pair is comparable only if book, framework, mapping, responsibility scope, period, currency and recognition basis agree or an authorized bridge is pinned.

Every row names one book and ledger revision. Ledger account identity is ledger, code and effective version. Responsibility uses an effective Responsibility Centre version, not a bare organizational-unit identifier. Reorganization creates successor versions without rewriting history.

## Consolidation and elimination

Every perimeter is purpose-qualified. Inclusion requires control basis, authority, evidence and interval; common ownership is insufficient. Consolidated figures pin Consolidation Scope and immutable Consolidation Run.

Eliminations post only to consolidation books, cite both legs and a matching key, and expose matched, unmatched and residual amounts. An unmatched leg becomes a visible break, never a silent one-sided entry.

## Currency, period and comparability

Transaction, functional and presentation currencies remain explicit. Rate, type, date, source and rate-set version are pinned. Amounts from different currencies, periods, books, bases or scenarios are never added without a named authorized transformation.

Every row is classified comparable, bridged or not comparable, with the blocking axis recorded. Translation and transformation preserve source amounts and provenance.

## Allocation and residuals

Cost allocation is analytical attribution, not a posting. Within one run, axis and currency, allocated results plus materialized residual equal the source within tolerance. Parallel allocation axes are non-additive.

Untagged, unmatched and unallocated amounts are first-class rows with reason and share. Any total excluding them discloses the exclusion. Residual suppression fails the view.

## Projection, time and governance

Event, posting, cutoff, run, issue, observation, ingestion and knowledge times remain distinct. A view resolves source revisions and policies valid at both its world time and knowledge cut.

Output carries digest, all input pins, policy revision, rule versions, completeness declaration and gap/conflict register. Scope changes, transformations, post-cutoff adjustments and published projections require recorded authority.

## Acceptance result

L-STAT uses EUR and L-MGMT uses USD; presentation is GBP. The plan comes from a pinned WM-ECO-012 revision and actuals from pinned postings and balances. One intercompany sale is eliminated with both legs and an FX residual. One cost pool remains unallocated with a reason. A request for combined GBP spend without a rate set and cross-book transformation is blocked; the view returns per-book subtotals, elimination residual, unallocated share, missing policy fields and required transformation rules.

## Required invariants

1. Plan, posting, balance, statement and derived-row identities remain distinct.
2. Every row names book and ledger revision.
3. No cross-currency, cross-period, cross-book, cross-basis or cross-scenario arithmetic occurs without an authorized transformation.
4. Every figure pins period, currency, basis, framework, mapping and knowledge cut.
5. Eliminations post only to consolidation books and disclose residuals.
6. Allocated plus residual equals source within one run, axis and currency.
7. Parallel allocation axes are non-additive.
8. Residual and unallocated shares are never hidden.
9. Source facts are read-only.
10. Views are immutable and declare completeness.
11. Comparability is classified, never assumed.
12. Perimeter membership grants no access.

## Holds

Responsibility Centre, Consolidation Scope/Run, Chart of Accounts/Mapping, Cost Allocation, Metric Definition, FX Rate Set and Intercompany Match remain unallocated. WM-ECO-018 contradicts its out-of-scope boundary by claiming consolidation ownership; WM-ECO-018/017 composition direction conflicts; WM-ECO-015/016 relation types disagree; WM-ECO-012 has no approved outgoing relations; WM-ORG-012 parentage and WM-MAT-008 cardinality remain unsettled. Crosswalks, immutable pins, fixtures and independent review are absent. No installability or publication-readiness claim is made.
