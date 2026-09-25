# EM-LND-01 local synthesis

## Disposition

- Create an **Organizational Structure Landscape profile** over WM-ORG-002, WM-ORG-003, WM-ORG-004 and WM-ORG-016.
- Do not create a catalogue/runtime identifier.
- OrganizationLandscape is a deterministic projection; StructureAxis is a governed profile construct; StructureSnapshot is an immutable generated artifact.

## Boundary

The profile reads authoritative units and hierarchy/reporting edges, teams and memberships, positions and reporting relations, and assignments. It creates none of them and has no write path. Changes always go through the owning model.

A view is computed from axis set, world time, record time, root, depth and disclosure class. It pins constituent versions/digests and has its own output digest for reproducibility, but this artifact identity does not make it a new business aggregate.

## Axis semantics

- Administrative: unit-to-unit managerial containment; one parent per interval; acyclic.
- Functional: unit/post reporting or affiliation; multiple edges allowed when declared; acyclic only when the chosen profile requires hierarchy.
- Project: agent-to-team membership plus separately governed team nesting; membership is many-to-many and not a hierarchy.
- Supervisory: assignment/post/agent reporting; one effective supervisor per assignment and axis after declared precedence.

Cardinality and cycle rules apply per axis and validity interval, never to the union of all edges.

## Invariants

1. Every edge has an axis identifier and world-time interval.
2. Validation uses an axis-scoped rule-set version.
3. Person, Unit, Team, Position and Assignment are references; views do not copy their master records.
4. One world-time/record-time pair applies consistently across all constituent models.
5. A view is refused when any source cannot reconstruct the requested horizon.
6. Views are immutable, digest-identified, reproducible and marked non-reimportable.
7. Scenario facts never mix with authoritative facts.

## Acceptance result

Two assignments of one person can appear on different project and supervisory axes without violating a global single-manager rule. A future unit reparenting produces reproducible pre-change, post-change and historically-known-at views while retaining one person identity and the original assignment histories.

## Holds

All four bases remain `publishableCanonical: false`. Cross-model reconstruction horizons and crosswalks are not yet verified. Scenario branching is unsupported by the source models and must remain fixed to `authoritative` until a planning extension is designed. Axis vocabularies and hierarchy rules need profile fixtures. This checkpoint is not an installable release.
