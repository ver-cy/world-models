Verdict.

Accept the proposed disposition. Profile WM-DAT-005, WM-ACT-053, and WM-DAT-006. Do not create a Transformation model. Transformation has no independent lifecycle. A lineage assertion is a dependent record, not an aggregate root. Binding conditions: an assertion producer may be a pipeline task/attempt or an evidenced activity; corrected outputs must be distinct external snapshots.

Strongest evidence.

The reserved split already separates intended topology (WM-DAT-005), pinned occurrence (WM-ACT-053), and observed edges (WM-DAT-006). A preserved retry is a second attempt under one run pin. A manual correction is an evidenced activity that writes a new snapshot and new edges without inventing a run. An opaque input is a boundary node with unresolved ancestry. Column-name match is rejected as derivation proof, which is what stops WM-DAT-006 from becoming a guessed graph. None of these require a Transformation master.

Strongest counterexample.

A reusable mapping spec (same SQL/UDF used by many pipelines, versioned and retired on its own calendar) looks like a Transformation master. If that object changes without a new pipeline-definition identity, “definition component + pinned logic” becomes ambiguous. Mitigation without a fourth model: the run pins an immutable content-addressed logic payload (hash + locator). Share-by-hash is not mastership. A later logic catalog is outside EM-DAT-03.

Identity / mastership.

WM-DAT-005 is the aggregate root for the reusable pipeline definition: definition key + version. It masters intended topology and definition components. It does not master datasets, schemas, runs, or edges. WM-ACT-053 is the aggregate root for the pipeline-run occurrence: run-id. Attempts are children of the run, not new runs. The pin (definition revision, logic hashes, inputs, interval) is payload, not the identifier; a replay with identical pins is a distinct run compared by manifest equality. WM-DAT-006 is a store of dependent assertion records, not a third aggregate root and not a lineage catalog. Dataset and schema identities remain external. Boundary nodes reference an external or unresolved dataset; they are not local masters.

Transformation placement.

No independent lifecycle. Semantics live in three places only: a definition component on WM-DAT-005 (intended slot and classification attributes), pinned logic on the WM-ACT-053 run (immutable digest per executed component), and an observed edge on WM-DAT-006 (what was actually produced). “What ran” is the task/attempt plus pin. Cross-pipeline reuse is shared payload hash. Field-level clauses stay attributes of the component and pin, not child entities. An independent Transformation lifecycle would invent versioning, ownership, and retirement for slots that exist only inside a definition.

Lineage assertion.

Dependent record. Composite identity: producer-event, source-ref, target-ref, granularity, capture-method, evidence-ref. It cannot be created without endpoints and a producer event. Producer is WM-ACT-053-profiled: a task/attempt or an evidenced activity (correction, harvest, declaration)—not “any statement.” Records persist after the run ends; dependent does not mean cascade-delete. Orphan means missing producer-event reference. Treating the assertion as an aggregate root would allow a curated edge catalog that reconstitutes intended topology inside WM-DAT-006. Supersession adds a record; it does not mutate the producing run or prior assertions.

Partial-lineage rules.

Absent edge means unknown, not “no derivation,” unless a closed-world perimeter is declared. Perimeter is explicit and scoped (run, producer, interval, component set); default is open-world; it does not transit across runs. Name match, correlation, and co-occurrence never prove direct derivation. Granularity is part of identity; dataset-grain and column-grain are different assertions with no automatic promotion. Capture method, producer, confidence, and evidence are mandatory. Confidence does not transitively mint A→C from A→B and B→C. Opaque inputs are required boundary nodes with ancestry unresolved. Intended topology never auto-materializes observed edges. Unexecuted intended hop is not observed; executed undeclared hop is observed-unplanned. Partial graphs are valid.

Reproducibility gate.

A run is reproducible only if an immutable processing-context manifest is pinned at start and not rewritten. Minimum content: definition identity and revision; intended-component snapshot actually selected; logic content hash per executed component; input identities plus interval/as-of; output-affecting parameters; attempt sequence including preserved retries; lineage-capture producer; closed-world flag. Manifest mutation after first attempt invalidates that run identity. A retry may append attempts; it may not replace the pin. A manual correction carries its own manifest fragment and does not mutate the prior run.

Scenario.

Boundary node Xin: unresolved ancestry, capture = declared-source. R1 pins D.v3, hashes {H1,H2}, inputs {Xin@s0, I_int[T0–T1]}, interval T0–T1, immutable manifest M1. Attempt A1 fails after partial work and is preserved; any durable A1 object is a distinct external snapshot and is not silent R1 lineage. Attempt A2 succeeds and writes Xout@s1. Complete observed edges come from A2. A1 and A2 share R1; retry is not a new run or definition. Evidenced activity C1 (not a pipeline run) corrects Xout@s1 → Xout@s2 with actor, time, ticket/patch evidence, and a manifest fragment. New observed edges from C1. R1 pin and R1 assertions stay unchanged. R2 is a separate run with manifest M2. It may read Xout@s2 and/or Xin@s0. Its edges are observed from R2 capture. Xin ancestry remains unresolved. R2 does not rewrite R1 or C1. Rejected: collapsing A1 into A2; inventing a run for C1; treating Xout@s1 and Xout@s2 as one output; inferring R2 edges from R1 topology; filling Xin with a synthetic upstream.

Invariants.

1. Every run pins exactly one definition revision, one code-hash set, one input set, one interval.
2. Attempts belong to a run; a retry does not mint a new run-id.
3. Intended topology is not observed lineage; neither auto-projects to the other.
4. An observed edge exists only with granularity, capture method, producer, confidence, and evidence.
5. Column-name equality or correlation does not assert derivation.
6. Absent edge means unknown unless a closed-world perimeter is declared.
7. Manual correction is an evidenced activity; it shall not create a pipeline run.
8. Opaque input shall appear as a boundary node with unresolved ancestry.
9. Reproducibility requires an immutable processing-context manifest; post-start mutation breaks the gate.
10. A lineage assertion cannot exist without endpoints and a producing run or evidenced activity.
11. Dataset/schema mastership remains external; pipelines do not mint dataset identity.
12. Pinned logic is content-addressed on the run; share-by-hash is not a Transformation master.
13. Later correction or downstream run adds assertions; it does not rewrite prior pins or prior assertions.
14. Closed-world declaration is explicit and scoped; it is not the default and does not transit across runs.
15. Producer of a WM-DAT-006 record shall be a task/attempt or an evidenced activity.
16. An intended component with no successful attempt yields no observed edge from that component.
17. Partial durable output from a failed attempt, if it exists, has its own external snapshot identity.

Minimum completion shape.

WM-DAT-005: definition id, revision, component list. WM-ACT-053: run-id, attempt set including preserved retries, pin, immutable manifest, per-attempt status. WM-DAT-006: zero or more edges with endpoints, grain, capture, producer, confidence, evidence; boundary-node flags; closed-world flag. External dataset/schema refs only. Optional evidenced-activity record for correction. Incomplete if the pin is missing, the manifest is mutated, a retry is collapsed, an assertion lacks evidence, an opaque input is omitted, or a correction is modeled as a fake run.

Blockers.

If WM-ACT-053 cannot retain multiple attempts under one run, the retry scenario inflates identity. If WM-DAT-006 is run-scoped only, manual correction forces invented runs. If the manifest is mutable or optional, the reproducibility gate fails. If intended topology and observed lineage share one association type, they will be conflated. Closed-world as default would convert missing lineage into “no dependency.” If corrected output identity is not an external snapshot, C1 mutates R1’s target. Shared logic-catalog demand must not be satisfied by creating Transformation. Unresolved ancestry must be first-class, not a foreign-key failure. Mixed-grain capture without grain-on-identity will merge distinct assertions. Continuous intervals are undefined unless a closed window can be pinned.
