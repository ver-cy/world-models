# EM-OPS-01 local synthesis

## Disposition

- Complete reserved WM-ACT-003 as the Process / Workflow aggregate.
- Complete reserved WM-ACT-009 as the Method / Procedure knowledge aggregate.
- Create no third model ID: process instances, work items and step executions remain WM-ACT-003 components until independent mastership and lifecycle evidence proves otherwise.

## Boundary

WM-ACT-009 owns reusable authored knowledge: method, procedure, immutable edition, procedure step, competence requirement, standard reference and adopter-owned adoption record. Publication or adoption never constitutes execution.

WM-ACT-003 owns operational flow semantics: process family, concurrent variant, immutable released definition, steps, gateways, roles, state model, process instance, work item, step execution, deviation and compensation. A process references the exact adopted method/procedure edition that it operationalizes. It does not copy the knowledge artifact.

A work item represents offered or assigned work and has an assignment lifecycle. A step execution records observed performance. Either may exist without the other. Step execution may reference an atomic act, but cardinality and ownership remain held until WM-ACT-002 is reviewed.

## Version and execution contract

A released process definition is identified by process family, variant and version and is immutable. Variants are concurrently valid alternatives; versions form supersession lineages within each variant. Drafts are not citable by execution instances.

Every process instance pins its released definition. Every step execution records the applicable pins, times, performer, result and conformance-relevant observations. Traces are append-only. Deviation, manual exception, escalation and compensation are explicit facts; compensation adds a linked execution rather than rewriting history. Planned BPMN/CMMN paths never prove the observed path.

Method and procedure editions are immutable after release. Adoption becomes effective on the adopter's date. Errata or revised instructions produce a new edition linked by supersession. Publishing a new edition does not silently change an active or completed process.

## Invariants

1. Every execution resolves to an immutable released process definition and variant.
2. Released definitions, method editions and recorded trace events are immutable.
3. A deviation is explicit; missing trace evidence is not conformance.
4. Work-item state changes are distinct from execution events.
5. Planned flow is not evidence of actual performance.
6. Conformance and cycle-time metrics are reproducible derived projections.
7. Method-edition effect starts at adoption, not publication.
8. Historical replay uses exact definition, method-edition and event-order pins.

## Acceptance result

One process family has two concurrently valid variants. Separate instances pin each variant. A manually executed out-of-sequence step creates a deviation and, where needed, a compensating execution. A newly adopted procedure edition affects only work after its effective adoption point. Both traces remain reproducible without rewriting earlier instructions or outcomes.

## Holds

Both source descriptions remain under migration boundary review, and their wildcard BPMN, CMMN and ISO imports plus MUC/MMAS claims are not carried into the candidates. The prepared candidates add WorkItem and append-only execution structures, avoid atomic-act cardinality claims, define immutable edition/adoption semantics and provide eight replay/conformance fixtures. Relations remain candidate rows. Exact Grok comparison, one frozen semantic audit, package conversion and live verification are still required before release.
