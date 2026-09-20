# External research focus: WM-OBJ-007 Vehicle

Research a vendor-neutral, multimodal vehicle meta-model for a physical artifact
that transports or is designed to transport people, cargo, equipment or itself
through road, rail, water, air or other operational media.

Separate the individual vehicle from vehicle type, model, variant, component,
operator, trip, shipment, registration, title, permit, certificate, maintenance
work order and telemetry event. Use primary official sources across modes,
including UNECE vehicle construction categories, ISO road-vehicle identity,
official road manufacturer/VIN services, EU type approval, IMO ship identity,
ICAO aircraft registration, European rail registers, W3C SSN/SOSA observation
semantics and RFC 3339 time.

Cover the Vercy five facets in depth: stable multimodal identity and class;
geometry, dimensions, mass, capacity, materials, construction, propulsion,
energy, controls and condition; recognition markings and sensor observations;
mobility, carrying, towing, operating-envelope, interaction and safety
affordances; manufacture, ownership, registration, custody, location, service,
inspection, compliance, incidents, access, retention and provenance.

Keep quantities with unit, tolerance, method, condition, observation time and
source. Keep design limits distinct from measured state. Treat per-mode legal
and technical rules as profiles, not universal properties. Do not infer
ownership from custody, registration from identifiers, or operability from
existence.

Target about 7 bundles, 16 layers, no more than 32 findings, exactly 3 useful
questions per finding and 10 to 12 controlled functions. Return only the
required research JSON contract.
