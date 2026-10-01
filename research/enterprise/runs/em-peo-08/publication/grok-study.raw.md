# Grok independent study — EM-PEO-08

## Verdict

Accept with gaps. Identifier-unassigned roots only: GradeScheme, RoleProfile, GradeAssignment. GradeLevel is owned by a SchemeVersion. GradeCalibration is not a root; profile it as given WM-ACT-034 moderation plus WM-REC-010 ratification. Reuse Position, Party Role, Assessment/Evaluation, Education/Qualification, Decision/Approval Record, Employment, Payroll/Compensation, Attestation/Credential. Skill/Competency stays reserved without a specification. Allocate no identifier. This review does not claim publication readiness.

## Strongest evidence

Decision/Approval and Assessment/Evaluation already supply ratification and moderation, so calibration need not be a fourth root. Owned GradeLevel-in-SchemeVersion plus a dated GradeAssignment root is the only shape that keeps historical citations stable, models dual-track standing as two assignments with two WM-REC-010s, and keeps PositionGrade distinct from person standing. The rule that a grade decision mutates only the assignment forces the required separations.

## Strongest counterexample

Merger map of A.v1/L8 “Principal Architect” with no B-axis counterpart, then a later pay change. Equal labels or ordinals must not invent a B-level; the crosswalk WM-REC-010 must not create a B assignment; a later reassessment must not move compensation band, pay decision, payroll fact, PositionGrade, qualification, credential, or access. Any fused grade–pay–position object fails.

## Identity / mastership

Unassigned masters: GradeScheme, RoleProfile, GradeAssignment. Owned, not roots: SchemeVersion, GradeLevel, Track/Axis, directed Crosswalk mapping. PositionGrade is a relation on Position, not a root. Calibration is not a master. GradeLevel is not independently masterable. Equal labels across schemes are not shared identity.

## Scheme / levels

Separate Scheme (ladder family), SchemeVersion (immutable after WM-REC-010 freeze), GradeLevel (owned: code, label, ordinal, track/axis, narrative). Dual-track is one scheme with at least two tracks, not two schemes. Ordinal is local to version and track. Relabel or add levels only via a new version. Historical assignments keep the version they cited. Pre-freeze drafts are not assignment targets.

## Role profile

Unassigned root. Expectation template only: grade range on a named SchemeVersion and track, qualification, credential. Many Positions may cite one profile; a Position need not have one. Must not store assigned grade, pay, access, or incumbent, and must not subtype Position or Party Role. Scope to a SchemeVersion or an explicit carry-forward; no silent retarget. Competency expectations deferred.

## Assignment

Unassigned root. Subject = Employment; Party Role occupancy instance only if Employment is absent. Forbidden: bare Party/Person, Position, Party Role type, RoleProfile, compensation object. Cites exactly one GradeLevel in one SchemeVersion (track if multi-axis). Time-bounded, superseding. Required authorizing WM-REC-010; optional WM-ACT-034 evidence. Dual-track IC and Manager standing means two assignments and two ratifications. Two current rows on the same Employment, version and axis are invalid.

## Calibration

Process profile, not a type. WM-ACT-034 = panel, version in force, evidence, recommendation, dissent. WM-REC-010 = ratification of assignment, version freeze, or crosswalk. Act without ratification is recommended, not in force. Evidence is not the assignment and not a rating.

## Crosswalk / merger

Owned directed mapping, not a root. Pin source version, target version, direction, purpose and semantic loss. Purposes: merger-consolidation, reporting-roll-up, mobility-interpretation. Reject pay, access and pay-eligibility-hint purposes. Unmappable level = null map plus reason; no neighbor-ordinal coercion. Many-to-one and one-to-many are allowed if loss is stated. Keep source schemes; optionally map both into a new target version. Approval is a WM-REC-010, not an assignment and not pay. Maps are not retroactive.

## Competency / qualification / performance

Defer proficiency-typed expectations and calibrate-against-proficiency. Performance rating is Assessment/Evaluation evidence only. Qualification and credential may be expected; holding them does not assign a grade. Profile fulfillment does not create a GradeAssignment.

## Compensation / position / access

A grade WM-REC-010 mutates only GradeAssignment and that decision. It changes no band, pay decision, payroll fact, Position, PositionGrade, qualification, credential or access. Pay needs separate compensation authority. Incumbent may be over or under the seat. No access master is in the listed drafts: state the invariant; do not bind a type.

## Privacy / time

Assignments are effective-dated. As-of queries treat scheme version, assignment, PositionGrade, band, pay decision and payroll fact as independently dated. Reassessment never rewrites a cited level; it inserts and closes. Ended Employment closes current assignments; records are retained. Assignment and decision may outlive employment; panel notes follow Assessment/Evaluation retention. Calibration-purpose read does not authorize pay, access or disclosure. Do not treat grade and pay as a published join.

## Scenario

S1: Single-axis A.v1 L1–L8 versus one dual-track scheme B.v1 (IC and Manager). Dual-track standing is two assignments, not two schemes. S2: A.v1/L8 unmappable; null map plus reason; person stays on A until a separate B assignment is ratified. S3: 2022 GA1 A.v1/L5 closes on 2026 reassessment; GA2 cites B.v1/IC/I4; 2022 as-of still sees L5. S4: pay is unchanged until Payroll/Compensation issues its own pay decision; grade authority is neither sufficient nor necessary for pay, position or access.

## Invariants

I1 GradeLevel identity is Scheme, Version, level-code, track or axis; it is not a root. I2 Equal labels or ordinals never prove equivalence and never insert a map row. I3 Assignment cites one GradeLevel in one SchemeVersion. I4 Subject is Employment, or occupancy only if Employment is absent. I5 Grade decision mutates only assignment and its WM-REC-010. I6 PositionGrade is not GradeAssignment; neither updates the other. I7 RoleProfile holds expectations only. I8 Version is immutable after freeze. I9 Reassessment inserts and closes; never rewrites cited level. I10 Crosswalk is owned, directed, version-pinned, purpose-pinned and loss-stated; pay and access purposes are rejected. Also: one current assignment per Employment, version and axis; calibration is act plus decision; ratings, qualifications and credentials are not grades; crosswalk approval is not assignment or pay; competency is out of scope; independently dated as-of; no published grade-pay join; calibration access is not disclosure authority.

## Minimum model set

GradeScheme; owned SchemeVersion, GradeLevel, Track/Axis and Crosswalk; RoleProfile; GradeAssignment; Position plus PositionGrade; Party Role; Employment; WM-REC-010; WM-ACT-034; Education/Qualification; Attestation/Credential; Payroll/Compensation with band, pay decision and payroll fact kept separate. Out: Skill/Competency, access master, GradeCalibration as a type.

## Blockers

B1 Skill/Competency reserved, no spec. B2 No target IDs: cannot publish or bind allocated types. B3 Position draft must expose PositionGrade distinct from GradeAssignment. B4 Assignment subject must be Employment in the Employment and Party Role drafts. B5 WM-ACT-034 and WM-REC-010 composition unverified. B6 Crosswalk purpose vocabulary and semantic loss have no existing type. B7 Access master absent. B8 Payroll/Compensation must distinguish band, pay decision and payroll fact. B9 Assessment/Evaluation must keep ratings evidence-only.

## Candidates and gaps

Accept GradeScheme root, SchemeVersion owned, GradeLevel owned, Track/Axis owned, RoleProfile root, GradeAssignment root, PositionGrade as Position relation. Reject GradeCalibration as root, accepting WM-ACT-034 plus WM-REC-010 profile; reject GradeCrosswalk as root, accepting owned mapping; reject identifier allocation and pay/access purposes. Defer competency-typed relations. Gaps: optional RoleProfile-to-Position reference; Employment subject; PositionGrade distinctness; required authorizedBy WM-REC-010; optional evidencedBy WM-ACT-034; moderation against SchemeVersion; locked crosswalk shape; freeze then new version; explicit profile carry-forward; access unbound.
