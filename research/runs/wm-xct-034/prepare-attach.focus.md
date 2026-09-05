Research safe proof preparation and attachment operations for WM-XCT-034
Digital Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Define read/as-of, prepare-signing-input, request external sign/prove and
  attach-returned-proof operations only.
- Every mutation has idempotency and optimistic-concurrency preconditions.
  Preparation returns exact protected input or digest with payload/version,
  algorithm/parameters, proof purpose, context/audience, policy pins, request
  correlation identifier and expiry.
- Private-key access, signer authorization and cryptographic primitive execution
  remain external. Never send unpinned mutable references to the executor.
- Before attachment, check request correlation, exact payload/digest,
  algorithm/parameters, verification-method reference, protected context,
  expiry and replay/idempotency. Reject mismatched or unsolicited proofs.
- Reads distinguish current state from explicit historical/as-of state and do
  not infer validity from proof presence or prior successful verification.
- Proof bytes are immutable and attachment appends a host-bound version; it does
  not create host identity, approve workflow or construct an audit log.
- Target 1-2 bundles, 3-4 layers and 6-8 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `sig-prep-`.
