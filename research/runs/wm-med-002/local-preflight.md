# WM-MED-002 local preflight

## Frozen subject

`WM-MED-002 Media Asset / Rendition` describes one governed media-asset record
and the identity-bearing technical representations associated with it. A media
asset may point at a preservation master, mezzanine, access copy, thumbnail,
segment set or other rendition, but every representation keeps its own stable
identifier, byte-level fixity, media type, technical characteristics and
lifecycle state.

The slash in the catalogue name is a scope label, not permission to collapse
the asset, every rendition and the represented intellectual content into one
identity. The record is a logical management aggregate; a rendition is a
separately addressable technical representation within that aggregate.

## External masters and adjacent models

- `WM-MED-001 Creative Work / Content` owns abstract intellectual content,
  authorship and work-level identity.
- `WM-MED-003 Publication / Edition` owns release, edition and publication
  identity.
- `WM-MED-004 Audio / Video Recording`, `WM-MED-005 Image / Graphic`,
  `WM-MED-006 3D Asset / Scene` and `WM-MED-007 Broadcast / Stream` own
  medium-specific semantics.
- `WM-MED-008 Content Authenticity Credential` owns signed provenance claims;
  it may bind to an asset or rendition but cannot replace its identity.
- People, organizations, agreements, rights statements, policies, storage
  services, locations, workflows, observations and preservation events remain
  external references.

## Required coverage

Cover identity and relationships; technical representation inventory; byte
fixity and format identification; dimensions, duration, tracks and encoding
profiles without duplicating specialist models; creation and derivation
lineage; embedded and sidecar metadata; rights and policy bindings; accessibility
and localization renditions; preservation, storage, availability and integrity;
publication/distribution projections; authenticity evidence; lifecycle,
supersession and deletion; quality and fitness assessments; security and
privacy risks; machine-actionable retrieval, validation and transformations.

## High-risk conflations to reject

- abstract work, expression, edition, asset record, rendition and file bytes;
- filename, URL, storage key, checksum and durable asset identity;
- encoding format, media type, codec, container, profile and conformance;
- preservation master, source capture, mezzanine and best-quality copy;
- derivation claim and cryptographically verifiable provenance;
- technical quality, perceptual quality, accessibility and fitness for purpose;
- availability, possession, custody, ownership, copyright and licensed use;
- deletion request, logical withdrawal, storage deletion and verified erasure.
