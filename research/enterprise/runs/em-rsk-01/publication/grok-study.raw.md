# Grok independent study — EM-RSK-01

## Verdict
Conditional accept. Reuse WM-KNW-015 as the persistent Risk / Opportunity identity. Restrict WM-XCT-027 to a host-scoped Risk Assessment Context. Keep one identifier-unassigned Control candidate owning definition, implementation state and lifecycle. Reference evidence, appetite and acceptance. Control Assessment cannot safely profile WM-ACT-034 until a written crosswalk is closed. EM-RSK-02 is Audit, Review and Finding, not treatment; EM-RSK-01 may reference treatment and execution outcomes but must not absorb a treatment workflow. No identifier is allocated and no canonical completeness is claimed.

## Identity and mastership
WM-KNW-015 masters risk identity, articulation, valence, classification pin, owner and lifecycle. Assessment revisions and comparability pins live on the host embedding WM-XCT-027; any current estimates on WM-KNW-015 are a current-view projection. WM-XCT-027 binds one assessment context to a risk revision, cited controls and effectiveness determinations, and compares residual position with referenced appetite or tolerance. It does not own risk, control register, effectiveness evidence or treatment workflow. Control remains identifier-unassigned and independently owns definition, implementation state and lifecycle. Implementation state is not effectiveness.

## Assessment and comparability
An assessment is time-bounded and distinct from risk identity. It pins scope, exclusions, horizon, as-of time, recorded time, valid-until time, criteria version, method version, technique version, expression mode and scale. Contexts are comparable only when pins match or a declared conversion records trace and caveats. Missing scale, method, criteria, scope or horizon makes records incomparable. Inherent and residual are distinct findings. Residual cites controls, current effectiveness, changed dimension and explanation.

## Control design, execution and effectiveness
Four layers remain separate: Control master; Control Execution occurrence; time-bounded effectiveness determination; referenced policy or requirement. A failed execution does not rewrite the control definition. Effectiveness needs method, sample, evidence chain, confidence, validity window and invalidation triggers. Control existence, implementation or green policy status never proves effectiveness or closes risk. WM-XCT-027 may cite these facts but cannot author a shadow control register.

## Residual risk and treatment
Residual risk requires a pinned assessment context, cited controls, cited current effectiveness and appetite comparison. Appetite is referenced, not set. Acceptance is a referenced decision and is not a close-the-risk verb. EM-RSK-02 is an assurance contour and cannot be treated as the treatment master. WM-KNW-015 may carry a response option and treatment-plan reference, but treatment execution has no published master in this contour. Do not invent one.

## Shared cause
Shared cause is a referenced source or event, not a shared identity or assessment. One control linked to three risks is coverage topology. Common cause does not imply common residual, horizon or evidence chain.

## Invariants
1. An assessment contains scale and horizon; a score without both is not an assessment.
2. Control existence, implementation state or policy status never proves effectiveness or closes risk.
3. Design, implementation, operation and tested effectiveness are distinct assertions.
4. Residual risk without cited controls, cited effectiveness, changed dimension and comparison or acceptance reference is incomplete.
5. Estimates compare only with matching or explicitly convertible scale, method, criteria, scope and horizon.
6. One control to many risks is linkage, not shared identity or assessment.
7. Failed execution changes only assessments whose population, period, mechanism and evidence chain match.
8. Test completion is not residual-risk closure; conclusions expire and have invalidation triggers.
9. Evidence, appetite and acceptance are referenced, not owned.
10. Treatment execution is not owned here; EM-RSK-02 is not that workflow.

## Scenario
Control C is linked to R1, R2 and R3. C fails for population P, period T, mechanism M and evidence E. Only the assessment whose pins match P, T, M and E may change. Other assessments remain unchanged until their matching evidence chain is shown. Green policy status closes none. Shared cause does not rewrite the second risk if its assessment does not cite the failed mechanism and evidence.

## Blockers
- WM-KNW-015 overlaps Assessment Context and treatment-plan semantics; reuse requires an explicit mastership cut.
- Risk Treatment has no published treatment master and EM-RSK-02 is audit, not treatment.
- Control has no assigned identifier and remains unassigned.
- WM-ACT-034 is not an EM-RSK-01 target and WM-ACT-033 already includes control assessment as an engagement type.
- All relevant published models remain reviewable drafts with source, relation and composition holds.
- Candidate types still include Risk Treatment and Control Execution while the proposed boundary strips treatment and keeps execution separate.

## WM-ACT-034 challenge
Not yet safe. WM-ACT-034 is a generic Assessment / Evaluation aggregate with subject, criteria version, method, evidence, criterion outcomes, composite result, conclusion and validity window. That shape is necessary but not sufficient. Design versus operating effectiveness are not first-class, activity and judgment sit on one aggregate, parentage is unratified, and no completed relation contract exists. A completed assessment must not be read as residual-risk closure or implementation state. Gate profiling on a written occupancy crosswalk against WM-ACT-033 and WM-XCT-027; make population, period, mechanism and evidence chain mandatory and preserve the design-versus-operation split. If the generic aggregate cannot do so without overload, keep testing as an activity that emits a cited effectiveness conclusion. Do not invent a replacement identifier.
