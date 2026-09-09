Research only the decision core of WM-KNW-010 Decision / Rationale.

- Use the exact registry identity and output `entry_kind` `aggregate`.
  `standalone-mm` in the frozen registry is a record-plane planning class, not
  an allowed subject-model entry kind. The aggregate root is the governed
  decision content: the issue resolved, considered alternatives, evaluation,
  selected outcome and linked rationale.
- The `model` block must describe the boundary of the final combined
  WM-KNW-010, not merely this split pass. Its purpose, scope statement,
  in-scope list, out-of-scope list and boundary notes must include the complete
  core + reasoning + governance model. Assigned split areas must never appear
  in `out_of_scope`, and the scope statement must not say "this pass". Only
  `structure.bundles`, functions and evidence gathering are limited below.
- Cover stable decision identity and version discriminator; decision type and
  jurisdiction/profile; decision question or problem; objectives and desired
  effects; context, scope and affected subjects; constraints and decision
  rules; candidate alternatives including the no-action option; eligibility
  and exclusion; criteria, measures and weights; evaluation results and
  comparisons; selection, disposition and explicit outcome; unresolved
  conditions and consequences stated as decision content.
- Explicitly distinguish the decision content from the decision-making or
  approval activity (WM-ACT-024), its document/record container (WM-REC-010),
  a legal judgment (WM-POL-021), a claim (WM-KNW-007), cited evidence
  (WM-KNW-008), an executable rule or policy and downstream implementation.
- Do not create detailed bundles for rationale/evidence/argumentation,
  participation/authority, lifecycle, provenance, access, audit or retention;
  those belong to the other split passes. Boundary notes may cite them.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight distinct question kinds.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `dr-core-`.
- Limit functions to framing, registering alternatives, evaluating and
  recording the selected decision outcome. Provide complete schema-valid
  service_layers and coverage objects, but keep them concise; the merger takes
  canonical service layers from `governance`.
- Prefer primary standards and first-party specifications for decision models,
  decision tables and requirements, including OMG DMN where applicable. Keep
  mathematical decision-analysis methods and domain-specific decision rules
  as optional bindings unless their primary sources support broader claims.
