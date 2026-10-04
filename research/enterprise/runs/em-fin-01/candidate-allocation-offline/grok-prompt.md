# Independent review request: EM-FIN-01 Budget, responsibility centre and funding

Act as an independent enterprise finance information-architecture reviewer. Use public sources only and do not request private financial records.

Primary existing model:

- WM-ECO-012 Budget: https://ver.cy/models/wm-eco-012-budget/
- EM-FIN-01 assignment: https://ver.cy/enterprise/models/em-fin-01/

Other relevant Vercy boundaries are WM-ORG-002 Organizational Unit, WM-ORG-004 Position, WM-ECO-016 Financial Transaction / Journal Entry and WM-XCT-032 Currency / Monetary Value.

Local and Claude review concluded:

1. Reuse WM-ECO-012 for budget revisions, scenarios, ceilings, funding sources, allocation/allotment, amendments, forecasts, actual references and variance.
2. Add a thin Enterprise profile requiring version-pinned responsibility-centre references and conservation rules.
3. Create a new cross-domain Responsibility Centre entity because cost-centre codes are consumed by several models but no authoritative centre master exists.
4. Keep Funding Allocation inside WM-ECO-012 rather than creating another aggregate.

Test:

- whether a responsibility centre has identity/lifecycle independent of organizational unit, position, legal entity, ERP code, budget line and journal posting;
- how it survives reorganization, merge/split and code changes without rewriting historical attribution;
- version-scoped manager/accountability, ledger, chart/segment, currency, measurement-basis and hierarchy bindings;
- whether funding allocation belongs inside the budget aggregate;
- conservation across multiple funding sources, residual rules and cross-budget sources;
- comparison of original budget, revised budget, forecast, commitments and actuals without conflation.

Acceptance scenario: two funding sources finance one project; then an organizational reorganization and budget revision occur. Historical postings retain the centre version effective when recorded, plan/forecast/actual remain distinct and no funding amount becomes available twice.

Choose exactly: REUSE ONLY, PROFILE, NEW MODEL, or a justified combination. Do not assign a numeric model identifier.

Return no more than 1000 English words with headings:
DECISION
BUDGET BOUNDARY
RESPONSIBILITY CENTRE BOUNDARY
FUNDING CONSERVATION
ACCEPTANCE SCENARIO
HOLDS AND PUBLICATION RECOMMENDATION
