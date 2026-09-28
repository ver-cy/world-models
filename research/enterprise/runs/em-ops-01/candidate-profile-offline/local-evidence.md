# EM-OPS-01 provider-reconciled synthesis

+## Decision
+
+Complete both reserved models on `vr.wm-act-003` and `vr.wm-act-009`; create no new catalogue or runtime identifier. Preserve both `0.2.0-legacy` assemblies byte-identically as non-installable references with external claim-retraction notes.
+
+## Boundary
+
+`vr.wm-act-009` owns reusable method/procedure knowledge, edition-scoped instruction content, immutable editions, competence requirements and adopter-owned adoption records. `vr.wm-act-003` owns process family, mandatory variant (including the `__default__` sentinel), immutable released definitions, instances and the append-only execution trace. Task, assignment, atomic act, policy, actor and evidence identities remain external references.
+
+The execution trace uses one cross-type monotonic sequence for process events, work-item events, step executions, deviations, compensation and cutover. Current state is derived. Correction and compensation append records. A change of definition or knowledge pins in flight requires an authorized cutover and applies only to later sequence positions.
+
+Definitions, instances and executions carry zero-to-many knowledge-edition digest pins. Adopter-specific adoption is resolved at instance scope. A method-less process never fabricates an edition. Method-edition manifests transitively pin the exact procedure editions they incorporate, so replay closes on immutable instruction text.
+
+Conformance is an immutable projection over canonical digests of the ordered trace and one or more pin regimes. Partial or unknown coverage can only be inconclusive. Counterfactual results remain separate from historical results.
+
+## Provider reconciliation and audit
+
+Claude and Grok independently selected COMPLETE BOTH RESERVED MODELS. Grok supplied stricter cutover, adoption, pin and conformance requirements. The single frozen Claude audit confirmed the decision, returned REVISE and supplied a closed forty-item checklist. Candidate revision 3 applies that checklist once; the audit was not rerun.
+
+## Evidence and release state
+
+Revision 3 contains 32 WM-ACT-003 invariants, 25 WM-ACT-009 invariants and 80 declarative fixtures. Candidate validation passes. Fixtures remain declarative and `fixturesExecuted=false`; CRUD, roles, installable artifacts, relation-ledger approval, external identifier verification and live verification remain open. Therefore `publishableCanonical=false` and no blocker is published.
+