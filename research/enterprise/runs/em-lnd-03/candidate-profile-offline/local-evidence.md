# EM-LND-03 local synthesis

## Disposition

- Define Workforce Landscape as a governed, reproducible projection over personnel, employment, assignment, position and organization masters.
- Define Workforce Scope as its versioned scope and counting parameterization. It has artifact identity so results can be reproduced, but no independent subject-model identity.
- Reuse WM-XCT-002 for authorized population access and WM-XCT-003 for output shape. Allocate no new runtime/model identifier.

## Identity and mastership

WM-PER-001 masters natural-person identity; WM-ORG-005 employment relationship; WM-ORG-016 work assignment; WM-ORG-004 position; WM-ORG-002 unit/hierarchy snapshot. The landscape masters no person, relationship, assignment, position or status fact and resolves each figure to pinned sources.

One person can have several simultaneous or successive employment relationships and assignments. Relationship endpoints do not identify a relationship, and relationship multiplicity never creates additional persons.

## Population boundary and counting

Workforce Scope states reporting-party role, included relationship/assignment states, person/position inclusion, unnamed or pooled occupancy policy, boundary organizations, world/knowledge time, point-in-time or period-average convention and period-end rule. Missing parameters make a figure unpublishable.

Measures stay distinct:

- unique persons: distinct WM-PER-001 anchors;
- legal headcount: qualifying employment relationships for the reporting employer under a named scheme;
- distinct employed persons: unique people behind those relationships;
- active relationships: asserted in-scope WM-ORG-005 records;
- assignments: in-force WM-ORG-016 records;
- positions: established WM-ORG-004 seats, including vacancies as declared;
- FTE: either demand-side authorized position FTE or supply-side allocated assignment effort, with rule and denominator;
- capacity: available effort after interruptions and constraints.

No measure is summed across kinds. Suppressed and unknown are never zero. Vacant positions contribute position/FTE demand but no person. Active status is asserted and cannot be inferred from payroll, badge, assignment or contract dates.

## Contractors and dual affiliation

Contractors, volunteers and agency workers can have assignments without host employment. They contribute to declared assignment, FTE or capacity measures but not host legal headcount. Agency employment belongs to the agency while the host owns assignment/presence context. Statistical, tax, social-insurance and labor classifications remain separate purpose-qualified schemes.

One person employed by A and B yields one unique person, two employment relationships and one employer headcount in each employer perimeter. Cross-employer allocated FTE may exceed 1.0 and must not be clipped without an explicit cross-employer rule.

## Time, privacy and disclosure

Every result records world-time and knowledge-time, period convention, scope/version pins and completeness. Scenario results remain separate from authoritative results.

Counts near one, small cross-tabs, release deltas, extrema, unusual FTE fractions and unique dual-affiliation patterns can disclose individuals. WM-XCT-002 limits purpose and audience; WM-XCT-003 fixes aggregate-only shape, suppression, grain and linkability, with cohort/privacy control references. Person anchors are resolved inside the population calculation and never emitted.

## Acceptance scenario

Person P has employment with A and B and allocations 0.6 and 0.5. Unique persons equals 1. A and B each report legal headcount 1; group relationship headcount is 2 while group distinct employed persons is 1. Active relationships equal 2, assignments equal 2 and allocated FTE equals 1.1 under the declared cross-employer method. All published figures retain their distinct names, denominators and disclosure controls.

## Invariants

1. Every figure names perimeter, period and counting method.
2. Person identity is resolved by anchor, never relationship count.
3. Relationships, assignments, positions, persons, FTE and capacity remain distinct measures.
4. Active status is asserted, never inferred.
5. Each classification split names scheme and purpose.
6. Vacancies never create persons.
7. Contractors do not become host employees through assignment.
8. Consolidated measures declare deduplication rules.
9. Suppressed, unknown and zero remain distinct.
10. Small cohorts and repeated releases pass disclosure controls.
11. The landscape has no write path to source masters.
12. Released views pin inputs and carry a reproducible fingerprint.

## Minimal profile shape

Workforce Scope records stable versioned scope id, population predicate, party-role filter, period and boundary convention, measure set with denominator, counting basis, FTE rule and standard-hours reference, deduplication and dual-affiliation rules, consolidation boundary, access grant, projection/cohort-floor references and source pins. Workforce Landscape records view id, scope reference, world/knowledge time, figures with suppression markers, provenance tuple, fingerprint and completeness state.

## Holds

WM-ORG-005 and WM-ORG-016 remain non-canonical, and their composition relation is unapproved. Workforce measurement is an explicit gap in WM-ORG-016 and extension-grade in WM-ORG-002. No shared normative FTE/headcount definition, fixtures or verified crosswalk exists. Privacy/cohort controls were referenced but not independently reviewed here. This checkpoint makes no canonical completeness, installability or publication claim.
