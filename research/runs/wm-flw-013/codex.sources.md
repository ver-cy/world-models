# WM-FLW-013 Codex source notes

The synthesis treats Supply-chain Trace / Chain of Custody as a reusable graph
pattern, not a replacement for the objects, events or evidence it links. GS1
EPCIS 2.0.1, CBV 2.0 and Global Traceability 2.0 provide the main event,
critical-data, object, aggregation, transformation, location, source,
destination, query and error-declaration semantics. UN/CEFACT supplies the
cross-industry multimodal and cross-organizational visibility boundary.

ISO 22095 provides generic chain-of-custody terminology and models. Its 2026
mass-balance part makes system boundary, conversion and attribution rules
explicit; ISO 22005 is a food-traceability profile and ISO 28000 contributes
security-management context. FDA food traceability and the EU Digital Product
Passport remain jurisdictional profiles. DCSA Track and Trace and IATA ONE
Record remain maritime-container and air-cargo modal profiles.

RFC 3339 and RFC 8785 support qualified clocks and deterministic integrity
input. PROV-O, DQV, ODRL and Verifiable Credential Data Integrity support
provenance, quality, governed disclosure and verification material. A digest,
signature or valid credential can support an assertion but does not by itself
prove real-world truth, custody, conformity or legal effect.
