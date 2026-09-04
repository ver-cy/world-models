Research the assertion envelope and endpoint-reference boundary for WM-XCT-036
Alias / Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary,
  including relation semantics, evidence/confidence, lifecycle and governance.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Model an identified, versioned assertion between externally owned source and
  target references. The assertion has weak host-dependent identity and does
  not merge, rename, allocate or take ownership of either endpoint.
- Define assertion identity, issuer, creation and effective times, source and
  target roles, endpoint locators, namespace/scheme, tenant/Dimension,
  jurisdiction, purpose and applicable entity/type scope.
- Distinguish the assertion's own identifier from identifiers cited at its
  endpoints. Cover source/target version pins, composite keys, endpoint
  resolution status, immutable snapshots versus live references, and explicit
  provenance locators without importing the endpoint records.
- Cover one-to-one, one-to-many, many-to-one and conditional mappings. State
  how order, membership and conditions are represented rather than hiding
  cardinality in repeated fields.
- Cover missing, unresolved and dangling endpoints, self links, duplicate
  assertions, conflicting endpoint versions and malformed references. Separate
  absence from explicit unknown and explicit not-same.
- Keep relation classification and formal equivalence closure outside this
  focus: reference them in the complete model boundary but do not duplicate
  their findings here.
- Do not own identifier allocation, naming, endpoint records, matching engine,
  data merge, redirect execution, reasoning closure, authorization or audit.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-asrt-`.
- Prefer primary W3C RDF/OWL resource semantics, IETF URI/IRI and link
  standards, and identifier authority guidance.
