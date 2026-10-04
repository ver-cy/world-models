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
