# Single frozen semantic audit — EM-WRK-06

You are the sole independent frozen auditor. No tools, browsing, standards claims, identifier invention or registry mutation. This audit runs exactly once and will not be repeated.

Audit the reconciled proposal and artifacts below. Fixed identity decision: Dependency Type Registry and Impact Scenario each need independent identity but remain registry-unassigned; Dependency remains a narrowed WM-XCT-037 edge; Criticality Assessment profiles WM-ACT-034; evidence citation, observation, claim, risk and endpoint masters remain external.

Find material contradictions, missing fields, unenforceable invariants, lifecycle/version/provenance/time/snapshot defects, unsafe inverse/transitivity/cycle/propagation semantics, epistemic and completeness ambiguity, causal or risk boundary leaks, and profile gaps. Known registry/base publication gaps are holds, not artifact defects. Return:
1. Verdict ACCEPT or REVISE.
2. Numbered material defects with exact evidence.
3. Required bounded fixes.
4. One JSON fenced array of additional fixtures with target, id, kind, input, expect and optional expectedCode, covering every defect. Targets must be DependencyTypeRegistry, ImpactScenario, or EM-WRK-06-profile.
5. Explicit identifier decision.
6. Freeze decision: closed, no rerun.


## local-evidence.md
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


## grok-study.raw.md
Verdict: Accept with boundary corrections. Not publication-ready. No identifier is allocated.

Independent roots, identifier-unassigned only: Dependency Type Registry and Impact Scenario. Dependency stays the edge inside narrowed WM-XCT-037. CriticalityAssessment profiles WM-ACT-034. DependencyEvidence is a binding, not a master. Claim stays WM-KNW-007; risk stays WM-KNW-015; observation stays WM-MAT-008; citation stays WM-KNW-008. Endpoints remain foreign masters.

WM-XCT-037 boundary: retain edge declaration, canonical direction, inverse-derivation rule, arity, guards, lag, phase tags, type binding (reference, not catalog), epistemic state, completeness, snapshot pin, and a declarative propagation licence that carries type filter, phase window, lag bound, and unknown-edge policy. Move type vocabulary to the unassigned registry. Move computed affected-set projection to Impact Scenario. Refuse absorption of evidence payload, observation, causal claim, risk, assessment, and endpoint mastership. Resolve the Dependency/Impact contradiction by reference, not by keeping Impact inside the edge work item.

Strongest evidence: an edge can be incomplete while its type is stable; a projection can be computed on a frozen graph without mutating the edge; an assessment can be revised without rewriting the declaration. Keeping type catalog, impact projection, assessment, claim, and risk inside WM-XCT-037 collides with WM-ACT-034, WM-KNW-007, WM-KNW-008, WM-KNW-015, and WM-MAT-008.

Strongest counterexample: if type, phase, and licence collapse into path reachability, an API change and a resource delay on one frozen graph yield the same affected set, and a path through an unknown edge is treated as a proven causal chain. Both results are false.

Identity/mastership. Edge identity is the dependency record pinned to a snapshot. Type identity is a registry entry, versioned separately. Scenario identity is a projection run over a pinned graph, licence set, and change event. Assessment identity stays with WM-ACT-034 and references the edge set. Evidence identity stays external. Over-narrowing risk: a licence that is only a boolean cannot make the two events diverge; the licence must stay declarative and still carry type, phase, lag, and unknown policy, without becoming the scenario.

Edge/type. The edge binds a registry entry; it does not own the vocabulary. Canonical direction is stored. Inverse is derived, never a second master edge, and only where the type marks the relation invertible or symmetric. Arity is binary; multi-party dependence is a set of binary edges. Arity violations are invalid, not low-confidence.

Evidence/epistemics. The edge holds known, unknown, absent, or incomplete, plus confidence. Unknown is an epistemic gap; absent is asserted non-existence. Both lower completeness and block licensed traversal. Confidence pins to WM-KNW-008 citation and WM-MAT-008 observation, not to path length. Citation supports a declaration; observation may ground a citation; neither is the edge.

Graph rules. Guards are activation conditions: a failed guard deactivates traversal without deleting the declaration. Lag is a temporal annotation and does not grant licence. Phase qualifies activation and propagation; cross-phase requires an explicit licence. Transitivity is not default: the type must mark composition eligible, and every participating edge must carry a licence. Cycles may be recorded; the type may forbid them; every run must declare stop, bound, or reject, and must terminate. Propagation limits (depth, type filter, phase filter, licence) are mandatory.

Impact scenario. An unassigned root for a frozen projection under a licence. It is not the edge, not a risk, and not an assessment. Later edge edits do not rewrite a pinned scenario.

Criticality/assessment. Profile only. Scheme parameters (bands, phase window, licence gate) sit on the WM-ACT-034 instance, pinned to snapshot and edge set. Revising the assessment must not rewrite the edge. A scheme that cannot pin a snapshot under that profile is a blocker, not a reason for a new root.

Causality/risk. A licensed path is not a WM-KNW-007 claim. Risk may consume a scenario; it is not computed by the edge. Path existence is rejected as causal proof.

Time/version/snapshot. Affected sets and assessments are invalid without a graph snapshot pin, registry version, and licence version. Live mutation invalidates the projection.

Scenario. Frozen graph: A (API contract) provides B (service); B uses C (resource pool) with lag; B triggers D (batch) under a schedule phase; an unknown B–configures–E edge is present. API change on A, licence limited to interface consumers at contract/runtime phase: affected set is {B}; C excluded by type, D by licence. Resource delay on C, licence limited to capacity consumers at runtime with lag: affected set is {B} under lag; A is not inverse-affected unless inverse derivation is licensed; D is excluded. Sets differ by type, phase, and licence. Completeness falls because of the unknown edge. Neither result is a claim or a risk.

Invariants.
1. Canonical direction is asserted; inverse is derived only if the type permits.
2. Arity is binary; violations are invalid.
3. A failed guard deactivates traversal without deleting the edge.
4. Lag does not grant a propagation or causal licence.
5. Cross-phase propagation requires an explicit licence.
6. Transitivity requires type eligibility and a per-edge licence; default is non-transitive.
7. Propagation must terminate on cycles under a declared policy.
8. Unknown and absent are distinct; both lower completeness and block traversal.
9. Completeness falls if an unknown or incomplete edge lies on a candidate path.
10. Confidence is evidence-bound and snapshot-bound, not path-derived.
11. A scenario result requires a snapshot pin.
12. Propagation stops at licence, phase, depth, or incomplete edge.
13. No graph path is a proven causal chain.
14. Criticality is an assessment output, not an edge attribute.
15. API-change and resource-delay events on one frozen graph must be able to differ by type, phase, or licence.

Minimum model set: narrowed WM-XCT-037 edge; unassigned Dependency Type Registry; unassigned Impact Scenario; CriticalityAssessment as a WM-ACT-034 profile; DependencyEvidence as a binding to WM-KNW-008 and WM-MAT-008. Endpoints, claim, risk, and observation stay foreign.

Blockers: residual Impact or type-catalog ownership in WM-XCT-037; auto-promotion of a path to a claim; unknown edges still traversed; criticality unable to pin a snapshot under the profile; any identifier beyond the two unassigned roots; a licence too thin to separate the two events.


## candidate-allocation-offline-dependency-type-registry/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-WRK-06","proposedName":"Dependency Type Registry","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed dependency-type vocabulary remains identifiable independently of dependency edges and graph snapshots while its type semantics evolve through releases.","versionIdentity":"Changes to endpoint classes, arity, direction, cardinality, phase, cycle, transitivity, guard or propagation rules create immutable registry versions.","independentLifecycle":["draft","reviewed","approved","published","effective","deprecated","superseded","retired"],"mastership":"enterprise dependency-semantics authority"},"boundary":{"owns":["persistent dependency-type-registry identity","dependency-type definitions","canonical direction and endpoint-class constraints","arity and cardinality rules","phase and lag semantics","cycle and transitivity rules","guard, propagation licence and stop-rule templates","release, deprecation and supersession history"],"references":[{"target":"WM-XCT-037","purpose":"Dependency edge and impact semantics"},{"target":"WM-ACT-034","purpose":"Criticality assessment"},{"target":"WM-KNW-008","purpose":"Evidence citation"},{"target":"WM-MAT-008","purpose":"Observation evidence"},{"target":"WM-KNW-015","purpose":"Risk record"}],"excludes":["dependency edge or endpoint identity","evidence payload or observation","impact scenario or traversal result","criticality assessment or causal claim","risk determination or authorization","graph snapshot or completeness assertion"]},"objects":{"DependencyTypeRegistry":{"identity":["dependencyTypeRegistryId"],"required":["name","ownerRef","status"],"optional":["successorRef","retiredAt"],"lifecycle":["draft","reviewed","approved","published","effective","deprecated","superseded","retired"]},"RegistryRelease":{"identity":["dependencyTypeRegistryId","releaseVersion"],"required":["typeDefinitions","validFrom","contentDigest","status"],"optional":["validTo","supersedesRelease"]}},"invariants":["Dependency type exists independently of any edge and may have zero instances.","Every dependency edge pins one exact type-registry release and canonical type.","Canonical direction is dependent to prerequisite unless the pinned type explicitly defines otherwise.","Inverse edges are derived and never stored as duplicate facts.","Endpoint classes, arity, cardinality and phase constraints are explicit.","Cycles are allowed only by type-specific rules.","Transitivity requires a declared basis and is never inferred from topology.","Guards never project as unconditional dependencies.","Propagation licences are deny-by-default and scoped by type, phase and direction.","Lag semantics pin calendar, zone and timezone database release.","Type deprecation never deletes historical edges.","Registry releases are immutable and superseded explicitly."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","WM-XCT-037 type, impact and identity contradictions require normative resolution.","Package conversion and live verification are pending."]}


## candidate-allocation-offline-dependency-type-registry/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Dependency Type Registry","cases":[{"id":"zero-edge-type","kind":"positive","input":"A new regulated dependency type is published before any edge uses it.","expect":"The type remains valid with independent identity and lifecycle."},{"id":"phase-specific-types","kind":"positive","input":"One endpoint pair has build and runtime dependencies with different rules.","expect":"Separate typed edges pin the same registry release and phases."},{"id":"deprecated-type","kind":"positive","input":"A type is superseded by a refined successor.","expect":"Historical edges retain the prior type version."},{"id":"duplicate-inverse","kind":"negative","input":"Both canonical and inverse edges are stored as independent facts.","expect":"The duplication is rejected."},{"id":"topology-implies-transitive","kind":"negative","input":"Transitivity is inferred solely from graph shape.","expect":"The inference is rejected."},{"id":"unguarded-projection","kind":"negative","input":"A guarded dependency is projected as unconditional.","expect":"The projection is rejected."}]}


## candidate-allocation-offline-dependency-type-registry/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## candidate-allocation-offline-impact-scenario/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-WRK-06","proposedName":"Impact Scenario","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A frozen impact-analysis scenario remains identifiable across later graph, type and propagation changes while retaining its trigger, assumptions and outputs.","versionIdentity":"Changes to trigger, seeds, graph snapshot, registry, propagation profile, horizon or assumptions create a successor scenario rather than mutating a released one.","independentLifecycle":["draft","executed","reviewed","released","stale","superseded","withdrawn"],"mastership":"impact-analysis authority"},"boundary":{"owns":["persistent impact-scenario identity","trigger and altered seeds","immutable graph snapshot and digest","baseline and horizon","type-registry and propagation-profile pins","assumptions and analysis mode","candidate exposure output and frontier","staleness, supersession and withdrawal history"],"references":[{"target":"WM-XCT-037","purpose":"Dependency graph snapshot and edges"},{"target":"WM-ACT-034","purpose":"Assessment promoting exposure to affectedness"},{"target":"WM-KNW-008","purpose":"Evidence citation"},{"target":"WM-MAT-008","purpose":"Observation"},{"target":"WM-KNW-007","purpose":"Causal attribution claim"},{"target":"WM-KNW-015","purpose":"Risk record"}],"excludes":["dependency type, edge or endpoint identity","evidence payload or observation identity","criticality assessment or affectedness determination","causal claim or risk determination","authorization or source-master mutation","automatic negative conclusion from missing edges"]},"objects":{"ImpactScenario":{"identity":["impactScenarioId"],"required":["trigger","seeds","graphSnapshotRef","typeRegistryReleaseRef","propagationProfileRef","analysisMode","horizon","status"],"optional":["baselineRef","assumptions","exposureSet","cycleWitnesses","unexpandedFrontier","completenessRef","successorRef"],"lifecycle":["draft","executed","reviewed","released","stale","superseded","withdrawn"]}},"invariants":["Released impact scenarios are immutable and corrections create successors.","Every scenario pins graph snapshot, type registry, propagation profile, horizon and code lists.","Traversal requires an explicit propagation licence.","Cycle traversal is bounded and reports witnesses, stop reasons and frontier.","Candidate exposure never becomes affected or not affected without assessor determination.","Negative conclusions require covering completeness for subject, kind and phase.","A stale scenario cannot support a negative conclusion.","Graph paths never prove causal chains.","Suppressed or omitted edges remain visible with reason codes.","Event, observation and ingestion times remain distinct.","Changes to graph, registry, profile or completeness can stale prior output.","No analysis writes to endpoint or dependency masters."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Completeness, traversal and staleness contracts require canonical approval.","Package conversion and live verification are pending."]}


## candidate-allocation-offline-impact-scenario/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Impact Scenario","cases":[{"id":"api-change","kind":"positive","input":"An API change traverses interface and package dependencies through build and runtime phases.","expect":"The scenario records typed traversal, stop reasons and candidate exposure."},{"id":"resource-delay","kind":"positive","input":"A resource delay traverses runtime capacity dependencies and stops at co-location edges.","expect":"The affected set differs from the API scenario because type and licence differ."},{"id":"stale-graph","kind":"positive","input":"A covering graph snapshot changes after release.","expect":"The scenario becomes stale without rewriting its original output."},{"id":"path-is-cause","kind":"negative","input":"Every traversed graph path is asserted as proven causal chain.","expect":"The causal inference is rejected."},{"id":"empty-means-safe","kind":"negative","input":"No returned edges is treated as no impact without completeness evidence.","expect":"The negative conclusion is rejected."},{"id":"analysis-mutates-endpoints","kind":"negative","input":"Impact traversal writes affected status into endpoint masters.","expect":"The mutation is rejected."}]}


## candidate-allocation-offline-impact-scenario/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}
