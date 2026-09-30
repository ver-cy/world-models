**Verdict.** Conditional accept: reuse and complete WM-ACT-043 for continuity. The ownership split and claim separations are sound. Do not treat the draft as complete until Backup Policy has an assigned identity and recovery-order, consistency, isolation, fixture, and partial/blocked rules are bound in that draft. Reject any collapse of policy, execution, and restore verification. Reject the synthetic chain as recovered. Reject backup-job success as RTO or RPO proof.

**Strongest evidence.** Backup / Data Protection Policy has an independent owner and lifecycle and applies beyond continuity plans. BIA and ContinuityPlan stay aggregate-owned releases. RestoreTest stays an exercise event. RecoveryEvidence stays a scoped observation. Backup execution and recovery points stay platform observations. Only that split keeps impact tolerance, recovery objective, contractual commitment, and observed outcome from overwriting one another.

**Strongest counterexample.** Chain depending on identity, a database, and an external signer: database backup jobs green; database restore passing at object scope; signer unavailable; recovery point 12 hours old against a 1-hour RPO. Those facts cannot support “chain recovered” or “jobs prove RTO/RPO.”

**Identity / mastership.** BIA and ContinuityPlan are aggregate-owned releases; the aggregate holds mastership and the release is the publication unit. A plan cites a specific BIA release. Backup Policy is independently mastered and is the only identifier-unassigned new-model candidate; a ContinuityPlan must not own it. RestoreTest is an exercise event in the draft family. RecoveryEvidence is a scoped observation, not a master type. Backup execution and recovery points have no business mastership. A versioned recovery-order artifact is release-tied to the ContinuityPlan aggregate. No type codes are assigned here.

Backup Policy and reusable Restore Verification need **two identities**, not one and not profile-of-each-other. One identity would mix policy owner, lifecycle, and extra-plan scope with verification cadence, isolation, fixtures, and chain criteria. Profile-of-each-other fails because verification is not a constrained policy and policy is not a test protocol: a current policy version cannot certify a restore, and a passed test cannot amend policy. Backup Policy is the sole new-model candidate. Reusable Restore Verification is a distinct identity completed inside WM-ACT-043 — a reusable specification instantiated by RestoreTest, with results in RecoveryEvidence. It may be a profile of RestoreTest. It must not be a profile of Backup Policy and must not receive a second minted new-model identity. Profiling either against a generic Policy or VerificationSpec is allowed only if those parents already exist in WM-ACT-043, which this review cannot assert.

**BIA / objectives.** A BIA release masters impact tolerance (MTPD, tolerable loss) for a named aggregate. A ContinuityPlan release masters recovery objectives (RTO, RPO) for that aggregate. Contractual commitment is a third claim class. Observed outcome is a fourth. None overwrites another. Evaluate consistency only on the same aggregate, scope, and BIA/plan release pair: RTO must be ≤ MTPD; RPO must be ≤ tolerable loss; otherwise the plan release is inconsistent. A tighter contractual figure is a commitment gap, not a silent override. Observed duration or recovery-point age never rewrites RTO, RPO, MTPD, or tolerable loss.

**Policy / execution / restore.** Three layers remain distinct. Policy is the independently owned normative artifact. Execution is backup jobs and recovery points as platform observations. Restore verification is the reusable specification instantiated by RestoreTest, with RecoveryEvidence as the scoped result. Green execution is not verification. Object-scope restore is not chain verification. Policy does not own evidence.

**Exercises versus real events.** RestoreTest is a planned exercise event: isolated, scoped, fixture-declared. A real incident recovery is a different event class and must not share identity or outcome with an exercise. Exercise evidence cannot be relabelled incident evidence. Isolation failure invalidates continuity claims from that exercise. Fixture limits cap claimable scope; a stubbed signer is not the external signer.

**Dependencies / order.** The ContinuityPlan release carries a versioned recovery-order artifact and explicit bootstrap dependencies. Every RestoreTest cites that order version. An older order does not evidence the current plan. A node cannot precede a declared bootstrap dependency. Chain order is dependency order, not backup-job order. An unmet bootstrap edge makes chain outcome blocked or partial even if a lower-layer restore passed.

**Evidence / time.** RecoveryEvidence is scoped (object, dependency, or chain) and bound to a named recovery point and time. Unscoped or untimed evidence cannot support a recovered claim. Backup-job green is execution evidence only. Object-scope restore pass is that scope only. A recovery point older than declared RPO is an RPO miss even if jobs are green.

**Scenario.** The synthetic chain depends on identity, a database, and an external signer. Database backups are green — execution observation only. Database restore passes at object scope — not chain recovery and not RTO. The signer is unavailable — required dependency unmet — chain outcome blocked or partial, never recovered. The recovery point is 12 hours old against a 1-hour RPO — observed lag misses RPO; RTO is not inferred. Reject “the chain is recovered.” Reject “backup jobs prove RTO/RPO.”

**Invariants.**
1. BIA and ContinuityPlan exist only as aggregate-owned releases; a plan cites a specific BIA release.
2. BackupPolicy is not owned by a ContinuityPlan.
3. Policy ≠ backup execution ≠ restore verification.
4. Impact tolerance ≠ recovery objective ≠ contractual commitment ≠ observed outcome.
5. RTO ≤ MTPD and RPO ≤ tolerable loss on the same aggregate and release pair; else the plan release is inconsistent.
6. RestoreTest is an exercise event, not a production recovery event; exercise evidence cannot be relabelled incident evidence.
7. RecoveryEvidence scope is explicit; a broader claim than that scope is invalid.
8. The RestoreTest cites a recovery-order version; bootstrap dependencies are explicit; a node cannot precede a declared bootstrap dependency.
9. Fixture use is declared; fixture limits cap claimable scope.
10. Outcomes include pass, partial, and blocked; an unmet required dependency forbids chain-recovered.
11. Platform backup and recovery-point observations cannot be promoted to RTO/RPO proof.
12. Test isolation failure invalidates continuity claims from that exercise.
13. Object-scope restore pass does not entail chain-scope recovery.
14. A recovery point older than declared RPO is an RPO miss even if jobs are green.

**Minimum model set.** BusinessImpactAnalysis (release); ContinuityPlan (release); BackupPolicy (new, identifier unassigned); versioned recovery-order artifact; reusable Restore Verification specification (completed inside WM-ACT-043, not a second new mint); RestoreTest event; RecoveryEvidence; platform backup-execution observation; platform recovery-point observation; bootstrap/dependency relation. No type codes.

**Blockers.** BackupPolicy identity is unassigned; reuse cannot complete without mastership and identifier assignment. Recovery-order artifact is required but untyped in the proposal fragment. Restore Verification specification mastership is unspecified and must not inherit BackupPolicy or ContinuityPlan ownership. RTO/MTPD and RPO/tolerable-loss consistency are not enforceable release predicates. Partial/blocked vocabulary and evidence-scope binding are not first-class, so chain claims stay ambiguous. Collapsing execution observations into evidence identity would let platform jobs be read as objective proof.
