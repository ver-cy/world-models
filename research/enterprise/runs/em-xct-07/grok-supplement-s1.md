Team locks agree on dropping a second mandate master, keeping ActionRequest as a native object, and hiding existence from denied readers. S1 amendment follows.

EM-XCT-07 — bounded research supplement S1

Amendment to the original independent brief. Not an implementation approval. Not agreement with another provider. Parent exclusions already in force (validity-token default, break-glass, XCT-029 Agreement import) stay excluded.

Retrieval (this supplement)

Independently hashed this session:

Artifact	File SHA-256	Result
XCT-001 spec.yaml	fa942556a3f460729db2e94b24d1efd4d33ee2e5fb0b1deed3ce040756acf474	matches the supplement brief
EFA spec.json 0.1.0	cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582	matches
K1 function seed	e93a14c18a08f1a07ed0ea13c13f4e3b860c87d131e26e6ff83e3a7a56e4a9c0	matches
K2 act seed	b262d62aaf41bec6c754ccac6bd65710cb9b85086fc791b9620eef9116f128ef	matches

XCT-001 publication metadata also carries synthesisSha256 b7e519210f7cc00c1972e23e420c89ba366d72260c08193d7b9f371da730cf9f. That is a different digest than the file SHA. Do not conflate them.

XCT-001 0.3.1-enterprise.1 records contestable control. “Control answers ‘who may grant’; access answers ‘who may do what, now’.” Runtime authorization, credentials and legal validity are outside its boundary. It already describes a scoped revocable DelegationMandate, explicit sub-delegation limits, and mandate-verification evidence. verify-delegated-authority and grant-or-revoke-delegation-mandate are declarative functions, not a shipped verifier.⁠Ver

EFA 0.1.0 WriteGrant authorizes particular writers to admit a source’s observations for an exact scope/predicate. StewardshipAssignment conveys duties, not execution or sub-delegation. MastershipRule conveys source precedence, not permission. The module does not implement action execution or a general delegation-chain register.⁠Ver

K1 0.2.0: a function is “a named purpose an agent can fulfil” (name, definition, domain, typical outputs). Ability is not action; function is not permission and not an executable operation definition. Seed Markdown; WM-ACT rows remain queued.⁠Ver

K2 0.2.0: actClass is “the typed verb an act instantiates” (name, definition, domain, expected participants). Act occurrences align with Event. Missing from an operation definition: parameters, preconditions, effect boundary, retirement, adapter binding, immutable version.⁠Ver

D1 (three synthetic ActionRequest objects + SubmissionEvents; six envelope checks; fourteen rejected inputs) and the isolated SQLite 24-test prototype are representational / local-behavioral evidence only. They are not cited below as implemented authorization or native installation.

Decision 1 — definition / request / event / basis
Identity	Disposition	Why it earns a separate identity
ActionDefinition	NEW sibling object. ALIGN to K2 actClass and K1 function. Not a profile of those incomplete seeds. Not an external-only pin for increment-1.	Increment needs parameters, preconditions, effect boundary, retirement, adapter binding and immutable version. Seeds do not have them. Listed verb is still not permission. When WM-ACT-001/002 publish, a later profile/refinement is possible — deferred.
ActionRequest	NEW native object (keep original).	Independent intent identity, immutable frozen content, lifecycle derived from Events. Generic object revision ≠ execution state. D1 shows envelope fit; identity is chosen semantically, not because fewer objects would be prettier.
ActionProposal	Embedded draft (keep).	No object admission, no retry key, no requestId.
Attempt / observation Events	PROFILE of native Event (keep).	Occurrence identity. subjectIds are retained object IDs or record IDs (request, resource, prior Event).
Standing mandate	EXTERNAL REFERENCE to XCT-001 DelegationMandate. Withdraw the original brief’s “new small DelegationMandate master.”	XCT-001 already owns that artifact. Minting a second master would duplicate control. XCT-001 still does not evaluate “may do this action now.”
AuthorityDecision	EMBEDDED fresh action-scoped snapshot (keep).	Separate from standing control. Host PDP fills allow|deny|unevaluable at accept and at each delivery.
WriteGrant / StewardshipAssignment / MastershipRule	Do not reuse as execution permission.	EFA scopes observation admission, duties, and source precedence only.
MMAS Contract profile	DEFER as increment-1 basis.	Contract is a semantic license. Standing control already sits in XCT-001. A Contract binding would overlap without an exact record map.
Retry digest	Payload field + host table. Not a subject.	Derived hashes are not known Event subjects.
dutyId	REFERENCE XCT-029 only.	Performed action still does not prove fulfilment.

Original brief otherwise stands: seven party roles; ordered digest ≠ Interchange fingerprint; execution ≠ disclosure; local synthetic SET-TO-DECLARED-VALUE only.

Decision 2 — one native binding

Binding. ActionRequest is a retained native object. requestId = objectId. Lifecycle Events cite that objectId and the target resource objectId/recordId in subjectIds. A correction Event may also cite the prior Event ID. The retry key and ordered payload digest live on the request object and in the host RetryKey table — never as Event subjects, never as a minted keySlot object.

Pending identity. A proposal is not an admitted object. First admission creates the request object in pending (accepted for delivery, not committed effect). Retries reuse the same objectId + same retry key.
Immutable content. Frozen payload, pins, party tuple and digest do not change after admission. Later Events do not rewrite the object bytes.
Event issuer versus intended actor. Native actorId is the recorder/observer (host admission actor). actingIdentity and representedPrincipal stay on the request object and may be copied into Event payload. Do not collapse them.
Retries. Same object + same ordered digest. Each delivery may append attempt-recorded. Effect Event at most once.
Correction. New Event; subjects include request objectId and corrected eventId. Appends knowledge; does not undo the effect.
Archive / admission. Host admits objects under its trusted configuration. The generic installer is not a semantic execution engine. Companion validator owns request-shape, digest, party tuple and intersection fields.

File durability (design choice, not demonstrated). One file lock around several writes is not an atomic multi-file commit. Increment-1 should use a single authoritative store transaction (the SQLite prototype pattern) or, if files are used, specify: write order, fsync, crash ⇒ unknown if any file of the set is missing, and a real unique constraint on (keyNamespace, dimensionId, executorId, retryKey). A provenance.requestId property is not that constraint. Absence of an effect record proves no effect only if that store is authoritative and complete.

Decision 3 — minimal direct-delegation fixture

Standing grant does not ship as a registry in this package. External reference to a host-owned XCT-001 mandate is adequate for increment-1.

Fixture contract (synthetic records + intersection checker only):

principalScope and delegateScope as independent field sets (not one boolean “delegated”).
hostVerifiedIssuerStanding: allow|deny|unevaluable plus xct001MandateRef, supplied by the host. The package does not verify credentials and does not run XCT-001’s declarative functions.
Exact intersection required: Dimension ∩ resourceId+version ∩ actionDefinitionId+version ∩ purpose ∩ audience/executor ∩ time window.
chainDepth must equal 1. Attribution mode = representation. Impersonation rejected. Widening rejected.
WriteGrant and StewardshipAssignment presented as execution grants are rejected.

This is narrower than XCT-001 (which models sub-delegation limits). Increment-1 still forbids chains. Host standing plus a fresh AuthorityDecision remain two different facts.

Decision 4 — denial, deadline, cancel, disclosure, terms

Terms (locked).

delivery = transport arrival.

attempt = execution try inside the lock (attempt-recorded).

effect = durable put + effect-observed.

These three are not interchangeable.

Lifecycle.

Proposal: open → withdrawn | rejected-precondition | admitted-as-pending.

Request: pending → committed | cancelled | expired (may remain pending).

rejected-precondition (malformed, wrong tenant, digest conflict, document-text-as-grant, WriteGrant-as-execute): terminal. No request object, or no later apply.
Denied execution on a pending request: retryable until requestExpiresAt. Each delivery re-checks current authority. First-deny-is-terminal is rejected for increment-1: it cannot represent “deny now, grant restored before expiry” without minting a new key, and it confuses policy flicker with client error.
Replay after deadline: expired. No apply. Same key does not resurrect a proposal or a pending request.
Cancellation race: cancel of pending succeeds if the effect is not committed. An in-flight try that already reserved under the lock either commits or parks unknown. Cancel of committed work is a new compensation request: payload carries the old before-value; current resource revision must equal the original receipt’s after-revision; intervening updates reject it.
Caller-unknown. After response loss the caller’s outcome is unknown even if the store committed or rolled back. External in-flight/reconciliation is deferred, not simulated.

Disclosure (locked). Execution allow ≠ disclosure allow. For a reader who fails the current disclosure check, the outward response is identical for absent, existing pending, existing committed, conflicting digest, and retired tombstone. One generic not-available. A “duplicate-but-not-disclosable” or “conflict” answer to a denied reader leaks existence. Conflict and tombstone detail are host-internal or for authorized parties only.

Decision 5 — tests, facets, why not publishable
Protocol facets (selected types)

ActionDefinition

identity-class: versioned operation-catalogue sibling of actClass; not a K1 function; not a permission.
direct-properties: actionCode, definitionVersion, payload schema, effectClass=local-synthetic-set, reversibility, preconditions, retirement, adapter binding.
recognition-observation: recognised by id+version pin; a document heading does not recognise a grant; ALIGN citation to K2 name/domain only.
capabilities-behaviour-actions: describe/validate/retire; listed verb grants nothing.
context-evidence: issuer, Dimension, schema digest, optional actClassCitation.

ActionRequest

identity-class: admitted intent object; requestId=objectId; not an Event.
direct-properties: definition pin, resource pin, frozen payload, ordered digest, retry key, expiry, party tuple, xct001MandateRef 0..1, state pending|committed|cancelled|expired.
recognition-observation: companion shape + native object envelope; generic object state is not execution state.
capabilities-behaviour-actions: admit, deliver-attempt, commit-put, cancel-pending, expire; no self-grant.
context-evidence: embedded AuthorityDecision, host issuer-standing, Events whose subjectIds include this objectId.

AuthorityDecision (embedded)

identity-class: evaluation snapshot, not a mandate and not a master.
direct-properties: allow|deny|unevaluable, evaluatedAt, validityHorizon, action/resource/actor/principal/purpose pins.
recognition-observation: recognised only as payload on request or attempt; unevaluable ⇒ no effect.
capabilities-behaviour-actions: none in package; host PDP writes it.
context-evidence: policy pins, XCT-001 mandate ref; diagnostics host-only.

Attempt / observation Event

identity-class: native Event occurrence.
direct-properties: required native fields; eventType in attempt-recorded | effect-observed | effect-unknown | effect-compensated | observation-corrected.
recognition-observation: subjectIds resolve to retained request/resource/prior-event IDs only.
capabilities-behaviour-actions: append; correct-by-new-event; no undo.
context-evidence: actorId=recorder; payload carries acting identity; disclosure check before payload return.

DelegationMandate is not a selected type here.

Indispensable tests

Mark implemented only when delivered code shows the result. D1 envelopes and the SQLite prototype do not satisfy this list.

Same key + same digest → one effect.
Same key + changed bound field → conflict, no effect.
Wrong audience/tenant → rejected-precondition.
Fresh deny on pending → no effect, request still pending.
Grant restored before expiry → later delivery may commit once.
Replay after expiry → no effect.
Intervening resource update blocks put and compensation.
Compensation requires old before-value and current revision = receipt after-revision.
Correction appends; no undo.
Denied reader: absent / existing / conflict / retired → identical not-available.
Delivery ≠ attempt ≠ effect.
subjectIds are real object/record IDs; digest is not a subject.
SET after intervening work does not double-apply.
Partial write / crash → unknown, not invented success.
Document text “Publish” → rejected-precondition.
WriteGrant or StewardshipAssignment as execute grant → reject.
Restored internally-valid snapshot is a new epoch; no automatic replay.
Why a frozen audit still cannot publish
D1 is envelope feasibility, not installed Dimensions, authorization or execution.
SQLite 24-test prototype: no real credentials, no final schema, a delegated boolean is not scope containment, not native-installed.
XCT-001 mandate functions are declarative; no shipped verifier.
File lock ≠ atomic multi-file commit.
A store restored to an older internally valid snapshot can look complete and still be discontinuous; an epoch field in that same snapshot cannot prove continuity.
maxUses needs an authoritative concurrent counter — deferred.
This supplement has not been independently audited as shipped code.
No exactly-once claim for external or restored stores.
Strongest S1 counterexample

Two failures that survive the original brief’s mitigations.

A. Retryable deny without a fresh check. Pending request; XCT-001 standing mandate revoked between deliveries; client retries after response loss. Terminal-deny strands a later re-grant. Retryable-deny without re-evaluation resurrects revoked standing. The increment must re-check host standing and mint a new AuthorityDecision on every delivery.

B. Snapshot restore plus “no effect record ⇒ no effect.” Authorized client commits. Store is restored to a pre-commit snapshot that is internally valid. A denied reader still sees not-available (existence-hiding holds). An authorized reconciler treats the missing effect record as proof of no effect and replays the put, creating a second effect in the restored epoch. Increment-1 must treat restore as a new epoch requiring operator reconcile, not automatic replay.

Residual: local SET-TO-DECLARED-VALUE under one trusted host remains the only honest executable slice. Everything else stays host-supplied or deferred.