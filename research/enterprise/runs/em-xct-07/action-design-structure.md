# D1 discovery structure and whole-object coverage

Companion to `action-contract-provisional.md`. These are proposed research/implementation routes, not already shipped functions. No provider has approved D1. Four Bundles, eight Layers and twenty-four Findings give each question a retained artifact and a bounded next action. They become catalog structure only after implementation and audit.

## Bundle 1 — Intent and identity

### Layer 1 — Definition and proposal

| Finding | Questions | Retained artifact | Proposed action |
|---|---|---|---|
| F01 Exact action meaning | Which immutable definition revision governs the parameters? Does the host resolve those exact bytes? | Versioned definition reference, digest and closed parameter schema. | Resolve the pin; reject a digest mismatch or unsupported operation before admission. |
| F02 Proposal has no execution power | Who suggested the operation? Has separate authenticated submission occurred? | Advisory ProposalEvent and explicit later request context link. | Record the suggestion; require host submission and current execution permission before any effect. |
| F03 Definition lifecycle | Is the definition admitted for a first effect now? What happens after retirement? | Trusted definition availability record and versioned retirement policy. | Deny new first effects under a retired definition; evaluate replay/read under current policy without re-execution. |

### Layer 2 — Request and exact content

| Finding | Questions | Retained artifact | Proposed action |
|---|---|---|---|
| F04 Intended-operation identity | Is this the same intended operation? Can it be referenced while pending and after completion? | Immutable ActionRequest object and original SubmissionEvent. | Admit one independent identity; require a new identity for a semantic change. |
| F05 Exact ordered parameters | Does reordering labels alter intent? Which byte rules prevent ambiguous hashes? | Canonical intent bytes, algorithm version and digest. | Validate closed input; preserve arrays and Unicode code points; compare both bytes and hash. |
| F06 Immutable versus current context | Which values describe intent? Which must be refreshed on each attempt? | Intent, separate current host decisions and unchanged original admission. | Exclude current decision IDs/times from retry identity; bind actor, principal, target, definition and purpose exactly. |

## Bundle 2 — Representation and current permission

### Layer 3 — Roles and scope

| Finding | Questions | Retained artifact | Proposed action |
|---|---|---|---|
| F07 Actor and principal | Who acts and on whose behalf? Can a startup use the same party for both? | Distinct actorId/principalId and trusted session binding. | Match authenticated fixture actor; permit equal roles without manufacturing another party. |
| F08 Bounded direct delegation | Does the principal currently have the scope? Is delegated scope no wider? | Separate principal/delegate scope records, verified basis reference where used and decision evidence. | Intersect action/resource/purpose/time/audience/Dimension scope; reject unsupported chains and impersonation. |
| F09 Issuer and accountability | Who may install scope? Does an owner or title itself authorize execution? | Trusted fixture governor, issuer standing and accountable-party reference. | Accept policy changes through the trusted host; retain accountability separately from permissions. |

### Layer 4 — Execution, disclosure and revocation

| Finding | Questions | Retained artifact | Proposed action |
|---|---|---|---|
| F10 Current execution decision | Which policy revision permitted this attempt? Was it current inside the transaction? | AttemptEvent with nonportable decision evidence and evaluation time. | Re-evaluate after acquiring the write transaction; serialize policy changes with effect commit. |
| F11 Result disclosure | May the caller see a cached receipt now? Do errors expose existence or conflicts? | Current read decision and sanitized outward response contract. | Check disclosure before revealing receipt, replay, digest or detailed errors; test identical withheld responses across internal states. |
| F12 Revocation and known time | Did revocation commit before execution? Is remote freshness actually guaranteed? | Local transaction order, policy revision and host freshness limits. | Deny under current local policy; preserve past receipts; do not claim knowledge of unobserved remote revocation. |

## Bundle 3 — Execution and recovery

### Layer 5 — Retry and atomic local effect

| Finding | Questions | Retained artifact | Proposed action |
|---|---|---|---|
| F13 Namespace and key retention | Where is the key meaningful? Can a retired key or request ID be reused? | Durable key-to-intent mapping and tombstones. | Enforce key and request-ID uniqueness; stop on missing state or unexpected executor epoch. |
| F14 Concurrent delivery | Can two attempts commit two effects? Does retry preserve the original receipt? | Transactional effect, receipt and attempt log with unique constraints. | Serialize independent connections; commit one effect, retain one receipt and distinct attempts. |
| F15 Resource version | Is this a first effect or a retry after later work? Does the expected revision still apply? | Original precondition, before/after revisions and retained receipt. | Locate a committed request before checking current revision; require compare-and-set for a new effect. |

### Layer 6 — Cancellation, uncertain response and compensation

| Finding | Questions | Retained artifact | Proposed action |
|---|---|---|---|
| F16 Cancellation race | Did cancellation win before effect commit? Is the request terminal? | Authorized DispositionEvent in the execution transaction order. | Cancel pending work; reject contradictory receipt/disposition histories and cancellation after effect. |
| F17 Lost response | Did the transaction commit despite timeout? Is absent state actually the latest complete history? | Original receipt, caller observation and governed continuity evidence. | Perform a fresh authorized read; preserve unknown caller knowledge until reconciled; stop after untrusted restoration. |
| F18 Compensation | Which receipt is being compensated? Has any intervening update occurred? | New request/key, typed receipt link, before-value and exact prior after-revision precondition. | Re-authorize a new operation; reject cross-resource links, forged receipts and intervening revisions. |

## Bundle 4 — Evidence and adoption

### Layer 7 — Observation and whole history

| Finding | Questions | Retained artifact | Proposed action |
|---|---|---|---|
| F19 Receipt versus observation | Is this a committed receipt or someone's report? Does performance prove duty fulfilment? | Distinct ReceiptEvent and OutcomeObservationEvent with issuer and evidence. | Derive execution state from trusted receipts/dispositions; leave obligation fulfilment to its own process. |
| F20 Corrected knowledge | Which earlier observation is corrected, by whom and when? Does correction alter the effect? | Append-only same-observer/request chain with retained predecessors. | Validate the full chain; append a correction without replacing observations or receipts. |
| F21 Consistent history | Are subjects, pins, attempts, outcomes and clocks consistent? What proves current completeness? | Retained native records plus semantic validation report and host continuity context. | Reject orphaned, branched, duplicated or contradictory histories; distinguish archive validity from admission and completeness. |

### Layer 8 — Native binding and migration

| Finding | Questions | Retained artifact | Proposed action |
|---|---|---|---|
| F22 Native representation | Which record is the request object? Which occurrences are actual Events? | Object/Event projections, nested schemas and export manifest. | Validate outer and nested/history contracts; avoid a fake aggregate host or duplicate request-state fact. |
| F23 Adoption and legacy import | Can a Task, Contract, WriteGrant or document become executable? Who authorized conversion? | Staging/proposal mapping and explicit host submission. | Import as untrusted context; never infer action authority from labels, source priority or past acts. |
| F24 Release and recovery limits | Which tests ran? What must the real host supply, and can an old database be detected? | Frozen pins, native fixtures, independent audits and continuity runbook. | Publish the implemented audited boundary; retain restore/epoch limits and package verification evidence. |

## Five exact facets for each proposed record type

These are the protocol's exact keys. Generic lifecycle or governance headings do not replace them. Embedded values remain parts of their records; any additionally exported type needs equally explicit coverage.

| Type | identity-class | direct-properties | recognition-observation | capabilities-behaviour-actions | context-evidence |
|---|---|---|---|---|---|
| ActionRequest | Independent immutable intended operation; unique requestId/key; native object, not an occurrence or grant. | Definition pin, actor/principal, namespace, target/revision, purpose/deadline, ordered parameters and optional links. | Exact admitted canonical bytes and submission; execution state derived from trusted events. | Submit once, attempt, cancel pending work, authorized read, compensate by new request; no intent edit. | Host policy, external definition/basis, admission, resource/receipt history and retention/continuity limits. |
| ProposalEvent | Advisory occurrence identified by eventId; no request or permission implied. | Proposed definition, target, purpose, parameters, suggested principal, proposer and clocks. | Recorded suggestion with source and optional predecessor; never execution evidence. | Record or supersede through a new advisory event; submission is a separate operation. | Source material, potential principal and later request link; document instructions are untrusted context. |
| SubmissionEvent | Original admission occurrence for one immutable request; exactly one per request. | Request ID, intent digest, admitted definition pin and trusted submission instant. | Matches retained request and admitting host; duplicate imports do not make new submissions. | Record authenticated admission; cannot itself produce the resource effect. | Trusted host, canonical bytes and submission policy; archive shape alone proves no admission. |
| AttemptEvent | One execution/replay occurrence for an admitted request; eventId, distinct from effect ID. | Operation, outcome, fresh decision evidence/time and request pin. | Distinguished denied/stale/replayed/committed outcomes in retained history; private diagnostics stay private. | Attempt under current scope or replay without another effect; no widening or grant issuance. | Transaction order, current policy, session, definition availability, receipt and disclosure rules. |
| ReceiptEvent | Unique authoritative receipt of the local effect; native Event plus separate effect identity. | Before/after revisions and ordered values, request/definition pins and successful attempt. | Trusted through the retained transaction; historical value is not current resource state. | Authorized read/replay and compensation reference; no overwrite or effect undo. | Executor, transaction boundary, precondition, retry history and bounded storage assumptions. |
| DispositionEvent | Terminal no-effect disposition for pending request; native Event. | Cancel/expire/precondition reason, request pin, instant and current governance decision. | Valid only without receipt and according to serialized lifecycle; deadline acts before materialization. | Cancel, materialize expiry or reject precondition; cannot cancel completed effect. | Trusted host, deadline/resource evidence, authorization and execution race order. |
| OutcomeObservationEvent | Observer's knowledge assertion, distinct from effect and execution state. | Reported unknown/success/failure, evidence, observer, clocks and optional corrected Event. | Retains known-at history; same-observer chain updates interpretation without erasing records. | Append permitted reports/corrections; cannot execute, grant, discharge duty or replace receipts. | Request, observer provenance, retained predecessor, evidence and admission/disclosure policy. |

## Embedded and private shapes

- **DefinitionRef / BasisRef**: versioned references, no local master identity; exact ID/revision/digest; recognized by trusted resolution; can be checked or rejected, never self-authorize; issuer/source/version form their context.
- **DecisionEvidence**: occurrence-scoped part identified by containing event and field path; exact scoped result, policy pin/time/issuer; recognized as historical check evidence; explains that attempt but cannot authorize another; trust and freshness are external context.
- **CanonicalIntent**: value contained in one request; closed immutable fields/byte algorithm; equality requires bytes as well as digest; supports validation/conflict detection, not edits; request/admission are its context.
- **DeduplicationEntry / Tombstone**: private control state keyed by namespace/key with unique request-ID binding; original pins/retention state; recognized only in trusted latest executor storage; permits lookup/refusal, not business action; continuity/recovery are required context. It is not a user-editable metamodel.

## Acceptance plan beyond the existing spike

The original 24 spike tests remain unchanged. These D1 groups need new implementation and execution; they are not passing-test claims:

1. Schema/encoding: duplicate keys, unknown fields/version, malformed IDs/refs/clocks, boolean integers, surrogates, Unicode normalization distinctions, array order/duplicates and exact definition pins.
2. Identity: changed intent/same key; same request ID/new key; admission survives retry; inert proposals; a true native request object.
3. Authority: principal/delegate scope containment, wrong issuer/audience/Dimension/purpose, expired basis/definition, unsupported chains/impersonation, fresh decision with unchanged intent, revoked execution and separately permitted result read.
4. Disclosure: no stored-state detail for unauthorized callers; execute-only caller gets identical withheld structure for absent/pending/committed/conflicting/retired states; diagnostics stay private.
5. Lifecycle: admission without effect; denied attempt leaves pending; exact expiry boundary; concurrent cancel/execute gives one permitted terminal result; stale precondition; no post-effect cancellation.
6. Atomicity: independent connections, pre-receipt rollback, post-commit lost response, retry after intervening work, committed replay after deadline with fresh rights, busy/error handling and cleanup.
7. Evidence: wrong issuer/subject/pin, orphan receipt, duplicate effect/disposition, impossible clocks, cross-observer/request correction, retained predecessor and branches; corrections leave resource unchanged.
8. Compensation: new key/identity, real retained target, exact before-value/after-revision, cross-resource/forged/intervening targets rejected; both receipts and revision increments preserved.
9. Continuity/migration: tombstones, missing database, expected epoch mismatch, explicit inability to detect coherent rollback without an external root; proposal-only legacy import and no inferred rights.
10. Adoption: three synthetic profiles; nested/native validation; exact dependencies; downloaded package tests; substantive studies plus frozen audits; catalog structure and prior runtime preserved.
