# Single frozen semantic audit — EM-TEC-10

You are the sole independent frozen auditor. No tools, browsing, standards claims, identifier invention or registry mutation. This audit runs exactly once and will not be repeated.

Audit the reconciled proposal and artifacts below. Fixed identity decision: Operational Change profiles request-side WM-ACT-032; Change Window, Freeze Period and Rollback Plan profile WM-ACT-008; Escalation Rule profiles WM-KNW-012/013; Change Execution and Duty Roster each have independent identity but remain registry-unassigned. Request, authorization, execution, release, deployment, rollback intent, plan, execution, verified state, standing assignment, roster shift and IAM grant remain distinct.

Find material internal contradictions, missing fields, unenforceable invariants, lifecycle/version/provenance/time defects, unsafe authority or IAM implications, rollback/handover gaps and boundary leaks. Known registry/base publication gaps are holds, not artifact defects. Return:
1. Verdict ACCEPT or REVISE.
2. Numbered material defects with exact evidence.
3. Required bounded fixes.
4. One JSON fenced array of additional fixtures with target, id, kind, input, expect and optional expectedCode, covering every defect. Targets must be ChangeExecution, DutyRoster, or EM-TEC-10-profile.
5. Explicit identifier decision.
6. Freeze decision: closed, no rerun.


## local-evidence.md
# EM-TEC-10 local synthesis

## Disposition

- Profile WM-ACT-032 as **Operational Change** for proposal, assessment, disposition and closure references. Request and execution remain separate.
- Profile WM-ACT-008 as **Change Window / Freeze Period** and **Rollback Plan**.
- Propose identifier-unassigned **Change Execution** and **Duty Roster** roots because both have independent occurrence identity and lifecycle.
- Profile WM-KNW-012/013 as **Escalation Rule** and its condition.
- Reuse WM-SFT-008 for release, WM-SFT-009 for software deployment, WM-ORG-016 for standing work assignment, WM-ACT-006 for execution tasks and the decision triad for authorization.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Change Request owns the proposal, requested delta, proposed window, rollback intent, assessment and disposition references. Decision rationale, approval act and issued instrument stay in WM-KNW-010, WM-ACT-024 and WM-REC-010. Change Execution owns what actually occurred against one approved request revision.

Change Window is a reusable schedule entry that may exist without a particular change and may govern many executions. Duty Roster owns shift occurrences and handovers; WM-ORG-016 owns standing eligibility/assignment. IAM grants remain external and never derive automatically from the roster.

## Request, authorization and execution

Request, decision and execution are separate records. Authorization freezes an approved proposal revision plus conditions and effectivity. An execution pins that revision and never edits it. Emergency change records the content relaxed, authority, reason and required retrospective completion.

One approved revision may have multiple executions. A release becomes obtainable in WM-SFT-008 but changes no runtime state until deployment or another execution occurs. WM-SFT-009 is the software-deployment specialization; Change Execution also supports non-software operational changes.

## Windows and rollback

Change Window has identity, recurrence, exclusions, overrides, disclosure class, timezone identifier, tzdb release and version. Freeze Period uses the same schedule profile plus a prohibitive rule. A window is permission to disturb within an envelope, never authorization to execute.

Rollback intent in WM-ACT-032, versioned Rollback Plan in WM-ACT-008, rollback execution in Change Execution and verified restored state are four different facts. Partial rollout records per-target outcome. `rolled back` never implies `restored` without verification evidence.

## Duty roster and escalation

Person, role, standing assignment, roster shift and IAM grant remain distinct. A shift references an eligible assignment and states service/scope, start/end, timezone and roster revision. Substitution and override create linked records with authorizer and effective instant.

Handover records outgoing/incoming parties, instant, open incidents and in-flight changes, plus incoming acknowledgment. Missing acknowledgment is a gap. Escalation Rule references a condition, resolves the target through the roster as-of event time and states timeout/repetition; it cites authority but confers none.

Any privileged access for on-call work is a separate time-bounded authorized and audited grant with expiry. Roster membership alone provides no permission.

## Acceptance result

Change C is authorized against revision R1 and binds EU and US windows with distinct zones. Execution E1 in the EU window partially fails. Pinned rollback plan P1 triggers execution E2, and verification V1 proves restored state. During E2, duty passes from A to B with explicit acknowledgment. Authorization remains attached to R1; the unused US window remains bound. The chain R1→E1→P1→E2→V1 is preserved, and B gains no administrative rights from the roster or handover.

## Required invariants

1. A window is never authorization.
2. Execution pins an approved request revision.
3. Release, deployment and operational change remain distinct.
4. One authorization may govern multiple executions.
5. Rollback intent, plan, execution and verified state remain distinct.
6. Partial rollout records per-target results.
7. Duty roster never grants IAM permission.
8. Roster entries reference standing assignments.
9. Substitution and override are additive and attributable.
10. Handover requires acknowledgment; silence is a gap.
11. Every instant carries offset; recurring schedules also pin zone and tzdb release.
12. Approved revisions, plans, windows, rosters and rules are immutable and superseded explicitly.

## Holds

Change Execution and Duty Roster lack registry allocation. WM-SFT-010 has no complete specification. Reused bases remain non-canonical drafts with source and provider holds. Relation rows for request→execution, execution→window, roster→assignment and escalation evaluation are absent. Workforce conflict-of-interest, timezone, access-grant and verification fixtures are incomplete. No installability or publication-readiness claim is made.


## claude-study.raw.md
# EM-TEC-10 — Operational Change and On-call Duty

## Verdict

| Candidate | Independent identity? | Disposition |
|---|---|---|
| OperationalChange | No — same record as the request through disposition | **Profile** WM-ACT-032 (operational/IT change profile) |
| ChangeWindow | **Yes** — exists without any change, shared and recurring | **Profile** WM-ACT-008 (window and freeze-period profile) |
| ChangeExecution | **Yes** — occurrence, repeatable per approved revision | **New**, identifier unassigned |
| RollbackPlan | Yes, as a versioned plan; **no** as a separate model | **Profile** WM-ACT-008; rollback *execution* is a ChangeExecution occurrence |
| DutyRoster | **Yes** — declared gap in the dossier | **New**, identifier unassigned |
| EscalationRule | No | **Profile** WM-KNW-012 (rule slot; condition in WM-KNW-013) |

No identifiers are allocated.

## Evidence

WM-ACT-032 owns the request-side view only and explicitly excludes work orders, releases, deployments and rollback execution; it records a *proposed* window, backout *intent* and test *intent*, and lists change freezes and blackout calendars as a known omission delegated to "the executing model's change schedule". That executing model does not exist in the dossier. WM-SFT-009 is software-scoped (release→runtime environment) and excludes non-software change. WM-ORG-016 excludes "concrete shift instances, time capture, timesheets and attendance actuals" and composes with a "Schedule, roster and availability model" that is likewise absent. Two structural gaps are therefore evidenced, not assumed.

## Identity/mastership

- Change request and disposition: WM-ACT-032; decision rationale WM-KNW-010, approval act WM-ACT-024, authoritative record WM-REC-010.
- Window and freeze calendar: WM-ACT-008 (recurrence, working calendars, IANA tz identifier plus database release, floating-time preservation).
- Release: WM-SFT-008; deployment occurrence: WM-SFT-009; runtime target: WM-SFT-010.
- Standing eligibility and authority: WM-ORG-016; person and role master data remain external.
- Rosters and shift instances: new DutyRoster candidate.
- Escalation rule: WM-KNW-012; alerts and events stay in observability and are referenced only.
- Assignable work steps: WM-ACT-006.

## Request/decision/change

Request, decision and execution are three records. WM-ACT-032 carries the outcome value plus a version-pinned WM-KNW-010 reference; the deciding act is WM-ACT-024; the authoritative instrument is WM-REC-010. Approval freezes an *approved revision* (proposal statement serial + conditions + effectivity). Execution never edits that revision; it cites it. Emergency change relaxes mandatory submission content, never the record of what was relaxed, by whose authority and by when it must be completed (WM-ACT-032 policy); retrospective authorisation is a new decision bound to the same request, not an edit.

## Window/schedule

A ChangeWindow is a WM-ACT-008 schedule entry with its own identity, recurrence rule, exclusions and overrides, disclosure class and version counter. A freeze period is the same profile with a prohibitive character, paired with a WM-KNW-012 rule so the prohibition is normative and derogable (registered derogation with granting authority, bounded validity, compensating obligation). A window is a *permission-to-disturb envelope*, never an authorization: authorization is the WM-ACT-024/WM-REC-010 pair. Overlapping windows are retained and intersected on absolute instants; a change binding two windows holds two pinned window references, each with its own tz identifier.

**Release without immediate change**: WM-SFT-008 stops where a release becomes obtainable. A published artifact with no deployment to a governed target changes no runtime state, so no operational change is required. An inert or feature-flagged deployment, or a pre-authorised standard change model with a bound authority, likewise needs no fresh normal change — but still produces a ChangeExecution record.

## Execution/deployment/rollback

ChangeExecution is the missing generic occurrence: identity, declared desired state, window binding, state machine, partial/failed outcome, evidence references. WM-SFT-009 becomes a software specialisation of it; WM-ACT-006 supplies assignable steps. Four things stay separate: rollback **intent** (WM-ACT-032), rollback **plan** (WM-ACT-008, version-pinned, with trigger conditions), rollback **execution** (a ChangeExecution occurrence with kind=rollback and a typed link to the reverted occurrence), and **verified state** (post-change verification evidence referenced from WM-SFT-015, never restated). A partial rollout records per-target outcome; "rolled back" is an execution claim, "restored" is a verification claim, and neither implies the other.

## Duty roster/assignment

Five distinct things: person (external master), role (classifier), WM-ORG-016 assignment (standing, time-bounded eligibility and authority), DutyRoster shift instance (who is on call for which service, from when to when, in which tz), and IAM grant (external, downstream). A roster entry references an assignment; it does not create one. Substitution and override are new entries with substitute, substituted-for, authoriser and effective instant — never edits. Handover is an explicit record: outgoing and incoming parties, instant, open-incident and in-flight-execution references, and an acknowledgment by the incoming party. Absence of acknowledgment is a recorded gap, not an assumed acceptance.

## Escalation/IAM

An EscalationRule is a WM-KNW-012 rule slot: condition reference (WM-KNW-013), target resolved through the roster at the event instant, timeout and repetition, and an authority reference that is *cited*, not conferred. Evaluation and notification transport are external. **Negative case rejected**: roster membership confers no administrative rights. WM-ORG-016 states RBAC user assignment is a downstream projection carrying no temporal bound, and that SSD-safe occupancy can still yield over-privilege. Any elevation during duty is a separate, time-boxed, individually authorised and audited grant with mandatory expiry and post-hoc review.

## Time/version/handover

Every instant is RFC 3339 with seconds and explicit offset; event, observation and ingestion times are separate fields. Windows and rosters additionally carry the IANA zone identifier and the tzdb release in force, so a rule change invalidates and forces recomputation of stored future local times. Floating time is preserved, never coerced. DST gaps and overlaps require a declared resolution policy per window. Approved revisions, plans, rosters and rules are versioned and superseded, never overwritten; execution pins the version it acted on.

## Acceptance scenario

Change C is approved once against revision R1, with windows W-EU and W-US (distinct zones, one crossing a DST transition). Execution E1 runs in W-EU and fails partially. Rollback plan P1 (pinned) triggers; execution E2 (kind=rollback, links E1) runs, and verification V1 evidences restored state. During E2 the roster hands over from A to B with acknowledgment. C's authorization is unchanged — no re-approval, because authority attaches to R1, not to a window or an operator. W-US remains bound and unexecuted. Evidence chain R1→E1→P1→E2→V1 is intact; B acquires no administrative rights from the handover.

## Invariants

1. A window is not an authorization.
2. Execution references an approved revision.
3. Duty does not extend IAM automatically.
4. Rollback intent, plan, execution and verified state are four separate records.
5. One approved revision may have many executions; occurrence ≠ approval.
6. Freeze prohibitions are derogable only by recorded, bounded derogation.
7. Every instant carries offset, zone identifier and tzdb release.
8. Handover requires acknowledgment; silence is a gap, not consent.
9. Release ≠ deployment ≠ change.
10. Partial rollout records per-target outcome; no aggregate success is inferred.
11. Substitutions and overrides are additive and linked.
12. Names, dates and window labels are never identifiers.

## Minimal model set

Reuse: WM-ACT-032, WM-ACT-008, WM-ORG-016, WM-SFT-008, WM-SFT-009, WM-ACT-006, WM-KNW-012/013, WM-ACT-024, WM-KNW-010, WM-REC-010. Profile: OperationalChange, ChangeWindow/FreezePeriod, RollbackPlan, EscalationRule. New, unallocated: ChangeExecution, DutyRoster.

## Holds

The executing change-schedule and roster models both referenced by adjacent drafts do not exist; WM-SFT-010 has no specification; WM-ACT-032, WM-SFT-008, WM-SFT-009, WM-KNW-012 and WM-KNW-010 carry single-provider waivers and unverified source pins; relation rows for change→execution, execution→window and roster→assignment are absent; WM-ORG-016 declares conflict-of-interest and workforce-measurement gaps that bear on rosters. Fixtures for two-window, failed-rollout and handover cases are missing. No canonical completeness, installability or publication readiness is claimed.


## grok-study.raw.md
Verdict: Conditional accept. Change Execution and Duty Roster both need independent identity. Profiling is valid only as association, not as subtype collapse. Identifier-unassigned roots stay unassigned. No publication readiness is claimed.

Strongest evidence: The adjacent drafts already split the objects this proposal must not merge. WM-ACT-032 owns the request, WM-ACT-008 owns time-bound plan and revision, the decision triad owns authorization, WM-ACT-006 owns task, WM-ORG-016 owns standing assignment, WM-SFT-008 owns release, WM-SFT-009 owns deployment, and WM-KNW-012/013 own rules. The proposal extends that split instead of building a parallel change stack.

Strongest counterexample: One change is authorized once, revision R approved against plan version P1, with a separate EU window and a US freeze. Execution starts in the EU window, records a partial failure, rolls back under plan version P0, and a verified restored state is observed. Mid-span, the EU on-call shift hands over to the US shift. A single WM-ACT-008 cannot be window, freeze, authorization, rollback plan, rollback execution, and verified state. A WM-ORG-016 assignment cannot be the shift, the acknowledgment, and an IAM grant. Without separate execution and roster identities, evidence, revision, and rights become ambiguous.

Identity/mastership: Operational Change, on the request side only, is a profile of WM-ACT-032. Authorization mastership stays with the decision triad. Change Execution is a new root: it masters start, partial failure, abort, evidence, and completion. Duty Roster is a new root: it masters the time-bounded shift and handover acknowledgment. WM-ACT-008 masters plan revision and window intervals, not execution or rights. WM-ORG-016 masters standing assignment, not the shift. No schedule or assignment masters the others.

Request/decision/change: Request, authorization, and execution are three identities. The request states intent and cites a candidate revision. The decision authorizes or refuses that revision and may cite windows as constraints. Execution records what ran. Closing or failing execution does not rewrite the request or the decision. A task (WM-ACT-006) may be raised by execution; it is not the change.

Window/schedule: Change Window and Freeze Period are interval profiles on WM-ACT-008. A window constrains when execution may start; it does not authorize. Authorization cites the window. EU and US windows are separate interval instances, each pinned to timezone and tzdb release, not one local-time field. Freeze is a prohibition interval, not a denied decision.

Execution/deployment/rollback: Rollback intent sits on the request or decision. Rollback plan version sits on the WM-ACT-008 profile. Rollback execution and verified restored state sit on Change Execution, with evidence attached there, not overwritten into the plan. Release (WM-SFT-008) is not a deployment and not a change. Deployment (WM-SFT-009) may be caused by execution; it is not the change and not the window. Partial failure is an execution state; it does not auto-close the request.

Duty roster/assignment: Standing assignment (WM-ORG-016), roster shift, and IAM grant are three objects. The roster is the shift instance: who is on call, in which window, under which timezone. Handover is an explicit acknowledgment between shifts, not inferred from shift end. Roster membership never confers, implies, or auto-provisions administrative or change-execution rights.

Escalation/IAM: Escalation Rule is a profile of WM-KNW-012/013. It may name a roster role or shift as the notify target. It must not mint an IAM grant. Any right is a separate authorized object with its own decision. Escalation does not authorize the change and does not start execution.

Time/version/handover: Every window and shift pins timezone and tzdb release. Execution cites the approved request revision and the plan version that ran. A later plan version does not rewrite the version cited by a completed or failed execution. Handover requires acknowledgment before the receiving shift may act under that change. Unacknowledged shift end is not a handover.

Scenario: Change C is requested, decision D approves revision R against plan P1, citing EU window W-EU (open) and US freeze W-US. Execution E1 starts in W-EU, partial-fails, and evidence is attached to E1. Rollback execution E2 runs plan P0; verified restored state is recorded on E2, not on P1. Roster shift S-EU hands over to S-US; acknowledgment is stored on the roster, and S-US receives no IAM grant from membership. Escalation names S-US; a separate decision would be required for any right.

Invariants:
1. Request identity ≠ authorization decision identity ≠ execution identity.
2. Release identity ≠ deployment identity ≠ change identity.
3. Window and freeze do not authorize; authorization cites them.
4. Rollback intent ≠ plan revision ≠ rollback execution ≠ verified restored state.
5. Standing assignment ≠ roster shift ≠ IAM grant.
6. Roster membership grants no administrative or execution rights.
7. Every timed fact pins timezone and tzdb release.
8. Execution cites approved revision and the plan version that ran.
9. Handover requires explicit acknowledgment, not inferred shift end.
10. Partial failure does not auto-close the request or the decision.
11. Rollback evidence attaches to execution and does not overwrite the plan.
12. EU and US windows are separate interval instances.
13. An escalation rule may name a roster role but must not mint an IAM grant.
14. A later plan version does not rewrite the version cited by a past execution.

Minimum model set: profiled Operational Change on WM-ACT-032; profiled Change Window, Freeze Period, and Rollback Plan version on WM-ACT-008; independent Change Execution; independent Duty Roster; profiled Escalation Rule on WM-KNW-012/013; existing decision triad, WM-ORG-016, WM-SFT-008, WM-SFT-009, and WM-ACT-006 linked by association only.

Blockers: The two new roots have no assigned identifiers and must not be given any here. Rollback must not be fully collapsed onto WM-ACT-008. Window must not be treated as authorization. Roster must not be treated as an IAM source. Until those splits are held as associations with separate mastership, the profile reuse is not safe to implement.


## candidate-allocation-offline-change-execution/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-TEC-10","proposedName":"Change Execution","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"One actual operational-change occurrence remains identifiable independently of its request, authorization, window, release, deployment and rollback evidence.","versionIdentity":"Corrections append successor assertions for the same occurrence; retries, partial continuations and rollback actions receive distinct linked execution identities.","independentLifecycle":["scheduled","started","partially-completed","completed","failed","rollback-started","rolled-back","aborted","closed"],"mastership":"operational change-execution authority"},"boundary":{"owns":["persistent change-execution occurrence identity","approved request-revision pin","authorization and condition references","actual start, end and target scope","per-target actions and outcomes","window and operator references","rollback execution linkage","verification, correction and closure lineage"],"references":[{"target":"WM-ACT-032","purpose":"Operational Change request"},{"target":"WM-ACT-008","purpose":"Change Window and Rollback Plan"},{"target":"WM-SFT-008","purpose":"Release or build"},{"target":"WM-SFT-009","purpose":"Software deployment specialization"},{"target":"WM-ACT-006","purpose":"Execution task"},{"target":"WM-REC-010","purpose":"Issued authorization instrument"}],"excludes":["change request, approval or decision identity","window, freeze period or rollback-plan identity","release, build or deployment identity","task, observation or verification-evidence identity","standing assignment, roster shift or access grant","automatic restored-state assertion"]},"objects":{"ChangeExecution":{"identity":["changeExecutionId"],"required":["approvedRequestRevisionRef","authorityRef","targetScope","startedAt","status"],"optional":["endedAt","windowRef","operatorRefs","perTargetOutcomes","rollbackPlanRef","rollbackExecutionRef","verificationRefs","supersedesRef"],"lifecycle":["scheduled","started","partially-completed","completed","failed","rollback-started","rolled-back","aborted","closed"]}},"invariants":["Every execution pins exactly one approved request revision and its conditions.","Request, authorization and execution retain separate identities.","One authorization may govern multiple executions without rewriting the approved revision.","A window permits disturbance within an envelope but never authorizes execution.","Release availability never changes runtime state without deployment or execution.","Partial rollout records per-target actions and outcomes.","Rollback intent, plan, execution and verified restored state remain distinct.","Rolled back never means restored without verification evidence.","Emergency execution records relaxed controls, authority, reason and retrospective obligations.","Retries and continuations receive distinct linked execution identities.","Corrections append successors and preserve prior assertions.","Execution closure never grants or revokes standing assignment or IAM access."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Request-to-execution, window and verification relation contracts require canonical approval.","WM-SFT-010 and non-software execution crosswalks remain incomplete."]}


## candidate-allocation-offline-change-execution/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Change Execution","cases":[{"id":"partial-failure-rollback","kind":"positive","input":"Execution E1 partially fails, triggers rollback plan P1 and linked execution E2, then verification V1 proves restored state.","expect":"The full R1-E1-P1-E2-V1 chain remains distinct and traceable."},{"id":"multiple-windows","kind":"positive","input":"One approved revision binds EU and US windows but executes only in EU.","expect":"The execution records the EU window while the unused US window remains unchanged."},{"id":"emergency-change","kind":"positive","input":"An emergency execution relaxes one control under named authority.","expect":"The relaxation, reason and retrospective obligation are explicit."},{"id":"window-is-authorization","kind":"negative","input":"Presence of an open window is treated as authorization.","expect":"The inference is rejected."},{"id":"rollback-is-restored","kind":"negative","input":"Rollback completion is treated as verified restoration.","expect":"The claim is rejected without verification evidence."},{"id":"release-is-deployment","kind":"negative","input":"A published release is treated as executed on runtime targets.","expect":"The inference is rejected."}]}


## candidate-allocation-offline-change-execution/profile-candidate.json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-TEC-10","name":"Enterprise Operational Change and Escalation","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ACT-032","WM-ACT-008","WM-KNW-012","WM-KNW-013","WM-SFT-008","WM-SFT-009","WM-ORG-016","WM-ACT-006"],"constraints":["WM-ACT-032 owns the Operational Change request, proposed delta, assessment and disposition references.","WM-ACT-008 profiles Change Window, Freeze Period and Rollback Plan as immutable schedule or plan releases.","WM-KNW-012 and WM-KNW-013 profile Escalation Rule and condition without conferring authority.","Release, deployment, operational execution and verification remain separately mastered.","Window, authorization, rollback intent, rollback plan, rollback execution and restored-state evidence remain distinct.","Roster membership and escalation resolution never grant IAM permission." ]}


## candidate-allocation-offline-change-execution/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## candidate-allocation-offline-duty-roster/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-TEC-10","proposedName":"Duty Roster","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed roster remains identifiable across shift occurrences, substitutions and handovers while its schedule revisions evolve independently of standing assignments and access grants.","versionIdentity":"Changes to shift schedule, coverage scope, recurrence, timezone, eligibility or handover rules create immutable roster revisions; substitution and override append linked records.","independentLifecycle":["draft","published","effective","amended","suspended","superseded","retired"],"mastership":"operations workforce-scheduling authority"},"boundary":{"owns":["persistent duty-roster identity","service and coverage scope","versioned shift schedule","timezone and tzdb-release pins","eligible standing-assignment references","shift occurrences","substitution and override records","handover, acknowledgment and retirement history"],"references":[{"target":"WM-ORG-016","purpose":"Standing work assignment and eligibility"},{"target":"WM-ACT-008","purpose":"Schedule profile"},{"target":"WM-KNW-012","purpose":"Escalation rule"},{"target":"WM-KNW-013","purpose":"Escalation condition"},{"target":"WM-ACT-006","purpose":"On-call work task"}],"excludes":["person, role or standing-assignment identity","IAM grant or administrative permission","incident, escalation or change-execution identity","employment or attendance record","payroll or timesheet authority","automatic acknowledgment or acceptance"]},"objects":{"DutyRoster":{"identity":["dutyRosterId"],"required":["serviceScope","ownerRef","status"],"optional":["successorRef","retiredAt"],"lifecycle":["draft","published","effective","amended","suspended","superseded","retired"]},"RosterRevision":{"identity":["dutyRosterId","revision"],"required":["shifts","timezoneId","tzdbRelease","validFrom","contentDigest"],"optional":["eligibilityRules","handoverRules","validTo","supersedesRevision"]}},"invariants":["Every shift references an eligible standing assignment.","Person, role, assignment, roster shift and IAM grant retain separate identities.","Roster membership never grants physical or logical access.","Every instant carries an offset; recurring schedules pin timezone and tzdb release.","Substitution and override append attributable records with authorizer and effective instant.","Handover records outgoing and incoming parties, instant, open work and incoming acknowledgment.","Missing acknowledgment remains an explicit gap and never becomes acceptance.","Escalation resolves its target through the roster as of event time.","Escalation rule cites authority but confers none.","Privileged on-call access requires a separate time-bounded authorized audited grant.","Roster revisions are immutable and superseded explicitly.","Roster retirement never closes employment, assignment, incidents or in-flight changes."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Timezone, conflict-of-interest, access-grant and handover contracts require canonical approval.","Package conversion and live verification are pending."]}


## candidate-allocation-offline-duty-roster/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Duty Roster","cases":[{"id":"cross-zone-shifts","kind":"positive","input":"EU and US shifts use named timezones and a pinned tzdb release.","expect":"Each occurrence resolves deterministically with offset and revision."},{"id":"acknowledged-handover","kind":"positive","input":"Duty passes from A to B with open incidents, in-flight changes and B's acknowledgment.","expect":"The handover is attributable and preserves unresolved work."},{"id":"authorized-substitution","kind":"positive","input":"C substitutes for B under an authorized override.","expect":"A linked substitution record changes the effective shift without rewriting the roster."},{"id":"roster-grants-admin","kind":"negative","input":"On-call roster membership automatically grants administrator access.","expect":"The permission inference is rejected."},{"id":"silence-is-ack","kind":"negative","input":"No response from the incoming party is treated as handover acknowledgment.","expect":"The acceptance inference is rejected."},{"id":"assignment-is-shift","kind":"negative","input":"A standing work assignment is used as the roster occurrence.","expect":"The identity merge is rejected."}]}


## candidate-allocation-offline-duty-roster/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}
