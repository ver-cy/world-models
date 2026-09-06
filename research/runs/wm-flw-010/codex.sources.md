# WM-FLW-010 Codex source notes

The fallback synthesis uses official standards bodies, public authorities and
maintainers. The governing distinction is structural: Transmodel separates a
ROUTE from its JOURNEY PATTERN and journeys; GTFS gives `routes.txt`,
`trips.txt`, `stop_times.txt` and `shapes.txt` its own profile semantics; OGC
Routing Pilot material represents a computed route using a definition,
overview and ordered segments; EU multimodal rules describe a machine-readable
travel itinerary returned from a journey request.

The OGC API Routes overview and Route Exchange Model are used only as developing
design material. The OGC standards roadmap still lists Route Exchange Model
21-001 as proposed on 2026-09-06, so the model does not claim approved OGC
conformance. GeoSPARQL, GeoJSON, ISO 19133, ISO 19141 and OGC Moving Features
support spatial/navigation alignment and the route-versus-actual-trajectory
boundary. OWL-Time and RFC 3339 support typed clocks; PROV-O, DQV and ODRL
support lineage, quality and governed access.

The result is deliberately format-neutral. Source vocabularies are external
profiles with pinned versions and semantic-loss declarations, not the model's
canonical storage format.
