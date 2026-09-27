# EM-DAT-03 local synthesis

## Disposition

- Create an Enterprise profile across three reserved models: WM-DAT-005 owns reusable Data Pipeline definitions, WM-ACT-053 owns Pipeline Run executions, and WM-DAT-006 owns append-only Lineage Assertions.
- Do not create a Transformation model. Definition components and pinned logic belong to WM-DAT-005; executed task/stage attempts belong to WM-ACT-053; observed transformation characterisation belongs to the WM-DAT-006 edge.
- Add a version-pinned crosswalk from definition step to executed task/attempt to lineage edge. It is a mapping, never identity equality.
- Keep dataset/schema identities in WM-DAT-001/004 and generic provenance in WM-XCT-012.
- Allocate no runtime or model identifier.

## Identity and clocks

Pipeline definitions use owner namespace, pipeline id and immutable version. Definition components use pipeline version plus stable component id. Runs use orchestrator-issued run identity; attempts use run, task and monotonic attempt sequence. Input and output bindings pin dataset version or snapshot, partition, digest, role and effective interval. Lineage assertions have append-only identities and supersession links.

Four clocks remain independent: definition version, run/attempt sequence, lineage assertion supersession and dataset state. Released definitions and recorded attempts are immutable; rerun, retry, backfill and correction append successors.

## Intended topology and observed lineage

WM-DAT-005 declares expected topology and derivations. WM-DAT-006 records evidenced observations about a run. Declared, emitted and confirmed edges are distinct states. Divergence between definition and execution is a reconciliation finding, never a silent definition edit.

Every lineage edge declares relation type, direct or indirect dependency mode, subtype, masking, granularity, capture method, producer/schema version, confidence and evidence. Name similarity, temporal adjacency or co-occurrence may appear only as low-confidence inferred evidence and can never establish direct derivation.

Missing lineage does not mean no dependency under the default open-world assumption. Coverage claims require a versioned perimeter, denominator, supported granularities, opaque segments and known manual steps.

## Manual correction, opaque input and reproducibility

A manual correction is a separately evidenced activity with agent/position, ticket or approval, before/after dataset versions and a propagated manual-dependency flag. It is not fabricated as a pipeline run.

An opaque external input is a boundary node with the best available identity, unresolved-upstream status, cause code and explicit confidence effect. Its internal ancestry remains unknown.

A reproducible output requires the immutable run binding set: definition/component revision, code and dependency digests, parameters/configuration and secret references, input pins and digests, interval/watermark, runtime environment, attempts, output digest, nondeterminism declaration and validation/quality evidence. Missing elements lower the claim to explainable or partially reproducible.

## Acceptance scenario

Run R1 pins pipeline P v2.1, input snapshots A@s41/B@s17 and code digest c9 and produces D@v7 with observed edges. R2 pins A@s42/B@s17; its failed first attempt remains, its successor succeeds and produces D@v8, while a failed quality rule proves run success is not fitness. A steward manually creates D@v9 from D@v8 with ticket evidence and no invented run. An external vendor input C has unknown upstream lineage; a name match is retained only as inferred indirect evidence. The graph is explicitly partial.

## Invariants

1. Definition, component, run, task, attempt, binding, output and assertion identities remain distinct.
2. Released definitions and recorded attempts are immutable.
3. Every run pins definition, logic digest, input states and effective interval.
4. Retry never overwrites a failed attempt.
5. Declared, materialized and published outputs are separate assertions.
6. Run success proves neither quality, freshness, publication nor acceptance.
7. Every lineage edge declares capture method, producer, granularity, confidence and evidence.
8. Correlation and name matching never establish direct derivation.
9. Missing edges imply absence only inside an explicit closed-world perimeter.
10. Manual dependencies are declared and propagated.
11. Opaque inputs remain boundary nodes with unresolved ancestry.
12. Coverage figures identify the exact perimeter revision and denominator.
13. Lineage references pipeline/run/dataset/schema masters and does not reproduce them.
14. Reproducibility claims enumerate unknown or nondeterministic factors.

## Holds

All three primary releases remain non-canonical reviewable drafts with single-provider limitations. Their relations are candidate; WM-DAT-006 has an unresolved WM-XCT-012 parent and perimeter-versioning defects; confidence grading and several artifact/function links lack settled authority. Runtime-specific profiles, immutable pins, crosswalk validation and fixtures are incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
