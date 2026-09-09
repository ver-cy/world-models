Research durable validation evidence for WM-XCT-034 Digital Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover trusted time as evidence distinct from signer-claimed time: time-stamp
  request/imprint, token identity, TSA/policy reference, nonce, accuracy and
  ordered relation to signature generation and validation.
- Cover validation evidence sufficient for independent replay: signature input
  digest, certificate/path snapshot or references, revocation status and
  freshness, trust configuration, algorithm policy, verifier/tool version,
  validation instant, verdict and reasons.
- Cover long-term validation and archival preservation without depending on one
  container: evidence embedding versus external evidence package, renewal by
  new timestamps or evidence records, algorithm/key expiry and evidence-chain
  continuity.
- Cover transparency-log inclusion/consistency proof references and signed-tree
  checkpoints only as optional corroboration; a log entry does not itself prove
  signer identity or document truth.
- Address missing/retracted/unavailable status responders, expired certificates,
  revoked-after-signing keys, compromised TSA, hash collision migration,
  orphaned external content and clock uncertainty.
- Keep immutable proof bytes and prior validation evidence; correction occurs
  by supersession/invalidation assertions, not mutation. Deletion remains an
  external retention/legal-hold decision.
- Do not own generic audit, evidence/case, archive-storage, blockchain, notary,
  CA/TSA or transparency-log operations.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 questions each.
- Every local ID must begin with `sig-evid-`.
- Prefer RFC 3161, RFC 4998/6283, RFC 5816, ETSI EN 319 102-1 and TS 119 102-2,
  relevant CAdES/XAdES/PAdES LTV profiles and RFC 9162 transparency semantics.
