# EM-XCT-07 — bounded research supplement S1

Continue your independent research on the original shared EM-XCT-07 brief. This is the same supplement for Claude and Grok. It is not a request to agree with another provider or approve implementation. Answer in English, preferably within 2,200 words, with explicit choices, strongest counterexamples and exact remaining limits. Preserve your original study; this is a separate amendment. Do not request private company data or infer permission to execute anything.

The original work exposed unresolved choices about operation-definition ownership, accepted-request identity and standing delegation. The following additional public Vercy facts and inspected native behavior must inform the final bounded design.

## 1. Existing ownership and fact-authority boundary

https://ver.cy/models/wm-xct-001-ownership-stewardship/spec.yaml is 0.3.1-enterprise.1, exact SHA-256 fa942556a3f460729db2e94b24d1efd4d33ee2e5fb0b1deed3ce040756acf474. Its subject is a contestable control assertion. Its delegated-authority layer already describes a scoped revocable DelegationMandate, explicit subdelegation limits and mandate verification evidence. Runtime authorization evaluation/enforcement, credentials and legal validity are outside its boundary. `verify-delegated-authority` and `grant-or-revoke-delegation-mandate` are declarative functions, not evidence of a shipped runtime verifier. A selected review read the full boundary/composition/functions and both complete mandate findings, not all legal domains or external sources.

https://ver.cy/models/wm-xct-001-ownership-stewardship/profiles/enterprise-fact-authority/0.1.0/spec.json has SHA-256 cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582. Its executable authority.py and schema were read in full. Its WriteGrant authorizes particular writers to admit a source's observations for an exact scope/predicate under FactAuthority. StewardshipAssignment conveys duties, not generic execution or subdelegation; MastershipRule conveys source precedence, not permission. The host supplies a trusted governance/read configuration. It does not implement action execution or a general delegation-chain register.

Conclusion to evaluate: cite an existing host-owned versioned control/mandate basis in the first increment, retain fresh action-scoped host decisions separately, and avoid a duplicate DelegationMandate master or widening source WriteGrant into general execution permission. A Contract profile remains an alternative only if its exact record binding, ownership and overlap can be justified.

## 2. Legacy function and act-class concepts already exist

https://ver.cy/models/docs/activity-work/K1-function-and-capability.md (0.2.0, exact public SHA-256 e93a14c18a08f1a07ed0ea13c13f4e3b860c87d131e26e6ff83e3a7a56e4a9c0) describes named functions, capabilities, proficiency, agent attributions, evidence, capacity and requirements. Its `function` is a named purpose an agent can fulfil, with name, definition, domain and typical outputs.

https://ver.cy/models/docs/activity-work/K2-act-action.md (0.2.0, exact public SHA-256 b262d62aaf41bec6c754ccac6bd65710cb9b85086fc791b9620eef9116f128ef) describes atomic recorded acts, `actClass`, participants, involved objects, outcome, responsibility and derivation. `actClass` is the typed verb an act instantiates, with name, definition, domain and expected participants. Act occurrences align with the core Event concept.

These are complete public Markdown seeds, not completed researched publications or executable schemas. Their corresponding WM-ACT-001/002 research rows remain queued. Their conformance labels and wildcard imports have not been validated. The exact public bytes match the website source; differences from repository Markdown are only line endings and a middle-dot encoding repair. Do not invent a semantic conflict from those byte differences.

This raises a concrete choice: is an exact versioned operation definition a profile/refinement of actClass/function, a new sibling object, or an external pinned definition for the first increment? The operation needs parameters, preconditions, effect boundary, retirement, adapter binding and immutable version semantics; none is a permission by itself.

## 3. Native and architecture facts inspected directly

Public architecture sources, fully read and byte-pinned by the orchestrator:

- https://ver.cy/spec/docs/02-architecture/MMAS-Core.md
- https://ver.cy/spec/docs/02-architecture/MMAS-Interchange.md
- https://ver.cy/spec/docs/04-core-concepts/Contract.md
- https://ver.cy/spec/docs/04-core-concepts/Event.md

The native runtime validator resolves Event `subjectIds` against retained **object IDs or record IDs**, including an earlier Event ID. A derived hash such as keySlotId is not automatically a known subject. It must remain in payload or refer to a real retained record; creating an otherwise meaningless slot object is not required. The Event payload is open and needs its own nested/history validator. Object facets are also open. The generic installer is not a semantic execution engine.

A D1 experiment successfully validates three synthetic ActionRequest objects and their SubmissionEvents against closed request shape checks and the two native outer schemas. That is six envelope checks and fourteen rejected malformed/inconsistent inputs, not installed Dimensions, authorization or execution. It establishes representational feasibility only. A request object would have independent intent identity, immutable content and lifecycle derived from native events; its generic object state must not be confused with execution state. An acceptance-Event anchor is also technically possible, provided its subjects and whole-history contract are coherent. Decide by semantic identity, not merely field fit or a preference for fewer objects.

## 4. Implemented experiment versus proposed guarantees

An original isolated SQLite prototype passed 24 behavioral tests. One local BEGIN IMMEDIATE transaction serializes its trusted synthetic policy, one ordered label-list mutation, deduplication binding and original effect receipt. Repeated SET after intervening work is prevented by locating a committed matching request before checking the current resource revision. Current execution and separate current disclosure checks exist. The prototype has no real credentials, final schema, complete lifecycle or native installation; its simple delegated boolean is not full scope containment.

One file lock around several file writes is not an atomic multi-file commit. Any file-based alternative must specify crash recovery, durability and actual uniqueness enforcement. A provenance.requestId property is not itself a unique database constraint. Absence of an effect record proves no effect only if the retained state is authoritative and complete. Even a local database restored to an older internally valid snapshot can violate that assumption; an epoch in the same restored store cannot independently prove continuity. Do not claim distributed or external exactly-once effects.

A candidate first lifecycle is pending → committed/cancelled/expired/rejected-precondition; denied execution can remain pending until expiry, with a fresh permission check on each delivery. A stricter terminal-denial policy is an alternative. A local transaction's caller may have unknown outcome after response loss even though the authoritative database has either committed or rolled back. General external in-flight/reconciliation semantics can be deferred instead of simulated dishonestly.

Compensation is a new authorized request/key referencing an original retained receipt. The label example must use the old before-value and require the current revision to equal that receipt's after-revision; intervening updates reject it. Observation corrections append knowledge without undoing an effect. Optional maxUses needs a real authoritative concurrent counter or must be deferred.

## 5. Five decisions required now

1. Select the smallest useful definition/request/event/basis boundary in light of the legacy and ownership material. Give an exact reuse/profile/new/external/defer disposition and the justification for every independent identity.
2. Choose one native binding that has no invented unresolved key subject or fake aggregate host. Explain pending identity, retries, event issuer versus intended actor, immutable content, correction and archive/admission limits.
3. State the minimal direct-delegation fixture contract: independent principal scope and delegate scope, verified issuer standing supplied by host, exact Dimension/resource/action/purpose/audience/time intersection, no chains or impersonation. Decide whether a standing-grant profile belongs in the first package or an external reference is adequate.
4. Resolve terminal denial versus retryable denial, replay after the request deadline, cancellation race, separate disclosure and attempt terminology. For a denied reader, absent/existing/conflicting/retired states must produce the same outward response; a duplicate-but-not-disclosable response leaks existence. Distinguish transport delivery from execution try and effect.
5. Name the indispensable implementation tests and any reason the resulting small increment still cannot be published after genuine frozen audits. Use the protocol's exact five facet keys for the selected types: identity-class, direct-properties, recognition-observation, capabilities-behaviour-actions, context-evidence.

The original parent's validity-token default, contradictory break-glass treatment and required Agreement dependency are already explicitly excluded under the owner's authorization. They require no new permission request. Do not mark a proposed case as implemented unless actual delivered code/results demonstrate it. Keep source-grounded facts, your design choices and unverified assumptions distinct.
