# EM-XCT-05 — candidate semantic contract and release assignment

This Codex design accompanies the R3 research direction. It is not part of the R1/R2/R3 code-audit corpus unless explicitly listed in a later freeze. It is not a published metamodel. The two completed research studies and their disagreements are preserved separately. The current code README governs prototype-specific details including complete snapshot validation, matching as-of time, self-objections under segregation and immediate-only active supersession checks.

## Independent types and containment

**ContextPackageProposal** is an immutable revision of a proposed collection of source-object projections. Its qualified record ID denotes the proposal across corrections; revision and content digest identify one exact statement. It has one Dimension, one author/capture time, one audience, purpose, environment, known-prior-release context and custody context, and 1–32 embedded members. Each member has a locally unique key, one source-object pin, one schema pin, one shape pin and 1–64 fields. A field is an embedded metadata value with an exact scalar-name declaration, kind and 1–8 classification-binding pins. Members and fields have no independent exported lifecycle.

**JointDisclosureReview** is an independently identified immutable assessment revision of exactly one proposal revision/digest. It has one reviewer, authority pin, method pin, 1–16 evidence pins, assessment time, a finite half-open validity interval, one verdict and a residual-risk statement. Optional supersession names another review of the same proposal identity. Multiple reviews can coexist; their disagreement is visible. The review neither owns the source objects nor calculates a new business report.

All record properties are required by the prototype schema; `supersedes` is explicitly nullable. Empty classification/evidence sets are invalid, not public/clear defaults. No structured source-value payload is supported; free-text risk notes and identifiers may still contain sensitive facts and need explicit governance. `number` is a description of an external field kind, not numeric payload support. The byte bound may constrain cardinalities before their individual maxima.

## Whole-object coverage

| Type | Canonical facet | Status | Concrete coverage / reason |
|---|---|---|---|
| ContextPackageProposal | identity-class | required | Format/version, Dimension, qualified proposal ID, opaque revision, content digest; one collection, independent from its members' object identities. |
| ContextPackageProposal | direct-properties | required | Finite exact member/field set and all audience/purpose/environment/context pins; schema supplies type, cardinality and nullability. |
| ContextPackageProposal | recognition-observation | required | Author and capture time state who recorded which exact source revision/context. Host identity resolution and truth remain external, with no unpinned delegated-type claim. |
| ContextPackageProposal | capabilities-behaviour-actions | required | Seal, validate, import immutable revisions, inspect applicability against a trusted snapshot; these operations do not grant access or deliver values. |
| ContextPackageProposal | context-evidence | required | Exact source/schema/shape/classification/prior-release/custody pins. The host resolves them independently. |
| JointDisclosureReview | identity-class | required | Independent review ID/revision/digest and exact proposal reference; reviewer and assessed object are distinct roles. |
| JointDisclosureReview | direct-properties | required | Verdict, risk statement, assessment/validity times and optional supersession pin. |
| JointDisclosureReview | recognition-observation | required | Method/evidence pins and assessed proposal establish the declared observation context; no calibrated confidence or inference-prevention proof. |
| JointDisclosureReview | capabilities-behaviour-actions | required | Record a verdict, correct through another immutable revision, validate internal references, count or exclude it under current host state; no authorizing or deleting action. |
| JointDisclosureReview | context-evidence | required | Reviewer/authority/method/evidence pins, relation to proposal and previous review, current authority and completeness supplied by host snapshot. |

No facet is blanket-delegated to an unavailable model. Physical dimensions are not relevant direct properties of these information records. Byte storage size is an implementation bound, not the object's physical ontology.

## Mastership, rights and time

| Fact group / relation | Semantic owner and authoritative system | Writer | Reader / purpose | Time and provenance | Conflict / retention |
|---|---|---|---|---|---|
| Source identity, revision and fields | Domain owner / its actual source master; no HR/ERP assumed | Domain-authorized writer | Only authorized proposal preparers | Exact opaque source/schema/shape pins and capture time | Source conflict remains unresolved by this companion; source custodian controls retention. |
| Classification binding | Designated classification authority / binding register | Authorized classifier, outside this module | Restricted preparer/reviewer scope | Exact binding record pin; source authority owns scheme, term and validity | No inferred downgrade or scheme ordering; binding itself may be sensitive. |
| Proposal revision | Company Dimension's proposal register | Host-authorized proposer | Internal reviewers for a declared purpose | Immutable author/capture/context; revision tokens are unordered | Same ID/revision with different content rejected; current pin selected by host. |
| Review verdict and evidence | Review owner / review register | Authorized attributed reviewer | Authorized review consumers, never automatically the external recipient | Assessment time and half-open validity distinct from source/capture time | Disagreeing applicable verdicts produce conflict; all evidence retained subject to actual custody rules. |
| Current authority / active set | Host governance register | Authorized governance operator | Internal applicability checker | Current snapshot digest and evaluation time bound in report | Snapshot completeness, withdrawal and actor identity are host assertions; stale/contradictory snapshots must not be silently repaired. |
| Supersession | Review register | Reviewer/owner authorized to correct a review | Authorized historical readers | Exact existing target, same proposal identity, nondecreasing assessment times | Local immutable import verifies link/digest/type/cycle constraints. Host explicitly selects active revisions. |
| Custody / previous releases | Named record custodians and disclosure history owners | Custodian and release recorder | Need-to-know reviewers | Exact current opaque context pins; distinct custodians may have distinct schedules | Equality is not a retention/disclosure/destruction decision. No blanket perpetual evidence-retention rule. |

The prototype's dictionaries are host assertions, not credentials. Admission needs both inspect and record assertions, plus external object-specific writer authorization. Current inspection requires host permission before record diagnostics. Production handling of denied versus missing, timing, caching and recipient copies remains outside the module.

## Lifecycle and corrections

The prototype stores immutable revisions and treats applicability as a derived answer. It does not overwrite a persisted record's historical verdict on expiry, withdrawal or context change. A proposal revision is created, can receive reviews, and can cease to be the host's current pin. A review is recorded as cleared/rejected/inconclusive; it may be withdrawn or superseded through separately governed current state. Every verdict has a finite window; expired negative verdicts are explicitly reported as ignored and do not count in the first profile. A persistent-objection profile would need a separately reviewed contract.

Pure merge is transactional and idempotent over a complete bounded local register. Durable compare-and-swap, root selection, authentication, current governance snapshot construction, actual pin resolution and disposal remain host responsibilities. Version 0.0.0-prototype.1 is preserved under its original validator; R2 refuses mixed-version reinterpretation. No automatic upgrade/downgrade exists.

## Sixteen candidate invariants

1. Each embedded member names exactly one source object; package membership can span objects but a projection cannot silently do so.
2. Qualified ID, record revision, source/schema revision, lifecycle/applicability and digest remain distinct.
3. All local reference occurrences of an ID agree on revision/digest; the prototype cannot carry two purported current versions of that ID in one record.
4. No undeclared source value or nested/wildcard field is accepted by the metadata-only grammar.
5. A missing classification binding or evidence set cannot become an empty/public/clear default.
6. A review pins exactly the proposal identity/revision/digest; membership, shape, audience or any bound context change invalidates that match.
7. A current snapshot pins the proposal itself and independently declares all current member/context values.
8. The complete supplied review set equals the active pin set; duplicate or competing active revisions are invalid.
9. Active and withdrawn sets are disjoint; an active successor cannot leave its superseded target active.
10. Review assessment does not predate proposal capture; applicability uses `[validFrom, validTo)` and future capture is stale.
11. Current author/reviewer catalogs and authority pin are applied; segregation is explicit and actor-alias identity remains a host duty.
12. Conflicting eligible verdicts cannot silently select a winner. Excluded verdicts retain their pin, result and reason in restricted diagnostics.
13. Every returned report identifies its proposal, snapshot digest, evaluation time and counted/ignored records, and explicitly conveys no serving authorization.
14. Same stored identity/revision cannot be repointed; repeat import is idempotent and a failed merge leaves the caller's store unchanged.
15. Local review/proposal and supersession links resolve by exact pin/type, preserve proposal identity and nondecreasing assessment time, and do not cycle.
16. Pin equality, a human clearance and any custody-context reference establish no source truth, inference guarantee, current grant, legal conclusion, completed delivery or destruction.

Invariants 1–15 combine local checks with clearly named host attestations; invariant 16 is a semantic boundary and is not a proof produced by unit tests. The 24 draft question routes remain in `implementation-assignment.md` and must be normalized into the final Bundle/Layer/Finding tree against this two-type design. Their earlier five-object candidate table is superseded by `reconciliation.md`.

## Release work still required

Read both R2 audits, reconcile and remediate blockers; generate the final semantic tree and stable package identity/version; build representative native V3 binding with separate nested semantic validation; run three full synthetic Company Dimension acceptance scenarios; audit the exact final package; publish through the canonical pipeline and verify HTTP, runtime/search/resolve and exact bytes. Neither a source-study consensus nor prototype acceptance substitutes for those checks.
