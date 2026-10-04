# WM-ACT-043 bounded external research focus

Produce one complete schema-valid result for `WM-ACT-043 Business Continuity / Recovery`.

Treat it as a governed continuity-capability aggregate whose released plans may
be invoked by incident response. Cover capability identity and scope, critical
products and services, prioritized activities, impacts and time objectives,
dependencies and minimum resources, continuity strategies, solution selection,
plan releases and procedures, activation criteria and authority, communications,
people and competence, supply-chain continuity, exercise programmes and
scenarios, evaluation and corrective actions, disruption activation, continuity
mode, restoration, recovery, reconstitution, return to business as usual,
metrics, provenance, interoperability, retention, access and safe agents.

Keep Incident, Incident Response, Risk, Organization, Product or Service,
Activity, Person, Role, Facility, Asset, Information System, Dataset, Supplier,
Contract, Communication and Audit masters separate. Do not conflate BIA impact
windows with promised recovery targets, plan approval with operational
activation, invocation with successful recovery, backup existence with verified
restorability, exercise success with real-event capability, or restored service
with normal operations.

The registry parent candidate is `WM-ACT-008 Plan / Schedule`; the only relation
ledger row is candidate incoming `WM-ACT-042 REFERENCE WM-ACT-043`, meaning an
incident response may invoke a continuity or recovery plan. Treat both as
candidate metadata, not approved composition.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer ISO 22301:2019 with Amendment 1:2024, ISO 22313:2020, ISO/TS
22317:2021, ISO/TS 22331:2018, ISO/TS 22318:2021, ISO/TS 22330:2018, ISO
22398:2013, NIST SP 800-34 Rev. 1, NIST SP 800-184, NIST CSF 2.0, FEMA
Continuity Guidance Circular 2018 with 2024 update, EU DORA, W3C PROV-O and RFC
3339. Mark ISO catalogue abstracts and regional profiles as limited evidence.
