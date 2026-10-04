# EM-XCT-07 predecessor and native-runtime comparison

Evidence date: 22 September 2026. Author: Codex. This records completed comparison and provisional design alternatives. It does not represent a provider consensus, validated implementation or publication approval.

## Published predecessors

| Registry predecessor | Current runtime ID | Exact version | Runtime | Semantic relation to an action execution protocol | Decision and loss boundary |
| --- | --- | --- | --- | --- | --- |
| WM-XCT-002 | vr.wm-xct-002 | 0.3.0-research.1 | Published and installable as a research draft | Overlap on permission instruments, scope, purpose, authority and time; excludes write/execution | Semantic reference only. Retain the read/disclose model for that subject; do not present generic execution permission as its exact subtype. Imported consent would incorrectly make one basis universal. |
| WM-XCT-029 | vr.wm-xct-029 | 0.3.0-research.1 | Published and installable as a research draft | Overlap on an obligated action and observed performance; excludes execution/enforcement | Semantic reference only. Link a duty where one exists. Do not require an agreement for every action or discharge a duty merely because a command ran. |
| XCT-07 in the early enterprise analysis | EM-XCT-07 research contour | Candidate, not a release | No executable metamodel established by that candidate | Working requirements: preconditions, permission_ref, effect, idempotency_key | Retain as a research crosswalk, not as a runtime import. Free text and an unqualified permission pointer cannot supply executable validation or authenticated authority. |

The exact public specification/AGENTS/publication bytes match the canonical repository. Their SHA-256 values and runtime metadata are retained in parent-retrieval.json. Each complete specification was read, including six bundles, sixteen layers, twenty-nine findings, all questions/artifacts, thirteen function descriptions, all service layers, source inventories, coverage and adjudication. Selected source claims were independently checked; the full external source inventories were not all revalidated. Parent holds remain in force.

Both publication inventories contain spec.yaml, publication.json, AGENTS.md and index.html. Their run inventories contain research results, adjudication, normalization and research-format validation. No executable effect adapter, request replay fixture or actual action engine was found there. A synthesis validation pass confirms that research structure, not execution semantics. File inventories and reports are in source-verification.json.

## Native Vercy comparison

MMAS-Core, MMAS-Interchange, Contract and Event 2.0 drafts have been read in full; their public HTTP bytes now exactly match the local copies. These are architecture drafts, not a demonstration of current production enforcement. Event is already an independent occurrence assertion. Contract is a semantic license with purpose, scope, parties, authority, validity and duties; an API action definition is not automatically that same subject.

The native event schema already carries eventId, eventType, subjectIds, actorId, occurredAt, recordedAt, payload and provenance. The generic validator permits a subject to resolve to an object OR another existing record ID. Thus an event stream can refer back to a request-submission event and a real target object without inventing an artificial Request host solely for storage. A semantic ActionRequest identity can still be justified separately if its lifecycle requires more than a submission event; providers are asked to decide this.

The generic event payload is open and no action-state reducer is invoked by the native writer. Its runtime-model contract defines fact paths, not nested event contracts. An empty fact-path contract may correctly describe an event-only package, provided installer tests demonstrate that choice and explicitly invoke the separate event/history validator. It would be misleading to declare an unrelated fact path merely to appear supported.

The writer's local atomic directory lock and refusal to overwrite preserve individual appended records. They do not atomically commit an effect in another database, a whole sequence of events or an external operation. Event writes have no request-specific expected-head guard. A host must enforce stream completeness, admission/mastership, current authorization and optimistic concurrency in its actual transaction. Native retrieval remains a projection, not an authorization or execution endpoint.

MMAS-Interchange's semantic fingerprint sorts arrays. A command digest that binds ordered arguments must use a separate declared byte encoding and retain the exact bytes. Generic semantic identity and exact content integrity are different checks. A digest does not authenticate its author or confer permission.

## Provisional candidate alternatives for provider adjudication

| Candidate | Smallest plausible form | Independent identity and lifecycle question | Master and rights | Rejected conflation |
| --- | --- | --- | --- | --- |
| ActionContract | Versioned action-definition contract, referencing any applicable semantic license | Definition ID survives renaming; changed behavior/schema produces a new immutable revision. Is this a package definition rather than an instance master? | Domain owner and implementation registry; deployment admission separately trusted | Documentation that lists an action grants permission to execute it |
| ActionRequest | Immutable intent record associated with a submission event, plus a derived stream state | One intent differs from its delivery attempts. If eventId is used as request anchor, it must remain explicit across corrections/retries | Authenticated requester authors intent; executor owns acceptance/execution observations | A proposal, a retry and a new intended effect share an undifferentiated task status |
| AuthorityBinding | Qualified external decision reference or embedded decision observation | One evaluation has its own scope/time/version; retaining it does not keep its permission current | Trusted policy host owns decision; caller-supplied references are untrusted claims | Permission flag, role assignment or PROV relation acts as a bearer credential |
| ActionResult | Profile of native Event describing a bounded observation; optional result payload reference | Observation ID differs from effect identity; unknown is not failure; corrections append evidence | Admitted observer/master; fresh disclosure decision controls retrieval | Transport success or a corrected observation proves fulfilment or reverses a real effect |

These are provisional alternatives, not four mandatory new masters. Publication should wait for substantive independent studies and a separate frozen implementation audit. Scope can be decomposed: original declarative action/event protocol and a reversible synthetic local adapter first, credential chains, external-effect adapters and production authorization integration later. The final decision must preserve all contour requirements or name the remaining assignment explicitly.

## Problems to keep visible

WM-XCT-002 contains an unlisted-role validity-token read path beside default-deny access, and inconsistent break-glass treatment. WM-XCT-029 requires an Agreement reference in composition despite allowing duties without agreements. Neither ambiguity is resolved by copying their metadata. A model owner, record master, performer and represented principal can differ.

An action's current execution authorization, current result-disclosure authorization and past audit evidence serve different questions. A retained idempotency key must suppress duplicate effects even if the caller cannot see the original result; a disclosure denial must not imply that the effect did not happen. A new authorization observation is not a new immutable intent. Resource and policy changes must be checked at a stated transaction boundary. Unknown outcome requires reconciliation, and deleting history must not silently permit an old key again.

The shared provider brief describes five general conceptual facets. Final package coverage must use the exact enterprise protocol facets for every exported type: identity-class, direct-properties, recognition-observation, capabilities-behaviour-actions, context-evidence. These supplement the field, time and rights matrices; the brief does not override the required coverage format.
