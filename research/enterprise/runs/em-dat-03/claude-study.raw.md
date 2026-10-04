## Verdict

**PROFILE across three reserved models; no new model identifier, no new runtime identity.** DataPipeline → WM-DAT-005 (definition master). PipelineRun → WM-ACT-053 (execution master). LineageAssertion → WM-DAT-006 (the assertion *is* its aggregate root). **Transformation gets no master**: it is one concept with three already-owned identities — a versioned component plus pinned logic reference in WM-DAT-005, a task/stage/attempt instance in WM-ACT-053, and a characterisation of an observed edge (dependency mode, subtype, masking, logic ref) in WM-DAT-006. Minting a Transformation master would duplicate the definition master and split lineage edge semantics. EM-DAT-03 therefore delivers a version- and digest-pinned conformance layer plus one crosswalk (definition step ↔ executed task ↔ characterised edge), not a fourth aggregate. Dataset/schema stay with WM-DAT-001/004; generic provenance stays with WM-XCT-012.

## Evidence

The frozen specs already separate the three planes explicitly. WM-DAT-005's boundary notes assign time-bounded execution, attempts, input/output instances and runtime events to WM-ACT-053, and cross-system provenance observations plus their evidence to WM-DAT-006, keeping only "expected derivations and non-owning lineage references." WM-DAT-006 reciprocates: it receives job and run references and a **read-only carried run outcome** and models no scheduling, retries or state transitions. WM-ACT-053 policy states that successful process exit proves neither publication, correctness, conformance, freshness nor acceptance.

The three contour invariants are already grounded, not new: run pins input versions (WM-ACT-053 immutable bindings, effective data interval, watermark); lineage carries source and granularity (WM-DAT-006 capture method + producer + asserted granularity levels); absence of lineage ≠ absence of dependency (WM-DAT-006 `lgp-world-assumption`, per-node observation status, open gap register). The queue's `evidence_depth: index-and-publication-metadata` understates the frozen specs; `boundary_decision` nevertheless remains pending.

## Identity/mastership

- **Pipeline definition**: owner namespace + pipeline id + version. Name, path, schedule, repository, deployment or digest never identify alone.
- **Steps/components**: pipeline id + version + independent component id; component identity is owned by the definition version, not by the run.
- **Transformations**: no independent identity. Definition side = component id + version-pinned logic artifact digest. Execution side = task/stage instance id + attempt. Observed side = edge id + dependency mode + subtype + masking + commit-pinned logic reference. The crosswalk is an explicit mapping, never an equality.
- **Runs**: orchestrator-issued run id. Job name, date, state and retry number never identify a run or any constituent.
- **Attempts**: run id + task id + monotonic attempt sequence; independently identifiable, immutable; retry creates a successor and never overwrites failure.
- **Input bindings**: run id + binding id, pinning dataset version/snapshot/partition + digest + role + effective interval.
- **Output bindings**: declared, materialized and published are three separate assertions with their own times, versions, digests and visibility.
- **Lineage assertions**: assertion id, append-only, `supersedes` link; endpoints carry a stable field identifier *and* the observed name *and* a version/snapshot pin; capture method, producer and immutable schema version are mandatory.

Four independent clocks must not be collapsed: definition version, run/attempt sequence, assertion supersession, dataset state pin.

## Definition versus execution

Intended topology is a declaration in the definition version (expected input/output field mapping, expected derivation). Observed lineage is an evidenced assertion about one run. A declared edge, an emitted edge and a confirmed edge are three states. A released definition may never be edited to match what a run did; divergence is recorded as a reconciliation divergence, not a definition patch. Backfill, replay and rerun are successor runs with predecessor links and their own data interval — they never rewrite the original run or its evidence.

## Lineage assertion

Every edge carries: relation type; dependency mode (DIRECT value derivation versus INDIRECT influence such as filter, join, sort, window); subtype; masking flag; capture method (observed, parsed, declared, inferred, manual) with that method's declared blind spots; producer with immutable schema version; confidence grade against a declared scale; and evidence references.

**Derivation versus correlation** is enforced by capture method, not by prose. Column-name coincidence, schedule adjacency and co-occurrence may be recorded *only* as `capture_method = inferred` with the inference rule named and confidence at the lowest grade, and may **never** be typed DIRECT/IDENTITY. The contour's negative case is thereby rejected structurally: a name match is an inference with a stated blind spot, not a proven transformation.

**Partial observation without false causality**: a perimeter declaration names in-perimeter systems, opaque segments with entry and exit boundary nodes, the asserted granularity levels, the world assumption, and recognised manual steps. Under the default open-world assumption a missing edge means unobserved, not absent. Coverage ratios are computed only against that declared denominator; unclosed gaps go to the register with a remediation horizon.

## Manual correction and opaque input

A manual correction is not a silent gap and not a pipeline run. It is recorded as an activity with `activity_kind = manual edit`, a named agent (position preferred over person), a declared manual step in the perimeter, evidence (ticket, approval), and a **manual dependency flag** set true on the produced edges — a flag that propagates to downstream edges. Confidence is downgraded and the compensating control named. If no run record exists, that absence is stated explicitly rather than implied.

An opaque external input is a boundary node: identified by the best available authority, falling back to location-derived binding or digest with the weakness recorded and its confidence impact declared; `observation status = unresolved upstream` with a cause code; entry boundary of an opaque segment whose internal steps are declared unobservable. Its downstream edges inherit the lowest confidence available for their capture method.

## Reproducibility

Sufficient evidence to reproduce one concrete output is the run's immutable binding set plus a processing context manifest: definition version and component revision; logic artifact digest and resolved dependencies; resolved parameters, configuration and secret *references*; input version/snapshot/partition pins with digests; effective data interval and watermark; engine, environment, region, clock and locale; run and attempt identity with state history; output version, digest and row count; declared non-determinism factors; and the validation and quality results with metric, threshold and window. If any element is unknown, the manifest's reproducibility claim level degrades to *explainable*, never *reproducible*.

## Lifecycle

Definitions: draft → reviewed → approved → published → deployed → active → paused → deprecated → retired; released versions immutable, successors linked. Runs: requested, queued, dispatched, started, running, retrying, succeeded, failed, cancelled, timed out, skipped, unknown — each source-qualified with its own event and knowledge times; corrections append. Assertions: asserted → confirmed → superseded → retracted → tombstoned; a tombstone retains identifier, relation type and time axes so traversal stays sound.

## Scenario

Pipeline P v2.1.0. **R1** (interval 09-01/09-02) pins A@s41, B@s17, code digest c9; succeeds; D@v7 materialized then published; field edges A→D, B→D observed, DIRECT/AGGREGATION, high confidence. **R2** (09-02/09-03) same definition and digest, A@s42, B@s17; attempt 1 fails on timeout and is preserved; attempt 2 succeeds; D@v8. A completeness rule on D@v8 fails — R2 success proves nothing about fitness. **Manual correction**: a steward amends 14 rows, D@v8 → D@v9, no run, manual flag true, evidenced by ticket not by code, so D@v9 is explainable but not reproducible. **Opaque input**: vendor drop C has no upstream lineage and no contract version; its only link to D@v9 is a column-name match, recorded as inferred/INDIRECT at lowest confidence. Outcome: one observed segment with digests, one manual segment evidenced procedurally, one inferred edge, one unknown upstream — a partially evidenced chain with a measured coverage ratio, not fabricated completeness.

## Invariants

1. Definition, run, task, attempt, binding, materialization and assertion have separate resolvable identities. 2. Released definitions and recorded attempts are immutable; corrections append successors. 3. Every run pins definition revision, code digest, input versions and effective interval. 4. Retry never overwrites failure. 5. Declared, materialized and published outputs are distinct assertions. 6. Run success is not data quality, freshness, publication or acceptance. 7. Every edge carries capture method, producer, granularity and confidence. 8. Derivation requires evidence; correlation may only be `inferred`. 9. Name coincidence is never DIRECT. 10. Absence of an edge is meaningful only under a declared closed-world perimeter. 11. Manual steps are declared, flagged and propagated. 12. Opaque inputs are boundary nodes with cause codes, never inferred ancestry. 13. Coverage claims require a published perimeter denominator. 14. Lineage stores no pipeline definitions, run state machines, dataset bytes or schema masters.

## Minimal completion shape

Make normative, as profile constraints only: mandatory capture method + producer + confidence on every edge; mandatory perimeter and granularity declaration before any coverage claim; mandatory world-assumption code; ban on DIRECT/IDENTITY for name-match evidence; mandatory manual dependency flag with propagation rule; mandatory input version pin plus interval on every run; mandatory separation of materialized and published; mandatory reproducibility claim level with enumerated unknowns; mandatory predecessor link on backfill/replay; mandatory stable field id alongside observed name; the step↔task↔edge crosswalk; and a resolution rule for the perimeter-declaration versioning defect so a coverage figure can name the perimeter revision it measured.

## Holds

No canonical completeness and no installability are claimed. All three specs are `publishableCanonical: false`, `reviewable-draft`, and single-provider: WM-DAT-005 and WM-ACT-053 are Codex-only with Claude and Grok waived; WM-DAT-006 is Claude-only with Grok waived. Every relevant relation is candidate: WM-DAT-005 CONTAINS WM-ACT-053, WM-DAT-005 COMPOSE WM-DAT-006, WM-DAT-001 COMPOSE WM-DAT-006; WM-DAT-005's registry parent WM-ACT-003 is outside the dossier. WM-DAT-006 carries unresolved defects that this profile depends on: its own registry parent WM-XCT-012 is never referenced in the result; assertion/record/instance/bundle/payload scopes are not disambiguated; the perimeter declaration is non-serial while coverage reports are serial, so a coverage figure cannot currently be pinned to the perimeter revision it measured; the Iceberg citation is main-branch and rejected as stable; five artifacts have no producing function; and the confidence grading scale has no normative source. Field-level and row-level generalisation, streaming windowing, and the GDPR-versus-retention resolution remain design decisions, not conformance. `boundary_decision` for EM-DAT-03 stays **pending** until the candidate relations are approved and the WM-DAT-006 defects are cleared; if independent review finds the fourteen invariants to be deployment policy rather than portable semantics, downgrade to REUSE ONLY and publish only an adoption mapping.
