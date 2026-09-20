# WM-XCT-017 Codex pre-provider boundary

Status: preparatory boundary analysis. This is not a provider result.

- An attestation is a source-qualified assertion by an attester. A credential
  is a bounded representation of one or more claims with issuer and lifecycle
  metadata. A presentation is a separate disclosure event and artifact.
- Credential validity, cryptographic verification, current status, issuer
  authority, claim truth and relying-party acceptance are separate judgments.
- The credential references issuer, subject, holder, verifier, keys, mandates,
  evidence, policies and decisions; it does not absorb their master records.
- Licence and permit credentials may evidence an external permission-bearing
  grant, but this model does not itself own authorization or enforcement.
- Issuance, delivery, activation, suspension, revocation, expiry, renewal,
  correction and supersession preserve immutable lineage and effective time.
- Selective disclosure does not automatically provide zero knowledge,
  unlinkability or anonymity. Status checking can create correlation risk.
- Holder custody of a copy does not imply ownership of issuer assertions or
  authority to alter them.

Adjudication must reject mutable issued claims without lineage, status treated
as timeless, issuer identity conflated with authority, proof equated with claim
truth, presentation history treated as issuer-owned by default, hidden
information loss and credential evidence represented as the permission itself.
