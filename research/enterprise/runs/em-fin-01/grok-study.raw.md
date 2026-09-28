## DECISION

Justified combination: **reuse WM-ECO-012** for the budget aggregate; add a **thin enterprise profile** on that model; create a **new cross-domain Responsibility Centre entity**. Reject REUSE ONLY. Do not create a separate Funding Allocation aggregate. Do not assign a numeric model identifier.

WM-ECO-012 already owns the governed plan: identity and revision, scenarios, ceilings and envelopes, funding sources, allocation and allotment, amendments, forecasts, actuals as external references, and variance. The assignment still fails if those records treat a cost-centre code as an organizational-unit alias, or if a revision can mint the same source amount twice. EM-FIN-01 states the contour directly: an organizational unit need not coincide with a financial centre. No published Vercy model masters that centre. Classifying a unit as a cost centre inside WM-ORG-002 does not close the gap.

## BUDGET BOUNDARY

Reuse WM-ECO-012 for Budget, BudgetVersion and BudgetScenario. In-scope there, and not to be forked: purpose and owner; period and recognition basis; currency and unit; ceilings, envelopes, allocation, time-phased allotment and availability; funding sources with earmark, restriction, matching and release; amendments, transfers, carryover, lapse, freeze and cancellation; forecasts held separately from the approved revision; commitment and actual bindings that preserve external mastership; plan / forecast / commitment / actual / cash variance.

Out of the budget boundary: Responsibility Centre master lifecycle; ledger posting (WM-ECO-016); organizational-unit and position masters (WM-ORG-002, WM-ORG-004); consumption and cost-allocation algorithms (EM-FIN-05). Funding Allocation stays a structured record inside the budget version (ceiling → envelope → allocation → allotment → availability). Extracting it would split conservation across two roots and recreate double availability. Cross-budget use of one source is a referenced draw on that source, not a second aggregate. EM-FIN-05 remains the consumption / charging contour; it must reference budget availability and the centre, not remaster funding.

The enterprise profile must add what the world model leaves open: every budget line, allocation, allotment and forecast line carries a version-pinned Responsibility Centre reference; period and currency are mandatory; monetary amounts use the WM-XCT-032 mixin with a pinned code-list edition and an explicit measurement basis; a plan revision must not mutate actuals or commitments; original, revised, forecast, commitment and actual remain separately based states.

## RESPONSIBILITY CENTRE BOUNDARY

Create one new entity. Cost, revenue, profit, investment and funds centres are kinds of that entity, not sibling masters. An ERP cost-centre code is a versioned alias, never the identity.

The centre has identity and lifecycle independent of:

- Organizational unit. WM-ORG-002 models internal structure. It may list “cost centre” as a unit kind and a concurrent roll-up, but finance hierarchies remain referenced masters, not owned there. Folding the centre into the unit tree forces org tree = finance tree and fails the assignment’s negative case.
- Position. WM-ORG-004 asks whether the cost centre that bears a seat differs from the holding unit, and treats budget and funding as bindings onto the seat.
- Legal entity, ledger and journal. WM-ECO-016 treats cost centre as an analytical dimension with an external dimension owner. Posted entries are immutable; correction is reversal, not rewrite.
- Budget line. Classification of an amount is not mastership of the centre.

Consumers already point at codes they do not own: budget classification, journal dimensions, position placement, work-assignment scope. EM-LND-10 names responsibility centres as a landscape object alongside plans, actuals and consolidation perimeters.

Required shape: stable family identity; immutable, effective-dated versions (world time and record time); predecessor / successor edges for merge, split, reparent and code change; version-scoped bindings to manager or accountability seat, organizational unit, legal entity, ledger and chart segment, currency, measurement basis, and hierarchy parent. Historical journals and budget lines store the centre version effective when recorded. Reorganization may apportion current-period authority only. It must not cascade-rewrite past attribution.

## FUNDING CONSERVATION

WM-ECO-012 names sources, earmarks, release gates, envelopes and allocations. It does not yet state the assignment invariant that an allocation has a base and a remainder rule. The profile must.

Every allocation cites a source base on a named funding source in a named budget version, and a named remainder rule (lapse, carryover, return-to-source, residual-to-unallocated, or prohibited reallocation). In one revision, the sum of allocations from one source cannot exceed that source’s authorized amount in the same currency, pinned code-list edition and measurement basis. Residual is computed: authorized − allocated − reserved − lapsed + carry-in. Unknown is not zero.

A successor budget version does not increase source availability unless the source authorization itself is amended. Cross-budget use of one source is allowed only if the source register records the drawn amount once; receiving budgets reference that draw. Commitments and actuals consume availability; they do not create it. Quantization residuals follow WM-XCT-032 allocation-and-residual rules rather than silent absorption.

## ACCEPTANCE SCENARIO

T0. Project P is financed by grant Source A (earmarked) and own-funds Source B. Budget version V1 allocates 60 from A and 40 from B to Responsibility Centre X version 1 (manager M1, ledger L1, segment S1). Remainder: A lapses unused; B returns to the unallocated pool. Commitments and actuals reference centre X v1 and budget V1. Plan, forecast, commitment and actual are stored as distinct states.

T1. Reorganization moves the department. Centre X v1 remains frozen. Centre X v2 binds the new unit and manager M2 under the same family identity. Historical journal lines keep X v1. The negative case — moving a department rewrites past expenses onto the successor centre — is a failed implementation.

T2. Budget revision V2 supersedes V1. V2 may re-split 50 A + 50 B. Source A’s authorized amount is unchanged unless the grant is amended, so V2 cannot make the original 60 available again beside the new 50. Forecasts attach to V2 without mutating V1 or actuals. Variance compares V1, V2, forecast, commitment and actual on the centre versions pinned at record time. Two sources never become available twice; history reconciles.

## HOLDS AND PUBLICATION RECOMMENDATION

Do not treat this card as publication-ready. WM-ECO-012 is a reviewable draft with independent review waived and an empty approved relationship ledger. Conservation fixtures, jurisdiction recipes and chart-of-accounts crosswalks remain deferred. Neighbouring models used here are likewise reviewable drafts.

Before publication: specify the Responsibility Centre entity with fixtures for reorg, merge, split and code change; add conservation fixtures for multi-source and cross-budget draws; approve relation-ledger rows from the budget profile and the centre to WM-ORG-002, WM-ORG-004, WM-ECO-016 and WM-XCT-032; declare seams so EM-FIN-05, EM-ORG-04 / WM-ORG-002 and EM-FIN-02 do not remaster the centre or funding availability; keep period, currency and measurement-basis pins mandatory. Until the centre is registered, consumers should continue to carry an explicit external dimension-owner reference rather than treat a live ERP code as identity.

Research-protocol form of result: reuse plus profile plus new subject, not a mechanical majority vote. One broken scenario — rewrite of historical centre attribution — is enough to require the split.