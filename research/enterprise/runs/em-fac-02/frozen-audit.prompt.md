# EM-FAC-02 frozen semantic audit prompt

You are the sole final Claude Opus high no-tools auditor. This is exactly one frozen audit after an independent Claude study, local synthesis, and the exact visible Grok response. Do not browse, use tools, invent identifiers, claim publication readiness, or request another study.

Admitted evidence is limited to the initial Claude study, local synthesis, exact visible Grok response, and candidate artifacts appended below. Grok used hidden browsing contrary to the prompt; all hidden reasoning and sources are excluded. The visible response is complete and is admitted as text only.

Audit the settled boundary and artifacts:

- Reuse WM-ECO-034 for Sustainability Disclosure only.
- Profile Activity Data over WM-FLW-015 and WM-MAT-008; no Activity Data root.
- Inventory Boundary, Emission Factor Registry, and Environmental Impact Calculation Run are independent identifier-unassigned roots.
- Results are contained by immutable calculation runs; factor versions are contained by governed factor sets.
- Organizational, operational, and value-chain boundaries remain distinct.
- Location-based and market-based methods remain distinct and non-additive.
- Measured, estimated, modelled, allocated, and spend-proxy values remain distinguishable; financial cost never becomes an impact quantity.
- Supplier Scope 1 and buyer Scope 3 inventories are never netted across counterparties.
- No runtime or model identifier is allocated.

Return:

1. Verdict on decision and artifacts.
2. Numbered material defects, each with exact deterministic remediation.
3. A single exact JSON array of additional fixtures. Every fixture must contain `id`, `target`, `kind`, `input`, `expect`, `violates`, `closesDefect`; every negative must also contain `expectedCode`.
4. Exact final counts for prior, additional, and total fixtures, split into positive and negative.
5. Freeze decision. Do not ask for or perform a rerun.


## Initial Claude study

# Independent Review — EM-FAC-02 Impact, Sustainability and Environmental Reporting

## Verdict
Five candidates resolve to **two reuses, one profile, and three new masters (identifiers unassigned)**.

- **SustainabilityDisclosure → reuse** WM-ECO-034. It already owns disclosure and revision identity, applicability, assurance binding, publication and restatement lineage. No new identity.
- **ActivityData → profile, not new.** Consumption-type activity reuses WM-FLW-015 (assertion kind, boundary, interval, quantity/unit/conversion, meter and observation references, allocation driver and residual, gross/net components, reconciliation). Measured non-consumption quantities reuse WM-MAT-008. WM-FLW-015 already declares consumption "an activity datum for external factor, footprint or LCA calculations."
- **ImpactBoundary → new.** Independent identity, identifier unassigned.
- **EmissionFactor → new.** Independent identity, identifier unassigned.
- **ImpactCalculation → new**, as immutable run plus contained results, referencing WM-ACT-009 for the method edition and WM-ACT-053 for generic execution. Identifier unassigned.

## Evidence
WM-ECO-034 (complete), WM-FLW-015, WM-MAT-008, WM-DAT-001, WM-ORG-001, WM-ORG-012, WM-OBJ-001, WM-KNW-012; prior boundary work EM-FAC-01, EM-OPS-01, EM-DAT-04, EM-DAT-06, EM-FIN-05. Every base is a reviewable draft; four carry single-provider waivers; no approved relation edges exist.

## Identity/mastership
**ImpactBoundary** needs its own identity because one boundary version is consumed by many periods, many runs, many disclosures, and by non-disclosure consumers (procurement, operations). WM-ECO-034 asserts boundaries *per disclosure revision*, which cannot serve an inventory reused outside reporting. Its lifecycle is driven by consolidation changes and a recalculation policy, not by a reporting cycle.

**EmissionFactor** needs its own identity: distinct publisher, dataset release, vintage, geography, technology, validity window, numerator/denominator quantity kinds, uncertainty or pedigree, licence, and reuse across organizations. It is not a normative rule (WM-KNW-012), not an observation (WM-MAT-008), not a metric definition (EM-DAT-05). Structure it as FactorSet → Factor → FactorVersion, referencing WM-DAT-001 for the source dataset release and licence.

**ImpactCalculation** needs its own identity as an execution event: immutable, pinning boundary version, method edition, factor versions, activity record revisions, GWP characterization set, allocation rule and unit conversions. This mirrors the accepted Allocation Run pattern (EM-FIN-05) and Report Issue pattern (EM-DAT-06).

Reused as references: WM-ORG-001 (entities), WM-ORG-012 (control/ownership basis), WM-OBJ-001 (shared asset instance), WM-KNW-012 with WM-KNW-013 (allocation rule, significance threshold, recalculation policy), EM-DAT-05 (metric definition).

## Disclosure/boundary
Disclosure is a **reported assertion**; boundary is an **inventory scope**. WM-ECO-034 must narrow to asserting a reported value that *cites* a run, and must not own factor, calculation or boundary lifecycles — which its own boundary notes already require but its scope statement contradicts.

Three separately versioned boundaries: **organizational** (entities in scope and consolidation approach — equity share, financial control, operational control), **operational** (which sources within those entities, and Scope 1/2/3 classification), **value-chain** (per-category upstream/downstream inclusion with coverage percentage and exclusions). None implies another. Equity share attributes a share of each source; control approaches attribute 100% of controlled sources and push the remainder to Scope 3. Changing approach changes results without any physical change.

## Activity data
Every activity record carries: assertion kind (measured, metered, derived, allocated, estimated, modelled, spend-proxy), quantity kind and unit, interval, boundary reference, source evidence, completeness of the base population, and uncertainty. Measured and estimated are never merged into one field. Missing data is never zero. Spend is an explicitly labelled proxy quantity, not a physical one.

## Factor registry
Required on every FactorVersion: publisher, dataset release, reference year, geography, technology or activity match, numerator and denominator quantity kinds, source method (supplier-specific, grid average, residual mix, spend-based EEIO), uncertainty or pedigree, validity window, licence, supersession link. GWP characterization (AR5/AR6, GWP100) is a **separate characterization set**, not an emission factor; CO₂e conversion is a second, separately pinned multiplication. Proxy or substituted factors record a representativeness downgrade on the run, not on the factor.

## Calculation/result
A run is immutable and pins: boundary version, method edition, activity record revisions, factor versions, characterization set, allocation rule version, conversion table, executor, execution time. Results name scope, category, gas, quantity, unit, method kind, coverage, uncertainty and excluded residual. Corrections append successor runs; predecessors remain resolvable. A run is not a disclosure and not a posting.

## Units/method/uncertainty
Conversions are recorded with factor, direction and authority (UN/CEFACT Rec 20, QUDT, UCUM via WM-FLW-015 alignment). Activity uncertainty, factor uncertainty and representativeness are recorded separately and never collapsed into one score. Coverage percentage and exclusion list accompany every aggregate. Location-based and market-based results are two results of one activity record: both valid, **non-additive**, never summed or averaged; market-based without a retired instrument uses residual mix.

## Double counting/allocation
Each participant's inventory is valid in its own boundary. A supplier's Scope 1 appearing as a buyer's Scope 3 Category 1 is **by design, not double counting**, and must not be netted or deduplicated across counterparties. Double counting is an error only *within* one boundary and one axis:

1. Uniqueness invariant: one source/asset/interval maps to exactly one (boundary version, scope, category) triple per run.
2. Shared assets: apportionment with declared driver, residual, and total share ≤ 1 among participants under the same consolidation approach; a counterparty's claimed share is stored as an assertion, never as truth.
3. Market instruments: unique claim enforced by certificate retirement or cancellation reference.
4. Cross-organization aggregation is declared non-additive, like parallel allocation axes.

## Time/version/recalculation
Separate clocks: activity interval, factor validity, characterization set version, reporting period, run time, disclosure issue time, restatement time. Base year is a boundary-scoped fact with a recalculation policy (WM-KNW-012 statement, threshold in WM-KNW-013). A structural change triggers recalculation; the recalculated base year is published beside the original with both versions resolvable.

## Assurance/publication
Assurance engagement, scope, level and conclusion remain external and reference specific run and result versions, not the whole disclosure. Approval, assurance, filing, publication and compliance stay independent states (WM-ECO-034 holds this correctly). Publication and filing map to WM-REC-002 and WM-ACT-044 patterns; WM-ECO-033 remains a provisional parent with no settled edge.

## Acceptance scenario
Run 1: location-based, grid average factor, AR6 GWP100, operational-control boundary v2 → result R1. Run 2: same activity records, market-based, supplier-specific plus residual mix → R2. R1 and R2 differ, are both explainable, and are flagged non-additive. Boundary v3 switches to equity share and divests a site. Run 3 produces R3 plus a recalculated base year. A bridge record decomposes R3 − R1 into boundary change, method change, factor vintage change and activity change. Comparability flag: **non-comparable**. Nothing is silently restated.

**Negative case rejected:** cloud spend is admitted only as an estimated spend-proxy activity with EEIO factor, currency, year, deflator, wide uncertainty and low representativeness. It is never labelled measured, never supports a market-based claim, and is not comparable with a kWh-based supplier-specific result.

## Invariants
1. Every result pins boundary, method edition, factor versions and characterization set.
2. Units are compatible; conversions are recorded with authority.
3. Measured, metered, derived, allocated, estimated and proxy are separately labelled.
4. Missing data is never zero.
5. Organizational, operational and value-chain boundaries do not imply one another.
6. Location-based and market-based results are non-additive.
7. One source/interval maps to one scope/category per boundary version.
8. Shared-asset shares total ≤ 1 within one consolidation approach.
9. Market claims require a unique instrument retirement reference.
10. Cross-counterparty inventories are never netted.
11. Runs are immutable; corrections append successors.
12. Financial cost is never an impact quantity.
13. Coverage and exclusions accompany every aggregate.
14. Boundary change triggers recalculation and a non-comparability flag.
15. A disclosure cites a run; it never substitutes for one.

## Minimal model set
Reuse: WM-ECO-034, WM-FLW-015 (activity profile), WM-MAT-008, WM-DAT-001, WM-ORG-001, WM-ORG-012, WM-OBJ-001, WM-KNW-012/013, WM-ACT-009, WM-ACT-053, EM-DAT-05. New, identifiers unassigned: ImpactBoundary, EmissionFactor (set/factor/version), ImpactCalculation (run plus results).

## Holds
"Impact" is overloaded: WM-ECO-034 uses it for materiality effects on people and environment; EM-FAC-02 uses it for quantified emissions. Rename the new candidate to an inventory-quantification sense before allocation. WM-ECO-034's scope statement contradicts its own out-of-scope list on metric definitions, calculations and factors. WM-MAT-008's uncertainty and traceability layer is unreachable through its function set, weakening the uncertainty dependency. WM-ORG-012 is Codex-only with proposed edges only, so consolidation basis rests on unapproved relations. No home exists for the GWP characterization set, nor for assurance engagement identity. No approved relation edges, no fixtures, no source pins. This is a research adjudication only: no canonical completeness, installability or publication readiness is claimed.


## Local synthesis

# EM-FAC-02 local synthesis

## Disposition

- Reuse WM-ECO-034 as Sustainability Disclosure and require it to cite external calculation results.
- Profile Activity Data over WM-FLW-015 for consumption quantities and WM-MAT-008 for other measured quantities.
- Propose identifier-unassigned **Inventory Boundary**, **Emission Factor Registry** and **Environmental Impact Calculation Run** roots. The narrower names avoid conflating quantified inventories with every social or environmental impact assertion.
- Keep results contained in the calculation run and factor versions contained in a governed factor set.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Inventory Boundary needs independent identity because one version can support many periods, calculations, disclosures and operational or procurement uses. Its lifecycle follows consolidation changes and recalculation policy, not a disclosure issue cycle.

Emission Factor Registry has publisher, dataset release, vintage, geography, technology, validity, units, uncertainty, licence and supersession independent of any calculation. Environmental Impact Calculation Run is an immutable execution that pins all inputs and produces contained results.

Organizations, relationships, assets, source datasets, observations, resource-consumption facts and policies remain externally mastered. WM-ECO-034 owns the reported disclosure revision, not those facts or calculation lifecycles.

## Disclosure and boundary

Disclosure is a reported assertion. Inventory Boundary defines what the calculation includes. WM-ECO-034 must cite the boundary and run rather than reproduce their histories.

Organizational boundary states included entities and consolidation approach such as equity share, financial control or operational control. Operational boundary classifies sources into Scope 1, 2 and 3. Value-chain boundary declares upstream/downstream categories, coverage and exclusions. None implies another.

A change from control to equity-share treatment changes attribution without physical activity changing and therefore creates a successor boundary and possible base-year recalculation.

## Activity data

Activity records declare measured, metered, derived, allocated, estimated, modelled or spend-proxy status; quantity kind and unit; interval; source evidence; completeness; uncertainty and boundary reference.

Measured and estimated values never share an undifferentiated field. Missing data is unknown, not zero. Spend is an explicitly labelled proxy and never a physical measurement.

## Factor registry

Every Factor Version records publisher, source dataset and release, reference year, geography, technology/activity match, numerator and denominator quantity kinds, method class, uncertainty or pedigree, validity interval, licence and supersession.

GWP characterization is a separate versioned set rather than an emission factor. CO2e conversion therefore pins both the emission factor and characterization set. Proxy substitutions record representativeness downgrade on the calculation run.

## Calculation and result

An immutable run pins boundary version, method edition, activity revisions, factor versions, characterization set, allocation rule, conversion table, executor and execution time. Results declare scope, category, gas, quantity, unit, method, coverage, uncertainty and excluded residual.

Corrections produce successor runs. A run is neither a disclosure nor a financial posting. A disclosure cites selected result revisions.

## Units, methods and uncertainty

Unit conversions record factor, direction, authority and version. Activity uncertainty, factor uncertainty, coverage and representativeness remain separate dimensions.

Location-based and market-based calculations may use one activity record but produce non-additive results. A market-based result without a uniquely retired instrument uses an appropriate residual mix and discloses the limitation.

Financial cost is never an impact quantity. Cloud spending may support a spend-proxy estimate with an EEIO factor, currency-year normalization, broad uncertainty and low representativeness; it cannot be labelled measured emissions.

## Double counting and allocation

A supplier's Scope 1 and a buyer's Scope 3 Category 1 are both valid in their own boundaries and are not netted across counterparties. Double counting is checked within one boundary and reporting axis.

Each source, asset and interval maps once to a boundary version, scope and category per run. Shared assets use a declared driver and residual; shares total at most 1.0 under one consolidation approach. Market claims require unique retirement or cancellation evidence. Cross-organization aggregates remain explicitly non-additive.

## Time, version and recalculation

Activity interval, factor validity, characterization release, reporting period, run time, disclosure issue and restatement time remain distinct. Base year is boundary-scoped and cites a versioned recalculation policy.

Structural changes trigger a successor boundary and recalculated base-year result. Original and recalculated versions remain resolvable, with a bridge decomposing differences into boundary, method, factor and activity changes.

## Assurance and publication

Assurance engagement, scope, level and conclusion remain external and pin specific run and result versions. Approval, assurance, filing, publication and compliance are separate states. Publication never turns an estimate into an observation or makes a result true by itself.

## Acceptance result

Run R1 uses operational-control boundary v2, location-based grid factors and AR6 GWP100. R2 uses the same activity with market-based supplier factors plus residual mix. Both are valid and non-additive. Boundary v3 changes to equity share and removes a site; R3 and a recalculated base year are produced. A bridge explains method, factor, boundary and activity differences and marks R1/R3 non-comparable. No prior result is silently rewritten.

## Required invariants

1. Every result pins boundary, method, factor and characterization versions.
2. Units are compatible and conversions cite authority.
3. Measured, derived, allocated, estimated and proxy values stay distinct.
4. Missing data is never zero.
5. Organizational, operational and value-chain boundaries remain separate.
6. Location- and market-based results are non-additive.
7. One source/interval maps once per boundary and reporting axis.
8. Shared-asset shares total at most 1.0 within one approach.
9. Market claims cite unique retirement evidence.
10. Counterparty inventories are not netted across boundaries.
11. Runs are immutable and corrected by successors.
12. Financial cost never substitutes for impact quantity.
13. Coverage and exclusions accompany aggregates.
14. Boundary change triggers recalculation and comparability review.
15. A disclosure cites a calculation; it does not replace it.

## Holds

Inventory Boundary, Emission Factor Registry and Environmental Impact Calculation Run have no registry allocations. WM-ECO-034's scope overlaps external metric, factor and calculation masters despite contrary boundary notes. No allocated home exists for GWP characterization sets or assurance-engagement identity. WM-MAT-008 uncertainty linkage and WM-ORG-012 consolidation relations remain incomplete. Relations, fixtures and source pins are unapproved or missing, and the bases remain non-canonical drafts. No installability or publication-readiness claim is made.


## Exact visible Grok response

Verdict: Accept the proposal. Reuse WM-ECO-034 for disclosure only. Profile Activity Data on WM-FLW-015 and WM-MAT-008. Allocate independent, identifier-unassigned roots to Inventory Boundary, Emission Factor Registry, and Environmental Impact Calculation Run. No other identifier. Results stay run-contained; factor versions stay set-contained. This is an assessment of the proposal, not a publication-readiness claim.

Strongest evidence: The five EM-FAC-02 subjects are different lifecycle objects. A disclosure cites an inventory; it does not choose consolidation approach, hold activity, version factors, or own a calculation. Organizational boundary (equity vs control) is a dated decision, not the organization master. Location-based and market-based Scope 2 are dual methods over the same activity. Factor source and version must be reusable across runs. A result that is not frozen with its boundary snapshot, activity selection, method, and factor-set version cannot explain a later difference without restating history.

Strongest counterexample: A cloud invoice amount treated as measured kilowatt-hours, multiplied by a grid factor, and stored as the activity’s emissions. Spend is a financial proxy, not a measured energy quantity. The same invoice can support a location-based run and a market-based run with unequal results. Collapsing spend-proxy into measured, or writing one emissions number onto the consumption master, fails quantity-versus-cost separation and makes the two methods silently comparable. A second failure of the same class is eliminating a supplier’s valid Scope 1 because the buyer recorded Scope 3 for the same physical flow.

Identity/mastership: Three candidates need independent roots. Inventory Boundary is not the organization master, not a relationship, and not a disclosure: it records consolidation approach, operational scope, value-chain inclusion, period, exclusions, and base-year policy. Emission Factor Registry is not a dataset of observations and not a run: it holds source, version, geography, gas, GWP set, unit, validity, and residual versus grid-average character, with versions set-contained. Environmental Impact Calculation Run is not a disclosure and not a factor set: it pins the boundary version, activity snapshot, factor-set version, method, conversions, allocation, coverage, uncertainty, and evidence, and contains its results. Activity Data does not get a root. Assurance and filing do not get roots inside EM-FAC-02.

Disclosure/boundary: WM-ECO-034 remains the publication surface and references one or more runs. It does not own boundary, activity, factors, calculation, assurance, or filing. Organizational boundary (equity share, financial control, operational control) is separate from operational boundary (scopes) and from value-chain boundary. A control approach and an equity approach are alternative consolidations, not attributes of the legal entity.

Activity data: Profile on resource consumption and observation. Each use carries quantity, unit, period, source evidence, and an exclusive quality class: measured, estimated, or spend-proxy. Cloud spend remains spend-proxy. It cannot be labeled measured emissions. Impact quantity is not the financial cost on the same record.

Factor registry: A factor is identifiable by source and version, not by a floating name. Geography, gas, GWP set, unit, and validity sit on the set version. A run references that version; it does not copy an unversioned factor that can change later.

Calculation/result: Results exist only inside the run that produced them. Two methods on one activity snapshot are two runs. A boundary change is a new run. Prior results stay immutable and are labeled non-comparable, not restated.

Units/method/uncertainty: The run pins method (including location-based versus market-based), factor source and version, activity units, impact units, conversion factors, GWP set, uncertainty, coverage, allocation rule, exclusions, and evidence. Incompatible units block the run. Missing method pin or missing factor version blocks the run.

Double counting/allocation: Supplier Scope 1 and buyer Scope 3 may both be valid inventories. No cross-counterparty netting or elimination. Intercompany and value-chain allocation is an explicit rule on the run. Absence of a rule is not permission to add the same physical flow twice inside one inventory or to drop either counterparty’s inventory.

Time/version/recalculation: Boundary version, factor-set version, and activity snapshot are pinned. Recalculation policy (structural change, base year, significance) is declared and applied only by creating a new run. Published totals are not overwritten when a later boundary or factor set appears.

Assurance/publication: Assurance opinion and filing act are outside the run and outside the reused disclosure master. Disclosure may cite assured runs; assurance does not become an attribute that rewrites results.

Scenario: Same activity snapshot and boundary B1 produce run R1 (location-based) and run R2 (market-based). Results differ and are both retained. A later shift from operational control to equity share is boundary B2 and run R3. R1 and R2 remain explainable and are not comparable to R3. No silent restatement. A cloud invoice amount never enters R1 or R2 as measured tCO2e.

Invariants:
1. Disclosure does not own boundary, activity, factors, results, assurance, or filing.
2. Organizational, operational, and value-chain boundaries are distinct.
3. Equity share, financial control, and operational control are alternative approaches.
4. Location-based and market-based methods are distinct pins; neither overwrites the other.
5. Measured, estimated, and spend-proxy are exclusive quality classes.
6. Spend-proxy is not measured emissions; cloud spend fails as exact measured emissions.
7. Impact quantity is distinct from financial cost.
8. Factor identity includes source and version; referenced set versions are immutable.
9. Results are run-contained; recalculation creates a new run.
10. A boundary or method change does not silently restate prior runs.
11. Units, conversions, GWP, uncertainty, coverage, allocation, exclusions, and evidence are pinned on the run.
12. Supplier Scope 1 and buyer Scope 3 may coexist; no cross-counterparty netting.
13. Coverage gaps and exclusions are stated, not implied by missing rows.
14. Assurance and filing cannot mutate a closed run.

Minimum model set: reused WM-ECO-034; Activity Data profiled on WM-FLW-015 and WM-MAT-008; new Inventory Boundary; new Emission Factor Registry; new Environmental Impact Calculation Run; links only to already drafted organization, relationship, physical-item, policy/rule, and dataset masters.

Blockers: activity quality class cannot be carried without collapsing into cost; factor source, version, GWP, geography, or gas cannot be pinned apart from the run; consolidation approach exists only as org hierarchy; a result is stored on the activity or factor; boundary or factor change overwrites a prior total; supplier Scope 1 is netted against buyer Scope 3.


## Inventory Boundary allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-FAC-02","proposedName":"Inventory Boundary","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"One governed inventory boundary persists across reporting periods, calculation runs, disclosures and recalculations.","versionIdentity":"Consolidation approach, included entities, operational scope, value-chain coverage or recalculation policy changes create immutable successor revisions.","independentLifecycle":["draft","approved","effective","superseded","retired"],"mastership":"sustainability inventory-governance authority"},
"boundary":{"owns":["stable boundary identity","organizational consolidation approach","operational scope classification","value-chain coverage and exclusions","base-year and recalculation policy","immutable revisions and comparability lineage"],"references":[{"target":"WM-ORG-001","purpose":"Included organization identities"},{"target":"WM-ORG-012","purpose":"Group and consolidation context"},{"target":"WM-OBJ-001","purpose":"Included asset identities"},{"target":"WM-FLW-015","purpose":"Consumption activity inside the boundary"},{"target":"WM-ECO-034","purpose":"Disclosures citing boundary revisions"}],"excludes":["activity and observation facts","emission-factor identity","calculation execution and results","disclosure lifecycle","assurance engagement"]},
"objects":{"InventoryBoundary":{"identity":["inventoryBoundaryId"],"required":["name","ownerRef","status","currentRevisionRef"],"optional":["successorRef"],"lifecycle":["draft","approved","effective","superseded","retired"]},"BoundaryRevision":{"identity":["inventoryBoundaryId","revision"],"required":["consolidationApproach","includedEntityRefs","operationalScopes","valueChainCoverage","exclusions","recalculationPolicyRef","effectiveFrom","contentDigest"],"optional":["effectiveTo","supersedesRevision","baseYear"]}},
"invariants":["Organizational, operational and value-chain boundaries remain separate facets.","Every calculation pins one immutable boundary revision.","A consolidation-method change creates a successor revision.","Boundary revision never rewrites source activity.","Missing boundary coverage is never inferred as zero.","Each source, asset and interval maps once per boundary and reporting axis.","Shared-asset shares total at most one within one consolidation approach.","Base year is boundary-scoped and cites a recalculation policy.","Structural change triggers recalculation and comparability review.","Original and recalculated results remain resolvable.","Boundary bridge distinguishes boundary, method, factor and activity effects.","Disclosure cites a boundary revision and never owns it.","Access and confidentiality follow source masters.","Retired boundary identifiers and revisions are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review is pending.","Consolidation relations and characterization-set authority remain incomplete.","Frozen audit, relation approvals and source pins remain pending."]}


## Enterprise sustainability profile candidate

{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-FAC-02","name":"Enterprise Sustainability Activity and Disclosure Binding","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ECO-034","WM-MAT-008","WM-FLW-015","WM-DAT-001","WM-ORG-001","WM-ORG-012","WM-OBJ-001","WM-KNW-012"],"constraints":["WM-ECO-034 owns disclosure revisions and cites external boundaries and calculation results.","WM-FLW-015 owns consumption quantities while WM-MAT-008 owns other measured observations.","Activity data states measured, derived, allocated, estimated, modelled or spend-proxy status explicitly.","Missing data remains unknown and financial spend never becomes a physical impact measurement.","Approval, assurance, filing, publication and compliance remain separate states.","Disclosure publication never changes evidence quality or calculation truth."],"holds":["Three new roots remain unassigned.","WM-ECO-034 overlap and assurance mastership require reconciliation.","Independent Grok review and frozen audit remain pending."]}


## Inventory Boundary fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Inventory Boundary","cases":[{"id":"control-to-equity","kind":"positive","input":"A boundary changes from operational control to equity share.","expect":"A successor revision and base-year recalculation preserve the prior boundary and bridge attribution differences."},{"id":"parallel-market-location","kind":"positive","input":"One activity set supports location- and market-based calculations.","expect":"Both results pin the same boundary revision and remain non-additive."},{"id":"site-removal","kind":"positive","input":"A successor boundary excludes one sold site.","expect":"The structural change triggers recalculation and comparability review."},{"id":"scope-collapse","kind":"negative","input":"Organizational, operational and value-chain boundaries are stored as one undifferentiated scope.","expect":"The boundary is rejected because the facets have different semantics."},{"id":"missing-is-zero","kind":"negative","input":"Uncovered supplier activity is counted as zero.","expect":"The result is rejected because missing coverage is unknown."},{"id":"double-map","kind":"negative","input":"One source interval maps twice to Scope 1 in the same axis.","expect":"The run is rejected for within-boundary double counting."},{"id":"rewrite-boundary","kind":"negative","input":"A new consolidation approach overwrites the prior boundary revision.","expect":"The mutation is rejected; a successor and bridge are required."}]}


## Inventory Boundary validation policy

{
  "format": "vercy-allocation-validation/v1",
  "requirements": {
    "modelIdMustBeNull": true,
    "registryIdMustBeNull": true,
    "allocationState": "unassigned",
    "minimumInvariants": 8,
    "minimumReferences": 3,
    "minimumFixtures": 3,
    "requiresPositiveAndNegativeFixtures": true,
    "requiresStableIdentityStatement": true,
    "requiresIndependentLifecycle": true
  }
}


## Emission Factor Registry allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-FAC-02","proposedName":"Emission Factor Registry","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"A governed factor registry and factor set persist independently of any calculation run or disclosure.","versionIdentity":"Publisher releases, vintage, geography, technology, method, units, uncertainty, licence or supersession changes create immutable factor versions.","independentLifecycle":["draft","published","effective","superseded","withdrawn","retired"],"mastership":"emission-factor publisher or governed registry"},
"boundary":{"owns":["registry and factor-set identity","immutable factor versions","publisher and source release provenance","quantity kinds, units, validity and uncertainty","licence, geography, technology and supersession"],"references":[{"target":"WM-DAT-001","purpose":"Source dataset identity and release"},{"target":"WM-MAT-008","purpose":"Measured or derived factor observations"},{"target":"WM-KNW-012","purpose":"Method and provenance documentation"},{"target":"WM-ECO-034","purpose":"Disclosures citing results derived from factors"}],"excludes":["activity facts","inventory boundary","calculation run and result","GWP characterization-set identity","disclosure and assurance lifecycle"]},
"objects":{"EmissionFactorRegistry":{"identity":["factorRegistryId"],"required":["publisherRef","name","status","currentReleaseRef"],"optional":["licenceRef","successorRef"],"lifecycle":["draft","published","effective","superseded","withdrawn","retired"]},"FactorVersion":{"identity":["factorRegistryId","factorId","version"],"required":["sourceDatasetRef","referenceYear","geography","activityMatch","numeratorKind","denominatorKind","methodClass","uncertainty","validFrom","contentDigest"],"optional":["validTo","technology","supersedesRef","licenceRef"]}},
"invariants":["Every factor version names publisher and source dataset release.","Numerator and denominator quantity kinds and units are explicit.","Validity, vintage, geography and technology match are explicit.","Factor uncertainty and pedigree remain separate from activity uncertainty.","Proxy substitution records a representativeness downgrade.","GWP characterization set remains separately versioned.","CO2e conversion pins both factor and characterization versions.","A factor version never owns source activity or calculation results.","Licence and reuse restrictions propagate to derived evidence.","Withdrawn factors remain resolvable for historical runs.","Unit conversions cite direction, authority and version.","Financial cost never substitutes for an impact factor without an explicit spend-proxy method.","Corrections create successor versions and preserve cited history.","Registry identifiers and factor versions are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review is pending.","No allocated characterization-set master exists.","Frozen audit, source pins and crosswalks remain pending."]}


## Emission Factor Registry fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Emission Factor Registry","cases":[{"id":"factor-version-pin","kind":"positive","input":"A run uses a 2024 regional grid factor and AR6 GWP100.","expect":"It pins the factor version and separate characterization-set version."},{"id":"factor-successor","kind":"positive","input":"The publisher replaces a factor after methodology correction.","expect":"A successor version preserves historical citations."},{"id":"proxy-downgrade","kind":"positive","input":"A technology-specific factor is unavailable and a regional proxy is used.","expect":"The run records proxy substitution and representativeness downgrade."},{"id":"factor-without-units","kind":"negative","input":"A factor lacks denominator quantity kind and unit.","expect":"The factor is rejected as dimensionally unusable."},{"id":"gwp-embedded","kind":"negative","input":"A CO2e factor hides the GWP characterization release.","expect":"The result is rejected because characterization must be separately pinned."},{"id":"overwrite-factor","kind":"negative","input":"A corrected factor overwrites the cited 2023 version.","expect":"The mutation is rejected; successor lineage is required."},{"id":"cost-is-emissions","kind":"negative","input":"Cloud spend is labelled measured emissions without an EEIO method.","expect":"The claim is rejected; spend is only an explicit proxy with uncertainty."}]}


## Emission Factor Registry validation policy

{
  "format": "vercy-allocation-validation/v1",
  "requirements": {
    "modelIdMustBeNull": true,
    "registryIdMustBeNull": true,
    "allocationState": "unassigned",
    "minimumInvariants": 8,
    "minimumReferences": 3,
    "minimumFixtures": 3,
    "requiresPositiveAndNegativeFixtures": true,
    "requiresStableIdentityStatement": true,
    "requiresIndependentLifecycle": true
  }
}


## Environmental Impact Calculation Run allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-FAC-02","proposedName":"Environmental Impact Calculation Run","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"Each calculation execution has immutable identity independent of its disclosure and source facts.","versionIdentity":"Corrections or changed inputs create successor runs rather than editing a completed execution.","independentLifecycle":["planned","running","completed","failed","superseded","retired"],"mastership":"environmental inventory calculation authority"},
"boundary":{"owns":["immutable calculation execution identity","pinned boundary, method, activity, factor and characterization inputs","executor and execution time","contained scoped results, coverage, uncertainty and residuals","reconciliation and successor lineage"],"references":[{"target":"WM-ECO-034","purpose":"Disclosure revisions selecting calculation results"},{"target":"WM-FLW-015","purpose":"Consumption activity inputs"},{"target":"WM-MAT-008","purpose":"Other measured activity inputs"},{"target":"WM-DAT-001","purpose":"Pinned source datasets"},{"target":"WM-OBJ-001","purpose":"Source assets"}],"excludes":["source activity identity","factor-registry identity","inventory-boundary identity","disclosure lifecycle","financial posting","assurance engagement"]},
"objects":{"ImpactCalculationRun":{"identity":["calculationRunId"],"required":["boundaryRevisionRef","methodEditionRef","activityRevisionRefs","factorVersionRefs","characterizationSetRef","executorRef","executedAt","status"],"optional":["allocationRuleRef","conversionTableRef","successorRunRef"],"lifecycle":["planned","running","completed","failed","superseded","retired"]},"ImpactResult":{"identity":["calculationRunId","resultId"],"required":["scope","category","gasOrImpactKind","quantity","unit","method","coverage","uncertainty"],"optional":["excludedResidual","sourceRefs"]}},
"invariants":["Every result pins boundary, method, factor and characterization versions.","Units are compatible and conversions cite authority.","Measured, derived, allocated, estimated and proxy inputs remain distinct.","Missing data is never zero.","Location- and market-based results are non-additive.","One source interval maps once per boundary and axis.","Market claims cite unique retirement evidence.","Counterparty inventories are not netted across boundaries.","Runs are immutable and corrected by successors.","A run is neither a disclosure nor a financial posting.","Coverage and exclusions accompany aggregates.","Activity, factor, representativeness and coverage uncertainty stay separate.","Disclosure cites selected result revisions without copying their history.","Run and contained-result identifiers are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review is pending.","Boundary, factor-registry and characterization-set allocations are unresolved.","Assurance identity, frozen audit, relations and fixtures remain pending."]}


## Environmental Impact Calculation Run fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Environmental Impact Calculation Run","cases":[{"id":"dual-method-runs","kind":"positive","input":"One activity record produces location- and market-based results.","expect":"Two non-additive results pin their own factor and market-evidence inputs."},{"id":"successor-run","kind":"positive","input":"A factor correction requires recalculation.","expect":"A successor run preserves original inputs and results."},{"id":"shared-asset-residual","kind":"positive","input":"A shared asset is allocated 90 percent across targets.","expect":"Results total 0.9 and the remaining 0.1 is exposed as residual."},{"id":"missing-as-zero","kind":"negative","input":"Unreported activity is silently treated as zero.","expect":"The run is rejected because missing coverage must remain explicit."},{"id":"cross-boundary-netting","kind":"negative","input":"Supplier Scope 1 is netted against buyer Scope 3.","expect":"The run is rejected because counterparty inventories are not netted."},{"id":"mutate-completed-run","kind":"negative","input":"A corrected factor replaces results inside a completed run.","expect":"The mutation is rejected; a successor run is required."},{"id":"run-is-posting","kind":"negative","input":"An impact result is recorded as a ledger posting without a journal entry.","expect":"The substitution is rejected."}]}


## Environmental Impact Calculation Run validation policy

{
  "format": "vercy-allocation-validation/v1",
  "requirements": {
    "modelIdMustBeNull": true,
    "registryIdMustBeNull": true,
    "allocationState": "unassigned",
    "minimumInvariants": 8,
    "minimumReferences": 3,
    "minimumFixtures": 3,
    "requiresPositiveAndNegativeFixtures": true,
    "requiresStableIdentityStatement": true,
    "requiresIndependentLifecycle": true
  }
}

