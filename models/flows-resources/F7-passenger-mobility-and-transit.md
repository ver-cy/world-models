# F7 Passenger Mobility & Transit

This meta-model describes how people move through shared transport: networks of stops and routes, published timetables, the vehicle journeys that actually run, the trips passengers take across them, and the fare products and zones that price access. It is its own model because passenger service semantics (headways, punctuality, accessibility, fares, privacy of individual movement) are distinct from goods logistics, even where the two share corridors and terminals.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f7"
  csn: world.passengerMobility
  version: 0.2.0
  displayName: Passenger Mobility & Transit
  description: Transit networks, schedules, vehicle journeys, passenger trips, fares and ridership.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.passengerMobility
bundles:
  - csn: world.passengerMobility.network
    displayName: Network
    layers:
      - world.passengerMobility.network.stopsAndStations
      - world.passengerMobility.network.routesAndLines
  - csn: world.passengerMobility.service
    displayName: Service
    layers:
      - world.passengerMobility.service.timetables
      - world.passengerMobility.service.realtimeOperations
  - csn: world.passengerMobility.journey
    displayName: Journey
    layers:
      - world.passengerMobility.journey.tripsAndLegs
      - world.passengerMobility.journey.ridershipAggregates
  - csn: world.passengerMobility.fare
    displayName: Fare
    layers:
      - world.passengerMobility.fare.fareProducts
      - world.passengerMobility.fare.tariffZonesAndRules
imports:
  - source: gtfs
    version: "*"
  - source: transmodel
    version: "*"
  - source: netex
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `network` | The fixed structure of transit | `stopsAndStations`: stop places, platforms and interchange facilities Â· `routesAndLines`: ordered sequences of stops served by lines |
| `service` | What is planned and what runs | `timetables`: published scheduled services and calendars Â· `realtimeOperations`: actual vehicle journeys, positions, delays and cancellations |
| `journey` | How people use the system | `tripsAndLegs`: passenger trips composed of legs on services Â· `ridershipAggregates`: anonymized usage volumes per route, stop and period |
| `fare` | Pricing access | `fareProducts`: tickets, passes and their validity rules Â· `tariffZonesAndRules`: zonal structures and transfer rules |

## Objects

- `stopPlace`: a station, stop or interchange where passengers board and alight; key attributes: stopId, location, accessibilityFeatures.
- `transitRoute`: a named line serving an ordered sequence of stop places; key attributes: routeId, mode, operatorRef.
- `scheduledService`: a timetabled journey on a route with a calendar; key attributes: serviceId, departureTimes, calendar.
- `vehicleJourney`: an actual run realizing a scheduled service on a date; key attributes: journeyId, vehicleRef, actualTimes, status.
- `trip`: a passenger's journey composed of one or more legs; key attributes: tripId, originStop, destinationStop, legCount.
- `fareProduct`: a purchasable right to travel; key attributes: productType, price, validityPeriod, zoneScope.
- `tariffZone`: a pricing area of the network; key attributes: zoneId, zoneRing, memberStops.
- `ridershipAggregate`: anonymized usage volume for a scope and period; key attributes: scope, period, boardings, occupancyIndex.

## Relationships

- `transitRoute` -> serves -> `stopPlace` (n:m): the ordered stop sequence of a route.
- `scheduledService` -> operatesOn -> `transitRoute` (n:1): the route a timetabled journey follows.
- `vehicleJourney` -> realizes -> `scheduledService` (n:1): the actual run of a planned service.
- `trip` -> usesLegOn -> `vehicleJourney` (n:m): the runs a passenger trip touched.
- `fareProduct` -> validIn -> `tariffZone` (n:m): the zonal scope of a product.
- `ridershipAggregate` -> summarizes -> `transitRoute` (n:1): usage volumes attributed to a route per period.

## Events

- `timetablePublished`: a new schedule version for a route or network became effective.
- `serviceDeparted`: a vehicle journey began at its origin stop.
- `serviceArrived`: a vehicle journey completed at its destination stop.
- `serviceCancelled`: a planned service did not run.
- `disruptionDeclared`: a network or route level disturbance was announced with its scope.
- `fareValidated`: a fare product was used to access a service (recorded without personal linkage by default).
- `tripCompleted`: a passenger trip closed, contributing to ridership aggregates.

## Contracts

- `openTimetableFeed`: public access to network, stop and schedule data.
- `realtimeOperationsFeed`: subscribed consumers receive positions, delays and disruptions.
- `ridershipStatisticsAccess`: planners receive anonymized ridership aggregates, never individual trips.

## Projections

- `journeyPlannerView`: stops, routes, timetables and realtime status merged for trip planning; omits ridership and fare revenue data.
- `operatorPerformanceView`: an operator's own punctuality, cancellations and occupancy; omits other operators.
- `cityRidershipAggregate`: usage volumes per corridor and period for planning; omits all personal and vehicle-level detail.

## Composition

- COMPOSE `world.money` (F2): fare prices embed the money value object.
- REFERENCE `world.person` (M1): a trip may be linked to a passenger identity only under an explicit contract; the default recording is anonymous.
- REFERENCE `world.emission` (F6): service activity recorded here provides activity data for transit emission estimates.
- REFERENCE `world.goodsMovement` (F3): passenger and freight services share corridors, terminals and multimodal interchange.
- imports: GTFS (ALIGN): field equivalences for timetable and network publication.
- imports: Transmodel (ALIGN): conceptual public transport reference semantics.
- imports: NeTEx (ALIGN): network, timetable and fare exchange structure equivalences.

## Stewardship

Transit operators steward network, schedule, operations and fare records for their own services; ridership aggregates are stewarded by the operator or a statistics office archetype. Trip records belong to the passenger where personal linkage exists, and all access is granted by the respective steward through the catalogue's S1/S2 ownership and access models, with audit via S4.
