# F6 Emission & Environmental Flux

This meta-model describes quantified releases of substances and energy into the environment: the sources that cause them, the pathways they take to air, water and soil, the factors and measurements that quantify them, the abatement measures that reduce them, and the verification that makes the numbers trustworthy. It is its own model because an emission record is a derived claim: it must be reproducible from method plus activity data and independently verifiable, which imposes an evidence discipline that the underlying activity models do not need.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f6"
  csn: world.emission
  version: 0.2.0
  displayName: Emission & Environmental Flux
  description: Emission sources, quantification methods, release pathways, abatement and verification.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.emission
bundles:
  - csn: world.emission.inventory
    displayName: Inventory
    layers:
      - world.emission.inventory.emissionSources
      - world.emission.inventory.emissionFactors
  - csn: world.emission.measurement
    displayName: Measurement
    layers:
      - world.emission.measurement.directMeasurement
      - world.emission.measurement.estimationMethods
  - csn: world.emission.flux
    displayName: Flux
    layers:
      - world.emission.flux.releasePathways
      - world.emission.flux.ambientFlux
  - csn: world.emission.abatement
    displayName: Abatement
    layers:
      - world.emission.abatement.abatementMeasures
      - world.emission.abatement.verification
imports:
  - source: ghg-protocol
    version: "*"
  - source: ipcc-guidelines
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `inventory` | What emits and by how much per unit of activity | `emissionSources`: stationary, mobile and process sources and their ownership Â· `emissionFactors`: per-activity release coefficients and their provenance |
| `measurement` | How quantities are established | `directMeasurement`: continuous and sampled monitoring series Â· `estimationMethods`: calculation methods combining factors with activity data |
| `flux` | Where releases go | `releasePathways`: routes to air, water and soil Â· `ambientFlux`: dispersion, deposition and uptake by sinks |
| `abatement` | Reducing and attesting | `abatementMeasures`: interventions that reduce source output Â· `verification`: independent attestation of quantified records |

## Objects

- `emissionSource`: an activity or asset that releases substances; key attributes: sourceType, ownerRef, siteRef, activityDataRef.
- `quantifiedEmission`: a substance quantity released by a source over a period; key attributes: substance, quantity, unit, period, method.
- `emissionFactor`: a coefficient linking activity to release; key attributes: substance, activityUnit, factorValue, provenance.
- `measurementSeries`: a monitored time series at a source or ambient point; key attributes: parameter, samplingMethod, interval, instrumentRef.
- `releasePathway`: the route a release takes into an environmental medium; key attributes: medium, dischargePoint, dispersionCharacteristics.
- `abatementMeasure`: an intervention reducing releases from a source; key attributes: measureType, expectedReduction, commissionedAt.
- `verificationStatement`: an independent attestation over a set of quantified emissions; key attributes: verifierRef, scope, opinion, issuedAt.

## Relationships

- `quantifiedEmission` -> emittedBy -> `emissionSource` (n:1): the causing source.
- `quantifiedEmission` -> quantifiedUsing -> `emissionFactor` (n:1): the coefficient used when estimated.
- `quantifiedEmission` -> evidencedBy -> `measurementSeries` (n:m): the monitoring data used when measured.
- `quantifiedEmission` -> releasedVia -> `releasePathway` (n:1): the medium and route of a release.
- `abatementMeasure` -> appliesTo -> `emissionSource` (n:m): sources an intervention reduces.
- `verificationStatement` -> attests -> `quantifiedEmission` (1:n): records covered by an attestation.

## Events

- `emissionQuantified`: a release quantity was computed or measured for a source and period.
- `measurementRecorded`: a monitoring sample or interval was appended to a series.
- `exceedanceDetected`: a measured or quantified value crossed a declared threshold.
- `abatementCommissioned`: a reduction measure entered operation at a source.
- `verificationIssued`: an independent verifier attested a set of quantified emissions.
- `factorRevised`: an emission factor was updated, marking dependent records for recomputation.

## Contracts

- `verifiedInventoryAccess`: consumers read quantified emissions that carry a verification statement.
- `monitoringDataFeed`: oversight and research consumers receive measurement series under agreed granularity.
- `aggregateFluxStatistics`: territory and sector aggregates provided without source-level identity.

## Projections

- `publicInventoryView`: verified aggregates by territory, sector and substance; omits source-level and method detail.
- `verifierEvidenceView`: methods, factors, series and activity references for records under verification; omits unrelated sources.
- `sourceOwnerView`: an owner's own sources, quantifications and abatement performance; omits other owners.

## Composition

- REFERENCE `world.energy` (F1): fuel and power flows provide activity data for combustion sources.
- REFERENCE `world.wasteFlow` (F5): treatment and disposal operations are emission sources with their own activity data.
- REFERENCE `world.goodsMovement` (F3): freight transport activity underlies mobile source estimates.
- REFERENCE `world.passengerMobility` (F7): passenger service activity underlies transit emission estimates.
- REFERENCE `world.landParcel` (P2): stationary sources and discharge points are sited on identified parcels.
- imports: GHG Protocol (ALIGN): accounting boundary and scope semantics for organizational inventories.
- imports: IPCC guidelines (ALIGN): estimation method tiers and default factor semantics.

## Stewardship

The emitting owner stewards its source and quantification records, while an independent environmental verifier archetype holds attestation access and a statistics office archetype stewards published aggregates. Access is granted by the respective steward through the catalogue's S1/S2 ownership and access models, with verification trails audited via S4.
