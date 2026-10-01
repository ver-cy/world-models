Harper’s draft is 988 words. Cutting ~90 words and submitting. The team lock stands.  
**Verdict.** Conditionally accept. Allocate no identifier. Not publication-ready. Create identifier-unassigned roots: Learning Program, Enrollment, Career Path, Succession Plan, and — override — Learning Result. Narrow WM-ACT-038 to scheduled delivery/cohort. Profile Development Plan on WM-ACT-008; readiness on WM-ACT-034; nomination and appointment on WM-REC-010 as distinct decisions. Keep assignment in WM-ORG-016, qualification award on WM-PER-008, credential on WM-XCT-017. Do not profile Learning Result on WM-PER-008. Enrollment survives delivery cancellation as historical participation, not an active seat.

**Strongest evidence.** One Program Version can address two development objectives; one Delivery pins that version; one Enrollment yields two Learning Results, each pinning objective, version, and assessment basis. The same split then carries attendance-with-fail, a succession revision that leaves WM-ORG-016 untouched, and a later appointment that still requires WM-REC-010.

**Strongest counterexample.** Profiling Learning Result on WM-PER-008 and treating Enrollment as a delivery child. “Attended, failed, then delivery cancelled” must retain Enrollment, Attendance, Assessment Result, and an unsuccessful Learning Result, and must write neither qualification nor credential. A PER-008 profile either drops the fail or corrupts the award register. A delivery-child enrollment vanishes with cancellation and removes the participation anchor.

**Identity/mastership.** Learning Program + owned Version: catalog. WM-ACT-038 Delivery: schedule. Enrollment and Learning Result: learning-record steward. WM-PER-008: HR qualification register. WM-XCT-017: issuer. WM-ACT-008 Development Plan: people-development. Career Path: org path catalog. Succession Plan: talent slate. WM-ACT-034 readiness/assessment: assessment steward. WM-REC-010: decision steward. WM-ORG-004: structure. WM-ORG-016: assignment. Stewards and identities must not be shared.

**Definition/delivery.** Learning Program is the reusable definition. Version is owned composition, not a peer root: immutable snapshot of objectives, structure, assessment design. Delivery implements exactly one Version; many Deliveries per Version. Cancelling a Delivery does not version or delete the Program. Publishing a new Version does not rewrite existing Deliveries or Results. Course-versus-curriculum grain is a spec gap; do not invent a Course root.

**Enrollment.** Independent unassigned root, not a child of Delivery and not WM-ORG-016. Required Person + Delivery. Survives cancellation with status cancelled/superseded; not an active seat. Distinct from attendance, completion, assignment, and plan lines. Waitlist/transfer are spec gaps.

**Result/qualification/credential.** Keep separate: Assessment Result (WM-ACT-034 output); Learning Result (unassigned root: Person + objective/version + assessment basis + achieved|not-achieved); competency assertion (gap; not a root); qualification award (WM-PER-008, optional, downstream); credential (WM-XCT-017, optional artifact). Fail writes Assessment Result + unsuccessful Learning Result only. Retakes append; history is not overwritten.

**Development plan.** Accept WM-ACT-008 profile. Scheduled revisable program toward named objectives. Not a decision, path, slate, assignment, or aspiration. May reference many objectives and many Programs. Revision does not appoint or reassign.

**Career path.** Accept unassigned root. Reusable position-class structure with recommended programs/objectives. Advisory unless an explicit gate is attached. Person does not own the path. Aspiration toward a path or position-class is a relation/spec gap, not a new identifier.

**Succession/readiness.** Accept unassigned Succession Plan root: versioned slate for a Position/class. Slate membership ≠ incumbency. Revision shall not mutate WM-ORG-016. Readiness is a WM-ACT-034 evaluation against a pinned position/path-step profile and basis. Ready-now is not a seat and not access.

**Appointment/access.** Nomination ≠ appointment; both WM-REC-010. Slate ≠ nomination ≠ appointment. Appointment is required even if the person is already slated. Appointment authorizes assignment; it does not embed WM-ORG-016 facts. Access entitlement is out of band.

**Privacy/retention.** Cancel ≠ erase. Enrollment, attendance, assessment evidence, unsuccessful Learning Results, readiness, nominations, and slates have clocks independent of catalog and delivery status. Do not copy assessment payload onto PER-008 or onto assignment. Awarded qualifications may outlive evidence. Ready-now must not leak as access.

**Scenario.**
1. Program P v1 addresses O1 and O2. Delivery D pins v1. Development Plan references P for both objectives.
2. Person X enrolls E on D, attends, fails assessment A. Attendance yes; completion optional; Assessment Result = fail; LR1/LR2 = not-achieved for O1/O2 + v1 + A; no PER-008; no XCT-017. If D cancels, E survives.
3. Succession Plan SPv2 supersedes SPv1 for Position Pos; incumbent Y keeps assignment A0.
4. Later WM-REC-010 appointment names X to Pos; then WM-ORG-016 assignment A1 starts and A0 ends if replacement. No access from readiness or slate.

**Invariants.**
I1 Delivery pins exactly one Program Version; Version is owned by Learning Program.
I2 Delivery is not the definition; cancel does not delete Program or Enrollment.
I3 Enrollment is an independent root; cancel ≠ erase; cancelled enrollment is not an active seat.
I4 Attendance ⇏ completion ⇏ passed assessment.
I5 A Learning Result pins exactly one objective/version and an assessment basis.
I6 One Enrollment/Delivery may produce many Learning Results.
I7 Failed assessment shall not create PER-008 award or XCT-017 credential.
I8 Qualification and credential are downstream of Learning Result, never substitutes.
I9 Retake appends new Assessment Result and Learning Result.
I10 A plan is not a personnel decision.
I11 Development Plan may reference many objectives and many Programs.
I12 Career Path is reusable definition, not a person-owned plan; aspiration is neither.
I13 Succession revision shall not mutate WM-ORG-016; slate ≠ incumbency.
I14 Readiness is time-stamped evaluation, not assignment and not access.
I15 Nomination ≠ appointment; appointment requires explicit WM-REC-010 even if slated.
I16 Appointment does not store assignment facts; assignment remains WM-ORG-016; none of plan/readiness/slate/enrollment confer access.

**Minimum model set.** Unassigned roots: Learning Program (owns Version), Enrollment, Learning Result, Career Path, Succession Plan. Narrowed: WM-ACT-038 Delivery. Profiles: Development Plan on WM-ACT-008; Readiness on WM-ACT-034; Nomination and Appointment on WM-REC-010. Unchanged: WM-PER-008, WM-XCT-017, WM-ORG-004, WM-ORG-016, WM-ACT-034 Assessment Result. Non-roots: Aspiration, Attendance, Completion, Competency assertion, PathStep, SlateEntry.

**Blockers.** B1 Learning Result as PER-008-only profile. B2 Enrollment as delivery child. B3 WM-ACT-038 not narrowed. B4 Aspiration unspecified. B5 Appointment→assignment handoff (create vs authorize vs record). B6 Readiness target profile/version pin. B7 Path-step advisory vs gated. B8 Program-composes-Program grain. B9 Competency assertion home. B10 Retention clocks for fail evidence vs awards. B11 Enrollment waitlist/transfer.

Relation/spec gaps (list only): Delivery→Version; Version→Objective+; Enrollment→Person+Delivery; Learning Result→Person+ObjectiveVersion+AssessmentBasis; Award→Learning Result*; Credential→Award|Learning Result; Plan→Objective+; PathStep→Position-class; SlateEntry→Person+Readiness; Appointment→Person+Position authorizes ORG-016; Aspiration→Path|Position-class. Rejected collapses: Career Path or Succession Plan onto WM-ACT-008; Learning Result onto PER-008; readiness as assignment/access/appointment; slate as nomination/appointment; enrollment as WM-ORG-016.
