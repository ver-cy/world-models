# Health Care Delivery

- Name: Health Care Delivery
- Catalogue ID: WM-ACT-014
- Registry ID: vr.wm-act-014
- Type: Published Vercy aggregate
- Version: 0.3.0-research.1
- Specification: https://ver.cy/models/wm-act-014-health-care-delivery/spec.yaml
- Storage type: format-independent; select a binding in the page constructor
- Interface: https://ver.cy/models/wm-act-014-health-care-delivery/#template-builder
- Processes: https://ver.cy/processes/
- Model agent protocol: https://ver.cy/model-agent-protocol.md
- Research evidence: https://github.com/ver-cy/world-models/tree/feat/mega-model-registry/research/runs/wm-act-014

Read this file first, then `spec.yaml`. Traverse Bundle → Layer → Finding →
Questions and Artifacts. The specification is published, while its research
assurance remains `reviewable-draft`. Do not claim canonical completeness
while `researchAdjudication.publicationHolds` is non-empty. Preserve source
references, master-system identity and access rules.

## Five-facet gate

Before creating or changing an instance, inspect the specification for explicit
coverage of: identity and class; direct properties; recognition and observation;
capabilities, behaviour and possible actions; context and evidence. Treat each
facet as required, optional, not applicable with a reason, or delegated through
a pinned model reference. Do not invent physical properties for abstract
objects. For physical measurements preserve units, tolerances, method,
conditions, observation time, uncertainty and provenance.

Keep capability, behaviour, state, transition, affordance, operation,
precondition, effect, reversibility, permission, constraint, hazard and failure
mode distinct. Resolve delegated child models and master systems instead of
copying their domains into this model.

## Agent lifecycle route

1. **Fill:** read the nearest owner and Dimension policies, resolve master
   identities, ask only for missing facts or authority, then record facts,
   hypotheses and unknowns distinctly with evidence and observation time.
2. **Extend:** propose a versioned extension when the published bundles and
   layers cannot express a required concept. Preserve stable IDs and namespace
   ownership; do not silently widen the model boundary.
3. **Edit:** validate authority, purpose, current version and concurrency before
   mutation. Preserve history and provenance. Treat access expansion, external
   writes and material side effects as confirmation-gated actions.
4. **Validate:** run schema, semantic, reference, permission, evidence and
   five-facet checks before and after a write. Report unresolved references,
   lossy projections, stale observations and publication holds.
5. **Retire:** deprecate and supersede through the declared lifecycle. Preserve
   immutable history and resolvable references. Require confirmation before
   deletion, destructive migration or irreversible external action.

Autonomous work is limited to policy-authorized reading, local population of
confirmed facts, validation, indexing and non-destructive maintenance. Propose
schema changes and new imports. Require confirmation for publication, broader
access, external writes, deletion and irreversible effects. Follow the model
agent protocol and the nearest local `AGENTS.md` whenever their rules are more
restrictive.
