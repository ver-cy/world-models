# Enterprise Assertion Provenance — working boundary proposal

Status: original proposal for reconciliation with the independent studies; not frozen, implemented, accepted or published as an installable model.

## Grain and identity

Use an original companion associated with WM-XCT-012. Its account of a claim is not the claim itself, not the captured bytes, not a source catalogue entry and not a full instance of all three legacy mixins. A later native contract must use its own specification digest and namespace. Keep the older parent references semantic-only; do not promote their conceptual composition descriptions into runtime imports.

The smallest credible implementation needs distinct identified records for capture, account, evidence relation and assessment. Collapsing them into one mutable confidence field would erase independent attribution and withdrawal. Prefer four record kinds in a bounded trusted-host register:

| Kind | Independent identity and target | Required semantic fields | Master and lifecycle |
|---|---|---|---|
| CaptureActivity | One acquisition attempt of one source representation; source URI/version is distinct from capture ID | source reference; actual acquisition mode; source/capture time; observer/tool; representation digest or explicit unavailable state; scope of what was acquired | Register records the account of acquisition. Source storage remains external. Repeating an acquisition is a new event, not a correction of a previous event |
| ProvenanceRecord | One accountable account about an exact external claim revision, including an explicit subject scope | exact claim reference; account author; epistemic kind; generation activity/method; input capture/claim pins; limitations; event and receipt clocks | Account author or explicitly delegated writer corrects the account. It does not modify the externally mastered claim |
| EvidenceLink | One accountable relation between a pinned evidence revision and an exact target account/claim revision | relation kind; source pin; target pin; scope/selector; relation author; rationale for asserted support/refutation | Relation author can correct/withdraw its own link. Source author does not automatically own the relation |
| ConfidenceAssessment | One assessor's judgement about one pinned account for one purpose under one method | exact target pin; assessor; method and scale identity/version; qualitative value; reasons, limitations and basis pins | Assessor owns the judgement. A changed method/target or independent reassessment creates a new assessment; no averaging or implicit carryover |

Native register storage may be one aggregate object with immutable admitted snapshots, provided the four inner record kinds keep separate stable identities and revision pins. The snapshot is a storage boundary, not their shared semantic identity. A production adapter and independent concurrent event streams remain later work.

## Epistemic separation

The provenance account declares observed acquisition, source assertion, inference, proposal or unverified information. The activity declares what actually occurred: reading bytes, querying a live endpoint, analyzing inputs or drafting a proposal. The evidence link declares support, refutation, context or citation. The confidence assessment declares the assessor's qualified judgement. These dimensions must not be conflated.

The negative case is tested structurally: a file-read capture cannot satisfy an account declaring live-endpoint observation; an AI synthesis activity cannot satisfy observed-acquisition. Matching declarations still do not prove the activity happened or that the external claim is true. A human review is a new accountable judgement; it does not magically turn inference into direct observation.

A first implementation can safely defer numerical probability and statistical calibration. Qualitative assessments still need a named scheme, method, purpose and basis, and may be absent. Absence is not low confidence, zero or 0.95. No universal quality grade or risk score is inferred.

## History, graph and governance

Require exact internal revision/content pins. External claim and source pins identify representations without claiming availability or truth. Entity URI, source digest, record ID, record revision and schema version remain separate. Repeated copies that share a known origin can be flagged, but distinct root IDs never prove independence.

Admission is a pure trusted-host operation. Current host configuration decides writer/reader/purpose. Receipt time and current register head must come from the host; copying history into a new root is not authenticated import. Immutable per-record revision chains and exact snapshot-prefix checks can detect rewriting against the latest trusted root supplied by the host. They cannot independently discover that root or enforce durable concurrency.

Derivation references should point to exact already-recorded input revisions, making the local derivation graph acyclic. Ordinary external citations may be cyclic and do not become package imports. Retraction or correction of an input emits an impact result requiring review of dependent accounts and assessments. It never silently changes the dependent claim's content or asserts that it is false. Historical as-of views preserve the prior reliance state.

Disclose only complete authorized register views in the first reference. Hiding contrary evidence while reporting a clean verdict would be misleading. Denial must precede diagnostic parsing and expose no restricted IDs, counts or reasons. Partial disclosure, retention/erasure, credentials, PKI, source connectors and legal admissibility remain separate research work.

## Minimum question routes

| ID | Question and finding | Artifact | Permitted reference action |
|---|---|---|---|
| Q01 | What was directly acquired, and by whom? Separate capture from claim truth | CaptureActivity and representation pin | Show acquisition account; never infer source truth |
| Q02 | Is this source-asserted, inferred or proposed? Separate account and activity kind | ProvenanceRecord plus generation method | Explain declared kind and its limits |
| Q03 | How is an unreliable account withdrawn? Preserve immutable history | Retraction revision and impact report | Append an authorized withdrawal; propose re-review |
| Q04 | Is this the claim, its account or its evidence? Preserve grain | Typed IDs and external target reference | Resolve exact record kind |
| Q05 | What survives rename or relocation? Distinguish source location and identity | Qualified external pin | Retain ID; record a new acquisition if content changes |
| Q06 | Correction or a new acquisition/assessment? Preserve activity identity | Change reason and predecessor pin | Correct metadata or mint a genuinely new event |
| Q07 | What is missing or disputed? No selected truth from absent evidence | Evidence links and explicit limitations | Return insufficient-context and known gaps |
| Q08 | Who may change this record? Authorship is not authentication | Host-owned writer configuration | Validate current scope; emit generic rejection |
| Q09 | Which system masters which data? Avoid a new master for the external claim | Mastership matrix | Link to the owning system |
| Q10 | What was known at a particular time? Keep occurrence/capture/receipt separate | As-of history with exact pins | Read historical account without rewriting it |
| Q11 | Which state transitions are allowed? Distinguish account lifecycle from kind | Transition table and immutable revisions | Admit authorized creation/correction/withdrawal |
| Q12 | Which links and cardinalities are required? No dangling executable references | Closed schema and local graph check | Reject malformed or unresolved internal pins |
| Q13 | What can this reader see for this purpose? Avoid evidence leakage | Full-register projection gate | Return full permitted view or generic denial |
| Q14 | What is the smallest useful setup? Optional confidence, no mandatory ERP | Startup capture/account example | Compose the bounded companion |
| Q15 | What can an agent conclude or propose? Keep evidence distinct from permission | Impact report and agent guide | Explain and propose a check; do not contact, publish or change rights |
| Q16 | Are multiple citations independent? Repetition is not corroboration | Declared origin paths and overlap flags | Flag shared inputs; never count distinct roots as proof |
| Q17 | Can two confidence values be compared? Method and scale matter | Exact assessment and scheme pins | Refuse automatic cross-scheme arithmetic |

## Candidate invariants for executable coverage

1. No internal ID collision between capture, account, relation and assessment.
2. Every internal reference resolves to the exact cited revision and digest, not the latest record by name.
3. External claim content stays outside the companion; a new claim revision receives explicit new reliance.
4. All revisions and trusted receipts are retained; conflicting replay, truncation and historical replacement are rejected.
5. File acquisition cannot satisfy a live-system observation declaration; synthesis cannot satisfy direct acquisition.
6. Citation does not acquire support polarity by default; support requires a distinct attributable relation.
7. Source byte-integrity failure does not mean the claim is false.
8. Derivation references follow recorded precedence; no local derivation cycle or self-supporting fixed-point is accepted.
9. Retraction/correction marks downstream reliance for review without changing external conclusions.
10. Confidence needs purpose, method, scale and assessor; absence is explicit and numerical probability is deferred.
11. Reader/purpose denial happens before revealing diagnostics; it returns no hidden IDs/counts.
12. Native envelope validation never substitutes for the nested semantic companion.
13. Startup, conflicting group sources and AI synthesis fixtures exercise different failure modes.
14. Import/export round trips preserve exact identities, kinds and pins; lossy migration is refused.

These are proposed requirements. Independent studies may change the record decomposition, transition semantics or the smallest defensible implementation. No test or readiness claim is made in this document.
