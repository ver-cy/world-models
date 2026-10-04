# Verdict

Reuse the frozen bases; add two roots and one profile; do not extend any master.

| Candidate | Decision | Independent identity? |
|---|---|---|
| ResourceDemand | New model candidate, identifier unassigned | **Yes** — a demand exists, persists and may stay unmet with no pool, plan, scenario or allocation |
| ResourcePool | New model candidate, identifier unassigned | **Yes** — reusable across plans, scenarios and periods; survives membership turnover |
| CapacityPlan | **Profile over WM-ACT-008 Plan/Schedule** | No new root — WM-ACT-008 already owns plan identity, revision, baseline, change log, provenance |
| AllocationScenario | Immutable addressable release owned by the CapacityPlan aggregate | Addressable identity, **not** a root; cannot exist without its plan |
| ResourceAllocation | Identified scenario-scoped assertion owned by the same aggregate | Addressable identity, **not** a root; every allocation is scenario-bound |

No identifier is allocated for any candidate.

# Evidence

WM-ORG-016 is a reified n-ary relationship binding assignee, organization, post, scope and period; it explicitly excludes shift instances, timesheets, demand forecasting and matching algorithms, and its `effort-allocation-and-capacity` finding is declared normatively ungrounded — workforce measurement (FTE, headcount, coverage) is a published **gap** and a publication hold. It therefore cannot master planned capacity. WM-ECO-012 separates proposal, ceiling, authorized, allocated, available, committed, actual and paid states for money only, and forbids collapsing bases. WM-ACT-008 supplies plan identity, baselines, working calendars, duration kinds (elapsed / working / effort), dependency networks, float and a scoped `resource-assignment-and-contention` finding. WM-FLW-015 supplies quantity-kind and unit discipline (UN/CEFACT Rec 20, QUDT, UCUM), assertion kinds, allocation-with-residual and the rule that stock, input, use and forecast never collapse. WM-XCT-009 supplies calendars, zones, offsets and release pinning. WM-PER-001 and WM-OBJ-001 are referenced masters only.

# Identity/mastership

Person → WM-PER-001. Employment/assignment → WM-ORG-016 (and its own parents). Physical/compute asset instance → WM-OBJ-001. Money → WM-ECO-012. Actual consumption → WM-FLW-015. Time reference data → WM-XCT-009. Plan → WM-ACT-008.

ResourcePool masters only pool identity, unit, calendar, effective-dated membership edges and declared capacity assertions. Membership references a person, an item instance or a class-plus-quantity; it never restates employment, title, condition or civil identity. Demand masters requirement, not assignee. Allocation masters the reified edge demand ↔ pool (or pool member) ↔ scenario ↔ interval ↔ quantity, and writes nowhere else.

# Resource kinds/units

Every demand, capacity and allocation carries quantity kind, unit, unit scheme and version. Human effort, machine time and money are **separate quantity kinds with no conversion path in this model**. Any conversion (GPU-hours → currency, FTE → cost) is an external, evidenced, version-pinned factor producing a different assertion, not an addend. The negative case is rejected structurally: summation is permitted only within one quantity kind, one unit, one pool, one interval, one scenario.

# Demand/pool

Demand: requesting work reference, competence or resource-class requirement, quantity, unit, interval or deadline, divisibility, substitutability, priority, uncertainty (range or confidence), and whether it is a named-person request or a competence request. Competence matching is a scored, source-qualified candidacy assertion against pool membership; it never becomes an assignment.

Pool: identity, kind, unit, calendar, shared-team flag, divisibility rule, overbooking policy, reservation policy, effective-dated members, and capacity assertions distinguishing **nominal**, **calendar-available**, **committed elsewhere** and **effective available**.

# Capacity plan/scenarios

CapacityPlan profiles WM-ACT-008: horizon, pinned pools, pinned demands, calendars, tz-database release, unit registry version, baselines and change log. AllocationScenario is an immutable hypothesis release pinning plan revision, pool versions, demand set, capacity assertions and assumptions. Scenarios are mutually exclusive and non-additive. Selection of a scenario as baseline requires a separate authorized decision; a scenario is neither an actual nor an approval.

# Allocation/reservation

Allocation states: proposed → reserved (hold, with expiry) → confirmed → released / consumed-elsewhere. Reservation consumes effective available capacity within its scenario and interval; expiry restores it. Confirmation of a human allocation may *trigger* a downstream WM-ORG-016 assignment or WM-ACT-008 schedule entry by reference — it never creates, amends or ends one. Allocation of money is a WM-ECO-012 allocation referenced here, never re-mastered.

**>100% is an error** when, within one scenario, one pool (or member), one interval and one unit, confirmed plus reserved quantity exceeds effective available capacity including the declared overbooking allowance. **>100% is not an error** across distinct scenarios, across incompatible unit or calendar pins, or against nominal capacity where policy declares an overbooking factor. Unknown capacity yields *unknown*, never *available*.

# Human/asset/compute boundaries

Named-person assignment (WM-ORG-016) ≠ competence demand ≠ pool membership ≠ scenario allocation. A specialist is indivisible as an entity but divisible in time-share; a single GPU is indivisible for exclusive jobs while the GPU pool is divisible in GPU-hours. Indivisible members carry an exclusivity flag: any second confirmed allocation over an overlapping interval is a conflict regardless of fraction. Shared teams are pools whose members belong to several pools; double membership does not multiply capacity — capacity is counted once per member per interval across all pools.

# Time/calendar

Every interval carries an instant with explicit offset, IANA zone identifier and tz-database release. Elapsed, working and effort durations are never interchanged. Pool calendars, member calendars and demand calendars are pinned separately; conflict detection runs on a single declared expansion calendar. DST gaps and overlaps require an explicit resolution policy. Recurrence is a rule plus overrides, never a persisted occurrence list.

# Plan versus fact

Planned capacity, reservation, confirmed allocation, scheduled work, assignment in force, and actual consumption (WM-FLW-015) are six distinct facts with distinct authorities and clocks. A plan never proves performance; consumption never retroactively rewrites a baseline. Variance is an explicit comparison assertion carrying both pins.

# Acceptance scenario

Projects A and B each raise a competence demand for one specialist (effort unit) and a demand in GPU-hours. In scenario S1 both specialist demands allocate to member SPEC-1 over the same week: 0.6 + 0.5 = 1.1 of effective available capacity → conflict finding, scenario-scoped, with both allocations retained. GPU-hour demands sum within the pool's effective hours → no conflict, but an exclusive single-GPU job overlaps → indivisibility conflict. In scenario S2 one demand shifts interval → no conflict. Nothing is written to WM-PER-001, WM-ORG-016 or WM-OBJ-001; SPEC-1's employment terms and the GPU asset records are unchanged.

# Invariants

1. Units and calendar are mandatory on every quantity. 2. No cross-kind summation. 3. Conflict is evaluated within one scenario, pool, interval and unit. 4. Plan never substitutes for fact. 5. Demand may exist unmet. 6. Allocation is scenario-scoped and immutable after release. 7. Reservations carry expiry; expiry restores capacity. 8. Overbooking is an explicit declared policy, never an inferred tolerance. 9. Indivisible members admit one confirmed overlapping allocation. 10. Member capacity is counted once across all pools. 11. Allocation writes to no external master. 12. Unknown capacity is unknown. 13. Every allocation pins pool version, calendar and tz release. 14. Money allocation resolves to WM-ECO-012. 15. Actuals resolve to WM-FLW-015.

# Minimal model set

WM-PER-001 (ref) · WM-OBJ-001 (ref) · WM-ORG-016 (ref) · WM-ECO-012 (ref) · WM-FLW-015 (ref) · WM-XCT-009 (mixin, required) · WM-ACT-008 + CapacityPlan profile · ResourcePool (new, unassigned) · ResourceDemand (new, unassigned) · AllocationScenario and ResourceAllocation (addressable, plan-owned).

# Holds

No identifiers allocated. **Contradiction:** WM-ACT-008 `f-resource-assignment-and-contention` already claims assignment, availability and over-allocation — it must be scoped to intra-plan entries, with cross-plan contention owned here, or one node withdrawn. **Contradiction:** WM-FLW-015 admits a `planned` assertion kind, overlapping CapacityPlan; the two must be partitioned (forecast consumption vs capacity commitment). **Gap:** WM-ORG-016 has no grounded FTE, headcount or coverage definition, so the effort unit is a Dimension declaration, not a canonical one. **Gap:** no reserved registry entry for pool, demand or scenario; relation rows unapproved. WM-ECO-012 and WM-FLW-015 are single-provider-waiver reviewable drafts with absence-of-external-review holds; WM-FLW-008 parentage is held. All bases remain non-canonical reviewable drafts with open source pins. No claim of canonical completeness, installability or publication readiness is made.
