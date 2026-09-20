Research the format-neutral signature and proof core for WM-XCT-034 Digital
Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary,
  including content binding, trust validation, preservation and governance.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Model a proof/signature as a host-bound value with a stable identifier,
  version and state; distinguish claimed signer, signing actor, key/controller,
  credential subject and verified signer identity.
- Cover proof purpose, scope, method/algorithm identifiers and parameters,
  signature value, public-key or verification-method reference, signed instant
  as a claim, and explicit verification status. A timestamp is not identity.
- Cover single signatures, independent co-signatures, ordered countersignatures,
  endorsements and threshold/multi-party signatures without treating them as
  equivalent. Make cardinality and dependency explicit.
- Separate authenticity, integrity, origin attribution, approval, authorization,
  non-repudiation and legal effect. A valid cryptographic signature alone must
  not assert all of them.
- Treat symmetric MACs, checksums, hashes, seals, time-stamps, electronic seals,
  selective-disclosure proofs and zero-knowledge attestations as explicit
  neighbors or qualified proof kinds, not silent synonyms for digital signature.
- Do not own private keys, identity/person records, credentials, CA operations,
  trust anchors, the host document/data, authorization policy, audit log,
  notarization or legal-effect determination.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `sig-core-`.
- Prefer primary NIST FIPS 186-5, IETF signature container/protocol standards,
  W3C Data Integrity, ETSI signature-policy/validation standards and current
  legislation only for carefully bounded regional notes.
