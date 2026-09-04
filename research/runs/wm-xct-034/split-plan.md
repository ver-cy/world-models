# WM-XCT-034 bounded Claude research plan

WM-XCT-034 is a format-neutral mixin for a digital signature or other
cryptographic proof bound to a host statement, artifact or event. It is
researched through twelve bounded, independently schema-valid passes.

1. `signature-core` owns proof identity, signed-subject binding, signer and key
   references, method identity, purpose and multi-signature topology.
2. `payload-binding` owns protected content selection, digest-based binding,
   content identity/version, detached references and protected parameters.
3. `canonicalization-security` owns transforms, canonicalization, domain
   separation, reference resolution and ambiguity/replay defenses.
4. `binding-projections` owns detached/enveloped/enveloping forms, projection
   losses and round-trip limits across major signature bindings.
5. `trust-chain-status` owns verification-method resolution, certificate and
   trust-path references, key status, revocation and historical validation.
6. `algorithm-verdict` owns algorithm policy, security strength, cryptographic
   verification inputs and structured result semantics.
7. `evidence-preservation` owns trusted time, validation evidence, long-term
   preservation, renewal, transparency and independently replayable evidence.
8. `governance-facts` owns authority, lifecycle, provenance, access, retention,
   legal-policy references and interoperability controls.
9. `service-layers` owns the complete canonical service-layer and AGENTS.md
   bootstrap contract with only a compact supporting structure.
10. `prepare-attach` owns read, prepare, external sign/prove request and safe
    correlation/attachment semantics.
11. `multi-sign-lifecycle` owns co-sign, countersign, invalidate and supersede
    operation semantics.
12. `verification-operations` owns verify, renew/preserve, export/project and
    disposition-readiness semantics.

Each pass uses a disjoint local-ID prefix. The deterministic merger keeps the
complete boundary from `signature-core`, service layers from `service-layers`,
remaps sources and validates the union. A later no-tools
adjudication must verify that the result remains a host-scoped proof mixin and
does not become a key manager, identity record, certificate authority, trust
list, authorization decision, document, notarization service, audit log,
generic evidence model or zero-knowledge predicate-attestation model.
