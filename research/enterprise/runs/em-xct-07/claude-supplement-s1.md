EM-XCT-07: Supplement S1 amendment (Claude)

This amendment leaves the original study in place and changes it only where this document says so. It is research, not an approval to implement.

0. Evidence I checked myself for S1

I downloaded every pinned source.

SHA-256 prefixes that match the supplement exactly:

Source	SHA-256 prefix	Size
WM-XCT-001 spec.yaml (version 0.3.1-enterprise.1)	fa942556a3f46072…	305,345 bytes
fact-authority spec.json	cf027b56d01f23e3…	19,364 bytes
K1	e93a14c18a08f1a0…	—
K2	b262d62aaf41bec6…	—

What I found inside WM-XCT-001:

The delegated-authority layer has two findings.
delegation-mandate-scope has these elements: de-delegated-power, de-mandate-constraint, de-attribution-mode and de-subdelegation-depth. Mandate IRIs are minted by the issuing control record's namespace.
mandate-verification-revocation has de-mandate-status, de-revocation-effective-at, de-revocation-published-at and de-reliance-rule.
The boundary excludes runtime authorization evaluation and enforcement.

Architecture drafts. The supplement gives no hashes for these, so I record the ones I got:

Draft	SHA-256 prefix
MMAS-Core	bc7428da…
MMAS-Interchange	28d673eb…
Contract	a9c8c059…
Event	25217f98…

Event.md says Events are immutable and that corrections are new Events referencing the corrected one. Contract.md lists delegation and capability agreements among the forms it contemplates.

What I did not verify:

I did not run authority.py.
I did not see the D1 experiment or the SQLite prototype. I rely on the supplement's description of them.
I did not read all legal domains of WM-XCT-001.
1. Corrections to my original study
Using keySlotId as an Event subject is invalid. The native validator resolves subjectIds only against retained object IDs or record IDs, so a derived hash is not a known subject. I withdraw the slot-subject design.
The Contract-profile DelegatedExecutionGrant is withdrawn from the first increment. WM-XCT-001 already owns a scoped, revocable DelegationMandate. A second master would duplicate it.
My guarantee that "a provenance.requestId scan gives at most one revision" is withdrawn. A property is not a uniqueness constraint. Several file writes under one lock are also not atomic.
The unknown / reconciled states are removed from the local lifecycle. In a single-store transaction the authoritative store has either committed or rolled back. Only the caller can be uncertain. General external reconciliation is deferred rather than simulated.
The "epoch retirement proves purge safety" rule is weakened. An epoch list that lives in the same store proves nothing after that store is restored from an older snapshot. See §6.
2. Decision 1: smallest boundary and dispositions
Concern	Disposition	Independent identity?
Versioned operation definition	NEW sibling object OperationDefinition, with an optional pinned crosswalk actClassRef 0..1 to K2	Yes. Requests must pin an immutable version with parameters, preconditions, effect boundary, adapter binding and retirement.
K2 actClass	EXTERNAL crosswalk only, not a profile	No. K2 is an unresearched seed whose conformance labels and wildcard imports are unvalidated. Refining it would import unresolved semantics. An actClass is also a verb taxonomy, not an executable contract with parameters or retirement.
K1 function	Not used. At most a descriptive note.	No. A function is a purpose an agent can fulfil, not an operation.
Accepted request	NEW object ActionRequest, immutable, exactly one revision	Yes. See §3.
Submission, commit, cancel, expiry, precondition rejection, correction	Event profiles on native events	Each has its eventId only.
Effect receipt	Event profile em-xct-07.effect.committed.v1	Its eventId. It references a real resource record ID.
Standing delegation basis	EXTERNAL reference to a host-owned, versioned WM-XCT-001 DelegationMandate record	Owned there, not here.
Fresh action-scoped decision	Embedded in the commit event (decisionRef, policySetVersion, evaluatedAt) plus a host-private decision log	No separate master.
Source WriteGrant, StewardshipAssignment, MastershipRule	Explicitly not accepted as execution authority	—
Disclosure decision	Host function, not recorded as a public Event	—
maxUses counter	DEFER	—

Justification for the WM-XCT-001 choice (a design choice, grounded in the sources above):

A mandate conveys standing: who may exercise which powers, with which constraints, to what depth, until revocation.
That standing is necessary for execution but not sufficient. The executor's host still makes a fresh decision per execution try.
WriteGrant is excluded because it authorizes admitting observations for a scope and predicate, not performing effects. Widening it would silently turn fact admission into execution permission.

Counterexample. WM-XCT-001 mandates are about control powers over objects. They may have no field for executor audience or purpose.

Response. Audience and purpose must be expressible inside de-mandate-constraint. Where they cannot be expressed, the fixture fails closed and the request is denied. EM-XCT-07 must never extend the mandate locally. If real mandates routinely cannot carry audience, that is a WM-XCT-001 change request, not grounds for a new EM-XCT-07 master.

3. Decision 2: one native binding

Chosen binding: request object plus events. I decide this by semantic identity. A request has intent identity before any execution event exists: it can be pending, retried, cancelled or expired. Every later event is about that intent. An acceptance-event anchor would force the submission event to be both an occurrence and the durable subject of a multi-event history. The request object is the honest subject.

The request object

Its type is em-xct-07.action-request.
The host mints its objectId at submission.
It has exactly one revision and no previousRecordId ever. Any second revision fails validation.
Its generic object "state" is never read as execution state. The execution lifecycle is derived only from events.

Immutable content

definitionRecordId (the exact pinned version).
Dimension, tenant and executor audience.
resourceObjectId and expectedResourceRecordId.
actingIdentityId and principalId.
mandateRecordId (0..1) and purposeCode.
The ordered payload.
deadline.
keyScope and retryKey.
requestDigest, computed with the RFC 8785 byte contract and restrictions from my original study.
compensatesReceiptEventId (0..1).

Events. Every lifecycle event has subjectIds = [requestObjectId]. The commit event also adds the real resource record ID it produced. The Event actorId is the issuer, meaning the host executor that recorded the event. The intended actor lives only in the request content. actorId is never evidence of authority.

Retries

Uniqueness of the tuple (keyScope, retryKey) is enforced by an actual unique constraint in the authoritative store.
The same key with the same digest resolves to the existing request. No new object is created.
The same key with a different digest is a conflict. Nothing is written.

Correction

Content errors in a request cannot be corrected. The fix is to cancel, if still pending, and resubmit with a new key.
Observation errors are corrected by a correction Event that references the event being corrected, following Event.md. The effect itself is never undone.

Mastership (a design choice). In the first increment the authoritative execution store is a single local transactional database (SQLite, in the style of the prototype). It holds the synthetic resource state, the request rows, the unique key constraint and the receipts.

The native runtime objects and events are an emitted evidence export:

They are written after commit and are idempotent by eventId and recordId.
They are validated by the package's own nested and whole-history validator.
A failed export never changes execution truth. It is retried from the store.

I am choosing this over a file-runtime master because a correct file-based commit would need a journal, fsync ordering and recovery that nobody has designed yet. That work is deferred.

Admission and archive limits

Native admission validates envelopes only.
Archiving request bodies must keep the key row (scope hash, digest, terminal state) in the authoritative store for as long as keys can be presented.

Counterexample. Export lag means the native Dimension can show a pending request that is actually committed.

Response. The native view is labeled as evidence with an exportedAt time. Execution queries go to the authoritative store. Whether Vercy accepts a non-native execution master is itself an open governance question (see §6).

4. Decision 3: minimal direct-delegation fixture contract

The host supplies three records. None is created by EM-XCT-07.

Principal scope. A set of exact tuples, each with a validity interval. A tuple is (Dimension, resource objectId, definition recordId, purpose, executor audience). The principal's authority basis comes from a host-owned WM-XCT-001 control or title record, referenced by record ID.
Delegate scope. A WM-XCT-001 mandate referenced by record ID. The same tuples are expressed through de-delegated-power and de-mandate-constraint. It has de-subdelegation-depth = 0 and an de-attribution-mode that attributes acts to the delegate on behalf of the principal, never as the principal.
Issuer standing verification. A host verification record, not a boolean. It carries the verifier, verifiedAt, the mandate record ID, the observed status and the revocation-published-at value it saw.

Fixture rule, evaluated inside the commit transaction at host time t. Permit only if all of the following hold:

The request's exact tuple is in the principal scope and in the delegate scope.
t falls within both intervals and t ≤ deadline.
The mandate status is active.
The revocation-effective-at value is absent or later than t.
The verification record is no older than the definition's freshness bound.
The acting identity is the mandate's assignee, and the principal is not the acting identity.

The rule never uses wildcards, never takes a union, has no chain input, and has no impersonation mode. Any request carrying a nested actor or a sub-mandate is denied.

First-package decision. No standing-grant profile ships. The external mandate reference is adequate, because the fixture needs only exact record binding plus the host verification record.

Residual limit. The fixture proves only containment logic over host-asserted records. It verifies no credential and establishes no legal validity.

5. Decision 4: denial, deadline, cancellation, disclosure and terminology

Terminology

Delivery. A transport arrival of a submission or retry message. It may be duplicated or reordered.
Execution try. One transaction that evaluates a pending request: authority, deadline, precondition and cancel status. It ends in commit or in rollback with no effect.
Effect. The committed mutation together with its receipt event.

Delivery and execution try each have no stored identity. Only the request and the receipt do.

Lifecycle. Pending moves to exactly one of: committed, cancelled, expired or rejected-precondition.

Choice: denial is retryable. A denied execution try leaves the request pending. Each delivery before the deadline gets a fresh check. This covers the realistic case where a founder or approver grants permission after submission. The deadline bounds the exposure.

I rejected terminal denial because it pushes callers to mint a new key after a transient denial. That multiplies requests and makes the same logical intent span several keys.

Counterexample. Retryable denial lets a caller probe for policy changes. The host must rate-limit execution tries per request. Terminal denial should remain a per-definition option for high-risk operations.

Deadline

The deadline is checked with the host clock inside the transaction, so no commit can occur after it.
A replay after the deadline returns the expired state (subject to disclosure). It never runs a fresh check that could commit.
Expiry is recorded lazily, by the first execution try or a sweeper after the deadline. Either way it is idempotent: one expired event.

Cancellation race

Cancel and execute are serialized in the same store. Whichever commits first wins.
A cancel after commit is refused as "already committed". Reversing the effect then needs a compensation request.
A cancel on a pending request records a cancelled event, and no later try can commit.

Disclosure

Every status or result view needs a fresh read check at render time.
For a caller whose status-read check fails, the states absent, existing (any state), conflicting and retired produce byte-identical responses: the same status code, the same body shape and no identifier.
I withdraw my earlier "duplicate; not disclosable" response, because it leaks existence.

Strongest counterexample: the retry-safety versus disclosure trade-off.

A submitter who still holds execute authority but has lost read authority cannot learn that their request committed.
They may then submit a new key and produce a second effect.

Mitigation, which is a host policy requirement and not something this package can guarantee:

The acting identity of a request should hold minimal status-read on it (state and requestId only, never a result body) for as long as it could still execute.
Any host that separates the two rights accepts duplicate-effect risk explicitly.

Compensation

A compensation is a new authorized request with a new key and compensatesReceiptEventId.
For the label example: its payload is the receipt's before-value, and its expectedResourceRecordId must equal the receipt's after-revision.
Any intervening update causes rejected-precondition. Reversal is therefore conditional, never guaranteed.
6. Decision 5: facets, indispensable tests, publication blockers

Facets. These are the selected types, using the protocol's exact facet keys.

OperationDefinition

identity-class: A new sibling object. objectId is stable and recordId identifies a version. It is not a permission.
direct-properties: Parameter schema (ordered arrays, integer-only numbers), target type, precondition kind (exact expected revision), effect boundary (local-synthetic.label-set only), adapter binding, compensation pairing, deadline ceiling, freshness bound, retirement status, and actClassRef 0..1.
recognition-observation: A request is recognized as an instance of an OperationDefinition only by an exact definitionRecordId match. Name or text matching never counts.
capabilities-behaviour-actions: It is validated by the package. Once retired, pending requests are refused at their next execution try.
context-evidence: Steward and registry master, with a digest over the normative fields.

ActionRequest

identity-class: A new object holding immutable intent. It has one revision and a host-minted ID.
direct-properties: The bound content in §3.
recognition-observation: Deduplication uses the unique constraint on (keyScope, retryKey) plus a digest comparison.
capabilities-behaviour-actions: It can be submitted, retried, cancelled, expired, committed or rejected on precondition, and its state is derived from events only.
context-evidence: The mandate reference, principal basis reference, host decisions and export timestamps.

Effect receipt

identity-class: An Event profile, identified by its eventId.
direct-properties: requestObjectId, before-value, after-value, beforeRecordId, afterRecordId, decisionRef, policySetVersion and evaluatedAt.
recognition-observation: It has exactly one row in the authoritative store, keyed uniquely by request.
capabilities-behaviour-actions: It can be referenced by compensation and corrected by later Events. It is never edited.
context-evidence: The issuer is the host executor. The intended actor comes from the request, and it carries a real resource record ID.

Indispensable tests (all proposed; none is implemented by me)

Same key and digest produce one effect under concurrent deliveries.
Same key with a changed digest is a conflict that writes nothing.
Payload array reordering changes the digest.
Wrong Dimension, tenant or audience is refused before a row exists.
Mandate revoked with effective time ≤ t is denied, and the request stays pending.
A commit attempt after the deadline yields expired and never commits.
A stale expected revision yields rejected-precondition.
A cancel/commit race produces exactly one terminal state.
A retry after commit discloses nothing without a fresh read check, and the absent, existing, conflicting and retired responses are byte-identical.
An agent that saw "Publish" in a document, with no current permission, leaves its request pending until expiry and produces no effect.
Compensation succeeds only when the current revision equals the receipt's after-revision.
A correction event appends history and leaves resource state unchanged.
A chain, impersonation or wildcard input is denied.
A fault injected between commit and export: re-export converges and duplicates are rejected by ID.
The native validator admits the exported events with real subjects, and the package validator rejects forged histories (gaps, second request revisions, receipts without a prior pending state).

Only prototype-derived behaviour (serialized policy, deduplication, receipt, and precondition-before-duplicate ordering) has been demonstrated by others. Every one of the cases above is a proposal until delivered code and results exist.

Reasons the small increment still cannot be published, even after genuine frozen audits

Continuity. A store restored to an older, internally valid snapshot can re-accept consumed keys and hide receipts. Nothing in the same store can prove continuity. Publication must state this limit and require an external monotonic anchor. The anchor itself is deferred.
Master placement. Vercy has not yet decided whether a non-native local transactional store may be the execution master while native records serve as evidence.
Mandate expressiveness. It is unverified whether WM-XCT-001 mandates can carry audience and purpose in de-mandate-constraint without extension.
K2 status. The actClassRef crosswalk to K2 cannot be claimed as conformance while WM-ACT-002 remains queued.
Trust. All authority is host-asserted, so the package must be published as a semantic contract plus a reference fixture, never as an authorization system.
Scope of guarantees. At most one local effect per request holds only inside one store and one transaction. No distributed or external exactly-once claim can be made.