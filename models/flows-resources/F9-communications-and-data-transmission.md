# F9 Communications & Data Transmission

This meta-model describes communications as a service layer of the world: the radio spectrum bands and the grants that allocate them, the addressing and numbering resources that make endpoints reachable, the network services operators provide, the interconnection links that stitch networks together, and the aggregate traffic that flows across them. It is its own model because it manages scarce shared resources (spectrum, addresses, numbers) governed by registries, and its unit of flow is traffic measured in aggregates rather than discrete consignments.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f9"
  csn: world.communications
  version: 0.2.0
  displayName: Communications & Data Transmission
  description: Spectrum grants, addressing and numbering, network services, interconnection and traffic aggregates.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.communications
bundles:
  - csn: world.communications.spectrum
    displayName: Spectrum
    layers:
      - world.communications.spectrum.bandPlan
      - world.communications.spectrum.grantsAndLicences
  - csn: world.communications.addressing
    displayName: Addressing
    layers:
      - world.communications.addressing.numberingPlans
      - world.communications.addressing.ipAddressBlocks
      - world.communications.addressing.routingRegistry
  - csn: world.communications.service
    displayName: Service
    layers:
      - world.communications.service.serviceOfferings
      - world.communications.service.coverageAndCapacity
  - csn: world.communications.traffic
    displayName: Traffic
    layers:
      - world.communications.traffic.interconnection
      - world.communications.traffic.trafficAggregates
imports:
  - source: itu
    version: "*"
  - source: ietf
    version: "*"
  - source: bgp-registries
    version: "*"
  - source: iana
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `spectrum` | The shared radio resource | `bandPlan`: frequency bands and their designated uses Â· `grantsAndLicences`: allocations of bands to operators with conditions and terms |
| `addressing` | Making endpoints reachable | `numberingPlans`: telephone numbering resources and their assignment Â· `ipAddressBlocks`: internet address space allocations Â· `routingRegistry`: autonomous systems and route announcements |
| `service` | What operators provide | `serviceOfferings`: network services and their characteristics Â· `coverageAndCapacity`: where services reach and at what capacity |
| `traffic` | What actually flows | `interconnection`: links and exchange points between networks Â· `trafficAggregates`: measured volumes per link, service and period |

## Objects

- `networkService`: a communications service offered by an operator; key attributes: serviceType, operatorRef, qualityParameters.
- `spectrumBand`: a frequency range with a designated use; key attributes: lowerFrequency, upperFrequency, designatedUse.
- `spectrumGrant`: an allocation of a band to an operator; key attributes: granteeRef, territory, conditions, validity.
- `addressBlock`: a block of internet address space; key attributes: prefix, allocationStatus, registryRef.
- `numberingResource`: a telephone numbering range or code; key attributes: rangeType, digits, assigneeRef.
- `autonomousSystem`: a routing domain identified by number; key attributes: asNumber, operatorRef, routingPolicy.
- `interconnectionLink`: a traffic exchange link between two networks; key attributes: linkType, capacity, exchangePointRef.
- `trafficAggregate`: measured traffic volume for a scope and period; key attributes: scope, period, volume, direction.

## Relationships

- `spectrumGrant` -> allocates -> `spectrumBand` (n:1): the band an allocation covers.
- `networkService` -> operatesUnder -> `spectrumGrant` (n:m): grants a wireless service depends on.
- `addressBlock` -> announcedBy -> `autonomousSystem` (n:m): who originates routes for a block.
- `networkService` -> uses -> `numberingResource` (n:m): numbering ranges serving a service.
- `interconnectionLink` -> connects -> `autonomousSystem` (n:2): the two networks a link joins.
- `trafficAggregate` -> measuredOn -> `interconnectionLink` (n:1): where a volume was observed.

## Events

- `grantIssued`: a spectrum band was allocated to an operator under stated conditions.
- `grantExpired`: a spectrum allocation ended and the band returned to the commons pool.
- `blockAllocated`: an address block or numbering range was assigned to an operator.
- `routeAnnounced`: an autonomous system began originating routes for an address block.
- `routeWithdrawn`: a route announcement ceased.
- `linkEstablished`: a new interconnection between two networks went live.
- `outageOccurred`: a service, link or coverage area became unavailable.
- `trafficSampled`: a traffic aggregate was measured and recorded for a scope and period.

## Contracts

- `publicRegistryLookup`: open resolution of spectrum grants, address blocks, numbering assignments and routing records.
- `coverageDataAccess`: consumers read service coverage and capacity data for planning and comparison.
- `trafficStatisticsFeed`: subscribed consumers receive traffic aggregates without endpoint or subscriber detail.

## Projections

- `publicRegistryView`: who holds which spectrum, addresses and numbers; omits commercial and operational internals.
- `operatorCapacityView`: an operator's own services, links, utilization and outages; omits other operators.
- `nationalTrafficAggregate`: territory-level traffic volumes and trends; omits all per-link and per-subscriber detail.

## Composition

- REFERENCE `world.organization` (O1): operators, registries and exchange point stewards as organizations.
- REFERENCE `world.energy` (F1): network facilities are consumption points in the energy model.
- COMPOSE `world.money` (F2): interconnection settlement amounts embed the money value object.
- imports: ITU (ALIGN): spectrum band designation and numbering governance semantics.
- imports: IETF (ALIGN): internet addressing and routing protocol semantics.
- imports: BGP registries (REFERENCE): externally governed routing registry objects (route, aut-num).
- imports: IANA (REFERENCE): externally governed address and protocol registries.

## Stewardship

Operators steward their service, link and traffic records, and registrar archetypes steward the address, numbering and routing registries. Spectrum bands are a commons: grants are recorded through the catalogue's S1 ownership model as commons allocations, access to all records is granted by the respective steward via S1/S2, and registry changes are audited via S4.
