# EM-PEO-07 frozen semantic audit prompt

You are the sole final Claude Opus high no-tools auditor. This is exactly one frozen audit after independent Claude study, local synthesis and exact Grok response. Do not browse, use tools, invent identifiers, claim standards conformance, or request another study.

Audit the decision and artifacts below. Preserve the settled boundary unless the artifacts materially contradict the admitted evidence:
- Absence, Worklog and Timesheet are identifier-unassigned independent candidates.
- Work Calendar profiles WM-XCT-009 and Availability is a derived projection.
- Time Approval is an identified append-only decision inside Timesheet.
- WM-ACT-008 is reference-only.
- No runtime/model identifier is allocated.

Return:
1. Verdict on decision and artifacts.
2. Numbered material defects, each with exact deterministic remediation.
3. A single exact JSON array of additional fixtures, each with id, target, kind, input, expect, violates, closesDefect, and expectedCode on every negative.
4. Exact final counts for prior, additional and total fixtures, positive and negative.
5. Freeze decision. Do not ask for or perform a rerun.

## Initial Claude study

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


## Local synthesis

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


## Exact Grok response

Verdict: Conditionally acceptable. The proposed separations hold if Absence, Worklog and Timesheet receive independent identity, Time Approval stays an append-only decision inside Timesheet, and Work Calendar and Availability remain derived projections. Capacity must be closed on contractual pattern, calendar, absence and allocation only. Worklog must not enter residual capacity and must not be treated as proof of presence or quality. Blockers below prevent unconditional acceptance.

Strongest evidence: The proposal already separates contractual pattern, calendar, absence, planned availability, assignment allocation and actual work, and it states the rules that keep those separations intact: missing is unknown not zero; medical reason is excluded from ordinary availability; every interval carries offset, timezone and ruleset release; nominal and exact durations stay distinct; overlaps are retained and flagged; approved periods are immutable and corrections are additive. WM-ACT-008 is correctly held reference-only. Work Calendar profiling WM-XCT-009 as a projection, and Availability as a projection, match those boundaries.

Strongest counterexample: Half-time engagement (0.5 contractual pattern) with two project allocations that together equal that pattern, on a DST fall-back day with a repeated local hour. Two worklogs both claim the repeated hour and overlap. An already-approved timesheet is then “corrected” by rewriting the approved interval, and residual capacity is recomputed by subtracting worklog exact duration from nominal availability. The result is either double capacity (both worklogs summed into the repeated hour) or a negative residual. That fails missing=unknown, nominal≠exact, overlap retention, approved immutability, additive correction, and the ban on worklog as presence or quality evidence.

Identity/mastership: Independent identity is required for Absence, Worklog and Timesheet. They are identifier-unassigned new-model candidates with their own lifecycles (fact, reported observation, period container) and cannot be projections of person, employment, assignment, task, WM-XCT-009 or WM-ACT-008. Time Approval does not require a peer model identity; it is an append-only decision identified inside Timesheet (timesheet identity plus sequence). Work Calendar does not; it profiles WM-XCT-009. Availability does not; it is computed. No identifiers are assigned here.

Calendar/pattern: Contractual pattern is the employment-scoped nominal commitment (for example half-time). Work Calendar is a derived profile of WM-XCT-009: offset, timezone, ruleset release, and the distinction between nominal and exact duration. It does not own pattern, absence or allocation. WM-ACT-008 remains a plan/schedule reference, not the master of these facts.

Absence/privacy: Absence is an independent person/employment-scoped fact. Medical reason is structurally excluded from ordinary availability, not merely hidden by policy. An ordinary availability view may see that capacity is reduced; it must not see the medical reason. Missing absence is unknown, not zero.

Availability/allocation: Availability is the derived projection of pattern ∩ calendar − ordinary absence, bounded by assignment allocation. Two project allocations may partition that residual; they must not exceed it. Worklog does not consume residual. Allocation is planned commitment, not actual work.

Worklog: Worklog is an independent reported observation of actual work against an assignment or task. It is not proof of presence, productivity or quality. Overlaps are retained and flagged, not collapsed. A missing worklog is unknown, not zero hours. Exact duration is stored separately from nominal duration.

Timesheet/approval: Timesheet is an independent period container that references worklogs and the planned allocations in scope. Time Approval is an append-only decision inside that container. An approved slice is immutable. A later decision does not rewrite it.

DST/overlap: Every interval binds offset, timezone and ruleset release, so a skipped hour (spring-forward) and a repeated hour (fall-back) are unambiguous. Nominal duration is not rewritten to equal exact duration. Overlapping worklogs on the repeated hour stay flagged observations; they are not additive capacity.

Corrections: Approved periods are immutable. A correction is a new additive decision that references the prior approval. It does not delete, overwrite or negate history in place. Residual capacity is recomputed from pattern, calendar, absence and allocation, not by rewriting the approved snapshot.

Scenario: Person under a half-time contractual pattern, Europe/Athens, ruleset release fixed. Spring-forward day has 23 exact hours and a shorter nominal window. Two assignments each take half of the 0.5 pattern, so residual after allocation is zero. No ordinary absence. Two worklogs overlap on the transition and are retained and flagged; they do not change availability or residual. Timesheet aggregates the reported observations for the period. Approval freezes that slice. A later correction is appended and linked; the approved slice is unchanged; residual stays non-negative and is not double-counted. The same rules hold on a fall-back repeated hour.

Invariants:

1. Missing is unknown, never zero.
2. Worklog is observation only, not proof of presence, productivity or quality.
3. Medical reason is excluded from ordinary availability.
4. Every interval carries offset, timezone and ruleset release.
5. Nominal duration and exact duration remain distinct.
6. Overlaps are retained and flagged, never silently collapsed.
7. Approved periods are immutable.
8. Corrections are additive and reference the prior approval.
9. Availability is derived, not a master.
10. Work Calendar profiles WM-XCT-009 and has no independent mastership.
11. Allocation cannot exceed pattern residual after ordinary absence.
12. Worklog sum does not consume contractual capacity.
13. Time Approval identity is scoped inside Timesheet.
14. Residual capacity is never negative and never double-counted.
15. WM-ACT-008 is reference-only.

Minimum model set: Contractual pattern (employment boundary); Work Calendar as derived profile of WM-XCT-009; Absence (independent identity); assignment allocation (assignment boundary); Availability (derived); Worklog (independent identity); Timesheet (independent identity); Time Approval as append-only decision inside Timesheet. WM-ACT-008 reference-only. Person, employment, assignment, task and observation remain boundary types, not substitutes for the three new identities.

Blockers: Identifiers for Absence, Worklog and Timesheet are still unassigned, so master references cannot be closed. The non-negative residual rule is not yet specified as pattern ∩ calendar − ordinary absence − allocation, with overlap flags non-summable and worklog excluded. Medical exclusion must be structural. Approved immutability needs an explicit supersession link that does not rewrite history. Until those four are closed, the DST, half-time, dual-allocation, overlap and correction cases are not safe.


## Absence allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-PEO-07","proposedName":"Absence","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed absence case remains identifiable across request, decision, cancellation and correction while its operational effect is projected separately.","versionIdentity":"Changes to interval, operational category, quantity, approval or cancellation create append-only versions; a distinct absence episode creates a new case.","independentLifecycle":["draft","requested","approved","rejected","effective","cancelled","corrected","closed"],"mastership":"workforce absence-management authority"},"boundary":{"owns":["persistent absence identity","engagement and person references","effective interval and quantity","operational absence category","request and decision history","cancellation and correction lineage","minimum-disclosure classification","availability-projection effect"],"references":[{"target":"WM-PER-001","purpose":"Person anchor"},{"target":"WM-ORG-005","purpose":"Employment or engagement"},{"target":"WM-ORG-016","purpose":"Work assignment"},{"target":"WM-XCT-009","purpose":"Time and calendar rules"},{"target":"WM-ACT-008","purpose":"Scheduled intent reference"}],"excludes":["person, employment, assignment or calendar identity","clinical diagnosis or medical record","worklog, timesheet or approval identity","availability projection or capacity fact","payroll, entitlement or legal determination","automatic disclosure of protected reason"]},"objects":{"Absence":{"identity":["absenceId"],"required":["personRef","engagementRef","interval","operationalCategory","status"],"optional":["quantity","requestRef","decisionRef","protectedReasonRef","successorRef"],"lifecycle":["draft","requested","approved","rejected","effective","cancelled","corrected","closed"]}},"invariants":["Every absence names person, engagement, interval and operational category.","Absence lifecycle remains separate from employment, assignment and calendar masters.","Ordinary availability receives only minimum operational effect.","Clinical and diagnostic reasons never enter ordinary availability.","Approval, rejection, cancellation and correction remain attributable acts.","Corrections append successors and never rewrite approved history.","Missing absence data never means present or available.","Approved absence reduces planned availability only under the applicable calendar and policy.","Absence never proves payroll entitlement or medical status.","Every interval pins offset, timezone and ruleset release.","Cancellation preserves prior decision and effective history.","Disposition never deletes person or employment records."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Labor, privacy and medical-data policy crosswalks require jurisdictional review.","FTE and nominal-duration semantics require canonical grounding."]}


## Absence profile candidate

{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-PEO-07","name":"Enterprise Work Calendar and Availability","decision":"PROFILE","newRuntimeId":false,"bases":["WM-XCT-009","WM-ACT-008","WM-PER-001","WM-ORG-005","WM-ORG-016"],"constraints":["Work Calendar profiles WM-XCT-009 with pinned employment, assignment and organizational inputs.","Availability is a derived projection with a complete input manifest and never a mastered person fact.","Contracted, planned available, allocated and actual time remain separate quantities.","Nominal working duration and exact elapsed duration never substitute for each other.","DST gaps and overlaps use explicit timezone and ruleset policy.","Overcommitment is a finding over allocations and never rewrites source assignments." ]}


## Absence fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Absence","cases":[{"id":"approved-leave","kind":"positive","input":"A half-time worker has approved leave for one nominal working day.","expect":"Availability applies the operational effect under the pinned calendar without exposing protected reason."},{"id":"cancelled-leave","kind":"positive","input":"Approved future absence is cancelled before effectivity.","expect":"Cancellation is appended and the original decision remains."},{"id":"spring-forward","kind":"positive","input":"Absence spans a DST spring-forward transition.","expect":"Nominal and elapsed durations remain separately computed."},{"id":"medical-reason-in-calendar","kind":"negative","input":"A diagnosis is copied into ordinary availability.","expect":"The disclosure is rejected."},{"id":"missing-means-present","kind":"negative","input":"No absence record is treated as proof of presence.","expect":"The inference is rejected."},{"id":"rewrite-approved","kind":"negative","input":"An approved interval is edited in place.","expect":"The mutation is rejected."}]}


## Absence validation policy

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## Worklog allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-PEO-07","proposedName":"Worklog","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A reported observation of performed work remains identifiable independently of person, assignment, task, timesheet and approval records.","versionIdentity":"Corrections create linked adjustment or superseding records; a distinct reported interval or quantity creates a new worklog.","independentLifecycle":["draft","reported","submitted","corrected","voided","included","closed"],"mastership":"performer or authorized work-reporting authority"},"boundary":{"owns":["persistent worklog identity","performer and engagement references","interval or quantity and unit","charge target and work reference","reporting method","phenomenon, result and ingestion times","source and correction lineage","timesheet inclusion reference"],"references":[{"target":"WM-PER-001","purpose":"Performer identity"},{"target":"WM-ORG-005","purpose":"Engagement"},{"target":"WM-ORG-016","purpose":"Assignment"},{"target":"WM-ACT-006","purpose":"Task or work target"},{"target":"WM-XCT-009","purpose":"Time rules"},{"target":"WM-MAT-008","purpose":"Observation pattern"}],"excludes":["person, assignment, task or engagement identity","presence, productivity or quality determination","absence, availability or capacity","timesheet or approval identity","payroll result or invoice","automatic overlap reconciliation"]},"objects":{"Worklog":{"identity":["worklogId"],"required":["performerRef","engagementRef","quantity","unit","method","reportedAt","status"],"optional":["interval","chargeTargetRef","workRef","resultTime","ingestionTime","supersedesRef"],"lifecycle":["draft","reported","submitted","corrected","voided","included","closed"]}},"invariants":["Worklog is a reported observation and never proves presence, productivity or quality.","Missing worklog is unknown and explicit zero requires a record.","Performer, engagement, assignment and task remain externally mastered.","Every quantity declares unit, basis and interval or observation period.","Result time, report time and ingestion time remain distinct.","Overlapping worklogs remain recorded and are flagged rather than silently merged.","Capacity computation counts overlapping elapsed time once under a declared rule.","Corrections are additive and linked to predecessors.","Worklog inclusion never changes the source record identity.","Timesheet approval never makes the worklog objectively true.","Nominal and elapsed durations remain distinct.","Voiding preserves provenance and prior inclusion history."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Effort units, overlap and payroll crosswalks require canonical governance.","Package conversion and live verification are pending."]}


## Worklog fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Worklog","cases":[{"id":"reported-project-time","kind":"positive","input":"A worker reports two hours against a project task with result and ingestion times.","expect":"The worklog is attributable without proving presence or quality."},{"id":"overlapping-logs","kind":"positive","input":"Two project worklogs overlap by thirty minutes.","expect":"Both remain, an overlap finding is emitted and capacity is not doubled."},{"id":"explicit-zero","kind":"positive","input":"A worker explicitly reports zero time for a required period.","expect":"Zero is distinguished from missing."},{"id":"worklog-proves-presence","kind":"negative","input":"Reported time is treated as verified physical presence.","expect":"The inference is rejected."},{"id":"missing-is-zero","kind":"negative","input":"No worklog is interpreted as zero work.","expect":"The collapse is rejected."},{"id":"silent-overlap-merge","kind":"negative","input":"Overlapping records are silently merged into one.","expect":"The mutation is rejected."}]}


## Worklog validation policy

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## Timesheet allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-PEO-07","proposedName":"Timesheet","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A period-scoped declaration of a fixed member set remains identifiable across submission, approval, rejection and later correction independently of its worklogs.","versionIdentity":"Member-set or declaration corrections create linked successor revisions or adjustment entries; an approved revision is immutable.","independentLifecycle":["draft","submitted","returned","approved","rejected","superseded","adjusted","closed"],"mastership":"time-reporting and approval authority"},"boundary":{"owns":["persistent timesheet identity","person, engagement and reporting period","immutable member-set digest","submission declaration","approval decision and scope","authority and decision time","return, rejection and adjustment history","supersession and closure lineage"],"references":[{"target":"WM-PER-001","purpose":"Person anchor"},{"target":"WM-ORG-005","purpose":"Engagement"},{"target":"WM-ORG-016","purpose":"Assignment context"},{"target":"WM-XCT-009","purpose":"Reporting period calendar"},{"target":"WM-REC-010","purpose":"Issued approval record"}],"excludes":["worklog identity or content mastership","presence, performance or quality proof","payroll calculation or payment","employment or assignment identity","absence or availability projection","silent mutation of approved periods"]},"objects":{"Timesheet":{"identity":["timesheetId"],"required":["personRef","engagementRef","period","status"],"optional":["successorRef","closedAt"],"lifecycle":["draft","submitted","returned","approved","rejected","superseded","adjusted","closed"]},"TimesheetRevision":{"identity":["timesheetId","revision"],"required":["memberWorklogRefs","memberDigest","declaration","contentDigest"],"optional":["approval","adjustmentRefs","supersedesRevision"]}},"invariants":["Every timesheet identifies one person, engagement and reporting period.","Submission freezes an immutable member set and digest.","Approval names scope, authority, decision and time.","Approval attests review and never proves presence, productivity or quality.","Approved revisions are immutable.","Corrections create linked successor revisions or adjustment entries.","Worklogs remain independently identified and externally mastered.","Rejection and return remain distinct from withdrawal or correction.","Time Approval is aggregate-owned and never an independent model root.","Timesheet approval never creates payroll result or payment.","Missing worklogs remain unknown and explicit zero remains a worklog assertion.","Closed timesheets remain resolvable with all approvals and adjustments."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Payroll, labor-policy and approval-authority crosswalks require canonical review.","Package conversion and live verification are pending."]}


## Timesheet fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Timesheet","cases":[{"id":"approved-period","kind":"positive","input":"A submitted period pins five worklogs and is approved by an authorized reviewer.","expect":"Member digest, approval scope, authority and decision time are immutable."},{"id":"post-approval-adjustment","kind":"positive","input":"One worklog is corrected after approval.","expect":"A linked adjustment or successor revision preserves the original approved period."},{"id":"returned-period","kind":"positive","input":"A reviewer returns a timesheet for clarification.","expect":"Return is recorded without approval or deletion."},{"id":"approval-proves-quality","kind":"negative","input":"Approved timesheet is used as proof of work quality.","expect":"The inference is rejected."},{"id":"edit-approved-members","kind":"negative","input":"An approved member set is edited in place.","expect":"The mutation is rejected."},{"id":"approval-is-payment","kind":"negative","input":"Timesheet approval is treated as completed payroll payment.","expect":"The inference is rejected."}]}


## Timesheet validation policy

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}

