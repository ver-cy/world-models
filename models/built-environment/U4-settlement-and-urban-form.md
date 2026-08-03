# U4 Settlement & Urban Form

This meta-model describes cities, towns and villages and their internal spatial anatomy: districts, blocks, built-up extents, density and morphology. It is its own model because urban form is an aggregate view over buildings (U1) and networks (U3) that changes slowly, is analyzed at its own scales, and is stewarded by planning and statistical actors rather than by individual asset owners.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:u4"
  csn: world.settlementUrbanForm
  version: 0.2.0
  displayName: "Settlement & Urban Form"
  description: "Settlements, their districts and blocks, built-up extents, density and urban morphology."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.settlementUrbanForm
bundles:
  - csn: world.settlementUrbanForm.anatomy
    displayName: "Anatomy"
    layers:
      - world.settlementUrbanForm.anatomy.settlementExtent
      - world.settlementUrbanForm.anatomy.districts
      - world.settlementUrbanForm.anatomy.blocks
  - csn: world.settlementUrbanForm.morphology
    displayName: "Morphology"
    layers:
      - world.settlementUrbanForm.morphology.density
      - world.settlementUrbanForm.morphology.builtFormMetrics
  - csn: world.settlementUrbanForm.dynamics
    displayName: "Dynamics"
    layers:
      - world.settlementUrbanForm.dynamics.growth
      - world.settlementUrbanForm.dynamics.classification
imports:
  - source: citygml
    version: "*"
  - source: degurba
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `anatomy` | The spatial decomposition of a settlement | `settlementExtent`: the observed built-up footprint Â· `districts`: administrative and analytic subdivisions Â· `blocks`: the smallest street-bounded urban units |
| `morphology` | The measurable character of built form | `density`: population, coverage and floor area ratios Â· `builtFormMetrics`: grain, height mix, street pattern indicators |
| `dynamics` | How settlements change and are classified | `growth`: successive extents and expansion records Â· `classification`: assignment to settlement classification schemes |

## Objects

- `settlement`: a named inhabited place (city, town, village); key attributes: name, settlementClass, extentRef
- `district`: an administrative or analytic subdivision of a settlement; key attributes: districtKind, area
- `block`: the smallest urban unit bounded by streets or natural edges; key attributes: area, perimeter
- `urbanExtent`: the observed built-up footprint of a settlement at a date; key attributes: observedAt, area, method
- `densityMeasure`: a dated density value for a spatial unit; key attributes: measureKind, value, referenceDate
- `morphologyProfile`: a characterization of built form; key attributes: profileClass, indicators
- `classificationAssignment`: assignment of a settlement or district to a scheme term; key attributes: scheme, term, assignedAt

## Relationships

- `settlement` -> subdividedInto -> `district` (1:n): the administrative and analytic partition of a settlement
- `district` -> subdividedInto -> `block` (1:n): blocks tile each district
- `block` -> aggregates -> `building` (1:n): the buildings of U1 that stand within the block
- `settlement` -> hasExtent -> `urbanExtent` (1:n): successive extents form the growth history
- `densityMeasure` -> describes -> `district` (n:1): each measure applies to one settlement, district or block
- `settlement` -> servedBy -> `network` (n:m): the U3 networks that serve the settlement

## Events

- `extentObserved`: a new built-up extent was measured for a settlement
- `districtRedrawn`: district boundaries were changed
- `blockReplatted`: block geometry was restructured, typically after redevelopment
- `densityMeasured`: a density value was computed for a spatial unit at a reference date
- `classificationChanged`: a settlement or district moved to a different scheme term

## Contracts

- `openUrbanFormLicense`: public release of extents, blocks and density aggregates
- `planningBaselineAccess`: steward-granted access to full morphology data for plan-making
- `statisticalExchange`: delivery of aggregates to a statistics office under agreed definitions

## Projections

- `atlasProjection`: settlements, districts and extents for reference mapping; omits per-building detail
- `planningBaselineProjection`: form and density indicators for plan-making; omits any owner or occupant information
- `growthTimelapseProjection`: successive extents in time order; omits internal subdivisions

## Composition

- REFERENCE `world.buildingStructure` (U1): blocks aggregate individual buildings modelled there
- REFERENCE `world.physicalInfrastructureNetwork` (U3): the serving networks that structure urban form
- REFERENCE `world.landParcelCadastre` (P2): blocks tile the same ground as cadastral parcels; alignment is resolved through the cadastre
- REFERENCE `world.addressLocationReferencing` (U7): settlement and district names feed the place name layer there
- REFERENCE `world.observedPhenomenon` (X2): densification and growth can be published as observation series in X2
- imports: citygml (ALIGN: city object and level-of-detail semantics)
- imports: degurba (REFERENCE: degree of urbanisation classification scheme)

## Stewardship

The owner archetype is the settlement steward, a municipal planning office archetype for form records and a statistics office archetype for derived aggregates. The steward grants access per S1/S2, and published aggregates carry their scheme and reference date so consumers can detect drift.