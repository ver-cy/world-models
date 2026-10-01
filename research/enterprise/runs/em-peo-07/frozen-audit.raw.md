# EM-PEO-07 — Frozen semantic audit

Sole final audit. No tools, no browsing, no rerun. No runtime or model identifier is allocated here. No standards conformance, canonical completeness or installability is claimed.

---

## 1. Verdict

**Decision: upheld.** The settled boundary survives the artifacts and all three inputs. Specifically:

- **Absence, Worklog, Timesheet as identifier-unassigned independent candidates — upheld.** Each passes a distinct identity test on a distinct lifecycle (governed case, reported observation, period container), and none is reducible to WM-PER-001, WM-ORG-005, WM-ORG-016, WM-ACT-006, WM-XCT-009 or WM-ACT-008.
- **Work Calendar profiles WM-XCT-009; Availability is a derived projection — upheld.** WM-XCT-009's own position that derived working-day calendars are not master data is the controlling evidence, and nothing in the artifacts contradicts it.
- **Time Approval is an identified append-only decision inside Timesheet — upheld.** Approval identity is `timesheetId` + sequence; it is aggregate-owned and is not a peer model root.
- **WM-ACT-008 is reference-only — upheld, and reinforced.** Its admitted `known_omissions` (VAVAILABILITY not modelled beyond free-busy; no capacity, rostering or working-time limits) and its unresolved `deferredResearch` question disqualify it as master. Its `publishableCanonical: false` status independently bars mastership here.
- **No identifier allocated — upheld.** All three candidates hold `modelId: null`, `registryId: null`, `allocationState: "unassigned"`.

**Artifacts: not acceptable as frozen, remediable without new study.** Sixteen material defects follow. Twelve are internal contradictions or unsatisfiable invariants inside the artifacts themselves — the artifacts assert rules that their declared object shapes cannot express. One (defect 10) introduces an identifier not present in any admitted evidence. None of the sixteen requires a new study, a new source, or a reopened boundary question: each has a mechanical remediation stated below.

Two points considered and **rejected as defects**, recorded so they are not reopened:

- Grok's reading that Timesheet should reference "the planned allocations in scope" is **not adopted**. Pulling allocation references into the period container would let Timesheet carry a capacity assertion, which its own `excludes` correctly forbids. Allocation stays on WM-ORG-016 and reaches the projection, not the timesheet.
- Grok's blocker "identifiers are still unassigned, so master references cannot be closed" is **not a defect**. Unassigned identity is the settled state of this contour. It remains a hold, already recorded on all three candidates.

### Invariant slug vocabulary used in §3

`inv-interval-pins-offset-tz-release`, `inv-missing-is-unknown`, `inv-medical-reason-excluded`, `inv-quantities-separate`, `inv-allocation-fraction-of-contracted-capacity`, `inv-worklog-not-presence-productivity-quality`, `inv-overlaps-retained-not-collapsed`, `inv-worklog-excluded-from-capacity`, `inv-nominal-exact-distinct`, `inv-approved-immutable`, `inv-corrections-additive-linked`, `inv-availability-derived-with-manifest`, `inv-work-calendar-no-independent-mastership`, `inv-residual-never-negative-never-doubled`, `inv-time-approval-scoped-inside-timesheet`, `inv-act-008-reference-only`, `inv-quantity-declares-unit-and-basis`, `inv-external-mastership-preserved`, `inv-overcommitment-is-finding-not-rewrite`, `inv-evidence-grounded-reference`.

---

## 2. Material defects and exact remediation

**1. The profile candidate lists WM-ACT-008 among `bases`, contradicting reference-only.**
A `PROFILE` decision over a base asserts the right to constrain and extend that base. Listing WM-ACT-008 as a base makes it a profiled model, which is exactly the mastership the decision refuses. WM-PER-001 is likewise a reuse anchor, not a profiled base.

*Remediation.* In the profile candidate set `"bases": ["WM-XCT-009","WM-ORG-005","WM-ORG-016"]`. Add `"references": [{"target":"WM-ACT-008","purpose":"Scheduled intent, reference-only"},{"target":"WM-PER-001","purpose":"Person anchor, reference-only"}]`. Append the constraint: `"WM-ACT-008 and WM-PER-001 are reference-only; this profile never constrains, extends, redefines or re-masters them."` Add `"canonicalPublishable": false`.

**2. No closed availability formula, no non-negativity rule, no overcommitment reporting rule.**
The profile asserts that the four quantities stay separate but never states how availability is computed or what happens when allocation exceeds it. The Absence invariant "Approved absence reduces planned availability only under the applicable calendar and policy" names no policy. With no closed form, the DST/half-time/dual-allocation case has no defined answer.

*Remediation.* Append to the profile constraints, verbatim:
`"plannedAvailability = (contractualPattern ∩ workCalendarWorkingTime) − approvedOrdinaryAbsence, evaluated against the pinned manifest."`
`"allocationResidual = contractedCapacityFraction − Σ(assignmentAllocationFraction) over concurrent assignments in the period."`
`"residualFraction is published only when allocationResidual ≥ 0; it is never published negative and never clamped silently."`
`"When allocationResidual < 0 the projection publishes residualFraction 0 together with an overcommitment finding carrying excessFraction = −allocationResidual, and leaves every source assignment, absence and worklog unchanged."`
`"No worklog, timesheet or approval is an input to plannedAvailability or allocationResidual."`

**3. Worklog invariant 7 admits worklogs into capacity computation.**
`"Capacity computation counts overlapping elapsed time once under a declared rule"` concedes that worklogs feed capacity, which directly contradicts the boundary that worklog is observation only and does not consume contractual capacity. The rule is also undeclared.

*Remediation.* Replace Worklog invariant 7 with two invariants:
`"Worklog never reduces planned availability, contracted capacity or allocation residual."`
`"Overlapping worklogs are reported under an elapsed-time reconciliation rule that counts each overlapping clock interval once for reporting only; the reconciled figure is never summed into capacity, availability or residual."`
Add to Worklog `excludes`: `"capacity, availability or residual computation input"`.

**4. `interval` and `period` are undeclared scalars, so the offset/timezone/ruleset invariants are unsatisfiable.**
Absence invariant 10, Worklog's time-rules reference and Timesheet's `period` all depend on a structure none of the three objects declares. As written, a bare local date range satisfies the schema while violating the invariant.

*Remediation.* Declare one shared structure in each candidate's `objects` map as `Interval`, with `"required": ["startInstant","endInstant","startOffset","endOffset","tzid","tzdbRelease"]` and `"optional": ["durationKind","nominalDuration","exactDuration"]`. Make `Absence.interval`, `Timesheet.period` and `Worklog.interval` typed as `Interval`. Add to each candidate's invariant list: `"An interval is rejected unless both bounds carry an explicit offset and the interval carries tzid and tzdbRelease."`

**5. Nominal versus exact duration has no representation.**
All three inputs require the distinction; no object carries a field that expresses it, so "nominal and exact never substitute" cannot be checked.

*Remediation.* On `Interval` make `durationKind` required with closed enumeration `["exact","nominal"]`. On `Worklog` add required `durationKind` and optional `nominalDuration` alongside `quantity`. Add to the profile constraints: `"A nominal duration is never rewritten to equal an exact duration and an exact duration is never rewritten to equal a nominal duration; a transition day carries 23 or 25 exact hours with its nominal day unchanged."`

**6. Medical exclusion is a projection rule, not structural.**
`Absence.optional` includes `protectedReasonRef`, so the protected reason hangs off the same object the ordinary availability projection reads. Exclusion then depends on every consumer honouring a policy. Separately, `operationalCategory` has no closed enumeration, so a diagnostic string satisfies the schema.

*Remediation.* Remove `protectedReasonRef` from `Absence.optional`. Declare a separate object `AbsenceProtectedReason` with `"identity": ["absenceId","reasonSequence"]`, `"required": ["absenceRef","reasonCoding","lawfulConditionRef","recordedAt"]`, held in a separately governed partition, and declare the link resolvable **only** from the protected side — the ordinary record holds no forward path. Add to `Absence.excludes`: `"protected reason storage or any forward reference to it"`. Set `operationalCategory` to the closed enumeration `["unavailable","partially-available","available-with-restriction"]`. Add the invariant: `"operationalCategory accepts only its enumerated values; any free-text, coded clinical or diagnostic value is rejected."` Add the hold: `"Resolution of AbsenceProtectedReason requires an additional lawful condition per WM-PER-001 and is excluded from every default projection."`

**7. Absence has no revision object, and `successorRef` conflates two different successions.**
`versionIdentity` promises append-only versions and `invariants` promise that corrections append successors, but the only object is a flat `Absence` with `successorRef`. Timesheet got this right with `TimesheetRevision`; Absence did not. `successorRef` is also doing double duty for "corrected version of this case" and "next distinct episode", which are different relations.

*Remediation.* Reduce `Absence` to `"identity": ["absenceId"]`, `"required": ["personRef","engagementRef","status"]`, `"optional": ["closedAt"]`, with `status` declared derived from the latest revision. Add `AbsenceRevision` with `"identity": ["absenceId","revision"]`, `"required": ["interval","operationalCategory","revisionStatus","recordedAt","actorRef"]`, `"optional": ["quantity","quantityUnit","quantityBasis","requestRef","decisionRef","supersedesRevision"]`. Delete `successorRef`; add `relatedEpisodeRef` to `Absence.optional` for episode-to-episode linkage only. Remove `corrected` from the case lifecycle; corrections are revisions, not a case state.

**8. Worklog permits an in-place `corrected` state.**
A `corrected` lifecycle state on a mutable `Worklog` means the reported value is overwritten, which defeats additive correction and destroys the as-reported observation.

*Remediation.* Replace the Worklog lifecycle with `["draft","reported","submitted","included","superseded","voided","closed"]` — `corrected` is removed. Add the invariant: `"A Worklog is immutable once reported; a correction is a new worklogId carrying supersedesRef, and the predecessor transitions to superseded with its reported values intact."` Rename `supersedesRef` to `supersedesWorklogRef` and add optional `supersededByWorklogRef` so the link is bidirectionally resolvable.

**9. Time Approval is asserted everywhere and declared nowhere.**
`TimesheetRevision.approval` is an unstructured optional field. There is no approval identity, no sequence, no authority, no separation-of-duties constraint, no append-only guarantee — yet the boundary rests on all five.

*Remediation.* Add to the Timesheet candidate's `objects`: `TimeApproval` with `"identity": ["timesheetId","approvalSequence"]`, `"required": ["scope","authorityRef","approverRef","decision","decidedAt","memberDigest"]`, `"optional": ["priorApprovalSequence","rationale"]`, where `scope` is the closed enumeration `["entry","day","period"]` and `decision` is `["approved","rejected","returned"]`. Delete `TimesheetRevision.approval`; replace it with optional `approvalSequences`. Add the invariants: `"TimeApproval entries are append-only; an existing sequence is never overwritten, reordered or deleted."` and `"Where separation of duties applies, approverRef must not equal the timesheet personRef."` Add to `excludes`: `"TimeApproval as an independent model root or externally mastered record"`.

**10. The Timesheet candidate references WM-REC-010, which no admitted evidence supports.**
WM-REC-010 appears in none of the study, the synthesis or the Grok response, and the purpose given — "Issued approval record" — would place approval mastership outside the Timesheet aggregate, contradicting the settled boundary. I cannot verify that this identifier exists and will not treat it as grounded.

*Remediation.* Remove `{"target":"WM-REC-010","purpose":"Issued approval record"}` from Timesheet `references`. The remaining four references (WM-PER-001, WM-ORG-005, WM-ORG-016, WM-XCT-009) satisfy `minimumReferences: 3`. Record the hold: `"Whether an issued-record model should carry externally attested approval evidence is an open question deferred to registry allocation; no such reference is asserted here."`

**11. Absence `owns` "availability-projection effect" while `excludes` "availability projection or capacity fact".**
A direct internal contradiction. One of the two must yield, and the boundary says the projection is not Absence's.

*Remediation.* Replace the owned item `"availability-projection effect"` with `"declared operational effect consumed by the availability projection"`. Keep the `excludes` entry unchanged.

**12. Quantities carry no unit or basis.**
`Absence.quantity` is optional with no unit and no basis field, so "4" is schema-valid and meaningless. Worklog's invariant `"Every quantity declares unit, basis and interval or observation period"` names a `basis` and an `observationPeriod` that the `Worklog` object does not have. WM-ORG-016's FTE and effort-fraction gap makes an undeclared basis a live hazard, not a formality.

*Remediation.* On `AbsenceRevision` declare the co-presence rule: `quantity` requires both `quantityUnit` and `quantityBasis`. On `Worklog` move `basis` into `required` and add optional `observationPeriod`, with the invariant: `"Exactly one of interval or observationPeriod is present on every Worklog."` Add to both candidates: `"A quantity without a declared unit, code system and basis is rejected; rounding occurs only at projection."`

**13. The Availability and Work Calendar projection manifest and run identity are undefined.**
"Complete input manifest" is asserted in the profile and in both invariant lists, with no statement of what the manifest contains or how a run is identified — so a projection with no release pinning satisfies the artifact as written.

*Remediation.* Add to the profile a `projections` block declaring `WorkCalendarProjection` and `AvailabilityProjection`, each with `"identity": ["runId"]` and `"required": ["computedAt","tzdbRelease","calendarRuleSetRelease","organizationalScopeRef","periodRef","patternRef","absenceSetDigest","allocationSetDigest","policyRef"]`. Add the constraints: `"A projection missing any manifest element is not published."` and `"An earlier projection is never re-derived in place; a new computation is a new runId."`

**14. The profile candidate has no fixture set and no validation policy, and the three existing validation policies are under-specified.**
Absence, Worklog and Timesheet each carry fixtures plus a policy; the profile — which owns the residual formula, the DST rules, the overlap rule and the manifest, i.e. the whole contested surface — carries neither. The existing policies also set `requiresPositiveAndNegativeFixtures: true` with no per-kind minimum, and require nothing of fixture structure. *Closed by artifact edit and by the profile fixtures in §3, not by a single case.*

*Remediation.* Add `{"format":"vercy-allocation-validation/v1","requirements":{"newRuntimeIdMustBeFalse":true,"canonicalPublishableMustBeFalse":true,"minimumConstraints":10,"minimumBases":1,"minimumFixtures":10,"minimumPositiveFixtures":4,"minimumNegativeFixtures":6,"requiresProjectionManifest":true,"requiresExpectedCodeOnNegatives":true}}` for the profile. In all four policies add `"minimumPositiveFixtures": 3`, `"minimumNegativeFixtures": 3`, `"requiresExpectedCodeOnNegatives": true`, `"requiresViolatesOnNegatives": true`, `"requiresDefectLinkage": true`.

**15. Fixture records carry no `violates` and no `expectedCode`, so the nine prior negatives are not deterministically checkable.**
"The disclosure is rejected" names no rule and no code. Two implementations can both pass. *Closed by artifact edit.*

*Remediation.* Add `violates` and `expectedCode` to every prior negative, exactly as follows, and `"violates": null, "expectedCode": null` to every prior positive.

| Prior negative | violates | expectedCode |
|---|---|---|
| `medical-reason-in-calendar` | `inv-medical-reason-excluded` | `EM-PEO-07-ABS-101` |
| `missing-means-present` | `inv-missing-is-unknown` | `EM-PEO-07-ABS-102` |
| `rewrite-approved` | `inv-approved-immutable` | `EM-PEO-07-ABS-103` |
| `worklog-proves-presence` | `inv-worklog-not-presence-productivity-quality` | `EM-PEO-07-WKL-101` |
| `missing-is-zero` | `inv-missing-is-unknown` | `EM-PEO-07-WKL-102` |
| `silent-overlap-merge` | `inv-overlaps-retained-not-collapsed` | `EM-PEO-07-WKL-103` |
| `approval-proves-quality` | `inv-worklog-not-presence-productivity-quality` | `EM-PEO-07-TSH-101` |
| `edit-approved-members` | `inv-approved-immutable` | `EM-PEO-07-TSH-102` |
| `approval-is-payment` | `inv-timesheet-not-entitlement-or-payment` | `EM-PEO-07-TSH-103` |

**16. Timesheet root `status` competes with revision state, weakening approved immutability.**
`Timesheet.required` includes `status` while `TimesheetRevision` holds the approval and the member digest. If the root status is independently writable, an approved revision can be made to appear draft without touching the revision — immutability of the revision becomes cosmetic.

*Remediation.* Add `revisionStatus` to `TimesheetRevision.required` with the enumeration `["draft","submitted","returned","approved","rejected","superseded","adjusted","closed"]`. Redeclare `Timesheet.status` as `"derived": "latestRevision.revisionStatus"` and add the invariant: `"Timesheet.status is derived from the latest revision and is never independently written."`

---

## 3. Additional fixtures

Conventions: `violates` and `expectedCode` are `null` on positives, since conforming input violates nothing. `closesDefect` is the primary defect number from §2. `target` is the candidate name, or `Enterprise Work Calendar and Availability` for the profile.

```json
[
  {"id":"cal-residual-closed-form","target":"Enterprise Work Calendar and Availability","kind":"positive","input":"Half-time engagement with contractedCapacityFraction 0.5 against a declared FTE basis, two concurrent assignments at 0.25 each, no ordinary absence, Europe/Athens, tzdbRelease and calendarRuleSetRelease pinned in the manifest.","expect":"plannedAvailability is computed as pattern intersected with calendar working time minus approved ordinary absence; allocationResidual is published as 0.0; no worklog is read.","violates":null,"closesDefect":2,"expectedCode":null},
  {"id":"cal-residual-published-negative","target":"Enterprise Work Calendar and Availability","kind":"negative","input":"contractedCapacityFraction 0.5 with concurrent allocations 0.25 and 0.35; the projection publishes residualFraction -0.10.","expect":"The projection is rejected; a negative residualFraction is never published.","violates":"inv-residual-never-negative-never-doubled","closesDefect":2,"expectedCode":"EM-PEO-07-CAL-001"},
  {"id":"cal-overcommitment-finding","target":"Enterprise Work Calendar and Availability","kind":"positive","input":"contractedCapacityFraction 0.5 with concurrent allocations 0.25 and 0.35.","expect":"residualFraction 0 is published with an overcommitment finding carrying excessFraction 0.10; both source assignments, the absence set and every worklog remain unchanged.","violates":null,"closesDefect":2,"expectedCode":null},
  {"id":"cal-worklog-subtracted-from-residual","target":"Enterprise Work Calendar and Availability","kind":"negative","input":"Residual capacity is recomputed by subtracting the exact elapsed duration of the period's worklogs from plannedAvailability.","expect":"The computation is rejected; worklogs are not inputs to availability or residual.","violates":"inv-worklog-excluded-from-capacity","closesDefect":3,"expectedCode":"EM-PEO-07-CAL-002"},
  {"id":"cal-overlap-summed-into-capacity","target":"Enterprise Work Calendar and Availability","kind":"negative","input":"Two worklogs on different charge targets overlap by one clock hour; both elapsed durations are summed and charged against contracted capacity.","expect":"The computation is rejected; the overlapping clock interval is counted once for reporting only and never enters capacity.","violates":"inv-overlaps-retained-not-collapsed","closesDefect":3,"expectedCode":"EM-PEO-07-CAL-003"},
  {"id":"cal-fall-back-repeated-hour","target":"Enterprise Work Calendar and Availability","kind":"positive","input":"Europe/Athens fall-back day 2026-10-25 on which local 03:00-03:59 occurs twice, first at offset +03:00 then at offset +02:00, with tzdbRelease pinned.","expect":"The day resolves to 25 exact hours with both occurrences distinguished by offset; the nominal working day from the contractual pattern is unchanged and plannedAvailability does not grow.","violates":null,"closesDefect":5,"expectedCode":null},
  {"id":"cal-spring-forward-nominal-stable","target":"Enterprise Work Calendar and Availability","kind":"positive","input":"Europe/Athens spring-forward day 2026-03-29 on which local 03:00-03:59 does not exist.","expect":"The day resolves to 23 exact hours; the week still yields five nominal working days and plannedAvailability neither shrinks nor inflates.","violates":null,"closesDefect":5,"expectedCode":null},
  {"id":"cal-nominal-rewritten-to-exact","target":"Enterprise Work Calendar and Availability","kind":"negative","input":"On the spring-forward day the nominal working duration is rewritten to 7 hours to match the 23 exact clock hours of the day.","expect":"The rewrite is rejected; nominal duration is never derived from or replaced by exact elapsed duration.","violates":"inv-nominal-exact-distinct","closesDefect":5,"expectedCode":"EM-PEO-07-CAL-004"},
  {"id":"cal-manifest-complete","target":"Enterprise Work Calendar and Availability","kind":"positive","input":"An AvailabilityProjection run declares runId, computedAt, tzdbRelease, calendarRuleSetRelease, organizationalScopeRef, periodRef, patternRef, absenceSetDigest, allocationSetDigest and policyRef.","expect":"The projection is publishable as derived, non-master output addressed by runId.","violates":null,"closesDefect":13,"expectedCode":null},
  {"id":"cal-manifest-missing-release","target":"Enterprise Work Calendar and Availability","kind":"negative","input":"An AvailabilityProjection is published with no tzdbRelease and no calendarRuleSetRelease in its manifest.","expect":"Publication is rejected; an incomplete manifest is not publishable.","violates":"inv-availability-derived-with-manifest","closesDefect":13,"expectedCode":"EM-PEO-07-CAL-005"},
  {"id":"cal-availability-mastered-as-person-fact","target":"Enterprise Work Calendar and Availability","kind":"negative","input":"A computed availability window is stored as a mastered attribute of the person and later read as authoritative without a run manifest.","expect":"The mastership is rejected; availability is derived and resolvable only as an identified run.","violates":"inv-work-calendar-no-independent-mastership","closesDefect":13,"expectedCode":"EM-PEO-07-CAL-006"},
  {"id":"cal-act-008-profiled","target":"Enterprise Work Calendar and Availability","kind":"negative","input":"The profile adds a constraint that narrows a WM-ACT-008 scheduling component and treats WM-ACT-008 as a profiled base.","expect":"The constraint is rejected; WM-ACT-008 is reference-only and is never profiled, constrained or extended.","violates":"inv-act-008-reference-only","closesDefect":1,"expectedCode":"EM-PEO-07-CAL-007"},
  {"id":"cal-act-008-reference-only","target":"Enterprise Work Calendar and Availability","kind":"positive","input":"A dated scheduled commitment held in WM-ACT-008 is cited by the availability projection as planned intent.","expect":"The citation resolves as a reference; the commitment does not master pattern, absence, allocation or availability, and the projection still derives from pattern, calendar, absence and allocation only.","violates":null,"closesDefect":1,"expectedCode":null},
  {"id":"abs-revision-append","target":"Absence","kind":"positive","input":"An approved absence is shortened by one day; a new AbsenceRevision records the shorter interval with recordedAt, actorRef and supersedesRevision.","expect":"The prior revision, its interval, its operationalCategory and its decision remain retrievable; the case identity is unchanged.","violates":null,"closesDefect":7,"expectedCode":null},
  {"id":"abs-in-place-revision-edit","target":"Absence","kind":"negative","input":"The interval on an existing approved AbsenceRevision is edited in place with no successor revision.","expect":"The mutation is rejected; corrections append a revision and never rewrite one.","violates":"inv-corrections-additive-linked","closesDefect":7,"expectedCode":"EM-PEO-07-ABS-001"},
  {"id":"abs-new-episode-new-case","target":"Absence","kind":"positive","input":"The same person is absent again two months after a closed case, for an unrelated reason.","expect":"A new absenceId is created and linked by relatedEpisodeRef; it is not recorded as a revision of the closed case.","violates":null,"closesDefect":7,"expectedCode":null},
  {"id":"abs-category-enumeration","target":"Absence","kind":"positive","input":"An absence on medical grounds is recorded with operationalCategory partially-available and its clinical reason held as an AbsenceProtectedReason with a lawfulConditionRef.","expect":"The ordinary availability projection reads only the enumerated operational category and has no forward path from Absence to the protected reason.","violates":null,"closesDefect":6,"expectedCode":null},
  {"id":"abs-diagnosis-in-category","target":"Absence","kind":"negative","input":"operationalCategory is set to a coded diagnostic value rather than one of unavailable, partially-available or available-with-restriction.","expect":"The value is rejected; operationalCategory accepts only its enumerated values.","violates":"inv-medical-reason-excluded","closesDefect":6,"expectedCode":"EM-PEO-07-ABS-002"},
  {"id":"abs-protected-reason-without-condition","target":"Absence","kind":"negative","input":"An ordinary capacity report resolves AbsenceProtectedReason and renders the clinical reason without an additional lawful condition.","expect":"The resolution is rejected; the protected partition is reachable only under an additional lawful condition and is excluded from every default projection.","violates":"inv-medical-reason-excluded","closesDefect":6,"expectedCode":"EM-PEO-07-ABS-003"},
  {"id":"abs-interval-missing-release","target":"Absence","kind":"negative","input":"An absence interval is recorded as two local dates with no bound offsets, no tzid and no tzdbRelease.","expect":"The interval is rejected; both bounds require explicit offsets and the interval requires tzid and tzdbRelease.","violates":"inv-interval-pins-offset-tz-release","closesDefect":4,"expectedCode":"EM-PEO-07-ABS-004"},
  {"id":"abs-quantity-with-basis","target":"Absence","kind":"positive","input":"A partial-day absence records quantity 4 with quantityUnit hour and quantityBasis the declared contractual nominal day.","expect":"The quantity is accepted and is interpretable without inferring a basis; rounding occurs only at projection.","violates":null,"closesDefect":12,"expectedCode":null},
  {"id":"abs-quantity-without-basis","target":"Absence","kind":"negative","input":"A partial-day absence records quantity 4 with no quantityUnit and no quantityBasis.","expect":"The record is rejected; quantity requires a declared unit, code system and basis.","violates":"inv-quantity-declares-unit-and-basis","closesDefect":12,"expectedCode":"EM-PEO-07-ABS-005"},
  {"id":"abs-publishes-availability-projection","target":"Absence","kind":"negative","input":"The absence record publishes a computed availability window as its own owned output.","expect":"The publication is rejected; Absence owns a declared operational effect and never an availability projection or capacity fact.","violates":"inv-quantities-separate","closesDefect":11,"expectedCode":"EM-PEO-07-ABS-006"},
  {"id":"wkl-correction-supersedes","target":"Worklog","kind":"positive","input":"A reported worklog of 6 hours is corrected to 4 hours after submission.","expect":"A new worklogId records 4 hours with supersedesWorklogRef; the predecessor transitions to superseded with its reported 6 hours, its reportedAt and its method intact and bidirectionally linked.","violates":null,"closesDefect":8,"expectedCode":null},
  {"id":"wkl-in-place-correction","target":"Worklog","kind":"negative","input":"The quantity on a reported worklog is overwritten from 6 to 4 hours on the same worklogId.","expect":"The mutation is rejected; a Worklog is immutable once reported and corrections create a superseding record.","violates":"inv-corrections-additive-linked","closesDefect":8,"expectedCode":"EM-PEO-07-WKL-001"},
  {"id":"wkl-duration-kind-exact","target":"Worklog","kind":"positive","input":"Work spanning the Europe/Athens spring-forward transition is reported with durationKind exact, bounded instants carrying offsets +02:00 and +03:00, and a separately stated nominalDuration of one working day.","expect":"Exact elapsed duration and nominal duration are both retained and neither is derived from the other.","violates":null,"closesDefect":5,"expectedCode":null},
  {"id":"wkl-nominal-as-exact","target":"Worklog","kind":"negative","input":"A worklog reports one nominal working day and the value is read as exact elapsed clock time in a duration sum.","expect":"The substitution is rejected; nominal and exact durations are never interchanged.","violates":"inv-nominal-exact-distinct","closesDefect":5,"expectedCode":"EM-PEO-07-WKL-002"},
  {"id":"wkl-observation-period-basis","target":"Worklog","kind":"positive","input":"A weekly aggregate of 20 hours is reported with observationPeriod, basis, unit hour and no interval.","expect":"The record is accepted with exactly one of interval or observationPeriod present, and its phenomenon, result and ingestion times remain distinct.","violates":null,"closesDefect":12,"expectedCode":null},
  {"id":"wkl-quantity-without-unit","target":"Worklog","kind":"negative","input":"A worklog reports quantity 7.5 with no unit, no code system and no basis.","expect":"The record is rejected; every quantity declares unit, code system and basis.","violates":"inv-quantity-declares-unit-and-basis","closesDefect":12,"expectedCode":"EM-PEO-07-WKL-003"},
  {"id":"wkl-ambiguous-local-fall-back","target":"Worklog","kind":"negative","input":"A worklog on the Europe/Athens fall-back day starts at local 03:30 with no offset, so the instant is ambiguous between the +03:00 and +02:00 occurrences.","expect":"The entry is rejected and flagged as an anomaly; the ambiguity is never silently resolved to either occurrence.","violates":"inv-interval-pins-offset-tz-release","closesDefect":4,"expectedCode":"EM-PEO-07-WKL-004"},
  {"id":"wkl-overlap-reduces-availability","target":"Worklog","kind":"negative","input":"Two overlapping worklogs on different charge targets are used to reduce the person's plannedAvailability for the day.","expect":"The reduction is rejected; worklogs are retained and flagged as observations and never consume availability, capacity or residual.","violates":"inv-worklog-excluded-from-capacity","closesDefect":3,"expectedCode":"EM-PEO-07-WKL-005"},
  {"id":"tsh-approval-declared","target":"Timesheet","kind":"positive","input":"A submitted revision pinning five worklogs is approved by an authorized reviewer who is not the performer.","expect":"A TimeApproval is written at timesheetId plus approvalSequence 1 with scope period, authorityRef, approverRef, decision approved, decidedAt and the frozen memberDigest.","violates":null,"closesDefect":9,"expectedCode":null},
  {"id":"tsh-approval-as-root","target":"Timesheet","kind":"negative","input":"TimeApproval is given a standalone root identity and is resolved without its timesheetId.","expect":"The identity is rejected; TimeApproval is identified only as timesheetId plus approvalSequence inside the aggregate.","violates":"inv-time-approval-scoped-inside-timesheet","closesDefect":9,"expectedCode":"EM-PEO-07-TSH-001"},
  {"id":"tsh-self-approval","target":"Timesheet","kind":"negative","input":"Under an applicable separation-of-duties rule, approverRef equals the timesheet personRef.","expect":"The approval is rejected; the approver must be distinct from the performer where separation of duties applies.","violates":"inv-time-approval-scoped-inside-timesheet","closesDefect":9,"expectedCode":"EM-PEO-07-TSH-002"},
  {"id":"tsh-approval-entry-overwritten","target":"Timesheet","kind":"negative","input":"An existing TimeApproval at approvalSequence 1 is overwritten with a later rejection decision.","expect":"The overwrite is rejected; approvals are append-only and a later decision is a new sequence referencing the prior one.","violates":"inv-approved-immutable","closesDefect":9,"expectedCode":"EM-PEO-07-TSH-003"},
  {"id":"tsh-unverified-base-reference","target":"Timesheet","kind":"negative","input":"The candidate asserts a reference to an issued-record model that appears in no admitted evidence for this contour, and routes approval mastership to it.","expect":"The reference is rejected; references must be grounded in admitted evidence and approval mastership stays inside the Timesheet aggregate.","violates":"inv-evidence-grounded-reference","closesDefect":10,"expectedCode":"EM-PEO-07-TSH-004"},
  {"id":"tsh-revision-immutable","target":"Timesheet","kind":"positive","input":"Revision 1 is approved; a later reporting change opens revision 2 with supersedesRevision 1.","expect":"Revision 1 keeps its memberWorklogRefs, memberDigest, contentDigest, revisionStatus approved and its approval sequences; Timesheet.status is derived from the latest revision.","violates":null,"closesDefect":16,"expectedCode":null},
  {"id":"tsh-root-status-independent-write","target":"Timesheet","kind":"negative","input":"Timesheet.status is written directly to draft while the latest revision carries revisionStatus approved.","expect":"The write is rejected; Timesheet.status is derived from the latest revision and is never independently written.","violates":"inv-approved-immutable","closesDefect":16,"expectedCode":"EM-PEO-07-TSH-005"},
  {"id":"tsh-period-missing-tz","target":"Timesheet","kind":"negative","input":"The reporting period is recorded as two local dates with no tzid and no tzdbRelease.","expect":"The period is rejected; period bounds carry explicit offsets and the period carries tzid and tzdbRelease.","violates":"inv-interval-pins-offset-tz-release","closesDefect":4,"expectedCode":"EM-PEO-07-TSH-006"},
  {"id":"tsh-post-approval-supersession","target":"Timesheet","kind":"positive","input":"After approval of revision 1, one member worklog is superseded by a corrected worklog reducing it by two hours.","expect":"The approved memberDigest and total of revision 1 are unchanged; a linked adjustment entry carries the two-hour delta with reason, classification and authorising agent, and the prior approval remains retrievable.","violates":null,"closesDefect":8,"expectedCode":null}
]
```

---

## 4. Exact final fixture counts

**Prior fixtures: 18 — 9 positive, 9 negative.**
**Additional fixtures: 40 — 16 positive, 24 negative.**
**Total fixtures: 58 — 25 positive, 33 negative.**

| Target | Prior (P/N) | Additional (P/N) | Total (P/N) |
|---|---|---|---|
| Absence | 6 (3/3) | 10 (4/6) | 16 (7/9) |
| Worklog | 6 (3/3) | 8 (3/5) | 14 (6/8) |
| Timesheet | 6 (3/3) | 9 (3/6) | 15 (6/9) |
| Enterprise Work Calendar and Availability | 0 (0/0) | 13 (6/7) | 13 (6/7) |
| **All targets** | **18 (9/9)** | **40 (16/24)** | **58 (25/33)** |

Every one of the 24 additional negatives carries a distinct `expectedCode`. With the §2.15 remediation applied, all 33 negatives in the total set carry a distinct code: 24 in the `-001`..`-00n` ranges and 9 in the `-101`..`-103` ranges.

Post-remediation validation check: Absence 16 fixtures (7/9), Worklog 14 (6/8), Timesheet 15 (6/9) each clear `minimumFixtures: 3` and the added per-kind minimum of 3; the profile's 13 (6/7) clears its `minimumFixtures: 10`, `minimumPositiveFixtures: 4` and `minimumNegativeFixtures: 6`. Timesheet retains 4 references after removing the ungrounded one, clearing `minimumReferences: 3`. All three candidates retain 12 invariants or more against `minimumInvariants: 8`.

---

## 5. Freeze decision

**FROZEN — boundary and disposition. Artifact revision is a deterministic edit pass. No rerun, no further study, no identifier allocation.**

Frozen as settled, not to be reopened on this contour:

- Absence, Worklog and Timesheet are independent, identifier-unassigned new-model candidates.
- Work Calendar profiles WM-XCT-009; Availability is a derived projection with a pinned manifest and a run identity.
- Time Approval is an identified append-only decision inside the Timesheet aggregate, never a peer root.
- WM-ACT-008 is reference-only, as base and as reference.
- No runtime or model identifier is allocated; `modelId`, `registryId` stay null and `allocationState` stays `unassigned`.
- Worklog is excluded from availability, capacity and residual. Overlaps are retained, flagged, counted once for reporting and never summed into capacity.
- Medical reason is excluded structurally, not by policy.
- Approved slices are immutable; corrections are additive and bidirectionally linked.

The sixteen defects are defects of expression, not of boundary: each remediation in §2 is a stated, mechanical edit to an existing artifact, and §3 supplies the fixtures that close thirteen of them. Applying §2 and §3 is sufficient to freeze the artifacts; nothing in this audit requires a new study, a new source, a new review round or a reconsidered disposition.

Holds carried forward unresolved, and explicitly **not** blocking this freeze: registry allocation for the three candidates; WM-ACT-008's `publishableCanonical: false` and open publication holds; the single-provider waivers on WM-ORG-005 and WM-MAT-008; WM-ORG-016's acknowledged FTE and effort-fraction gap, on which the declared capacity basis depends; WM-XCT-009's precision/uncertainty gap and absent global holiday register; candidate-status registry relations to WM-ORG-016; the absence of any working-time-law, collective-agreement or workforce-measurement source in this dossier, which leaves labour-law limits and measurement-validity claims unverified; and the open question behind defect 10, deferred to registry allocation. Package conversion and live verification remain pending.
