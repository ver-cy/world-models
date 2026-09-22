# R3 supplementary adoption-document review — unchanged executable candidate

This is additional input for the SAME frozen R3 candidate, not a code revision or a new broad study. Review the complete frozen adoption documents and field tables that were previously hash-listed only. Also review the separate proposed publication addendum below, which openly records remaining limitations without changing the frozen implementation. Use no tools or external browsing. State actual method and input completeness. Do not rerun tests or claim to verify raw hashes from displayed text.

Please check that these documents do not contradict the already supplied spec/code, do not promote candidate fixture locks to publication, and clearly disclose finite capacity, external host authority/continuity, limited caller projections, remaining archive-time validation and test gaps. If any text is truncated or omitted, return INPUT INCOMPLETE naming the file/fragment. Otherwise give accept-with-explicit-limits or concrete remaining release blockers for the candidate WITH this addendum. Do not mistake an acknowledged future improvement for code that exists now. Preserve your independent judgment; no publication authority is requested from you. All content is generic/synthetic and authorized for review.

FILE README.md FRAGMENT 1/2 — 6000 characters
<fragment>
# Enterprise Action Requests

Version 0.1.0 candidate. **Not released; R1/R2 audits and subsequent corrections are retained as historical evidence. Final release disposition is in review.json.** English semantic package with a synthetic Python/SQLite reference. Two modeled objects — ActionDefinition and ActionRequest — and seven native Event profiles. The synthetic label resource, policy snapshots and storage tables are fixture infrastructure, not additional enterprise metamodels.

Use ActionDefinition to describe a governed, versioned operation with an exact parameter contract, target, precondition, effect boundary and steward. Description never grants permission. A descriptive-only definition can represent an external company operation without giving this package an execution adapter. In the reference implementation only the explicitly named synthetic ordered-label replacement can execute. It accepts no command, script, endpoint, SQL expression or remote side effect.

An ActionRequest is a durable statement of intent, independent of an occurrence or result. The host mints its ID once, outside the client intent digest. Events distinguish a submission, a delivery, a current-policy execution try, a committed effect receipt, a terminal disposition, an observer's knowledge and retirement of a retained retry key. Proposed actions remain proposals in their originating context; there is no proposal-to-execution inference.

The minimum useful adoption is one descriptive definition, one accountable steward and its parameter-document reference. Executable adoption additionally requires a trusted host, an isolated local store, explicit identities, scopes, resource version, deadline, disclosure rules and retained evidence. No ERP, HRIS or agent platform is required.

## Reference use

Python 3.12 and jsonschema 4.26.0 were selected for the fixture. Install the declared dependency in an isolated environment. `python test_action.py` checks the source modules. `python build_bundle.py` regenerates the standalone companion. `python action_bundle.py PATH_TO_EXPORT` checks a complete export. The bundle and sibling `action.schema.json` must be pinned as a unit by the host; neither proves its own trusted origin.

`Executor.create` creates a fresh test store exclusively. Reopen with its separately retained epoch. `add_definition`, `set_policy`, `add_resource`, `retire_definition`, `retire_key` and `snapshot` are **trusted fixture administration**, never endpoints for untrusted callers. A host must verify issuer standing and the referenced basis before admitting policy, authenticate the actor and supply trustworthy monotonic time. Fixture Pins have deterministic invented preimages; they are not external credentials or verified mandates.

`dispatch(wire_json, retry_key, authenticated_actor, host_time)` admits and tries an intent. Initial admission requires submit permission; each attempt requires current execute permission. `lookup`, `cancel` and `observe` apply current disclosure/action scopes. Do not accept authenticated_actor, host_time or `_fault` directly from an untrusted request. The reference has no login, signing, identity-proof, network server or production authorization integration.

Build an example with `fixtures.fixture(path, 'startup')`, `'matrix'` or `'ai-service'`; all are invented organizations. The latter two use direct representation by a distinct actor. They do not assert AI subjecthood. The host is responsible for legitimate principal identity and authority outside this fixture.

## Limits that affect adoption

This release is a bounded reference, not an exactly-once distributed executor. Its only effect is replacing a list in the same SQLite transaction that retains the request, revision and receipt. SQLite/OS/storage guarantees, privileged file integrity and host isolation are assumptions. Process rollback and independent connections are tested; hardware power failure is not.

A coherent old database has the same epoch and valid hashes. The restore-limit test deliberately demonstrates that it can be replayed. **After recovery or uncertain continuity, stop dispatch and reconcile against a trusted external latest-history anchor; never automatically resend merely because the local database says absent.** No external continuity service ships here. Likewise, a new key is a new intent, so automatic key replacement after a lost response can duplicate a business effect.

All export contents are privileged evidence. Native records and manifests do not enforce read rights. Serve them only through host-controlled projections. `validate_snapshot` and `verify_export` establish internal consistency and file closure relative to the supplied cut, not authenticity, authority, completeness against the world, or the latest cut. Native outer schemas alone do not validate nested action meaning.

The package does not implement delegation chains, impersonation, use counters, remote effects, durable distributed sagas, receipts from third parties, arbitrary descriptive-action invocation, operational credentials, legal mandate validation, force cancellation of an already committed effect, erasure, per-field disclosure, or production history restoration. Retired keys retain the complete immutable intent and receipt in this fixture; this is not a compliant deletion mechanism.


R2 adds atomic 10,000-row capacity bounds, a reserved final global policy revocation, complete operation replay, and portable record filenames. At capacity, never replace a retry key or silently start a new store. Same-pin compensation is unavailable after definition retirement. An interrupted export with a torn file needs a fresh directory; between-files interruption can resume the exact cut. Test installations retain the mandatory snapshot and manifest inside the Dimension and label the model lock candidate/simulationOnly.

The global event limit can be exhausted by a caller holding even one current right; host rate/admission limits are m
</fragment>
END README.md FRAGMENT 1/2

FILE README.md FRAGMENT 2/2 — 806 characters
<fragment>
andatory and are not implemented here. Lifetime capacity is at most about 3,333 pending submissions or 2,500 first commits before other Events. Caller event projections omit global counters; privileged archives retain them. Each new test installation includes all adoption documentation and requirements (nine pinned files).

## Package and review state

See `model-spec.md`, `model-fields.md`, `whole-object-coverage.yaml`, `mastership-and-rights.yaml`, `composition.yaml`, `crosswalk.json`, `invariants.md`, `migration.md` and the executable sources. Frozen reviewer input and exact acceptance reports must accompany the eventual release. D1 and the earlier 24-test transaction / 14-negative shape experiments remain separate historical research evidence; they are not acceptance of this implementation.

</fragment>
END README.md FRAGMENT 2/2

FILE model-spec.md FRAGMENT 1/4 — 6000 characters
<fragment>
# Semantic contract

The logical model does not depend on Python, JSON, SQLite or the native file layout. Version 0.1.0 selects a bounded binding, not universal execution semantics. Both independent research studies and their S1 amendments informed this D2 selection. Descriptive-only definitions, host-minted request IDs and the precise implementation are Codex choices revised after the frozen R1 and R2 audits. Audit-round evidence records the review state at its capture; final release disposition is separate in review.json.

## Identity and lifecycle

ActionDefinition identity is `definitionId` within a Dimension's governed namespace. Each `version` is an immutable semantic revision with a full-content digest. Renaming changes the revision, not the stable object. The same ID/version with changed content is rejected. A version has a half-open validity interval. Retirement is a monotonic host-governance overlay recorded by control sequence; it never edits the retained definition body and cannot silently reactivate. A new revision can be added. A definition has a steward and a declared master; fixture admission is a host decision, not validation of their real-world standing.

Descriptive-only definitions pin an external parameter-contract document and identify their target, preconditions and intended external effect in text. The document is not fetched or interpreted. Such definitions can be cataloged as company knowledge but cannot enter the reference executor. Executable definitions use the closed labels contract, synthetic resource type, fixed precondition/effect identifiers and local adapter. Free text never changes that operation.

ActionRequest identity is a host-minted `requestId`. It has exactly one immutable intent and one submission event. The retained key slot is `(store/Dimension, authenticated actor, exact retry key)`; the stored key hash excludes no actor information. The store supplies Dimension isolation. Intent includes the dimension, exact definition pin, resource and expected revision, ordered labels, actor/principal, purpose, audience, deadline and optional compensation receipt. It contains no request ID, decision, receipt or current rights. Server-minted IDs therefore remain recoverable when the first response is lost.

The semantic state is reconstructed from events: pending → committed, cancelled, expired or rejected-precondition. Only pending can acquire a terminal state. A current-policy denial leaves it pending. Expiry is materialized on a dispatch/cancel try at `now >= expiresAt`; passive lookup can still return pending after the deadline and must not be read as permission to execute. Committed requests never become expired. Native object state remains `active`: native existence and execution state are different concepts. Key retirement is an orthogonal retained-key marker permitted only after a terminal state.

Every admitted dispatch and retained replay with at least one current applicable right retains a delivery and a current-policy try, including terminal replay. A caller with no current applicable rights cannot grow the event log; administrative control sequence still advances for a completed read/refusal transaction. A malformed body, unauthorized new submission, conflicting key or retired key is not admitted as a delivery event. Transport telemetry outside this boundary is external. Therefore delivery count, try count and effect count differ. Cancellation and observation have their own tries without fabricated transport-delivery events. Each effect has one receipt Event; at most one effect belongs to a request. Caller receipt and observation responses are projections, not complete Event records: they omit global sequence and controlSequence. Full counters remain only in privileged snapshot/native evidence. A response projection must not be passed off as a schema-valid native Event.

## Authority and confidentiality

The host's fixture policy is a list of closed direct-representation/self rules. Each records actor, principal, mode, issuer, issuer-standing evidence and external basis. The basis is a host-owned reference snapshot; this package does not create a second mandate registry or claim exact conformance to a WM-XCT-001 record schema. Source WriteGrant, source precedence, stewardship duties, function/capability descriptions and obligation claims never become execution permission.

For one rule, both principalScope and delegateScope must independently contain the exact Dimension, full definition pin, resource, purpose, audience, current time and requested operation. A permission split across different rules is not combined into one valid intersection. No wildcards, role inference, chains, implicit audience, or use counters exist. The immutable request does not freeze policy: each try retains the then-current policy revision, matched rule digests, definition availability and decision. The host supplies verified policies and issuer evidence; the code checks their declared exact scopes, not their external truth.

Current read permission is independent of execute. A caller without current read receives exactly `{"status":"withheld"}` for successful execution, denial, malformed input, absent key, conflict, retired key and supported internal error paths. The guarantee covers response shape/content, not constant-time behavior, transport status, host logs or system outages. A conflict requires read permission for both the old intent and proposed context before returning `key-conflict`. A current read grant can inspect a receipt after execute is revoked. A readable denied dispatch reports current-execution-denied together with retained requestState, requestId, intentDigest and any prior receipt. Pending denial is therefore distinguishable from a committed result whose replay is now denied. Successful dispatch replay still requires current execute rights and definition availability; lookup remains independently governed. A retired-key lookup/dispatch returns the 
</fragment>
END model-spec.md FRAGMENT 1/4

FILE model-spec.md FRAGMENT 2/4 — 6000 characters
<fragment>
retained result with status key-retired without a new try. Observe on a retired key is withheld.

The API only retrieves a key in the authenticated actor's namespace. Cross-actor administration and organizational reporting require separately authorized projections. Reads of exported native files bypass this API and therefore require host-controlled access. Observation requires both read and observe. It records the authenticated actor's claim, never turns it into authoritative effect truth.

## Effects, cancellation and correction

Request admission, policy selection, definition availability, cancellation, key binding, resource revision, effect and receipt share `BEGIN IMMEDIATE` serialization in one SQLite database. Resource updates are append-only revisions. Expected revision is checked before a first effect; a replay checks the retained intent/key first and cannot reapply after intervening work. Injected failures before effect and between effect and receipt roll back the whole transaction. A simulated response loss occurs after commit and is resolved using the same key. No test simulates storage hardware failure.

Cancellation and execution contend for the same lock and can produce only one terminal outcome. Cancel does not undo a committed effect. Compensation is a new intent/key/request referencing a retained receipt. It requires the same actor, principal, purpose, audience, Dimension, definition and resource; the original before-labels; and the current revision equal to the original after-revision. An intervening update rejects compensation, even when labels happen to look equal. Retiring or expiring the exact definition also blocks same-pin compensation, even if that effect once succeeded. Cross-version or emergency compensation is not implemented. The narrow same-actor compensation rule can be widened only by an explicitly versioned and reviewed host contract.

An observation correction references one earlier observation by the same observer on the same request. A predecessor can have only one direct correction, producing a linear correction chain. Another independent observation by that same actor can coexist. A different observer identity cannot access this actor-scoped key through the supplied API. Corrections never replace receipts, delete predecessors, cancel requests or modify labels. Claims `caller-unknown`, `caller-observed-success` and `caller-observed-failure` describe observer knowledge, not executor states.

## Byte contract and bounded representation

The normative intent/definition/rule digest is SHA-256 of the reference Python encoding: sorted object keys by Unicode code point, compact separators, unescaped non-ASCII UTF-8, no BOM, no whitespace, ordered arrays retained, no Unicode normalization. It is explicitly **not RFC 8785 JCS**. Raw-file hashes are separate. Duplicate JSON keys, floating-point literals, NaN/infinities, invalid UTF-8 and unpaired surrogates are rejected; integers must be real Python ints within ±(2^53−1), never bools.

An individual input is at most 128 KiB, depth 24, 128 object members, 256 array entries and 4096 characters per string before tighter schema constraints. IDs use the bounded ASCII grammar; labels allow Unicode, duplicates and order, at most 32 labels of 200 characters. Empty labels and an empty list are valid opaque synthetic values; this is not a company taxonomy validator. Host times are integer UTC epoch seconds in [2000-01-01, 2100-01-01]; windows are half-open. No leap-second or subsecond semantics is implied. Snapshot collections and authoritative tables are each limited to 10,000 rows. Every transaction checks every table before commit. Overflow rolls back the whole operation, including admission, evidence, effect and control-sequence increment. Caller endpoints withhold that failure; trusted administration raises Refused. No automatic deletion, new key, new database or rollover occurs. Definitions/resources/requests/events cannot grow past their limit. Policy revisions 0 through 9,998 occupy at most 9,999 rows; the final row, revision 9,999, is reserved for an empty global-revocation policy. Once full, no further policy revision is possible; the host must preserve history and halt this fixture or arrange a separately reviewed migration. Reads remain available under current policy when only another table is full. The explicit capacity is a reference boundary, not an enterprise-scale storage design.

## Native evidence and history

Native objects carry `enterpriseActionDefinition` and `enterpriseActionRequest` facets. A request facet contains only immutable identity, intent and admission; semantic state is derived from native Event profiles. Definition versions form a native object-revision chain. Resource snapshots are synthetic fixture object revisions. Event subjects resolve to actual request/definition/resource object IDs or actual prior Event IDs, never a retry hash masquerading as an object.

Seven event profiles: Submission, Delivery, Try, Receipt, Disposition, Observation and KeyRetirement. Event issuer is the trusted host; request actor/principal and observation observer remain separately explicit. `recordedAt` and `occurredAt` coincide for the local synthetic engine; receipt occurrence is the atomic local commit evidence, not an external system's clock. Export time is separate.

The privileged snapshot retains every definition, policy revision, resource revision, request and event. Global control sequence orders policy changes, definition retirement, resource creation and tries, even at the same host second. Lookup and snapshot also allocate a sequence and advance the nondecreasing host clock; they are serialized transactions, not read-only filesystem operations. The history validator checks selected policy was current at that control sequence, recomputes exact-scope decisions, replays lifecycle and effects, checks compensation/correction and compares final snapshots. Each event-bearing control sequence must conta
</fragment>
END model-spec.md FRAGMENT 2/4

FILE model-spec.md FRAGMENT 3/4 — 6000 characters
<fragment>
in one complete operation with a single request, time and issuer: submission when new, delivery plus execute try, and every required outcome; or cancel/observe try and its required outcome; or key retirement. Missing tails are refused even when derived snapshots were rewritten. Administrative mutations cannot share that sequence with an event operation. This still cannot authenticate the source or prove that an internally coherent cut is the latest.

Native exports are idempotent evidence, not a second execution master. `snapshot.json`, deterministic native files and an exact-file manifest are produced at one cut; manifest is written last. Interruption before the manifest leaves an invalid incomplete export. A between-files interruption can resume with the retained identical snapshot and directory. A torn file or changed cut requires a fresh directory; conflicting old evidence is preserved. This is not a power-loss recovery claim. Record filenames use the SHA-256 of each full case-sensitive logical ID, avoiding Windows colon/alternate-stream and case-folding names while keeping the logical ID in the payload. Extra files, subdirectories or symlinks are refused. Existing different bytes are refused. This does not claim atomicity across native files. `verify_export` checks exact closure/digests and semantic regeneration; a hostile party recomputing a complete fake archive can still forge a coherent story unless a trusted external expected root is supplied by the host.

## Dependencies and adoption

The instance graph links requests to definitions/resources and prior receipts. The specification graph has conceptual comparisons to WM-XCT-001/002/029, EFA and K1/K2, with no unverified mandatory inheritance. The delivery graph includes Python sources, standalone companion, sibling schema and reference runtime; jsonschema is an external pinned dependency. A publisher can deliver the companion without importing the full parent universes. Optional descriptive K2 alignment is never exactMatch.

Native installation uses a separately labeled new synthetic Dimension fixture and explicit companion validation. WM-XCT-040 0.1.1 currently rejects an empty runtime path map, while the pinned native runtime schema and creator/validator accept it. The test helper uses that native route, exact nine-file installation and a lock explicitly marked status candidate with simulationOnly true; it does not modify the published composer or claim its composition acceptance. Empty runtime `paths` is intentional: this package introduces object facets and Event payloads, not generic fact paths. An outer native pass cannot prove their semantics. Actual production publication and HTTP verification remain separate release gates. Generic automatic composition support for object/Event-only packages is an outstanding platform issue.

## Endpoint and supporting-evidence qualifications

Admitting a new request requires an existing synthetic-executable definition and an allowed declared purpose. Admission may occur while that definition is retired, outside its validity interval or while execute is denied; it produces pending intent, not an executable promise. A later try recomputes availability. An expired pending request is materialized as expired on a dispatch by a caller with at least one current applicable right, even when execute is denied; this creates no effect. Cancel needs cancel authority to create its terminal disposition. Denied cancel retains a try only for a current reader; denied observe retains no event. These endpoint differences are deliberate and do not imply ambient permission.

The retry hash is an unsalted digest of actor and key and is NOT a secrecy mechanism for a weak key. Host-generated unpredictable retry keys and controlled export access are external duties. Host event issuer, authenticated actor, represented principal, definition steward and policy issuer are different roles. The fixture trusts that the host verified issuer-standing and basis references; it does not require all declared policy issuers to equal the event recorder.

Native ActionDefinition state active records existence, not current availability. Native request state active is not execution state. Full policy revisions, definition retirement and the cut metadata are mandatory companion evidence. Each installation stores snapshot.json, manifest.json and exact projected record files under data/action-exports/cut-<controlSequence>/ inside the Dimension, and validates from stored readback together with native records. No native facet becomes a second execution master. Startup, matrix and AI-service fixtures exercise self versus direct representation in separate namespaces; they do not implement complete organizational or AI governance semantics.

Creation exclusively reserves a new database path. If initialization fails, a partial file may remain; do not automatically reuse, erase or reopen it as valid. The operator must preserve diagnostic evidence and deliberately select a fresh path after resolving the failure. No migration from unpublished R1 stores or exports is supported; start new synthetic fixtures while keeping R1 evidence unchanged. Archive validation is privileged and assumes host resource isolation; it is not a public arbitrary-file upload service.

## Finite lifetime and host admission control

The 10,000-row **global event** limit generally binds before requests/resources. With no later operations, each pending submission uses three Events (at most 3,333 requests) and each first commit uses four (at most 2,500 commits). Replays, observations, cancellations and retirement consume more. A current read-only caller's dispatch replay writes a delivery and denied try; an authorized observer can also grow history. The zero-rights protection does not prevent a single-right caller from exhausting this shared fixture. **The trusted host must rate-limit/admission-limit all event-producing calls across actors, reserve capacity for its needs
</fragment>
END model-spec.md FRAGMENT 3/4

FILE model-spec.md FRAGMENT 4/4 — 2193 characters
<fragment>
 and stop before exhaustion. No quotas, rollover, fairness or production availability guarantee are implemented.** Plain lookup retains no Event rows. Never delete evidence or create a new key/store to evade the bound. The final empty policy row permits global revocation but does not reserve event space.

The boundary tests directly seed valid 10,000-row histories with SQL, validate them, then exercise public operations and atomic rollback. They do not claim 10,000 public admissions, load testing or enterprise-scale performance. Current-policy selection uses binary search on ordered control sequences, and native projection uses a request-ID lookup map; no workload latency or combined-boundary throughput is asserted.

## Exact evidence bytes and installation package

Manifest and snapshot files must equal their documented file_bytes encoding, not merely parse to an equal JSON value. Native record bytes are also exact. Integer cut counters cannot be floats or booleans. The archive hash identifies one byte representation; a trusted external expected root is still required for origin/latest claims. Internal intent encoding remains Python json.dumps with ensure_ascii=False, sorted code-point keys and compact separators: quotes and backslashes are escaped, backspace/formfeed/newline/carriage-return/tab use short escapes, other U+0000–U+001F use lowercase \u00xx, and U+2028/U+2029 are raw UTF-8. Unicode is never normalized. Simultaneous schema and whole-wire limits apply: the nominal maximum of 128 rules is not a promise that any such array fits within 128 KiB.

New synthetic installations include the spec, AGENTS, runtime map, schema and companion plus README, model-spec, adoption-limits and requirements.txt. Readback verifies all nine files. Their jsonschema dependency remains an externally installed pinned dependency, not a bundled package. Candidate/simulationOnly fixture locks do not become published locks merely because tests pass. This acceptance covers one evidence cut per new Dimension; incremental multi-cut native installation and migration are not implemented. The source new-store initializer can leave a partial file on failure as already documented.

</fragment>
END model-spec.md FRAGMENT 4/4

FILE adoption-limits.md FRAGMENT 1/1 — 2749 characters
<fragment>
This release is a bounded reference, not an exactly-once distributed executor. Its only effect is replacing a list in the same SQLite transaction that retains the request, revision and receipt. SQLite/OS/storage guarantees, privileged file integrity and host isolation are assumptions. Process rollback and independent connections are tested; hardware power failure is not.

A coherent old database has the same epoch and valid hashes. The restore-limit test deliberately demonstrates that it can be replayed. **After recovery or uncertain continuity, stop dispatch and reconcile against a trusted external latest-history anchor; never automatically resend merely because the local database says absent.** No external continuity service ships here. Likewise, a new key is a new intent, so automatic key replacement after a lost response can duplicate a business effect.

All export contents are privileged evidence. Native records and manifests do not enforce read rights. Serve them only through host-controlled projections. `validate_snapshot` and `verify_export` establish internal consistency and file closure relative to the supplied cut, not authenticity, authority, completeness against the world, or the latest cut. Native outer schemas alone do not validate nested action meaning.

The package does not implement delegation chains, impersonation, use counters, remote effects, durable distributed sagas, receipts from third parties, arbitrary descriptive-action invocation, operational credentials, legal mandate validation, force cancellation of an already committed effect, erasure, per-field disclosure, or production history restoration. Retired keys retain the complete immutable intent and receipt in this fixture; this is not a compliant deletion mechanism.


R2 adds atomic 10,000-row capacity bounds, a reserved final global policy revocation, complete operation replay, and portable record filenames. At capacity, never replace a retry key or silently start a new store. Same-pin compensation is unavailable after definition retirement. An interrupted export with a torn file needs a fresh directory; between-files interruption can resume the exact cut. Test installations retain the mandatory snapshot and manifest inside the Dimension and label the model lock candidate/simulationOnly.

The global event limit can be exhausted by a caller holding even one current right; host rate/admission limits are mandatory and are not implemented here. Lifetime capacity is at most about 3,333 pending submissions or 2,500 first commits before other Events. Caller event projections omit global counters; privileged archives retain them. Each new test installation includes all adoption documentation and requirements (nine pinned files).

</fragment>
END adoption-limits.md FRAGMENT 1/1

FILE requirements.txt FRAGMENT 1/1 — 19 characters
<fragment>
jsonschema==4.26.0

</fragment>
END requirements.txt FRAGMENT 1/1

FILE model-fields.md FRAGMENT 1/7 — 6000 characters
<fragment>
# Complete field contract

Every schema object is closed. All table fields are required; explicit null alternatives are shown. A required nullable reference preserves unknown/absent distinctly from a fabricated default. Arrays preserve supplied order, including labels and duplicates; membership semantics are explicitly documented for scopes. Sensitivity is host-governed restricted context by default; declaration catalogs may be projected publicly only with separate authority.

## ActionDefinition

Master/writer: Definition steward / trusted admitting host. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| format | `{"enum":["enterprise-action-definition/0.1.0"]}` | Exact wire format/version discriminator; unknown formats are refused. |
| definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Stable governed identity of the operation, independent of its revision. |
| version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| name | `{"type":"string","minLength":1,"maxLength":2048}` | Human-readable label; not an identity or execution instruction. |
| description | `{"type":"string","minLength":1,"maxLength":2048}` | Explanatory text; never changes the selected adapter effect or grants rights. |
| mode | `{"enum":["synthetic-executable","descriptive-only"]}` | Whether a definition is descriptive-only or admitted to the closed synthetic adapter. |
| parameterContract | `{"anyOf":[{"enum":["ordered-label-list/1"]},{"type":"object","properties":{"uri":{"type":"string","pattern":"^(urn:\|https://)[!-~]+(?![\\s\\S])","maxLength":512},"revision":{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"},"sha256":{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}},"required":["uri","revision","sha256"],"additionalProperties":false}]}` | Exact labels-contract identifier for execution, or opaque pinned external parameter document for descriptive use. |
| targetType | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Declared target class; executable definitions require the synthetic ordered-label resource. |
| precondition | `{"type":"string","minLength":1,"maxLength":2048}` | Fixed guard identifier for executable definitions; descriptive text for external-only use. |
| effectBoundary | `{"type":"string","minLength":1,"maxLength":2048}` | Fixed local effect identifier for executable definitions; descriptive text for external-only use. |
| adapter | `{"enum":["local-sqlite-ordered-labels/1","none"]}` | Only local-sqlite-ordered-labels/1 executes; none is descriptive-only. |
| validFrom | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Inclusive beginning of definition/scope validity, integer UTC epoch seconds. |
| validUntil | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive end of definition/scope validity, integer UTC epoch seconds. |
| purposes | `{"type":"array","items":{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"},"minItems":1,"maxItems":16,"uniqueItems":true}` | Exact case-sensitive allowed definition purposes; no wildcards or purpose inference. |
| authorityRequirement | `{"enum":["current-exact-principal-and-actor-scope"]}` | Explicit requirement for current exact principal and actor scope; not a grant. |
| compensation | `{"enum":["new-request-restores-before-labels-at-exact-after-revision","external-unspecified"]}` | Selected compensation contract, or external-unspecified for descriptive definitions. |
| stewardId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Accountable semantic steward asserted by the admitting host; no automatic execution authority. |
| masterId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Declared definition master; host verifies the source before admitting this snapshot. |
| legacyCrosswalk | `{"anyOf":[{"type":"object","properties":{"uri":{"type":"string","pattern":"^(urn:\|https://)[!-~]+(?![\\s\\S])","maxLength":512},"revision":{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"},"sha256":{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}},"required":["uri","revision","sha256"],"additionalProperties":false},{"type":"null"}]}` | Optional descriptive legacy alignment Pin; null means no alignment claimed. |

## ActionRequestSnapshot

Master/writer: Requesting principal for intent; host for admission and derived fields. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| keyHash | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Digest of authenticated actor ID and exact retry key within one Dimension store; retained for nonreuse. |
| intentDigest | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | SHA-256 under the bounded Python encoding of the complete immutable intent. |
| intent | `{"type":"closed object","children":"expanded below"}` | One immutable statement of requested effect and context. |
| intent.format | `{"enum":["enterprise-action-intent/0.1.0"]}` | Exact wire format/version discriminator; unknown formats are refused. |
| intent.dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Owning Dimension namespace; exact match against trusted store required. |
| intent.definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/versi
</fragment>
END model-fields.md FRAGMENT 1/7

FILE model-fields.md FRAGMENT 2/7 — 6000 characters
<fragment>
on/content hash used for this intent. |
| intent.definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Stable governed identity of the operation, independent of its revision. |
| intent.definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| intent.definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| intent.resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Existing synthetic target resource identity; no URL or executable command. |
| intent.expectedRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Required target version before the first effect; optimistic concurrency, not a timestamp. |
| intent.parameters | `{"type":"closed object","children":"expanded below"}` | Closed ordered-label payload; arbitrary action parameters are unsupported by the executor. |
| intent.parameters.labels | `{"type":"array","items":{"type":"string","maxLength":200},"minItems":0,"maxItems":32}` | Replacement list; order and duplicates are meaningful, Unicode is not normalized. |
| intent.actorId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Executor identity that must match the separately authenticated host actor. |
| intent.principalId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Party represented; distinct from actor in direct-representation mode. |
| intent.purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Exact intended use; participates in both scope checks and definition purposes. |
| intent.audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| intent.expiresAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive deadline for a first effect while pending; does not expire committed receipts. |
| intent.compensatesReceiptId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"},{"type":"null"}]}` | Optional retained prior receipt to compensate; context and revision guards apply. |
| submittedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Host admission time, integer UTC epoch seconds. |
| submissionEventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Exactly one native submission Event belonging to this request. |
| state | `{"enum":["pending","committed","cancelled","expired","rejected-precondition"]}` | Derived execution state from retained history; never native object state or caller-editable intent. |
| receiptId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"},{"type":"null"}]}` | Derived committed receipt Event ID; null if no effect committed. |
| keyRetired | `{"type":"boolean"}` | Derived retained-key marker, permitted only after a terminal state. |

## Intent

Master/writer: Authenticated requesting actor; immutable after host admission. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| format | `{"enum":["enterprise-action-intent/0.1.0"]}` | Exact wire format/version discriminator; unknown formats are refused. |
| dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Owning Dimension namespace; exact match against trusted store required. |
| definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Stable governed identity of the operation, independent of its revision. |
| definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Existing synthetic target resource identity; no URL or executable command. |
| expectedRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Required target version before the first effect; optimistic concurrency, not a timestamp. |
| parameters | `{"type":"closed object","children":"expanded below"}` | Closed ordered-label payload; arbitrary action parameters are unsupported by the executor. |
| parameters.labels | `{"type":"array","items":{"type":"string","maxLength":200},"minItems":0,"maxItems":32}` | Replacement list; order and duplicates are meaningful, Unicode is not normalized. |
| actorId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Executor identity that must match the separately authenticated host actor. |
| principalId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Party represented; distinct from actor in direct-representation mode. |
| purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Exact intended use; participates in both scope checks and definition purposes. |
| audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| expiresAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Ex
</fragment>
END model-fields.md FRAGMENT 2/7

FILE model-fields.md FRAGMENT 3/7 — 6000 characters
<fragment>
clusive deadline for a first effect while pending; does not expire committed receipts. |
| compensatesReceiptId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"},{"type":"null"}]}` | Optional retained prior receipt to compensate; context and revision guards apply. |

## submission Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["submission"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.intentDigest | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | SHA-256 under the bounded Python encoding of the complete immutable intent. |

## delivery Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["delivery"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.intentDigest | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | SHA-256 under the bounded Python encoding of the complete immutable intent. |

## try Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["try"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.decision | `{"type":"closed object","children":"expanded below"}` | Fresh host scope evaluation retained outside immutable request identity. |
| payload.decision.action | `{"enum":["execute","cancel","observe"]}` | Operation being evaluated: execute, cancel or observe. |
| payload.decision.policyRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Exact current-at-control-sequence host policy snapshot used in the decision. |
| payload.decision.allowed | `{"type":"boolean"}` | Computed scope result, additionally requiring definition availability for execute. |
| payload.decision.matchedRuleDigests | `{"type":"array","items":{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"},"minItems":0,"maxItems":128,"uniqueItems":true}` | Exact matching complete rule digests; one rule must contain both scopes. |
| payload.decision.definitionAvailable | `{"type":"boolean"}` | Ho
</fragment>
END model-fields.md FRAGMENT 3/7

FILE model-fields.md FRAGMENT 4/7 — 6000 characters
<fragment>
st-computed definition validity/retirement status at this try. |

## receipt Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["receipt"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| payload.definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Stable governed identity of the operation, independent of its revision. |
| payload.definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| payload.definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| payload.resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Existing synthetic target resource identity; no URL or executable command. |
| payload.beforeRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Resource revision consumed by the effect. |
| payload.afterRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Resource revision produced; exactly beforeRevision+1. |
| payload.beforeLabels | `{"type":"array","items":{"type":"string","maxLength":200},"minItems":0,"maxItems":32}` | Exact retained target list before the effect. |
| payload.afterLabels | `{"type":"array","items":{"type":"string","maxLength":200},"minItems":0,"maxItems":32}` | Exact target list after the effect, equal to request parameters. |
| payload.compensatesReceiptId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"},{"type":"null"}]}` | Optional retained prior receipt to compensate; context and revision guards apply. |
| payload.tryEventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Causal same-request/same-transaction Try Event; cannot be reused for another downstream result. |

## disposition Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["disposition"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.from | `{"enum":["pending"]}` | Disposition source must be pending. |
| payload.to | `{"enum":["cancelled","expired","rejected-precondition"]}` | Terminal target: cancelled, expired or rejected-precondition; never committed through this profile. |
| payload.reason | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Guard reason token for a disposition, or explanatory observation/correction text. |
| payload.tryEventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Causal same-request/same-transaction Try Event; cannot be reused for another downstream result. |

## observation Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za
</fragment>
END model-fields.md FRAGMENT 4/7

FILE model-fields.md FRAGMENT 5/7 — 6000 characters
<fragment>
-z0-9._:-]{2,127}(?![\\s\\S])"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["observation"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.observerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Authenticated actor whose knowledge is claimed; correction preserves the observer. |
| payload.claim | `{"enum":["caller-unknown","caller-observed-success","caller-observed-failure"]}` | Caller knowledge only; cannot alter authoritative execution state. |
| payload.reason | `{"type":"string","minLength":1,"maxLength":2048}` | Guard reason token for a disposition, or explanatory observation/correction text. |
| payload.correctsEventId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"},{"type":"null"}]}` | Optional earlier same-observer/request observation, with at most one direct correction. |
| payload.tryEventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Causal same-request/same-transaction Try Event; cannot be reused for another downstream result. |

## key-retirement Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":1,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["key-retirement"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.retained | `{"enum":[true]}` | True marker preserving the key and complete evidence; not an erasure statement. |

## Pin (supporting value, not separate model)

Master/writer: Trusted host context builder. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| uri | `{"type":"string","pattern":"^(urn:\|https://)[!-~]+(?![\\s\\S])","maxLength":512}` | Opaque exact urn/https evidence reference; not fetched, resolved or normalized here. |
| revision | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Opaque exact evidence revision; or a host sequence in auxiliary storage. |
| sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |

## DefinitionRef (supporting value, not separate model)

Master/writer: Trusted host context builder. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Stable governed identity of the operation, independent of its revision. |
| version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |

## Scope (supporting value, not separate model)

Master/writer: Trusted host context builder. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Owning Dimension namespace; exact match against trusted store required. |
| definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}
</fragment>
END model-fields.md FRAGMENT 5/7

FILE model-fields.md FRAGMENT 6/7 — 6000 characters
<fragment>
(?![\\s\\S])"}` | Stable governed identity of the operation, independent of its revision. |
| definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Existing synthetic target resource identity; no URL or executable command. |
| purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Exact intended use; participates in both scope checks and definition purposes. |
| audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| actions | `{"type":"array","items":{"enum":["submit","execute","read","cancel","observe"]},"minItems":0,"maxItems":5,"uniqueItems":true}` | Exact operation memberships inside one scope; not inherited from a role. |
| validFrom | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Inclusive beginning of definition/scope validity, integer UTC epoch seconds. |
| validUntil | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive end of definition/scope validity, integer UTC epoch seconds. |

## Rule (supporting value, not separate model)

Master/writer: Trusted host context builder. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| actorId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Executor identity that must match the separately authenticated host actor. |
| principalId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Party represented; distinct from actor in direct-representation mode. |
| mode | `{"enum":["self","direct-representation"]}` | Self requires actor==principal; direct-representation requires distinct actor/principal and forbids further delegation. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| issuerStanding | `{"type":"closed object","children":"expanded below"}` | Host-verified reference evidence that the issuer may supply this authority basis. |
| issuerStanding.uri | `{"type":"string","pattern":"^(urn:\|https://)[!-~]+(?![\\s\\S])","maxLength":512}` | Opaque exact urn/https evidence reference; not fetched, resolved or normalized here. |
| issuerStanding.revision | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Opaque exact evidence revision; or a host sequence in auxiliary storage. |
| issuerStanding.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| basis | `{"type":"closed object","children":"expanded below"}` | External host-owned mandate/control basis Pin; not a new canonical mandate record. |
| basis.uri | `{"type":"string","pattern":"^(urn:\|https://)[!-~]+(?![\\s\\S])","maxLength":512}` | Opaque exact urn/https evidence reference; not fetched, resolved or normalized here. |
| basis.revision | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Opaque exact evidence revision; or a host sequence in auxiliary storage. |
| basis.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| principalScope | `{"type":"closed object","children":"expanded below"}` | Complete scope held by the principal and verified by the host. |
| principalScope.dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Owning Dimension namespace; exact match against trusted store required. |
| principalScope.definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| principalScope.definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Stable governed identity of the operation, independent of its revision. |
| principalScope.definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| principalScope.definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| principalScope.resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Existing synthetic target resource identity; no URL or executable command. |
| principalScope.purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Exact intended use; participates in both scope checks and definition purposes. |
| principalScope.audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| principalScope.actions | `{"type":"array","items":{"enum":["submit","execute","read","cancel","observe"]},"minItems":0,"maxItems":5,"uniqueItems":true}` | Exact operation memberships inside one scope; not inherited from a role. |
| principalScope.validFrom | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Inclusive beginning of definition/scope validity, integer UTC epoch seconds. |
| principalScope.validUntil | `{"type":"int
</fragment>
END model-fields.md FRAGMENT 6/7

FILE model-fields.md FRAGMENT 7/7 — 2802 characters
<fragment>
eger","minimum":946684800,"maximum":4102444800}` | Exclusive end of definition/scope validity, integer UTC epoch seconds. |
| delegateScope | `{"type":"closed object","children":"expanded below"}` | Complete scope permitted to this actor; must independently contain the request context. |
| delegateScope.dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Owning Dimension namespace; exact match against trusted store required. |
| delegateScope.definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| delegateScope.definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Stable governed identity of the operation, independent of its revision. |
| delegateScope.definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| delegateScope.definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}(?![\\s\\S])"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| delegateScope.resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Existing synthetic target resource identity; no URL or executable command. |
| delegateScope.purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}(?![\\s\\S])"}` | Exact intended use; participates in both scope checks and definition purposes. |
| delegateScope.audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}(?![\\s\\S])"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| delegateScope.actions | `{"type":"array","items":{"enum":["submit","execute","read","cancel","observe"]},"minItems":0,"maxItems":5,"uniqueItems":true}` | Exact operation memberships inside one scope; not inherited from a role. |
| delegateScope.validFrom | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Inclusive beginning of definition/scope validity, integer UTC epoch seconds. |
| delegateScope.validUntil | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive end of definition/scope validity, integer UTC epoch seconds. |

Derived fields: requestId/keyHash/intentDigest/submissionEventId are minted/calculated at admission; state/receiptId/keyRetired are projections; all event IDs/sequences/times/decision/receipt fields are generated from the trusted host transaction. Intent fields and definition content are asserted inputs subject to validation. No physical units apply except UTC epoch-second time. Full guards, conflict rules and byte identity are in model-spec.md.

</fragment>
END model-fields.md FRAGMENT 7/7

FILE bindings/native-v3.md FRAGMENT 1/1 — 2092 characters
<fragment>
# Native binding

Install spec.json, AGENTS.md, runtime-model.reference.json, action.schema.json, action_bundle.py, README.md, model-spec.md, adoption-limits.md and requirements.txt using install_fixture.py for NEW synthetic Dimensions. WM-XCT-040 0.1.1 rejects empty fact paths; the pinned native schema/creator/validator allow object/Event-only bindings. This explicit fixture does not change that published composer or claim its composition acceptance. The single companion contains the engine, history validator and native exporter assembled from three source modules; only jsonschema is an external Python dependency. The empty fact-path map is intentional. The fixture lock says status candidate and simulationOnly true. It never labels this unpublished candidate as published. Generic composer support remains an outstanding platform issue.

Read back installed bytes and run the installed companion, then append exported objects before events in sequence through the native writer. Store the complete export under data/action-exports/cut-<controlSequence>/ inside the Dimension. Read snapshot.json and manifest.json back from that directory, verify exact closure, then validate the native Dimension AND compare every stored native record against the stored companion snapshot. Policy and definition-retirement evidence in the companion cut is mandatory; native object state alone does not indicate availability. Hashed record filenames preserve logical IDs inside the records. Expected record IDs/subjects resolve to actual native objects or preceding events. The installed tests demonstrate three fresh organizational/commercial-company Dimensions, not a migration of existing company data.

The native store is an evidence projection. It has no authority to execute, edit or reconcile the master database. Host projections must protect its contents. Instance namespace, master and current expected release digest are supplied by the host. Failed nested validation cannot be waived by a valid outer record. A restored or copied valid native archive is not an execution resume token.

</fragment>
END bindings/native-v3.md FRAGMENT 1/1

FILE publication-addendum-r3.md FRAGMENT 1/2 — 6000 characters
<fragment>
# Publication and adoption qualifications — frozen R3 candidate

This addendum makes the reviewed reference's remaining limits explicit. It does not change its code, schema, semantic fields, fixture installer or frozen test reports. Original candidate files retain their capture-time wording; the eventual `profile-manifest.json` establishes published lifecycle and the eventual `review.json` establishes release disposition. A candidate/simulationOnly fixture lock is not publication evidence.

## Useful scope

Adopt a descriptive ActionDefinition to catalog a governed operation. Description, guidance actions and the question field named `permittedActionId` confer no execution or disclosure right. That field is a navigation reference to guidance only. Questions are host guidance with evidence requirements, not machine-verified truth or authority decisions.

The executable companion is an isolated synthetic example: replacement of ordered opaque labels in one SQLite store. It is not a production workflow/authorization service. The owner of an adopting host must independently supply authentication, legitimate principal/actor authority and issuer standing, time, disclosure, database/file isolation, rate/admission controls and recovery continuity. The finite event budget is shared across actors. Any current right holder can consume it through event-producing calls. It supports at most about 3,333 pending submissions or 2,500 first commits before other events; no quota, fair sharing or rollover exists. The final empty policy row reserves global revocation, not execution capacity.

## History and disclosure

The engine enforces a nondecreasing host clock for every transaction. Archive replay checks control order, per-table times, operation completeness, policy selection and effect consistency, but does not impose one globally monotonic recorded-time sequence across all administrative tables. A consistently rewritten snapshot with a backdated administrative row can pass. This is a known validator limit, not evidence that the engine emitted it. Neither archive validity nor matching epoch proves authenticity, latest state or safe restoration. After uncertain recovery, halt dispatch and reconcile against an external trusted latest-history anchor.

Callers receive only receipt or observation projections with global sequence/controlSequence omitted; they do not receive Submission, Delivery, Try, Disposition or KeyRetirement records through these endpoints. Those are privileged evidence requiring separate host projections. A receipt includes beforeLabels and afterLabels of the shared synthetic resource, potentially reflecting earlier work under another purpose/audience. Current request read permission in this fixture exposes that whole receipt; a production host needs an independently reviewed resource/disclosure boundary. No per-field confidentiality or cross-context noninterference is claimed.

Retired-key cancel, like lookup/dispatch, returns key-retired and retained receipt to a current reader without a new event. Observe on a retired key is withheld. Same-pin definition retirement or expiry blocks compensation. Resource revision zero is host administration; later revisions belong to the local executor's guarded effect. Native projections never become an execution master.

## Installation and evidence qualifications

The test installer copies nine frozen assets including its required adoption documents and dependency declaration. It does not itself run a scenario or produce an execution snapshot; the acceptance workflow creates the cut and stores snapshot/manifest/records inside each fresh synthetic Dimension. It tests one cut, not incremental installation or existing-Dimension migration. Published WM-XCT-040 generic composition remains unsupported for this empty fact-path binding.

The candidate fixture lock includes canonical release URLs together with candidate/simulationOnly labels and exact local hashes. Do not resolve that candidate URL and substitute returned bytes for the installed pin. Resolve a released package separately and verify its actual published digest before adoption. The nine-file fixture does not install review.json or this addendum; consult them from the complete released package, and retain them locally if offline review is needed. The installer is a test helper, not the recommended production rollout path.

The 69 source tests and the same 69 on the standalone bundle are distinct behavioral cases, not 138 independent requirements. Three native installations use the pinned toolchain and exact installed bytes. Capacity cases seed valid histories with SQL before replay/rollback tests; they do not demonstrate 10,000 public API calls or load performance. The intent half of the newline test is not independently discriminating because authentication/scope also reject those modified intents; definition/policy halves and static source analysis support the grammar correction. Generated-ID collision and cross-table backdating have no dedicated R3 tests. Neither hardware faults nor timing-channel resistance was tested.

Unit reports record Python/SQLite versions; the native report records exact source/tool pins but does not independently record runtime versions. Do not attribute an unrecorded runtime inventory to that report. The dependency declaration is jsonschema==4.26.0; it is externally installed and not bundled.

## Further work

Future pinned revisions should strengthen cross-table historical clock validation, add the missing discriminating edge tests, normalize standalone parse's oversized-integer ValueError, improve resource/event mastership wording and guidance reference naming, retain release review documents in installation, and record native runtime versions. Native multi-cut support, external continuity, real authority integration, stronger disclosure, quotas/rollover and broader action parameter/effect contracts require separate design and acceptance. EM-XCT-07 remains a pa
</fragment>
END publication-addendum-r3.md FRAGMENT 1/2

FILE publication-addendum-r3.md FRAGMENT 2/2 — 63 characters
<fragment>
rtially covered research contour after this bounded increment.

</fragment>
END publication-addendum-r3.md FRAGMENT 2/2

Input coverage: {"README.md": 2, "model-spec.md": 4, "adoption-limits.md": 1, "requirements.txt": 1, "model-fields.md": 7, "bindings/native-v3.md": 1, "publication-addendum-r3.md": 2}
Raw file hashes (not display verification): {"README.md": "5bd455c9177b093f6de4e46b272f3994223389769a428088dbb6d025c6d8f3e6", "model-spec.md": "d9dc6e635438de856f00bf55c2a5492516043b4cfd6f12461d248d24b1cda7e2", "adoption-limits.md": "535a4cda8bee98257bfbb08647e3a6b258a9f33b690590671aa3b067bfc3084f", "requirements.txt": "756cc9e506ae4ee1a6f6c0507088b5cfc0dc8ba350fb2d2d46f1ffa72033adb6", "model-fields.md": "ccf254055f977c9e0ac34e6c5dd3db003dfccf19fc0da8804fc22bb35b4ce946", "bindings/native-v3.md": "7cc0e712ba19849f35463f0efe17fce3b374cc76e2f6af383f4a1f81f25ea99b", "publication-addendum-r3.md": "38babffe182cc9dd13f16bbd0d6d0c333644b9f0bf9f6a688a2c24e111bb0274"}
