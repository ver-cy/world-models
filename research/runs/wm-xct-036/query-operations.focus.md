Research query, resolution and traversal semantics for WM-XCT-036 Alias /
Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Define current and as-of read, resolve, traverse and compare-assertions
  operations with explicit inputs, outputs, preconditions and failure modes.
- Resolution and traversal accept explicit relation kinds, maximum allowed
  strength loss, context, as-of instant, direction, hop limit and access scope.
  They return every candidate path with edge provenance and never silently
  select a canonical identifier.
- Comparison explains differing authority, relation semantics, confidence,
  context, time, evidence and lifecycle state without adjudicating externally
  owned truth.
- Cover ambiguity, no-answer, truncated traversal, cycles, contradictory
  not-same edges, stale endpoints, hidden evidence and incomplete access.
- Functions calculate, validate or report only: no matching, entailment
  materialisation, redirect execution, endpoint mutation or authorization.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-query-`.
- Prefer primary RDF/SPARQL, temporal, provenance and access-safe query sources.
