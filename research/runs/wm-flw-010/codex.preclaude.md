# Codex pre-provider hypothesis for WM-FLW-010

## Boundary

Route / Itinerary should be an aggregate family only for catalogue convenience,
with a mandatory kind discriminator. Route is a directed reusable or computed
network path. Itinerary is a selected or candidate ordered planning result.
Actual journey execution, movement observations and outcomes remain in
WM-FLW-009; master networks, schedules, services, people, vehicles and booking
objects remain external.

## Proposed structure

1. Identity, kind and boundary.
2. Network path and ordered structure.
3. Constraints, criteria and selected plan.
4. Temporal, service and resource plan.
5. Lifecycle, change and evaluation.
6. Provenance, access and interoperability.

Each bundle should contain two layers and four findings. Each finding should
ask three model-specific questions and define one data element and one serial
evidence artifact. Ten functions should register, define, compose, constrain,
record candidates, select, bind schedules/resources, validate continuity,
supersede/replan and project. Routing computation itself remains an external
engine function; this model records the governed request, parameters, result
and lineage.

## Expected hard points

- Transmodel ROUTE and JOURNEY PATTERN differ from GTFS route and trip.
- OGC route-exchange work is useful but not yet an approved standard.
- A route can outlive many itineraries and journeys; an itinerary may compose
  several modal routes, off-network legs and activities.
- Alternatives, predictions, estimates and selected/confirmed plans need typed
  state and immutable successor history.
- A future major version may split this aggregate into linked Route and
  Itinerary models; current projections must remain loss-aware.
