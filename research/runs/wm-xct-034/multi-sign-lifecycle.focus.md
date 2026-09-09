Research multi-signature and proof lifecycle operations for WM-XCT-034 Digital
Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Define independent co-sign, dependency-aware countersign, invalidate and
  supersede operations only.
- Every mutation has idempotency and optimistic-concurrency preconditions.
  Original proof bytes and every earlier version remain immutable.
- Co-signatures bind independently to the same pinned payload/version;
  countersignatures bind to the exact prior signature bytes/digest. Preserve
  dependency order, purpose and required participant/threshold declarations.
- Report partial multi-party completion per member and dependency; never infer
  threshold satisfaction, authorization or workflow approval from a subset
  unless an external policy result explicitly states it.
- Invalidation appends a reasoned assertion scoped to proof, signer/key,
  payload binding or policy use; it does not revoke a key/certificate or delete
  content. Supersession links correction/replacement and effective interval.
- External cryptographic execution, authorization, policy enforcement, audit
  storage, host lifecycle and physical deletion remain outside.
- Target 1-2 bundles, 3-4 layers and 6-8 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `sig-life-`.
