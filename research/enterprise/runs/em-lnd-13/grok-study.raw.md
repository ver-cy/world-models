# EM-LND-13 — Grok independent review

**Verdict.** Accept. Neither DataLandscape nor AnalyticalLineageView requires independent identity. DataLandscape is a versioned governed snapshot-projection over WM-DAT-001 Dataset, WM-DAT-005 Pipeline, WM-DAT-006 Lineage, WM-DAT-008 Data Product, plus schema, measurement, Metric Definition, and Report/Statement definition. AnalyticalLineageView is an issued-at-pinned profile of WM-DAT-006. Reject live-unversioned-filter landscapes and title-as-identity.

**Strongest evidence.** Dual identity would split mastership of the same Dataset or Lineage edge. Formula-change impact rides on versioned Metric Definitions and pinned Report issues, not view identity. Rights inheritance works only if the projection is not a second rights master.

**Strongest counterexample.** An auditor needs “the official landscape at board-pack date.” Later WM-DAT-006 edges may gain capture methods, revised confidence, or new links. That looks like a demand for view identity; it is issued-at pinning plus an immutable observed-set on a handle. Independent identity would fork lineage mastership and stop impact at “the landscape changed.” If published, identity sits on WM-DAT-008 whose payload is the projection.

**Identity/mastership.** Neither candidate is a master class. Mastership stays with Dataset, Pipeline, Lineage, Data Product, schema, measurement, Metric Definition, and Report/Statement definition. A handle binds access, issued-at, completeness perimeter, and rights stamp only; it must not mint a parallel identifier space. A reusable lineage view that owns edges duplicates WM-DAT-006.

**Definition/run separation.** Definitions (Metric Definition, Report/Statement definition, Pipeline, analysis definition) are disjoint from occurrences (observations, report issues, pipeline runs, studies, claims). A formula/method change yields a successor Metric Definition; it does not mutate the prior definition or rewrite issued reports or claims.

**Lineage/impact.** Every WM-DAT-006 edge records type, granularity, capture method, producer, confidence, and evidence. Endpoints address definition versions or run/issue instances, never titles. Impact returns two sets: affected definitions, and concrete issues/runs pinned to a prior method. AnalyticalLineageView may select and require attributes; it must not invent edges, alter evidence, or change type or granularity.

**Comparability.** Same KPI title does not establish comparability. Compare formula/method, units, population, dimensions, and null policy; mismatch on any axis blocks numeric comparison.

**Reports/analytics.** A Report issue pins definition versions, input Dataset/Data Product versions, issue time, and observed completeness/freshness. Conclusions, studies, and claims retain stale and incomplete markers from those pins; projection must not drop them.

**Completeness/freshness.** Missing edges mean unobserved, not absent, unless the query sits inside a declared closed completeness perimeter. Perimeters are explicit, scoped, time-bounded, and attached to a projection/profile issue. Emptiness is not completeness. Freshness is capture-time relative to issued-at.

**Access/projection.** DataLandscape inherits the most restrictive applicable source rights from the pinned source set and cannot create rights sources do not confer. Access computed on a live source set is non-reproducible.

**Scenario.** Metric Definition M uses method F1 with units, population, dimensions, and null policy recorded. Report/Statement definitions Rd1 and Rd2 bind M. Issues I1 and I2 are released from Rd1 under F1; I3 from Rd2 under F1. Formula changes to F2 (title unchanged), minting successor M*. Affected definitions: M, M*, Rd1, Rd2, any Pipeline that materializes M. Concrete releases I1–I3 remain bound to F1 and must not be rewritten. Later F2 issues are a different method; title match does not make I1 comparable to them. Edges Dataset/Pipeline/Data Product → Metric Definition version → Report/Statement definition → report issue carry the six required attributes, distinguishing F1 from F2. Impact is traced on the masters; projection and profile only display a governed subset. A third report definition with no edge to M is unobserved unless a closed perimeter covers report definitions.

**Invariants.**
1. Neither candidate is a master class; mastership stays with Dataset, Pipeline, Lineage, Data Product, schema, measurement, Metric Definition, and Report/Statement definition.
2. A handle binds access, issued-at, perimeter, and rights only; it is not enterprise identity.
3. Definitions are disjoint from observations, issues, runs, studies, and claims.
4. A formula/method change yields a successor Metric Definition; prior versions and issued reports are not mutated.
5. Every lineage edge records type, granularity, capture method, producer, confidence, and evidence; endpoints address versions or issues/runs, never titles.
6. Missing edge means unobserved unless a closed completeness perimeter applies to that projection issue.
7. Closed perimeters are explicit, scoped, and time-bounded; emptiness is not completeness.
8. KPI title equality does not establish comparability; compare formula/method, units, population, dimensions, and null policy.
9. Report issues pin definition versions, inputs, and times.
10. Conclusions retain stale and incomplete markers; projections must not drop them.
11. Projections inherit source rights only; they cannot amplify rights.
12. AnalyticalLineageView must not invent edges, alter evidence, or change type or granularity.
13. Impact returns affected definitions and affected concrete issues/runs as two sets.
14. Schema and measurement bound metric inputs.

**Minimum profile shape.** AnalyticalLineageView (WM-DAT-006 profile, no new class): issued-at; completeness-perimeter {open|closed, scope, bound-time}; selection overlay {allowed edge types, granularities, producers, capture methods}; required edge attributes {type, granularity, capture method, producer, confidence, evidence}; endpoints to masters only, each with a definition-vs-run qualifier; incomplete-edge set; unobserved-marker; freshness relative to issued-at; rights-inheritance stamp.

DataLandscape (snapshot-projection, no new class): issued-at; included master-object set; attached profile issue; completeness-perimeter; freshness markers; inherited rights; stale/incomplete markers on included reports and conclusions.

**Blockers.** Title-as-identity or unversioned Metric Definitions. Report issues that do not pin inputs and times. Lineage edges missing any of the six attributes. Handles treated as master IDs. Live unversioned landscapes. Inferring absence from missing edges without a closed perimeter. Comparability keyed on KPI title. Profiles that invent or rewrite edges. Conclusions that drop stale/incomplete markers. Live-set access; demote any existing Landscape or AnalyticalLineageView master IDs to handles.
