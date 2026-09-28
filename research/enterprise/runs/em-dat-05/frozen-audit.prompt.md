# Frozen no-tools semantic audit — EM-DAT-05

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

Disposition: NEW MODEL candidate for cross-domain Metric Definition. The numeric model and runtime identifiers remain unassigned. Audit the boundary and candidate semantics only.

Audit questions:
- Does stable Metric identity remain distinct from immutable DefinitionVersion identity without duplicating observation, series, goal, target, quality or report masters?
- Are formula, unit/scale, quantity kind, population, dimensions/additivity, method/source, absence and comparability rules sufficient and mutually consistent?
- Do recalculation, restatement, missing periods, target pins and invalid aggregation preserve history and fail closed?
- Is any candidate field deployment policy or an accidental second authority?
- Which inherited holds prevent registry allocation or canonical publication while still allowing an identifier-unassigned reviewable draft?

Return at most 500 words with exactly: Verdict (ACCEPT WITH LIMITS, REVISE, or REJECT); Critical findings; Required holds; Scenario result; Identifier decision. Treat registry allocation and inherited base blockers as holds unless they contradict the candidate.

## Candidate

{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-DAT-05",
  "proposedName": "Metric Definition",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "version": "0.1.0-candidate.2",
  "identityTest": {
    "stableIdentity": "A metric exists independently of any observation, target, report or quality assessment and remains identifiable across compatible definition revisions.",
    "versionIdentity": "Each activated semantic definition is immutable and separately addressable.",
    "independentLifecycle": ["draft", "active", "superseded", "withdrawn", "tombstoned"],
    "mastership": "metric or semantic-definition registry"
  },
  "boundary": {
    "owns": [
      "stable metric identity",
      "immutable definition versions",
      "formula and expression-language binding",
      "numerator denominator base and index components",
      "metric kind quantity kind scale and comparison direction",
      "version-pinned unit reference",
      "dimensions and additivity declarations",
      "population inclusion and exclusion boundary",
      "version-pinned method and source bindings",
      "null and absence semantics",
      "facet-level compatibility and comparability declarations"
    ],
    "references": [
      {"target": "WM-XCT-025", "purpose": "Reusable observable result fields"},
      {"target": "WM-DAT-010", "purpose": "Series and observations"},
      {"target": "WM-KNW-011", "purpose": "Targets and objectives"},
      {"target": "WM-DAT-007", "purpose": "Data-quality assessments"},
      {"target": "WM-XCT-008", "purpose": "Quantity and unit values"},
      {"target": "WM-XCT-026", "purpose": "Quality-measure registration pattern only; not a metric owner"}
    ],
    "excludes": [
      "observed values or series membership",
      "target values or attainment decisions",
      "data-quality assessment lifecycle",
      "report statement or publication lifecycle",
      "procedure unit population classification or source-data mastership"
    ]
  },
  "objects": {
    "Metric": {"identity": ["metricId"], "required": ["name", "ownerRef", "status"], "optional": ["aliases", "retiredAt"], "lifecycle": ["proposed", "active", "retired"]},
    "DefinitionVersion": {"identity": ["metricId", "version"], "required": ["formula", "expressionLanguageRef", "metricKind", "unitRef", "populationBoundary", "nullSemantics", "contentDigest", "status"], "optional": ["components", "dimensions", "methodRefs", "sourceRefs", "supersedesVersion"], "lifecycle": ["draft", "active", "superseded", "withdrawn", "tombstoned"]},
    "PopulationBoundary": {"identity": ["boundaryId"], "required": ["unitOfAnalysis", "inclusionRules", "exclusionRules", "effectiveFrom"], "optional": ["effectiveTo", "classificationRefs"]},
    "DimensionRule": {"identity": ["dimensionRuleId"], "required": ["dimensionRef", "additivity", "aggregationPolicy"], "optional": ["exceptions", "hierarchyRef"]},
    "ComparabilityDeclaration": {"identity": ["declarationId"], "required": ["fromVersion", "toVersion", "verdict", "facetResults", "authorityRef", "decidedAt"], "optional": ["restatementMethodRef", "evidenceRefs"]}
  },
  "comparabilityVerdicts": ["comparable", "comparable-with-restatement", "non-comparable"],
  "absenceStates": ["zero", "unknown", "not-applicable", "missing", "suppressed"],
  "invariants": [
    "Stable metric identity is distinct from immutable definition-version identity.",
    "An activated definition version is never modified in place.",
    "A definition never stores an observed value, series head, target value or attainment verdict.",
    "Ratio and rate definitions declare numerator and denominator semantics.",
    "Unit code includes code-system identity and version; dimensionless is explicit.",
    "Each aggregable dimension declares additivity behavior; unsupported aggregation fails closed.",
    "Population unit, inclusion rules and exclusion rules are mandatory before activation.",
    "Method and source bindings are version-pinned references.",
    "Zero, unknown, not-applicable, missing and suppressed remain distinct states.",
    "A formula, method, unit, population, dimension or null-policy change creates a successor version.",
    "Every semantic change requires a facet-level comparability verdict.",
    "Absence of a comparability verdict means non-comparable.",
    "A facet-level comparability verdict may narrow but never silently widen the metric-level verdict.",
    "New quantity-kind or phenomenon semantics mint a new Metric identity rather than a definition version.",
    "Recalculation and restatement create new observation vintages and never overwrite prior observations.",
    "Equal-authority definition conflicts are never silently merged.",
    "Superseded and withdrawn versions remain resolvable and provenance-linked."
  ],
  "holds": [
    "Independent Grok review is pending.",
    "Registry identifier allocation is pending and no numeric gap may be guessed.",
    "Neighboring models retain publication holds.",
    "One frozen semantic audit is pending after provider reconciliation.",
    "Package conversion and live verification are pending."
  ]
}


## Fixtures

{
  "format": "vercy-model-allocation-fixtures/v1",
  "proposedName": "Metric Definition",
  "version": "0.1.0-candidate.2",
  "cases": [
    {"id": "method-and-population-change", "kind": "positive", "input": "Headcount/method A/population P1 changes to FTE/method B/population P2.", "expect": "Metric identity remains; a new immutable definition version is created and is non-comparable unless reconciled."},
    {"id": "missing-not-zero", "kind": "negative", "input": "One reporting period has no observation.", "expect": "The period remains missing or unknown and is never substituted with zero."},
    {"id": "recalculation", "kind": "positive", "input": "Historical source data is recalculated under a successor definition.", "expect": "New observations pin the successor version; old observations remain unchanged."},
    {"id": "invalid-aggregation", "kind": "negative", "input": "A semi-additive metric is summed over an unsupported time dimension.", "expect": "Aggregation fails closed under the dimension rule."},
    {"id": "headcount-plus-fte", "kind": "negative", "input": "Person headcount observations are summed with FTE observations.", "expect": "Aggregation is refused because quantity kind, statistical unit and definition version are not commensurable."},
    {"id": "undeclared-additivity", "kind": "negative", "input": "A metric is aggregated across a dimension with no additivity declaration.", "expect": "Aggregation is refused because undeclared is not additive."},
    {"id": "explicit-restatement", "kind": "positive", "input": "Two versions differ but an approved restatement method and evidence exist.", "expect": "Comparability is comparable-with-restatement and references the method and evidence."},
    {"id": "restatement-preserves-vintage", "kind": "positive", "input": "A published mapping restates four historical periods under a successor definition.", "expect": "Four new observation vintages are created and every prior observation remains resolvable."},
    {"id": "target-version-pin", "kind": "negative", "input": "A target bound to definition V1 is evaluated silently with V2 observations.", "expect": "Evaluation is refused until the target is explicitly rebound or a declared restatement is applied."}
  ]
}


## Local evidence

# EM-DAT-05 local synthesis

## Disposition

**NEW MODEL candidate: cross-domain Metric Definition aggregate.** The model is required because a metric definition exists before any observation or target, is referenced by records with independent lifecycles, and must preserve immutable historical versions when its formula or population changes.

The new aggregate must not absorb observations, targets, goals, quality assessments, reports, procedures, units, code lists or populations. It governs the reusable definition that those records cite.

## Proposed object boundary

Stable identity belongs to the metric. Each activated definition version is immutable and addressable. The aggregate owns only the definition-version components necessary for interpretation and comparability:

- formula and expression-language binding;
- numerator, denominator, base and index components;
- metric kind, quantity kind, scale and comparison direction;
- unit reference with version-pinned code system;
- dimensions and additivity behavior;
- population boundary with inclusion and exclusion rules;
- method and source bindings by reference;
- null/absence semantics;
- compatibility and comparability declarations between definition versions.

External records retain their own authority:

- WM-XCT-025 supplies reusable result fields;
- WM-DAT-010 owns series and observations;
- WM-KNW-011 owns targets and objectives;
- WM-DAT-007 owns data-quality assessments;
- procedure, unit, population, classification and source-data masters are referenced.

## Lifecycle

Definition version: `draft -> active -> superseded -> withdrawn/tombstoned`. Activation freezes semantics. Editorial label corrections that do not change meaning require explicit classification; formula, method, unit, population, dimension or null-policy changes always mint a successor version. Metric identity may retire but remains resolvable.

## Required invariants

1. Stable metric identity is distinct from immutable definition-version identity.
2. An activated definition version is never modified in place.
3. A definition never stores an observed value, series head, target value or attainment verdict.
4. Ratio/rate definitions declare numerator and denominator semantics.
5. Unit code includes code-system identity and version; dimensionless is explicit.
6. Each aggregable dimension declares additivity behavior; unsupported aggregation fails closed.
7. Population unit, inclusion and exclusion boundaries are mandatory before activation.
8. Method and source bindings are version-pinned references.
9. Zero, unknown, not applicable, missing and suppressed are distinct states.
10. A change to formula, method, unit, population, dimensions or null policy requires a facet-level comparability verdict.
11. Absence of a comparability verdict means non-comparable.
12. Superseded and withdrawn versions remain resolvable and provenance-linked.

## Acceptance result

For a KPI changing from headcount/method A/population P1 to FTE/method B/population P2:

- the new semantics produce a new definition version;
- the missing period remains a gap or coded missing result, never zero;
- recalculation emits new observations bound to the new definition version and retains the old observations;
- cross-version comparison is rejected unless an explicit reconciliation supports `comparable-with-restatement`;
- comparisons using the same definition version remain valid subject to coverage and observation-quality rules.

## Evidence limits

All five neighboring models are reviewable drafts and several lack independent external review or frozen relations. Standards are alignment targets only. The model identifier remains unassigned. These limits permit a bounded research candidate, but not canonical publication.


## Initial Claude study

DECISION

**NEW MODEL.** Register a new cross-domain aggregate, *Metric Definition* (identifier to be assigned; EM-DAT-05 is the contour, not the entry). The dossier shows a named hole, not a gap in an existing owner: WM-KNW-011 carries a **required** REFERENCE to an "Indicator / measure definition model (sibling; identifier to be assigned by the registry)"; WM-DAT-007 references an external "Metric Registry"; WM-DAT-010 references external "Variable … and Unit models". Three published models depend on an authority that has no entry. PROFILE and EXTEND both fail because no candidate owner's purpose admits a domain-neutral definition of a measurable quantity.

BOUNDARY PROOF

**WM-XCT-025** is `entry_kind: mixin` with no independent identity — its own aggregate-root hold states that "whether a field-group instance carries its own identifier and version must be answered". It defines *how a reported value is interpretable*, pinning unit code systems and citing a procedure by reference; it explicitly excludes method authoring and unit minting. A definition that must exist before any observation, and outlive all of them, cannot be a field group hosted on observation records.

**WM-DAT-010** owns "collection and series identity, versions, keys", observation membership and order. Its own boundary note separates "series definition, observation collection and observation", and it excludes owning "Variable, Classification, Unit … Population" masters. Absorbing the metric definition would make every definition change a series event and would force definition identity to live inside a time-series head.

**WM-KNW-011** is the decisive negative: `out_of_scope` names "Indicator/metric definitions, computation methods and data collection procedures (measure model owns these; the goal only carries a reference and target parameters)". It holds baseline, target value, operator and horizon — a commitment, not a definition. Its unassigned required reference is the hole itself.

**WM-DAT-007** does hold a finding titled "Metric definition, indicator, formula, direction, scale, unit and aggregation" — but scoped as "source-qualified **assessment** context" for a declared subject, consumer and purpose, with a purpose hold making thresholds and aggregation purpose-dependent. Its metrics are quality metrics in that bounded context; a headcount KPI is not a data-quality dimension.

**WM-DAT-002** has the closest structural content (measure/formula/unit/direction, population, DSD, series key) but is bounded to an official statistical product under a legal mandate, and its `out_of_scope` explicitly rejects "Universal domain indicator catalogues".

**Independent identity and lifecycle:** a metric definition is created before any series exists, is cited by goals, assessments and reports that have disjoint lifecycles, survives the retirement of every series that used it, and must be versioned on formula change without touching any observation. No neighbour's lifecycle can carry that.

MINIMAL CONTRACT

**Identity:** stable `metric_id` (definition-independent) + immutable `definition_version`; the version is the addressable unit, the metric is the continuity anchor.

**Owned child records:** ComponentSpec (numerator, denominator, base/index); DimensionDefinition (role, code-list reference, version pin); PopulationBoundary (unit type, inclusion, exclusion); MethodBinding (procedure reference, version, data-source bindings); NullSemanticsPolicy; ComparabilityBreak (facet, predecessor, verdict, reconciliation).

**Lifecycle:** draft → active → superseded → withdrawn/tombstoned, per version; the metric identity itself only retires. No in-place edit after activation.

**External references (non-owning):** unit and quantity-kind registry (QUDT/UCUM/Rec 20) via WM-XCT-025's pinning pattern; code-list and classification registry; procedure/method catalogue; population and statistical-unit master; WM-DAT-010 for series; WM-XCT-025 as the result field group for observations; WM-KNW-011 for targets; WM-DAT-007 for assessments; PROV-O provenance mixin.

**Core fields (14):** 1 metric_id; 2 definition_version + status + effective window; 3 canonical label and language variants; 4 metric_kind (count, ratio, rate, index, ordinal); 5 formula_expression with expression-language and version; 6 numerator_ref / denominator_ref; 7 unit_code + unit_code_system + system_version; 8 quantity_kind and scale_type; 9 declared precision and rounding rule; 10 aggregation_function + additivity class per dimension; 11 comparison_direction (polarity); 12 dimension_definition set; 13 population_boundary_ref; 14 method_binding_ref; plus null_semantics_ref, comparability_key, supersedes_ref, provenance.

**Invariants:** (1) `metric_id` is immutable across all versions; relabelling never mints identity. (2) An activated version is immutable; any change mints a new version. (3) No version carries an observed value, a current value, or a series head. (4) Ratio/rate kinds have exactly one numerator and one denominator spec; counts have none. (5) `unit_code` never appears without code system URI and pinned version; its dimension must be commensurable with the declared quantity kind; dimensionless is declared, not inferred. (6) Every dimension over which aggregation is permitted declares an additivity class; non-additive metrics refuse aggregation rather than default to sum. (7) No version activates without a PopulationBoundary stating unit type, inclusion and exclusion. (8) No version activates without a MethodBinding naming procedure, version and data-source bindings. (9) NullSemanticsPolicy enumerates zero, unknown, not-applicable, missing and suppressed as five distinct codes; no numeric sentinel, no coercion between them. (10) Any change to formula, method, unit, population or dimensions mints a version **and** a ComparabilityBreak verdict per changed facet; absence of a verdict means non-comparable (fail-closed). (11) No target value, achievement operator or baseline is stored here; targets reference versions. (12) Comparability verdicts are advisory and facet-scoped; they are never asserted for versions lacking method or population declarations. (13) Superseded and withdrawn versions remain resolvable; tombstone, never delete.

**Functions:** `issue_definition_version` (mint an immutable version with the complete descriptor set and predecessor comparability verdicts); `evaluate_comparability` (two versions × facet set × period → comparable / comparable-with-restatement / non-comparable, with reasons; advisory only); `bind_method_and_sources` (attach method, data-source bindings and null policy; refuses activation while incomplete).

ACCEPTANCE WALKTHROUGH

KPI *utilisation*, v1 (method A, headcount, population P1) and v2 (method B, FTE, population P2). **Missing period 2026-Q1:** no observation is written; the gap is WM-DAT-010's order/gap check and, where a record exists, WM-XCT-025's coded `data-absent-reason` "missing" — never 0. **Recalculation:** v2 is applied to 2025; new observations pin v2, and the v1 observations for 2025 are retained, not overwritten (WM-DAT-010's revision/supersession lineage). **Verdicts:** v2-2025 vs v2-2026 → comparable. v1-2025 vs v2-2025 → **non-comparable** on unit, method and population facets; comparable-with-restatement only if a ComparabilityBreak declares reconciliation. Any window spanning 2026-Q1 → comparable with declared coverage deficiency, never averaged over the gap. **Negative case:** headcount summed with FTE is refused at invariants 5, 7 and 10 before any arithmetic.

HOLDS AND LIMITS

Alignment is claimed as documented mapping, not conformance: SDMX dimension/measure/attribute and code-list structure (via WM-DAT-002, WM-DAT-010), QB's dataset-owns-observation separation, SOSA's observableProperty/procedure-versus-act split, QUDT/UCUM binding strictly by reference per WM-XCT-025, PROV-O for version derivation and attribution. Constraints: all five neighbours are reviewable drafts under single-provider waivers with empty or unfrozen relationship contracts, so their exclusions are declared but not enforceable; WM-DAT-007 and WM-DAT-010 admitted **no** external review (timeouts); WM-XCT-025's identity question is open; standard version pins are unverified under live-source holds. The gap rests on `catalogueSearchFinding` alone — no negative-search log was inspected.

PUBLICATION RECOMMENDATION

Register as **candidate**, `review_state: boundary-review-required`, two-provider review mandatory — no waiver, since every neighbour already carries one. Before advancing: freeze relation rows to WM-KNW-011, WM-DAT-007, WM-DAT-010 and WM-XCT-025, and have WM-KNW-011's unassigned "measure definition" reference resolved to this identifier. Publish the comparability verdict vocabulary and null-semantics code list as governed artefacts, since invariants 9 and 10 are unenforceable without them. Do not mark identity or lifecycle covered until the child-record contracts are frozen.


## Grok study

DECISION

**NEW MODEL.** No published Vercy model has compatible identity, purpose and lifecycle for a cross-domain Metric Definition master. REUSE ONLY and PROFILE are unavailable because there is no generic definition aggregate to reuse or constrain. EXTEND fails the compatible-owner test on every candidate. scepticism of a new runtime identity is warranted; the gap is still real. Do not allocate a numeric WM-DAT identifier.

BOUNDARY CHECK

WM-XCT-025 is a mixin with no standalone record. It carries result semantics (measurand binding, unit, method pin, uncertainty, absence reason, supersession). It cannot own metric identity or immutable definition versions.

WM-DAT-010 owns a governed observation collection and series context. It treats variable, indicator, measure, unit and population as external and requires series definition, collection and observation to remain separate identities. It is the right neighbour for vintages, gaps and restated observations, not the definition master.

WM-KNW-011 owns goals and target commitments. It explicitly does not own metrics or measures and binds versioned measure definitions held elsewhere. Composition identifiers for the measure sibling are unassigned. A goal may fix disaggregation, unit or population parameters; it must not redefine the measure.

WM-DAT-007 records metric, formula, scale and aggregation only as assessment context for a declared subject, purpose and time. Those fields are not a reusable indicator catalogue.

WM-DAT-002 owns official statistical products. It excludes universal indicator catalogues. A statistical product may use a metric definition; it must not become the generic master.

WM-XCT-008 and WM-XCT-026 are also not owners. Quantity/Unit is an embeddable value object. Quality/Confidence is a mixin whose registered-measure pattern is useful to cite, but it is scoped to quality assertions (DQV-style), not KPI, statistical or operational measures.

The assignment already separates formula versions from measured-result versions and forbids storing the value on the definition. That split is the identity the catalogue lacks.

MINIMAL PORTABLE CONTRACT

Own two records only.

**Metric.** Stable identity of one intended phenomenon / quantity kind. Survives rename, steward change, translation, dashboard move and target rebinding.

**MetricDefinitionVersion.** Immutable operational meaning that observations and targets pin. New version when any of these change while the phenomenon remains the same: formula or components; unit or scale, including index base and seasonal adjustment; population eligibility; dimension set or grain; additivity class; method class that changes meaning; legal absence-code set; rounding or precision that changes reported values. Editorial label, owner, access class and target binding do not mint a version.

New Metric identity when quantity kind or phenomenon changes (headcount ≠ FTE; unique visitors ≠ sessions). Correspondence between metrics is not identity continuity.

A version owns: formula or pinned procedure-class; quantity-kind and unit/scale references; dimension set and additivity declarations; population-boundary rules (target versus frame, inclusion/exclusion, double-count rule, statistical unit type); method and source-class bindings; legal absence codes; polarity only when definitional; comparability class to prior versions, including facet-level overrides.

Reference, do not own: observations, series, vintages, targets, goals, procedures, unit masters, population masters, quality assessments, official-stat products, reports.

Portable semantics are the list above. Organisation-specific KPI policy stays outside: RAG thresholds, SLO budgets, incentive links, reporting calendar, scorecard weight, local display name, approval workflow, confidentiality of reports, which source system is authoritative here.

Absence codes stay five-way distinct and are never coerced to 0 or a single null:

- zero — observed 0 with method, period and population present
- unknown — phenomenon applies; value not known
- not-applicable — cell outside eligibility
- missing — expected observation not received
- suppressed — known or computed, withheld

Censoring and limits of detection remain observation-result states (WM-XCT-025), not definition states.

Additivity is declared per named dimension and aggregation path: additive, semi-additive, non-additive, additive-after-restatement, or undeclared. Undeclared is not additive. Aggregation is refused unless quantity kind, unit/scale, statistical unit type, additivity class, population frames and comparability class all allow it. Headcount persons summed with FTE is structurally illegal.

Comparability of two versions of the same metric is declared, never inferred. Default is non-comparable.

- comparable — same operational meaning; series may concatenate
- comparable-with-restatement — a published mapping exists; restated vintages are new observations
- non-comparable — incommensurable unit, universe, additivity, method or grain

Facet-level class may narrow metric-level class; it must not silently widen it.

Invariants

1. Metric identity survives definition-version change; concept change re-identifies.
2. A published definition version is immutable; correction mints a successor plus a comparability class.
3. The measured value is never a field of the definition.
4. An observation pins definition version, method, period and population.
5. Zero, unknown, not-applicable, missing and suppressed remain distinct; no numeric sentinel.
6. Aggregation is refused unless additivity, unit/kind, statistical unit, population and comparability all allow it.
7. Missing comparability class means non-comparable.
8. Recalculation and restatement create new observation vintages; history is not overwritten.
9. Units and aggregation paths are explicit on the version.
10. Equal-authority definition conflicts are not silently merged.
11. Population and unit masters remain external; only eligibility rules and unit/scale refs are owned.
12. Many series and many goals may use one metric; neither relationship transfers ownership.

ACCEPTANCE SCENARIO

Metric M = workforce size. V1 = period-end headcount, unit person, payroll frame, additive across org unit only inside one country frame. V2 = FTE. If quantity kind or statistical unit differs, (V1, V2) is non-comparable unless a published restatement mapping exists, in which case the class is comparable-with-restatement.

Observations O(V1, 2023-Q1), O(V1, Q2), Q3 coded missing (not zero, not not-applicable), O(V1, Q4) each pin V1, method, period and population. Recalculation writes O(V2, Q1–Q4) as a new vintage. V1 rows remain. Comparing V1 Q2 with V2 Q2 is refused unless the restatement is applied. Summing V1 persons with V2 FTE is refused. A target bound to V1 is not silently re-scored on V2 values.

The new aggregate makes this decidable by giving observations something durable to pin. WM-DAT-010 owns the series, gap and vintage; WM-XCT-025 owns result-field semantics; WM-KNW-011 owns the target.

STANDARDS ALIGNMENT LIMITS

Alignment only; no conformance claim.

SDMX: Metric ≈ Concept; definition version ≈ concept plus measure, unit, methodology and OBS_STATUS vocabulary. This model is not a DSD, Dataflow or DataSet. SDMX _T / inapplicable dimensions map to not-applicable, not to missing.

RDF Data Cube: definition version may project toward qb:MeasureProperty plus component constraints. It is not a qb:Observation, qb:DataSet or qb:Slice.

SOSA/SSN: Metric is closer to ObservableProperty plus a reusable Procedure class. An observation remains the act that yields a Result for a FeatureOfInterest. Population frames and KPI additivity are outside SOSA.

QUDT / UCUM: quantity kind, unit and dimension vector are referenced, not owned. Commensurability checks belong at the reference, not as a second unit master.

PROV-O: each definition version is an Entity; successors use wasRevisionOf / wasDerivedFrom. Calculation runs are Activities that used a version and generated observations. This model does not own the provenance graph.

Loss must be declared on every projection: SDMX drops formula AST and facet-level comparability; Data Cube drops absence-code policy; SOSA drops additivity; QUDT drops population; PROV-O drops measure semantics.

PUBLICATION RECOMMENDATION

Publish as a new subject-model research draft under EM-DAT-05. Keep the two-record split. Compose by reference to WM-XCT-025, WM-XCT-008, WM-DAT-010, WM-KNW-011, WM-DAT-007 and WM-DAT-002. Cite WM-XCT-026 only as a quality-measure register pattern. Leave numeric allocation to the registry. Required fixtures: the two-method / missing-period / recalculation path; the headcount-plus-FTE negative case; a restatement vintage that does not overwrite; and an undeclared-additivity refusal.