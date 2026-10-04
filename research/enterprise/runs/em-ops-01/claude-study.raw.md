# EM-OPS-01 Boundary Review — Process, Procedure and Execution

## Verdict

- **WM-ACT-003 Process / Workflow — COMPLETE RESERVED MODEL.** It is the operational-flow aggregate and owns definition, variant, instance and step-execution identity. Completion is required, not a new ID.
- **WM-ACT-009 Method / Procedure — COMPLETE RESERVED MODEL.** It is the reusable knowledge artifact (method, procedure, edition, adoption). Not a duplicate of WM-ACT-003; no merge/retire.
- **ProcessInstance / ActivityExecution — no new model ID.** They stay inside WM-ACT-003's `execution` bundle. A third aggregate is not provable from this dossier: the trace has its own *lifecycle* but no independent *identity* — an instance cannot be named without a pinned definition edition. Split trigger deferred, with criteria below.
- **ProcessMethod (contour candidate type) — REUSE ONLY** as `method` in WM-ACT-009 with a domain tag. No separate type.
- **Anything beyond the two reserved rows — DEFER** pending crosswalk evidence.

## Evidence state

Both rows are `described-previous-version` / `migration-boundary-review`, `evidence_depth: index-and-publication-metadata`, `priority_confidence: low`, and both research rows are `blocked-on-providers`, `validation_status: not-valid-or-not-run`. The supplied specs carry `muc: "2.0: Conformant"` and `mmas: A1`; nothing in the dossier supports either claim, so both are treated as unsupported assertions, not evidence. Imports are wildcards (`bpmn: "*"`, `cmmn: "*"`, `iso-management-systems: "*"`, `iso-9001: "*"`) — no standards conformance, compatibility or installability is claimed here. The two relationship-ledger rows are `review_state: candidate` and grant nothing. Enterprise v1 fields (OPS-01/02/03) are `candidate-not-normative`. No fixtures exist for either candidate.

## Boundary and aggregate identities

**WM-ACT-009 owns:** `method` (approach), `procedure` and `procedureStep` (instructions), `edition` (published immutable version), `standardReference`, `competenceRequirement`, `adoptionRecord`. Its identity is *publication* identity: authored, versioned, adopted, superseded. It never owns an instance, a timestamp of work, or an outcome. It only references organizations (WM-ORG/O1) and capabilities (K1).

**WM-ACT-003 owns:** `process` (definition family), `variant`, `releasedDefinition` (the immutable triple below), `step`, `gateway`, `role`, `state`, `processInstance`, `stepExecution`, `workItem`, `deviation`. Its identity is *operational* identity. It only references a method edition in WM-ACT-009 — the link is directional and held on the process side, which both specs already agree on and which is correct: many processes in many organizations may codify one method edition.

Three boundaries need correcting in the supplied specs:

1. **Method vs procedure vs process definition.** A method is reasoning, a procedure is instruction text, a process definition is an executable flow with roles, gateways and states. The dossier's scope line is right: methodology sets rules, not a process instance. Therefore `process -> codifies -> method` must resolve to a *method edition*, never to the method family.
2. **ActivityExecution vs act (WM-ACT-002).** The K3 spec asserts `stepExecution -> recordedAs -> act (one-to-one)`. WM-ACT-002's spec is not in the dossier, so that cardinality is a hold. The defensible allocation: `stepExecution` owns the process-context identity (instance, step, variant pin, timing, performer, outcome, conformance flags) and *references* the atomic act. It does not own act identity.
3. **Task/work-item vs execution event.** Neither spec has a `workItem`. Assignment is not execution: a work item can be offered, claimed, reassigned, escalated or expire with zero `stepExecution` rows. `workItem` must be added to WM-ACT-003 as a separate object with its own state machine.

## Version/variant/adoption semantics

- **Released edition identity:** `(processId, variantKey, version)` — immutable once released. Drafts have no citable identity and no instance may reference one.
- **Version vs variant:** a new *version* supersedes along a lineage; a *variant* is a concurrently valid alternative path set under the same process family, each variant carrying its own version lineage. Two variants are not two definitions and not two versions.
- **Method edition adoption:** `adoptionRecord` stays in WM-ACT-009, owned by the adopter, and is effective from the adoption date — not from the publication date. A process pins the *edition it adopted*, resolved through the adoption record, so publishing edition 4.0 does not silently re-point live processes.
- **`procedureRevised` is a defect.** The K6 event is described as "instructions were changed within an edition cycle". That mutates a released artifact and is precisely what makes the negative case reachable. It must be retired and replaced by an errata-producing `editionReleased` with `supersedes` lineage.

## Execution and trace contract

Trace is append-only. `processInstance` pins the released-edition triple at start; each `stepExecution` re-pins the triple and the method-edition ref in force at *its* start time, so a mid-flight edition change is visible in the trace instead of rewriting it. Deviation, manual exception, escalation and compensation are all recorded as first-class facts: compensation is a new `stepExecution` linked `compensates -> stepExecution`, never a deletion or edit. Conformance is **derived**, computed over (trace, pinned edition) and materialized only in the `performanceDigest` projection — it is never stored as truth on a definition. The BPMN/CMMN model is the planned path only; an observed trace is the sole evidence of what happened. Replay is `as-of` by pinned refs and a monotonic event sequence.

Split criteria that would justify a third model ID later: trace mastership demonstrably separate from definition mastership (BPM engine vs process registry), an independent retention/erasure lifecycle, or traces citable without a resolvable definition edition. None is evidenced today.

## Invariants

1. `processInstance.definitionRef` and every `stepExecution.definitionRef` resolve to an immutable released edition triple; drafts are unreferenceable.
2. Released editions and recorded trace events are immutable; correction occurs only by new edition or new compensating event.
3. Every departure from the pinned definition is stored explicitly as a `deviation`; silence is not conformance.
4. A BPMN/CMMN model never constitutes evidence of the actual path.
5. `workItem` state changes are not `stepExecution` records, and either may exist without the other.
6. Conformance and cycle-time figures are derived projections, recomputable from pinned refs alone.
7. Method-edition effect on a process begins at adoption, not publication.

## Scenario walkthrough

**Negative — revised instruction rewrites closed history.** Procedure edition 3.0 is edited in place via `procedureRevised`, or an instance references the method *family* rather than an edition. A completed instance's steps then resolve to new instruction text, its conformance flips retroactively, and last quarter's digest changes with no event explaining it. Blocked by invariants 1, 2 and 7 plus retirement of `procedureRevised`: the change becomes edition 3.1 `supersedes` 3.0, the closed instance keeps its 3.0 pins, and replay reproduces the original result.

**Acceptance — one process, two variants, one manual exception, one new procedure edition.** Process D v2.0 releases variants A and B. Instance I1 pins (D, A, 2.0); I2 pins (D, B, 2.0). In I2 a work item is escalated and a step performed out of sequence: one `deviation` (kind `manual-exception`) plus a `compensates` execution. Mid-flight, procedure edition 4.0 is released and adopted; I1 and I2 keep 3.0 on already-started steps, later steps pin 4.0 with the adoption date recorded. Result: two separately reproducible traces, distinguishable by variant, deviation set and edition pins, with no shared mutable state.

## Migration path

1. Rename `vercy:world:k3` / `k6` and the K3/K6 spec paths to WM-ACT-003 / WM-ACT-009 identifiers; keep `legacy_alias` only.
2. Remove `muc` and `mmas` claims until independently verified; replace wildcard imports with pinned versions or drop the import.
3. Add `variant`, `releasedDefinition`, `workItem`; retire `procedureRevised`; restate conformance as derived; add `compensates`.
4. Build fixtures for the negative and acceptance scenarios, including replay-after-edition-change.
5. Only then run the APQC/BPMN, EPCIS/SCOR and AAS-PLM/EAM/WMS crosswalks, confirm mastership among BPM/ERP/WMS/PLM/EAM, and promote relations.

## Gaps and publication holds

Holds: wildcard imports; unsupported MUC 2.0 and MMAS A1 claims; both candidate relation rows (`COMPOSE -> WM-ACT-002` conflicts with the spec's REFERENCE role and would wrongly claim act identity; `REFERENCE -> WM-KNW-012` unverified); `stepExecution -> act` one-to-one cardinality pending WM-ACT-002's spec; WM-ACT-009's empty `composition_role`, `default_link_type` and `relations_ref`; no fixtures or publication packages; missing `workItem`; mutable-edition defect; unresolved mastership across BPM/ERP/WMS/PLM/EAM; `blocked-on-providers` synthesis for both rows. No publication readiness, installability, compatibility or standards conformance is asserted.
