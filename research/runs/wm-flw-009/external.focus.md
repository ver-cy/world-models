# WM-FLW-009 bounded external research focus

Produce one complete schema-valid result for `WM-FLW-009 Journey / Trip`.

Treat the root as one identity-bearing planned, undertaken or completed movement
of a person or vehicle between declared places or journey endpoints. Cover
journey identity and kind; traveller, driver, operator, vehicle and party roles;
person trip versus vehicle journey; origin, destination, intermediate calls and
ordered legs or stages; purpose and journey reason; transport modes and mode
changes; planned, predicted, estimated, observed and actual departure, arrival,
passing and duration values; operating day and time-zone basis; route, path,
network, place and stop references; service, schedule and trip-pattern bindings;
access, transfer and connection context; accessibility and traveller constraints;
status, progress, cancellation, diversion, interruption and completion; actual
trajectory and position evidence; distance, speed, occupancy, emissions and
quality observations; grouping into wider travel and subtrips; provenance,
privacy, access, retention, reconciliation and loss-aware projections.

Keep reusable route and path definitions, itinerary and journey-plan products,
transport network, places, stops, schedules, services, bookings, tickets, fares,
vehicles, people, organizations, shipments, consignments, cargo, incidents,
weather, payments and sensor records as external masters. Do not conflate a
person trip with a vehicle service journey, a journey with its reusable route,
a requested or proposed itinerary with an accepted plan, planned or predicted
times with observations, a position fix with a completed trajectory, a boarding
with a whole passenger trip, a vehicle journey with its operating block, or a
trip purpose with every activity performed en route.

The candidate parent `WM-FLW-007 Passenger Mobility / Transit` is narrower in
some respects and broader in others: retain it as a compositional reference
rather than assuming inheritance. Preserve the candidate incoming relation
`WM-FLW-011 Shipment / Consignment REFERENCE WM-FLW-009`: a shipment may cite
transport journeys, but cargo and custody remain shipment-owned. Treat
`WM-FLW-010 Route / Itinerary` as a boundary neighbor whose reusable route and
planning result remain external.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer Transmodel EN 12896 and its passenger-information material,
GTFS Schedule and Realtime, OGC API Moving Features and Moving Features
encodings, UNECE/Eurostat/ITF transport-statistics definitions, UN Tourism
statistics, EU multimodal travel-information rules, UK National Travel Survey
definitions, Schema.org Trip, GeoSPARQL, OWL-Time, RFC 3339, PROV-O, DQV and
ODRL. Pin versions or access dates and keep modal, statistical, jurisdictional,
privacy, licensing and conformance limits explicit.

