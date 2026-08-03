# P7 Fauna & Wildlife

This meta-model describes animal life: taxa and their names, populations and their demography, marked individuals and the tracks they leave, the habitats and ranges they occupy, and the protection that attaches to them. It is its own model because animals move: identity has to survive movement across boundaries, populations are estimated rather than counted, and individual tracking data is both scientifically central and highly sensitive. Plants are modelled in P6 with a deliberately aligned taxonomic pattern; kept animals as an activity belong to K9.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p7"
  csn: world.faunaAndWildlife
  version: 0.2.0
  displayName: "Fauna & Wildlife"
  description: "Animal taxa, populations, marked individuals and their movements, ranges, habitats and protection status."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.faunaAndWildlife
bundles:
  - csn: world.faunaAndWildlife.taxonomy
    displayName: "Taxonomy and names"
    layers:
      - world.faunaAndWildlife.taxonomy.taxonConcept
      - world.faunaAndWildlife.taxonomy.nameAndSynonymy
  - csn: world.faunaAndWildlife.populationAndMovement
    displayName: "Population and movement"
    layers:
      - world.faunaAndWildlife.populationAndMovement.abundanceAndDemography
      - world.faunaAndWildlife.populationAndMovement.individualAndMarking
      - world.faunaAndWildlife.populationAndMovement.migrationAndTracking
  - csn: world.faunaAndWildlife.habitatAndRange
    displayName: "Habitat and range"
    layers:
      - world.faunaAndWildlife.habitatAndRange.rangeDistribution
      - world.faunaAndWildlife.habitatAndRange.habitatRequirement
  - csn: world.faunaAndWildlife.protection
    displayName: "Protection and take control"
    layers:
      - world.faunaAndWildlife.protection.conservationAssessment
      - world.faunaAndWildlife.protection.listingAndTradeControl
imports:
  - source: darwin-core
    version: "*"
  - source: iucn-red-list-categories
    version: "*"
  - source: cites-appendices
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `taxonomy` | Which animal is meant, under which name | `taxonConcept`: taxon concepts, rank and circumscription Â· `nameAndSynonymy`: scientific and vernacular names with synonymy and authorship |
| `populationAndMovement` | How many there are and where they go | `abundanceAndDemography`: population units, estimates, age and sex structure, survival and recruitment Â· `individualAndMarking`: identified individuals, rings, tags, collars and their attachment history Â· `migrationAndTracking`: telemetry fixes, routes, stopovers and seasonal movement patterns |
| `habitatAndRange` | Where the taxon can and does live | `rangeDistribution`: distribution polygons, seasonal ranges and range change Â· `habitatRequirement`: habitat features a taxon depends on, including breeding and refuge sites |
| `protection` | What status and controls apply | `conservationAssessment`: assessed status with criteria and scope Â· `listingAndTradeControl`: protective listings and trade control appendices attaching to a taxon |

## Objects

- `taxon`: an animal taxon concept; key attributes: taxon identifier, rank, parent taxon, accepted name reference, circumscription reference
- `animalPopulation`: a delimited population unit; key attributes: taxon reference, range reference, estimated size, confidence interval, trend, estimation method
- `taggedIndividual`: an identified animal carrying a mark; key attributes: individual identifier, mark type and code, attachment date, age class, sex, fate status
- `trackingFix`: a reported position for a marked individual; key attributes: timestamp, coordinates, positional error, sensor type, activity flags
- `habitatPatch`: an area providing required habitat; key attributes: geometry, habitat class, function (breeding, feeding, refuge), quality assessment
- `rangePolygon`: a mapped distribution for a taxon; key attributes: taxon reference, season, presence category (resident, breeding, passage), delineation method
- `wildlifeSurvey`: a counting or detection effort; key attributes: method, effort, area covered, date range, detection probability, observer references
- `conservationAssessment`: an assessed status; key attributes: taxon reference, category, criteria, scope, assessment date, assessing body reference

## Relationships

- `animalPopulation` -> ofTaxon -> `taxon` (n:1): populations are always populations of a named taxon concept
- `taggedIndividual` -> memberOf -> `animalPopulation` (n:1): marked animals are attributed to the population they were caught in
- `trackingFix` -> reports -> `taggedIndividual` (n:1): every fix carries the individual and device that produced it
- `wildlifeSurvey` -> estimates -> `animalPopulation` (n:1): an estimate is a dated result of a method, not a property of the animals
- `animalPopulation` -> inhabits -> `habitatPatch` (n:m): populations use several patches with different functions
- `rangePolygon` -> delimits -> `taxon` (n:1): distribution is mapped per taxon and season
- `conservationAssessment` -> assesses -> `taxon` (n:1): status claims attach to taxa within a stated geographic scope
- `habitatPatch` -> partOf -> `ecosystemAsset` in P8 (n:1): habitat patches are components of larger ecosystem units

## Events

- `sightingRecorded`: an animal was observed and the record entered the occurrence stream
- `individualTaggedAndReleased`: an animal was captured, marked and released, starting an individual history
- `trackingFixReceived`: a device reported a position, adding to a movement track
- `populationSurveyCompleted`: a survey concluded and produced an abundance estimate with its uncertainty
- `mortalityEventRecorded`: a death or mass mortality was observed and attributed where possible
- `rangeShiftDetected`: the mapped distribution moved beyond the previous seasonal envelope
- `protectedListingChanged`: a listing or trade control status for a taxon was added, upgraded or removed
- `humanWildlifeConflictReported`: an interaction causing damage or risk was reported and logged

## Contracts

- `telemetryFeedContract`: terms for delivery of tracking data, including latency, precision limits and permitted secondary use
- `sensitiveLocationRedactionContract`: terms under which nest, den and roost coordinates are generalized, and who may hold the precise locations
- `citizenObservationContract`: terms for volunteer submitted sightings, covering attribution, licence and verification workflow
- `sharedPopulationExchangeContract`: terms for exchanging counts and tracks of a migratory population with a neighbouring register

## Projections

- `publicRangeMap`: seasonal distribution polygons and status by taxon; omits breeding site coordinates and individual tracks
- `populationTrendSeries`: estimates and trends over time with method notes; omits raw detections and observer identity
- `taggingCohortView`: full individual and fix history for the operator that marked the animals; omits other operators' cohorts

## Composition

- ALIGN `world.floraAndVegetation` (P6): the taxon, name and occurrence pattern is aligned so botanical and zoological records join cleanly
- REFERENCE `world.ecosystemAndBiome` (P8): habitat patches and populations are components of ecosystem assets
- REFERENCE `world.waterBodyAndHydrology` (P3): aquatic populations are attributed to the bodies and reaches described there
- REFERENCE `world.agricultureAndHusbandry` (K9): kept and farmed animals are described there and reference taxa here
- REFERENCE `world.publicHealthAndEpidemiology` (B14): zoonotic surveillance uses populations and mortality events recorded here
- REFERENCE `world.naturalPhenomenonAndHazard` (P9): mass mortality and die-off occurrences link to hazard events there
- REFERENCE `world.physicalInfrastructureNetwork` (U3): barriers, crossings and collision hotspots are structures there that shape movement here
- REFERENCE `world.disclosureScopeAndProjectionPolicy` (S3): the generalization rules for sensitive locations are defined there
- imports: darwin-core (EXTEND): the occurrence and taxon record backbone this model specializes
- imports: iucn-red-list-categories (ALIGN): categories and criteria for conservation assessment
- imports: cites-appendices (REFERENCE): trade control listings referenced rather than copied

## Stewardship

An ecology commons steward keeps the wildlife register: it curates taxa and ranges, accredits survey and tagging programmes and publishes population estimates and status. Tagging operators and volunteer observers keep attribution to the records they contribute, precise locations of sensitive sites and live tracks are released only under S2 access contracts shaped by S3, and every such read is logged in S4.
