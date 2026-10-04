You are the single frozen semantic auditor for EM-PEO-08. No tools, no browsing. Review only the frozen material below. Return ACCEPT or REVISE, then a closed numbered checklist. Check identity, lifecycle, mastership, version pins, temporal behavior, privacy, crosswalks, profile boundaries, stable rule IDs, fixture coverage, no guessed identifiers and no publication claim.

## provider-comparison.md
# EM-PEO-08 provider comparison

Claude and Grok agree on exactly three identifier-unassigned roots: Grade Scheme, Role Profile and Grade Assignment. Both keep Grade Level owned by an immutable scheme version and treat Grade Calibration as WM-ACT-034 moderation plus WM-REC-010 ratification. No identifier is allocated.

Grok sharpens the assignment subject: Employment is required when present, with a concrete Party Role occupancy allowed only when Employment is absent; bare Person, Position, role type, profile and compensation subjects are rejected. It also restricts crosswalk purposes, requires explicit null mappings for unmappable levels and defers competency-typed expectations while WM-PER-009 lacks a current specification.

The reconciled revision 2 incorporates those constraints, keeps PositionGrade separate, and defines independently dated as-of behavior. Publication remains held.

## claude-study.raw.md
# EM-PEO-08 — Grades and Expectation Profiles

## Verdict

- **GradeScheme** — **new root**, identifier unassigned. Versioned level-system definition (authority, jurisdiction, dimensionality, level set, ordering semantics, deprecation, crosswalk register).
- **GradeLevel** — **no independent root.** Scheme-scoped member of the GradeScheme aggregate; it has no identity outside a scheme version.
- **RoleProfile** — **new root**, identifier unassigned. Versioned expectation definition referencing a role-type term, Position/Party Role, a GradeScheme level and competency expectations.
- **GradeAssignment** — **new root**, identifier unassigned. A subject-scoped level assertion. The authorizing act profiles WM-REC-010; supporting evidence profiles WM-ACT-034; employment/position supply context by reference only.
- **GradeCalibration** — **no new root.** Two profiles: moderation/agreement evidence on WM-ACT-034, per-subject ratified outcomes on WM-REC-010. The deliberative occasion itself is an unclosed gap (WM-ACT-025 absent from the dossier).

No identifiers allocated; no relation rows proposed as approved.

## Evidence

WM-ORG-004 already owns `grade-level-and-job-evaluation` for the **seat** and states pay range and grade ladders are "referenced by key", with compensation plan master data out of scope. WM-XCT-023 is a reified assertion mixin that carries no permissions, no value semantics, and binds role types to an externally governed concept scheme. WM-ACT-034 owns criteria binding at pinned version, moderation, rater agreement and the prohibition on coercing indeterminate results. WM-REC-010 owns competence, reasons, validity window and supersession. WM-ECO-031 owns compensation terms and requires separate approval before release. WM-PER-008 owns framework levels (EQF/ISCED) with an explicit non-equivalence rule. WM-PER-009 is reserved with no specification.

## Identity/mastership

Distinct identities: scheme definition; scheme version; level; crosswalk assertion; role profile version; position grade (job-evaluation outcome); grade assignment; grade decision; calibration session; calibration outcome; assessment result; competency assertion; qualification award; pay band; pay decision; payroll fact. Scheme owners master schemes and levels. Job-evaluation authorities master position grade. The grade authority masters assignments. WM-REC-010 decision authorities master decisions. WM-ECO-031 masters pay. WM-ACT-034 masters assessment and moderation evidence.

## Grade scheme/levels

Yes — GradeScheme owns GradeLevels. Levels are non-independent parts canonicalizing under (scheme, version, level key). Dimensionality is a scheme property: single ladder, dual-track, or n-axis (scope × complexity × autonomy). Ordinal position is scheme-local and carries no cross-scheme meaning. Level retirement creates a successor version with mapping lineage; prior assignments keep the version they were decided under.

## Role profile

RoleProfile is a versioned definition, not an instance. It exists with no position and no occupant, is reused across many positions, and survives position abolition — so it is neither a WM-ORG-004 profile nor a WM-XCT-023 assertion. It references the role-type vocabulary term, zero-or-many Positions, a GradeScheme level, and competency expectations at pinned scheme/scale versions (WM-PER-009 plus the Proficiency Scale proposed at EM-PEO-03). Expectations are requirements on any holder; they are never assertions about an occupant.

## Assignment

GradeAssignment needs an independent assertion root. A decision is a dated act; the assertion has its own validity window, evidence set, revalidation interval, supersession chain and challenge state, and must remain resolvable after the deciding body changes. It is not a role, so WM-XCT-023 is rejected as the carrier. It is not employment status, so WM-ORG-005 is rejected. It pins subject, employment or position context, scheme version, level, effective interval, basis, deciding authority and WM-REC-010 decision reference. Precedent: the Person Capability Assertion root proposed at EM-PEO-03.

## Calibration

Calibration is moderation, not classification. WM-ACT-034 already supplies reviewer independence, agreement statistics against a threshold, disagreement adjudication and finalisation freeze — the calibration session profiles that. Each ratified change is a separate WM-REC-010 decision producing a successor GradeAssignment. Calibration never rewrites a finalised assessment result. Session composition, recusal and the deliberative occasion remain unowned in this dossier.

## Crosswalk/merger

A mapping between two ladders is an assertion, not a property of either scheme. It pins source and target scheme versions, direction, purpose (pay benchmarking ≠ career progression ≠ statutory reporting), authority, strength, and declared loss. It is partial by construction: unmapped levels stay unmapped. Matching labels ("Middle") or matching ordinals prove nothing. The negative case — declaring two companies' Middle one global level without a crosswalk — is a defect: it fabricates equivalence, erases dimensionality and destroys purpose scope.

## Competency/qualification/performance

Job grade (scheme level), skill proficiency (competency at a scale level), performance rating (assessment of a period's work) and qualification level (EQF/NQF) are four non-convertible axes. None derives from another. WM-PER-008 already forbids treating framework levels as equivalence. Performance rating has no owner in this dossier and must not be stored as a grade level; it profiles WM-ACT-034.

## Compensation/position/access

A grade decision changes nothing else. Pay requires its own WM-REC-010 decision plus a WM-ECO-031 term binding; WM-ECO-031 keeps calculated, approved, released and paid as independent states. Position grade changes only through job-evaluation authority in WM-ORG-004. Qualification and credential status change only through WM-PER-008/WM-XCT-017 issuers. Access is never derived: WM-XCT-023 already forbids implicit grants.

## Privacy/retention

Performance and calibration evidence are deny-by-default, purpose-bound, minimum-disclosure. Separate scopes for level, rationale, comparative ranking and dissent. The subject reads what they need to contest. Retention triggers differ per assertion, decision and evidence item; legal hold suspends disposition; disposal never cascades to person, employment, position or payroll.

## Time/provenance

Separate: effective, decided, asserted, assessed, calibrated, observed, communicated and knowledge times. RFC 3339 with explicit offset. Retroactive reassessment appends a successor and preserves what was previously believed.

## Acceptance scenario

Company A: single ladder L1–L10. Company B: dual-track (IC1–IC6, M1–M4) over scope × autonomy. Purpose-qualified partial mapping pins both versions: A-L5 → {IC3} narrow, for pay benchmarking only. B-M2 has no A counterpart — recorded unmappable, not forced. A historical 2024 reassessment appends a successor assignment and a new decision; the original assessment result and level stay final and readable. The resulting pay change is refused until a separate compensation decision under WM-ECO-031 authority exists.

## Invariants

1. Every level reference names scheme and version. 2. Ordinals and labels are scheme-local. 3. Mappings are partial, directional, purpose-qualified and loss-declaring. 4. Position grade ≠ person grade. 5. Grade ≠ proficiency ≠ performance ≠ qualification. 6. RoleProfile expectation ≠ occupant assertion. 7. A grade decision changes no pay, position, qualification or access. 8. Compensation change requires its own authority. 9. Calibration appends; it never overwrites assessments. 10. Unmappable is a recorded state, never a default or a zero. 11. Finalised results are not recomputed against later scheme versions. 12. Missing grade is unknown.

## Minimal model set

GradeScheme (with GradeLevel members), RoleProfile, GradeAssignment — three unassigned roots. Profiles: grade decision and calibration outcome on WM-REC-010; assessment and moderation on WM-ACT-034; expectations bound to WM-ORG-004 and WM-XCT-023; pay to WM-ECO-031; qualification to WM-PER-008/WM-XCT-017.

## Holds

No target IDs allocated. All supplied bases are non-canonical reviewable drafts; WM-ACT-034 carries a single-provider waiver and an access-dimension downgrade hold; WM-PER-008, WM-ORG-005, WM-ECO-031 and WM-XCT-017 are codex-only waived. No approved relation rows exist for any proposed edge. WM-PER-009 has no specification and its legacy reference conflates human capability with system function. Performance rating, calibration-session occasion, job-family architecture and pay-band master data have no owner here. HR Open, ESCO, SFIA and SPACE crosswalks, and all source pins, are unverified. No claim of canonical completeness, installability or publication readiness.

## grok-study.raw.md
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

## GS/allocation-candidate.json
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-PEO-08",
  "proposedName": "Grade Scheme",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A governed grading framework remains identifiable independently of people, positions, assignments and compensation while its level semantics evolve through immutable releases.",
    "versionIdentity": "Any change to axes, levels, ordering, applicability or crosswalk semantics creates a successor scheme version.",
    "independentLifecycle": [
      "draft",
      "reviewed",
      "approved",
      "published",
      "effective",
      "deprecated",
      "superseded",
      "retired"
    ],
    "mastership": "enterprise grade architecture authority"
  },
  "boundary": {
    "owns": [
      "grade-scheme identity",
      "immutable scheme versions",
      "scheme-version-owned grade levels",
      "axis and ordering semantics",
      "applicability and jurisdiction",
      "directional purpose-qualified crosswalk assertions",
      "deprecation and successor history"
    ],
    "references": [
      {
        "target": "WM-ORG-004",
        "purpose": "Position and job-evaluation context",
        "contractState": "provisional"
      },
      {
        "target": "WM-XCT-023",
        "purpose": "Role assertion context",
        "contractState": "provisional"
      },
      {
        "target": "WM-PER-009",
        "purpose": "Competency definition",
        "contractState": "provisional"
      },
      {
        "target": "WM-PER-008",
        "purpose": "Qualification context",
        "contractState": "provisional"
      },
      {
        "target": "WM-ECO-031",
        "purpose": "Compensation boundary",
        "contractState": "provisional"
      }
    ],
    "excludes": [
      "person or position identity",
      "person grade assignment",
      "role profile",
      "performance rating",
      "qualification or credential",
      "compensation band or payroll fact"
    ]
  },
  "objects": {
    "GradeScheme": {
      "identity": [
        "gradeSchemeId"
      ],
      "required": [
        "name",
        "ownerRef",
        "status",
        "createdAt"
      ],
      "optional": [
        "jurisdiction",
        "successorRef"
      ]
    },
    "GradeSchemeVersion": {
      "identity": [
        "gradeSchemeId",
        "versionId"
      ],
      "required": [
        "tracksOrAxes",
        "levels",
        "status",
        "effectiveFrom",
        "contentDigest",
        "freezeDecisionRef"
      ],
      "optional": [
        "effectiveTo",
        "supersedesVersionRef"
      ],
      "assignmentTargetWhen": "status is frozen or effective"
    },
    "GradeLevel": {
      "identity": [
        "gradeSchemeId",
        "versionId",
        "trackOrAxisKey",
        "levelKey"
      ],
      "required": [
        "label",
        "semantics"
      ],
      "optional": [
        "ordinal",
        "axisCoordinates"
      ],
      "root": false
    },
    "GradeCrosswalk": {
      "identity": [
        "gradeSchemeId",
        "crosswalkId",
        "revision"
      ],
      "required": [
        "sourceVersionRef",
        "targetVersionRef",
        "direction",
        "purpose",
        "mappingRows",
        "semanticLoss",
        "decisionRef",
        "effectiveFrom"
      ],
      "optional": [
        "effectiveTo",
        "supersedesRef"
      ],
      "root": false
    }
  },
  "invariants": [
    "GradeLevel identity is local to one scheme version and track or axis; it is not a root.",
    "A dual-track ladder is one scheme with multiple tracks, not multiple schemes.",
    "Labels and ordinals never prove cross-scheme equivalence.",
    "Published or frozen scheme versions are immutable.",
    "Only frozen or effective scheme versions are assignment targets.",
    "Relabeling, reordering or adding levels creates a successor version.",
    "Historical assignments retain their cited version.",
    "Crosswalks are owned, directed, version-pinned, purpose-pinned and semantic-loss declaring.",
    "Unmappable is an explicit null mapping with reason; neighbor ordinals are never coerced.",
    "Many-to-one and one-to-many mappings declare loss.",
    "Crosswalk approval creates no GradeAssignment and changes no pay or access.",
    "Crosswalks are never retroactive.",
    "Retirement preserves historical resolution.",
    "Missing grade is unknown, never a default.",
    "Scheme changes mutate no person, employment, position, compensation or access master.",
    "No identifier is allocated without registry reservation."
  ],
  "holds": [
    "Registry allocation is pending; no identifier is guessed.",
    "External relations and reciprocal contracts remain provisional.",
    "Base models remain non-canonical drafts; WM-PER-009 has no current specification.",
    "Privacy, retention, package conversion and live conformance remain pending."
  ],
  "candidateRevision": 2,
  "relationPolicy": "Every external relation is provisional until reciprocal registry approval.",
  "digestPolicy": {
    "algorithm": "SHA-256",
    "canonicalization": "UTF-8 canonical JSON, sorted keys, no insignificant whitespace",
    "coverage": "all released semantic fields",
    "verification": "unverified until live conformance"
  },
  "privacyPolicy": {
    "purposeLimited": true,
    "minimumDisclosure": true,
    "denyByDefaultEvidence": true,
    "unknownDistinctFromAbsent": true
  },
  "allowedCrosswalkPurposes": [
    "merger-consolidation",
    "reporting-roll-up",
    "mobility-interpretation"
  ],
  "forbiddenCrosswalkPurposes": [
    "pay",
    "access",
    "pay-eligibility-hint"
  ]
}

## GS/fixtures.json
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Grade Scheme",
  "executable": false,
  "status": "declarative-normative-expectations",
  "cases": [
    {
      "id": "single-axis",
      "kind": "positive",
      "input": "A ten-level version is frozen before use.",
      "expect": "Normatively, it is an eligible assignment target.",
      "rules": [
        "GS-INV-01"
      ]
    },
    {
      "id": "dual-track",
      "kind": "positive",
      "input": "One version has IC and Manager tracks.",
      "expect": "Normatively, it remains one scheme with track-local levels.",
      "rules": [
        "GS-INV-02"
      ]
    },
    {
      "id": "partial-map",
      "kind": "positive",
      "input": "A level has no target counterpart.",
      "expect": "Normatively, the mapping is null with a reason.",
      "rules": [
        "GS-INV-03"
      ]
    },
    {
      "id": "many-one",
      "kind": "positive",
      "input": "Two source levels map to one target.",
      "expect": "Normatively, semantic loss is declared.",
      "rules": [
        "GS-INV-04"
      ]
    },
    {
      "id": "historic-pin",
      "kind": "positive",
      "input": "A successor version is published.",
      "expect": "Normatively, old assignments still resolve against the old version.",
      "rules": [
        "GS-INV-05"
      ]
    },
    {
      "id": "label-match",
      "kind": "negative",
      "input": "Two schemes use Principal.",
      "expect": "Normatively, no equivalence is inferred.",
      "rules": [
        "GS-INV-06"
      ]
    },
    {
      "id": "ordinal-coercion",
      "kind": "negative",
      "input": "L8 is mapped to nearest target ordinal.",
      "expect": "Normatively, the coercion is rejected.",
      "rules": [
        "GS-INV-07"
      ]
    },
    {
      "id": "pay-purpose",
      "kind": "negative",
      "input": "A crosswalk purpose is pay eligibility.",
      "expect": "Normatively, the purpose is rejected.",
      "rules": [
        "GS-INV-08"
      ]
    },
    {
      "id": "draft-target",
      "kind": "negative",
      "input": "An assignment cites a draft version.",
      "expect": "Normatively, the assignment is rejected.",
      "rules": [
        "GS-INV-09"
      ]
    },
    {
      "id": "retro-map",
      "kind": "negative",
      "input": "A crosswalk rewrites prior mappings.",
      "expect": "Normatively, the retroactive mutation is rejected.",
      "rules": [
        "GS-INV-10"
      ]
    },
    {
      "id": "freeze-edit",
      "kind": "negative",
      "input": "A frozen level label is edited.",
      "expect": "Normatively, a successor version is required.",
      "rules": [
        "GS-INV-11"
      ]
    },
    {
      "id": "crosswalk-assignment",
      "kind": "negative",
      "input": "Crosswalk approval creates a person assignment.",
      "expect": "Normatively, the inference is rejected.",
      "rules": [
        "GS-INV-12"
      ]
    },
    {
      "id": "missing-grade",
      "kind": "semantic",
      "input": "No grade is recorded.",
      "expect": "Normatively, the state is unknown.",
      "rules": [
        "GS-INV-13"
      ]
    },
    {
      "id": "retirement",
      "kind": "semantic",
      "input": "A scheme retires.",
      "expect": "Normatively, historical references remain resolvable.",
      "rules": [
        "GS-INV-14"
      ]
    }
  ]
}

## RP/allocation-candidate.json
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-PEO-08",
  "proposedName": "Role Profile",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A reusable versioned expectation definition remains identifiable without a position or occupant.",
    "versionIdentity": "Changes to role scope, grade expectation, competency requirements or applicability create a successor version.",
    "independentLifecycle": [
      "draft",
      "reviewed",
      "approved",
      "published",
      "effective",
      "deprecated",
      "superseded",
      "retired"
    ],
    "mastership": "enterprise role architecture authority"
  },
  "boundary": {
    "owns": [
      "role-profile identity",
      "immutable role-profile versions",
      "role-type binding",
      "grade expectation",
      "competency and qualification expectations",
      "applicability rules",
      "effective and successor history"
    ],
    "references": [
      {
        "target": "WM-XCT-023",
        "purpose": "Role assertion and role type",
        "contractState": "provisional"
      },
      {
        "target": "WM-ORG-004",
        "purpose": "Applicable positions",
        "contractState": "provisional"
      },
      {
        "target": "WM-PER-009",
        "purpose": "Competency expectation",
        "contractState": "provisional"
      },
      {
        "target": "WM-PER-008",
        "purpose": "Qualification expectation",
        "contractState": "provisional"
      },
      {
        "target": "WM-REC-010",
        "purpose": "Authorizing decision",
        "contractState": "provisional"
      }
    ],
    "excludes": [
      "occupant capability assertion",
      "position identity",
      "employment relationship",
      "grade assignment",
      "performance rating",
      "compensation decision"
    ]
  },
  "objects": {
    "RoleProfile": {
      "identity": [
        "roleProfileId"
      ],
      "required": [
        "name",
        "ownerRef",
        "status",
        "createdAt"
      ],
      "optional": [
        "roleTypeRef",
        "successorRef"
      ]
    },
    "RoleProfileVersion": {
      "identity": [
        "roleProfileId",
        "versionId"
      ],
      "required": [
        "gradeExpectation",
        "qualificationExpectations",
        "credentialExpectations",
        "applicability",
        "status",
        "effectiveFrom",
        "contentDigest",
        "authorizationRef"
      ],
      "optional": [
        "applicablePositionRefs",
        "effectiveTo",
        "supersedesRef",
        "carryForwardDecisionRef"
      ]
    }
  },
  "invariants": [
    "A RoleProfile is a reusable expectation definition, not a Position, Party Role or occupant assertion.",
    "A RoleProfile may exist without a Position or occupant.",
    "Many Positions may cite one profile and a Position may cite none.",
    "Published versions are immutable.",
    "Grade expectation pins scheme version, track or axis and a level or bounded range.",
    "Qualification and credential expectations remain externally mastered.",
    "Competency expectations are absent, not unknown facts, while WM-PER-009 is unspecified.",
    "Expectations never assert occupant capability, qualification, grade, pay or access.",
    "A profile stores no incumbent, assignment, compensation object or permission.",
    "Version carry-forward requires an explicit decision and never silently retargets.",
    "Applicability is explicit and time-bounded.",
    "Profile fulfillment creates no GradeAssignment.",
    "Unknown occupant capability is never inferred.",
    "No identifier is allocated without registry reservation."
  ],
  "holds": [
    "Registry allocation is pending; no identifier is guessed.",
    "External relations and reciprocal contracts remain provisional.",
    "Base models remain non-canonical drafts; WM-PER-009 has no current specification.",
    "Privacy, retention, package conversion and live conformance remain pending."
  ],
  "candidateRevision": 2,
  "relationPolicy": "Every external relation is provisional until reciprocal registry approval.",
  "digestPolicy": {
    "algorithm": "SHA-256",
    "canonicalization": "UTF-8 canonical JSON, sorted keys, no insignificant whitespace",
    "coverage": "all released semantic fields",
    "verification": "unverified until live conformance"
  },
  "privacyPolicy": {
    "purposeLimited": true,
    "minimumDisclosure": true,
    "denyByDefaultEvidence": true,
    "unknownDistinctFromAbsent": true
  },
  "competencyExpectationPolicy": "Deferred while WM-PER-009 lacks a current specification; no proficiency-typed relation is asserted."
}

## RP/fixtures.json
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Role Profile",
  "executable": false,
  "status": "declarative-normative-expectations",
  "cases": [
    {
      "id": "vacant-profile",
      "kind": "positive",
      "input": "A profile exists before any Position.",
      "expect": "Normatively, the definition remains valid.",
      "rules": [
        "RP-INV-01"
      ]
    },
    {
      "id": "multi-position",
      "kind": "positive",
      "input": "Several Positions cite one profile.",
      "expect": "Normatively, the reuse is conformant.",
      "rules": [
        "RP-INV-02"
      ]
    },
    {
      "id": "grade-range",
      "kind": "positive",
      "input": "A profile pins a version, track and bounded range.",
      "expect": "Normatively, the expectation is reproducible.",
      "rules": [
        "RP-INV-03"
      ]
    },
    {
      "id": "qualification",
      "kind": "positive",
      "input": "A qualification expectation cites its master.",
      "expect": "Normatively, the expectation does not award it.",
      "rules": [
        "RP-INV-04"
      ]
    },
    {
      "id": "carry-forward",
      "kind": "positive",
      "input": "A successor scheme is adopted by decision.",
      "expect": "Normatively, the profile retargets only through explicit carry-forward.",
      "rules": [
        "RP-INV-05"
      ]
    },
    {
      "id": "incumbent",
      "kind": "negative",
      "input": "A profile stores an incumbent.",
      "expect": "Normatively, the payload is rejected.",
      "rules": [
        "RP-INV-06"
      ]
    },
    {
      "id": "assigned-grade",
      "kind": "negative",
      "input": "A profile stores a person's grade.",
      "expect": "Normatively, the assertion is rejected.",
      "rules": [
        "RP-INV-07"
      ]
    },
    {
      "id": "pay",
      "kind": "negative",
      "input": "A profile changes pay.",
      "expect": "Normatively, the mutation is rejected.",
      "rules": [
        "RP-INV-08"
      ]
    },
    {
      "id": "access",
      "kind": "negative",
      "input": "Profile fulfillment grants access.",
      "expect": "Normatively, the inference is rejected.",
      "rules": [
        "RP-INV-09"
      ]
    },
    {
      "id": "silent-retarget",
      "kind": "negative",
      "input": "A scheme successor silently updates the profile.",
      "expect": "Normatively, the retarget is rejected.",
      "rules": [
        "RP-INV-10"
      ]
    },
    {
      "id": "competency-gap",
      "kind": "semantic",
      "input": "WM-PER-009 lacks a specification.",
      "expect": "Normatively, proficiency-typed expectations are deferred.",
      "rules": [
        "RP-INV-11"
      ]
    },
    {
      "id": "occupant-inference",
      "kind": "negative",
      "input": "An occupant is assumed qualified.",
      "expect": "Normatively, the inference is rejected.",
      "rules": [
        "RP-INV-12"
      ]
    },
    {
      "id": "mutable-version",
      "kind": "negative",
      "input": "A published version is edited.",
      "expect": "Normatively, a successor is required.",
      "rules": [
        "RP-INV-13"
      ]
    },
    {
      "id": "no-position",
      "kind": "positive",
      "input": "No Position cites a profile.",
      "expect": "Normatively, the profile may still exist.",
      "rules": [
        "RP-INV-14"
      ]
    }
  ]
}

## GA/allocation-candidate.json
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-PEO-08",
  "proposedName": "Grade Assignment",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A governed assertion that a subject holds a grade in a stated employment or position context remains identifiable independently of the subject and scheme.",
    "versionIdentity": "Reassessment, correction or changed authority creates a successor assignment linked to a separate decision.",
    "independentLifecycle": [
      "draft",
      "proposed",
      "decided",
      "effective",
      "challenged",
      "superseded",
      "revoked",
      "expired"
    ],
    "mastership": "authorized enterprise grade assignment authority"
  },
  "boundary": {
    "owns": [
      "grade-assignment identity",
      "subject and employment or position context",
      "pinned scheme version and level",
      "basis, evidence and authority binding",
      "validity and revalidation",
      "challenge and supersession history"
    ],
    "references": [
      {
        "target": "WM-PER-001",
        "purpose": "Person subject",
        "contractState": "provisional"
      },
      {
        "target": "WM-ORG-004",
        "purpose": "Position context",
        "contractState": "provisional"
      },
      {
        "target": "WM-ORG-005",
        "purpose": "Employment context",
        "contractState": "provisional"
      },
      {
        "target": "WM-REC-010",
        "purpose": "Authorizing decision",
        "contractState": "provisional"
      },
      {
        "target": "WM-ACT-034",
        "purpose": "Assessment and calibration evidence",
        "contractState": "provisional"
      },
      {
        "target": "WM-ECO-031",
        "purpose": "Compensation boundary",
        "contractState": "provisional"
      }
    ],
    "excludes": [
      "grade-scheme definition",
      "role profile",
      "person or position identity",
      "employment status",
      "assessment evidence payload",
      "salary, pay band or payroll fact"
    ]
  },
  "objects": {
    "GradeAssignment": {
      "identity": [
        "gradeAssignmentId"
      ],
      "required": [
        "contextType",
        "contextRef",
        "schemeVersionRef",
        "trackOrAxisKey",
        "levelRef",
        "decisionRef",
        "effectiveFrom",
        "status",
        "recordedAt",
        "recordedBy"
      ],
      "optional": [
        "effectiveTo",
        "evidenceRefs",
        "supersedesRef",
        "challengeState",
        "closureReason"
      ],
      "contextTypes": [
        "employment",
        "role-occupancy-without-employment"
      ]
    }
  },
  "invariants": [
    "Every assignment pins one exact scheme version, track or axis and GradeLevel.",
    "Subject context is Employment when it exists, otherwise one concrete role occupancy.",
    "Bare Person, Party, Position, role type, RoleProfile and compensation are forbidden subjects.",
    "Every assignment requires a separate authorizing WM-REC-010 decision.",
    "WM-ACT-034 evidence is optional and externally mastered.",
    "Two-track standing requires two assignments and two ratifications.",
    "At most one current assignment exists per context, scheme version and track or axis.",
    "Reassessment appends a successor and closes the predecessor; it never rewrites the cited level.",
    "Challenge state preserves effective-time history.",
    "PositionGrade and GradeAssignment never update each other.",
    "A grade decision mutates only its GradeAssignment and decision record.",
    "A grade decision changes no compensation band, pay decision, payroll fact, position, qualification, credential or access.",
    "Ended Employment closes current assignments without erasing them.",
    "As-of queries independently time scheme version, assignment, PositionGrade and compensation facts.",
    "No published grade-pay join is implied.",
    "Calibration-purpose access grants no disclosure authority.",
    "No identifier is allocated without registry reservation."
  ],
  "holds": [
    "Registry allocation is pending; no identifier is guessed.",
    "External relations and reciprocal contracts remain provisional.",
    "Base models remain non-canonical drafts; WM-PER-009 has no current specification.",
    "Privacy, retention, package conversion and live conformance remain pending."
  ],
  "candidateRevision": 2,
  "relationPolicy": "Every external relation is provisional until reciprocal registry approval.",
  "digestPolicy": {
    "algorithm": "SHA-256",
    "canonicalization": "UTF-8 canonical JSON, sorted keys, no insignificant whitespace",
    "coverage": "all released semantic fields",
    "verification": "unverified until live conformance"
  },
  "privacyPolicy": {
    "purposeLimited": true,
    "minimumDisclosure": true,
    "denyByDefaultEvidence": true,
    "unknownDistinctFromAbsent": true
  },
  "subjectPolicy": "Employment is required when it exists; otherwise a concrete Party Role occupancy instance is permitted. Bare Party, Person, Position, Party Role type, RoleProfile and compensation objects are forbidden.",
  "currentUniqueness": "At most one current assignment per context, scheme version and track or axis."
}

## GA/fixtures.json
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Grade Assignment",
  "executable": false,
  "status": "declarative-normative-expectations",
  "cases": [
    {
      "id": "employment-subject",
      "kind": "positive",
      "input": "An Employment receives one grade on the IC axis.",
      "expect": "Normatively, the assignment pins context, version, level and decision.",
      "rules": [
        "GA-INV-01"
      ]
    },
    {
      "id": "occupancy-fallback",
      "kind": "positive",
      "input": "No Employment exists but a concrete occupancy does.",
      "expect": "Normatively, the occupancy may be the context.",
      "rules": [
        "GA-INV-02"
      ]
    },
    {
      "id": "dual-track",
      "kind": "positive",
      "input": "One Employment holds IC and Manager standings.",
      "expect": "Normatively, two assignments and two decisions are required.",
      "rules": [
        "GA-INV-03"
      ]
    },
    {
      "id": "reassessment",
      "kind": "positive",
      "input": "A 2022 assignment changes in 2026.",
      "expect": "Normatively, a successor is appended and 2022 remains queryable.",
      "rules": [
        "GA-INV-04"
      ]
    },
    {
      "id": "challenge",
      "kind": "positive",
      "input": "The subject contests a grade.",
      "expect": "Normatively, challenge state preserves history.",
      "rules": [
        "GA-INV-05"
      ]
    },
    {
      "id": "bare-person",
      "kind": "negative",
      "input": "A Person is the direct subject.",
      "expect": "Normatively, the assignment is rejected.",
      "rules": [
        "GA-INV-06"
      ]
    },
    {
      "id": "position-subject",
      "kind": "negative",
      "input": "A Position is the direct subject.",
      "expect": "Normatively, the assignment is rejected.",
      "rules": [
        "GA-INV-07"
      ]
    },
    {
      "id": "duplicate-current",
      "kind": "negative",
      "input": "Two current IC assignments exist for one context and version.",
      "expect": "Normatively, the uniqueness violation is rejected.",
      "rules": [
        "GA-INV-08"
      ]
    },
    {
      "id": "implicit-pay",
      "kind": "negative",
      "input": "A grade decision changes compensation.",
      "expect": "Normatively, the mutation is rejected.",
      "rules": [
        "GA-INV-09"
      ]
    },
    {
      "id": "position-sync",
      "kind": "negative",
      "input": "A PositionGrade automatically changes an assignment.",
      "expect": "Normatively, the inference is rejected.",
      "rules": [
        "GA-INV-10"
      ]
    },
    {
      "id": "qualification-sync",
      "kind": "negative",
      "input": "A qualification creates a grade.",
      "expect": "Normatively, the inference is rejected.",
      "rules": [
        "GA-INV-11"
      ]
    },
    {
      "id": "access-sync",
      "kind": "negative",
      "input": "A grade grants access.",
      "expect": "Normatively, the inference is rejected.",
      "rules": [
        "GA-INV-12"
      ]
    },
    {
      "id": "overwrite",
      "kind": "negative",
      "input": "Reassessment overwrites the 2022 row.",
      "expect": "Normatively, the destructive update is rejected.",
      "rules": [
        "GA-INV-13"
      ]
    },
    {
      "id": "employment-end",
      "kind": "semantic",
      "input": "Employment ends.",
      "expect": "Normatively, current assignments close but remain retained.",
      "rules": [
        "GA-INV-14"
      ]
    },
    {
      "id": "as-of",
      "kind": "semantic",
      "input": "A 2022 query runs after a 2026 successor.",
      "expect": "Normatively, the 2022 assignment remains effective for that instant.",
      "rules": [
        "GA-INV-15"
      ]
    },
    {
      "id": "calibration-only",
      "kind": "negative",
      "input": "A moderation recommendation lacks ratification.",
      "expect": "Normatively, no in-force assignment is created.",
      "rules": [
        "GA-INV-16"
      ]
    }
  ]
}

## profile-candidate.json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-PEO-08",
  "name": "Enterprise Grade Architecture and Calibration",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ORG-004",
    "WM-XCT-023",
    "WM-PER-008",
    "WM-ACT-034",
    "WM-REC-010",
    "WM-ORG-005",
    "WM-ECO-031",
    "WM-XCT-017"
  ],
  "constraints": [
    "Grade, proficiency, performance, qualification and compensation remain separate axes.",
    "GradeCalibration is a process profile: WM-ACT-034 recommendation plus WM-REC-010 ratification.",
    "A moderation act without ratification is not in force.",
    "PositionGrade is a Position relation and is distinct from GradeAssignment.",
    "GradeCrosswalk is scheme-owned and is not a root.",
    "Crosswalk and calibration decisions create neither grade assignment nor compensation change.",
    "No grade, profile, assignment or decision confers access."
  ],
  "candidateRevision": 2,
  "candidateRoots": [
    "Grade Scheme",
    "Role Profile",
    "Grade Assignment"
  ],
  "deferredBases": [
    {
      "id": "WM-PER-009",
      "reason": "reserved but no current specification"
    }
  ],
  "relationState": "provisional-reviewable-draft"
}
