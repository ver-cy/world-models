Research algorithm-policy and verification-verdict semantics for WM-XCT-034
Digital Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover signature and digest algorithm identifiers with complete parameter sets,
  curve/group/key-size references, approved/deprecated/forbidden state,
  security-strength target and pinned policy/version at validation time.
- Cover algorithm agility, downgrade resistance, absent/ambiguous parameters,
  weak hashes, randomized versus deterministic signatures, hybrid/composite
  signatures and post-quantum transition without inventing universal policy.
- Define cryptographic verification inputs and structured outcomes: valid,
  invalid, indeterminate, unsupported, malformed, policy-rejected and
  evidence-incomplete, each with machine-readable reasons.
- Keep cryptographic validity, trust-path outcome, identity binding,
  authorization, proof purpose, qualification and legal effect as separate
  dimensions. A successful primitive check must not collapse them.
- Treat signing time as an untrusted claim unless external evidence supports it.
  Record verifier/tool/version and policy pins for reproducibility, while
  execution and enforcement remain external.
- Target 1-2 bundles, 3-4 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds.
- Every local ID must begin with `sig-verdict-`.
- Prefer primary NIST FIPS 186-5, SP 800-57, SP 800-131A, official PQC migration
  guidance, IETF algorithm registries and ETSI signature-validation semantics.
