# WM-XCT-006 Codex pre-provider boundary

Status: preparatory boundary analysis. This is not a provider result.

- The model is a cross-cutting proof and verification mixin, not a credential,
  identity, key, authorization, decision or audit-log master.
- The attested statement and its canonical representation must be bound to the
  proof. Predicate semantics, parameterization and issuer or source authority
  remain explicit.
- Zero knowledge, selective disclosure and unlinkability are independent
  properties. A signature or verifier success does not prove all three.
- Request, challenge, proof creation, presentation, receipt, verification,
  policy evaluation and relying-party decision are separate events.
- Proof-system, curve or group, cryptosuite, canonicalization, circuit,
  verification key, trusted setup or ceremony and status method are versioned.
- Never persist private witnesses, undisclosed claims, holder secrets or
  verifier correlation data beyond the minimum authorized purpose.
- A cryptographic success establishes only the verified statement under the
  declared inputs and assumptions. It does not establish identity truth,
  authorization, freshness, eligibility or business acceptance by itself.

Adjudication must reject claims of generic zero knowledge, hidden witness
storage, ambiguous statement or circuit identity, reusable unbound proofs,
silent algorithm fallback, verification equated with authorization, and
destructive removal of challenge, status or verification evidence.
