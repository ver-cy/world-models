# Enterprise Action Requests — provisional contract direction

EM-XCT-07, design revision D1, 22 September 2026. **Codex design proposal only.** Grok's independent study is complete and critically assessed. Claude's substantive study and both frozen implementation audits are pending. This document is not a released metamodel, an implementation approval or a production execution service. The earlier 24-test transaction experiment does not implement this complete contract.

## Purpose and usable boundary

Give a company Dimension an unambiguous description of an explicitly submitted action request, the attempts to execute it, the current authority checks and the resulting evidence. The first proposed package describes and validates those records and demonstrates one reversible operation on an invented local workspace: replace an ordered list of labels under a resource revision precondition. It cannot execute arbitrary commands, interpret instructions in documents, publish content, call external APIs or authenticate real parties.

Use one independently identified immutable **ActionRequest** per intended operation. Its reason for identity is that it can remain pending, be cancelled, expire, be referenced by several attempts and receive a receipt or later observations. This is a semantic choice, not a workaround for a narrow Event envelope. Native Vercy Events represent the submission, attempts, terminal dispositions and observations. References to an Event record ID are legal in the native runtime; using an Event as an intent anchor remains a valid alternative for a smaller submission-only profile. That alternative is rejected provisionally here because cancellation and pending work need a durable intent that is not itself an occurrence.

The request has no editable semantic revisions. Changing actor, principal, target, parameters, purpose, deadline or definition requires a new request ID and retry key. Generic native object `state` is not an execution state. A request can remain an active record after its execution has completed; the derived execution state comes from authoritative events. No parallel request-state fact is required.

## Reuse and new meaning

| Candidate | D1 decision | Boundary |
|---|---|---|
| ActionContract / ActionDefinition | Exact external definition reference plus a bounded local adapter definition. | MMAS Contract already expresses a semantic license. Do not invent a second universal contract master. A production definition registry is external; its exact revision and schema must be resolved by the host. |
| ActionRequest | New independently identified intent, projected to a native object. | Immutable intent; submitter and intended actor need not be the same role, but this first adapter requires them to be the same authenticated fixture identity. |
| ActionResult | Native executor ReceiptEvent and separate OutcomeObservationEvent profiles. | A receipt from the authoritative local transaction is different from a caller's report, a duty's fulfilment or a current resource snapshot. |
| AuthorityBinding | Embedded evidence of a host decision plus optional versioned external authority-basis reference. | A record of a check, never a portable grant. A fresh decision is outside the immutable intent digest. |
| DelegationMandate | External referenced basis; no new master. | Ownership already describes scoped mandates. The first adapter demonstrates only a host-configured direct representation relationship. |
| ActionProposal | Advisory native Event profile. | May be drafted by a person or an AI service. No automatic conversion, execution or authority. A later request may cite it as context. |
| Attempt | Native Event profile. | Each authorized delivery/retry gets its own attempt occurrence and decision evidence. A retry does not receive a second effect identity. |
| Deduplication record | Private authoritative adapter state. | One key-to-intent binding in a retained namespace; not a user-editable business object or a catalog metamodel. |
| Compensation | New ActionRequest with a typed link to a retained earlier receipt. | A new currently authorized, version-guarded operation. It does not erase the original request or guarantee restoration after intervening changes. |

No runtime imports of WM-XCT-001/002/029 are implied by these conceptual references. Exact dependencies for an installable package remain to be decided and checked against native bindings.

## Record and field contract

All shapes are closed. IDs are case-sensitive opaque identifiers, not display labels or authenticated identities. Local native record IDs must satisfy the native pattern. External URIs require separate validation; do not assume that every URI fits a native record ID. All nullable optional fields are explicit in the canonical intent. Reject duplicate JSON keys, unsupported schema versions, non-finite numbers, unpaired Unicode surrogates and unknown fields before hashing.

The proposed ActionRequest has exactly one `intent` and one host-generated `admission` record:

| Intent field | Cardinality / type | Meaning and constraint |
|---|---|---|
| requestId | 1 identifier | Independent intended-operation identity, immutable and unique in a Dimension. Reusing it under another key is forbidden. |
| dimensionId, executorId, executorEpoch, retryKey | 1 each | Retained deduplication namespace and exact key. A new executor epoch is a governance recovery boundary, never permission to resend an old request. |
| definitionRef | 1 closed tuple | Definition ID, immutable revision and exact SHA-256 of the accepted definition artifact. The trusted host resolves and verifies it. |
| actorId, principalId | 1 each | Intended authenticated actor and represented principal. Equality is permitted. Inequality requires an explicit current direct representation rule in the first adapter. |
| purpose | 1 nonempty code | Exact purpose matched by current host policy; no free-text instruction interpretation. |
| resourceId, expectedRevision | 1 each | Target of the bounded effect and nonnegative integer compare-and-set revision. A reference is not evidence of access. |
| expiresAt | 1 UTC instant | Latest permitted first effect; half-open deadline (`now < expiresAt`). A replay of a committed result is not a first effect. |
| parameters | 1 closed object | For the first adapter only, `labels`: ordered array of bounded strings. Preserve order and duplicates unless the exact definition forbids them. No arbitrary operation name, code, URL or script. |
| basisRef | 0..1 versioned reference, explicit null | Historical claimed basis context. If supplied it must match the host's verified basis; omission is not ambient authority. No inline credential. |
| proposalEventId | 0..1 reference, explicit null | Context only. Citing an advisory proposal does not activate it or inherit rights. |
| compensatesReceiptId | 0..1 reference, explicit null | Typed link to an earlier trusted effect receipt on the same resource. Host verifies the retained target; compensation remains a new request. |

`admission` contains one trusted submittedAt, submittedBy, admitted definition pin, immutable intent digest and submission event ID. It is generated once, stored durably and returned unchanged after a lost response. It is not part of the client retry input. The definition pin repeats the verified intent pin as admission evidence, not a second mutable value. Accountable owner is retained in the current host decision/definition context rather than treated as an implicit grant or client-controlled principal.

Each semantic event uses native `eventId`, `eventType`, `subjectIds`, `occurredAt`, `recordedAt`, `actorId`, `payload` and `provenance`. The request is a subject. Specific payloads are separately closed and validated:

- **ProposalEvent**: proposer, proposed definition/target/parameters/purpose and optional represented-principal suggestion. No accepted request, decision or effect. A proposal's later alteration is another proposal Event with a link, not overwrite.
- **SubmissionEvent**: request ID and exact immutable intent digest; trusted admitting host actor and admission timestamp. Exactly one original submission per request.
- **AttemptEvent**: request ID, attempt ID equal to the Event ID, current host decision evidence, operation (`execute` or `replay`) and outcome (`denied`, `stale`, `expired`, `replayed`, `committed`, `retired`). A claimed decision has no authority outside the trusted adapter. Denied callers receive no identifying diagnostics; any privileged audit is retained internally.
- **ReceiptEvent**: request ID, successful attempt ID, authoritative effect ID, before/after resource revision, ordered before/after value, exact definition and intent pins. Exactly one successful effect receipt for a request. A receipt is historical; do not present its value as the resource's current value.
- **DispositionEvent**: request ID and terminal disposition (`cancelled`, `expired`, `rejected-precondition`) with current governance decision and reason code. It cannot follow a committed receipt. A denied attempt alone is not terminal.
- **OutcomeObservationEvent**: request ID, observer, reported knowledge (`unknown`, `reported-success`, `reported-failure`), evidence references and optional corrected Event ID. It never changes the authoritative execution state. A correction must target an earlier observation of the same observer/request, preserve history and form one unbranched correction chain in the retained view. A reported success is not an executor receipt.

The reference code must choose whether a distinct AttemptEvent `attemptId` field is worth repeating; if present, equality with native Event identity is mandatory. No hidden independently mutable AuthorityDecision object is introduced: embedded decision evidence is identified by its containing event plus a field path. An external decision reference may be stored only as a versioned provenance reference. A denied unknown request identifier goes only to the host's private security log; it does not invent an ActionRequest or a native AttemptEvent with an unresolved subject. Access-controlled attempts against retained admitted requests can be represented by the profile. Native event actorId identifies the issuer of the assertion: the executor for its receipts, admitting host for submissions, or observer for observations. The requested actor/principal stay in the pinned intent.

## Host trust and authority

The adapter owns a current policy configuration and the test session identity. The caller supplies intent, not the policy, current clock, identity proof or live-state snapshot. The synthetic fixture still trusts its harness to supply those roots; the package must say so explicitly.

For a first execution, the current policy must permit the actor to act for the principal for the exact definition, resource, purpose, executor and Dimension, within the host policy's validity and the request deadline. Direct representation must be bounded by both the principal's current permitted scope and the actor's delegated scope. A single `delegated=true` field cannot prove that containment. The next implementation must represent and check both scopes separately, even in the fixture. No chain-depth greater than one, impersonation or emergency bypass is accepted.

The issuing party's standing is a trusted host configuration responsibility. If the fixture records an issuer, its role and scope must be explicitly installed by the fixture governor; a vice-president label is not evidence of the represented unit's authority. Real identity authentication, grant issuance, revocation transport and federation remain external.

Serialize policy changes, resource changes, admission, cancellation and execution in the same local SQLite write-transaction order. Authorization is evaluated after acquiring that transaction. A revocation committed before an execution transaction denies it; a later revocation does not retrospectively erase an earlier effect. No claim is made about remote revocation not yet known to the host or an external transaction.

## Retry identity and disclosure

Bind every intent field above using one documented byte algorithm: Python 3.12 JSON, UTF-8, sorted object keys, no ASCII escaping, compact separators, finite allowed values only, no Unicode normalization, arrays preserved exactly. Store both canonical bytes and their SHA-256. This is a bounded Python representation, not RFC 8785, not Vercy Interchange's order-insensitive semantic fingerprint and not a cryptographic authority proof. Equivalent display strings can remain different requests. Migration must preserve bytes or perform an explicit new namespace/version transition.

The key tuple is `(dimensionId, executorId, executorEpoch, retryKey)`. Same tuple and same intent bytes locate the original request; changed bytes conflict without executing. A separately enforced unique requestId prevents changing the key to reuse the same request identity. Fresh decision times/policy revisions, transport attempt IDs and admission receipt times do not enter this digest.

On every execution/replay call, check current execute permission before exposing deduplication state. A committed matching request can be replayed after its request deadline because it cannot produce a first effect, but only with current execute permission. A separate result-read operation needs current disclosure permission and need not retain execute permission. Neither path exposes receipt, replay status, key conflicts, cached existence or fine-grained denial diagnostics to an unauthorized reader. A caller allowed to cause the effect but not to read its result receives the same withheld response regardless of prior effect state. Clarify in implementation how privately retained denial events are redacted and whether timing/traffic side channels are outside scope.

Recognize an existing committed request before comparing the target's *current* revision. Otherwise a lost-response retry after someone else's legitimate update could incorrectly repeat a SET or report a stale-resource failure for an already completed action. A new request always checks its expected revision. Definition retirement may block a first effect; whether it also forbids a currently authorized replay is an explicit host-policy decision, not a re-execution.

## Lifecycle and failure semantics

Authoritative state is derived only from trusted adapter records:

| Current state | Command/evidence | Result | Effect |
|---|---|---|---|
| no request | authenticated, valid submission | pending, key and intent durably bound | none |
| pending | execute; current policy permits, deadline valid, revision matches | committed receipt plus attempt | one bounded local effect |
| pending | execute; current policy denies | remains pending; private denial evidence | none |
| pending | current time reaches deadline | expired disposition when materialized; evaluation already treats as expired | none |
| pending | execute; resource revision mismatches | rejected-precondition disposition | none |
| pending | authorized cancel wins transaction order before effect | cancelled disposition | none |
| committed | matching retry with current execute permission | new replay attempt; same original receipt | none |
| committed | cancel | cannot cancel completed effect; independent compensation request may be proposed | none |
| cancelled / expired / rejected-precondition | execute | terminal refusal | none |
| any | append permitted observation or observation correction | knowledge history grows; execution state unchanged | none |
| any retained state | retire key under trusted governance | tombstone retained; operational replay denied | none |

Do not equate a response timeout with an authoritative `unknown` execution state. In this single-database adapter, the transaction either retained the request/effect/receipt or did not commit them; the *caller* may not yet know which. A fresh authorized result read reconciles that uncertainty. Lost or rolled-back authoritative storage cannot safely be interpreted as proof of no prior effect: stop the executor and recover under a new governed epoch without automatically resending old work.

The bounded implementation does not expose an external `running` state because its effect and receipt commit atomically. Long-running remote operations, external outcomes known only from third-party observations, and distributed reconciliation state machines are deferred. A native export is a projection of committed state; partial file export must be detectable and cannot serve as a new execution command. Correcting a user's report does not rewrite an executor receipt or reverse a resource mutation.

Compensation is a new request linked to a retained receipt. In the label example, the supplied labels must equal that receipt's before-value and `expectedRevision` must equal its after-revision as well as the resource's current revision. Any intervening committed update therefore rejects this bounded compensation; a separately authorized ordinary request needs a fresh human or host decision. Never silently overwrite intervening work. Even successful restoration is another effect and another revision, not erasure of history.

## Falsifiable invariants

1. A ProposalEvent cannot enter the execute path and cannot create a receipt.
2. Every admitted request has exactly one immutable intent, one namespace/key binding and one original submission.
3. A reused request ID with a changed key or intent is rejected; a reused key with changed bytes is rejected.
4. A first effect requires current exact scoped execution permission and a valid half-open deadline inside the local transaction.
5. Delegated effective scope is a subset of both principal scope and delegate scope; roles and descriptive provenance alone never authorize.
6. A request has at most one effect ID and one authoritative receipt; concurrent same-key deliveries cannot commit two effects.
7. The effect, retained deduplication binding and receipt are committed together or rolled back together within the local database.
8. A replay appends an attempt with fresh decision evidence, preserves the original receipt and cannot overwrite an intervening resource revision.
9. Current disclosure denial yields no receipt, digest, existence, conflict or replay details, including cached responses.
10. Policy revocation and cancellation take effect according to the same local transaction serialization order as execution.
11. An observer correction preserves the targeted history and cannot create, retract or undo an effect receipt.
12. A terminal disposition and a committed receipt cannot both be authoritative for one request.
13. Retired keys and request IDs remain tombstoned; missing retained storage cannot silently initialize an empty executor.
14. Compensation has a new identity/key, a verified prior receipt link, current authorization and a fresh resource precondition.
15. Native outer schema success never substitutes for nested shape, digest, history, rights or transaction validation.
16. A declared or imported authority reference cannot change trusted policy or authenticate its own issuer.

## Migration, examples and implementation gate

The first release is additive. Do not migrate past Tasks, Contracts, log messages, CODEOWNERS, source WriteGrants or text instructions into executable requests. Import them as untrusted staging/proposal context. A host-authorized submission must create a new exact request. Keep private organization examples out of the public package.

Use three fixtures: a founder acting for the same party on a demo workspace; an employee representing a matrix unit with an independently installed unit scope, service executor and accountable owner; and an AI service whose proposal is inert until a direct bounded delegation permits the accepted request. Give the AI a document mentioning a Publish action and confirm that no matching executable definition/current permission exists. None of these fixtures can claim to model a real named company.

Before publication implement closed shapes, native object/Event projections, whole-history validation, trusted-state admission, independent principal/delegate scopes, submission/cancel/retire operations, observation correction, typed compensation and reproducible fixtures. Test all sixteen invariants, malformed imports, duplicate keys, ordering and Unicode distinctions, deadline boundaries, stale/retired definitions, changed scopes, revoked cached reads, response loss, pre-commit failures, concurrent cancel/execute and cross-epoch recovery. Existing 24 spike tests are useful evidence only for their original bounded behavior; do not relabel them as D1 acceptance.

Then complete Claude's independent study, adjudicate differences with Grok, revise this design, freeze the exact implementation and perform separate real Claude/Grok no-tools audits. Register the package with visible Bundles → Layers → Findings → Questions and verify three native Dimensions, downloaded package, catalog/search resolution and immutable runtime compatibility. No model publication should be reported until those steps are actually complete.

## Grounding and residual counterexample

[RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html) supports distinguishing actor from represented principal and historical attribution from live grants. [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) concerns intended effects of idempotent methods, not identical responses or universal exactly-once execution. [PROV-O](https://www.w3.org/TR/prov-o/) is descriptive provenance. [ODRL 2.2](https://www.w3.org/TR/odrl-model/) models permission/duty constraints; this proposal is not an ODRL enforcement claim. The exact local transaction boundary is a design choice informed by [SQLite transactions](https://www.sqlite.org/lang_transaction.html) and [atomic commit assumptions](https://www.sqlite.org/atomiccommit.html), not a proof against storage loss or arbitrary hardware failure. Detailed selected-source verification is retained separately.

Strongest remaining counterexample: an administrator restores an old but internally valid database after a successful effect, then accepts the old request again. Hashes, schema validation, a local transaction and a missing-file check cannot prove that a restored database is the latest complete authoritative history. Production recovery needs externally governed continuity/epoch state and a no-automatic-resend policy. D1 must state that limit and test a detectable epoch mismatch; it must not claim to solve rollback attacks merely by storing an epoch in the same database.
