# EM-PEO-07 local synthesis

## Disposition

- Reject WM-ACT-008 as the aggregate master; reuse it only for referenced plans and dated commitments.
- Profile **Work Calendar** over WM-XCT-009 calendar rules and pinned organizational inputs. It is a derived projection, not master data.
- Raise **Absence**, **Worklog** and **Timesheet** as identifier-unassigned new-model candidates.
- Keep **Time Approval** as an identified append-only decision inside the Timesheet aggregate.
- Treat **Availability** as a derived projection with a pinned input manifest, not an independently mastered object.

## Mastership and quantities

WM-PER-001 anchors the person, WM-ORG-005 the engagement and contractual work pattern, WM-ORG-016 the assignment/allocation share, WM-XCT-009 calendar/time reference data, and WM-ACT-008 scheduled intent. Planned availability, assigned allocation and actual work are different quantities.

Contracted capacity is defined against a declared FTE basis. Planned availability derives calendar working time minus approved absence and applicable constraints. Allocation is a share of contracted capacity across assignments. Actual time comes only from Worklog. Overcommitment is a finding over allocations, not an automatic rewrite.

## Absence and privacy

Absence has independent request, decision, cancellation and correction lifecycle. It carries effective interval and operational effect. Ordinary availability sees only the minimum operational category such as unavailable or partially available. Clinical or diagnostic reasons remain in a protected domain under an additional lawful condition and never enter the normal calendar projection.

## Worklog, timesheet and approval

Worklog is a reported observation of performer, interval/quantity, unit, charge target, method and phenomenon/result/ingestion times. It does not prove presence, productivity or quality. Missing worklog means unknown; asserted zero requires an explicit record.

Timesheet aggregates a period-scoped immutable member set and submission lifecycle. Approval names scope, authority, time and decision, and freezes the member digest. It attests review of the report, not truth of presence or performance. Approved periods are immutable; corrections create linked superseding revisions or later adjustment entries.

## Time-zone and overlap rules

Every interval includes an instant with explicit offset, timezone identifier and timezone database release. Exact elapsed duration and nominal working duration are never interchanged. DST gaps/overlaps require explicit resolution policy. Overlapping worklogs remain recorded and flagged; capacity computation counts elapsed time once and never silently merges records.

## Acceptance result

A half-time worker has two 0.25 allocations. During a spring-forward week, the contractual nominal day stays stable while exact elapsed time reflects the transition. Two overlapping project worklogs remain distinct and trigger an overlap finding without double-counting capacity. A post-approval correction produces a linked adjustment while the original approved timesheet and approval remain immutable. Capacity never becomes negative or doubles.

## Required invariants

1. Every time interval has offset, timezone and ruleset release.
2. Missing is unknown; zero is asserted.
3. Medical reasons never enter ordinary availability.
4. Contracted, available, allocated and actual time stay separate.
5. Worklog proves neither presence, productivity nor quality.
6. Nominal and exact durations remain distinct.
7. Overlaps are retained, disclosed and not double-counted.
8. Approved timesheets are immutable.
9. Corrections are additive and linked.
10. Availability carries its complete input manifest.

## Holds

WM-ACT-008 and adjacent bases remain non-canonical drafts. FTE/effort basis, precision, working-time law and collective-agreement semantics are unresolved. Absence, Worklog and Timesheet need registry allocation, independent source research, relation contracts and fixtures. No new identifier or installable release is created.
