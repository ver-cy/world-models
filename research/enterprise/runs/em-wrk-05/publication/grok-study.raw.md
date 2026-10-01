Verdict: Accept with conditions. Independent roots are required only for Resource Demand and Resource Pool. Capacity Plan is a profile of WM-ACT-008, not a root. AllocationScenario is a plan-owned immutable release, not a root. ResourceAllocation is a scenario-owned assertion, not a root. People, employment, work assignment, assets, money, calendars and actual consumption stay in their source masters. A share above 100% is not an error by itself.

Strongest evidence. The test is decidable only if conflict detection is a read of scenario assertions against pool capacity, exclusivity, divisibility, calendars and an explicit overbooking policy. Two projects compete for one specialist and one GPU pool. In one scenario the specialist’s shares sum to 110% and exclusive GPU intervals overlap; in the other the intervals do not overlap. Both outcomes are computed without writing the worker, employment, assignment or asset records. That is possible only if demand is competence-and-quantity, pool membership is not mastership, and allocation does not become assignment.

Strongest counterexample. If pool membership is derived from employment or asset mastership, or if an allocation identifies a named person or physical item as its subject, detecting the 110% share or the GPU overlap forces a write to WM-PER-001, WM-ORG-016 or WM-OBJ-001. The test then fails. A second failure mode is summing FTE, GPU-hours and currency into one load figure: the kinds are incommensurable, so the sum is not a conflict and not a capacity.

Identity and mastership. Resource Demand and Resource Pool need identifier-unassigned roots because neither is a person, an asset, a budget line, an assignment or a consumption event. Capacity Plan must not take a new root: its identity, version and baseline rules stay those of WM-ACT-008. AllocationScenario must not take a root: it is a release of that plan. ResourceAllocation must not take a root: it cannot outlive or contradict its scenario. Optional later binding to a named person or asset is a Work Assignment concern, not an allocation identity.

Resource kinds and units. Every demand, pool capacity and allocation carries a quantity kind, a unit, divisibility and exclusivity. FTE, GPU-hour and currency are not addable. Uncertainty stays attached to the assertion; it is not collapsed into a point value. A GPU pool and a specialist pool are different kinds even when both are scarce.

Demand and pool. Demand states competence, skill, role or resource kind, quantity, interval and constraints. It does not name a person or asset. Pool is a planning grouping. Membership is a planning role with an effective interval. It is not employment and not asset mastership. A person may sit in a pool without an assignment; an asset may sit in a pool without a transfer of title.

Capacity plan and scenarios. Capacity Plan profiles WM-ACT-008 with pool capacity over calendar intervals. AllocationScenario is an immutable release of that plan. An alternative is a different release, not an in-place edit of the approved baseline. Promoting a scenario is an explicit release, not a mutation of prior releases.

Allocation and reservation. ResourceAllocation asserts a reserved quantity of a kind, against a demand and a pool, inside one scenario. Reservation has an expiry. Confirmation is a distinct later state and is not implied by reservation. An expired reservation is not a confirmation and is not consumption.

Human, asset and compute boundaries. Specialist demand is competence demand. Named-person assignment remains WM-ORG-016. GPU and other assets remain WM-OBJ-001; the pool holds a planning membership, not the asset record. Compute capacity is a quantity kind on the pool, not a currency amount and not a headcount. Budget remains WM-ECO-012. Actual use remains WM-FLW-015.

Time and calendar. Capacity, demand and allocation intervals use WM-XCT-009 calendars and time zones. Capacity is not availability: availability is what remains after calendar, existing reservations and constraints. Overlap is evaluated in a stated zone. A non-overlap in one zone is not assumed in another.

Plan versus fact. Plan is not schedule, assignment or actual use. WM-ACT-008 holds plan and schedule structure. Assignment is organizational. Consumption is fact. A scenario may be feasible while the later assignment is refused and while actual consumption diverges.

Scenario. Scenario identity travels with every capacity and allocation assertion. The overlapping exclusive GPU case is a conflict in that scenario only. The non-overlapping case is not. Neither result rewrites the other scenario or the masters.

Above 100%. Not an error when the kind is divisible, the pool policy allows sharing or a stated overbook fraction, and the assertion is scenario-scoped: a 110% specialist share is then a soft load or a policy warning, not a master defect. It is an error when exclusivity is set and intervals overlap, or when reserved quantity of the same kind, unit and interval exceeds capacity times one plus the allowed overbook fraction. Overlapping exclusive GPU jobs are a conflict under exclusivity even if each job is under 100%. No cross-kind total is ever an error or a pass, because the total is undefined.

Invariants.
1. Demand does not name a person or asset.
2. Pool membership is not employment and not asset mastership.
3. Capacity is not availability.
4. Demand is not allocation.
5. Reservation is not confirmation; expiry is explicit.
6. An alternative scenario is not the approved baseline.
7. Plan is not schedule, assignment or actual consumption.
8. FTE, GPU-hours and currency are never summed.
9. Every assertion carries scenario identity, quantity kind, unit, calendar, time zone, exclusivity, divisibility, uncertainty and reservation expiry.
10. Overbooking exists only under an explicit policy.
11. Conflict detection does not write Person, employment, Work Assignment, Physical Item, Budget or Consumption.
12. A released scenario is immutable; change requires a new release.
13. Allocation does not create an assignment.

Minimum model set. Resource Demand root; Resource Pool root; Capacity Plan as a profile of WM-ACT-008; AllocationScenario as a plan-owned immutable release; ResourceAllocation as a scenario-owned assertion; references only to WM-ORG-016, WM-ECO-012, WM-PER-001, WM-OBJ-001, WM-XCT-009, WM-ACT-008 and WM-FLW-015.

Blockers. No overbooking-policy attribute is specified. Quantity-kind taxonomy is not fixed, so cross-kind rejection is unenforceable. Reservation expiry is not yet tied to the calendar. The later binding from a pool allocation to a Work Assignment is unspecified. Until those four are closed, the test can be described but not certified. This review does not assign identifiers and does not claim publication readiness.
