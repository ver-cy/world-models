# Enterprise identity linkage: EM-XCT-01

The first usable increment is a versioned reference profile associated with **WM-XCT-036 Alias / Same-as Mapping**, reusing a narrower **WM-XCT-011 Identifier Scheme** assignment carrier. It creates no new world-model ID. The broad enterprise identity contour remains partial.

## Boundary decision

An identifier is not a person, an account is not its owner, and a link is not a merge. The profile records a contextual assertion between a source referent and an existing local referent. It carries a qualified lookup key and an immutable source observation. A query evaluates a supplied assertion set; it does not create an authoritative identity cluster.

| Candidate | Selected form | Semantic owner | Reason and limitation |
|---|---|---|---|
| IdentifierBinding | Narrower WM-XCT-011 carrier | Source issuer | Preserves scheme/version/issuer/scope/value, source referent and assignment interval. Full scheme governance and later assignment-state revision remain external. |
| IdentityAssertion | WM-XCT-036 usage profile and explicit reference binding | Local identity steward | Has its own identity, evidence and correction history. It owns neither endpoint. |
| IdentityResolution | Derived query artifact | No independent master | An answer depends on input completeness, purpose, policy and two time coordinates. Persisting it as canonical person identity would overstate its meaning. |
| Account ownership | Deferred peer relationship | Account/person source authorities | Account-to-Person equality would erase shared, service and reassigned account distinctions. |
| Identity merge/split | Deferred transaction/migration concern | Subject owner | Requires endpoint lifecycle, survivorship, downstream repair and reversibility beyond this assertion ledger. |

The dependency graph of this reference is assertion profile → identifier carrier. Business links between referents do not create reciprocal package imports. WM-XCT-040 supplies a separately pinned composition tool; it is not the meaning of an identity assertion.

## Compared approaches and evidence

**Observed standard semantics:** [SCIM RFC 7643, sections 3.1 and 9.3](https://www.rfc-editor.org/rfc/rfc7643.txt) distinguishes provider IDs from client-scoped external IDs. This supports explicit qualification; it does not justify treating every imported HR or Git identifier as a SCIM resource. [RFC 3986, section 6.2](https://www.rfc-editor.org/rfc/rfc3986.txt) distinguishes exact comparison and scheme-specific normalization. We choose a restrictive exact-string profile and reject unsupported normalization.

**Observed formal alternatives:** [OWL 2 Individual Equality](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Individual_Equality) has stronger substitution semantics than the bounded local assertion here. [SKOS mapping properties](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#mapping) concern concepts; their names do not authorize Person equality. Global equality and automatic transitive closure are rejected for this profile. [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/) informs the distinction between revision/invalidation and deleting the described subject. Our receipt-time and bitemporal algorithm is a **design proposal**, not a claim that PROV-O mandates it.

**Observed operational practice:** [OpenRefine reconciliation](https://openrefine.org/docs/manual/reconciling) separates the original value, candidates and matching judgment. We retain source values and distinguish proposals from asserted links. We do not run an OpenRefine service, import matcher confidence as authority or claim cross-product conformance.

**Existing Vercy:** the complete current 011 and 036 JSON specifications were parsed, recursively inventoried and compared byte-for-byte with public files. Their AGENTS and publication metadata were read. Exact selected assignment/predicate definitions were retained for boundary review. This is stronger than a name match, but it is not a re-verification of all legacy sources or required parent fields. The full 036 specification still has 108-source and formal boundary holds. The profile crosswalk therefore claims narrower usage/overlap, never complete parent conformance.

`source-verification.json` records eight directly checked sources with edition, sections, date, HTTP result, byte digest, supported claim and inspection limit. Source text is paraphrased; third-party normative standards are not republished. Vercy upstream semantic packages retain the project's license. AI research is evidence to review, not a new normative authority.

## Independent studies and reconciliation

Claude and Grok received the same public boundary and synthetic acceptance requirements. Claude used a bounded CLI research run with web tools; Grok used the owner's browser in the visible Heavy mode. Actual transcripts and hashes are preserved. The precise underlying Grok model version was not exposed. Raw responses remain distinct from this Codex synthesis.

Both recommended reuse/profile over manufacturing three new entity models and treated resolution as derived. They differed on relation names: Claude retained the existing contextual-positive, explicit-negative and probable-match codes; Grok initially proposed new source-denotation predicates. Reading the exact parent register supported retaining `equivalent-in-context`, `not-same-assertion` and `probable-entity-match`. The last cannot activate; every assertion disables inference.

Both initial studies used examples that could be read as equating a Git account and a Person. The implementation is stricter: source-specific person-reference exports are demonstrated, while genuine user/service-account references retain their kind. An independently supplied scheme-kind register and disjoint subject-kind namespaces check those declarations. Real source semantics and account ownership require separate evidence and integration.

The initial Claude implementation audit blocked publication on receipt-time history preservation. Grok's focused audit identified type/namespace weaknesses and negative-result ambiguity. The revised live importer requires trusted receipt time after the input head; genesis commits to the fixed claim; namespace/type declarations are policy-bound; explicit negative and proposed-negative results are separate. The original blocking audit remains in the dossier. Follow-up verdicts and remaining limits are recorded in `review.md`.

Two objections became explicit design choices rather than new features. Conflicting assignment occurrences are retained in an assertion ledger and queried as contested, not rejected as if this were the issuer's allocator. Distinct assertion IDs may preserve independent identical claims; replay idempotency does not collapse their provenance. Backdated effective correction changes later knowledge views while preserving earlier answers only under the trusted import path. These are tested semantics, not a universal identity algorithm.

## Minimum useful configuration and scale

The startup profile needs one local subject namespace, a trusted policy, known source referents and reviewed links; it requires no HRIS or ERP product. The group fixture isolates issuer/tenant-qualified IDs and separates planned assignment occurrences across time. The AI-team fixture preserves Human and ServiceAccount distinctions. All data is synthetic and does not describe Apple, Google, OpenAI or the owner's actual systems.

This release intentionally makes no production-scale throughput claim. A large organization needs authenticated source adapters, complete input selection, indexed bitemporal storage, policy history, monitoring and transactional concurrency. The portable reference establishes semantics and negative cases that such implementations must preserve. Whole-object facets and fact ownership are recorded per exported contract type in the package.

## Next research assignments

1. **Account ownership and delegation:** distinguish account, credential metadata, principal, Person, service and role; test shared accounts, bots, ownership transfer and external collaborators. Never store secret values. Choose the existing relationship owner before creating any model.
2. **Assignment observation history:** preserve source-issued occurrence identity while closing or correcting validity later; separate source-valid, source-recorded and local-received times; support future-effective registrations without falsifying knowledge time.
3. **Policy history and federation:** separately model write grants, current read authorization, revocation, purpose, cross-Dimension projections and historical policy references. Test expiry, retroactive correction, denied disclosure and competing authorities.
4. **Merge/split and repair:** identify the endpoint owner, planned transaction, downstream referential repair, human decision, rollback and evidence retention. Prove that assertion retraction alone never merges or deletes a Person.
5. **Production binding:** enforce companion validation and receipt-time import before atomic writes; persist the complete head, reject concurrent/truncated histories, prove source-to-store round-trip and measure representative volumes.
6. **Parent ratification:** inspect complete mandatory field obligations, granularity, exclusivity, predicate admissibility, kind-change lineage, formal relationship edges and all legacy sources. A focused enterprise review must not be reported as closing those holds.

Each assignment needs its own independent Claude/Grok study, frozen audit, synthetic cases, source ledger and explicit publication boundary. The current increment is useful without claiming these tasks are complete.
