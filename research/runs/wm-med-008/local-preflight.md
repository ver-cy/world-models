# WM-MED-008 local preflight

## Frozen subject

`WM-MED-008 Content Provenance Credential` describes one governed,
issuer-attributable and integrity-protected set of provenance assertions bound
to a media asset, rendition, segment or region. It owns credential identity,
composition, proof and validation context, lifecycle and disclosure rules.

The credential is not the media asset, creative work, depicted event, person,
organization, signature, certificate, trust decision or human-facing label.
Technical validity establishes only the checks actually performed under the
pinned profile. It cannot be promoted to factual truth or universal trust.

## External masters and adjacent models

- `WM-MED-002 Media Asset / Rendition` owns the byte-bearing asset, rendition,
  media format, fixity and technical preservation identity. The registered
  `MIX-IN` relationship is retained as a credential binding capability.
- `WM-MED-001 Creative Work / Content` owns abstract intellectual content and
  authorship context.
- People, organizations, identities, devices, software, keys, certificates,
  actions, events, repositories, rights instruments, evidence and accountable
  trust decisions remain external masters.
- C2PA, W3C VC, COSE, X.509, PROV and IPTC are version-pinned projections or
  profiles, not the canonical storage format of the Vercy model.

## Required coverage

Cover credential, manifest, claim and assertion identity; issuer, signer,
holder, validator and verifier roles; subject asset and region scope; hard and
soft bindings; assertion payload and source; capture, edit, generation and
ingredient lineage; proof suites, key and certificate evidence; claimed and
trusted time; revocation and status; embedded and external storage; durable
recovery; component validation; contextual trust policy; accessible disclosure;
privacy, harms, redaction, lifecycle, retention, audit and loss-aware crosswalks.

## High-risk conflations to reject

- asset, rendition, credential, manifest store, manifest, claim and assertion;
- issuer, signer, claim generator, creator, subject, holder and verifier;
- hard binding, soft binding, identifier, fixity and asset identity;
- signature validity, signer trust, assertion truth and asset trustworthiness;
- claimed signing time, trusted timestamp, validation time and observation time;
- certificate validity, revocation status, trust-list membership and trust;
- provenance, authorship, copyright, ownership, editorial endorsement and truth;
- embedded credential, external manifest, repository record and display label;
- update, redaction, revocation, metadata removal, corruption and deletion.
