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
