Research only control linkage, implementation and effectiveness for WM-XCT-027
Risk / Control.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-027 boundary,
  including risk projection, control linkage/effectiveness and governance.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover authoritative control reference and revision; objective and control
  type; preventive/detective/corrective and manual/automated classifications;
  scope/applicability; risk-to-control linkage semantics; claimed treatment or
  reduction mechanism; owner/operator/tester references; design status;
  implementation status; operating status; frequency/triggers; dependencies;
  evidence references; test/assessment method and time; exceptions,
  deficiencies and compensating controls; coverage many-to-many relations;
  effectiveness conclusion, confidence and expiration; residual linkage.
- Keep the control catalogue, policy text, procedure, technical configuration,
  test case/result, evidence object, issue/remediation workflow and audit record
  in their owning models. A reference or digest binding here never grants
  ownership of those lifecycles.
- Distinguish existence, design adequacy, implementation, operation and tested
  effectiveness. Never infer effectiveness from documentation, map presence or
  absence of incidents, and never make a control framework mapping equal proof
  of conformance.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight question kinds.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `rctl-control-`.
- Limit functions to linking/unlinking controls, recording applicability and
  implementation assertions, binding evidence, recording effectiveness and
  explaining residual contribution. Provide complete valid service_layers and
  coverage, but the merger takes canonical service layers from `governance`.
- Prefer primary official material such as NIST SP 800-53/53A, OSCAL, ISO
  catalogues, COBIT/COSO public primary material and regulator guidance. Mark
  proprietary or paywalled frameworks as limited evidence.
