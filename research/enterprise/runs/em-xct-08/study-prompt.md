# Independent research: Vercy EM-XCT-08 — Sources, bindings and synchronization

Provide an independent, substantive design study in English for a public Vercy Enterprise metamodel. This is a research study, not a code audit or publication approval. Both independent reviewers receive this identical brief without the other's answer. All examples below are synthetic; do not use private connectors, local files, organizational records or secrets. Use public primary sources if tools are available. Distinguish actually opened source sections from prior knowledge and unverified assumptions. Do not claim to have run code. Return the study as your answer, not an external file. Start with whether this entire brief through END STUDY BRIEF is visible.

## Frozen research boundary

Help a startup and a large multi-tenant enterprise reliably represent how external source records are acquired, mapped to already governed business subjects, replayed, reconciled and checkpointed. Candidate vocabulary: SourceSystem, SourceBinding, ExtractionRun, SyncCursor, SyncConflict. These are candidates, not a mandate to create five independent object models. Recommend reuse/profile/shared contract/adapter/new/defer per candidate. A connector binding is not a Company, Person or Project; a tracker board is not automatically a new business Project. No global same-as, automatic subject merge, production connector implementation, credentials, legal compliance guarantee or distributed exactly-once claim is authorized by this scope. A bounded executable reference contract with explicit host duties can be the first increment.

Separate three graphs: business instances, specification dependencies, and package delivery. Cross-references do not require executable imports. Keep existing business subjects and source authority external. Explicitly distinguish proposal, source observation, accepted business fact and actual downstream effect. A source can be locally authentic without being the semantic master of a field.

## Existing published predecessors and comparison

Codex read the complete current WM-XCT-001 and WM-XCT-012 specifications (all structure, functions, sources, coverage and holds), plus complete Enterprise Fact Authority and Enterprise Assertion Provenance specifications. Current HTTP bytes matched local copies and runtime digests. These are reviewable drafts; their descriptive operational promises are not evidence of running engines. Their external legal/standard claims were not independently reverified wholesale for this contour.

1. Ownership / Stewardship, vr.wm-xct-001, 0.3.1-enterprise.1: https://ver.cy/models/wm-xct-001-ownership-stewardship/spec.yaml — SHA256 fa942556a3f460729db2e94b24d1efd4d33ee2e5fb0b1deed3ce040756acf474. Control standing, stewardship, delegated authority and register competence are distinct. Descriptive transfer/exclusivity functions require external ordering and authoritative operation; no source/destination checkpoint engine. Embedded metadata about the companion being absent from the runtime catalogue is stale: the live catalogue has a separate companion entry.
2. Provenance, vr.wm-xct-012, 0.3.0-research.1: https://ver.cy/models/wm-xct-012-provenance/spec.yaml — SHA256 aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5. Subject identity, byte binding, generation, activity, custody, assertion and verification verdict are distinct. Traversal continuation and lineage completeness describe a graph view, not a durably committed synchronization checkpoint. Streaming/sub-second provenance, production federation and sector-specific conformance are explicit gaps. Sources contain inherited verification holds.
3. Enterprise Fact Authority, vr.profile.enterprise-fact-authority, 0.1.0: https://ver.cy/models/wm-xct-001-ownership-stewardship/profiles/enterprise-fact-authority/0.1.0/spec.json — SHA256 cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582. Distinguishes accountable appointment, stewardship, source priority and current WriteGrant; source lineages stay separate, equal-priority conflicts retained. Full-register, host-internal serial admission has one receipt per second and external authentication/current-root duties. It is not a durable import buffer or cross-register transaction engine.
4. Enterprise Assertion Provenance, vr.profile.enterprise-assertion-provenance, 0.1.0: https://ver.cy/models/enterprise-assertion-provenance/versions/0.1.0/spec.json — SHA256 a8f41fb65aa5892c884731c9c4d06402637bf26bc55ab53a6ad9c7fbc34a44f0. Distinguishes Capture, Activity, exact external-claim account, EvidenceLink and ConfidenceAssessment. New acquisition/version/content means a new Capture. Withdrawal does not negate an external claim. It records integrity/acquisition declarations, not actual fetching/signature proof. Also bounded full-register serial admission, no durable connector engine. Empty runtime imports do not prove automatic cross-package integration.
5. Enterprise Identity 0.1.0 usage profile: https://ver.cy/models/wm-xct-036-alias-same-as-mapping/profiles/enterprise-identity/0.1.0/model-spec.md . Complete profile model specification read; its additional schema/code review is still in progress. QualifiedIdentifierAssignment differs from IdentityAssertion and its lifecycle event. SourceBinding is a frozen assertion carrier; full source-observation revision is deferred. Scope, issuer, purpose, scheme and assignment generation matter. Even equivalent-in-context has inferencePermitted=false. No merge/matching engine. This profile is associated with vr.wm-xct-036 (current parent 0.3.2-enterprise.1, archived profile semantic basis 0.3.0); it is NOT an independent runtime ID. The entire 1.45 MB current parent specification has NOT been read in this pass; do not infer whole-parent equivalence or conformance. Identity policy/host admission remain external to this new scope.

Compare these existing boundaries critically. Reuse their meanings at exact stated scope; do not inherit descriptive promises as implemented behavior. A first release can reference companions semantically without importing their full histories or one-receipt-per-second admission as the ingestion rate limit. Any adapter between contracts must be tested separately before claiming automatic integration.

## Primary approaches to compare

Compare at least three approaches: ontology/standard, actual source/connector practice, and another data-integration approach. Suggested public sources already examined in selected sections by Codex (your independent verification and alternatives welcome):
- W3C PROV-DM, Recommendation 30 April 2013, entity invalidation: https://www.w3.org/TR/prov-dm/#term-Invalidation . Invalidation is qualified to an entity, not all its real-world referents.
- Airbyte protocol, State and checkpointing: https://github.com/airbytehq/airbyte/blob/master/docs/platform/understanding-airbyte/airbyte-protocol.md . Source-emitted state alone is insufficient for resumption; destination-confirmed committed progress matters. Stream/global state and opaque source state have different constraints. Moving branch, not an immutable standard.
- Microsoft Graph delta overview, state tokens, replay and reset: https://learn.microsoft.com/en-us/graph/delta-query-overview . Tokens carry query state; replay and reset/reinitialization can occur. Expiry and deletion behavior are resource-specific; do not invent universal durations.
- Debezium PostgreSQL connector, snapshot, primary-key updates, replica identity: https://debezium.io/documentation/reference/stable/connectors/postgresql.html . Consistent snapshot/stream positions, restart semantics, delete/create key change and before-image limits matter. A transport tombstone is not business-subject death. Moving stable docs need an explicit version observation.

Do not quote paywalled unread standards or assert generic ISO conformance. Record source URL, version/date, exact section, observed/source-asserted/inference/proposal/unverified, and implications. Avoid copying source text or schemas.

## Design questions

1. Source tenant/instance identity versus connector installation, credential identity, source record key, key generation, capture and governed business subject?
2. What preserves identity across rename, board/project move, connection replacement, source restoration and key recycling? What changes require a new binding revision or source generation?
3. Mapping cardinalities, subject-kind checks, mapping issuer/purpose, ambiguity and explicit correction without silent reassignment?
4. Does source schema/configuration/mapping change invalidate a cursor, start a new epoch or require reprocessing? How to avoid silently remapping already committed data?
5. How to identify extraction attempts, logical batches and record occurrences separately; avoid conflating retry with a new acquisition?
6. What exact scope qualifies a complete snapshot: tenant, resource, query/filter, principal/visibility, partitions, schema, mapping revision and snapshot-consistency boundary?
7. Partial pagination, revoked visibility and inaccessible objects: absence, inaccessible, removed-from-scope and explicitly source-deleted must remain distinct. When can absence produce only a reconciliation candidate?
8. Opaque cursor sequence/epoch, source checkpoint emission, staging, destination durable acknowledgement, commit and rollback after process death?
9. Out-of-order delivery, old cursor reuse, stale expected head, concurrent writer fencing, source reset and lost continuity?
10. Same idempotency key/same payload versus changed payload, duplicate records and collisions across tenants/partitions/mapping revisions?
11. Partial record rejection: block commit, quarantine with durable manifest or explicitly accept loss? What does committed progress guarantee and not guarantee?
12. Mapping conflict versus competing source facts versus checkpoint/content conflicts: which has its own lifecycle and owner?
13. Historical correction, valid/source-event/observed/recorded/committed times; sequence cannot be replaced by unreliable source wall clocks.
14. Current authorization for intake, binding changes and replay; source permission is not destination permission. Revocation, disclosure and traceability of rejected attempts.
15. Sensitive raw payload, endpoint and cursor tokens: externally protected locator/digest versus opaque content. Which metadata can leak? No real secret values in model examples or logs.
16. Minimum useful local profile, extension to partitions/global state, resource budgets, retention and restart/recovery. What can a bounded SQLite reference actually prove?
17. Native Vercy V3 installation validates outer model/projection structure separately from nested semantic schema/code; a full register/receipt must not be smuggled into a fact that generic agents treat as an authoritative business field.
18. Provide at least 15 Finding → Question → Artifact → permitted Action routes and whole-object facets for EVERY proposed exported canonical and support type: identity-class, direct-properties, recognition-observation, capabilities-behaviour-actions, context-evidence.

## Synthetic acceptance cases (must disposition each)

A. Startup: Project P-1 is represented by two tracker boards; rename and move a board do not create a new Project or silently rewrite a binding.
B. International group: two source tenants both use key "42"; their records and checkpoint state stay distinct. Lexical "01" differs from "1" without an explicit scheme rule.
C. AI organization: dataset record changes generation/reuses key; old provenance stays attached to the old referent; a new capture alone does not infer identity continuity.
D. Replay identical logical batch after response loss: no duplicate effects, preserved receipt; changed payload under same key produces a conflict without overwriting prior evidence.
E. Crash before destination durable commit: cursor cannot advance. Crash after commit before response: retry returns committed result. State emission without effects is not a checkpoint.
F. Failed page or missing partition: snapshot is partial; no absence-based deletion. A complete snapshot under a changed filter/principal is not comparable to the previous scope.
G. Explicit source deletion withdraws source availability/assertion scope only; Project/Person remains governed by its own lifecycle.
H. Old epoch cursor, reset token, mapping/schema drift and source restore: reject unsafe resume and declare required reinitialization; do not sort opaque cursor strings.
I. Concurrent writers and stale expected-head updates cannot both commit one progress edge; partition/global scope differences explicit.
J. Quarantined malformed record cannot disappear behind a successful cursor; durable reject evidence and retry/recovery obligations are explicit.
K. Equal-authority sources disagree on a business fact: synchronization preserves both observations and defers fact selection; newest ingestion time alone cannot select the winner.
L. Binding points to the wrong subject kind or silently changes subject after a move: reject, retain history and require governed correction.
M. Revoked destination writer replays old payload: no fresh unauthorized effect or protected receipt disclosure.
N. Historical correction preserves what was previously known and does not fabricate source event time.
O. Export/import, upgrade/downgrade and restart preserve identity/coverage/checkpoint meaning or refuse with a precise loss report. At least ten meaningful negative fixtures across A–O.

## Requested answer

Give a mature but implementable recommendation: boundary decision per candidate; alternatives and disagreements; source matrix with actual verification limits; compact fields/cardinalities/lifecycle; at least eight enforceable invariants; all A–O outcomes; minimum viable first increment versus explicit later increments. Include mastership/disclosure, whole-object facets, specification dependency graph, migration and production host obligations. Propose the smallest coherent reference implementation and explain which end-to-end guarantees it cannot establish. Highlight critical counterexamples and any assumptions you reject. Do not approve nonexistent code or pretend this study completes publication review.

END STUDY BRIEF
