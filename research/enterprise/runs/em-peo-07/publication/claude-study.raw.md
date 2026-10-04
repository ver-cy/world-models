# EM-PEO-07 Availability and Time Accounting — independent review

## Verdict

**Reject WM-ACT-008 as the home for this contour.** Reuse it by reference only, for planned schedule entries and commitments. The dossier's own boundary text disqualifies it as master: its `known_omissions` state that "RFC 7953 VAVAILABILITY working-availability components were not fetched and are not modelled beyond free-busy" and that "Capacity planning, shift rostering, labour-law working-time limits and collective agreement constraints are not modelled." Its `deferredResearch` still asks whether availability components "subsume, conflict with, or complement" its working-calendar finding. A model that has not decided that question cannot own availability.

Disposition of the six candidate types:

| Candidate | Decision |
|---|---|
| WorkCalendar | **Profile** over WM-XCT-009; no new rule master |
| Absence | **New** (independent identity and lifecycle) |
| Availability | **Derived projection**, not a master entity |
| Worklog | **New** (event, on the WM-MAT-008 observation pattern) |
| Timesheet | **New** (period aggregate) |
| TimeApproval | **Part of** the Timesheet aggregate, as an identified append-only decision |

Contractual work pattern and allocation are **reused**, not rebuilt.

## Evidence

- WM-ORG-016 boundary note, time capture: "Hours actually worked are observations evidencing performance under an assignment. They are never the assignment itself and must not be used to infer its effective period." This grounds both the Worklog separation and the negative case.
- WM-ORG-016 boundary note, schedule: the assignment states pattern, availability windows and duty limits; "concrete dated shift or duty instances live in a scheduling model."
- WM-ORG-016 coverage, workforce measurement: **gap** — FTE, effort fraction, headcount conventions "structured but normatively ungrounded."
- WM-ORG-005 carries `f-capacity-working-time-pattern-overtime-and-predictability` and `f-leave-suspension-secondment-and-nonperformance-effect`, which "references the external event" — so the absence event is not mastered there. Its boundary note holds that payroll and attendance "existence or absence alone never proves relationship identity, status or continuity."
- WM-XCT-009 owns calendars, week rules, holidays, `build-working-day-calendar`, `adjust-date-to-business-day`, `resolve-local-to-instant` with gap/overlap policy, and states that derived working-day calendars "are not master data." It excludes "Labour-law entitlements, pay premiums and leave accrual."
- WM-MAT-008 supplies the record pattern: phenomenon/result/valid/ingestion time separated; absence expressed by coded reason and "never encoded as zero"; quality flags recorded, never evaluated; corrections additive.
- WM-ACT-006 places effort as a declared gap, delegating "detailed time recording, rates and cost" to a sibling model.
- WM-PER-001 excludes special-category data from default projections and requires an additional lawful condition per disclosure.

## Identity/mastership

Person anchor: WM-PER-001. Engagement and contractual capacity: WM-ORG-005. Assignment and allocation share: WM-ORG-016. Calendar reference data: WM-XCT-009, pinned by release.

Absence has independent identity: it is requested, decided, cancelled, shortened and retro-corrected by parties other than the assignment's owner, and survives assignment change. Worklog has independent identity as an event: one record per performer, interval and charge target, mastered by the capturing system. Timesheet has independent identity as a period-scoped submission with its own submit/approve/reopen lifecycle. Availability has **no** independent identity — it is a computation over pattern, calendar, absence and allocation, identified as a run with an input release manifest, exactly as WM-XCT-009 treats a working-day calendar.

## Calendar and work pattern

Three separable layers, none collapsible:

1. **Calendar rules** — weekend rule, holidays with their instruments, tz release — WM-XCT-009.
2. **WorkCalendar** — a derived, versioned projection binding a rule set to an organisational scope for a period; cites every input release; not master data.
3. **Contractual work pattern** — contracted capacity, standard pattern, predictability and reference hours on WM-ORG-005, realised per assignment in WM-ORG-016.

A holiday's day-off status is calendar data; its pay or accrual consequence is outside both this contour and WM-XCT-009.

## Absence and privacy

Absence records kind, requested and effective intervals, decision authority, decision time and relationship-level effect (does service, pay, notice or assignment continue). Its **reason category** is carried at two levels: an operational category sufficient for capacity (unavailable, partially available, available-with-restriction) and a protected clinical or diagnostic layer that is not part of the availability calendar at all. Medical grounds appear in ordinary availability only as an unavailability interval with an operational category; the reason resides in the health/absence-reason domain under an explicit additional lawful condition, excluded from every default projection, per WM-PER-001. Operational consumers need duration, effect and confirmation status — not diagnosis.

## Availability/capacity/allocation

Four distinct quantities:

- **Contracted capacity** — from the engagement (e.g. 0.5 of a declared FTE basis).
- **Planned availability** — calendar working time minus approved absence, within duty/rest limits; a projection with a pinned manifest.
- **Assigned allocation** — WM-ORG-016 allocation share per assignment; validated in aggregate across concurrent assignments.
- **Actual worked time** — Worklog only.

Allocation is a fraction of contracted capacity, never of raw calendar hours. Overcommitment is a finding against the allocation set, not a reduction of either side.

## Worklog

A Worklog is an observation: performer, interval or quantity, unit with code system, charge target, capture method, phenomenon time, result time and ingestion time. It records what was reported, not what was true. It is **not** evidence of presence (a physical-presence assertion has a different observing procedure), **not** a productivity measure (no output is bound), and **not** a quality signal (quality flags are recorded by other models, never derived here). Absent worklogs mean **unknown**, never zero: a coded absence reason is required, and zero is reserved for an asserted zero.

## Timesheet and approval

A Timesheet is a period-scoped submission over a performer and a set of worklogs, with states draft, submitted, approved, rejected, reopened, superseded. TimeApproval is an identified, append-only decision naming scope (entry, day, period), approver authority, decision time, and — where separation of duties applies — an approver distinct from the performer. Approval freezes the member set with a digest. Approval attests that the report was reviewed; it does not convert a worklog into presence or performance evidence.

## Time-zone/DST/overlap

Every interval carries an instant with explicit offset, plus tzid and tzdb release. Durations declare **exact** versus **nominal**: a "working day" is nominal and comes from the contracted pattern; elapsed clock time is exact. Capacity is never derived by subtracting instants across a transition. Spring-forward days contain 23 clock hours but an unchanged nominal day. Fall-back ambiguity requires an offset; otherwise the entry is flagged as an anomaly rather than silently resolved. Wall-clock-overlapping worklogs across two charge targets are **permitted and disclosed**; they are a validation finding against capacity, never auto-merged and never summed twice.

## Correction and audit

Corrections are additive. An approved period is immutable: a correction issues a superseding period revision or a signed adjustment entry in a later period, linked bidirectionally to the original, with reason, classification and authorising agent. Prior values, prior flags and prior approvals remain retrievable. No in-place edit, no obliteration, no re-derivation of an earlier availability projection without a new run record.

## Acceptance scenario

A half-time performer, 0.5 of a declared FTE basis, holds two assignments at 0.25 each. In the spring-forward week the working-day calendar yields five nominal days; the transition day resolves to 23 exact hours but the nominal day is unchanged, so planned availability does not shrink and does not inflate. Two same-day worklogs on different projects overlap by one clock hour: both are retained, the overlap is flagged, and the capacity check counts elapsed time once. A later correction reduces one entry by two hours after approval; the original approved period retains its total, and a linked adjustment carries the delta forward. Capacity stays at 0.5, allocation at 0.25 + 0.25, and neither doubles nor goes negative.

## Invariants

1. Every interval carries an explicit offset, tzid and tzdb release.
2. A missing record is unknown; zero requires an asserted zero.
3. Medical reasons never enter the ordinary availability calendar.
4. Planned availability, assigned allocation and actual time are never the same value.
5. Allocation is a fraction of contracted capacity, not of calendar hours.
6. Worklog proves neither presence, productivity nor quality.
7. Overlapping worklogs are disclosed, never merged, never double-counted.
8. Nominal and exact durations are declared and never interchanged.
9. Approved periods are immutable; corrections are additive and linked.
10. Availability is derived and carries its input release manifest.
11. Quantities name their unit and code system; rounding occurs only at projection.
12. Timesheet existence never proves entitlement, payment or compliance.

## Minimal model set

Reuse: WM-PER-001, WM-XCT-009 (mixin and reference), WM-ORG-016, WM-ACT-008 (reference), WM-ACT-006 (reference). Profile: WM-ORG-005 for contractual pattern and absence effect; WM-XCT-009 for WorkCalendar. New: **Absence**, **Worklog**, **Timesheet** (containing TimeApproval). Derived, non-master: WorkCalendar projection, Availability projection. No identifiers allocated.

## Holds

WM-ACT-008 is `publishableCanonical: false` with unresolved publication holds, and its mapping here is `conceptual-candidate` at `index-and-publication-metadata` depth. WM-ORG-005 and WM-MAT-008 rest on single-provider waivers. WM-ORG-016's FTE and effort-fraction definitions are an acknowledged gap, so partial-FTE arithmetic depends on a Dimension-declared basis. WM-XCT-009 records precision/uncertainty as a gap and no global holiday register. Registry relations to WM-ORG-016 remain candidate. No working-time-law, collective-agreement, HR Open, ESCO/SFIA or SPACE source appears in this dossier, so labour-law limits and measurement-validity claims are unverified. No canonical completeness and no installability is claimed.
