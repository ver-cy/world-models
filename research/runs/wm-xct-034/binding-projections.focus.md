Research signature binding forms and interoperability for WM-XCT-034 Digital
Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover enveloped, enveloping and detached forms, including payload discovery,
  reference resolution, protected headers/properties and attachment topology.
- Compare CMS/CAdES, XMLDSig/XAdES, JWS, COSE, PDF/PAdES and W3C Data Integrity
  as projections. None is canonical and none may silently supply a model-wide
  default.
- Record projection losses for proof purpose, signer/key identity, signed
  properties, canonicalization, detached references, countersignatures,
  timestamps, certificate/revocation evidence, multi-signature topology and
  long-term validation material.
- Cover round-trip impossibility, unsupported critical parameters, algorithm
  identifier/parameter differences, duplicate or conflicting embedded evidence,
  media-type ambiguity and unsafe fallback between bindings.
- Distinguish a binding profile/version from the logical proof version and from
  any host artifact version. External encoders/parsers own execution.
- Include template/artifact requirements for each projection plus loss and
  conformance reports, using master-system ID, governed IRI, then Dimension ULID
  and never a date as identifier.
- Target 2 bundles, 4-5 layers and 8-10 findings with 3-5 discriminating
  questions each. Use at least eight question kinds.
- Every local ID must begin with `sig-proj-`.
- Prefer primary IETF, W3C and ETSI binding standards and publicly available PDF
  signature material; mark paywalled clause-level limits explicitly.
