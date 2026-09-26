# EM-STR-03 Business Capability — adjudication

## Verdict

**Split, with narrowing reuse.** WM-ACT-001 cannot be completed as the Business Capability master. Retain and **narrow** it to agent-level Function / Competence / Proficiency / Capacity (its actual content), and **create** two identifier-unassigned candidates with independent identity: **BusinessCapability** and **CapabilityRealization**. **Profile** reserved WM-ACT-034 for **CapabilityAssessment** — no new root. **Reject** CapabilityLevel as a root: it resolves into (a) a versioned scale definition referenced from an assessment-scale registry and (b) a positional decomposition attribute of a parent-child edge. Allocate no identifiers.

## Evidence

WM-ACT-001 (K1, legacy, `described-previous-version`, `migration-boundary-review`) states its subject as "what an agent is able to do", owner "the capable agent", objects `capability`, `proficiencyLevel`, `capabilityAttribution` (agent ref, level, valid period), `capacityStatement`, `evidenceRecord`; composition REFERENCEs person (H1) and organization (O1); imports ESCO and O*NET; stewardship: "the profile belongs to the agent", disclosure by owner consent. That is occupational competence with individual privacy semantics. EM-STR-03 scope is enterprise ability to achieve a class of outcomes "independently of current structure and means", mastered by strategy/OKR/metric registry. Subject, owner, mastership and disclosure regime all differ. Priority (wave 2, score 63, reuse 0.52) reflects the occupational reading, not a strategic master. EM-OPS-01 and EM-LND-04 already record WM-ACT-001 as blocked for capability semantics.

## Identity/mastership

BusinessCapability identity anchors on the **outcome class plus the object it acts on**, never on name, unit, owner, process, system, budget line or decomposition path. Identity priority: capability-register master key → governed IRI → minted UUID/ULID marked surrogate. Master is the strategy function's capability register; WM-ACT-001 mastership ("the capable agent") must not be inherited. WM-ACT-001 retains mastership of individual competence and of capacity statements. CapabilityRealization is mastered by the capability register, not by the realizer's owning model.

## Capability/function/process

- **Function** (WM-ACT-001) is agent-scoped and named by purpose (welding, auditing); **capability** is enterprise-scoped and named by outcome class. A function may be a competence input to a realization; it is never the capability.
- **Process** (WM-ACT-003) is *how*: family/variant/immutable released version, instances, traces. Capability is *what*. Process realizes; it does not constitute.
- **Organizational unit** (WM-ORG-002) has parent-scoped identity, reorganization acts, lineage and tombstones; its names "are never identity". A capability defined by a unit inherits that lifecycle and dies at reorganization.
- **Team** (WM-ORG-003): bounded, enumerated, time-bounded membership; often transient.
- **Position** (WM-ORG-004): an occupant-independent seat; its competency requirements resolve against WM-ACT-001, not against BusinessCapability.
- **Product/service**: an offered outcome; many products may draw on one capability.
- **Resource**: a used or consumed asset.
- **Capacity** (WM-ACT-001 `capacityStatement`): volume per period. Capability existence and level are not capacity; capacity attaches to a realization for a stated period, never to the capability.

## Taxonomy/decomposition

Parent-child is **outcome specialization**: each child is a narrower outcome class of its parent; siblings are mutually exclusive at that tier; no node is defined as "what unit X does". Test: if reparenting or renaming a unit forces the tree to be redrawn, it is an org chart and is rejected. Tier codes (L1/L2/L3) are positional attributes of the edge, not identity, and may change under re-decomposition without changing capability identity. Decomposition edges carry validity intervals; re-decomposition supersedes edges, not nodes.

## Level/maturity/performance

Reject the v1 flat `level` and `maturity` code fields as non-normative. **Required level** is a demand-side statement with a pinned scale, a horizon and a driver (typically WM-KNW-011), held on a capability-requirement record — not on the capability. **Actual level** is only ever the conclusion of a finalised CapabilityAssessment, valid for that assessment's window. **Maturity** (institutionalization/repeatability against a method-bound scale) and **performance** (observed outcome measures over a period) are separate dimensions and must not be netted into one score; they may legitimately diverge. Performance evidence comes from WM-MAT-008 observations carrying phenomenon/result/ingestion time, unit code system plus code, uncertainty, and coded absence — never zero for missing measurement.

## Assessment/evidence

Profile WM-ACT-034: pin the criteria catalogue at version; declare scale, outcome vocabulary, aggregation model and decision rule **before** results; register evidence with digest and criterion linkage; preserve indeterminate, not-applicable and untested outcomes; separate determiner from decision authority; record assessor competence and impartiality; freeze on finalisation; change only by amendment or supersession. Historical assessments are never recomputed against a changed scale. Self-declared maturity without pinned criteria, declared method and evidence yields no actual level.

## Realization/coverage

A CapabilityRealization binds one capability to one realizer with: realizer kind (process/method/unit/team/position/system/resource/supplier), role (primary, contributing, supporting), coverage share with stated basis, validity interval, accountable party, and evidence. **A system is at most a supporting realizer.** Any claim of full realization requires at least one non-system realizer — a pinned WM-ACT-003 released definition or method plus an accountable unit or position. Coverage is a derived, as-of projection over the binding set; the map must distinguish unrealized (no binding), partially realized, realized-but-low-maturity, and unassessed. Absence of a binding is *unknown*, not zero coverage. Map completeness is an explicit scoped assertion, never implied.

## Organization/time/scenario

Keep separate: capability register effective interval; realization validity interval; assessment validity window; observation phenomenon/result/ingestion times; assertion knowledge time. Released capability-map versions are immutable and superseded explicitly. Scenario (target-state) maps are labelled per EM-LND-04; scenario realizations and scenario levels never feed authoritative coverage, actual level or performance.

## Acceptance scenario

Process P realizes capability C; P transfers from unit U1 to U2. C's identifier, outcome statement and decomposition position are unchanged and C is not versioned. Realization R1(C, P, primary, accountable U1) is closed at t; successor R2(C, P, primary, accountable U2) opens at t with the same WM-ACT-003 family/variant/version pin if no redesign occurred; if the transfer redesigns P, R2 pins a new released version. WM-ORG-002 records the reorganization act on the unit side. Prior assessments keep their windows and are not recomputed; realizer change fires a declared review trigger. Coverage recomputes as an as-of view. A map whose nodes are department names fails: the transfer would require renaming or deleting nodes, proving no capability identity existed.

## Invariants

1. Capability identity is outcome-defined and survives reorganization, renaming, process redesign and system replacement.
2. A department, team, position, system, product or budget line is never a capability definition.
3. Decomposition is outcome specialization; tier codes are edge attributes, not identity.
4. Required level and actual level are distinct records with distinct authorities.
5. Actual level exists only as a finalised assessment conclusion bound to a pinned scale and method.
6. Maturity and performance remain separate, un-netted dimensions.
7. Capacity is period-scoped and attaches to a realization, never to the capability.
8. A system supports; full realization requires a non-system realizer and an accountable party.
9. Missing binding or missing measurement is coded unknown/absent, never zero.
10. Scenario values never become authoritative actuals.
11. Released map versions are immutable and superseded explicitly.
12. Individual competence (WM-ACT-001) and enterprise capability never share identity or mastership.

## Minimal model set

WM-ACT-001 narrowed (agent function/competence/proficiency/capacity); BusinessCapability (new root, unassigned); CapabilityRealization (new root, unassigned); CapabilityRequirement / level statement (contained); CapabilityAssessment as a WM-ACT-034 profile; capability scale definitions by reference; realizer referents WM-ACT-003, WM-ORG-002/003/004; WM-KNW-011 for required-level drivers; WM-MAT-008 for performance observations.

## Holds

WM-ACT-001 and WM-ACT-003 are legacy previous-version descriptions under migration-boundary-review; their MUC/MMAS claims and wildcard imports are unverified. WM-ACT-034, WM-KNW-011 and WM-MAT-008 are single-provider-waiver reviewable drafts carrying live-source, coverage and relationship holds. WM-ORG-002/003/004 are dual-provider reviewable drafts with unresolved boundary items. Relationship contracts are empty; the frozen relations list contains no capability edges. No semantic crosswalk, mastership confirmation, scale registry or fixtures exist. No identifiers allocated. No canonical completeness, installability or publication-readiness claim is made.
