Research canonicalization and context-security semantics for WM-XCT-034
Digital Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover ordered transform/canonicalization chains and their versioned algorithm
  identifiers, parameters, input/output media types and externally executed
  implementation pins. The output protected bytes/digest must be reproducible.
- Cover URI and fragment resolution, base URI, character encoding, Unicode,
  whitespace, line ending, namespace, numeric/date, map-key ordering, duplicate
  key and RDF graph normalization issues without making one syntax canonical.
- Require domain separation and contextual/purpose binding when applicable.
  Address replay, substitution, wrapping, parser differential, confused-deputy
  and cross-protocol reuse; unknown critical transforms must fail closed.
- Distinguish an absent canonicalization step from an explicit identity/no-op
  step. Preserve the original host representation and record any irreversible
  transform or excluded content.
- Keep payload identity, proof verification, parsing/canonicalization execution,
  format encoding and security-policy enforcement external.
- Target 1-2 bundles, 3-4 layers and 6-8 findings with 3-5 discriminating
  questions each. Use at least eight question kinds.
- Every local ID must begin with `sig-c14n-`.
- Prefer primary XML C14N/XMLDSig, RFC 8785 JCS, W3C RDF Dataset Canonicalization
  and Data Integrity, JWS/COSE signing-input rules and security considerations.
