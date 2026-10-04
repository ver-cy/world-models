# Single frozen semantic audit — EM-STR-03

You are the sole independent frozen auditor. No tools, browsing, standards claims, identifier invention or registry mutation. This audit runs exactly once and will not be repeated.

Audit the reconciled proposal and artifacts below. Fixed identity decision: retire the enterprise-capability meaning from legacy WM-ACT-001 and narrow it to agent Function / Competence / Proficiency / Capacity; Business Capability and Capability Realization both have independent identity but remain registry-unassigned; Business Capability identity is outcome-class based; Capability Realization is a temporal evidenced binding with successor history; Capability Assessment profiles WM-ACT-034; Capability Level is a scale definition or assertion, never a root.

Find material internal contradictions, missing fields, unenforceable invariants, lifecycle/version/provenance defects, coverage and missingness conflation, decomposition leaks, and unsafe migration behavior. Known registry/base publication gaps are holds, not artifact defects. Return:
1. Verdict ACCEPT or REVISE.
2. Numbered material defects with exact evidence.
3. Required bounded fixes.
4. One JSON fenced array of additional fixtures with target, id, kind, input, expect and optional expectedCode, covering every defect. Targets must be BusinessCapability, CapabilityRealization, or EM-STR-03-profile.
5. Explicit identifier decision.
6. Freeze decision: closed, no rerun.


## local-evidence.md
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


## claude-study.raw.md
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


## grok-study.raw.md
Verdict. Accept with conditions. Split WM-ACT-001: retire its enterprise-capability semantics and narrow the residual to agent Function, Competence, Proficiency, and Capacity. Do not reuse or profile WM-ACT-001 as Business Capability. Introduce identifier-unassigned candidates for Business Capability, identified by outcome class, and for Capability Realization, which needs independent identity. Profile WM-ACT-034 for Capability Assessment. Capability Level is a scale definition or an assertion, not a root. This is an assessment of the proposal, not a claim of publication readiness.

Strongest evidence. The transfer test. Moving one process from unit U1 to unit U2 must leave capability identity unchanged and change only realization bindings. Identity based on outcome class survives reorganization, process redesign, and system replacement; department names fail that test because they move with the chart. A system can support a binding but cannot alone prove full realization, which matches an evidenced, multi-party binding rather than a system attribute. The required separations — required versus actual, maturity versus performance, capability versus capacity, unknown versus zero — stop one score from standing for four different claims.

Strongest counterexample. If practitioners define the outcome class by the current department or by the current process design, the transfer test fails and the new candidate collapses back into the legacy Function/Capability mix. A second failure mode: treating agent competence (the narrowed WM-ACT-001) as the enterprise capability, so identity moves with skilled people rather than with the outcome class. A third: making Capability Level the root, so a scale position is mistaken for the capability itself and history is overwritten when the score changes.

Identity/mastership. Business Capability is mastered as a stable outcome class: what the enterprise must be able to produce, not who performs it or how. Mastership does not transfer when a process moves from U1 to U2, and it is not held by organizational unit, department, process, system, role, or supplier. Narrowed WM-ACT-001 keeps mastership only of agent Function, Competence, Proficiency, and Capacity. Capability Realization is mastered separately as a temporal evidenced binding. Assessment is an evaluation record, a profile of WM-ACT-034, and does not mint or rename capability identity.

Capability/function/process. Capability, function, and process are distinct. Capability is the outcome class. Function in the narrowed WM-ACT-001 is agent behavior and competence, not a department. Process, including legacy WM-ACT-003, is how work is sequenced; it may realize a capability and must not define it. No 1:1 capability-to-process mapping is required.

Decomposition. Decompose only by outcome specialization: a parent outcome class contains child outcome classes. Decomposition is not an organizational hierarchy, not a process breakdown, and not a maturity ladder. Decomposition depth and Capability Level are different notions and must not share a scale.

Level/maturity/performance. Capability Level is reference scale or an assertion against that scale, never a root that owns the capability. Required level and actual level are distinct assertions on the same scale. Maturity is how far the ability is institutionalized. Performance is measured outcome achievement. Capacity is volume or sustainment, not the ability itself. Collapsing these into one score is rejected.

Assessment/evidence. Profile WM-ACT-034 Assessment/Evaluation; do not create a second assessment root. Evidence is carried by WM-MAT-008 Observation/Measurement Record. An assessment asserts a level at a time against a capability or a realization; it does not redefine the outcome class. Unknown is an explicit state. It is not a default of zero, and absence of evidence is not evidence of absence.

Realization/coverage. Capability Realization needs independent identity. Decision: yes. It is a temporal evidenced binding to processes, organizations, roles, systems, resources, or suppliers. A pure link cannot hold validity, supersession, partial coverage, concurrent bindings, or assessment history without mutating the capability or losing history. Coverage is the evidenced portion of the required outcome class in a scope and time; it may be partial, overlapping, or unknown. A system may be a binding participant and still be insufficient to prove full realization.

Organization/time/scenario. Bindings to WM-ORG-002, WM-ORG-003, and WM-ORG-004 sit on the realization and are time-bounded. Those units are participants, not capability owners. WM-KNW-011 goals may set required levels; they do not name capabilities. Scenario variants are different realizations or different assessments, not different capability identities.

Scenario. Transfer process P from U1 to U2. Capability identity stays the outcome class. The realization bound to U1 ends or is superseded; a realization bound to U2 starts, with roles, systems, or suppliers free to differ. Prior evidence stays on the earlier realization. A temporary performance dip does not delete the capability. Neither department name is accepted as the definition. A system that still supports the outcome does not by itself prove full realization after the transfer.

Invariants.
1. Capability identity is fixed by outcome class alone.
2. Reorganization does not change capability identity.
3. Process redesign does not change capability identity.
4. System replacement does not change capability identity.
5. Department or unit names are rejected as capability definitions.
6. Realization bindings may change while capability identity stays stable.
7. A system may support realization but cannot alone prove full realization.
8. Required level and actual level are distinct.
9. Maturity and performance are distinct.
10. Capability and capacity are distinct.
11. Unknown coverage is not zero coverage.
12. Capability Level is a scale definition or assertion, never a root.
13. Assessment does not create or rename the capability.
14. Agent competence, proficiency, and capacity stay outside Business Capability mastership.
15. Multiple realizations of one capability may coexist.
16. Ending a realization does not retire the capability.
17. Capability decomposition is by outcome specialization, not by org chart or process steps.
18. Absence of a realization record is not evidence that the outcome class does not exist.

Minimum model set. Unassigned Business Capability candidate; unassigned Capability Realization candidate with independent identity; Capability Level as scale or assertion only; Capability Assessment as a profile of WM-ACT-034; narrowed WM-ACT-001 for agent Function, Competence, Proficiency, and Capacity; links to organizational unit, team, position, goal, and measurement record; process treated as a legacy realization participant, not as the capability root.

Blockers. Outcome-class naming, equivalence, and deduplication rules are undefined. Realization granularity is undecided: one realization per binding tuple, or one realization with many participants. Scale ownership for Capability Level is undefined. Evidence-sufficiency rules are missing, including how supplier or system support counts. Double-count risk remains until enterprise-capability usage is explicitly retired from WM-ACT-001. No identifier is assigned, and nothing here is publication-ready.


## candidate-allocation-offline-business-capability/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-STR-03","proposedName":"Business Capability","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An enterprise ability defined by an outcome class and acted-upon object remains identifiable across reorganizations, process redesigns, system replacements and ownership changes.","versionIdentity":"Changes to outcome semantics, applicability or governed scope create immutable capability versions; decompositions change through versioned edges without changing capability identity.","independentLifecycle":["proposed","approved","active","constrained","deprecated","superseded","retired"],"mastership":"enterprise capability-register authority"},"boundary":{"owns":["persistent business-capability identity","outcome class and acted-upon object","definition, applicability and scope","capability decomposition edges","tier and specialization metadata","accountability and stewardship bindings","lifecycle, deprecation and successor lineage","required realization and assessment references"],"references":[{"target":"WM-ACT-001","purpose":"Agent-scoped function, competence, proficiency and capacity"},{"target":"WM-ACT-003","purpose":"Process or workflow realization method"},{"target":"WM-ACT-034","purpose":"Capability assessment"},{"target":"WM-KNW-011","purpose":"Required-level objective or driver"},{"target":"WM-MAT-008","purpose":"Performance observation"},{"target":"WM-ORG-002","purpose":"Organizational-unit realizer"}],"excludes":["agent function, competence, proficiency or capacity","process, organizational unit, team, position or system identity","product, service, resource or budget-line identity","capability realization binding","assessment result, maturity score or performance observation","scenario or target-state projection"]},"objects":{"BusinessCapability":{"identity":["businessCapabilityId"],"required":["outcomeClass","actedUponObject","ownerRef","status"],"optional":["definition","applicability","successorRef"],"lifecycle":["proposed","approved","active","constrained","deprecated","superseded","retired"]}},"invariants":["Capability identity is outcome-defined and survives organizational and technical change.","Unit, team, position, system, product, owner name and budget line never define capability identity.","Agent Function or Competence and Business Capability never share identity or mastership.","Capability decomposition is outcome specialization.","Tier labels are versioned edge attributes and never identity.","Re-decomposition supersedes edges while capability identities remain stable.","Required level, actual level, maturity, performance and capacity remain distinct.","Actual level exists only through a finalized method-bound assessment.","A system may support a capability but cannot alone prove full realization.","Missing realization or measurement is unknown or absent, never zero.","Scenario values never become authoritative actuals.","Retired capabilities remain resolvable for historical realizations and assessments."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Capability relation contracts, scale registry and semantic crosswalks require canonical approval.","Legacy WM-ACT-001 and WM-ACT-003 boundaries require migration adjudication."]}


## candidate-allocation-offline-business-capability/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Business Capability","cases":[{"id":"reorganization-survival","kind":"positive","input":"A capability moves from unit U1 to U2 while its outcome definition remains unchanged.","expect":"Capability identity remains stable and realization bindings change."},{"id":"process-redesign","kind":"positive","input":"The process realizing a capability is replaced by a successor process.","expect":"The capability persists and the realization references the new process version."},{"id":"new-outcome-class","kind":"positive","input":"A governed ability changes to a materially different outcome class.","expect":"A successor or distinct capability is created with lineage."},{"id":"department-is-capability","kind":"negative","input":"A department name is used as capability identity.","expect":"The identity definition is rejected."},{"id":"system-is-full-capability","kind":"negative","input":"A software system alone is asserted to fully realize a business capability.","expect":"The claim is rejected without accountable non-system realization."},{"id":"tier-is-identity","kind":"negative","input":"Moving from L2 to L3 creates a new capability solely from the tier label.","expect":"The identity change is rejected."}]}


## candidate-allocation-offline-business-capability/profile-candidate.json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-STR-03","name":"Enterprise Capability Assessment and Coverage","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ACT-001","WM-ACT-034","WM-KNW-011","WM-MAT-008","WM-ORG-002","WM-ORG-003","WM-ORG-004"],"constraints":["WM-ACT-001 is narrowed to agent-scoped Function, Competence, Proficiency and Capacity and never acts as the Business Capability master.","Capability Assessment profiles WM-ACT-034 with pinned criteria, scale, aggregation, decision rule and immutable finalization.","Capability Level is a scale definition or level assertion and never an independent root.","Required level is a demand statement while actual level is a time-bounded assessment conclusion.","Maturity, performance and capacity remain separate dimensions with separate evidence.","Coverage projections distinguish unrealized, partially realized, realized-but-low-maturity and unassessed." ]}


## candidate-allocation-offline-business-capability/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## candidate-allocation-offline-capability-realization/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-STR-03","proposedName":"Capability Realization","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A temporal evidenced binding between one capability and one realizer remains identifiable across organizational transfers, process revisions and capacity changes.","versionIdentity":"Changes to realizer, role, coverage, basis, validity, accountability or evidence create successor realization bindings rather than rewriting history.","independentLifecycle":["proposed","active","constrained","suspended","transferred","superseded","ended"],"mastership":"enterprise capability-register authority"},"boundary":{"owns":["persistent capability-realization identity","capability and realizer references","realizer kind and role","coverage share and basis","validity interval","accountable party","capacity and constraint references","evidence, transfer and successor lineage"],"references":[{"target":"WM-ACT-003","purpose":"Process or method realizer"},{"target":"WM-ORG-002","purpose":"Organizational-unit realizer"},{"target":"WM-ORG-003","purpose":"Team realizer"},{"target":"WM-ORG-004","purpose":"Position realizer"},{"target":"WM-MAT-008","purpose":"Performance evidence"},{"target":"WM-ACT-034","purpose":"Capability assessment"}],"excludes":["capability or realizer identity","process, organization, position or system lifecycle","assessment result or observation identity","required or actual capability level","scenario or target realization","resource allocation or work assignment"]},"objects":{"CapabilityRealization":{"identity":["capabilityRealizationId"],"required":["capabilityRef","realizerRef","realizerKind","role","validFrom","accountablePartyRef","status"],"optional":["validTo","coverageShare","coverageBasis","capacityRef","evidenceRefs","successorRef"],"lifecycle":["proposed","active","constrained","suspended","transferred","superseded","ended"]}},"invariants":["Every realization binds one capability to one explicit realizer for an interval.","Capability and realizer identities remain externally mastered.","Transfer creates a successor binding and never rewrites prior accountability.","Realizer lifecycle changes never cascade into capability identity.","Coverage share declares basis, denominator and effective period.","Capacity is period-scoped and attaches to realization rather than capability identity.","Full realization requires an accountable non-system realizer.","A system-only binding is supporting realization unless stronger governed evidence exists.","Missing bindings mean unknown unless scoped completeness proves coverage.","Scenario and target realizations never feed authoritative actuals.","Assessment and performance evidence remain external immutable records.","Ended realizations remain resolvable for historical coverage and assessment."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Realizer-role vocabulary, completeness and coverage contracts require canonical approval.","Package conversion and live verification are pending."]}


## candidate-allocation-offline-capability-realization/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Capability Realization","cases":[{"id":"unit-transfer","kind":"positive","input":"Process P and capability C transfer accountability from U1 to U2.","expect":"R1 closes and successor R2 opens while C and P retain identity."},{"id":"partial-realization","kind":"positive","input":"Two teams realize different shares of one capability.","expect":"Separate bindings record share, basis, interval and accountability."},{"id":"system-support","kind":"positive","input":"A system supports a capability alongside an accountable operations team.","expect":"System and team bindings remain distinct and coverage is evidence-based."},{"id":"transfer-overwrites-history","kind":"negative","input":"Changing accountable unit rewrites the existing realization.","expect":"The mutation is rejected."},{"id":"system-alone-full","kind":"negative","input":"A system-only binding is labelled full realization.","expect":"The conclusion is rejected."},{"id":"missing-means-zero","kind":"negative","input":"No realization row is treated as zero coverage.","expect":"The collapse is rejected without completeness evidence."}]}


## candidate-allocation-offline-capability-realization/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}
