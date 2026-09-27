# EM-WRK-05 local synthesis

## Disposition

- Propose identifier-unassigned **Resource Demand** and **Resource Pool** roots because each has an independent lifecycle and can exist without an allocation or plan.
- Profile **Capacity Plan** on WM-ACT-008 Plan / Schedule.
- Keep AllocationScenario as an immutable plan-owned release and ResourceAllocation as an identified scenario-owned assertion.
- Reuse WM-ORG-016 for human work assignments, WM-ECO-012 for money, WM-PER-001 for people, WM-OBJ-001 for physical items, WM-XCT-009 for calendars and WM-FLW-015 for actual resource consumption.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Resource Demand owns a requirement and may remain unmet without a pool, plan, scenario or allocation. Resource Pool owns a reusable grouping, its unit and calendar, effective-dated membership and capacity assertions; it survives membership turnover and reuse across plans.

Capacity Plan reuses WM-ACT-008 identity, revision, baseline and change history. AllocationScenario exists only under one plan revision. ResourceAllocation is the scenario-scoped edge from demand to pool or member over an interval and quantity.

People, assignments, asset instances, budgets, calendars and actual consumption stay in their source masters. Pool membership and allocation do not rewrite employment, assignment, asset, financial or operational facts.

## Resource kinds and units

Every demand, capacity and allocation declares quantity kind, unit, unit scheme and version. Human effort, machine time and currency are different quantity kinds and cannot be summed.

Any conversion such as GPU-hours to currency or FTE to cost is a separate evidence-bearing assertion with a pinned conversion factor and produces a new quantity. Summation requires the same quantity kind, compatible unit, pool, interval and scenario.

## Demand and pool

Demand declares requesting work, competence or resource class, quantity, interval or deadline, divisibility, substitutability, priority and uncertainty. A named-person request remains distinct from a competence requirement. Matching produces a scored candidacy assertion and never an assignment.

Pool declares kind, unit, calendar, membership rules, divisibility, reservation and overbooking policies. Its capacity distinguishes nominal, calendar-available, committed-elsewhere and effective-available values. Shared-team membership in several pools does not multiply the underlying person's capacity.

## Capacity plan and scenarios

Capacity Plan pins pools, demands, calendars, timezone database release, unit registry and planning horizon. Each AllocationScenario is an immutable hypothesis release with pinned plan revision, pool versions, demand set, capacity assertions and assumptions.

Scenarios are alternatives and are never added together. Selecting one as baseline requires an authorized decision. A scenario remains distinct from approval, schedule fact, work assignment and actual use.

## Allocation and reservation

ResourceAllocation records demand, pool or member, scenario, interval, quantity and status. A reservation has an expiry and temporarily reduces effective availability. Confirmation may trigger a referenced WM-ORG-016 assignment or schedule entry but cannot create or amend either master.

Within one scenario, pool or member, interval and unit, confirmed plus reserved demand cannot exceed effective availability plus an explicit overbooking allowance. Values above 100% across alternative scenarios are not a conflict. Unknown capacity remains unknown.

For indivisible members, overlapping confirmed allocations conflict regardless of fractional quantity. A person may be divisible by time-share while a particular GPU is exclusive for one job; the GPU pool can still be measured in GPU-hours.

## Time, calendar and plan versus fact

Every interval pins offset, IANA zone, timezone database release and applicable calendar. Elapsed, working and effort durations remain distinct. Conflict detection states which calendar expands recurrences and how DST gaps or overlaps are resolved.

Planned capacity, reservation, confirmed allocation, scheduled work, assignment in force and actual consumption are separate facts. A plan does not prove performance, and an actual never rewrites a baseline. Variance cites both immutable revisions.

## Acceptance result

Projects A and B each request one specialist and GPU-hours. In scenario S1, SPEC-1 is allocated 0.6 and 0.5 of effective weekly capacity, producing a scenario-scoped conflict while retaining both allocations. Aggregate GPU-hours remain within pool capacity, but two exclusive jobs overlap on GPU-1 and create an indivisibility conflict. In S2 one interval moves and both conflicts clear. No record in WM-PER-001, WM-ORG-016 or WM-OBJ-001 changes.

## Required invariants

1. Quantity kind, unit and calendar are mandatory.
2. Different quantity kinds are never summed.
3. Conflict is evaluated within one scenario, pool or member, interval and unit.
4. Demand may exist unmet.
5. Plan, reservation, allocation, schedule, assignment and actual remain distinct.
6. Allocation is scenario-scoped and immutable after release.
7. Reservations have expiry and release capacity when expired.
8. Overbooking is explicit policy, never inferred tolerance.
9. Indivisible members admit at most one overlapping confirmed allocation.
10. Member capacity is counted once across shared pools.
11. Allocation writes to no external master.
12. Unknown capacity is never treated as available.
13. Every allocation pins pool version, calendar and timezone release.
14. Money allocation remains WM-ECO-012-owned.
15. Actual consumption remains WM-FLW-015-owned.

## Holds

Resource Demand and Resource Pool have no registry allocations. WM-ACT-008's resource-assignment/contention scope overlaps cross-plan contention and must be narrowed. WM-FLW-015 planned consumption overlaps Capacity Plan and needs an explicit forecast-consumption versus capacity-commitment split. WM-ORG-016 lacks a grounded canonical FTE or headcount definition. Relation rows remain unapproved and reused bases retain non-canonical, source and provider holds. No installability or publication-readiness claim is made.
