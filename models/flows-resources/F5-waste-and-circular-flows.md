# F5 Waste & Circular Flows

This meta-model describes what happens to materials after their useful life: the classification of waste streams, their collection and consignment movement, treatment and hazard control, recovery of materials back into productive use, and final disposal with long-term aftercare. It is its own model because waste carries classification and liability semantics that outlive the ownership of the original good: a generator's responsibility persists along the chain, and circular loops turn an end state back into a resource input.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f5"
  csn: world.wasteFlow
  version: 0.2.0
  displayName: Waste & Circular Flows
  description: Waste streams from arising through collection, treatment, material recovery and final disposal.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.wasteFlow
bundles:
  - csn: world.wasteFlow.stream
    displayName: Stream
    layers:
      - world.wasteFlow.stream.wasteClassification
      - world.wasteFlow.stream.arisingAndCollection
  - csn: world.wasteFlow.treatment
    displayName: Treatment
    layers:
      - world.wasteFlow.treatment.treatmentOperations
      - world.wasteFlow.treatment.hazardControl
  - csn: world.wasteFlow.circularity
    displayName: Circularity
    layers:
      - world.wasteFlow.circularity.materialRecovery
      - world.wasteFlow.circularity.reuseAndRecycling
  - csn: world.wasteFlow.disposal
    displayName: Disposal
    layers:
      - world.wasteFlow.disposal.finalDisposal
      - world.wasteFlow.disposal.aftercareMonitoring
imports:
  - source: eu-waste-codes
    version: "*"
  - source: basel-convention
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `stream` | What waste is and where it arises | `wasteClassification`: stream types and hazard classification by external code list Â· `arisingAndCollection`: generators, arisings and collection services |
| `treatment` | Processing waste safely | `treatmentOperations`: sorting, shredding, composting, incineration and other operations Â· `hazardControl`: handling constraints and containment for hazardous streams |
| `circularity` | Returning materials to use | `materialRecovery`: outputs recovered from treatment Â· `reuseAndRecycling`: loops that feed recovered materials back into production |
| `disposal` | Ending the flow responsibly | `finalDisposal`: landfill and other terminal operations Â· `aftercareMonitoring`: long-term observation of closed disposal sites |

## Objects

- `wasteStream`: a classified category of waste with common handling rules; key attributes: streamCode, description, hazardClass.
- `hazardProfile`: the hazard characteristics governing a stream; key attributes: hazardProperties, handlingConstraints.
- `wasteConsignment`: an identifiable quantity of waste moving through the chain; key attributes: consignmentId, quantity, generatorRef, streamRef.
- `collectionService`: a service that gathers consignments from generators; key attributes: serviceArea, acceptedStreams, frequency.
- `treatmentOperation`: a processing step applied to consignments; key attributes: operationType, facilityRef, capacity.
- `recoveredMaterial`: a material output returned to productive use; key attributes: materialType, quality Grade, quantity.
- `disposalSite`: a terminal location for non-recovered waste; key attributes: siteType, remainingCapacity, aftercareStatus, parcelRef.
- `transferNote`: the record documenting a custody handover of a consignment; key attributes: noteId, fromHolderRef, toHolderRef, transferredAt.

## Relationships

- `wasteStream` -> classifiedBy -> `hazardProfile` (n:1): the hazard characteristics of a stream.
- `wasteConsignment` -> belongsTo -> `wasteStream` (n:1): the classification of a consignment.
- `collectionService` -> collects -> `wasteConsignment` (1:n): consignments gathered by a service.
- `treatmentOperation` -> processes -> `wasteConsignment` (n:m): the operations applied along a consignment's path.
- `treatmentOperation` -> yields -> `recoveredMaterial` (1:n): recovery outputs of an operation.
- `wasteConsignment` -> disposedAt -> `disposalSite` (n:1): the terminal location of a non-recovered consignment.
- `transferNote` -> documents -> `wasteConsignment` (n:1): the custody handovers of a consignment.

## Events

- `wasteCollected`: a consignment was gathered from its generator by a collection service.
- `consignmentTransferred`: custody of a consignment passed to another holder under a transfer note.
- `treatmentCompleted`: a treatment operation finished processing a consignment.
- `materialRecovered`: a recovered material output was produced and made available for reuse.
- `consignmentDisposed`: a consignment was deposited at a disposal site.
- `incidentRecorded`: a spill, misclassification or containment failure was recorded.
- `aftercareInspected`: a closed disposal site was inspected and its condition recorded.

## Contracts

- `transferNoteVerification`: an authorized party verifies the unbroken custody record of a consignment.
- `recoveryRateReporting`: consumers receive recovery and recycling rates per stream and period without generator identity.
- `disposalRecordAccess`: site stewards and oversight archetypes read disposal and aftercare records for a site.

## Projections

- `generatorReturnsView`: a generator's own arisings, consignments and their final outcomes; omits other generators.
- `processorOperationsView`: a processor's own operations, yields and capacity; omits upstream commercial data.
- `circularityStatisticsView`: stream-level recovery, recycling and disposal aggregates; omits all consignment identity.

## Composition

- EXTEND `world.goodsMovement` (F3): consignment movement and transfer notes specialize the F3 custody chain with generator liability and stream classification.
- REFERENCE `world.emission` (F6): releases from treatment and disposal operations are quantified in the emission model.
- REFERENCE `world.waterFoodSupply` (F4): food chain residues arise here, and recovered materials may re-enter production chains.
- REFERENCE `world.landParcel` (P2): disposal sites and their aftercare obligations attach to identified parcels.
- imports: EU waste codes (REFERENCE): the externally governed waste classification scheme, carried by code and version.
- imports: Basel Convention (ALIGN): notification and consent semantics for transboundary consignment movements.

## Stewardship

The generator stewards arising and stream records, and each processor stewards the treatment, recovery and disposal records it produces, so stewardship follows the custody chain while generator responsibility remains traceable end to end. Access is granted by the respective steward through the catalogue's S1/S2 ownership and access models, with custody verification audited via S4.
