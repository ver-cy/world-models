# EM-XCT-07 — Initial boundary reading

Status: research scoping in progress, 22 September 2026. This is Codex analysis, not a completed Claude/Grok study, accepted specification, implementation or release.

## Verified Vercy starting points

Public bytes for WM-XCT-002 and WM-XCT-029 specifications, publication metadata and AGENTS were downloaded and matched the canonical local publications exactly. Both are published 0.3.0-research.1 drafts with unresolved publication holds. Byte pins are in parent-retrieval.json.

For both specifications, the complete model boundary, composition, all thirteen function descriptions and research adjudication have been read. The 29 findings, full coverage and service layers of each have **not yet been completely read**. Source inventories are retrieved but not reverified. Functions are declarative descriptions, not evidence that an execution engine is shipped. Complete reading and any actual examples/validators remain necessary before the reuse decision and provider study boundary are final.

Observed in WM-XCT-002: the normative subject is permission to read/disclose. Write, modify and delete permission, identity proofing, title/delegation registries, token mechanics and enforcement are excluded. It distinguishes a proposal from an activated grant, authority verification from the grant itself, and a coverage decision from an exercise of access. Research holds include source/version uncertainty, security mechanics and arbitrary-depth machine delegation. An action-execution model cannot claim to be an exact subtype of this read-only contract without an explicit semantic extension.

Observed in WM-XCT-029: the subject is a duty or commitment and its discharge evidence. Dispatch, work execution and policy enforcement are excluded. Its XACML obligation alignment is a crosswalk only; importing a PEP enforcement function was expressly rejected. An obligation to perform an action does not establish permission or prove that it happened. The composition marks an Agreement reference required even while the boundary allows statutory and voluntary duties without an agreement: investigate that broad-parent applicability tension; do not copy it into a mandatory runtime import.

MMAS-Core, MMAS-Interchange, Contract and Event drafts were read in full from the local site source. Core supplies composition; Contract already governs purpose, parties, permission and delegation; Event already supplies immutable asserted occurrences, subjects, provenance and correction. A new execution record must justify its identity relative to those primitives. The Interchange fingerprint treats arrays as sets and excludes descriptive fields. **Inference:** do not use that fingerprint as an exact ordered action-request/idempotency content digest without a separate byte contract. This is a specific potential incompatibility, not a defect demonstrated by execution.

## Initial primary-source observations

- [RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html), January 2020, sections 1.1, 2.1 and 4.1: delegation retains the actor's identity beside the represented subject. Resource, audience and scope qualify a request. Nested prior actors are historical information, not extra grants to combine. Token exchange does not automatically propagate revocation. No token processing or RFC conformance is implemented here.
- [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/), selected sections 1.1, 2.5 and 2.9: permission, prohibition and duty are distinct; action refinement is not an execution result. Ordered logical constraints require preserved order; policy inheritance is acyclic. Full evaluator and licensing text are outside this initial reading.
- [EC2 idempotency practice](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html), live documentation: client tokens bind request parameters; changed parameters can conflict. Region/zonal scoping changes the effect boundary. This is an implementation-specific example, not a universal exactly-once guarantee.
- [HTTP Semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2), June 2022, idempotency definition: repeated identical requests have the same intended effect as one. Do not confuse it with identical responses, one network delivery or permission to retry an arbitrary action. Only the relevant definition has been confirmed in this reading.
- [Cedar authorization](https://docs.cedarpolicy.com/auth/authorization.html), live documentation, request and authorization sections: principal/action/resource/context are evaluated against policies. Default deny and forbid precedence coexist with skip-on-error diagnostics. A future strict denial on diagnostic errors must be called an application rule, not falsely described as Cedar's default.

These are short original research notes with links, not copied schemas or standards. Live documentation has no immutable release claim. Additional primary grounding, version checks and licenses are required before adopting structures.

## Questions to resolve next

1. Are ActionContract, ActionRequest, ActionResult and AuthorityBinding independent semantic objects, embedded records, profiles of existing Contract/Event/Request, or local bindings? Decide each separately; four candidate names do not require four new masters.
2. How are the action definition/version, issuer-qualified actor and represented principal, executor audience, resource/version, purpose and payload pinned without treating a claimed permission reference as trusted authorization?
3. What is the smallest practical trusted-host binding that validates current authorization and preconditions before a reversible local synthetic effect? Separate descriptive schema, policy decision, enforcement, transaction/lock and evidence.
4. How does a scoped retry key bind the immutable command while distinguishing new authority observations and transport attempts? A changed payload under the same key must conflict; an unknown outcome needs reconciliation before retry.
5. How are proposal, request, attempt, denied, observed-success, observed-no-effect and unknown-outcome separated? Timeout or missing evidence must not become success or failure-by-assumption.
6. Which result data may be returned after authority is revoked? Retrieving a cached result needs current disclosure authorization independently from suppressing a repeated effect.
7. How do correction, cancellation, compensation and record retention differ? A corrected observation does not undo a real action. Destroyed deduplication history cannot silently restore an old execution key.

Startup, matrix and AI/service examples will be synthetic. No live privileged action, production credential or private organizational extract is required. The next step is the remaining exact-parent reading, kernel/native contract comparison, then the same frozen public study boundary for actual independent Claude and Grok. No provider pass has started for EM-XCT-07 yet.
