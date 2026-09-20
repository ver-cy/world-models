Research only the semantic core of WM-KNW-006 Concept / Term.

- Treat the aggregate root as a stable concept identity and the terms,
  designations, lexical forms, definitions, notes and usage examples as
  subordinate or referenced descriptions. Use output `entry_kind` `entity`;
  `standalone-mm` in the registry is a planning class, not an allowed output
  entry kind.
- The `model` block must describe the boundary of the final combined
  WM-KNW-006, not merely this split pass. Its purpose, scope statement,
  in-scope list, out-of-scope list and boundary notes must include the complete
  core + relations + governance model. Assigned split areas must never appear
  in `out_of_scope`, and the scope statement must not say "this pass". Only
  `structure.bundles`, functions and evidence gathering are limited below.
- Cover identity and identifiers; preferred/admitted/deprecated terms;
  language, script and grammatical form; definitions and explanatory notes;
  scope and subject domain; referents/examples; usage context and audience;
  multilingual equivalence only at the designation/sense boundary.
- Explicitly distinguish concept, term/designation, lexical entry, word form,
  sense, referent/real-world entity, class/type and free-text keyword.
- Do not create bundles for concept schemes, hierarchical/associative
  relations, cross-scheme mappings, lifecycle, governance, provenance, access
  or quality: those belong to other split passes. Boundary notes may cite them.
- Target 2-3 bundles, 4-7 layers and 9-13 findings with 3-5 questions each.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `ct-core-`.
- Use at least eight distinct question kinds across the pass. Keep functions
  limited to core create/read/use operations. Provide the full required
  service_layers and coverage objects for validation, but keep them concise;
  the merge will take canonical service layers from the governance pass.
- Prefer primary standards and first-party specifications such as ISO/IEC or
  ISO terminology principles where publicly verifiable, W3C SKOS/RDF/OWL,
  W3C OntoLex-Lemon, and relevant terminology-exchange specifications. Never
  invent access to paywalled clauses.
