# WM-MED-008 pre-provider research notes

## Provisional boundary

Treat the subject as an aggregate credential record whose durable identity
survives changes of asset location, storage representation, validator and
display UI. Do not decide aggregate versus entity from the registry's
`standalone-mm` packaging label; the no-tools audit must adjudicate the kind.

The registered relationship to `WM-MED-002` is a mix-in capability: a media
asset can carry or reference provenance credentials, while the credential and
asset retain separate identities and lifecycles.

## Evidence plan

Use C2PA 2.4 for content-provenance composition and validation, W3C VC 2.0 for
generic credential roles and status, IETF standards for cryptographic and time
evidence, PROV and Web Annotation for lineage and scoped targets, and IPTC and
NIST for digital-source vocabulary and complementary AI transparency risks.
Record authority, release, URL, access status and the exact boundary each source
supports. Preserve absence of external provider review as a visible hold.
