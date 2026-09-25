# Independent review request: EM-OPS-01 Process, Procedure and Execution

Review this Enterprise metamodel boundary independently. Use public BPMN/CMMN, process mining, workflow, procedure-control and operational trace practice where useful. Separate standards evidence from design inference. Do not invent a Vercy identifier.

Two existing reserved candidates are under migration boundary review:

- WM-ACT-003 Process / Workflow: legacy K3 description with process definition and execution bundles.
- WM-ACT-009 Method / Procedure: legacy K6 description with codification, applicability and lifecycle bundles.

Proposed decision: **COMPLETE BOTH RESERVED MODELS**, no new ID. WM-ACT-009 owns method, procedure, immutable edition, competence requirements and adoption records. WM-ACT-003 owns process family, variant, immutable released definition, instance, work item, step execution, deviation and compensation. A process references the exact adopted method edition. ProcessInstance and ActivityExecution remain components unless separate identity/mastership/lifecycle is proven.

Rules to challenge:

- released definitions and editions are immutable;
- variants are concurrent alternatives, versions are supersession lineages;
- each instance and step execution pins the applicable process definition/variant and method edition;
- work assignment is distinct from observed execution;
- deviations, exceptions and compensations are append-only facts;
- planned BPMN/CMMN paths do not prove actual traces;
- conformance is a reproducible projection over a pinned definition and observed trace;
- method edition takes effect through adoption, not publication.

Test the negative case where an instruction update changes a completed process retroactively. Test the acceptance case with one process, two variants, a manual exception, compensation and a newly adopted procedure edition producing separate reproducible traces.

Current holds: wildcard imports, unsupported conformance claims, candidate-only relation ledger, unverified stepExecution-to-atomic-act cardinality, missing work-item structure and no executable fixtures.

Return at most 1000 words with: Verdict per reserved model; identity/lifecycle boundary; version/variant/adoption rules; assignment versus execution; trace and deviation semantics; scenario results; missing fields/relations; migration steps; publication blockers.
