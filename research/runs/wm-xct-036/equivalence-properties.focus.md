Research formal and contextual relation properties for WM-XCT-036 Alias /
Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Define declared properties and constraints for each relation kind rather than
  assuming all links are symmetric or transitive. Cover inverse, composition,
  domain/range, reflexivity, functionality/cardinality and non-equivalence.
- Contrast OWL identity, SKOS exact/close/broad/narrow/related mappings,
  identifier redirects/replacements, schema.org sameAs and probabilistic record
  linkage. Preserve the strongest semantics actually asserted and no stronger.
- Cover contextual and temporal equivalence by Dimension, jurisdiction,
  purpose, data version and effective interval. Define incompatibility between
  contexts and controlled relation weakening or strengthening.
- Define when A~B and B~C may or may not imply A~C, when a mapping can be
  inverted, how a weak or conditional edge constrains a path, and how
  confidence or authority may be reported without inventing certainty.
- Cover contradiction detection, explicit not-same constraints, invalid
  relation combinations and explosion/contagion risk from one false strong
  identity assertion. Closure is external; this model only validates or reports
  declared semantics.
- Do not execute reasoning, traversal, entity resolution, redirect handling or
  master-data merge.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-prop-`.
- Prefer primary W3C OWL, RDF and SKOS specifications and relevant schema.org
  documentation.
