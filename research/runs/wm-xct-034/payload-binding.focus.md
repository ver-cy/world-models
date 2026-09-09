Research protected-payload binding for WM-XCT-034 Digital Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Define exactly what host statement, artifact version, field set, graph or
  event is protected, without owning that host and without choosing a storage
  or signature format.
- Cover direct versus digest-based binding; digest method/value; content
  identifier, version and master-system reference; content type and length;
  whole-object versus selected-part scope; detached reference and immutable
  external-resource pinning.
- Separate protected from unprotected attributes and require critical protected
  parameters to be understood. Bind proof purpose, audience/context and expiry
  where the chosen proof method relies on them.
- Preserve the exact protected input or digest for dependent countersignatures.
  Treat missing, mutable, ambiguous or differently versioned payloads as an
  explicit failure, never as an empty or substituted value.
- Keep canonicalization mechanics, parsers, cryptographic execution, document
  storage and approval workflow external.
- Target 1-2 bundles, 3-4 layers and 6-8 findings with 3-5 discriminating
  questions each. Use at least eight question kinds.
- Every local ID must begin with `sig-payload-`.
- Prefer primary RFC 5652/7515/9052, W3C Data Integrity and XML Signature
  requirements that directly define protected input and reference binding.
