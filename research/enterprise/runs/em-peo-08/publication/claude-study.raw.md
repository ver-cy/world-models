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
