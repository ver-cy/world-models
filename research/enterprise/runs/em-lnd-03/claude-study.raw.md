# EM-LND-03 Workforce Landscape — independent review

## Verdict

Both candidates are **profile/projection constructs**. Neither needs independent subject identity; no new model ID is warranted.

- **WorkforceLandscape** is a view over records mastered elsewhere. It has no aggregate root, no lifecycle of its own, and asserts no fact that survives deletion of its sources. It is a WM-XCT-003 projection (grain class `aggregate_only`, occasionally `named summary`) over a population resolved from WM-ORG-005, WM-ORG-016, WM-ORG-004/002 and WM-PER-001.
- **WorkforceScope** is the scope clause and counting parameterisation of that projection — precisely the v1 fields `population_rule`, `period`, `fte_rule`, `access_scope`.

One qualification: *addressable* is not *independent*. WorkforceScope must carry a stable, versioned identifier and the landscape a compiled fingerprint, or no figure is reproducible or comparable across releases. That is artifact identity in the WM-XCT-003 sense (pinned inputs + digest), not subject-model identity. Reuse/extend, not new.

## Evidence

WM-ORG-016 declares workforce measurement a **gap**: effort allocation, FTE semantics, headcount boundary conventions and coverage metrics are "structured but not normatively grounded," publishable only as required declarations by the adopting Dimension; its adversarial checks state plainly that treating FTE as internationally standardised is false. WM-ORG-002 carries the only operating machinery — `compute-headcount-rollup` with declared counting basis, period convention, minimum cell size and suppression markers — but its own adjudication reclassified unit-grain measurement to extension-grade. WM-ORG-004 supplies authorized FTE, headcount allowance, pooled/overlap semantics and derived (never persisted) vacancy. WM-ORG-005 supplies relationship identity, multi-party roles and purpose-qualified status. The landscape therefore has no unowned semantics left to master.

## Identity/mastership

Person → WM-PER-001 (one anchor per natural person; record plane separated from entity plane; link, never destructive merge). Employment relationship → WM-ORG-005; a worker–employer pair may hold several concurrent or successive relationships, so the pair is not identity. Assignment → WM-ORG-016. Position and establishment → WM-ORG-004. Unit, hierarchy, snapshot → WM-ORG-002. The landscape masters nothing and must resolve every figure back to source records at a pinned version.

## Population boundary

Scope is "разрешённый управленческий контекст" — bounded by a WM-XCT-002 grant (grantor, grantee, purpose, window, fail-closed) and shaped by WM-XCT-003. The population predicate must state, explicitly: which party role the reporting entity holds (employer / agency / host / client / paymaster / platform), which relationship and assignment states are in force, whether vacant positions are in scope, and whether unnamed or pooled occupancy is included. Absent any of these the perimeter is undefined and the figure unpublishable.

## Counting semantics

Seven distinct measures, seven denominators, never summed across kinds:

| Measure | Counts | Source |
|---|---|---|
| Unique persons | distinct WM-PER-001 anchors | person anchor set |
| Legal headcount | relationships where the reporting entity is the **employing** party, under a named status scheme and purpose | WM-ORG-005 |
| Active relationships | relationships in asserted active state, any party role | WM-ORG-005 |
| Assignments | WM-ORG-016 records in force | WM-ORG-016 |
| Positions | established seats, filled or vacant | WM-ORG-004 |
| FTE | **demand-side** authorized FTE on positions **or** **supply-side** allocated effort share on assignments — declare which | WM-ORG-004 / WM-ORG-016 |
| Capacity | available effort in period after leave, suspension, secondment and duty/rest limits | WM-ORG-016 + WM-ORG-005 interruption effects |

Double-counting rules: one relationship may carry several concurrent assignments, so assignments never add to relationships; an assignment may exist with no employment at all; succession and acting cover create a second assignment on one post without duplicating the post; vacant seats carry establishment FTE and zero persons; unnamed occupancy is one assignment and zero unique persons; suppressed is not zero.

## Contractors and dual affiliation

Contractors and volunteers appear as assignments resting on a commercial or non-employment arrangement — WM-ORG-016 marks the link to WM-ORG-005 *not required*. They enter assignment, FTE and capacity measures and are excluded from the host's legal headcount. Agency work uses WM-ORG-005 typed roles: the agency is employing party and carries the legal headcount; the host carries presence, assignment and capacity. Employee/contractor splits must name the classification scheme and purpose — statistical, tax, social-insurance and labour-law status may legitimately differ and must never be collapsed. Concurrent contracts with the *same* employer produce several relationships and one employed person, so "distinct employed persons for employer E" is a separate measure from E's relationship headcount.

## Time and scenarios

Every figure carries an as-of instant and a knowledge instant (RFC 3339, explicit offset), plus the point-in-time versus period-average convention and the inclusive/exclusive period-end rule, which no cited source fixes. Mid-period joiners, leavers, transfers and same-day successions are resolved by the declared convention, not by implementation default. Active status is asserted; it may never be inferred from an assignment, payroll event, badge swipe or stale contract.

## Scenario

One person, two employers A and B, allocations 0.6 and 0.5.

- Unique persons: **1** (single WM-PER-001 anchor; two relationship records, no merge).
- Legal headcount: A = 1, B = 1. Group relationship-headcount = 2, group distinct employed persons = 1 — both publishable only if labelled.
- Active relationships: 2. Assignments: 2 (or more). Positions: 2 seats.
- FTE: A 0.6, B 0.5. Person-FTE 1.1 across employers is legitimate and must not be clipped; over-allocation validation is per-engagement, not cross-employer.
- The negative case fails as required: the person is never counted as two people.

## Invariants

1. Perimeter and counting method explicit on every figure.
2. Relationships never substitute for Person; dedup by anchor.
3. Small groups pass a disclosure policy; unresolvable cohort floor ⇒ shape unfit.
4. No measure summed across kinds.
5. Active status asserted, never inferred.
6. Every status split names scheme and purpose.
7. Vacant positions carry establishment, no person.
8. Consolidation declares whether it dedups.
9. Landscape masters nothing.
10. Suppressed ≠ zero.

## Minimal profile shape

**WorkforceScope**: `scope_id` (versioned, never a date or label), `population_rule`, `party_role_filter`, `period` + boundary convention, `measure_set` with per-measure denominator, `counting_basis`, `fte_rule` (standard-hours reference), `dedup_rule`, `dual_affiliation_rule`, `consolidation_boundary`, `access_scope` → WM-XCT-002 grant ref, `projection_ref` → WM-XCT-003 with `grain_class=aggregate_only` and `cohort_floor_ref` → WM-XCT-005, source version pins.

**WorkforceLandscape**: `view_id`, `scope_ref`, as-of and knowledge instants, figures with suppression markers, provenance tuple (policy version, template fingerprint, binding id, schema version, compile time), completeness flag.

## Privacy and disclosure

Disclosive aggregates: any count at or near one; unit × role × attribute cross-tabs on small teams; deltas between successive releases that reveal a single joiner or leaver; min/max/range statistics that expose an individual value; unusual FTE fractions as quasi-identifiers; a dual-affiliation pattern unique in the population; and the residual channels WM-XCT-003 names — existence of a response, record counts, ordering, error versus empty. Controls: WM-XCT-002 makes reading purpose-bound, minimum-disclosure and fail-closed; WM-XCT-003 fixes the leaving shape, requires a resolvable WM-XCT-005 cohort-floor reference on aggregate-only grain, and declares release-set linkability. Person identity is preserved by resolving anchors *inside* the population step and selecting no direct identifier into the output — only cardinality leaves; pseudonym namespaces and join keys stay withheld.

## Holds

Both mappings are conceptual-candidate, boundary-reviewed only. WM-ORG-005 COMPOSE WM-ORG-016 is a candidate relation, not approved. Workforce measurement is an open gap in WM-ORG-016 and extension-grade in WM-ORG-002; no normative FTE or headcount definition is available. WM-ORG-005 was published under a single-provider waiver with independent review absent. WM-XCT-005 is referenced through WM-XCT-003 and not itself reviewed here. No fixtures, no crosswalk verification, no identifier allocation. Not canonically complete and not installable.
