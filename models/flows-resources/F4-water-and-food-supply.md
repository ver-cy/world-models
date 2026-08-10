# F4 Water & Food Supply

This meta-model describes the supply chains that deliver safe water and food: the sources they draw on (aquifers, farms, fisheries), the treatment and processing that make output safe, the quality testing tied to identifiable batches, and the networks, reserves and endpoints that distribute supply to people. It is its own model because water and food flows carry batch-level safety assurance and continuity-of-supply semantics that go beyond generic logistics: a batch that fails a test must be traceable both backwards to its source and forwards to its endpoints.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f4"
  csn: world.waterFoodSupply
  version: 0.2.0
  displayName: Water & Food Supply
  description: Sources, treatment, quality assurance and distribution of water and food supply chains.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.waterFoodSupply
bundles:
  - csn: world.waterFoodSupply.source
    displayName: Source
    layers:
      - world.waterFoodSupply.source.waterSources
      - world.waterFoodSupply.source.agriculturalProduction
  - csn: world.waterFoodSupply.processing
    displayName: Processing
    layers:
      - world.waterFoodSupply.processing.treatmentProcesses
      - world.waterFoodSupply.processing.qualityTesting
  - csn: world.waterFoodSupply.distribution
    displayName: Distribution
    layers:
      - world.waterFoodSupply.distribution.networksAndLogistics
      - world.waterFoodSupply.distribution.storageAndReserves
      - world.waterFoodSupply.distribution.retailEndpoints
imports:
  - source: fao
    version: "*"
  - source: gs1-epcis
    version: "*"
  - source: codex-alimentarius
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `source` | Where supply originates | `waterSources`: aquifers, reservoirs, intakes and their yield · `agriculturalProduction`: farms, fisheries and harvest output entering the chain |
| `processing` | Making supply safe | `treatmentProcesses`: water treatment and food processing stages applied to batches · `qualityTesting`: tests, sampling plans and results tied to batches |
| `distribution` | Getting supply to people | `networksAndLogistics`: pipes, cold chains and delivery paths · `storageAndReserves`: buffers that secure continuity of supply · `retailEndpoints`: the points where supply reaches consumers |

## Objects

- `supplyChain`: a named end-to-end chain from sources to endpoints for a product or service area; key attributes: chainType (water, food category), serviceArea, operatorRef.
- `sourceSite`: an origin of raw supply (aquifer, reservoir, farm, fishery); key attributes: siteType, yieldCapacity, parcelRef.
- `batchLot`: an identifiable quantity of water or food moving through the chain; key attributes: lotId, productCode, quantity, productionDate.
- `treatmentFacility`: a plant applying treatment or processing stages; key attributes: facilityType, throughputCapacity, certifications.
- `qualityTest`: a sampled assessment of a batch or network point; key attributes: parameter, method, result, testedAt.
- `distributionNetwork`: the physical or logistical network moving supply; key attributes: networkType, coverageArea, capacity.
- `storageReserve`: a buffer stock securing continuity; key attributes: reserveType, currentLevel, targetLevel.
- `retailEndpoint`: a point where supply reaches consumers (tap zone, store, delivery point); key attributes: endpointType, location, servedPopulation.

## Relationships

- `supplyChain` -> originatesAt -> `sourceSite` (n:m): the sources feeding a chain.
- `batchLot` -> drawnFrom -> `sourceSite` (n:1): backward traceability of a lot.
- `batchLot` -> processedBy -> `treatmentFacility` (n:m): the treatment stages a lot passed through.
- `qualityTest` -> assesses -> `batchLot` (n:1): the lot a result applies to.
- `distributionNetwork` -> serves -> `retailEndpoint` (1:n): forward traceability to endpoints.
- `storageReserve` -> buffers -> `supplyChain` (n:1): the chain a reserve secures.

## Events

- `sourceExtracted`: raw water was abstracted or produce was harvested at a source site.
- `batchTreated`: a lot completed a treatment or processing stage.
- `qualityTestRecorded`: a test result was recorded against a lot or network point.
- `contaminationDetected`: a test or observation found supply unsafe, triggering trace and recall.
- `reserveDrawnDown`: a storage reserve fell below its target level.
- `deliveryCompleted`: a lot or continuous supply reached a retail endpoint.
- `shortageDeclared`: continuity of supply for an area was declared at risk.

## Contracts

- `traceabilityAccess`: an authorized party traces a lot backwards to sources and forwards to endpoints.
- `qualityResultsFeed`: oversight and endpoint stewards receive test results for chains serving them.
- `reserveLevelReporting`: continuity planners receive reserve levels without commercial detail.

## Projections

- `publicSafetyView`: per-area quality summaries and advisories; omits facility internals and commercial data.
- `operatorNetworkView`: an operator's own sources, facilities, network state and reserves; omits other operators.
- `provenanceTraceView`: the full source-to-endpoint path of one lot for recall handling; omits unrelated lots.

## Composition

- EXTEND `world.goodsMovement` (F3): movement of food and bottled water consignments specializes the F3 custody chain with lot identity and cold chain constraints.
- REFERENCE `world.energy` (F1): pumping, treatment and cold storage are consumption points in the energy model.
- REFERENCE `world.wasteFlow` (F5): processing residues and expired stock enter waste streams recorded there.
- REFERENCE `world.landParcel` (P2): source sites and facilities are sited on identified parcels.
- imports: FAO (ALIGN): agricultural production and commodity classification equivalences.
- imports: GS1 EPCIS (ALIGN): traceability event vocabulary for lot movements.
- imports: Codex Alimentarius (ALIGN): food quality and safety parameter reference standards.

## Stewardship

Operators (utilities, processors, distributors) steward the records of their own segment of each chain, while public health and agriculture oversight archetypes hold verification access to quality and traceability data. All access is granted by the respective steward through the catalogue's S1/S2 ownership and access models, with trace audits recorded via S4.
