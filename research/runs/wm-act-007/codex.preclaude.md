# Codex pre-Claude research: WM-ACT-007 Work Order

Status: provisional pre-provider analysis. This file is not a provider result, synthesis, validation report or publication input.

## Agent-native five-facet assessment

1. **Identity and class: required.** Authoritative ID/master system, class criteria, instance distinctions, whole/part boundary and class-definition version.
2. **Direct properties: required for native nonphysical properties; geometry, mass and material are not-applicable because the subject is not itself a physical object. References to physical subjects do not import their properties.
3. **Recognition and observation: required.** Recognition signals, method/interface, conditions, confusing alternatives, confidence, uncertainty, evidence and observation time; external models/datasets use pinned references.
4. **Capabilities, behaviour and possible actions: optional, with not-applicable allowed and explained.** Distinguish capability, behavior, state, transition, affordance, permitted action, precondition, input/tool, effect, reversibility, permission, constraint, hazard and failure.
5. **Context and evidence: required.** Origin, creator/issuer, owner/steward, location/operating context where relevant, history, related events/processes/contracts/systems, source, mastership, freshness, confidence, access, privacy and retention.

### Agent operation route

Generated AGENTS.md must route safe fill, extension, patch/edit, validation and retirement; distinguish fact/hypothesis/unknown; resolve child models and master systems; declare autonomy boundaries; run before/after checks; and link to https://ver.cy/model-agent-protocol.md once published. The unverified URL remains a visible hold.

### Agent-native gate

Before promotion, provider comparison and adjudication must answer all ten roadmap gate questions, verify every facet status/reason, require pinned references for delegated facets and reject fabricated physical fields on abstract subjects.


## Frozen boundary

A Work Order is an authoritative, versioned instruction that authorizes and constrains one or more units of work. It records why work was ordered, what outcome and scope are authorized, applicable constraints, target and references, planning commitments, resource requirements, responsibility, state, acceptance conditions and disposition.

The model owns the order's identity, authorization, scope, requirements, state transitions, changes, cancellation, acceptance criteria and closure decision. It may contain task references under the candidate `CONTAINS WM-ACT-006` relation, but it does not own task execution semantics. It references rather than duplicates procedures/work masters, schedules, assets, locations, people and organizations, inventory, costs, measurements, performed-work records, access control, enforcement and audit trails.

Requests for work are inputs and may be rejected without an order. A work order is not proof that work occurred. Completion claims and acceptance evidence are referenced results; the operational record remains owned by the relevant execution model.

## Primary evidence set

1. ISA, ANSI/ISA-95.00.05-2018 preview, transactions and Work Schedule/Work Performance/Work Record models: https://www.isa.org/getmedia/bbc0eb3e-d047-440d-88fc-642b14bd8d40/ISA-95-00-05-2018-preview.pdf
2. ISA, ISA-95 standard overview, enterprise-control information exchange boundaries: https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard
3. OPC Foundation, OPC UA for ISA-95 Part 4 Job Control, Job Order definition and resource requirements: https://reference.opcfoundation.org/specs/OPC-10031-4/4.1
4. OASIS PLCS, WorkOrder template, authority to undertake work, issue date, classification and unique identity: https://docs.oasis-open.org/plcs/plcslib/v1.0/cs01/data/contexts/OASIS/templates/WorkOrder/template.html
5. OASIS PLCS concept model, Work_order and Work_request distinction: https://docs.oasis-open.org/plcs/plcslib/v1.0/cs01/data/PLCS/concept_model/model_definitions.html
6. OASIS PLCS aviation maintenance DEX, authorization, reportable item and task reference: https://docs.oasis-open.org/plcs/dexlib/R1/dexlib/data/dex/aviation_maintenance/sys/plcs_info_model.htm
7. OASIS PLCS referencing_task template, versioned external task specification boundary: https://docs.oasis-open.org/plcs/dexlib/cs01/data/templates/referencing_task/sys/section.htm
8. UNECE UN/EDIFACT JOBOFF, Job Order message interoperability precedent: https://unece.org/fileadmin/DAM/trade/untdid/d97b/trmd/joboff_c.htm

## Proposed structure

### Bundle 1: authority-and-origin

- Layer `order-identity`: findings `authoritative-identity`, `classification-and-kind`.
- Layer `request-and-rationale`: findings `originating-request`, `business-or-operational-rationale`.
- Layer `authorization`: findings `issuing-authority`, `authorization-scope`.

Questions cover master-system ID and aliases; order class and jurisdiction/profile; request reference and requester; triggering condition and desired result; issuer authority and delegation; authorization limits, effective time and supersession.

### Bundle 2: ordered-work-definition

- Layer `scope-and-outcome`: findings `authorized-scope`, `required-outcome`.
- Layer `task-composition`: findings `contained-task-references`, `procedure-or-work-master-reference`.
- Layer `target-context`: findings `subject-or-target-reference`, `location-and-operational-context`.

Questions cover inclusions/exclusions; deliverable or condition sought; task identity, ordering and dependencies; immutable procedure version; affected asset/product/case reference; location, hierarchy scope and access constraints. Task and procedure lifecycles stay outside this model.

### Bundle 3: planning-and-constraints

- Layer `priority-and-time`: findings `priority-and-criticality`, `planned-window-and-deadline`.
- Layer `dependencies-and-holds`: findings `predecessors-and-blockers`, `permit-safety-quality-constraints`.

Questions cover priority authority and escalation; earliest/latest start, due window and timezone; predecessor orders/tasks and release conditions; permits, isolations, safety controls, quality gates and governing references. The work order stores bindings, not the external schedule or enforcement engine.

### Bundle 4: resource-requirements

- Layer `responsibility`: findings `responsible-party`, `assignment-and-acknowledgement`.
- Layer `required-resources`: findings `personnel-capability-requirements`, `equipment-material-asset-requirements`.
- Layer `commercial-bounds`: findings `estimated-effort-and-cost-bound`, `service-contract-reference`.

Questions cover accountable role/organization references; assignee acceptance or refusal; required competencies and quantities; equipment, physical asset, material and lot requirements; estimates, ceilings and approval thresholds; controlling agreement and service-level references. People, organizations, stock, pricing and contracts remain referenced models.

### Bundle 5: lifecycle-and-change-control

- Layer `order-state`: findings `lifecycle-state`, `release-and-dispatch`.
- Layer `change-control`: findings `revision-and-supersession`, `suspension-cancellation-and-expiry`.
- Layer `exception-management`: findings `deviation-and-escalation`, `conflict-and-duplicate-resolution`.

Questions cover draft/authorized/released/in-progress administrative state; authorized transition actor and event time; dispatch destination and acknowledgement; revision identity, reason and affected scope; cancellation authority and residual obligations; deviation approval and unresolved blockers; duplicate/conflicting order handling. Actual work state is a referenced execution fact, not silently inferred from order state.

### Bundle 6: acceptance-closure-and-governance

- Layer `completion-interface`: findings `completion-claim-reference`, `acceptance-criteria`.
- Layer `closure-and-disposition`: findings `acceptance-or-rejection`, `closure-and-retention`.
- Layer `evidence-and-access`: findings `provenance-and-quality`, `ownership-disclosure-and-access`.

Questions cover referenced performance/work record; measurable acceptance criteria and verifier; acceptance/rejection decision, defects and rework order links; closure reason, retention class, legal hold, tombstone and adopting-Dimension deletion authority; source lineage and confidence; record owner, delegated writers, disclosure policy and access exceptions. Evidence, access enforcement and audit records remain in their owning models.

## Candidate functions

1. `create-draft-order`: establish identity, origin and proposed scope without authorization.
2. `validate-order-boundary`: check task references, target, authority, constraints and required fields.
3. `authorize-order`: record the authorized revision, issuer authority, effective time and scope.
4. `release-order`: make an authorized order available to the bound dispatch/execution context.
5. `revise-order`: create a traceable successor revision without overwriting issued meaning.
6. `suspend-or-resume-order`: change administrative availability under named authority and reason.
7. `cancel-order`: terminate remaining authorization while preserving history and obligations.
8. `record-completion-claim`: bind an external performed-work record without asserting acceptance.
9. `accept-or-reject-result`: apply declared acceptance criteria and record the decision reference.
10. `close-order`: finalize disposition, unresolved exceptions and retention metadata.

## Composition decisions

- `CONTAINS WM-ACT-006`: retain only task references, order-local parameters and composition order; WM-ACT-006 owns task execution semantics.
- Reference a process/workflow model for orchestration and a procedure/work-master model for instructions and versions.
- Reference schedule/calendar models for detailed scheduling; retain only order-level windows and commitments.
- Reference assets, locations, people, organizations, materials and inventory rather than reproducing their identities or lifecycles.
- Reference contracts/cost models for commercial terms, performed-work/evidence models for actual results, and security/ownership/access/audit models for policy execution.
- ALIGN ISA-95/IEC 62264 job/work scheduling concepts, OPC UA ISA-95 Job Control, ISO 10303-239 PLCS/OASIS templates and UN/EDIFACT JOBOFF. No conformance claim is made.

## Mandatory service-layer decisions

- Identity priority: authoritative work-management master-system identifier; governed global identifier/IRI; adopting-Dimension UUID or ULID.
- Event timestamps use RFC 3339 with seconds and explicit offset or `Z`; authorization, release, lifecycle-event and acceptance times are distinct from observation/ingestion time.
- Create/update operations preserve issuer authority and immutable issued revisions. Reads require owner permission and may redact target, commercial, safety or personal details. Delete is retention/disposition driven: issued orders are tombstoned or cryptographically erased only under the adopting Dimension's retention and legal-hold policy; referenced model records are never cascaded here.
- Validation checks unique local IDs, resolvable references, authorized state transitions, temporal consistency, immutable procedure versions, required acceptance criteria, nonnegative resource quantities and explicit units.
- Coverage checklist: identity; lifecycle; relationships; temporal; provenance; ownership; validation; access; retention and deletion; interoperability; authority; task composition; constraints; resources; acceptance; exceptions.

## Holds and open questions

- Candidate `CONTAINS WM-ACT-006` relation needs coordinator review because containment may mean grouping references rather than lifecycle ownership.
- Cross-domain generality needs second-provider stress testing: manufacturing job order, maintenance work order, field-service order and administrative order use different state vocabularies.
- Exact sibling IDs for procedure, schedule, performed work, asset, organization, inventory, commercial terms and access/audit bindings must be selected from the registry without expanding this model's scope.
- Retention periods, signature requirements, safety permits and cancellation effects are jurisdiction/profile specific and cannot be universal defaults.
- This pre-Claude analysis does not satisfy the repository's provider, comparison, no-tools adjudication, synthesis, validation or publication gates.
