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
