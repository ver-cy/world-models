# P10 Soil & Agricultural Land

This meta-model describes soil as a mapped, sampled and classified resource and the agricultural capability that follows from it: profiles and horizons, laboratory chemistry and physical properties, capability and suitability ratings, and the degradation, contamination and management history that change land condition over time. It is its own model because soil is a slow-moving stock that is measured at points, mapped as units and managed as fields, three grains that must be reconciled explicitly. Farming as an activity is modelled in K9, the land unit as a registrable object in P2.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p10"
  csn: world.soilAndAgriculturalLand
  version: 0.2.0
  displayName: "Soil & Agricultural Land"
  description: "Soil profiles, map units and laboratory properties with agricultural capability, suitability and land condition over time."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.soilAndAgriculturalLand
bundles:
  - csn: world.soilAndAgriculturalLand.soilResource
    displayName: "Soil resource"
    layers:
      - world.soilAndAgriculturalLand.soilResource.profileAndHorizon
      - world.soilAndAgriculturalLand.soilResource.classificationUnit
      - world.soilAndAgriculturalLand.soilResource.soilMapping
  - csn: world.soilAndAgriculturalLand.fertility
    displayName: "Fertility and capability"
    layers:
      - world.soilAndAgriculturalLand.fertility.chemistryAndNutrient
      - world.soilAndAgriculturalLand.fertility.physicalProperty
      - world.soilAndAgriculturalLand.fertility.capabilityAndSuitability
  - csn: world.soilAndAgriculturalLand.condition
    displayName: "Land condition"
    layers:
      - world.soilAndAgriculturalLand.condition.degradationProcess
      - world.soilAndAgriculturalLand.condition.contaminationStatus
      - world.soilAndAgriculturalLand.condition.managementPractice
imports:
  - source: fao-soil-classification
    version: "*"
  - source: iuss-world-reference-base
    version: "*"
  - source: iso-28258-soil-data-exchange
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `soilResource` | What the soil is and where each kind occurs | `profileAndHorizon`: described profiles, their horizons and diagnostic features · `classificationUnit`: classification terms assigned to profiles and units · `soilMapping`: map units, polygons and digital soil property surfaces with their uncertainty |
| `fertility` | What the soil can support | `chemistryAndNutrient`: organic carbon, nutrients, pH, salinity and cation exchange · `physicalProperty`: texture, bulk density, structure, depth and water holding capacity · `capabilityAndSuitability`: capability classes and crop-specific suitability ratings with their limiting factors |
| `condition` | How land condition changes and why | `degradationProcess`: erosion, compaction, salinization, acidification and organic matter loss · `contaminationStatus`: contaminant findings, thresholds exceeded and remediation state · `managementPractice`: tillage, cover, amendment and irrigation practice as it bears on soil state |

## Objects

- `soilUnit`: a mapped soil unit; key attributes: unit identifier, geometry, dominant classification term, component proportions, map scale, purity
- `soilProfile`: a described profile at a site; key attributes: site coordinates, description date, depth described, classification assigned, describer reference
- `soilHorizon`: a layer within a profile; key attributes: depth interval, horizon designation, colour, texture class, structure, diagnostic features
- `soilSample`: material taken for analysis; key attributes: sample identifier, source horizon reference, depth interval, sampling date, laboratory reference, analysed determinands
- `capabilityClass`: a rating of general agricultural capability; key attributes: class code, definition, limiting factors, source system
- `suitabilityAssessment`: a crop-specific rating for a unit or field; key attributes: crop reference, rating, limiting factors, management assumptions, assessment date
- `degradationRecord`: an observed condition loss; key attributes: process kind, extent affected, severity, observation date, evidence reference
- `agriculturalField`: a managed land unit; key attributes: geometry, holder reference, current use, irrigation status, management history reference

## Relationships

- `soilProfile` -> composedOf -> `soilHorizon` (1:n): a profile is the ordered set of its horizons
- `soilProfile` -> typifies -> `soilUnit` (n:1): representative profiles anchor the description of a map unit
- `soilSample` -> takenFrom -> `soilHorizon` (n:1): every laboratory result traces to a depth interval in a profile
- `soilUnit` -> assignedCapability -> `capabilityClass` (n:1): general capability is a property of the mapped unit
- `suitabilityAssessment` -> rates -> `soilUnit` (n:m): suitability is stated per unit and per crop with its assumptions
- `agriculturalField` -> overlays -> `soilUnit` (n:m): a managed field usually spans several soil units
- `agriculturalField` -> partOf -> `parcel` in P2 (n:1): fields sit within registered land units without redefining them
- `degradationRecord` -> affects -> `soilUnit` (n:m): condition loss is recorded against units and, where known, fields

## Events

- `soilProfileDescribed`: a pit or auger site was described and classified
- `soilSampleAnalyzed`: laboratory results were returned and attached to a horizon
- `soilMapUnitRevised`: unit boundaries or component proportions changed after new evidence
- `capabilityClassReassessed`: the general capability rating for a unit changed
- `erosionEventRecorded`: a measurable loss of topsoil was observed after rainfall, wind or cultivation
- `salinizationDetected`: salinity crossed the threshold defined for a unit or field
- `contaminationConfirmed`: a contaminant exceeded its threshold at a sampled location
- `remediationCompleted`: works to restore soil condition finished and post-works results were recorded

## Contracts

- `laboratoryAnalysisContract`: terms for submitting samples and returning results, including method declaration, detection limits and reanalysis
- `farmSoilDataSharingContract`: terms under which field-level results held by a holder are shared with the steward, including the grain at which they may be republished
- `contaminationDisclosureContract`: terms for disclosing a confirmed contamination finding to an entitled party such as a prospective occupier or a land registrar

## Projections

- `publicSoilMap`: soil units, dominant classification and capability class; omits sample-level results and any holder-linked field data
- `holderFieldReport`: the complete profile, laboratory and condition record for the fields of one holder; omits neighbouring holdings
- `landCapabilityStatistics`: area by capability class, suitability and degradation status; omits unit geometry and holder identity

## Composition

- REFERENCE `world.landParcelAndCadastre` (P2): fields and units are located within registered land units and their holders resolve there
- REFERENCE `world.terrainAndLandform` (P1): slope, aspect and relief are limiting factors in capability and erosion assessment
- REFERENCE `world.subsurfaceAndMineralResource` (P5): parent material links the weathering profile to bedrock
- REFERENCE `world.waterBodyAndHydrology` (P3): infiltration, runoff and nutrient loading connect soil state to water response
- REFERENCE `world.ecosystemAndBiome` (P8): soil condition is an input to ecosystem condition and process accounts
- REFERENCE `world.agricultureAndHusbandry` (K9): cropping, grazing and amendment operations are described there and reference fields here
- REFERENCE `world.materialAndSubstance` (M1): contaminant identity, hazard class and thresholds resolve there
- REFERENCE `world.emissionAndEnvironmentalFlux` (F6): soil carbon change and nutrient losses are accounted as fluxes there
- REFERENCE `world.officialStatisticsAndIndicators` (N10) and `world.privacyAggregationAndCohortFloor` (S5): published land statistics respect the cohort grain defined there
- imports: fao-soil-classification (EXTEND): the classification backbone for units and profiles
- imports: iuss-world-reference-base (ALIGN): reference groups and qualifiers for cross-register comparability
- imports: iso-28258-soil-data-exchange (COMPOSE): the site, profile, horizon and result exchange structure

## Stewardship

An ecology and agronomy commons steward keeps the soil register: it maintains the map, accredits laboratories, publishes capability and condition and curates the long profile archive. Field-level data contributed by a holder remains that holder's under S1, republication happens only at the grain agreed in an S2 access contract and constrained by S5 cohort rules, and reads of holder-linked records are logged in S4.
