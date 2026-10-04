# Enterprise identity-assertion profile 0.1.0

## Boundary and canonical ownership

This is a narrower usage and representation profile of WM-XCT-036, not a new subject model. Identifier assignment meaning is reused from WM-XCT-011. A source binding is a frozen carrier value in an assertion, whose source authority remains external. An assertion is its own identified claim. The resolution result is a derived, disposable query artifact; it has no subject mastership. The externally supplied policy is a reference-test binding of local governance, not a new policy model owned by identity.

Included WM-XCT-036 concerns: assertion envelope, endpoint reference boundary, relation classification, contextual validity, evidence, immutable transition history, and a scoped read contract. Matching engines, graph closure, redirects, global equality, cluster mastership, disclosure engines and endpoint mutations remain excluded. The exact included source finding/layer IDs are recorded in `crosswalk.json`.

The profile admits `equivalent-in-context`, `not-same-assertion` and `probable-entity-match`, using the existing relation register. All have `inferencePermitted=false`; the third can never enter asserted state. The existing definition of equivalent-in-context limits its claim to a named context; here that context is the adopting Dimension, declared purpose, referent kind and interval. It does not mean account ownership, loose resemblance or global OWL equality. We deliberately retain existing codes instead of adopting Grok's proposed new names. Scores, names and email matches cannot activate a claim on their own.

## Types, identities and relationships

| Type | Identity and role | Cardinality and ownership |
|---|---|---|
| QualifiedIdentifierAssignment | Source-issued `assignmentId`, exact `scheme`, `schemeVersion`, `issuer`, `scope`, `value`; occurrence validity and source record | One frozen assignment carrier per assertion. Issuer owns the assignment; importer cannot reinterpret it. Simultaneously reserved asserted observations of an issuer-qualified assignment must agree. Proposals cannot reserve an occurrence; retraction releases the reservation while retaining evidence. Full source-observation revision remains deferred. |
| IdentityAssertion | Local issuer-qualified `id`, Dimension, purpose, predicate, fixed source and target, fixed validity | One source and one target. A subject can have many independent assertions. Zero or many assertions may concern one qualified ID. Conflicting claims are data to preserve. |
| AssertionRevisionEvent | Distinct `id`, genesis claim digest / previous event digest, effective time, recorded time, actor, state, reason and evidence | Ordered one-to-many owned history. Event IDs are unique across the provided set. Source evidence is referenced, not copied as private content. |
| EvidenceReference | Source-qualified URI plus kind and description | One or more per event. Activation requires source-record and review-decision categories; authenticity is a caller responsibility. |
| ReferenceAuthorityPolicy | Independently supplied URI/version and digest, Dimension, purpose, namespace, issuer list, actor permissions, readers and interval | One frozen policy for the bounded input set. The Dimension policy owner supplies it. It is not self-issued by an assertion. |
| ResolutionView | Canonical input digest, policy digest and two temporal coordinates | Computed on demand over one supplied set. Returns supporting/opposing/candidate/disputed IDs. No editable canonical subject or aggregate is created. |

The executable contract is `identity-profile.schema.json`; `assertion.schema.json`, `binding.schema.json`, `policy.schema.json` and `query.schema.json` are generated companion views. Field-level types, requiredness and cardinalities derive from that combined contract. `field-catalog.json` maps their carrier fields to ownership, sensitivity and the governing contract. All object schemas are closed. Optional open end is `null`; missing required context is rejected, not guessed. No numeric confidence is encoded, so absence cannot be confused with zero.

## Lifecycle, temporal queries and correction

An assertion begins proposed. Proposed can become asserted, disputed or retracted. Asserted can become disputed or retracted. Disputed can become asserted or retracted. Retracted is terminal. These are recorded issuer declarations; a derived view separately evaluates eligibility and conflict.

Each event must be authorized by the supplied frozen policy at its recording time. Recording times increase strictly. Effective times may be retroactive but cannot precede the assertion's start or exceed their recording time; they must also precede an exclusive claim end. At `(validAt, knownAt)`, select the latest recorded event known then whose effective time has arrived. Both assertion and assignment intervals are half-open. A later correction can change a current view. Earlier knowledge answers are preserved only for a retained set extended through the trusted live-import path described in README.md; standalone snapshot validation cannot guarantee reception history. The report's digest may change when the supplied set grows even though the historical substantive answer stays the same.

A changed endpoint, purpose, predicate or validity window is a new assertion ID, after explicit retraction of the old claim when appropriate. Append-only history is enforced relative to the caller's existing input by `import_assertion`; the reference cannot prove that an arbitrary standalone input has not been falsified or truncated. Live imports require new events stamped with the trusted receipt time after the global input head; retrospective snapshot restoration is outside this API. Concurrent persistence, event authentication and historical-policy recovery are separate integration duties.

## Invariants

1. Compare exact qualified keys only; issuer and tenant scope are never inferred.
2. Preserve scheme version, raw value and assignment occurrence. This profile has no normalization transform.
3. The assignment's declared referent kind must equal the target kind. Both declarations must match a trusted scheme-kind register and the target kind namespace. This checks declared semantics, not the real source system.
4. The target must be in the policy's local subject namespace; no positive identifier-to-identifier chains are traversed.
5. Fixed assertion content cannot change under the same assertion ID; previous event digests and historical prefixes remain intact.
6. Candidate relations never activate. Activation requires both source evidence and reviewer evidence as declared categories.
7. Policy digest, Dimension, purpose, permitted issuer, actor/state grant and recording-time validity must agree.
8. Read purpose and actor must be allowed by the same frozen policy that pins all claims; independent read-policy rotation is not supported. Historical knowledge cannot exceed evaluation time.
9. Validity cannot exceed the assignment interval. Unknown starts and invalid/reversed windows are refused.
10. Multiple active target IDs, active opposition against a positive target, or a dispute of a previously asserted claim produce contested status. Unasserted candidate disputes cannot veto acceptance. Authority ranking is deliberately absent.
11. Reviewed negative-only input produces denied-in-input; proposed negatives produce proposal-only. Inert positive candidates produce candidate; no applicable claim produces unknown.
12. Replaying an identical assertion is a no-op; divergent content or history truncation is refused. The acceptance harness compares the actual stored JSON snapshots with the source fixtures; arbitrary external converters are not certified.
13. The resolver does not grant access, export equality, mutate endpoints or assert global completeness.
14. A V3-valid outer fact can contain a semantically invalid snapshot; companion validation is mandatory.

## Questions and artifact routes

| Question | Inspect / produce | Permitted next action |
|---|---|---|
| What does this source ID actually denote? | Binding kind and source record | Request source evidence; do not infer Person from Account |
| Who owns its namespace? | Scheme, issuer, scope | Compare only within the qualified key |
| Which scheme version governs comparison? | Version and exact-string declaration | Refuse unsupported normalization |
| Is this a new assignment occurrence? | Assignment ID and validity | Preserve prior occurrence and inspect source history |
| What local subject does the claim concern? | Target ID and kind | Verify namespace and reference externally |
| Who may assert this link? | Policy digest and event actor grant | Validate declared grant, then authenticate externally |
| What evidence supports activation? | Source-record and review-decision references | Keep name/email-only material proposed |
| Is the claim only a candidate? | Relation and history | Never auto-activate a score |
| What was effective at a date? | Valid time and event effective time | Produce a scoped temporal view |
| What was known at that date? | Recorded times and knownAt | Preserve earlier substantive answers |
| Is another claim incompatible? | Complete caller-selected input set | Return contested; do not choose a winner |
| Is there explicit opposition? | Negative assertions and opposing IDs | Retain negative knowledge distinctly |
| How is a mistake corrected? | Retraction plus successor assertion | Use append-only import; leave endpoints intact |
| Can this link disclose another Dimension? | Namespace and external access policy | Deny implicit disclosure |
| Is a replay identical? | Assertion identity, digest and history prefix | No-op or explicit conflict |
| What is missing for a real merge? | Separate migration/transaction plan | Defer endpoint merge and split |
| What survives a round-trip? | Complete closed envelope | Refuse field-dropping conversions |
| Is this globally unique or authenticated? | Scope and caller trust assumptions | Answer insufficient-context; do not claim proof |

Every answer is conditional on available authoritative context. If evidence or permission is missing, request the relevant artifact or return a refusal/unknown; do not synthesize facts.

## Adoption and migration

Start with the synthetic fixtures. A real deployment needs source-specific mapping, source-issued assignment identities, authenticated policy/evidence, retention and access controls, storage concurrency and an independently selected complete input set. The reference does not allocate those responsibilities to Git, HRIS or an ERP merely by naming them.

Legacy matcher scores or denormalized identity columns enter review as proposals. Do not import an existing merge as accepted truth. A changed profile version requires explicit semantic comparison; unknown versions are refused. No automated downgrade or in-place Dimension migration is supplied. WM-XCT-040's exact new-Dimension composition route is used only with explicit pins and separate semantic/native readiness.

## Binding interpretation and excluded parent obligations

The lookup token denotes `binding.sourceReferentRef`; the contextual relationship is between that source referent and `target.id`, never token-to-Person equality. `endpointResolution` records externally checked resolution declarations; asserted claims require both resolved. The policy scheme register is a profile restriction, not a complete WM-XCT-011 scheme definition. Source-specific granularity, exclusivity, full assignment revision, qualifier vocabularies and WM-XCT-036 kind-change lineage remain deferred. The crosswalk is a narrower/overlap usage mapping, **not full conformance** to every required field in those parent findings. No new registry edge or final mixin/relationship classification is ratified by this release.

## Final audit clarifications

`evaluation_at` is the caller-supplied trusted current clock, not an arbitrary simulated future knowledge boundary. The function enforces `known_at <= evaluation_at`; the caller authenticates the clock. Static validation and the CLI do not enforce live reception history. At second precision, live imports are globally serialized to one new transition per second in the retained input set. An inverse subject index is not supplied.

Assignment observation reservations are scoped to claims that reached asserted and are not retracted. Unasserted proposals cannot permanently squat a source occurrence. Retraction releases that reservation without erasing the old observation; `retainedObservationConflicts` reports conflicting carried content across the full input, including proposals/retractions. Source truth is still external. A dispute uses only prior events effective at the queried valid time. A disputed previously asserted negative can produce contested even without a positive claim.

Integrity checks pin trusted local **source bytes**, not a hardened execution sandbox: Python import paths/bytecode and changes after verification remain part of the trusted environment. Loader parse/decode exceptions fail closed but are not all normalized to Invalid. Runtime schema integrity must be protected after installation. Source-referent namespaces, issuer qualification of assertion IDs, URI alias identity and complete parent endpoint admissibility remain external governance, not proven by string comparison.
