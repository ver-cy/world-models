# EM-PEO-08 local synthesis

## Disposition

- Propose identifier-unassigned **Grade Scheme**, **Role Profile** and **Grade Assignment** roots.
- Keep Grade Level as a scheme-version-owned member rather than an independent root.
- Profile Grade Calibration as moderation evidence on WM-ACT-034 and ratified per-subject decisions on WM-REC-010; create no calibration root.
- Reuse WM-ORG-004 for position/job-evaluation context, WM-XCT-023 for role assertions, WM-PER-009 and its proposed Proficiency Scale for competency expectations, WM-PER-008/WM-XCT-017 for qualification and credential facts, and WM-ECO-031 for compensation.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Grade scheme, scheme version, level, crosswalk assertion, role-profile version, position grade, person grade assignment, authorizing decision, calibration occasion, moderation evidence, assessment result, competency assertion, qualification award, pay band, compensation decision and payroll fact remain distinct.

Scheme owners master schemes and levels. Role-architecture stewards master role profiles. Job-evaluation authorities master position grade. Grade authorities master person assignments. WM-ACT-034 masters assessment/moderation evidence, WM-REC-010 masters decisions, and WM-ECO-031 remains the compensation source.

## Grade scheme and levels

Grade Scheme is a versioned definition with authority, jurisdiction, dimensionality, ordered or multi-axis level set, semantics, deprecation and crosswalk register. Grade Levels canonicalize under scheme, version and level key; a label or ordinal has no meaning outside that context. Retirement creates a successor scheme version while historical assignments remain pinned to their original version.

Mappings are independent assertions that pin both scheme versions, direction, purpose, authority, strength and declared loss. They are partial by design. Equal labels or ordinals never establish equivalence, and unmappable is an explicit result rather than zero or default.

## Role profile

Role Profile is a reusable versioned expectation definition that can exist without a position or occupant. It references a role-type term, applicable positions or role assertions, a scheme-version level and competency expectations pinned to competency and proficiency-scale versions. Expectations describe requirements for holders and never become claims about an occupant.

## Grade assignment and calibration

Grade Assignment independently asserts a subject's level in an employment or position context. It owns validity, evidence, revalidation, supersession and challenge state, and pins scheme version, level, basis, authority and WM-REC-010 decision. It is neither a Party Role nor employment status.

Calibration is moderation rather than classification. WM-ACT-034 records independence, agreement, disagreement resolution and finalized evidence. Each ratified change is a separate WM-REC-010 decision producing a successor Grade Assignment. Calibration never rewrites finalized assessments. The session/occasion boundary remains unresolved because WM-ACT-025 was outside the frozen dossier.

## Non-equivalent axes

Job grade, competency proficiency, period performance rating, qualification framework level and compensation band are distinct axes. None derives from another. A grade decision changes no salary, position, qualification, credential, role authority or access. Compensation requires its own authorized decision and WM-ECO-031 term binding.

## Privacy, time and retention

Performance and calibration evidence are deny-by-default, purpose-bound and minimally disclosed. Level, rationale, comparative ranking and dissent have separate scopes. The subject receives sufficient information and route to contest a decision. Effective, decided, asserted, assessed, calibrated, observed, communicated and knowledge times remain distinct. Retroactive reassessment appends a successor. Legal hold suspends disposition; disposal never cascades to person, employment, position or payroll masters.

## Required invariants

1. Every level reference names a scheme and version.
2. Labels and ordinals are scheme-local.
3. Crosswalks are partial, directional, purpose-qualified and loss-declaring.
4. Unmappable is explicit and never coerced.
5. Position grade and person grade assignment are distinct.
6. Grade, proficiency, performance, qualification and compensation are non-equivalent.
7. Role-profile expectations are not occupant assertions.
8. Grade decisions change no pay, position, qualification or access.
9. Compensation change requires separate authority.
10. Calibration appends successors and never overwrites assessments.
11. Final results are not recomputed under later scheme versions.
12. Missing grade remains unknown.

## Acceptance result

A single-axis L1–L10 ladder and a dual-track, multi-axis ladder are mapped only for the stated pay-benchmarking purpose. One source level maps narrowly, another remains unmappable. A historical reassessment appends a successor assignment and decision while the original evidence remains resolvable. A proposed pay change is rejected until separately authorized in the compensation domain.

## Holds

The three proposed roots have no allocations. All bases remain non-canonical drafts; WM-ACT-034 retains access and single-provider holds; WM-PER-009 lacks a current specification. No approved relations support the proposed edges. Performance rating, calibration session, job-family architecture and pay-band master data have no settled owner. Crosswalks, source pins and fixtures remain unverified. This checkpoint is not an installable release.
