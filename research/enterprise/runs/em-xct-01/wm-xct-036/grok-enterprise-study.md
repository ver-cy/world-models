# EM-XCT-01 — Enterprise identity links

**Bounded independent review.** Status of this note: design recommendation over inspected public sources. It is not a catalogue publication, not a second-provider verification of WM-XCT-036, and not a claim that tests were run.

**Recommendation in one line.** Reuse WM-XCT-011 for qualified identifier carriage and assignment; publish a *narrow enterprise profile* of WM-XCT-036 for identity assertions; treat IdentityResolution as a *named derived query contract* over authorized active claims. Do not mint a new world-model mixin merely to grow the catalogue. Do not store a golden Person produced by merge.

---

## 1. Inspection scope (what was actually read)

Inspected evidence is distinguished from proposals throughout. Where a file could not be read end-to-end, that limit is stated.

| Source | What was inspected | What was not |
|---|---|---|
| WM-XCT-011 spec.yaml + landing + AGENTS.md | Purpose, in/out of scope, assignment-record fields, reuse/quarantine, scheme-specific equivalence, mapping-as-assertion, collision language, privacy notes. Version **0.3.0-research.1**, mixin, **6 bundles / 20 layers**, dual-provider, `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`. AGENTS.md is a short pointer: read spec.yaml; do not claim canonical completeness while `publicationHolds` is non-empty. | Full YAML end-to-end; every finding/artifact; paywalled ISO texts cited by 011; deferred identifier families (E.164, CID/multihash, ledger addresses, etc.). |
| WM-XCT-036 spec.yaml + landing + AGENTS.md | Owned envelope, exclusions, endpoint non-ownership, relation-kind slot, evidence/confidence, lifecycle proposal→asserted→disputed→superseded→retracted→tombstoned, conflict recording. Version **0.3.0-research.1**, mixin, **27 bundles / 65 layers / 537 questions**. Landing discloses Claude-only owner waiver and live re-verification hold on **108** cited URLs. AGENTS.md is the same short pointer. | Full 65-layer YAML; the 108 sources; the historical Claude-only study. **This review does not repair that scope.** |
| WM-XCT-040 README 0.1.1 | Exact pinned composition, `commercial-company` preset, semantic-only vs native-binding, nested-snapshot companion validator, no migration of existing Dimensions, no IAM. | Byte-verification of SHA pins; running `composition.py`. |
| OWL 2 Direct Semantics (Rec. 11 Dec 2012) §2.3.6; Primer §4.7 | SameIndividual / DifferentIndividuals model conditions; no unique-name assumption. | Whole OWL 2 suite. |
| SKOS Reference (Rec. 18 Aug 2009) §10, §10.6.8 | exactMatch / closeMatch / relatedMatch; transitivity; why `owl:sameAs` is typically inappropriate. | SKOS Primer beyond mapping notes. |
| RFC 7643 (Sept 2015) §§2.2, 2.4, 3.1, 4.1, 9 | `id` vs `externalId`; `userName`; multi-valued `emails`; tenant anti-correlation. | Remainder of the RFC. |
| RFC 3986 (Jan 2005) §§1.2.2, 6, 6.2 | Identification ≠ access; comparison ladder; scheme-specific normalization. | §§1–5 except 1.2.2. |
| PROV-DM (Rec. 30 Apr 2013) Invalidation | Invalidation ends availability; does not erase prior generation/usage; distinct from Revision. | PROV-CONSTRAINTS, whole PROV-O. |
| Reconciliation API v0.2 (W3C CG Final, 10 Apr 2023) + OpenRefine recon docs | Heuristic candidates (`id`, `name`, `score`, optional `match`); client judgment distinct from service suggestion. **Not a W3C Recommendation.** | Data-extension/suggest APIs; scoring internals of any one service. |

FHIR Identifier (`system` / `value` / `period` / `assigner` / `use`) is cited by 011 as a shape analogue; this review used public datatype descriptions only and does not claim FHIR-profile conformance.

---

## 2. Boundary table

| Candidate | Decision | Owns in this study | Does not own | Why |
|---|---|---|---|---|
| **IdentifierBinding** | **Reuse** WM-XCT-011 assignment + carriage | Scheme-qualified value (as-received + scheme-canonical), assigner, issuer/tenant scope, use marker, valid time, record/knowledge time, reuse/quarantine policy, exclusive-binding flag | The Person/Agent referent; proofing; authn/authz; probabilistic linkage | 011 already binds “an identifier to a referent, with assigner, evidence and effective period” and forbids a universal normalizer. A second binding type would fork the parent. |
| **IdentityAssertion** | **Profile** of WM-XCT-036 (narrow) | Identified, versioned, Dimension-scoped claim that two *externally owned* references stand in a named relation, with evidence, bitemporal window, and append-only lifecycle | Endpoint mutation; equality closure; matching engines; merge/survivorship; access grants; audit storage; human proofing | 036 already draws this line: it “never allocates or renames an identifier, never edits an endpoint record, and never executes matching, merge, redirect, reasoning closure, authorization or audit.” |
| **IdentityResolution** | **Defer as a world-model**; **include as a derived query contract** in the executable profile | Four-state evaluation `accepted \| contested \| candidate \| unknown` at `(valid-time, knowledge-time)` under an independent policy | Subject mastership; golden-record persistence; property inheritance; disclosure | A single 036 envelope is one claim. Contested equal-authority links, rehires, and retraction-from-derived-views-only are properties of a *set* of claims plus policy. |
| Matching / reconciliation engines | **Out** | — | Candidate generation, scores, `match=true` | Reconciliation API is explicitly heuristic and service-agnostic; a candidate is not an assertion. |
| Destructive merge / split / reassignment of endpoints | **Out** unless a fully reversible contract is demonstrated (it is not) | — | Survivorship, Person collapse, identifier rewrite | 036 excludes merge; PROV invalidation ends *use* of an assertion entity, not the Person or the source row. |
| `owl:sameAs` export / SKOS exactMatch closure | **Out** of v1 | Optional later *documented alignment* with `inference_permitted=false` | Global individual equality; transitive IR interchange | See §4. |
| New mixin “EM-XCT-01” | **Do not mint** | Profile document + minimum schema | New owned semantics | Catalogue growth is not a design reason. |

Neighbor constraints from 011 remain in force: an identifier is a label, not a credential; RFC 3986 identification does not imply access; SKOS concept schemes govern meaning, identifier schemes govern denotation.

---

## 3. Five distinctions that must stay lexical

These are not synonyms. Treating any two as the same is a semantic-negative.

1. **Mapping assertion.** A reified, identified, versioned, Dimension- and purpose-scoped claim with evidence and a lifecycle. This is the 036 object, profiled. It does not mutate endpoints.
2. **Global logical equality.** OWL 2 `SameIndividual(a₁…aₙ)` is satisfied iff `(aⱼ)ᴵ = (aₖ)ᴵ` for all listed names. OWL does not assume unique names; asserting `sameAs` licenses a reasoner to copy every fact from one name onto the other.
3. **Matching candidate.** Reconciliation API / OpenRefine: a service returns `{id, name, score, match?}`. The protocol is heuristic; the client (or a later authorized steward) decides. `match=true` is a service opinion, not an enterprise identity decision.
4. **Resolver decision.** Policy evaluation over the *authorized active* assertion set at a pair of times, returning `accepted | contested | candidate | unknown` plus the supporting and contesting assertion ids. Computed, recomputable, non-authoritative.
5. **Destructive data merge.** Survivorship, golden-record construction, rewriting either endpoint, collapsing two Persons, deleting source rows. Out of scope.

SKOS makes the same kind of cut for concepts: `skos:exactMatch` is high-confidence interchangeability in information-retrieval applications, transitive, and a sub-property of non-transitive `skos:closeMatch` (compound-error rationale). SKOS §10.6.8: `owl:sameAs`, `owl:equivalentClass` or `owl:equivalentProperty` “would typically be inappropriate for linking SKOS concepts in different concept schemes, because the formal consequences that follow could be undesirable” — two concepts forced identical inherit both `skos:prefLabel`s and both schemes, which the SKOS integrity conditions reject. Enterprise HR ↔ Git ↔ issue-tracker links are *closer to scoped mapping assertions than to either OWL individual equality or SKOS concept interchange*. Default predicate for v1 is **not** `owl:sameAs` and **not** a live `skos:exactMatch` export.

---

## 4. Source-backed design

### 4.1 Qualified identifiers (011 reuse)

011’s assignment record is the atomic fact: identifier value unique within a system/namespace, referent reference, assigner, assignment effective time, optional record/ingestion time, optional validity period, optional use marker, optional evidence. Event time and record time are kept apart. Canonical form is produced only by the scheme’s own rule set; the as-received value is retained; there is no generic cross-scheme normalizer. Reuse, quarantine, reassignment, supersession, split and merge *rules of the scheme* are in 011; the referent itself is not.

RFC 3986 §1.2.2: “The URI itself only provides identification; access to the resource is neither guaranteed nor implied.” §6 comparison is a ladder: character-by-character, syntax-based, *scheme-based*, protocol-based. Scheme and host may be case-insensitive; other components are case-sensitive unless the scheme says otherwise. No universal lowercasing, Unicode folding, or email-as-URI equivalence.

SCIM RFC 7643 §3.1: `id` is service-provider issued, unique across that provider’s resources, stable, **non-reassignable**, `caseExact`, `readOnly`. `externalId` is client-issued, **scoped to the provisioning domain**, uniqueness **not** server-enforced. §4.1.2 `emails` are multi-valued with uniqueness `none`; a service provider SHOULD canonicalize mailbox form per RFC 5321, which is *scheme-specific* hygiene, not a Person key. §9: where multiple tenants can reference related information they should do so via *separate* identifiers so domains cannot perform identifier correlation.

**Profile rule.** Comparison key is `(schemeRef, issuerTenantRef, canonicalValue)`. Raw value alone is never a Person key. Shared mailbox, display name, and Git author string are *features*, not bindings.

### 4.2 Identity assertions (036 profile)

036 owns the assertion envelope: its own identifier and version, issuer/authorship/review, assertion time, effective window, separately recorded observation/ingestion time, tenant/Dimension, purpose, qualified endpoints that it does not own, relation-kind slot bound to an external vocabulary, evidence/confidence, and lifecycle including dispute, supersession, retraction and tombstone. It records conflicts without resolving them.

**Included layers for v1 (proposal, not a claim that 036 is internally partitioned this way in a ratified registry relation):** assertion envelope and identity; endpoint locators, namespace binding, version pins, snapshot-vs-live mode; evidence references and adjudication *records*; contextual validity and conflict pointers; lifecycle states.

**Excluded from the profile even if present in 036:** graph traversal / cluster materialization / redirect projection; command surfaces other than propose / assert / dispute / retract; any entailment stance other than `inference_permitted=false`; OWL `sameAs` export; matcher execution.

**Allowed relation kinds in v1:**

| Code | Meaning | Inference |
|---|---|---|
| `source-scoped-denotation` | This qualified source identifier denotes subject S in Dimension D during a validity window | false |
| `identifier-alias` | Two identifiers of the *same issuer/scheme family* are alternate codes for one assignment | false |
| `historical-identifier` | A previously assigned value denotes S only inside a closed window (rehire / reassignment) | false |
| `not-same` | Explicit denial that two references denote one subject | false |
| `candidate-evidence` | A recorded observation that a string/feature *may* be relevant; not a denotation claim | false |

`probable-entity-match` as a first-class asserted kind is refused in v1: it smuggles the matcher into the assertion store. Matcher output may be *attached as evidence* to a `candidate-evidence` envelope in state `proposed`.

### 4.3 Resolution as a derived contract

Resolution answers: *given this identifier or subject, this Dimension, this policy, this valid-time and this knowledge-time, what is the current authorized picture?*

```
resolve(subjectOrQid, dimensionRef, policyRef, asOfValid, asOfKnowledge)
  → { status, subjectRef?, bindings[], supporting[], contesting[], computedAt, receiptId }
status ∈ { accepted, contested, candidate, unknown }
```

Evaluation sketch (normative intent, not executable code):

- Collect assertions whose Dimension matches, whose authorization_ref is valid as-of `asOfKnowledge`, and whose validity window covers `asOfValid`.
- Drop those whose lifecycle state as-of `asOfKnowledge` is `retracted`, `superseded`, or `tombstoned`.
- If an authorized `not-same` conflicts with a denotation claim under equal authority → `contested`.
- If two authorized denotation claims assign the same qualified id to different subjects under equal authority → `contested`.
- If only `candidate-evidence` / `proposed` claims exist → `candidate`.
- If one consistent set of authorized `asserted` denotation claims remains → `accepted`.
- Otherwise → `unknown`.

A **receipt identity** `digest(policyRef, asOfValid, asOfKnowledge, supporting ∪ contesting)` may be emitted for audit. It is not subject mastership. Persisting the view as an editable golden record is a semantic-negative.

Retraction follows PROV invalidation of the *assertion entity’s effective use*: the assertion remains in the store; current derived views omit it; historical queries with `asOfKnowledge` before the retraction still see it. Endpoints are not rewritten.

### 4.4 Authority, mastership, disclosure

Three authorities, never collapsed:

| Authority | Speaks for | Cannot do |
|---|---|---|
| **Source / scheme authority** | Assignment of a value inside a namespace (011) | Create a Person; grant app access; override another issuer’s assignment |
| **Assertion authority** | The link claim (036 profile) | Mutate endpoints; force equality closure; disclose another Dimension |
| **Policy authority** | Who may propose/assert/retract; how equal-authority conflict is computed | Become a silent survivorship engine |

Cross-Dimension assertions grant **zero disclosure and zero access**. An accepted link is not an authorization decision. 036 already excludes authorization enforcement; 040 explicitly does not implement enterprise IAM.

Mastership of a Person/Agent record stays with the Dimension’s subject model. Mastership of an identifier stays with its scheme/issuer. Mastership of a link stays with the assertion envelope. Resolution has no mastership.

---

## 5. Questions (18)

1. What triple `(scheme, issuer/tenant, value)` is a QualifiedIdentifierBinding, and is string equality ever legal across schemes?
2. Which scheme-specific normalization is authorized, and is the as-received value retained?
3. When may two bindings denote one subject without minting two Persons or merging two existing Persons?
4. What evidence and authorizing role move an IdentityAssertion into `asserted`?
5. How is a *collision* (same lexical value, different issuer/tenant or different subjects in overlapping valid time) distinguished from an *alias* (same subject, different source identifiers)?
6. How is a reused or reassigned identifier temporally partitioned so prior and current subjects do not collapse?
7. How are a mapping assertion, `owl:sameAs`, a reconciliation candidate, a resolver decision, and a destructive merge kept distinct?
8. Who is assertion authority versus source/scheme authority, and what happens when they disagree?
9. How does resolution return `accepted|contested|candidate|unknown` at `(valid-time, knowledge-time)`?
10. How is an erroneous assertion retracted without deleting source evidence or rewriting endpoint identities?
11. Does a cross-Dimension assertion grant disclosure or access? (Required answer: no.)
12. How are shared mailbox, shared display name, and shared Git author string classified?
13. How is idempotent import defined on `structuralKey` plus content digest?
14. How are equal-authority incompatible assertions left contested rather than silently survived?
15. Which 011/036 layers are in the minimum executable profile, and which are non-normative for this enterprise use?
16. May a service-account identifier and a human identifier share an email and remain distinct subjects?
17. What do historical queries return after retraction or after a later `not-same`?
18. Is absent confidence different from `confidence=0`, and is absent evidence different from explicit unknown?

---

## 6. Invariants (12)

**I1 Qualified identity.** Comparison key is `(schemeRef, issuerTenantRef, canonicalValue)`. Cross-scheme string equality is illegal.

**I2 Scheme-local normalization.** Only the cited scheme’s rule set may produce `canonicalValue`. As-received is retained. No universal lowercasing, NFKC, or email identity equivalence.

**I3 Collision ≠ alias.** Same qualified id bound to two referents in overlapping valid time is a collision incident. Distinct qualified ids bound to one subject by authorized assertion are aliases.

**I4 Shared surface strings are evidence.** Mailbox, display name, Git author, and reconciliation score never auto-create a binding.

**I5 Assertion ≠ equality.** No local chaining, no reasoner, no `owl:sameAs` property inheritance, `inference_permitted=false` on every v1 kind.

**I6 Endpoints are immutable by this profile.** Assertion, dispute, and retraction do not allocate, rename, edit, or delete source records.

**I7 Bitemporal correction.** `validFrom/validTo` and `recordedAt` / knowledge-time are independent. Correction is a new envelope version plus invalidation of the prior envelope’s *use*, not an in-place rewrite.

**I8 Retraction preserves history.** Retracted assertions remain queryable as-of their knowledge-time. Source evidence is retained.

**I9 Equal-authority conflict stays contested.** No silent winner, no survivorship.

**I10 No inferred access.** Accepted link ⇏ authorization, disclosure, or cross-Dimension visibility.

**I11 Reassignment is a new window.** Reuse only when the scheme’s reuse policy permits it after quarantine. Prior window remains a historical binding.

**I12 Idempotent import.** Same `structuralKey` and content digest do not mint a second live assertion. Material change issues a new version that `supersedes` the prior.

---

## 7. Competing approaches

| Approach | Attractive because | Reject / accept for v1 |
|---|---|---|
| A. MDM golden-record + survivorship | One working Person | **Reject.** Irreversible endpoint mutation; excluded by 036. |
| B. Store `owl:sameAs` and run a reasoner | Familiar RDF | **Reject.** Global equality; permission and attribute bleed. |
| C. Export `skos:exactMatch` | Documented strength scale | **Defer.** Transitive IR interchange is still too strong for employee numbers; if ever used, `chaining=false`. |
| D. SCIM `externalId` as the only join | Already in IdP feeds | **Reject as sufficient.** No valid-time, no dispute, uniqueness not enforced, tenant-scoped by definition. |
| E. Reconciliation `match=true` as source of truth | Operational and scored | **Reject.** Candidates only. |
| F. Single 036 snapshot as “the resolution” | Fewer objects | **Reject as dishonest** for contested, bitemporal, multi-authority cases. |
| G. New IdentityResolution world-model mixin | Named thing in the catalogue | **Reject.** No new owned semantics. |
| H. Narrow 036 profile + 011 reuse + derived resolution contract | Fits owned/excluded lines | **Accept for v1.** |
| I. Persisted resolution receipt (digest only) | Auditable evaluation | **Optional companion**, marked derived and non-authoritative. |

Tradeoff accepted: operators must query resolution rather than read a merged Person. Tradeoff refused: irreversible merge in exchange for UI simplicity.

---

## 8. Minimum schema, cardinalities, lifecycle

### 8.1 Whole-object facets

Every stored object in the profile carries five facets:

1. **Identity of the object itself** — not derived from endpoints (`assertionId`, scheme registry key + canonical value, `receiptId`).
2. **Classification** — type and, for assertions, `relationKind` + equivalence plane (`identifier` or `record` only; cross-plane rejected).
3. **Temporality** — valid time and knowledge/record time as separate RFC 3339 instants.
4. **Authority / mastership** — who may speak, and what they do not own.
5. **Evidence and disclosure** — cited artefacts, sensitivity, Dimension scope; no implied access.

### 8.2 QualifiedIdentifierBinding (011 restricted field set)

| Field | Card. | Notes |
|---|---|---|
| `schemeRef` | 1 | 011 scheme / namespace token |
| `schemeVersion` | 0..1 | Carried with stored values |
| `issuerTenantRef` | 1 | SCIM-style domain scope |
| `rawValue` | 1 | As received |
| `canonicalValue` | 1 | Scheme rule only |
| `normalizationRuleRef` | 0..1 | Cite the scheme rule, never a global folder |
| `assignerRef` | 0..1 | 011 assigner |
| `useMarker` | 0..1 | official \| usual \| secondary \| temp \| old |
| `validFrom` / `validTo` | 1 / 0..1 | Assignment effective period |
| `recordedAt` | 0..1 | Knowledge time |
| `reusePolicy` | 0..1 | never \| quarantine-then-reassign \| unspecified |
| `exclusiveBindingFlag` | 0..1 | Exclusive-to-one-referent claim of the *scheme*, not a merge |
| `personalDataClass` | 0..1 | 011 privacy carriage |
| `credentialProhibition` | 1 | Default true: identifier ≠ authenticator |

Natural key: `(schemeRef, issuerTenantRef, canonicalValue, validFrom)`.

### 8.3 IdentityAssertion (036 restricted field set)

| Field | Card. | Notes |
|---|---|---|
| `assertionId` | 1 | Never derived from endpoints |
| `envelopeVersion` | 0..1 | |
| `structuralKey` | 0..1 | Idempotent import key |
| `supersedesRef` | 0..1 | Prior envelope |
| `issuerRef` / `authorizerRef` | 1 / 0..1 | Authorizer ≠ issuer when review is required |
| `dimensionRef` | 1 | Adopting company Dimension |
| `purposeCode` | 1 | |
| `sourceBinding` / `targetSubjectRef` | 1 / 1 | Target is a Dimension-local Person/Agent URI, not a second source id unless also qualified |
| `sourceAuthorityRef` / `targetAuthorityRef` | 0..1 / 0..1 | |
| `locatorForm` / `normalizationLevel` | 1 / 0..1 | |
| `referenceMode` | 1 | `snapshot` preferred over live |
| `relationKind` | 1 | Closed v1 set above |
| `negationModifier` | 0..1 | For explicit not-same |
| `plane` | 1 | `identifier` \| `record` |
| `evidenceRefs` | 0..n | |
| `confidence` | 0..1 | Optional; scale named; absent ≠ 0 |
| `assertedAt` / `validFrom` / `validTo` / `recordedAt` | 1 / 1 / 0..1 / 1 | |
| `state` | 1 | see lifecycle |
| `authorizationRef` | 1 | Must be valid to activate |
| `conflictsWith` | 0..n | Recorded, not resolved |
| `inferencePermitted` | 1 | Always false in v1 |

Cardinalities of the *claim*: v1 stores binary envelopes (one source binding, one subject). 1:n denotation is a *set of envelopes*, not a multi-target row that looks like a merge.

### 8.4 ResolutionView (derived)

`receiptId` 1; `dimensionRef` 1; `policyRef` 1; `asOfValid` 1; `asOfKnowledge` 1; `subjectRef` 0..1; `bindings` 0..n; `status` 1; `supporting` 0..n; `contesting` 0..n; `computedAt` 1. No survivorship fields. No access-grant fields.

### 8.5 AuthorityPolicy (independent object, not owned by 011/036)

`policyId`; `dimensionRef`; `whoMayPropose`; `whoMayAssert`; `whoMayRetract`; `equalAuthorityConflictRule=contested`; `crossDimensionDisclosure=none`; `matchingEngine=forbidden`; `owlSameAsExport=forbidden`. 036 does not own this object; referencing it is required so authorization is not smuggled into the identity mixin.

### 8.6 Lifecycle

```
proposed → asserted → disputed
                 ↘ superseded
                 ↘ retracted → tombstoned
disputed → asserted | retracted
```

Permitted transitions only. In-place edit of an asserted envelope is illegal; issue `envelopeVersion+1` with `supersedesRef`. Retraction writes `state=retracted`, `recordedAt=now`, optional PROV-style invalidation activity; it does not `DELETE`. Tombstone keeps the id resolvable as a tombstone.

Authorization: an assertion whose `authorizationRef` is expired, disputed, or absent cannot be `asserted` in the current knowledge-time view.

---

## 9. Semantic-negative cases (12)

1. Lowercasing a Git author mailbox and an HR mailbox, then merging two Persons.
2. Treating SCIM `externalId` equality across tenants as same subject (violates §3.1 domain scope and §9 anti-correlation).
3. Shared mailbox or shared display name collapsing two employees.
4. Reused employee number across subsidiaries without `issuerTenantRef`.
5. Rehire on the same number treated as one continuous assignment with no valid-time split.
6. Exporting accepted assertions as `owl:sameAs` so a reasoner copies Git permissions onto the HR Person.
7. Deleting an assertion row “to fix an error” instead of invalidating its use.
8. Writing a reconciliation `score` / `match=true` into `state=asserted` with no `authorizerRef`.
9. Expired or retracted `authorizationRef` still activating a current-view assertion.
10. Cross-Dimension accepted link granting read of the other Dimension’s Person attributes.
11. Encoding absent evidence as `confidence=0`, or encoding explicit unknown as SQL `NULL` meaning not-same.
12. Conflicting revision of the same assertion edited in place (breaks I7 and I12).

---

## 10. Three synthetic scenario traces

All records below are synthetic. No live tenant was queried.

**S1 — Startup, no ERP.** At t0 three QualifiedIdentifierBindings exist and no Person is minted from them: `HR:acme:E-1042`, `git:github.com/acme:user:42`, `jira:acme:account:88`. At t1 an authorized steward asserts three `source-scoped-denotation` envelopes to `person:urn:dim:startup:p-7` with evidence (offer letter, IdP link). Resolution(now, now) = `accepted` (three supporting, zero contesting). At t2 the Git binding is discovered to have been a reused bot token. The Git assertion is retracted. Current view: HR and Jira remain accepted on `p-7`; Git is absent from the derived view. Query with `asOfKnowledge < t2` still returns the asserted Git envelope. HR, Git, and Jira source rows are untouched. A later intern account sharing the display string “Alex Kim” produces no assertion; Resolution for the intern stays `unknown`.

**S2 — International group.** Subsidiary A assigns `employeeNumber=10021` to Alice 2019–2022. Subsidiary B assigns `employeeNumber=10021` to Bob from 2021. Two bindings, same lexical form, different `issuerTenantRef`, overlapping valid time. Shared mailbox `finance@group.example` and display name “A Smith” are contact points, not subjects — I4. Alice is rehired in A in 2024 on 10021 after quarantine: new assignment window, `historical-identifier` on the first period, new `source-scoped-denotation` on the second; Alice is one Person only because authorized assertions say so. Two equal-authority stewards then assert incompatible denotations of B’s 10021 onto Alice’s Person while Bob still holds it → Resolution = `contested`. A cross-Dimension pointer from Group-HR to Local-B carries `purpose=workforce-reconciliation` and `disclosure=none`; no attributes flow.

**S3 — AI organization.** `person:h-9` and `svc:sa-deploy` share `deploy@ai.example` and sometimes the Git author string `deploy`. A matcher returns score 0.91, `match=true`. That output is stored, if at all, as evidence on a `candidate-evidence` envelope in state `proposed`. Resolution = `candidate`. An intern’s disputed run cannot become `asserted`. An expired bot-token authorization cannot activate the envelope. A reviewer issues `not-same`. Service-account type and human type remain distinct. Retracting the candidate envelope deletes neither Git commits nor the IAM row.

---

## 11. Migration and composition

WM-XCT-040 0.1.1 creates **new** Dimensions only. “An existing Dimension requires a separate migration plan covering backup, loss analysis and data conversion.” It does not implement IAM, does not synthesize permissive runtime schemas, and does not treat Vercy V3 success as validation of nested domain content. Nested snapshots need a closed data schema **and** a companion domain validator. `semantic-only` stores a specification without claiming fact-schema readiness.

**Migration stance for this profile.** First implementation = new `commercial-company` Dimension, semantic-only, pinning 011 `0.3.0-research.1` and 036 `0.3.0-research.1` by version + specification digest under 040. No automatic import of existing MDM golden records as `accepted` assertions. If a later migration exists, each imported link must be re-issued as a 036-profile envelope with explicit `authorizerRef` and evidence; matcher dumps land as `candidate-evidence` / `proposed` only.

Round-trip: export of assertions must carry scheme, issuer scope, raw and canonical values, both times, state, and `supersedesRef`. Re-import uses I12. Resolution views are recomputed, not round-tripped as master data.

---

## 12. Minimum executable profile

What a startup can stand up without ERP:

1. Pin 011 and 036 under 040 as semantic-only.
2. Implement QualifiedIdentifierBinding carriage (fields in §8.2).
3. Implement IdentityAssertion propose / assert / dispute / retract (fields in §8.3, kinds in §4.2).
4. Implement `resolve(...)` as a pure function of stored assertions + one AuthorityPolicy (§4.3, §8.4–8.5).
5. Refuse `owl:sameAs` export, matcher-to-asserted promotion, cross-Dimension disclosure, and endpoint edits in the same transaction as an assertion.

That is enough for S1. S2 additionally requires `issuerTenantRef` and contested status. S3 additionally requires a service-account type distinct from Person and `candidate-evidence` as a non-denoting kind.

---

## 13. Proposed publication form and holds

**Publication form.** An enterprise *profile note* of WM-XCT-036 that mixes WM-XCT-011 by reference. Composed under WM-XCT-040 exact pins for a new commercial-company Dimension. Semantic-only until a companion validator exists. Do not create a new world-model entry “EM-XCT-01” as owned semantics.

**Holds that remain open (inspected, not closed by this review):**

- 011 source-verification and deferred identifier-family completeness; `publishableCanonical: false`.
- 036 Claude-only owner waiver; live re-verification of 108 URLs; empty relationship contract; `boundary-review-required`; parent link to 011 not independently ratified in the registry. This review does not wash that history.
- 040: no migration path; no companion identity validator delivered here; V3 ≠ domain-valid links.
- Policy object is required but not owned by 011 or 036 — risk of smuggling authorization into identity.
- “Canonical subject URI” in any implementation plan is a golden-record attractor; `subjectRef` must stay Dimension-local.

---

## 14. Principal design objections

1. **A single-assertion snapshot is not a resolution.** Contested equal-authority links, bitemporal retraction, and candidate-only matcher output are multi-assertion phenomena. Storing `resolution_status` on the assertion as master data will be treated as a merge.

2. **A stored ResolutionView with mastership is the same bug in a nicer suit.** A receipt digest is acceptable; an editable golden aggregate is not.

3. **Profiling 036 without an inclusion list will pull 65 layers.** Implementers will import graph traversal, redirect projection, and `sameAs` export. The profile must name included layers and set `inference_permitted=false`.

4. **011 already owns binding.** Inventing a parallel IdentifierBinding type guarantees drift on normalization and reuse.

5. **`owl:sameAs` is an anti-pattern here, not an optional pretty export.** OWL individual equality copies all properties; SKOS itself warns against this strength even for concepts. Employee numbers and Git accounts are weaker still.

6. **Email and `externalId` look like keys and are not.** SCIM says so in normative language. Any profile that “just lowercases email” has left 011 and RFC 3986.

7. **Retraction modelled as DELETE, or as destruction of the Person, misuses PROV.** Invalidation ends availability of the *assertion’s use*. Source evidence and endpoint identities remain.

8. **This study is bounded.** It does not verify 036’s 108 sources, does not close 011 holds, did not run tests, and cannot compose the profile into an existing Dimension under 040.

Those objections are why the first implementation is a profile-plus-derived-view, not a new model and not a merge engine.