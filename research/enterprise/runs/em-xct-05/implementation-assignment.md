# EM-XCT-05 — Provisional implementation assignment

Status: **Codex research proposal, awaiting reconciliation with completed independent studies**. This is an assignment for a future candidate, not an implemented or installable model. No runtime ID/version is reserved by this document. No approval, anonymization, deletion, IAM or regulatory-conformance claim is made.

## Boundary decisions to resolve

The useful first boundary is an exact, reviewable **context-package plan**, composed of single-object projection manifests. It should distinguish four questions: what output is proposed; who currently authorizes serving it; what combined-disclosure risk has been reviewed; and what the custodians must retain or dispose of. A single Boolean cannot answer all four.

| Registry candidate | Provisional disposition | What must remain external |
|---|---|---|
| DisclosurePolicy | Reference the pinned declarative shape and the host's current applicable-policy set; avoid a second generic permission language | Consent/grant administration, policy precedence and live enforcement |
| ClassificationAssignment | Carry exact source/field/assignment/scheme/term pins with status and time; compare against WM-XCT-020 Classification Binding before claiming specialization | Scheme authoring, classification judgment, downgrade authority and cross-scheme mappings |
| RetentionConstraint | Separate serving expiry, retention floor, disposal deadline and active hold references; report incompatible or missing constraints to the custodian | Legal interpretation, physical destruction, backup/recipient erasure and legal-hold administration |
| ProjectionContract | One canonical object and exact source revision/schema/selected field set; an immutable proposal, not a new object master | Transformations, source truth, authentication and recipient delivery |

WM-XCT-020 is currently named **Classification Binding**, not a confidentiality enforcement engine. Its published boundary explicitly separates schemes, mappings and policy evaluation. WM-XCT-005 is a legacy, non-installable catalogue entry; WM-XCT-035 and WM-XCT-038 are todo/non-installable. Do not invent executable delegation to them. Exact parent comparisons and holds remain required before freezing a candidate.

## Candidate objects and cardinalities to challenge

- **ProjectionManifest**: one independently identified manifest revision; exactly one canonical subject; one exact source artifact and schema pin; one source revision; a non-empty, unique selected-field list; one audience context; one qualified purpose; current classification-assignment references for every selected field. Source pointers and object IDs may themselves be sensitive.
- **ContextPackagePlan**: one aggregate identity and immutable revision; 1..N explicitly bounded component pins; one owner, audience, purpose and intended environment; an exact membership digest. A plan may contain multiple different projections of the same object only if that combination is explicitly reviewed. It must not imply that a multi-object report is a single-object Projection.
- **CompositionAssessment**: independent attributed assessment identity; exactly one plan digest and context; named method and its version; evidence; reviewer and authority reference; result and validity horizon; relevant prior-release context. Positive, negative, inconclusive and expired are distinct. It is an assessment, not a serving grant or a proof against arbitrary external knowledge.
- **RetentionConstraintSet**: exactly scoped artifacts/custodians/purposes with separate serving deadline, retention floor, disposal deadline and hold references. Unknown dates and trigger conditions remain explicit. No operation actually deletes records in the first reference.
- **ReadinessReport**: a derived internal artifact pinning exact evaluated inputs and missing prerequisites. It can say proposal-ready, denied or insufficient-context within a stated profile; it cannot certify live authorization, actual transmission or completed disposal.

Prefer fewer exported types if these are simply embedded immutable values. Do not give identity to every JSON fragment. An actual aggregate report additionally needs its calculation, source lineage, grain and disclosure boundary owned by the domain, separate from package membership.

## Host and implementation boundary

Start with a trusted-host, metadata-only reference unless provider reconciliation demonstrates a sound, narrow data-serving scope. It should validate identity/pins/cardinalities, bind review to exact context and detect missing or stale evidence. It should not automatically fetch payloads or expose metadata to requesters. A separately implemented serving integration must authenticate the caller, retrieve current policy/classification state, atomically recheck freshness at delivery, keep internal explanations restricted and preserve a generic external failure response.

Define a named canonical encoding and bounded input profile before using digests. Raw-byte digests, semantic JSON digests and identity are different. Pin the exact schema grammar and reference versions. No optional field may silently default to permission, public sensitivity, indefinite storage or successful deletion. Restrict unsupported field-path grammars rather than pretend a shallow include list validates nested data.

Corrections create a new manifest or assessment revision with explicit supersession. They do not overwrite earlier evidence. Replaying a proposal is distinct from reusing a stale serving decision. A subsequent source, shape, membership, purpose, audience, environment, classification, policy or prior-release-context change requires a fresh assessment where relevant. List precisely which changes invalidate which artifact; do not use a universal unexplained freshness flag.

## Question routes for a candidate tree

These 24 routes are draft requirements. Each must become an actual Bundle → Layer → Finding → Question → Artifact → allowed Action route, with explicit missing-context behavior.

| Bundle / layer | Question | Required artifact | Permitted action under host authority |
|---|---|---|---|
| Identity / subject | Q01 Which single canonical object does this projection describe? | Qualified object reference and identity decision | Resolve the reference or request missing identity evidence |
| Identity / subject | Q02 Which exact source revision and schema were used? | Source and schema pins, capture receipt | Verify declared pin consistency; do not infer source truth |
| Identity / subject | Q03 Is this a projection, a package or a domain aggregate report? | Boundary and aggregation declaration | Split incompatible boundaries or request an aggregate owner |
| Identity / classification | Q04 Which scheme and terms classify each selected field? | Versioned assignment set | Check complete references; return missing context for unknown labels |
| Identity / classification | Q05 Who can correct or downgrade the classification? | Current authority and correction evidence | Propose a governed correction; never infer authority from a role label |
| Identity / classification | Q06 Are multiple schemes or compartments comparable? | Explicit mapping and combination rules | Refuse an unsupported comparison |
| Disclosure / shape | Q07 Which exact fields and metadata may leave? | Closed shape and schema binding | Validate declared selection; request treatment for newly appearing fields |
| Disclosure / shape | Q08 Do nested values or relations include another object? | Path grammar, graph extent and nested boundary | Reject unsupported expansion; require separate projections |
| Disclosure / shape | Q09 Can omission, counts, errors or identifiers reveal withheld facts? | Residual-disclosure assessment | Restrict public diagnostics and escalate unresolved channels |
| Disclosure / current authority | Q10 Which current grant and policy cover audience and purpose? | Current host authorization evidence | Request a new host decision; never treat an old review as a grant |
| Disclosure / current authority | Q11 Has anything changed since the proposal was assessed? | Exact current source/policy/classification context | Invalidate stale serving readiness |
| Disclosure / current authority | Q12 What exactly is valid when a cache entry is reused? | Cache scope, expiry and revocation integration | Reevaluate current serving rights or refuse reuse |
| Composition / membership | Q13 Which exact component set was jointly reviewed? | Immutable membership and context digest | Verify equality; changed membership requires a new review |
| Composition / membership | Q14 What can be inferred from combining permitted components? | Scenario-specific joint assessment | Record unresolved risk or a qualified assessment, not a guarantee |
| Composition / membership | Q15 Which prior releases and external information were considered? | Prior-release context and assumptions | Reject an unsupported freshness claim; request missing context |
| Composition / aggregate | Q16 What does the aggregate measure and who owns its calculation? | Aggregate identity, calculation and lineage | Validate the declared boundary; do not execute an unreviewed calculation |
| Composition / aggregate | Q17 Which grain or privacy mechanism applies? | Pinned mechanism and parameter review | Require its verified implementation separately |
| Composition / aggregate | Q18 Does a positive assessment remain valid for another recipient? | Exact audience/environment/purpose binding | Refuse transfer of the assessment to a different context |
| Continuity / storage | Q19 When must serving stop, independently of retained evidence? | Serving deadline and current restriction | Stop new serving through the host; preserve permitted restricted evidence |
| Continuity / storage | Q20 Which custodian controls each source, cache, output and backup? | Scoped custody and lineage map | Identify unowned disposal work rather than claim global erasure |
| Continuity / storage | Q21 Do retention, disposal and hold obligations conflict? | Versioned constraints and active hold evidence | Produce a restricted unresolved-disposition artifact |
| Continuity / disposition | Q22 Was disposal requested, executed or independently verified? | Separate request, execution and verification records | Keep unknown execution unknown; never equate a tombstone with destruction |
| Continuity / disposition | Q23 What evidence may remain after disposal? | Minimal evidence/tombstone policy and scope | Request authorized disposition with an explicit evidence boundary |
| Continuity / disposition | Q24 Can this package migrate without widening disclosure or losing meaning? | Loss report, pin mappings and complete retained evidence | Permit only a tested conversion; reject unsupported downgrade |

## Acceptance invariants and adversarial tests

1. Each ProjectionManifest has exactly one canonical subject; a package has its own aggregate boundary.
2. Every source and policy/schema reference is qualified and pinned; a digest does not grant access.
3. Every selected field has a current, explicit classification assignment for the accepted scheme.
4. Unknown scheme, missing term, unclassified selected field or unsupported path prevents a ready decision.
5. Current authorization is scoped to audience, operation and purpose and remains external to a historical assessment.
6. Joint assessment pins the exact component set and context; per-component acceptance cannot substitute for it.
7. Repeated releases are assessed against explicit prior-release assumptions; no universal inference-prevention claim.
8. Public failure is generic; restricted diagnostic details and withheld metadata never appear in a recipient result.
9. Corrections and revocations preserve historical attribution without granting current serving authority.
10. Replay identity does not make an expired or revoked serving decision current.
11. Serving expiry, retention floor, disposal deadline and hold are distinct; unresolved conflicts never cause automatic destruction.
12. A delete marker, archive status or submitted request does not assert physical erasure.
13. Source, output, cache and backup custody are explicit; one custodian's action does not prove all copies erased.
14. Migration declares loss and disclosure changes; unsupported or widening transformations reject.

Test startup, matrix-group and AI-release cases from shared-boundary.md. Negatives must isolate the violated rule: missing subject; two subjects in one projection; source digest repointing; new unclassified field; same label from another scheme; nested relation expansion; metadata leak; changed purpose; revoked grant; stale cache; changed package membership; subtraction attack without joint assessment; prior-release-context drift; attempted reuse across recipients; conflicting retention/hold; deletion marker represented as destruction; partial-copy disposal called complete; silent schema downgrade. Include positive correction, exact proposal replay, proper contextual re-review and lossless same-version roundtrip.

## What to freeze before publishing

Reconcile the real Claude and Grok studies and record disagreements. Read complete relevant parent specifications/holds and settle the candidate boundary. Prepare closed schemas and meaningful fixtures; if executable, run all negative paths and three fresh native bindings, keeping outer-envelope and nested semantic checks separate. Map all five whole-object facets for each exported type. Freeze actual code/schema/contract inputs for independent audits. Publish a discoverable English card and question tree only after the package has earned its stated readiness, with no invented native installation, privacy or disposal claim.
