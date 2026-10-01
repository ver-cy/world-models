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

## Reconciled provider and audit result (2026-10-01)

The exact visible Grok response independently confirms the three-root boundary, disclosure/activity reuse, run-contained results, set-contained factors and non-netting semantics. Hidden browsing is excluded. One frozen Claude Opus high no-tools audit upheld the boundary, found 14 deterministic artifact defects and supplied an exact JSON array of 38 unique additional fixtures; its narrative table incorrectly says 36. All exact JSON fixtures were preserved and all defects were remediated without rerun. No identifier was allocated and no publication readiness is claimed.
