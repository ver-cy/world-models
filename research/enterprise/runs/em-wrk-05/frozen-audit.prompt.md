# Single frozen semantic audit — EM-WRK-05

You are the sole independent frozen auditor. No tools, browsing, standards claims, identifier invention or registry mutation. This audit runs exactly once and will not be repeated.

Audit the reconciled proposal and artifacts below. Fixed identity decision: Resource Demand and Resource Pool each have independent identity but remain registry-unassigned; Capacity Plan profiles WM-ACT-008; AllocationScenario is a plan-owned immutable release; ResourceAllocation is a scenario-owned assertion. People, employment, work assignment, physical items, money, calendars and actual consumption remain in their source masters.

Find material internal contradictions, missing fields, unenforceable invariants, lifecycle/version/provenance/time defects, unit and quantity-kind errors, unsafe overbooking or exclusivity semantics, capacity double counting, reservation/confirmation ambiguity, and boundary leaks. Known registry/base publication gaps are holds, not artifact defects. Return:
1. Verdict ACCEPT or REVISE.
2. Numbered material defects with exact evidence.
3. Required bounded fixes.
4. One JSON fenced array of additional fixtures with target, id, kind, input, expect and optional expectedCode, covering every defect. Targets must be ResourceDemand, ResourcePool, or EM-WRK-05-profile.
5. Explicit identifier decision.
6. Freeze decision: closed, no rerun.


## local-evidence.md
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


## grok-study.raw.md
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


## candidate-allocation-offline-resource-demand/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-WRK-05","proposedName":"Resource Demand","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A requirement for a resource quantity or capability remains identifiable while unmet, matched, planned, allocated or withdrawn independently of any pool, assignment or consumption record.","versionIdentity":"Changes to requesting work, resource class, quantity, interval, priority, divisibility, substitutability or uncertainty create immutable demand versions.","independentLifecycle":["draft","submitted","approved","open","partially-matched","matched","withdrawn","expired","closed"],"mastership":"work or portfolio demand authority"},"boundary":{"owns":["persistent resource-demand identity","requesting work reference","resource or competence class","quantity kind, unit and amount","interval or deadline","divisibility and substitutability","priority and uncertainty","match, withdrawal and closure history"],"references":[{"target":"WM-ACT-008","purpose":"Capacity Plan"},{"target":"WM-ORG-016","purpose":"Resulting human assignment"},{"target":"WM-PER-001","purpose":"Person identity"},{"target":"WM-OBJ-001","purpose":"Physical resource identity"},{"target":"WM-XCT-009","purpose":"Calendar and timezone rules"},{"target":"WM-FLW-015","purpose":"Actual resource consumption"}],"excludes":["resource pool or membership identity","person, asset, assignment or budget identity","allocation, reservation or scenario identity","schedule, availability or actual consumption","matching score as assignment","currency or cross-kind conversion"]},"objects":{"ResourceDemand":{"identity":["resourceDemandId"],"required":["requestingWorkRef","resourceClass","quantityKind","unit","quantity","status"],"optional":["interval","deadline","divisibility","substitutability","priority","uncertainty","successorRef"],"lifecycle":["draft","submitted","approved","open","partially-matched","matched","withdrawn","expired","closed"]}},"invariants":["Demand may exist unmet without a pool, plan, scenario or allocation.","Every demand declares quantity kind, unit, unit-scheme version and interval or deadline.","Human effort, machine time and currency are never summed.","A named-person request remains distinct from a competence requirement.","Matching creates a scored candidacy assertion and never an assignment.","Demand approval never proves availability or capacity.","Allocation, schedule, assignment and actual consumption remain separate facts.","Cross-kind conversion is an evidence-bearing assertion producing a new quantity.","Changing quantity, interval or resource class creates a successor version.","Withdrawal preserves previous approvals, matches and planning references.","Unknown supply never counts as available capacity.","Demand closure never rewrites external work, assignment or consumption masters."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","FTE, headcount and competence-unit definitions require canonical grounding.","WM-ACT-008 and WM-FLW-015 overlap requires resolution."]}


## candidate-allocation-offline-resource-demand/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Resource Demand","cases":[{"id":"unmet-specialist","kind":"positive","input":"A project requests one specialist but no pool can satisfy it.","expect":"The approved demand remains open and unmet without creating an assignment."},{"id":"gpu-hours","kind":"positive","input":"A project requests 100 GPU-hours for a fixed interval.","expect":"Quantity kind, unit, interval and uncertainty are explicit."},{"id":"revised-quantity","kind":"positive","input":"Demand increases from 100 to 140 GPU-hours.","expect":"A successor version preserves the prior requirement."},{"id":"match-is-assignment","kind":"negative","input":"The best matching person is automatically assigned.","expect":"The transition is rejected."},{"id":"sum-fte-currency","kind":"negative","input":"FTE and currency values are summed as capacity.","expect":"The calculation is rejected."},{"id":"demand-proves-availability","kind":"negative","input":"Approved demand is treated as available supply.","expect":"The inference is rejected."}]}


## candidate-allocation-offline-resource-demand/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## candidate-allocation-offline-resource-pool/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-WRK-05","proposedName":"Resource Pool","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A reusable governed grouping of resource supply remains identifiable across membership turnover and planning scenarios while its capacity assertions evolve.","versionIdentity":"Changes to kind, unit, calendar, membership rules, divisibility, reservation or overbooking policy create immutable pool versions; member changes are effective-dated.","independentLifecycle":["draft","approved","active","constrained","suspended","superseded","retired"],"mastership":"resource-supply or capacity authority"},"boundary":{"owns":["persistent resource-pool identity","resource kind and unit","calendar and timezone bindings","membership rules and effective membership","nominal and effective-capacity assertions","divisibility and exclusivity rules","reservation and overbooking policy","version, suspension and retirement history"],"references":[{"target":"WM-ORG-016","purpose":"Human standing assignment"},{"target":"WM-PER-001","purpose":"Person identity"},{"target":"WM-OBJ-001","purpose":"Physical resource identity"},{"target":"WM-XCT-009","purpose":"Calendar and timezone"},{"target":"WM-ACT-008","purpose":"Capacity Plan"},{"target":"WM-FLW-015","purpose":"Actual consumption"}],"excludes":["person, asset, assignment or calendar identity","resource demand or allocation identity","scenario, schedule or actual consumption","employment or asset mastership","budget or currency allocation","automatic duplication of member capacity"]},"objects":{"ResourcePool":{"identity":["resourcePoolId"],"required":["name","resourceKind","unit","calendarRef","ownerRef","status"],"optional":["membershipRules","divisibility","reservationPolicy","overbookingPolicy","successorRef"],"lifecycle":["draft","approved","active","constrained","suspended","superseded","retired"]},"PoolVersion":{"identity":["resourcePoolId","version"],"required":["capacityAssertions","validFrom","contentDigest"],"optional":["memberships","validTo","supersedesVersion"]}},"invariants":["Pool identity survives membership turnover and reuse across plans.","Pool membership never rewrites person, assignment, employment or asset masters.","Every capacity assertion declares quantity kind, unit, interval, calendar and evidence.","Nominal, calendar-available, committed-elsewhere and effective-available values remain distinct.","Member capacity is counted once across shared pools.","Divisibility and exclusivity are explicit per member or resource kind.","Reservations have expiry and release capacity when expired.","Overbooking is explicit policy and never inferred tolerance.","Unknown capacity is never treated as available.","Alternative scenarios are never summed.","Indivisible members admit at most one overlapping confirmed allocation per scenario.","Retired pool versions remain resolvable for historical plans and allocations."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Cross-pool capacity deduplication and unit registry require canonical governance.","Package conversion and live verification are pending."]}


## candidate-allocation-offline-resource-pool/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Resource Pool","cases":[{"id":"shared-specialist","kind":"positive","input":"One specialist belongs to two pools for different planning views.","expect":"Underlying capacity is counted once in consolidated conflict checks."},{"id":"exclusive-gpu","kind":"positive","input":"One GPU is exclusive per job while the pool is measured in GPU-hours.","expect":"Aggregate capacity and overlapping member exclusivity are evaluated separately."},{"id":"expired-reservation","kind":"positive","input":"A reservation expires without confirmation.","expect":"Its quantity returns to effective availability."},{"id":"double-count-member","kind":"negative","input":"Membership in two pools doubles one person's capacity.","expect":"The calculation is rejected."},{"id":"unknown-is-free","kind":"negative","input":"Missing capacity evidence is treated as available supply.","expect":"The inference is rejected."},{"id":"implicit-overbooking","kind":"negative","input":"Confirmed allocations exceed capacity without an explicit policy.","expect":"The scenario is flagged as conflict."}]}


## candidate-allocation-offline-resource-pool/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}
