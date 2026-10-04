# Frozen no-tools semantic audit — EM-DAT-03

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, infer missing catalogue text, invent identifiers, or grant publication authority.

The proposed result is a PROFILE over WM-DAT-005, WM-ACT-053 and WM-DAT-006, with external WM-DAT-001/004 dataset/schema and WM-XCT-012 provenance references. No new runtime/model identifier and no Transformation model are proposed.

Reconciled boundary:

1. WM-DAT-005 masters reusable versioned pipeline definitions and intended topology. WM-ACT-053 masters one run plus its ordered attempts and outcomes. WM-DAT-006 is the lineage model/root boundary owning append-only observed assertion records and their supersession lifecycle.
2. Each lineage edge/assertion is an addressable dependent record, not a new domain aggregate. It requires source and target references, granularity, capture method, a producing task/attempt or evidenced activity, confidence and evidence. It persists after the producer ends and is never cascade-deleted.
3. Transformation has no independent identity or lifecycle here. Its semantics are a definition component, immutable logic hash/locator pinned by the run, and observed edge characterisation. Reuse by content hash is not mastership. A future independently released logic catalogue is outside this contour.
4. Intended topology never auto-materializes observed lineage. Executed undeclared hops are observed-unplanned; intended unexecuted hops yield no observed edge. Name equality, correlation, co-occurrence and temporal adjacency never establish direct derivation.
5. One immutable processing-context manifest is pinned before run execution: definition revision, selected components, logic hashes, input identities and states, output-affecting parameters, environment, interval/as-of, lineage producer and closed-world flag. Attempts append without replacing the pin; a retry does not mint a new run.
6. A manual correction is an evidenced activity with actor, time, ticket/patch evidence and its own manifest fragment. It creates a distinct externally mastered output snapshot and new assertions without inventing a run or rewriting the earlier output, run or assertions.
7. Any durable partial output from a failed attempt receives its own external snapshot identity and evidence. It cannot be silently merged into a successor attempt's output.
8. Missing lineage means unknown by default. A closed-world perimeter is explicit and scoped to run, producer, interval and component set; it does not transit across runs. Mixed granularities are distinct assertions and confidence does not create transitive edges.
9. Opaque inputs are boundary nodes with unresolved ancestry and confidence impact. Unresolved ancestry is valid partial knowledge, not a foreign-key failure or synthetic upstream.

Scenario: R1 pins definition D.v3, logic hashes H1/H2, input Xin@s0 with unresolved ancestry, internal interval input and manifest M1. Attempt A1 fails and is preserved; any durable partial output has a distinct external snapshot. A2 succeeds and writes Xout@s1. Manual activity C1 corrects Xout@s1 into distinct Xout@s2 with evidence and its own manifest fragment. R2 is a separate run with M2 and may read Xout@s2. R2 does not rewrite R1 or C1, and no synthetic ancestry is invented for Xin.

Provider disagreement: Claude called the lineage assertion the WM-DAT-006 aggregate root. Grok called each assertion a dependent record and denied a third aggregate. The reconciliation treats WM-DAT-006 as the root/model boundary while its edge/assertion records remain addressable dependent records with their own append-only state and supersession. They cannot exist without endpoints and a producer and do not own endpoint or producer identity.

Audit questions:

- Does the reconciliation introduce a hidden new aggregate or identifier despite `newRuntimeId=false`?
- Are definition, run, attempt, external snapshot and lineage-record mastership unambiguous?
- Is the WM-DAT-006 root-boundary/dependent-record distinction internally coherent and faithful to both provider concerns?
- Does the scenario preserve retry, manual correction, failed partial output and unknown ancestry without mutation or invented runs?
- Identify any critical contradiction that makes even a held reviewable profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model edits and publication blockers as holds unless they contradict the profile itself.
