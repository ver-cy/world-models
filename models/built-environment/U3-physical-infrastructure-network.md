# U3 Physical Infrastructure Network

This meta-model describes roads, rail, pipes, grids and cables as physical networks: the topology of segments and nodes, their rated capacity and utilization, and their asset condition and maintenance. It is its own model because the physical asset base persists across operators and service arrangements, and its topology is the shared substrate that service points (U5), settlements (U4) and incidents (X3) all reference.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:u3"
  csn: world.physicalInfrastructureNetwork
  version: 0.2.0
  displayName: "Physical Infrastructure Network"
  description: "Roads, rail, pipes and grids as physical networks: topology, capacity and asset condition."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.physicalInfrastructureNetwork
bundles:
  - csn: world.physicalInfrastructureNetwork.topology
    displayName: "Topology"
    layers:
      - world.physicalInfrastructureNetwork.topology.segments
      - world.physicalInfrastructureNetwork.topology.nodes
      - world.physicalInfrastructureNetwork.topology.connectivity
      - world.physicalInfrastructureNetwork.topology.linearReferencing
  - csn: world.physicalInfrastructureNetwork.capacity
    displayName: "Capacity"
    layers:
      - world.physicalInfrastructureNetwork.capacity.ratedCapacity
      - world.physicalInfrastructureNetwork.capacity.utilization
  - csn: world.physicalInfrastructureNetwork.assetCondition
    displayName: "Asset condition"
    layers:
      - world.physicalInfrastructureNetwork.assetCondition.condition
      - world.physicalInfrastructureNetwork.assetCondition.maintenance
imports:
  - source: inspire
    version: "*"
  - source: iec-cim
    version: "*"
  - source: iso-19148
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `topology` | The physical shape and connectivity of the network | `segments`: linear stretches between nodes Â· `nodes`: junctions, switches, substations, terminals Â· `connectivity`: how segments and networks join Â· `linearReferencing`: positions along segments from a datum |
| `capacity` | What the network can carry and how loaded it is | `ratedCapacity`: engineering statements of carrying capability Â· `utilization`: observed load against rating |
| `assetCondition` | The physical state and upkeep of assets | `condition`: dated condition surveys and grades Â· `maintenance`: planned regimes and completed upkeep |

## Objects

- `network`: a named physical network of one mode (road, rail, water, power, district heat, sewage, telecom); key attributes: mode, operatorRef, extent
- `segment`: a linear stretch of network between two nodes; key attributes: length, mode, ratedCapacity, commissioningYear
- `node`: a junction, switch, substation, pumping station or terminal; key attributes: nodeClass, position, capacity
- `linearReference`: a position along a segment expressed as an offset from a datum; key attributes: segmentRef, offset, datum
- `capacityRating`: a dated engineering statement of what a segment or node can carry; key attributes: ratedValue, unit, validFrom, basis
- `conditionSurvey`: a dated assessment of the physical state of an asset; key attributes: surveyedAt, method, grade, defectsFound
- `maintenanceScheme`: a planned regime of upkeep for a set of assets; key attributes: cycle, scope, responsibleRef

## Relationships

- `network` -> comprises -> `segment` (1:n): a network is the sum of its segments
- `segment` -> connects -> `node` (n:m): each segment ends in nodes; a node joins many segments
- `segment` -> carriedBy -> `structure` (n:m): bridges, tunnels and pylons modelled in U1 carry segments
- `network` -> interconnectsWith -> `network` (n:m): interchange and transfer points between modes or operators
- `capacityRating` -> rates -> `segment` (n:1): ratings accumulate as engineering knowledge improves
- `conditionSurvey` -> assesses -> `segment` (n:1): each survey grades one segment or node
- `segment` -> tappedBy -> `servicePoint` (1:n): end users connect through service points modelled in U5

## Events

- `segmentCommissioned`: a new segment entered service
- `segmentDecommissioned`: a segment was permanently withdrawn from service
- `capacityRerated`: a segment or node received a new capacity rating
- `conditionSurveyed`: a condition survey was completed and graded
- `maintenanceCompleted`: planned or corrective upkeep was finished on an asset
- `closureOccurred`: a segment was temporarily closed or out of service

## Contracts

- `openNetworkMapLicense`: public release of simplified topology for mapping and routing
- `interOperatorExchange`: exchange of connectivity and capacity data at interconnection points between operators
- `conditionDataAccess`: operator-granted access to condition surveys for engineers, insurers or works planners

## Projections

- `routingGraphProjection`: topology and capacity as a graph for pathfinding; omits condition and maintenance detail
- `assetRegisterProjection`: assets with age, condition grade and maintenance state; omits utilization
- `publicMapProjection`: simplified geometry and classification for general maps; omits operationally sensitive attributes

## Composition

- REFERENCE `world.buildingStructure` (U1): carrying structures such as bridges and tunnels are modelled there
- REFERENCE `world.utilityServicePoint` (U5): where end users tap the network; supply semantics live in U5
- REFERENCE `world.settlementUrbanForm` (U4): segments traverse settlements and districts modelled there
- REFERENCE `world.landParcelCadastre` (P2): rights of way and easements over parcels are resolved in the cadastre
- REFERENCE `world.incidentEmergency` (X3): incidents affecting network assets are recorded there and mirrored as closure events here
- imports: inspire (ALIGN: transport and utility network themes)
- imports: iec-cim (EXTEND: power grid topology semantics for electrical networks)
- imports: iso-19148 (REFERENCE: linear referencing method for positions along segments)

## Stewardship

The owner archetype is the operator organization: the operator of each network stewards its asset records, and several operators can steward different networks over the same territory. Access to condition and capacity detail is granted by the operator through S2, with disclosures auditable via S4.