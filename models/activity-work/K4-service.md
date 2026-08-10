# K4 Service

This meta-model describes defined offerings and their delivery: what a provider offers, on what terms and at what promised quality, and what actually happened when the service was requested and delivered. It is its own model because an offering is a standing promise, distinct from the individual acts that fulfil it, and the promise-versus-performance gap is a first-class fact about the world.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k4"
  csn: world.service
  version: 0.2.0
  displayName: "Service"
  description: "Defined service offerings, their terms and their delivery."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.service
bundles:
  - csn: world.service.offering
    displayName: "Offering"
    layers:
      - world.service.offering.serviceDefinition
      - world.service.offering.offerTerms
      - world.service.offering.qualityCommitment
  - csn: world.service.delivery
    displayName: "Delivery"
    layers:
      - world.service.delivery.serviceRequest
      - world.service.delivery.deliveryEpisode
      - world.service.delivery.qualityObservation
imports:
  - source: cpsv-ap
    version: "*"
  - source: schema-org
    version: "*"
  - source: itil
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `offering` | The standing promise | `serviceDefinition`: what the service does and for whom · `offerTerms`: price, eligibility, channels and conditions · `qualityCommitment`: promised service levels |
| `delivery` | The performed reality | `serviceRequest`: a concrete demand for the offering · `deliveryEpisode`: the fulfilment of a request · `qualityObservation`: measured performance against commitments |

## Objects

- `service`: a defined offering; key attributes: name, purpose, target audience, classification, provider reference
- `offer`: the service under concrete terms; key attributes: price or fee basis, validity period, channel, capacity limits
- `eligibilityRule`: who may request the offer; key attributes: criteria, evidence required, exceptions
- `serviceLevel`: a promised quality parameter; key attributes: metric, target, measurement window, remedy
- `channel`: a way the service is reached; key attributes: kind (in person, online, phone), location or endpoint, hours
- `serviceRequest`: one demand instance; key attributes: requester reference, offer reference, submitted time, status
- `deliveryEpisode`: the fulfilment of a request; key attributes: performer, start and end, acts involved, result
- `qualityMeasurement`: an observed quality datum; key attributes: metric, value, episode reference, method

## Relationships

- `offer` -> offers -> `service` (many-to-one): the terms under which the service is available
- `service` -> providedBy -> `organization` (many-to-one): the provider standing behind the offering
- `service` -> reachableThrough -> `channel` (many-to-many): where and how it can be requested
- `serviceRequest` -> requests -> `offer` (many-to-one): the concrete offer being taken up
- `deliveryEpisode` -> fulfils -> `serviceRequest` (one-to-one): the performance answering the demand
- `deliveryEpisode` -> composedOf -> `act` (one-to-many): the atomic acts that made up the delivery
- `qualityMeasurement` -> evaluatesAgainst -> `serviceLevel` (many-to-one): performance compared with the promise
- `service` -> requiresCapability -> `capability` (many-to-many): abilities the provider must hold to deliver

## Events

- `serviceListed`: a service was defined and entered into a catalogue
- `offerPublished`: concrete terms for a service were made available
- `requestReceived`: a requester asked for the offering
- `deliveryCompleted`: a request was fulfilled and the episode closed
- `serviceLevelBreached`: measured performance fell outside a commitment
- `offerWithdrawn`: an offer was closed to new requests

## Contracts

- `catalogueAccess`: a consumer browses service definitions, offers and channels
- `serviceAgreement`: a requester and provider bind an offer's terms and service levels for a period
- `qualityReporting`: measured performance is disclosed to the requester or an oversight body per agreed cadence

## Projections

- `publicCatalogue`: services, offers, eligibility and channels for prospective requesters; omits capacity and internal performance
- `providerDashboard`: requests, episodes and quality against commitments; omits requester personal detail beyond references
- `eligibilityChecker`: rules shaped for automated screening; omits everything but criteria

## Composition

- REFERENCE `world.organization` (O1) and `world.person` (H1): providers and requesters
- REFERENCE `world.actAction` (K2): delivery episodes decompose into recorded acts
- REFERENCE `world.functionAndCapability` (K1): capability requirements of the offering
- REFERENCE `world.processAndWorkflow` (K3): the delivery workflow behind repeatable services
- imports: cpsv-ap (ALIGN): public service vocabulary aligned with the service definition layer
- imports: schema-org (ALIGN): schema:Service and schema:Offer semantics for catalogue publication
- imports: itil (REFERENCE): service management practice definitions for levels and episodes

## Stewardship

The service provider owns the offering and delivery records; requesters own their own request data. Access follows owner grants under the catalogue's ownership and access models (S1/S2), with audit via S4.
