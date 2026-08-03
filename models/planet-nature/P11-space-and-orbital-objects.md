# P11 Space & Orbital Objects

This meta-model describes the near-Earth space environment as a populated register: the objects placed in orbit and their registration particulars, the orbital states, manoeuvres and conjunctions that describe where they are and where they are going, the fragments they leave behind, and the space weather that acts on all of them. It is its own model because an orbital object has an identity that survives fragmentation, transfer and reentry, and because position here is a time-parameterized state rather than a fixed geometry. The object as a manufactured asset is described in M2 and M8, its radio use in F9.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p11"
  csn: world.spaceAndOrbitalObjects
  version: 0.2.0
  displayName: "Space & Orbital Objects"
  description: "Space objects and their registration, orbital states, manoeuvres, conjunctions and reentries, with the debris and space weather environment."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.spaceAndOrbitalObjects
bundles:
  - csn: world.spaceAndOrbitalObjects.objectRegistry
    displayName: "Object registry"
    layers:
      - world.spaceAndOrbitalObjects.objectRegistry.objectIdentity
      - world.spaceAndOrbitalObjects.objectRegistry.missionAndPayload
      - world.spaceAndOrbitalObjects.objectRegistry.registrationAndCustody
  - csn: world.spaceAndOrbitalObjects.orbit
    displayName: "Orbit and tracking"
    layers:
      - world.spaceAndOrbitalObjects.orbit.orbitalState
      - world.spaceAndOrbitalObjects.orbit.maneuverAndStationKeeping
      - world.spaceAndOrbitalObjects.orbit.conjunctionAndReentry
  - csn: world.spaceAndOrbitalObjects.environment
    displayName: "Space environment"
    layers:
      - world.spaceAndOrbitalObjects.environment.spaceWeather
      - world.spaceAndOrbitalObjects.environment.debrisEnvironment
imports:
  - source: un-register-of-space-objects
    version: "*"
  - source: ccsds
    version: "*"
  - source: iso-24113-space-debris-mitigation
    version: "*"
  - source: wmo
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `objectRegistry` | Which objects exist, what they are for and who answers for them | `objectIdentity`: designators, catalogue numbers, object class and physical characteristics Â· `missionAndPayload`: mission purpose, payloads, instruments and operational status Â· `registrationAndCustody`: registration entries, registering and operating party references and custody changes |
| `orbit` | Where an object is, where it is going and what it might hit | `orbitalState`: elements, state vectors and ephemerides at epoch with covariance Â· `maneuverAndStationKeeping`: planned and executed burns, drift control and disposal manoeuvres Â· `conjunctionAndReentry`: close approach assessments, collision probability, reentry prediction and disposal outcome |
| `environment` | What the surrounding space is doing | `spaceWeather`: solar activity, geomagnetic conditions, radiation and drag-relevant indices Â· `debrisEnvironment`: fragment populations, flux models by regime and altitude |

## Objects

- `spaceObject`: an object in or returned from orbit; key attributes: catalogue designator, international designator, object class (payload, rocket body, fragment), mass, dimensions, status
- `registrationEntry`: a filed registration particular for an object; key attributes: registering party reference, filing date, orbital parameters as filed, general function statement
- `payload`: an instrument or capability carried by an object; key attributes: payload identifier, function, operating bands reference, operational status
- `orbitalState`: the object's motion at an epoch; key attributes: epoch, reference frame, elements or state vector, covariance, determination source
- `orbitRegime`: a band of orbital space; key attributes: regime identifier, altitude and inclination bounds, typical use, congestion indicator
- `maneuver`: a planned or executed change of orbit; key attributes: planned and actual time, delta-v, purpose (collision avoidance, station keeping, disposal), execution status
- `conjunctionAssessment`: an assessed close approach between two objects; key attributes: time of closest approach, miss distance, collision probability, screening source, advisory status
- `spaceWeatherObservation`: a measured environmental condition; key attributes: index or variable, value, timestamp, source, affected regimes

## Relationships

- `spaceObject` -> hasRegistration -> `registrationEntry` (1:n): objects may be registered once or re-filed as particulars change
- `spaceObject` -> carries -> `payload` (1:n): payload identity is kept separate from platform identity
- `orbitalState` -> describes -> `spaceObject` (n:1): each state is a dated determination for one object
- `spaceObject` -> occupies -> `orbitRegime` (n:1): regime assignment follows the current orbit and supports congestion views
- `maneuver` -> changes -> `orbitalState` (n:1): burns link the state before to the state after
- `conjunctionAssessment` -> pairs -> `spaceObject` (n:m): each assessment names both objects and the states screened
- `spaceObject` -> fragmentedFrom -> `spaceObject` (n:1): debris keeps a traceable parentage to the object that produced it
- `spaceWeatherObservation` -> affects -> `orbitRegime` (n:m): drag and radiation conditions are attributed to the regimes they act on

## Events

- `objectLaunched`: an object reached orbit and entered the catalogue
- `objectRegistered`: registration particulars were filed or amended for an object
- `orbitDeterminationUpdated`: a new state was determined from tracking, superseding the previous epoch
- `maneuverExecuted`: a planned burn was carried out and the resulting orbit was re-determined
- `conjunctionWarningIssued`: a close approach crossed the screening threshold and operators were notified
- `fragmentationEventDetected`: a breakup or collision produced new catalogued fragments
- `reentryOccurred`: an object left orbit, with the predicted and actual footprint recorded
- `spaceWeatherStormOnset`: geomagnetic or radiation conditions crossed a defined storm level

## Contracts

- `catalogueAccessContract`: terms for reading the object catalogue, distinguishing the public identity view from restricted high-precision ephemerides
- `conjunctionNotificationContract`: terms for operator to operator notification, including contact points, response windows and confidentiality of manoeuvre plans
- `registrationFilingContract`: terms under which an operator files or amends registration particulars with the registrar
- `spaceWeatherAlertContract`: terms for delivery of environment alerts to operators and dependent infrastructure

## Projections

- `publicObjectCatalogue`: designators, class, regime and coarse elements; omits high-precision ephemerides, covariance and mission detail
- `operatorEphemerisView`: full state, covariance and manoeuvre history for the operator's own objects; omits other operators' holdings
- `debrisEnvironmentSummary`: fragment counts and flux by regime and altitude band; omits per-object identity
- `reentryRiskBrief`: predicted reentry window and footprint for ground authorities; omits payload and mission particulars

## Composition

- REFERENCE `world.physicalItemArtifact` (M2) and `world.deviceSensorAndComputingHardware` (M8): the object as a manufactured asset and its instruments are described there
- REFERENCE `world.metaObjectOwnershipAndStewardship` (S1) and `world.organization` (O1): ownership, operator identity and custody transfer resolve there
- REFERENCE `world.communicationsAndDataTransmission` (F9): radio spectrum grants, ground stations and link budgets belong to that model
- REFERENCE `world.atmosphereWeatherAndClimate` (P4): satellite-derived fields feed observation there, and upper atmosphere density conditions drag here
- REFERENCE `world.naturalPhenomenonAndHazard` (P9): reentry and debris fall are hazards to ground exposure zones described there
- REFERENCE `world.interstateRelationsAndTreaties` (A15): registration and liability obligations between registers are agreements held there
- REFERENCE `world.timeAndCalendarReference` (N11): epochs, time scales and leap second handling resolve there
- REFERENCE `world.occurrenceEvent` (X1): launches, breakups and reentries also surface as generic occurrences on the shared timeline
- imports: un-register-of-space-objects (REFERENCE): registration particulars referenced as filed rather than restated
- imports: ccsds (EXTEND): orbit, tracking and navigation data message structures this model specializes
- imports: iso-24113-space-debris-mitigation (ALIGN): disposal and passivation concepts used by the reentry and disposal layer
- imports: wmo (REFERENCE): space weather observation and index definitions shared with the atmospheric register

## Stewardship

A space object registrar keeps the catalogue and registration record, and a space environment steward publishes tracking, conjunction screening and space weather products, each accountable for what it issues. Objects themselves stay owned by their operators through S1, restricted ephemerides and manoeuvre plans are released only under S2 access contracts, and every read of restricted precision data is logged in S4.
