EM-XCT-07 — Action, Authority and Agent Delegation: independent research brief

Status: research and design recommendation only. It does not approve implementation, it does not agree with any other provider, and it does not claim conformance to OAuth, ODRL, XACML, PROV, Cedar or any security standard. All examples are synthetic.

0. Evidence ledger: what I retrieved and what I did not

Retrieved and checked independently

Both parent specifications, downloaded directly:
wm-xct-002 (Access Contract/Consent): SHA-256 9085d977…2a8e2a… correction, 9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db, 260,231 bytes.
wm-xct-029 (Obligation/Commitment): SHA-256 33b9845b2b334949d5538c1c859dbb41c23872577ae6d3502cd48267f17a8e2a, 299,395 bytes.
Both hashes match the brief. Parsing the JSON gave 6 bundles, 16 layers, 29 findings and 113 questions for 002, and 6 / 16 / 29 / 123 for 029. Each has 13 functions.
The two parent tensions the brief flags are real:
Default projection vs default deny. In 002 serviceLayers.crud.read, the default projection for an unlisted role is a validity token that reveals coverage and a scope fingerprint. Meanwhile serviceLayers.access.default_rule says deny by default.
Break-glass. In the same access.exceptions list, break-glass is both permitted under pre-published conditions and "not modelled here".
The 029 composition dependency is real. It lists the Agreement/Contract model as a REFERENCE with required: true. Its own boundary note says an obligation can exist with no agreement at all (statute, court order, unilateral commitment, commitment at large). EM-XCT-07 must not inherit that required reference. 
ver
Primary sources retrieved in full or at the relevant sections:
RFC 8693 (full text via datatracker).
RFC 9110 §9.2.2 (plain-text RFC).
ODRL Information Model 2.2 (W3C TR page: §2.5.2 logical constraints; Terminology for Validator/Evaluator; §2.1.2 Offer).
PROV-O (Delegation class definition).
AWS EC2 idempotency guide.
Cedar authorization reference.
draft-ietf-httpapi-idempotency-key-header-07.
RFC 8785 (JCS).

Not retrieved, or taken only from the brief

The MMAS-Core, MMAS-Interchange, Contract and Event drafts, and the native file-runtime 1.0.0 schema. I found no public links to them on ver.cy. Everything I say about their fields comes from the brief.
The 002 publication metadata.json at the path I guessed returned an empty body. The AGENTS.md file exists (960 bytes) but I did not analyse it.
I did not verify every source in the parents' inventories, including paywalled ISO texts.
Where I rely on search-engine excerpts rather than full pages (AWS, Cedar), I say so.
1. Core decision in one paragraph

EM-XCT-07 should ship as a small profile package with exactly one new object master: a versioned ActionDefinition. Everything else reuses existing Vercy constructs:

Every lifecycle occurrence (proposal, acceptance, authority decision, attempt, effect observation, reconciliation, cancellation, correction) is a real runtime Event with a profiled payload.
Standing delegation is a profile of Contract.
The retry binding, role block, authority snapshot and resource precondition are embedded values.
The executable part is two pieces: a pure deterministic reducer and validator, plus a transactional local synthetic adapter. The adapter can change only a demo-workspace object under the runtime's file lock, and only when a trusted host supplies identity, a policy decision and a clock.

None of the four candidate names survives as an independent object master.

2. Decisions for each candidate and proposed type
Candidate / concern	Decision	Result in EM-XCT-07	Why
ActionContract	NEW object, renamed	ActionDefinition (versioned, immutable per version)	No parent defines an operation's signature, effect class, target type, required authority, or replay and digest contract. "Contract" collides with Vercy Contract, which is a semantic license between parties. A definition is a type-level specification.
ActionRequest (proposed intent)	PROFILE of Event	em-xct-07.proposal.v1 event	A proposal is an asserted occurrence ("X proposed Y"). It confers nothing, so it needs no identity beyond its eventId.
ActionRequest (accepted request)	PROFILE of Event, plus embedded binding	em-xct-07.request.accepted.v1. The requestId is the eventId of the acceptance event. A derived key-slot identifier serves as the event subject.	The only extra identity justified is the retry binding: the scope, key and digest. That is a natural key, not a new master. The Event model already gives immutability, provenance and appended correction.
ActionResult	PROFILE of Event (several types)	attempt.started, effect.observed, reconciled, cancel.requested / cancelled, plus correction	An attempt, an effect observation and a reconciliation are distinct occurrences with distinct observers. The "result" is a reducer view, not a stored master.
Cached result served on retry	DEFER as a store; embedded rule	None stored. Every retry re-renders the view through a fresh read check.	This removes the most common leak path: stored response bodies.
AuthorityBinding (standing delegation)	PROFILE of Contract	DelegatedExecutionGrant	Contract already carries parties, purpose, scope, authority, permissions, validity, versioning and revocation. The profile adds fixed constraints: one hop, no re-delegation, no impersonation, and explicit audience, actions and resources.
AuthorityBinding (point-in-time decision)	PROFILE of Event	em-xct-07.authority.decided.v1, asserted by the host	A decision is an occurrence at a time under a policy version. It is evidence of what the host decided, not a credential.
Credential or token verification	DEFER to the host	None	The package consumes host-authenticated identifiers only.
Ownership, role and delegation registries	REFERENCE (external)	accountableOwnerRef, principalAuthorityBasisRef	Consistent with 002's boundary. The registries are not defined here.
Read/disclose authority for requests and results	REUSE WM-XCT-002 by crosswalk	readCheck requirement mapped to 002's coverage decision surface	002 owns read permission. EM-XCT-07 requires a check but does not redefine it, and it does not inherit the validity-token default.
Underlying duty	REFERENCE, optional (0..1)	dutyRef	A performed action is at most evidence for 029's fulfilment evaluation. There is no runtime import and no Agreement requirement.
Compensation	REUSE the request itself	A new accepted request with compensatesRequestId	Compensation is a new effect, not an undo.
Correction	REUSE Event appended correction	Correction event that supersedes an observation	History is appended to; effects are not reversed.
Idempotency ledger / index	Derived from events; not a master	The runtime index is only a cache	The validator can rebuild slot state from events alone.
3. Package boundary

In scope for the first increment ("EM-XCT-07 0.1.0-research")

spec.yaml, following the Vercy registry form.
JSON schemas for ActionDefinition, the DelegatedExecutionGrant profile, and eight event payload profiles.
The digest byte contract.
A semantic validator and a pure reducer.
A local synthetic adapter supporting exactly one effect class, local-synthetic.field-set, on objects of type em-xct-07.demo-workspace.
Fixtures for the cases in §15.

Out of scope

Authentication, credentials and token formats.
Policy languages and engines.
Ownership and role registries.
Networked or external effects, and arbitrary command execution.
Distributed transactions, outbox or saga orchestration.
Delegation chains, impersonation and emergency or break-glass powers.
Collective or multi-party approval.
Duty fulfilment or acceptance determination.
Accounting.

What a user could install and use now

Describe their organization's actions as ActionDefinitions: parameters, target type, effect class, required role references, compensation pairing and retention.
Describe delegated execution grants.
Validate proposed and recorded event histories offline against the invariants.
Compute the request digest and key-slot identifier.
Run the full lifecycle end to end against demo-workspace objects on a local file store, with a host stub that asserts identities and decisions.

What they must not believe is that the package authorizes anything in production. A host stub's "permit" is exactly as trustworthy as the stub.

What a production deployment must supply

Authenticated identity for actor, principal and delegate, and verification of grants against real registries.
A policy decision point with versioned policy sets and bounded revocation propagation.
Durable, access-controlled event storage with single-writer ordering per executor.
A transactional outbox or equivalent for any real external effect.
Clock discipline, rate limiting and key-entropy enforcement.
Legally reviewed retention.
An implementation of the 002 read check.
4. Role vocabulary (always separate fields, never inferred from each other)
Role	Field	Meaning	Source of truth
Acting identity	roles.actingIdentityId	Who is causing the request now: a person, service or agent	Host authentication
Represented principal	roles.representedPrincipalId	On whose behalf the request is made. Equals the acting identity when there is no delegation.	Host authentication plus grant
Issuer	grant.issuerId	Who issued the delegation grant. Must be the principal or the principal's host-verified representative.	Contract store and host verification
Executor / audience	binding.executorId	The system that performs the effect and to which the request is addressed	Adapter configuration
Accountable owner	roles.accountableOwnerRef	Who answers for the outcome on this resource	Ownership registry (external)
Observer	Event actorId on effect.observed	Who asserts what happened	Host or adapter
Master system	resource.masterSystemId	System of record for the target resource	Registry of the Dimension
Recorder	Event provenance	Who wrote the record	Runtime

A rule that follows from RFC 8693: the runtime Event actorId identifies who asserted that record. It is never evidence of authority.

RFC 8693 §1.1 distinguishes the two modes this table has to keep apart. Under impersonation A is given all of B's rights within a defined context and is indistinguishable from B; under delegation A keeps its own identity and it is understood that A is acting while representing B. EM-XCT-07 supports only the delegation mode. Acting identity and principal are always recorded separately. 
ietf

5. Identity and lifecycle boundary

Seven distinct identities are involved:

ActionDefinition version. The objectId is stable across versions and the recordId is unique per version. definitionDigest is computed over the definition's normative fields.
Proposal. Identified by its eventId. It can be accepted at most once. Rejection or expiry is terminal.
Accepted request. requestId is the acceptance eventId. It is unique within its key slot. Its content is frozen by requestDigest.
Authority decision. Identified by its eventId. There is one decision per attempt, and it binds requestId, requestDigest, attemptOrdinal and policySetVersion.
Attempt. Identified by its eventId. A request may have several attempts, but only after an evidenced not_applied outcome.
Effect. In the local adapter, the effect is the new object revision (its recordId). There is at most one per request.
Duty. External, from 029, referenced optionally.

A repeated request (same slot, same digest) is not a new request. A new attempt is not a new effect. A new effect under a different request is a different identity, even when the payload is identical.

Request state, derived by the reducer from events on the key slot

From	Event	To	Effect?
(none)	request.accepted	accepted	no
accepted	cancelled (host, before any attempt)	cancelled (terminal)	no
accepted	authority.decided deny or indeterminate	denied (terminal)	no
accepted	host-clock time > notAfter at the commit check	expired (terminal, recorded as authority.decided with reason expired)	no
accepted	precondition mismatch at commit	stale (terminal)	no
accepted	authority.decided permit, then attempt.started	in_flight	pending
in_flight	effect.observed applied	applied (final locally)	yes, exactly one revision
in_flight	effect.observed not_applied (with evidence)	accepted (a new attempt is allowed and needs a fresh decision)	no
in_flight	effect.observed unknown, or no observation	unknown	unknown
unknown	reconciled (with evidence)	applied or accepted	as evidenced
any	cancel.requested after an attempt started	unchanged; annotated as cancel-requested	does not stop the attempt

Compensation does not change the state of the original request. The reducer adds a compensatedBy annotation that points to the compensating request.

6. Retry key: namespace, binding and byte contract

Key scope, which selects the slot

dimensionId
tenantId
executorId
keyNamespace
keyEpoch
keyOwnerId (the host-authenticated acting identity)
retryKey (a client string; recommended 128-bit random, printable ASCII, 16–128 characters)

keyOwnerId is part of the scope so that a different caller can neither collide with a key nor probe for its existence.

AWS's practice shows why scope must be explicit. EC2 client-token idempotency is scoped per Availability Zone or per Region, so the same token can launch instances in a different zone or Region. That is vendor practice, not a standard. EM-XCT-07 makes the scope a declared tuple rather than an implicit property of the endpoint. 
AWS

Bound content, which fixes the digest. The binding object contains exactly these fields and nothing else:

The definition's objectId, recordId, version and digest.
dimensionId, tenantId and executorId.
The resource's objectId and expectedRecordId.
actingIdentityId, representedPrincipalId, and delegationGrantRecordId (or null).
purposeCode.
The ordered payload.
notAfter.
maxAuthorityAgeSeconds.
dutyRef (or null) and compensatesRequestId (or null).

The decision itself is not bound. Only the freshness requirement is bound, because the decision must be re-evaluated at commit time.

Byte contract

requestDigest = "sha256:" + hex(SHA-256(UTF-8("vercy:em-xct-07:request-binding:v1") ‖ 0x00 ‖ JCS(binding)))
keySlotId = "akey:" + hex(SHA-256(UTF-8("vercy:em-xct-07:key-slot:v1") ‖ 0x00 ‖ JCS(keyScope ∪ {retryKey})))

JCS is RFC 8785, https://www.rfc-editor.org/rfc/rfc8785. It sorts object properties but forbids changing array element order (§3.2.3). It forbids duplicate property names and preserves string data exactly. Note that it is an Independent Submission with Informational status, not an IETF standard. This is a design choice, and conformance to RFC 8785 is claimed only for these restricted inputs.

To avoid ambiguity in JCS number serialization, the profile restricts payloads further:

Numbers must be integers within ±(2⁵³−1).
Decimals are carried as strings with a declared format.
There is no Unicode normalization. Byte-exact strings are compared, and lone surrogates are rejected.
The validator must use its own parser that rejects duplicate keys.

Vercy Interchange's semantic fingerprint must not be used here, since it sorts arrays and drops descriptive fields. Two payloads such as steps:[a,b] and steps:[b,a] must produce different digests. This is also the behaviour ODRL's andSequence needs: its logical constraint requires all constraints to be satisfied in sequence (ODRL IM 2.2 §2.5.2, https://www.w3.org/TR/odrl-model/).

Retry rules

Same slot, same digest, request exists. No new request, attempt or effect is created. The host returns a reference and state only if a fresh read check passes. Otherwise it returns a uniform "duplicate; not disclosable" response.
Same slot, different digest. The retry is rejected as a key conflict and no effect occurs. The response reveals nothing about the original content. The conflict is audited in a host-private log and no event is written on the slot.
Vendor precedent: EC2 retries with the same client token but different parameters either succeed without further action or fail with IdempotentParameterMismatch. 
AWS
The idempotency-key draft recommends 422 for reuse with a different payload and 409 for concurrent processing (§2.7). It is an Internet-Draft that expired on 18 April 2026 (https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.txt), so treat it as a draft, not a standard.
Same slot while in flight. The retry returns the pending reference and never causes a second attempt.
A rejected, denied, expired, stale or cancelled request consumes its key. A retry cannot resurrect it and cannot re-run a changed policy under the old key. New authority requires a new key.
A proposal cannot be accepted twice. Retrying an acceptance returns the original acceptance or rejection.

Retention and purge. Keys are purged only by retiring a whole keyEpoch. The host keeps the list of retired epochs permanently and rejects keys from them with key_epoch_retired. It never treats them as new.

Purge-on-expiry is exactly what makes old keys unsafe. The idempotency-key draft allows a resource to purge keys on expiry (§2.3). In AWS Proton, client tokens expire eight hours after a request, and retrying with an expired token creates a new resource. The epoch rule makes this hazard impossible for EM-XCT-07 keys. 
AWS

Payload bodies may be purged earlier. When they are, a slot tombstone is kept containing scope hash, digest, terminal state and purgedAt.

7. Authority, delegation, TOCTOU and revocation

What never counts as authority

Labels, document text or model output (such as a "Publish" button seen in a document).
A permission name in a payload, an approved: true field, or a hash.
A grant record that has not been host-verified.

The reducer ignores all of these for authority. Only an authority.decided event is a decision, and only when the host wrote it inside the commit lock and it binds the current requestDigest.

Decision semantics. The possible outcomes are permit, deny and indeterminate. Indeterminate is treated as deny, and no permit is ever inferred from an error.

This is the package's own choice. It is stricter than Cedar's default. Cedar's algorithm is default-deny, lets a satisfied forbid override any permit, and skips a policy whose evaluation errors so that it does not factor into the decision. Cedar returns diagnostics that indicate which policies errored, and system owners may use them to monitor or even choose to fail closed on error. 
Cedarpolicy
Cedarland

Detailed diagnostics are host-private. The decision event carries only a closed reason code: permit, no_permit, forbidden, expired, grant_invalid, audience_mismatch, stale, definition_withdrawn or indeterminate.

Smallest useful delegation subset. Exactly one hop is supported: principal P grants delegate D through a DelegatedExecutionGrant. The grant contains:

An explicit list of ActionDefinition recordIds.
An explicit list of resource objectIds, with no wildcards.
Purpose codes.
notBefore and notAfter.
Audience executorIds.
An optional maxUses.
redelegation: false and impersonation: false, both fixed.

Effective authority is the intersection of P's host-determined authority, the grant's scope, and D's own eligibility to act as an agent at this executor. It is never a union. A grant cannot widen P's authority, because the intersection always includes P's own current authority.

This non-widening rule is a design choice. RFC 8693 does not mandate downscoping. Its security considerations note that delegation creates potential for abuse and suggest the scope claim, together with constraints such as limited token lifetime, to restrict where delegated rights can be exercised. 
ietf

Chains. Any request that presents a chain is rejected, and multi-hop support is deferred. This is stricter than RFC 8693. RFC 8693 says a token consumer applying access-control policy must consider only the top-level claims and the current actor, and that prior actors in nested act claims are informational only. EM-XCT-07 does not even carry a history chain, so a descriptive trail cannot be mistaken for authority. 
ietf

PROV-O is treated the same way: actedOnBehalfOf is descriptive provenance. PROV-O defines Delegation as assigning authority and responsibility to an agent to carry out a specific activity while the represented agent retains some responsibility for the outcome (https://www.w3.org/TR/prov-o/, Delegation class). That describes accountability. It does not verify permission, so a PROV export may be produced but is never consumed as authority.

Deferred explicitly: multi-hop chains, impersonation, emergency and break-glass powers (including 002's contradictory treatment of them), collective approval, and real credential verification.

Where the TOCTOU boundary sits (local adapter). Everything that decides whether the effect happens occurs inside one file-lock critical section:

Acquire the runtime lock.
Re-derive slot state from events and require accepted.
Read the host clock t. Require t ≤ notAfter.
Call the host decision function at time t. This evaluates grant validity and revocation as the host sees them at t, and the definition's withdrawal status.
Compare the head recordId of the target object with expectedRecordId.
Write authority.decided.
If the decision is permit, write attempt.started.
Write the object revision (the commit point), with provenance.requestId.
Write effect.observed applied.
Release the lock.

A revocation whose effective time is after t does not affect this commit. A revocation effective before t that the host has not yet seen is a residual risk. The host must declare and meet a revocation-visibility bound, and the package records grantStateObservedAt so the gap can be audited.

RFC 8693 §2.1 supports this stance. It says a token exchange does not create a tight linkage between input and output tokens, and that propagating revocation events is not a general property of the protocol. Revocation therefore has to be checked at commit, not assumed to have propagated. 
ietf

Ambiguous failure. Several crash windows exist because the event files and the object revision are separate files:

Crash between steps 7 and 8: after restart the request reads as unknown.
Reconciliation scans for a revision carrying provenance.requestId. If one is found, the outcome is applied; if not, it is not_applied. Either way, reconciliation writes a reconciled event with the evidence reference.
Crash between steps 8 and 9: reconciliation finds the revision and records applied.
Timeouts at the client never change state.

Cancellation. A cancel is effective only if the host acquires the lock before attempt.started. After that, the cancel is recorded but the outcome stands. Undoing an applied effect requires a compensating request.

What the design does not claim. It does not claim exactly-once external effects. The lock plus the uniqueness of provenance.requestId gives at most one local revision per request, and only inside one lock domain.

This matches the HTTP definition of idempotency. RFC 9110 §9.2.2 (https://www.rfc-editor.org/rfc/rfc9110#section-9.2.2) defines idempotency by intended effect: repeating a request has the same intended effect even if responses differ. It also says a client should not automatically retry a non-idempotent request without some means to know its semantics are idempotent, or to detect that the original was never applied. The key slot plus reconciliation is that "means to know", and only locally.

8. Schema outline

text
ActionDefinition (object; objectType "em-xct-07.action-definition"; one record per version)
  objectId 1, recordId 1, previousRecordId 0..1, version 1 (semver), definitionDigest 1
  actionTerm 1 (IRI; optional crosswalk to ODRL action)          name 1, description 0..1
  targetObjectType 1          effectClass 1 ∈ {local-synthetic.field-set}  (0.1.0 closed enum)
  parameterSchema 1 (JSON Schema subset: string, integer, boolean, enum, object, ordered array)
  reversibility 1 ∈ {compensable, not-compensable}; compensationDefinitionRef 0..1
  requiredAuthority 1: { allowedPrincipalRoleRefs 1..n, delegable 1 (bool), maxAuthorityAgeSecondsMax 1 }
  maxRequestLifetimeSeconds 1   keyRetentionEpochPolicyRef 1
  disclosure 1: { requestViewProjectionRef 1, resultViewProjectionRef 1 }  (resolved by 002-style read check)
  status 1 ∈ {draft, active, withdrawn}; withdrawnReason 0..1
  stewardId 1, masterSystemId 1

DelegatedExecutionGrant (Contract profile "em-xct-07.grant.v1")
  grantId 1, recordId 1, issuerId 1, principalId 1, delegateId 1
  audienceExecutorIds 1..n, actionDefinitionRecordIds 1..n, resourceObjectIds 1..n
  purposeCodes 1..n, notBefore 1, notAfter 1, maxUses 0..1
  redelegation 1 (const false), impersonation 1 (const false)
  verificationRef 1 (host-asserted), lifecycle via Contract (active/suspended/revoked; effectiveAt)

Event payload profiles (runtime event: recordType=event, schemaVersion=1.0.0, eventId, eventType,
  subjectIds=[keySlotId, resourceObjectId], occurredAt, recordedAt, actorId, payload, provenance, accessClass?)
  proposal.v1          {proposalId=eventId, binding(draft, no key), proposerId, sourceRef 0..1 (e.g. document locator — descriptive only)}
  proposal.rejected.v1 {proposalId, reasonCode}
  request.accepted.v1  {requestId=eventId, keyScope, keySlotId, binding, requestDigest, proposalId 0..1, seq=1}
  authority.decided.v1 {requestId, requestDigest, attemptOrdinal, decision, reasonCode, evaluatedAt,
                        policySetVersion, grantRecordId 0..1, grantStateObservedAt 0..1, deciderId, seq}
  attempt.started.v1   {requestId, attemptId=eventId, attemptOrdinal, decisionEventId, seq}
  effect.observed.v1   {requestId, attemptId, outcome∈{applied,not_applied,unknown}, observedAt,
                        evidence{resourceRecordId 0..1, method}, seq, supersedesEventId 0..1}
  reconciled.v1        {requestId, attemptId, outcome∈{applied,not_applied}, evidence, seq}
  cancel.requested.v1 / cancelled.v1 {requestId, requesterId, seq}
  (correction: Event appended-correction mechanism with target eventId; never deletes)

Embedded values: KeyScope, Binding, Roles, ResourcePrecondition{objectId, expectedRecordId}, AuthorityRequirement.

seq is a per-slot counter assigned by the host under the lock. The reducer rejects gaps, duplicates or out-of-order sequences, which covers reordered delivery.

9. Five-facet coverage for each semantic type

ActionDefinition

Identity/essence: A named, versioned operation over a target type. Identity is the objectId plus the recordId of the version, with a digest over the normative fields. It is not a permission and not a duty.
Lifecycle/time: draft → active → withdrawn. Versions are immutable. Withdrawal applies at commit time to pending requests, which are then denied with definition_withdrawn.
Relations/context: Target type, compensation pairing, optional ODRL action crosswalk, optional duty action-term crosswalk to 029.
Governance/authority: A steward owns it and the Dimension's action registry is its master. Required-authority references point to external role registries. Nothing in the definition itself grants anything.
Evidence/representation: JSON-compatible YAML object record plus digest. It is rendered to humans with the explicit notice that it is "a description, not a permission".

Proposal

Identity/essence: An asserted intent (eventId). It has no key and no effect.
Lifecycle/time: It is either accepted once, rejected, or expires at binding.notAfter.
Relations/context: May cite a source (a document locator) purely descriptively. Links to the resulting request.
Governance/authority: Anyone authenticated may propose. Proposing confers nothing.
Evidence/representation: An event. The source text is never interpreted as instructions.

Accepted request

Identity/essence: requestId (the eventId) plus keySlotId plus requestDigest. Its content is immutable.
Lifecycle/time: The state machine in §5. notAfter is bound in the digest, and the host clock is authoritative.
Relations/context: Definition version, resource precondition, roles, grant, duty and compensation links.
Governance/authority: Acceptance means structural validity and key reservation. It is not authorization.
Evidence/representation: An event. The digest can be recomputed by the validator.

Authority decision

Identity/essence: One per attempt, binding requestDigest and policySetVersion.
Lifecycle/time: Evaluated inside the lock. Its validity window is zero, because it applies only to its own attempt.
Relations/context: Grant record, basis references and the decider.
Governance/authority: Asserted by the host. Indeterminate means deny. Diagnostics are private.
Evidence/representation: An event with a closed reason code.

DelegatedExecutionGrant

Identity/essence: A Contract-profile instrument limiting what D may do for P.
Lifecycle/time: notBefore/notAfter plus Contract revocation with effective time. Freshness is checked at commit.
Relations/context: Issuer, principal, delegate, audience, actions, resources and purposes.
Governance/authority: One hop only. It is intersected with principal authority. Verification is by the host.
Evidence/representation: A Contract record with a verification reference. A PROV actedOnBehalfOf export is descriptive only.

Attempt

Identity/essence: One execution try (eventId, ordinal).
Lifecycle/time: Starts under the lock. Ends with an observation or with unknown.
Relations/context: Its decision event and its request.
Governance/authority: Only the host adapter may write it.
Evidence/representation: An event.

Effect observation and reconciliation

Identity/essence: An assertion that an effect was applied, not applied, or is unknown.
Lifecycle/time: Unknown persists until reconciled with evidence. Corrections supersede but never delete.
Relations/context: The resource revision recordId carrying provenance.requestId.
Governance/authority: The observer is identified, and the host is the master.
Evidence/representation: An event. Disclosure is gated by a fresh read check. An observation is not proof that a duty was fulfilled.
10. Mastership, rights, references and clocks

Masters

Data	Master
ActionDefinition	Dimension action registry
Grant	Contract store
Request-lifecycle events	The executor's event log (single writer, the host)
Demo-workspace resource	The runtime object store
Identities, roles, ownership	External systems
Runtime index	Cache only, never a master or permission source

Rights

Write events: host adapter only.
Create proposals: any authenticated party.
Accept requests: host, on behalf of an authenticated acting identity.
Author definitions: steward.
Issue grants: principal, or a verified representative.
Read anything: only through the read check, default deny, no validity-token default for unlisted roles, and no diagnostics, digests or key-slot state for unauthorized readers.

References

Every reference is either a recordId, which is version-exact, or an objectId plus an explicit precondition.
Floating "latest" references are forbidden in a binding.

Clocks

All timestamps are RFC 3339 UTC in seconds.
occurredAt is when the event happened; recordedAt is when the host wrote it.
Every expiry, freshness or grant-window comparison uses the host clock at the lock.
Client-supplied times are claims.
The host rejects notAfter beyond maxRequestLifetimeSeconds plus a declared skew allowance.
Ordering comes from seq, not timestamps.
11. Falsifiable invariants

Each can be tested by a fixture that should fail.

I1 No effect without a permit. Every revision carrying provenance.requestId=R is preceded, on R's slot, by an authority.decided permit with the same requestDigest. That decision was written in the same lock section, and no terminal state came before it.
I2 Proposals are inert. No revision references a proposalId. A proposal is linked to at most one acceptance, and a rejected or expired proposal has none.
I3 Key uniqueness. For each keySlotId there is at most one request.accepted. A retry with a different digest writes nothing on the slot.
I4 Single local effect. There is at most one revision per requestId. There can be multiple attempts only after an evidenced not_applied.
I5 Non-widening delegation. Wherever a grant is used: acting ≠ principal; the grant's audience includes executorId; action, resource and purpose are all in the grant; the host clock is within the grant window; the depth is 1; and principal authority was independently permitted.
I6 Text is not authority. Mutating payload flags, permission names or hashes cannot change the reducer's authority result. This is a property test.
I7 Unknown stays unknown. The reducer never outputs applied or not_applied for an attempt without an effect.observed or reconciled event carrying evidence.
I8 Append-only history. No event is deleted or rewritten. A correction references its target, and an applied local effect is never reclassified as not applied.
I9 Fresh read check. Every rendered view, including a retry response, is preceded by a read decision at render time. A denied reader receives a response that is byte-identical across "absent", "exists" and "conflict" cases.
I10 Stale precondition. A head recordId different from expectedRecordId at commit produces stale and no revision.
I11 Expiry. A host clock after notAfter at commit produces expired and no revision, even if an earlier decision was permit.
I12 Audience/tenant. An executorId or tenantId mismatch is rejected before key reservation, and nothing is written on any slot.
I13 Compensation is new. A compensating effect has its own requestId and slot. The original remains applied.
I14 Digest determinism. Identical bindings give identical digests. Reordering any array changes the digest. Reordering object keys does not.
I15 Purge safety. A key from a retired epoch is always rejected and never accepted as new.
12. Bundles, layers and Finding → Question → Artifact → Action routes

B1 Definition and identity (layers: L1 action-definition, L2 party-roles)
B2 Intent and request (layers: L3 proposal, L4 retry-binding)
B3 Authority and delegation (layers: L5 authority-decision, L6 delegation-grant)
B4 Execution and evidence (layers: L7 commit-boundary, L8 outcome-reconciliation, L9 compensation-correction)
B5 Disclosure and retention (layers: L10 read-check, L11 retention-purge)

#	Layer	Finding	Question	Artifact	Action
R1	L1	Operations lack a versioned signature	Which exact version and effect class does this request bind?	ActionDefinition record plus digest	register-definition (validator)
R2	L1	Withdrawn definitions must stop pending work	Is the definition active at commit time?	Definition status	commit-check denies with definition_withdrawn
R3	L2	Roles collapse into "user"	Who is acting, who is represented, who is accountable?	Roles block	validate-roles
R4	L3	Document text looks like a command	Did anyone with authority accept this, or was it only seen?	Proposal event	record-proposal; never execute
R5	L4	Retries duplicate effects	Does this slot already hold a request?	keySlotId, request.accepted	accept-or-dedupe
R6	L4	Changed payload reuses a key	Does the recomputed digest equal the stored digest?	requestDigest	reject-key-conflict
R7	L4	Array order can be silently normalized	Is the digest byte-exact over ordered arrays?	JCS byte contract	compute-digest fixture
R8	L5	Stale decisions are reused	Was the decision made inside this attempt's lock?	authority.decided	decide-at-commit (host)
R9	L5	Errors become permits	Is indeterminate handled as deny?	Reason code	reduce-decision
R10	L6	Delegation widens authority	Is the effective scope the intersection?	Grant profile	evaluate-delegation
R11	L6	Chains and impersonation creep in	Is depth 1 and impersonation false?	Grant constants	reject-chain
R12	L7	Concurrent writers race	Does the head equal the expected recordId under lock?	ResourcePrecondition	commit-effect
R13	L7	Revocation arrives mid-flight	What revocation view did the host have at t?	grantStateObservedAt	record-revocation-view
R14	L8	Timeouts get treated as failure	Is there evidence of the outcome?	effect.observed unknown	hold-unknown
R15	L8	Crash windows leave gaps	Does a revision with this requestId exist?	reconciled event	reconcile-scan
R16	L9	"Undo" hides history	Is compensation a new request?	compensatesRequestId	request-compensation
R17	L9	Wrong observation recorded	What does this correction supersede?	Correction event	append-correction
R18	L10	Cached results leak	Is the reader covered now?	002 coverage crosswalk	render-view
R19	L11	Purge re-enables keys	Is the epoch retired?	Retired-epoch list	retire-epoch
13. Executable acceptance design: what is semantic, what is host

A pure reducer plus a transactional local adapter is appropriate, and it is the smallest increment that can falsify I1–I15. A validator alone could not test I10–I13 or the crash windows.

Five separated layers

Semantic contract. Schemas, the byte contract and invariants. Pure data.
Reducer and validator. Pure functions. They take events, definition and grant records, plus an explicit now, and return state or violations. They have no I/O and no clock.
Host authorization (trusted, supplied).
authenticate() yields host-asserted identifiers.
decide(request, now) yields permit/deny/indeterminate with a policy version.
canRead(reader, view, now) yields a read decision.
clock().
The reference host stub is labelled "test only".
Storage and lock. The runtime's file lock and refuse-overwrite semantics. The runtime index is used only as a cache and can be rebuilt.
Effect transaction. The adapter performs the §7 sequence. Its only effect is setting a declared field on an em-xct-07.demo-workspace object. Anything else fails validation: no subprocess, no network, no credential.

Emitted evidence. Only runtime events and one object revision per applied request.

14. Synthetic application profiles

(a) Founder updates a demo workspace.

Founder F owns workspace W. Definition rename-workspace v1.0.0 sets displayName and is compensable by restore-workspace-name.
F is both acting identity and principal, with no grant.
F sends key K1 with expectedRecordId=W@r7.
The host decides permit, the adapter writes W@r8, and effect.observed records applied.
F's network drops and F retries with K1. The retry returns the reference after a read check, and there is no second revision.
To revert, F submits a new request, restore-workspace-name with expectedRecordId=W@r8 and key K2. W@r9 is written. Both requests remain in history.

(b) Matrix organization.

Employee E (acting identity) requests rename-workspace for unit U's workspace.
U is the represented principal, through a host-verified membership basis reference.
The executor is exec:demo-host. The accountable owner is U's head H, from the ownership registry.
The decision requires U's authority and E's eligibility. H is recorded as accountable owner but does not need to approve, unless the host's policy requires it, which is out of scope for collective approval.
The event actorId is the host for acceptance and E for the proposal. H never appears as actor.

(c) AI service with delegated execution.

Agent A proposes renaming W for F.
F issues grant G:
delegate A
audience exec:demo-host
action rename-workspace@r3
resource W
purpose demo-setup
window 30 minutes
maxUses 1
A's request carries acting identity A, principal F and grant G.
The effective scope is F's authority ∩ G ∩ A's agent eligibility. A second use, a different resource, a different executor or a chained sub-agent are all rejected.

Negative test: "Publish" seen in a document. Agent A reads a document containing a Publish control and instructions to publish. It records proposal.v1 with the document locator as sourceRef, then attempts publish-workspace under grant G. The host denies with no_permit, because the action is not in G and F has no current publish permission. The result:

No revision is written.
The proposal stays unexecuted.
A receives no diagnostics.
A validator fixture confirms that the text in the document never reaches authority evaluation.
15. Case matrix: first increment versus host requirement
Case	First increment (fixture plus reducer/adapter)	Host requirement in production
Retry with one effect	Implemented (I3, I4)	Durable single-writer log
Changed payload, same key	Implemented (I3, I14)	Uniform conflict response over the wire
Wrong audience or tenant	Implemented (I12)	Authenticated executor identity
Authority expiry	Implemented (I11, grant window)	Clock sync
Revocation	Implemented against a stub revocation list at t	Bounded revocation propagation, declared and monitored
Stale resource	Implemented (I10)	Preconditions for external resources (ETag/version)
Concurrent or reordered delivery	Implemented (lock, seq)	Distributed ordering if there are multiple executor nodes
Unknown outcome	Implemented, including crash-window fixtures (I7)	Real reconciliation against external systems of record
Cached-result disclosure denial	Implemented with a stub read check (I9)	002-compatible read-check implementation
Cancellation before and after start	Implemented	Cancellation semantics of external executors
Compensation	Implemented as a new request (I13)	Compensation feasibility for real effects
Corrected history	Implemented (I8)	Event-model correction rules as finalized
Publish-from-document negative	Implemented (I6, I2)	Prompt-injection controls in agent runtimes
Retired key epoch	Implemented (I15)	Retention legal review
16. Migration, compatibility, limits and deferred work

Versioning

Event types carry .v1. The digest and key-slot domain tags carry :v1.
A new canonicalization rule means a new domain tag and a new key namespace. Old slots remain bound to their original algorithm, and dual-read is required.
New definition versions get new recordIds. Pending requests keep their bound version, but a withdrawn version is denied at commit.
Grants follow Contract versioning. A request binds the exact grant recordId, and an amendment does not carry over to it.
Adding optional binding fields changes digests, so it requires a new binding version, never a silent addition.

Deferred increments

D1: external effect adapter with an outbox.
D2: multi-hop delegation with attenuation proofs.
D3: collective or multi-party approval.
D4: break-glass, as an enforcement-sibling concern.
D5: credential verification profiles (for example, mapping RFC 8693 act to roles).
D6: batch or ordered multi-action requests.
D7: duty-fulfilment evidence feed into 029.

Limits

A single lock domain.
Local synthetic effects only.
Host-asserted identities and decisions.
No confidentiality of the event store beyond what the host provides.
17. Source classification
Source	Type	Used for
RFC 8693 §§1.1, 2.1, 4.1, 5 — https://datatracker.ietf.org/doc/rfc8693/	IETF Proposed Standard	Delegation versus impersonation, nested actors as non-authoritative history, no inherent revocation propagation
RFC 9110 §9.2.2 — https://www.rfc-editor.org/rfc/rfc9110#section-9.2.2	Internet Standard (STD 97)	Idempotency means intended effect; responses may differ; retry caution
draft-ietf-httpapi-idempotency-key-header-07 §§2.2–2.4, 2.7	Expired Internet-Draft	Contrast only: purge-on-expiry, 422/409
RFC 8785 §3.2.3	Informational, Independent Submission	Byte canonicalization (design choice)
ODRL IM 2.2 §2.5.2 and Terminology — https://www.w3.org/TR/odrl-model/	W3C Recommendation	Ordered andSequence; an Evaluator determines rule satisfaction, which is not execution
PROV-O Delegation — https://www.w3.org/TR/prov-o/	W3C Recommendation	Descriptive responsibility only
AWS EC2 idempotency — https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html	Vendor practice	Scoped tokens, parameter mismatch
AWS Proton client token expiry	Vendor practice	Hazard example
Cedar authorization — https://docs.cedarpolicy.com/auth/authorization.html	Open-source project documentation	Default deny, forbid precedence, skip-on-error plus diagnostics

Everything else (epochs, intersection rule, indeterminate-as-deny, one-hop limit, byte contract) is my design choice.

18. Strongest counterexample, uncertainty and recommendation

Strongest counterexample to this design

The guarantees are true only because the effect and its evidence share one lock domain. Consider a user who builds a second adapter that calls a real SaaS API and reuses the reducer unchanged. Every fixture stays green:

The reducer sees attempt.started, then a timeout, then unknown.
Reconciliation "scans for a revision with requestId" and finds none, because the external system has no such revision. It records not_applied.
A new attempt runs and sends a second real effect.

I4, I7 and reconciliation are sound locally and unsound the moment "absence of local evidence" stops meaning "absence of effect". The design must therefore make reconciliation evidence class-specific:

not_applied is admissible only through an evidence method that the definition's effectClass declares authoritative.
The validator must reject any effectClass other than local-synthetic.field-set in 0.1.0.

Even so, the green test suite invites over-generalization. That is a documentation and social risk as much as a technical one.

A second counterexample: "reversible" is conditional. If a third party writes W@r9 between the effect and the compensation, the compensation's precondition goes stale and the effect is no longer reversible without a new decision about whose change wins.

Remaining uncertainty

Whether runtime 1.0.0 requires subjectIds to resolve to existing objects. If it does, the derived keySlotId needs a lightweight slot object, which is exactly the fake host object the brief warns against. This must be confirmed against the runtime before implementation.
Whether the Event draft's appended-correction mechanism allows reclassifying an outcome, or only metadata.
Whether Contract can express the fixed redelegation/impersonation constants and the intersection semantics without extension.
A uniform denial response still leaks timing. That is out of scope.
I did not read the MMAS, Event, Contract or runtime drafts myself.

Implementation-ready recommendation (not an approval)

Proceed with EM-XCT-07 0.1.0-research containing:

Exactly one new object type, ActionDefinition.
Eight Event payload profiles.
One Contract profile.
The RFC 8785-based byte contract with the integer and duplicate-key restrictions.
A pure reducer and validator.
The local synthetic adapter limited to local-synthetic.field-set.
Fixtures for I1–I15 and every row of §15.

Gate implementation on two checks:

Confirm the subjectIds resolution rule in runtime 1.0.0.
Obtain a written decision from Vercy maintainers that 002's validity-token default and break-glass exception are not inherited, and that 029's required Agreement reference is not imported.

Publish the package with a prominent statement: host-asserted decisions are not authenticated authority, and the at-most-once guarantee holds only within one local lock domain.