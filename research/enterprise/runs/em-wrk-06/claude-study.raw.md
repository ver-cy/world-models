# EM-WRK-06 — Dependencies and Impact Analysis: independent adjudication

## Verdict

WM-XCT-037 does **not** merely cover the edge declaration; as delivered it covers all five candidates in depth, and over-reaches on three. Dispositions:

- **Dependency** — reuse WM-XCT-037, narrowed to the edge assertion, type binding, conditions, epistemics, propagation licence and completeness.
- **DependencyType** — **separate, identifier unassigned.** WM-XCT-037 disclaims authoring the vocabulary in `boundary_notes` yet authors a full kind register with facets, stewardship and supersession (`dep-tech-kind-register`, `dep-tech-govern-kind-register`). Contradiction; extract or delete the disclaimer.
- **CriticalityAssessment** — **profile WM-ACT-034** (reserved). Do not keep `dep-res-criticality-impact` as local doctrine.
- **ImpactScenario** — **separate, identifier unassigned.** This is the "second aggregate" the dossier's own adjudication already names.
- **DependencyEvidence** — **no new model.** Bind WM-KNW-008 (citation), WM-MAT-008 (observation); keep only binding qualifiers inline.

No identifiers allocated.

## Evidence

Dossier-internal, cited from the frozen pack: (1) `out_of_scope` forbids closure, reachability, blast radius and impact execution, while `dep-impact-fn-derive-affected-set`, `dep-res-fn-project-downstream-impact` and `dep-res-fn-derive-resilience-determination` perform them — the recorded "boundary contradiction hold." (2) `dep-tech-edge-identity` and `dep-graph-edge-fact` declare first-class edge identity; `dep-life-weak-identity` declares weak host-dependent identity. (3) `known_omissions` still assigns impact propagation, blast radius, criticality scoring and the typed vocabulary to an "adjacent split" that the bundles deliver. (4) Completeness is independently declared in seven places. (5) Two artifacts key on content digests against `artifact_rules`. (6) Relationship contract empty; `factor_overlap` 0.06 with no aligned IDs. (7) ~15 duplicated source registrations inflate the declared 156.

## Identity/mastership

Independent identity is required where the thing survives the edge and carries its own lifecycle:

- **DependencyType**: yes. Register entries are proposed, adjudicated, published, deprecated, superseded, versioned and stewarded, and exist with zero edges. Retyping an edge is a separate remap record — proof of separation.
- **CriticalityAssessment**: yes, and it is *relational*, not a field: criticality binds edge × dependent purpose × scheme version × authority × validity window, with supersession. Two purposes yield two assignments over one edge.
- **ImpactScenario**: yes. Versioned, citable, frozen-input, superseded, with its own artifacts (scenario spec, affected-set register, trace, disclosure).
- **Dependency**: yes, but WM-XCT-037's own identity strength is unresolved and must be fixed before any identifier guidance is normative.
- **DependencyEvidence**: no. The evidence artifact is mastered by WM-KNW-008 / WM-MAT-008; only mode, method profile, confidence, locator reference and completeness qualify the edge.

Endpoint masters stay external throughout: referenced, pinned, never copied, never mutated.

## Dependency edge/type

Canonical direction is **dependent → prerequisite**; the inverse is *derived, never stored*. Foreign-direction terms are normalized once at import with source term, native direction and reversal flag preserved verbatim; undocumented native direction is rejected, not guessed. Type and direction are mandatory.

Arity: one dependent to one-or-many prerequisites natively; many-to-one and many-to-many as multiple assertions sharing a correlation key. Distinguish composite prerequisite groups (conjunctive) from alternative sets (disjunctive, n-of-m, same-target constraint) and ordered prerequisites. Self-edges, duplicates and reversed shapes are recorded, never silently normalized.

Conditions are guards with an explicit unmet-guard outcome — *inapplicable* versus *failed* — and an absolute prohibition on projecting a guarded edge as unconditional. Lag is a duration pinned to calendar, IANA zone and tz-database release, and is **orthogonal to ordering**: existence, ordering and lag are three axes. Phases: design, development, build, test, deploy, runtime — deploy is a declared local extension with unmapped residue. One endpoint pair may carry several phase-scoped edges with different licences.

## Evidence/epistemics

Five distinguishable states: asserted-present, **asserted-absent** (explicit non-dependency, first-class, scoped, attributed), unknown, not-assessed, unresolved. The SPDX None/NoAssertion versus CycloneDX empty-element inversion is normalized reversibly on import; round-tripping without the normalized state silently converts one into the other.

Determination method — declared, discovered, inferred, attested — is recorded with evidence references (locator, digest, media type, fragment selector) or an explicit no-evidence rationale. No payload is copied. Confidence is producer-asserted with a named, versioned scale; cross-scale arithmetic is blocked, since opaque 0–1 tool confidence and metrological uncertainty are not interconvertible.

## Graph rules

Transitivity is **declared per kind with a recorded basis**; unmarked transitive claims are invalid. Cycles are admissible only by per-kind rule, with cycle witnesses, strongly connected component membership, condensation and a closure-safety marker; unbounded closure over a cyclic subgraph is prohibited and ordering is undefined inside a component. Traversal declares path mode (walk, trail, simple, acyclic), direction, depth, breadth and budget, and always returns stop reasons plus the unexpanded frontier.

Completeness must collapse to **one normative statement**, scoped per subject × kind × phase, never inherited by transitive targets; absence of declaration reads as incomplete; an empty edge set is never exportable as independence.

## Impact scenario

A scenario is a frozen version pinning trigger reference, seed entities and alterations, an immutable graph snapshot with snapshot time and content hash, baseline kind (including explicit none-declared), propagation profile version, analysis mode, analysis time and horizon bands, plus code-list versions. Traversal yields a *candidate* set with exposure flags only; promotion to an affected status requires an assessor determination with justification for every not-affected and reached-not-propagating member. Negative and unknown members are published, never omitted.

Propagation licence is per kind × phase: traversal direction relative to canonical direction, transitivity limit, stop conditions, evidence threshold; withheld by default for co-location and correlation natures; approving role distinct from asserter.

## Criticality/assessment

Every stored criticality, severity or likelihood value binds a published scheme version and its notation. No composite score is computed locally — the objection to multiplying ordinal ranks is decisive. Criticality is an assessment record (WM-ACT-034 profile), superseded rather than overwritten, with review-due derived from the validity window.

## Causality/risk

**Rejected: every graph path is a proven causal chain.** A path licenses *exposure inference* only. Four claim statuses must remain separable: exposure inference, modelled prediction, observed outcome, attributed cause. Attributed cause requires a WM-KNW-007 claim with its own scope, evidence, confidence and acknowledged defeaters, citing the path as evidence — not as proof; unsupported attributions downgrade. PROV `wasInfluencedBy` is not causal. Statutory "indirect effect" and graph distance > 1 are not equivalent. Impact outputs feed WM-KNW-015 risk records; they are not risk determinations and confer no authorisation.

## Time/version/snapshot

Event time, observation time and record/ingestion time stay separate; RFC 3339 with seconds and explicit offset; −00:00 preserved as distinct from Z. Edges carry validity intervals; assertions are append-only with supersession, retraction and tombstones. Projections are stale when snapshot digest, licence profile version or completeness declaration changes, and a stale projection may not support a negative conclusion.

## Acceptance scenario

**API change**: kinds `conforms-to-interface` / `requires-package`, phases build+runtime, licence permits upstream traversal to consumers → affected set A = interface consumers and their transitive build dependents within depth bound.

**Resource delay**: kinds `attaches-to-storage` / `hosted-on`, nature = resource consumption, phase runtime, licence withholds propagation through co-location edges → affected set B = capacity-consuming runtime dependents only.

A ≠ B on the identical snapshot, because kind, phase and licence differ — the discriminator is not topology. One consumer reached only by an inferred edge, plus one unenumerated region, sets completeness = incomplete with named known-unknowns; the answer cannot state "no further impact."

## Invariants

1. Type and direction mandatory. 2. Inverse derived, never stored. 3. Cycles only by per-kind rule. 4. Absence of an edge never proves independence. 5. Negative or no-impact claims require a covering completeness declaration in force. 6. Traversal requires an explicit licence; deny by default. 7. Guarded edges never project as unconditional. 8. Unknown, not-assessed and asserted-absent never collapse. 9. Transitivity only when declared with a basis. 10. No cross-scale confidence arithmetic; no composite criticality score. 11. Likelihood and confidence remain separate fields. 12. Causal attribution requires a separate claim with evidence. 13. Scenario immutable after release; supersede, never edit. 14. Excluded edges report as suppressed, not absent. 15. No write to any endpoint master.

## Minimal model set

WM-XCT-037 (narrowed edge declaration, licence, completeness) + DependencyType register (unassigned) + ImpactScenario (unassigned) + WM-ACT-034 criticality profile + WM-KNW-008 / WM-MAT-008 evidence and observation bindings + WM-KNW-007 causal claim + WM-KNW-015 risk.

## Holds

No identifiers allocated. WM-XCT-037 is a non-canonical single-provider reviewable draft carrying eight publication holds, including unresolved traversal and identity contradictions, an empty composition contract, stale omissions, duplicate source registrations and 156 unverified pins. WM-ACT-034, WM-KNW-007, WM-KNW-008, WM-KNW-015 and WM-MAT-008 are all candidate, boundary-review-required, single-provider. Relation rows unapproved; fixtures and crosswalks absent. No claim of canonical completeness, installability or publication readiness.
