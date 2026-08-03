# S6 Verification & ZK Attestation

This meta-model describes proving without showing: a party demonstrates that a predicate over their data is true (of age, holds title, within bounds) while the data itself never leaves their control. It is its own model because attestation has machinery that neither the data model nor the contract model contains: predicate catalogues, proof schemes, freshness, revocation, and verifier policies, all of which must interoperate for a proof made by one party to convince another.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:s6"
  csn: world.attestation
  version: 0.2.0
  displayName: "Verification & ZK Attestation"
  description: "Proving predicates over owned data without disclosing the data: predicates, proofs, schemes, verifiers and revocation."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.attestation
bundles:
  - csn: world.attestation.predicate
    displayName: "Predicate"
    layers:
      - world.attestation.predicate.catalogue
      - world.attestation.predicate.grounding
  - csn: world.attestation.proof
    displayName: "Proof"
    layers:
      - world.attestation.proof.generation
      - world.attestation.proof.freshness
  - csn: world.attestation.verification
    displayName: "Verification"
    layers:
      - world.attestation.verification.verifierPolicy
      - world.attestation.verification.outcomes
imports:
  - source: mu-zero-knowledge-attestation
    version: "*"
  - source: w3c-verifiable-credentials
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `predicate` | What can be claimed | `catalogue`: registered predicate types with precise semantics Â· `grounding`: which owned data backs each predicate instance |
| `proof` | Making a claim convincing | `generation`: schemes, parameters and issuance of proofs Â· `freshness`: validity windows, re-proof triggers and revocation state |
| `verification` | Deciding to believe | `verifierPolicy`: which predicates, schemes and ages a verifier accepts Â· `outcomes`: verification results with replay protection |

## Objects

- `attestedPredicate`: a registered statement type about hidden data; key attributes: subject domain, predicate expression, disclosure class.
- `proof`: the cryptographic object demonstrating a predicate; key attributes: scheme reference, public inputs, created time, expiry.
- `proofScheme`: a cryptographic method with parameters; key attributes: family, parameters, security assumptions, deprecation state.
- `presentationRequest`: a verifier's challenge naming needed predicates; key attributes: requested predicates, freshness requirement, nonce.
- `verifierPolicy`: what one verifier accepts; key attributes: accepted predicates, accepted schemes, maximum proof age.
- `verificationResult`: the outcome of checking one proof; key attributes: verdict, checked time, policy version, replay marker.
- `revocationEntry`: a marker that a proof, or the data grounding it, is no longer valid; key attributes: revoked proof reference, reason class, effective time.

## Relationships

- `proof` -> demonstrates -> `attestedPredicate` (1..1): each proof settles exactly one registered predicate instance.
- `proof` -> generatedUnder -> `proofScheme` (*..1): the scheme fixes what the proof mathematically guarantees.
- `attestedPredicate` -> groundedIn -> `registryEntry` (1..*): predicates are about S1-registered objects the prover controls.
- `presentationRequest` -> asksFor -> `attestedPredicate` (1..*): verifiers request predicates, never underlying fields.
- `verificationResult` -> evaluates -> `proof` (1..1): one result per checked presentation, replay-protected by the request nonce.
- `revocationEntry` -> invalidates -> `proof` (1..*): a change in the grounding data can void every proof built on it.

## Events

- `predicateRegistered`: a new predicate type entered the catalogue with agreed semantics.
- `proofIssued`: a prover generated a proof over their data under a named scheme.
- `proofPresented`: a proof was handed to a verifier in answer to a presentation request.
- `verificationSucceeded`: a verifier checked a proof against policy and accepted it.
- `verificationFailed`: a proof was rejected for invalidity, staleness or policy mismatch.
- `proofRevoked`: a proof was invalidated because it expired or its grounding data changed.

## Contracts

- `presentationAgreement`: prover and verifier agree that only the predicate outcome changes hands, and what the verifier may retain.
- `schemeTrustList`: verifiers and provers agree which schemes and parameter sets count as convincing, and when old ones retire.
- `revocationFeed`: verifiers subscribe to revocation entries for proofs they have accepted and may need to re-check.

## Projections

- `verifierView`: predicate, verdict, scheme and freshness; never any underlying data.
- `proverWallet`: my proofs, their validity and where they were presented; omits other provers entirely.
- `schemeRegistry`: public schemes and parameters for interoperability; omits all proofs and predicates.

## Composition

- REFERENCE `world.ownership` (S1): the prover's standing comes from holding the grounding objects; a proof over data you do not control proves nothing here.
- REFERENCE `world.accessContract` (S2): a presentation is the minimal-disclosure alternative to a read grant, and presentation agreements are S2 contracts.
- REFERENCE `world.disclosureScope` (S3): a predicate is the limiting case of a projection, a shape where a single boolean leaves.
- REFERENCE `world.accessAudit` (S4): presentations and verification outcomes are logged without payload.
- imports: mu-zero-knowledge-attestation (EXTEND): the attestation primitive this model elaborates.
- imports: w3c-verifiable-credentials (ALIGN): the presentation and verification vocabulary mapped onto requests and results.

## Stewardship

The prover, who is the owner of the grounding data, controls predicates and proofs; each verifier owns only its policy and its results. Neither side ever holds the other's data, and the S4 log records that a verification happened, not what was proven about whom.
