# WM-MED-008 source verification

The Codex fallback uses 26 primary or official sources. Versions and current
status were checked on 7 September 2026 before synthesis. All source URLs
returned HTTP 200 in direct GET checks.

The normative center is C2PA Content Credentials 2.4 (April 2026). The official
2.4 index currently links some separately maintained guidance documents at
their 2.2 or 2.3 publication paths and the attestation document at 1.4. Those
paths and their role as current linked documents are preserved rather than
silently assigning them a 2.4 version.

Important interpretation constraints:

- C2PA Content Credential, W3C Verifiable Credential and a generic provenance
  record are aligned models, not identical objects.
- A valid signature supports integrity and signer attribution under a pinned
  profile. It does not prove factual truth, authorship, copyright, safety,
  editorial endorsement or universal trust.
- Hard binding is exact-profile digest evidence; soft binding is a recovery
  signal with possible ambiguity. Neither replaces governed asset identity.
- Claimed signing time, trusted timestamp, certificate validity, revocation
  observation, validation time and ingestion time are separate clocks.
- Trust-list membership, technical validation and a verifier's contextual trust
  decision are separate assertions with separate authorities.
- Legal identity, electronic-signature, privacy, copyright, evidentiary and
  disclosure effects require adopting-Dimension jurisdictional profiles.
