# EM-WRK-06 local synthesis

## Disposition

- Narrow and reuse WM-XCT-037 for the identified dependency assertion, type binding, conditions, epistemic qualifiers, completeness and declarative propagation licence.
- Propose identifier-unassigned **Dependency Type Registry** because types have their own proposal, approval, release, deprecation and supersession lifecycle independent of edges.
- Propose identifier-unassigned **Impact Scenario** because it freezes trigger, graph snapshot, propagation profile, assumptions and analysis output as a citable lifecycle object.
- Profile **Criticality Assessment** on WM-ACT-034.
- Reuse WM-KNW-008 and WM-MAT-008 for evidence citations and observations; DependencyEvidence remains an inline binding, not a new root.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

A Dependency is an identified, versioned assertion distinct from both endpoint masters. Endpoints remain externally owned and are pinned by qualified reference without copying or mutation.

Dependency Type exists with zero edges, is stewarded and versioned, and survives edge deletion. Impact Scenario survives graph changes as a frozen, supersedable analysis release. Criticality Assessment has independent assessment identity through WM-ACT-034. Evidence payloads remain in their producing systems; the edge stores only qualified references.

WM-XCT-037 currently contradicts these boundaries by disclaiming type-vocabulary authorship and impact computation while implementing both. The reused mixin must be narrowed before publication.

## Dependency edge and type

Canonical direction is dependent to prerequisite. Inverses are derived and never stored as separate facts. Import preserves the source term, native direction and reversal flag; unknown direction is rejected.

Type and direction are mandatory. Types declare endpoint classes, arity, phase, cardinality, cycle permission, transitivity, guards, propagation licence and stop rules. Composite prerequisite groups and alternatives remain explicit. Existence, ordering and lag are separate axes.

Lag pins duration semantics, calendar, IANA zone and timezone database release. One endpoint pair may carry several phase-scoped dependency assertions with different types and propagation licences.

## Evidence and epistemics

Asserted-present, asserted-absent, unknown, not-assessed and unresolved are distinct states. An empty edge set is never interpreted as independence without an in-force completeness statement for the relevant subject, kind and phase.

Determination method distinguishes declared, discovered, inferred and attested assertions. Each carries an evidence reference or explicit no-evidence rationale, named confidence scale, limitations and falsification condition. Evidence content is not copied.

Completeness is asserted once per subject, dependency kind and phase, includes known unknowns and never propagates to transitive targets.

## Graph rules and impact scenario

Transitivity is declared per type with a recorded basis; it is never inferred from graph shape. Cycles are allowed only by the type rule. Traversal over cyclic components is bounded and returns cycle witnesses, stop reasons and the unexpanded frontier.

An Impact Scenario pins trigger, altered seeds, immutable graph snapshot and digest, baseline, type-registry version, propagation-profile version, analysis mode, horizon and code lists. Traversal produces a candidate exposure set. Promotion to affected or not-affected requires an assessor determination, and negative results require justification.

Propagation licences are deny-by-default and type-and-phase scoped. They state traversal direction relative to canonical edge direction, depth/transitivity limits, stop conditions and evidence threshold. Co-location and correlation do not propagate by default.

## Criticality, causality and risk

Criticality is purpose-relative and scheme-qualified. The WM-ACT-034 profile binds edge, dependent purpose, scheme version, authority and validity interval. Severity, likelihood, confidence and uncertainty remain separate; ordinal scales are not multiplied into an invented composite.

A graph path supports exposure inference only. Modelled prediction, observed outcome and attributed cause remain separate claim states. Causal attribution requires a WM-KNW-007 claim with evidence, scope, confidence and defeaters. Impact outputs may feed WM-KNW-015 risk records but do not become risk determinations or authorization.

## Time, version and snapshot

Event, observation and ingestion times remain distinct. Dependency assertions are append-only and corrected through supersession, retraction or tombstone. Impact outputs become stale when the graph snapshot, type registry, propagation profile or covering completeness declaration changes.

A stale scenario may not support a negative conclusion. Omitted or suppressed edges are reported with reason rather than silently disappearing.

## Acceptance result

On the same frozen graph, an API change traverses interface and package dependencies through build and runtime phases, while a resource delay traverses runtime capacity dependencies and stops at co-location edges. The affected sets differ because type, phase and propagation licence differ, not merely topology. One inferred edge and one unenumerated region make completeness incomplete, so neither analysis may claim no further impact. Neither path is treated as a causal chain.

## Required invariants

1. Dependency type and canonical direction are mandatory.
2. Inverse edges are derived, never duplicated.
3. Cycles are allowed only by type-specific rules.
4. Absence of an edge never proves independence.
5. Negative conclusions require a covering completeness statement.
6. Traversal requires an explicit propagation licence.
7. Guarded edges never project as unconditional.
8. Unknown, not-assessed and asserted-absent never collapse.
9. Transitivity requires a declared basis.
10. Confidence scales are never combined without a mapping.
11. Likelihood, severity, criticality and confidence remain distinct.
12. Causal attribution requires a separate evidenced claim.
13. Impact scenarios are immutable after release.
14. Suppressed edges remain visible with stop reasons.
15. No analysis writes to endpoint masters.

## Holds

Dependency Type Registry and Impact Scenario have no registry allocations. WM-XCT-037 contains unresolved contradictions between its declared boundary and implemented type/impact functions, plus conflicting weak versus first-class identity statements, duplicate completeness rules and unverified pins. Relations remain unapproved and adjacent drafts remain non-canonical single-provider work. No installability or publication-readiness claim is made.

## Provider reconciliation and frozen-audit remediation

Grok accepted the boundary with corrections. The sole Claude audit retained the identity decision and found 16 material artifact defects. Revision 2 closes all defects without rerun: type and propagation releases are explicit, inverses and heterogeneous composition are licensed, epistemic states block traversal deterministically, snapshots are externally minted and reproducibly pinned, scenario bytes are immutable with status overlays, outputs remain candidate exposure, and the WM-ACT-034 profile separates affectedness from criticality. Publication remains held by registry allocation and base/relation readiness.
