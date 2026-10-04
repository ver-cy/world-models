**Verdict.** Accept with conditions. Neither KnowledgeLandscape nor DecisionDependencyView requires independent catalogue or runtime identity. Landscape may hold only a thin administrative profile handle for scope, authority, review, and retrieval policy. The view is a reproducible projection of pinned source releases plus query rules. Assertions stay mastered by their source models. Reject the proposal if any condition below is treated as optional.

**Strongest evidence.** The named models already partition mastership: WM-KNW-006 Concept/Term, WM-KNW-007 Claim, WM-KNW-008 Citation, WM-KNW-010 Decision/Rationale, WM-REC-001 Document/Record, WM-REC-010 Decision Record, WM-KNW-018 Concept Scheme. A landscape that only declares scope and policy, and a view that only projects pinned releases, can be governed without becoming a peer of those types. Citation-as-reference, scheme-qualified terms, and dated decision status already separate relation, truth, label, and validity. Adding catalogue identity would create a second master for the same assertions.

**Strongest counterexample.** If the landscape is stored as if it were a WM-KNW-018 scheme, or the view as if it were a WM-REC-010 record, consumers will cite “the landscape” or “the view” as if those were mastered records. A later source retraction then attaches to the projection instead of to WM-REC-001 / WM-KNW-007, and two decisions that share a citation become fate-coupled. That single identity creep falsifies every other rule in the proposal.

**Identity / mastership.** No new catalogue or runtime identifier for either candidate. Concept, term, claim, citation, decision, document, record, and scheme identifiers remain those of the source models. The landscape handle is administrative and non-mastering: it must not own assertions, must not act as a concept scheme, and must not decide validity. The view fingerprint is coordinates only: query rules, pinned releases of the source models, evaluation time. If audit needs “which landscape was in force,” bind the handle and pins onto the existing WM-REC-010; if a run must be evidenced, persist a WM-REC-001 record of the request, not a new view type.

**Semantic graph.** Nodes that may appear are only those seven named types. Landscape is not a node class. The view is a derived path set (decision → rationale → claim/citation/document/concept) computed from pins. Derived edges are references, not new assertions. Semantic relation never implies identity. Citation never implies truth. Closures are computed sets, not objects. The view must not mint identifiers in any named model.

**Impact propagation.** Retraction or claim rebuttal is a dated observation on the source (WM-REC-001 or WM-KNW-007), visible to citing WM-KNW-008 edges. Impact is notify-and-recheck to citing WM-KNW-010 / WM-REC-010 objects. Recheck is mandatory notice, not mandatory status change. Decision status remains mastered only by the decision and its record. Shared citation never couples decision fate. Landscape and view must not write back.

**Terminology conflict.** Term identity is scheme-qualified under WM-KNW-018. Surface label is not a key. Two schemes may both use “Portfolio” with incompatible meanings; inclusion of both schemes does not unify namespaces. Indexes and counts that drop scheme qualification are false merges and are blocked or flagged. A dated terminology-conflict observation may be recorded; it is not an identity operation and creates no concept. Paraphrase does not merge or mint.

**Missing source and uncertainty.** A WM-KNW-007 claim with no WM-KNW-008 citation to a WM-REC-001 record remains a claim. Absence of evidence is uncertainty, not falsity and not licence to invent a source. The decision that uses the claim is not automatically invalid. Every projection must show the claim as unevidenced. Later citation is a new source assertion. Later rebuttal is a dated observation plus notify-and-recheck, not auto-invalidation.

**Rights / inference controls.** Indexes, closures, counts, and summaries inherit source access on every participating node, intersected with landscape retrieval policy; most-restrictive wins. Enforcement is at generation. Forbidden: paraphrase of restricted content; inferred identity; path closure into a restricted node; a count that differs from caller-visible cardinality; any wording that two visible decisions share a source when that source is restricted.

**Time / version.** Retraction, rebuttal, supersession, and remains-effective are dated acts on source-mastered objects. A pin taken before retraction keeps pre-retraction state; later observations do not rewrite historical pins. Scheme version bounds which label–meaning pair is in force. Remains-effective after retraction is an explicit dated act, not a default.

**Scenario.** T0: Record R1 cited by decisions D1 and D2 via citations C1 and C2; both decisions effective. T1: R1 retracted; dated observation on R1; notify-and-recheck to D1 and D2; neither auto-invalidated; citations remain as reference facts. T2: D1 superseded by explicit dated act. T3: D2 explicitly remains effective by dated affirmation (retraction noted). Pin P0 shows both effective and both citing R1. Pin P3 shows R1 retracted, D1 superseded, D2 effective, C1 and C2 still projected. Restricted-summary test: caller sees D1 and D2 titles, not R1. Fail if the summary says they share a source, emits a shared-source count of one, paraphrases R1, or closes a path naming R1. Pass if citation targets are redacted or omitted and no aggregate discloses correspondence.

**Invariants.**

1. Semantic relation never implies identity.
2. Citation never implies truth.
3. Shared labels never justify concept merge.
4. Term identity is scheme-qualified; label is not a key.
5. Each assertion remains mastered only by its source model.
6. Landscape and view mint no identifiers in the seven named types.
7. Neither candidate receives catalogue or runtime identity.
8. Absence of citation is uncertainty, not falsity or invented evidence.
9. Unevidenced claims remain visible as unevidenced.
10. Terminology conflict yields a dated observation only.
11. Retraction or rebuttal yields dated observation plus notify-and-recheck; decisions are not auto-invalidated.
12. Two decisions citing one source may diverge (superseded vs remains-effective).
13. Pins reproduce source-release state; later observations do not rewrite pins.
14. Views and landscapes never write back assertions.
15. Indexes, closures, counts, summaries inherit source restrictions; most-restrictive wins.
16. Restricted correspondence cannot leak by paraphrase, inference, path, aggregation, or search summary.
17. Profile inclusion of multiple schemes does not unify namespaces.
18. Remains-effective after retraction is an explicit dated act.

**Minimum profile shape.** Landscape declaration (non-catalogue): referenced schemes and included source classes; governing authority; review cadence; retrieval policy that inherits source access and forbids leak by paraphrase or inference; explicit non-mastering flag; no assertion store; no merge authority; no decision-validity authority. View spec (non-catalogue): query rules over decisions, citations, claims, and records; pinned source releases; evaluation timestamp; projection contract of dated observations and notify-and-recheck with no auto-invalidation; every index, closure, count, and summary carries source restrictions.

**Blockers.** Treat landscape as a concept scheme. Treat the view as a decision record. Materialize view edges as citations owned by the view. Merge same-label concepts across incompatible schemes. Auto-invalidate decisions on source retraction. Compute summaries or indexes before access intersection. Leave remains-effective implicit after retraction. Specify the pin as a new view or catalogue identifier. Invent any catalogue or runtime code.

**Independent identity.** Neither candidate requires it. Policy-handle and pin-fingerprint are not assertion identity.
