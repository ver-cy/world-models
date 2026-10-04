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