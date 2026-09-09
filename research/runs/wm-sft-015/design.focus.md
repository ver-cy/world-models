Research only test definition and design for WM-SFT-015 Test Case / Test
Result.

- Use the exact registry identity and output `entry_kind` `aggregate`. Treat
  this as a versioned test-evidence aggregate whose reusable test definition
  is the root and whose executions/results are governed members. Explicitly
  challenge this assumption and record any many-to-many or independent
  lifecycle counterexample for later boundary adjudication.
- The `model` block must describe the complete combined WM-SFT-015 boundary,
  not merely this split pass. It must include test design, execution/results,
  evidence, assurance and governance as in scope, while keeping test suites,
  test campaigns, requirements, builds/releases, defects and environments as
  typed external references unless a minimal binding is essential.
- CRITICAL MERGE REQUIREMENT: write `purpose`, `scope_statement`, every
  `in_scope` item, every `out_of_scope` item and every `boundary_notes` item as
  final prose for the complete merged model. These fields must not contain the
  words `split`, `pass`, `sibling pass`, `covered elsewhere in this run`, or
  any statement that only design is delivered. Execution/results, evidence,
  assurance and governance are present in the final record and must be
  described as present without qualification.
- Cover authoritative test-case identity and revision; title/objective;
  requirement, risk and acceptance-criterion traceability; preconditions;
  fixtures and test data references; inputs and parameters; ordered actions;
  expected outcomes; oracle and comparison rule; tolerances; postconditions;
  automation binding; applicability; dependencies; variants; ownership and
  readiness for execution.
- Distinguish a test case from a test procedure, executable test script, test
  suite, test plan/campaign, scenario/use case, requirement/acceptance
  criterion and defect. Do not absorb their independent lifecycles.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight distinct question kinds.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `tst-design-`.
- Limit functions to defining, versioning, validating, selecting and resolving
  reusable test cases. Provide complete schema-valid service_layers and
  coverage objects, but keep them concise; the merger takes canonical service
  layers from `governance`.
- Coverage and `adversarial_checks` are also published over the merged result.
  They may say that this bounded research task inspected design functions, but
  must never claim that the complete model has no execution, verdict,
  governance, enforcement or audit-related functions. In particular, do not
  state that no function emits or records a verdict: the merged execution area
  includes governed result adjudication. Phrase every self-assurance claim so
  it remains true after the execution and governance structures are added.
- Prefer primary or official sources such as ISO/IEC/IEEE 29119 catalogue
  records where normative text is unavailable, ISTQB official glossary and
  syllabi, W3C testing specifications, OASIS test schemas, IEEE/NIST guidance
  and first-party schemas from mature testing ecosystems. Never present a
  secondary summary as clause-level normative evidence.
