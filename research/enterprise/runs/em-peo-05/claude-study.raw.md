# EM-PEO-05 — Learning, Development and Succession

## Verdict
Reuse five bases, narrow one, profile three, propose three identifier-unassigned roots, reject one candidate as a root. No identifiers allocated.

- **LearningProgram** — new root (unassigned). Reusable definition/programme/version is explicitly external to WM-ACT-038 and to WM-PER-008; no allocated model owns it.
- **Enrollment** — new root (unassigned), independent, not aggregate-owned.
- **LearningResult** — rejected as a root. Profile WM-PER-008 (`bind-assessed-learning-outcomes` → outcome achievement assertion).
- **DevelopmentPlan** — profile WM-ACT-008, with mandatory subject, purpose and disclosure additions.
- **CareerPath** — new root (unassigned) for the reusable path/ladder definition; aspiration is a worker-declared assertion carried on the DevelopmentPlan profile.
- **SuccessionPlan** — new root (unassigned); readiness profiles WM-ACT-034, nomination and appointment are WM-REC-010, assignment stays WM-ORG-016.

## Evidence
WM-ACT-038 `out_of_scope` places programme, course/activity definition, competency, enrollment, attendance, assessment, submission, result, qualification and credential in external masters, and its policies forbid inferring qualification from completion or mastery from one score. WM-PER-008 separates participation, component completion, assessed achievement, qualification definition, personal award, credential and recognition as non-equivalent lifecycle objects. WM-ACT-034 owns criteria binding, decision rule, criterion outcomes and finalisation. WM-ACT-008 carries intent mode, planned actions, baselines and many-to-many realization. WM-REC-010 owns authority, reasons, validity and supersession. WM-ORG-004 excludes career-path and job-family structures by name, leaving them to a sibling; WM-ORG-016 owns time-bounded occupancy.

## Identity/mastership
Distinct identities: learning definition/programme; definition version; delivery/cohort; session; enrollment; attendance assertion; assessment administration; assessment result; delivery completion assertion; learning result (outcome achievement); competency assertion; qualification definition; personal award; credential; development plan; development objective; career-path definition; aspiration; succession plan; pool membership/nomination; readiness assessment; appointment decision; assignment.

Mastership: curriculum steward → definitions; provider → delivery; registrar → enrollment and admission; assessor → results; awarding body → awards; issuer → credentials; worker plus manager → development plan (worker owns aspiration); talent-governance authority → succession plan and readiness; appointing authority → WM-REC-010; organization → WM-ORG-016. LMS is never the qualification, competency or assignment master.

## Learning definition/delivery
WM-ACT-038 does **not** currently own definition and must not; its scope already binds exact external revisions. It must be narrowed on two edges: (a) it may hold delivery-scoped participation and role *assertions* but not enrollment identity, admission authority or enrollment lifecycle; (b) its `parent_ids: WM-PER-008` is rejected — a delivery is not a child of a person-centred learner record. Replace with REFERENCE in both directions. Accept subject entry kind `aggregate` (registry `standalone-mm` is record-plane). Repeat deliveries create new roots; released rosters, events and grades stay immutable.

## Enrollment/participation
Enrollment is an independent root, not aggregate-owned. It has admission authority, eligibility and prerequisite decisions, capacity/waitlist position, transfer, withdrawal, learner rights and survives cancellation, postponement or replacement of the delivery; programme-level enrollment can exist before any delivery is scheduled. WM-ACT-038 holds a source-qualified participation binding referencing it. Attendance remains a separate assertion in WM-ACT-038 and is never inferred from access or login.

## Result/qualification/credential
Six non-collapsible assertions: attendance (WM-ACT-038); assessment result (WM-ACT-034); delivery completion/disposition (WM-ACT-038); **learning result** = outcome achievement assertion (WM-PER-008 profile) pinning the learning-objective identifier *and version*, the criteria version, scale version and assessment-result reference; competency assertion (WM-PER-009 concept + the Person Capability Assertion candidate from EM-PEO-03); qualification award (WM-PER-008) and credential (WM-XCT-017). Completion never becomes a learning result; a learning result never becomes an award; an award never becomes a credential; credential validity is never current competence.

## Development plan
DevelopmentPlan profiles WM-ACT-008. Mapping: plan identity and versioning → plan identity/supersession; intent mode fixed to a non-authorizing value; development objectives → goals and success criteria; activities → planned actions; target dates → temporal binding; approved version → baseline; progress and completion → progress/variance; enrollment, delivery, learning result and credential references → realization links (many-to-many, so one course serves several objectives). Required additions: subject person reference, purpose, lawful basis, disclosure class, and the rule that no plan element confers authority, entitlement, promotion or pay. Commitment structure may be used only where a genuine beneficiary obligation exists.

## Career path
Reusable CareerPath is a versioned definition: ordered or graph-structured stages referencing job families, WM-ORG-004 positions or grade levels, with typical progression criteria, competency expectations by stage and permitted lateral moves. It is organization-mastered, exists with no incumbent, and is a reference structure, not a promise. Aspiration is a worker-declared, time-stamped assertion citing a path or stage, carried on the DevelopmentPlan profile; it is never a management plan and never a nomination.

## Succession/readiness
SuccessionPlan is a root: scope (critical positions or role classes), review cycle, coverage state, pool membership, per-candidate readiness assertion, bench depth and risk notes. Readiness profiles WM-ACT-034 with pinned criteria, method, evidence, scale version, assessor competence and impartiality, and a validity window. Nomination is a WM-REC-010 record. Plan revision creates a successor version; it never mutates prior readiness assertions and never touches WM-ORG-016. Its review schedule may reference WM-ACT-008; its payload is not a plan of intended actions.

## Decision/appointment/access
Appointment requires an explicit WM-REC-010 decision (author, authority, competence, reasons, dissent, validity, challenge route), then a WM-ORG-016 assignment, then — and only then — derived access and authority. Readiness status, pool membership and nomination confer nothing. Access provisioning and de-provisioning derive from assignment state, never from a readiness label or a plan.

## Privacy/retention
Potential and readiness ratings are deny-by-default, purpose-bound, minimum-disclosure fields: visible to the named talent-governance role, the deciding authority and the subject, not to the subject's peers, not in directories, not in projections. Each rating records purpose, lawful basis, review interval after which it is stale or void, and a challenge/correction route producing an attributable successor rather than an overwrite. Retention triggers are class-specific (enrollment closure, result finality, award, credential status, plan closure, rating expiry, decision plus challenge window). Legal hold suspends disposition; disposition never cascades to person, position, employment or assignment masters.

## Acceptance scenario
One course definition version, one delivery, one enrollment, one completion assertion, one learning result; two development objectives both reference that single result — no duplicate result. A second learner attends fully (attendance satisfied) and fails assessment: assessment result fail, no completion, no learning result, no competency assertion, no award; attendance stands unchanged. Succession plan v3 supersedes v2 with changed readiness and pool; all WM-ORG-016 assignments are byte-identical. Six months later the appointment happens only via a WM-REC-010 decision plus a new assignment; access follows the assignment.

## Invariants
1. A plan is not a personnel decision. 2. Readiness is not appointment. 3. Readiness is not access. 4. Definition ≠ delivery ≠ enrollment. 5. Enrollment identity is external to any delivery. 6. Attendance is not learning. 7. Completion is not qualification. 8. A learning result pins objective version and assessment basis. 9. One score is not mastery. 10. Aspiration is not nomination. 11. Career path is not entitlement. 12. Plan revision leaves assignments unchanged. 13. Ratings expire and are contestable. 14. Finalized results and released delivery history are immutable; change is by successor.

## Holds
No approved relation rows exist for WM-ACT-038, WM-PER-008, WM-XCT-017 or WM-PER-009; every relation above is a proposal. WM-ACT-038, WM-PER-008 and WM-XCT-017 are single-provider Codex waivers; WM-ACT-034 is Claude-only. WM-ACT-034 carries access-dimension and retention holds that must close before it carries readiness ratings. WM-PER-009 has no specification and a flagged conflation of human capability with system function. LearningProgram, Enrollment, CareerPath, SuccessionPlan and the Person Capability Assertion candidate lack allocations and independent evidence. Source pins, crosswalks and fixtures are unverified. No canonical completeness, installability or publication readiness is claimed.
