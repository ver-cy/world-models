Research graph, traversal and cluster-boundary semantics for WM-XCT-036 Alias /
Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover traversal policies, maximum depth, cycle and repeated-node handling,
  path provenance, weakest-edge reporting, contradiction markers and the rule
  that traversal does not silently materialize inferred identity assertions.
- Cover equivalence clusters as derived views owned by an external reasoning or
  master-data policy: membership evidence, calculation rule and version,
  temporal snapshot, stability and reproducibility.
- Treat canonical representatives as external policy decisions. Record the
  selecting authority, rule, version, scope and effective interval without
  rewriting endpoint identities or converting preference into equivalence.
- Cover cluster split and merge lineage, retained aliases, historical member
  lookup, impacted assertions and downstream-reference impact reports. Preserve
  prior membership and representative decisions.
- Cover false-strong-edge contamination, cycles, disconnected subgraphs,
  contradictory not-same edges inside a cluster, stale members, orphaned
  representatives and maximum-path/hop safeguards.
- Functions may calculate, validate or report candidate paths and impacts, but
  must not execute ontology reasoning, endpoint mutation, entity resolution,
  master-data merge or redirect handling.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-graph-`.
- Prefer primary W3C OWL/RDF/SKOS semantics and graph-provenance standards.
