# WM-FLW-010 bounded external research focus

Produce one complete schema-valid result for `WM-FLW-010 Route / Itinerary`.

Treat the root as an aggregate family with a mandatory discriminator:
`route`, `itinerary`, or `combined-plan`. A route is a reusable or computed
directed path through network nodes, links and segments. An itinerary is an
ordered planning result made of legs, stages, calls, visits or transfers, with
planned times, modes, services, resources and constraints. Preserve the
distinction throughout identity, lifecycle, questions, artifacts and functions.

Cover stable identity and revision; origin, destination and ordered waypoints;
nodes, links, segments, geometry and topology; itinerary legs, stages, visits,
calls and transfers; direction and traversal order; planned timing, operating
day, validity and timezone basis; mode, service, schedule, vehicle and resource
references; traveller, vehicle, cargo, accessibility and operational
constraints; routing criteria and objective weights; candidate alternatives,
selection and rejection rationale; distance, duration, cost, emissions, energy,
risk, toll and quality estimates; disruption, invalidation, re-routing and
successor plans; source network, dataset, routing engine, algorithm, parameters,
computation job and provenance; privacy, access, retention, licensing,
reconciliation and loss-aware projections.

Keep journeys and actual movement, transport networks, places and stops,
schedules and services, people, vehicles, bookings, tickets, fares, activities,
accommodation, shipments, incidents, weather, routing engines and source
datasets as external masters. Do not conflate route with itinerary, reusable
route with computed route, itinerary with journey, line with route, route with
journey pattern, route segment with journey leg, waypoint with stop/call/visit,
topology with geometry, requested constraint with selected outcome, estimate
with commitment, alternative with selected plan, reroute with mutation, or
route lifecycle with routing-computation job lifecycle.

Treat candidate parent `WM-FLW-009 Journey / Trip` as a compositional reference,
not inheritance: Journey owns the planned or actual movement episode and its
observations/outcomes; Route / Itinerary owns path and planning-result identity,
composition, alternatives and successor-plan history. Flag whether this
aggregate family should later split into separate Route and Itinerary models.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer CEN Transmodel and NeTEx, GTFS Schedule, OGC API Routes and
the OGC Routing Pilot route exchange model, GeoSPARQL, GeoJSON, ISO 19133,
ISO 19141 or OGC Moving Features for the execution boundary, EU multimodal
travel-information rules, Schema.org Trip, OWL-Time, RFC 3339, PROV-O, DQV and
ODRL. Explicitly state that OGC API Routes and Route Exchange Model remain
proposed/developing material as of 2026-09-06. Pin versions or access dates and
keep modal, jurisdictional, accessibility, safety, privacy, licensing and
conformance limits explicit.

