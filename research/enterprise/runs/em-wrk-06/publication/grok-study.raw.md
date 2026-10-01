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
