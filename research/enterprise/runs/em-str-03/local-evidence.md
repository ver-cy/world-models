# EM-STR-03 local synthesis

## Disposition

- Narrow legacy WM-ACT-001 to agent-scoped Function, Competence, Proficiency and Capacity. Do not treat it as the Enterprise Business Capability master.
- Propose identifier-unassigned **Business Capability** and **Capability Realization** candidates because both have independent identity and lifecycle.
- Profile WM-ACT-034 as **Capability Assessment**. It receives no new root identifier.
- Treat **Capability Level** as either a versioned scale definition or a level assertion within a requirement or assessment. It is not a model root.
- Reuse WM-KNW-011 for required-level drivers, WM-MAT-008 for performance observations, and organization/process models as realization referents.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Business Capability identity is anchored in the class of outcomes and the object acted upon. It never derives from name, organizational unit, owner, process, system, product, budget line or decomposition path. It survives reorganization, process redesign and system replacement.

WM-ACT-001 describes what a capable agent can do, including proficiency and period-scoped capacity. Its owner and disclosure regime are agent-centric and remain separate from the enterprise capability register. Capability Realization is a temporal, evidenced binding between a capability and one realizer; it is mastered by the capability register rather than the realizer's source model.

## Capability, function, process and organization

Function is agent-scoped purpose. Business Capability is enterprise ability to achieve a class of outcomes. Process is the repeatable method by which work happens. Organizational unit, team and position are accountable or contributing realizers with their own lifecycles. Product or service is an offered outcome. Resource is used or consumed. Capacity is quantity available for a period and attaches to a realization.

A system is at most a supporting realizer. A claim of full realization requires at least one accountable non-system realizer and a pinned process or method where applicable. Department names are never capability definitions.

## Decomposition and levels

Capability decomposition is outcome specialization. Each child narrows the outcome class of its parent. Tier markers such as L1/L2/L3 are versioned edge attributes and never identity. Re-decomposition supersedes edges while keeping capability identities stable.

Required level is a demand statement with driver, horizon and pinned scale. Actual level is the conclusion of a finalized assessment for a validity window. Maturity measures institutionalization and repeatability against a method. Performance is observed outcome over a period. Maturity, performance and capacity remain separate dimensions.

## Assessment and evidence

Capability Assessment profiles WM-ACT-034. It pins criteria catalogue, scale, outcome vocabulary, aggregation model and decision rule before results. Evidence carries digest and criterion linkage. Indeterminate, not-applicable and untested outcomes remain explicit. Assessor competence and impartiality are recorded. Finalized assessments are immutable and never recomputed against a later scale.

WM-MAT-008 observations carry phenomenon, result and ingestion times, unit, method and uncertainty. Missing measurement is coded absence, never zero. Self-declared maturity without method and evidence yields no actual level.

## Realization and coverage

A Capability Realization records capability, realizer identity and kind, role, coverage share and basis, validity interval, accountable party and evidence. A successor binding records transfer or replacement without mutating history.

Coverage is an as-of projection over realization bindings. It distinguishes unrealized, partially realized, realized-but-low-maturity and unassessed. Missing bindings mean unknown unless a scoped completeness assertion proves coverage of the relevant population. Scenario realizations and target levels never feed authoritative actuals.

## Acceptance result

Process P realizes capability C and moves from unit U1 to unit U2. C keeps its identifier, outcome definition and decomposition position. Realization R1 closes at transfer time and successor R2 opens with U2 accountable. If P is unchanged, both bindings cite the same process release; if redesigned, R2 pins a successor process release. Historic assessments remain intact and the transfer triggers review. A department-name capability map fails because it would require deleting or renaming C.

## Required invariants

1. Capability identity is outcome-defined and survives organizational and technical change.
2. Unit, team, position, system, product and budget line never define a capability.
3. Function/competence and Business Capability never share identity or mastership.
4. Decomposition is outcome specialization; tier is an edge attribute.
5. Required and actual levels have distinct authorities and records.
6. Actual level exists only through a finalized method-bound assessment.
7. Maturity, performance and capacity remain separate.
8. Capacity is period-scoped and attaches to realization.
9. Full realization requires an accountable non-system realizer.
10. Missing binding or measurement is unknown/absent, never zero.
11. Scenario values never become authoritative actuals.
12. Released maps and assessments are immutable and explicitly superseded.

## Holds

WM-ACT-001 and WM-ACT-003 remain legacy-only migration boundaries. Business Capability and Capability Realization lack registry allocation. Current assessment, objective, observation and organization bases are non-canonical reviewable drafts. The repository has no approved capability relation contracts, scale registry, semantic crosswalk, source-master confirmation or fixtures. No canonical completeness, installability or publication readiness is claimed.

## Grok reconciliation and frozen audit

Grok accepted the identity split with conditions and confirmed that Capability Realization requires independent identity. The single frozen audit accepted that fixed identity decision, identified 21 artifact defects and supplied 55 fixtures. All bounded fixes are encoded in the two allocation candidates and the WM-ACT-034 profile without allocating identifiers.