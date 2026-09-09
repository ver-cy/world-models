Research the format-neutral assertion envelope and endpoint boundary for
WM-XCT-037 Dependency / Impact.

- Use the exact frozen registry identity `vr.wm-xct-037`, model ID
  `WM-XCT-037`, name `Dependency / Impact`, and `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-037 boundary,
  including typed dependencies, conditions, evidence, lifecycle, graph and
  impact semantics, governance and operations. Never mention a split, pass,
  sibling pass or partial delivery in model, coverage or adversarial prose.
- Model an identified, versioned dependency assertion between externally owned
  dependent/consumer and prerequisite/provider endpoints. State the canonical
  direction unambiguously and preserve any source vocabulary's direction.
- The assertion has weak host-dependent identity and does not allocate, own,
  copy, rename, merge, configure, deploy, invoke or monitor either endpoint.
- Define assertion identity, issuer, declared-at and effective times, dependent
  and prerequisite roles, endpoint locators, namespace/scheme, adopting
  Dimension, tenant, jurisdiction, purpose, applicable endpoint types and scope.
- Distinguish assertion identity from endpoint identity. Cover endpoint and
  assertion version pins, immutable snapshots versus live references, revision
  compatibility, unresolved/dangling endpoints and stale observations.
- Cover one-to-one, one-to-many, many-to-one, many-to-many and ordered
  dependencies; composite prerequisites; self-dependencies; duplicates;
  direction reversal; parallel assertions and explicit non-dependency.
- Separate absent, unknown, not-assessed, unresolved and explicitly independent
  states. Silence must never become proof that no dependency exists.
- Do not own dependency-type vocabularies, graph closure, impact computation,
  matching/discovery, endpoint state, change execution, authorization or audit.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `dep-core-`.
- Prefer primary W3C RDF/PROV, IETF URI/link, OASIS relationship-model and
  identifier-authority sources. Record unverified assumptions as gaps.
