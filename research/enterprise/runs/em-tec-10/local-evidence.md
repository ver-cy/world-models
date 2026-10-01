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

## Grok reconciliation and frozen audit

Grok conditionally accepted both independent roots and strengthened the request/decision/execution, freeze, rollback, handover and IAM boundaries. The single frozen audit accepted the fixed identity decision, found 21 artifact defects and supplied exact fixtures. All bounded fixes are encoded without allocating identifiers.
