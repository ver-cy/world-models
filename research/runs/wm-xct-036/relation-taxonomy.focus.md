Research the relation taxonomy and semantic-strength boundary for WM-XCT-036
Alias / Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary,
  including assertion endpoints, evidence/confidence, lifecycle and governance.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Define relation kinds with non-overlapping semantics: identifier alias,
  historical identifier, redirect/replacement, exact semantic match, close
  match, equivalent-in-context, probable entity match, explicit negative or
  not-same assertion and strict identity. Do not collapse them into one
  `sameAs` flag.
- Distinguish identifier equivalence, record equivalence, real-world entity
  identity, name/label alias, representation equivalence and referent
  replacement. Make misuse detectable with applicability and counterexamples.
- Treat `owl:sameAs` as a strong formal identity claim, not a convenient generic
  link. Keep SKOS exact/close mappings, schema.org `sameAs`, HTTP redirects and
  canonical links, database aliases and probabilistic match scores as distinct
  projections or neighboring semantics.
- For every relation kind declare directionality, symmetry, reflexivity,
  transitivity, invertibility, semantic strength, allowed endpoint types,
  contextual scope and whether inference is permitted. Do not compute closure.
- Cover explicit not-same separately from unknown, unassessed and absent.
  Include invalid combinations, overclaiming, relation downgrade/upgrade
  requirements, cycles and contradictory relation types.
- Do not own endpoint records, evidence adjudication, matching, data merge,
  redirect execution, reasoning closure, identifier allocation or naming.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-tax-`.
- Prefer primary W3C OWL, RDF and SKOS semantics, schema.org documentation and
  IETF HTTP/link standards.
