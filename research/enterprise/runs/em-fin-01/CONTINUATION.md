# EM-FIN-01 continuation

## State

The budget, responsibility-centre and funding contour is provider-reconciled and frozen-audited. Claude and Grok agree on the smallest composition:

- reuse WM-ECO-012 for Budget identity, revisions, scenarios, ceilings, funding sources, allocations, allotments, amendments, forecasts, commitment/actual references and variance;
- add a thin declarative Budget Responsibility profile over WM-ECO-012, with WM-XCT-032 monetary semantics;
- retain Responsibility Centre as an identifier-unassigned **NEW MODEL**;
- keep Funding Allocation inside the Budget revision.

Responsibility Centre is a finance-governed identity independent of organizational unit, position, legal entity, ERP alias, budget line and journal posting. Its candidate owns immutable effective-dated versions, bitemporal aliases/associations/hierarchies/posting eligibility, accountable-position and ledger bindings, closure, and merge/split succession. Historical postings remain pinned to the version effective at their accounting date; corrections use reversal and repost.

The single Claude frozen audit returned **ACCEPT WITH LIMITS**. CandidateRevision 3 closes all eight structural findings without rerunning the audit. Source conservation is based on released amount; carry-in is bound to the prior period's reconciled residual; unknown fails closed; successor revisions cannot recreate availability; and cross-budget draws fail closed until governance allocates an authoritative source-draw register.

## Validation

- Responsibility Centre candidate: 17 invariants, 5 reference boundaries, 16 fixtures;
- Budget Responsibility profile: 11 constraints, WM-XCT-032 mixin, no new runtime ID;
- identifier and registry ID remain null; no registry mutation is proposed by this checkpoint.

## Holds

- Responsibility Centre requires formal registry allocation;
- profile and centre must promote or remain held together;
- WM-ECO-012 and neighbouring finance relations remain unapproved reviewable drafts;
- cross-budget source-draw authority is unallocated and therefore fails closed;
- ledger/chart-segment field bindings and jurisdiction-specific authority rules need validation;
- standards are alignment targets only;
- canonical publication and live HTTP/runtime/search/package verification remain held.

## Next safe step

Retain this reviewable research package without publishing blocked artifacts. Continue with EM-FIN-03 only after fresh action-time confirmation for its saved Grok prompt.
