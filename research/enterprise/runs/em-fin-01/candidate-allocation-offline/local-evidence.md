# EM-FIN-01 local synthesis

## Disposition

- **Reuse WM-ECO-012 Budget** for budget identity, immutable revisions, scenarios, ceilings, funding sources, allocations, amendments, forecasts, actual references and variance.
- Create a thin **EM-FIN-01 Budget Responsibility profile** requiring version-pinned responsibility-centre references and source-side conservation rules.
- Research a **new Responsibility Centre entity**. Its identifier remains unassigned.
- Keep Funding Allocation inside WM-ECO-012.

## Responsibility Centre boundary

A responsibility centre is a finance-governed accountability unit whose lifecycle differs from organizational units, positions, legal entities, budget lines and journal postings. Published models already consume cost-centre codes but no authoritative centre master or reserved registry entry exists.

Owned semantics: persistent centre identity; immutable/effective-dated versions; centre type; aliases and ERP codes; accountable position; accountability scope; legal-entity, ledger, chart/segment and currency bindings; hierarchy; associated organizational units; succession and split/merge rules; posting-eligibility window; authority and evidence.

## Key invariants

1. Centre identity is never an organizational-unit id, ERP code or journal dimension value.
2. Centre versions have non-overlapping effective intervals.
3. A posting pins the centre version effective at posting/accounting time.
4. Reorganization never rewrites historical postings.
5. Centre merge/split creates lineage with explicit weights or reconciliation rules.
6. Alias codes are dated and resolve to one centre per instant.
7. Accountability is assigned to a position/role reference, not copied person data.
8. Currency, measurement basis and ledger binding are explicit and version-scoped.
9. Hierarchies are acyclic and may differ from organizational hierarchies.
10. Referenced versions remain resolvable after closure.

## Funding allocation profile

Every allocation declares source, destination centre version, amount or weight, allocation basis, effective period, restrictions, authority and residual rule. The sum of allocations from one released source cannot exceed the released amount for that period. Residual reconciliation is mandatory. Cross-budget conservation requires a shared funding-source identity and source-side released-amount authority.

## Acceptance result

Two sources fund a project through Budget revision r1 and Centre v1. Reorganization creates Centre v2 only when financial accountability changes; previous postings remain pinned to v1. Budget revision r2 and its forecast do not mutate r1 or actuals. Reconciliation rolls up v1/v2 through centre lineage while source-side conservation prevents double availability.

## Holds

WM-ECO-012 is a reviewable draft under a single-provider waiver and lacks approved relations. The Responsibility Centre model needs independent review, registry allocation, ledger/posting field validation and jurisdiction-specific finance review. Standards remain alignment targets only.
