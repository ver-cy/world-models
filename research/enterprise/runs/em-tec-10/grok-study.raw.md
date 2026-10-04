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
