# WM-XCT-006 bounded external research focus

Produce one concise, complete `model-research.schema.json` result for
`WM-XCT-006 Verification / ZK Attestation`.

## Frozen boundary

- Treat this as a mixin that binds a verifier request, predicate or statement,
  proof or attestation material, disclosure semantics, freshness and a
  source-qualified verification result to a host claim or interaction.
- The intended use is proving a predicate without disclosing underlying data,
  but do not claim zero knowledge unless the named proof system and profile
  establish it. Separate selective disclosure, derived proofs, SD-JWT, BBS,
  range or membership proofs, hardware remote attestation and generic digital
  signatures.
- Keep credential, subject, issuer, holder, verifier, key, trust registry,
  policy, decision, source dataset and audit-log masters external.
- Preserve statement and circuit identity, canonicalization and transcript
  binding, public inputs, commitments, proof-system and cryptosuite versions,
  keys or parameters, challenge, domain, nonce, audience, time, status and
  verification evidence.
- Distinguish cryptographic verification from authorization, identity truth,
  current eligibility and business acceptance.
- Exclude secrets, witnesses, private inputs and exploit-enabling material.

## Size and evidence limits

- Target 6 bundles, 12 layers, 24 findings, 72 discriminating questions, 24
  artifacts and 10 functions.
- Use at least 8 current primary official sources from at least 4 independent
  organizations. Prefer W3C VC Data Model, Data Integrity, Bitstring Status
  List and BBS cryptosuite, IETF SD-JWT, OpenID4VP, NIST and ZKProof or
  cryptographic primary specifications.
- Every structure and function element needs source references.
- State proof-system, trust, privacy, interoperability, implementation and
  external-review limitations as holds.
