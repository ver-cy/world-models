# P6 Flora & Vegetation

This meta-model describes plant life in two complementary ways: as taxa with names, occurrences and populations, and as vegetation cover, the mapped stands and canopies that clothe an area. It is its own model because a plant record is simultaneously a taxonomic claim (this is that species), a spatial observation (here, then) and a management fact (this stand, this condition), and those three must stay linked without collapsing into one another. Ecosystems as whole systems are modelled in P8, cultivated crops as an activity in K9; here the subject is the plants and their cover.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p6"
  csn: world.floraAndVegetation
  version: 0.2.0
  displayName: "Flora & Vegetation"
  description: "Plant taxa, occurrence records and populations together with mapped vegetation cover and conservation assessments."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.floraAndVegetation
bundles:
  - csn: world.floraAndVegetation.taxonomy
    displayName: "Taxonomy and names"
    layers:
      - world.floraAndVegetation.taxonomy.taxonConcept
      - world.floraAndVegetation.taxonomy.nameAndSynonymy
  - csn: world.floraAndVegetation.population
    displayName: "Occurrence and population"
    layers:
      - world.floraAndVegetation.population.occurrenceRecord
      - world.floraAndVegetation.population.abundanceAndDemography
      - world.floraAndVegetation.population.phenology
  - csn: world.floraAndVegetation.cover
    displayName: "Vegetation cover"
    layers:
      - world.floraAndVegetation.cover.vegetationType
      - world.floraAndVegetation.cover.standAndCanopyStructure
  - csn: world.floraAndVegetation.protection
    displayName: "Protection status"
    layers:
      - world.floraAndVegetation.protection.conservationAssessment
      - world.floraAndVegetation.protection.protectedListing
imports:
  - source: darwin-core
    version: "*"
  - source: iucn-red-list-categories
    version: "*"
  - source: tdwg-taxon-concept-schema
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `taxonomy` | Which plant is meant, under which name | `taxonConcept`: taxon concepts, rank and circumscription with the reference that fixes them Â· `nameAndSynonymy`: scientific and vernacular names, synonymy and name changes over time |
| `population` | Where plants are, how many, and in what phase | `occurrenceRecord`: individual observations and collections with place, time and evidence Â· `abundanceAndDemography`: population units, counts, cover estimates and size structure Â· `phenology`: timing of leafing, flowering, fruiting and senescence |
| `cover` | What the vegetation looks like as continuous cover | `vegetationType`: the classification of vegetation communities and their diagnostic species Â· `standAndCanopyStructure`: mapped stands with cover fraction, height class, layering and biomass |
| `protection` | What status a taxon or stand carries | `conservationAssessment`: assessed status, criteria applied and assessment date Â· `protectedListing`: listings that attach protection or trade control to a taxon |

## Objects

- `taxon`: a plant taxon concept; key attributes: taxon identifier, rank, parent taxon, circumscription reference, accepted name reference
- `taxonName`: a name applied to a taxon; key attributes: name string, nomenclatural status, authorship, publication reference, synonym relation
- `occurrenceRecord`: an observation or collection of a taxon at a place and time; key attributes: coordinates, coordinate uncertainty, date, recorder reference, basis of record, evidence reference
- `population`: a delimited set of individuals treated as a unit; key attributes: taxon reference, extent geometry, count or cover estimate, census method, trend
- `vegetationStand`: a mapped patch of vegetation; key attributes: geometry, vegetation type reference, cover fraction, canopy height class, layering, condition note
- `vegetationType`: a community class; key attributes: type identifier, definition, diagnostic taxa, parent type, source classification
- `phenologyObservation`: a recorded phenological stage; key attributes: population or stand reference, stage, date, observation method
- `conservationAssessment`: an assessed status for a taxon; key attributes: taxon reference, category, criteria, assessment date, assessing body reference, scope

## Relationships

- `taxonName` -> namesConcept -> `taxon` (n:1): several names, current and historical, can point at one concept
- `occurrenceRecord` -> identifiedAs -> `taxon` (n:1): each record carries the determination it was given and by whom
- `population` -> comprises -> `occurrenceRecord` (1:n): population units aggregate the records that evidence them
- `vegetationStand` -> classifiedAs -> `vegetationType` (n:1): each mapped patch carries one community class at a time
- `vegetationType` -> characterizedBy -> `taxon` (n:m): diagnostic species define what a community class means
- `phenologyObservation` -> observedOn -> `population` (n:1): timing observations attach to a population or stand
- `conservationAssessment` -> assesses -> `taxon` (n:1): status is a dated claim about a taxon within a stated scope
- `vegetationStand` -> occursWithin -> `ecosystemAsset` in P8 (n:1): cover patches sit inside the ecosystem units described there

## Events

- `occurrenceObserved`: a taxon was recorded at a place and time by an identified observer
- `voucherSpecimenDeposited`: physical evidence for a record was lodged in a collection
- `populationCensusCompleted`: a counting or cover survey finished and produced an abundance estimate
- `vegetationMapRevised`: stand boundaries or type attributions were updated after new imagery or fieldwork
- `standDisturbanceRecorded`: a stand was burned, cleared, felled, grazed down or otherwise disturbed
- `floweringOnsetRecorded`: a phenological stage was reached earlier or later than the reference timing
- `conservationStatusReassessed`: an assessment cycle changed the recorded status of a taxon
- `taxonNameSynonymized`: a name was moved into synonymy, requiring downstream records to be re-pointed

## Contracts

- `occurrenceDataPublicationContract`: terms for publishing occurrence archives, including licence, attribution and required data quality flags
- `sensitiveLocalityRedactionContract`: terms under which coordinates of threatened or collectable taxa are generalized before release, and who may see the precise locality
- `fieldSurveyAccessContract`: terms for entering land to survey plots, agreed with the holder of the land unit
- `collectionLoanAgreement`: terms for loan and destructive sampling of vouchered material

## Projections

- `publicChecklist`: accepted taxa, names and status for an area; omits record-level localities and observer identity
- `generalizedOccurrenceMap`: occurrences snapped to a coarse grid; omits precise coordinates for redacted taxa and any private landholder linkage
- `vegetationCoverStatistics`: area and cover fraction by vegetation type; omits stand geometry and observer detail

## Composition

- REFERENCE `world.ecosystemAndBiome` (P8): stands and populations are components of the ecosystem assets assessed there
- ALIGN `world.faunaAndWildlife` (P7): the taxon concept, name and occurrence pattern is aligned across both models so records join cleanly
- REFERENCE `world.soilAndAgriculturalLand` (P10) and `world.waterBodyAndHydrology` (P3): substrate and water availability condition the cover described here
- REFERENCE `world.terrainAndLandform` (P1): elevation and aspect explain zonation of vegetation types
- REFERENCE `world.agricultureAndHusbandry` (K9): cultivated crops and managed plantations are operations there and reference taxa here
- REFERENCE `world.naturalPhenomenonAndHazard` (P9): fire, drought and storm occurrences are recorded there and explain disturbance here
- REFERENCE `world.disclosureScopeAndProjectionPolicy` (S3): the redaction shape for sensitive localities is defined there
- imports: darwin-core (EXTEND): the occurrence, taxon and event record backbone this model specializes
- imports: iucn-red-list-categories (ALIGN): categories and criteria used by conservation assessments
- imports: tdwg-taxon-concept-schema (REFERENCE): taxon concept identifiers rather than a local copy of the taxonomy

## Stewardship

An ecology commons steward keeps the flora register: it curates taxon concepts, accepts occurrence records from surveys and volunteers, maintains the vegetation map and publishes assessments. Observers and collections retain attribution to their records, disclosure of precise localities is granted through S2 access contracts under the redaction policy in S3, and reads of unredacted localities are logged in S4.
