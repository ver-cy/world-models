Research trust-chain and revocation-status semantics for WM-XCT-034 Digital
Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover verification-method resolution for raw public keys, certificates,
  credential and DID-method references without owning those external records.
- Cover certificate path candidates, selected path, trust-anchor and trust-store
  version references; validation/as-of instant; basic constraints, name
  constraints, policy constraints, key usage and extended key usage.
- Cover key and credential validity intervals, compromise, revocation,
  suspension and supersession. Model CRL and OCSP evidence, responder
  authorization, thisUpdate/nextUpdate freshness, nonce behavior, stapling and
  hard-fail/soft-fail/unknown status without choosing one universal policy.
- Separate current-time validation from validation at signing/best-signature
  time and later historical replay. Missing or stale status evidence is
  indeterminate/evidence-incomplete, not automatically invalid cryptography.
- External CA issuance/revocation, trust-list operation, directory/DID
  resolution, policy decision and cryptographic execution remain outside.
- Target 1-2 bundles, 3-4 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds.
- Every local ID must begin with `sig-chain-`.
- Prefer primary RFC 5280/6960, ETSI certificate validation/trust-list standards
  and W3C DID resolution material where it is directly relevant.
