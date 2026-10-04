# Exact unsent Grok prompt — EM-RSK-04

Independent enterprise metamodel review. Do not browse, invent identifiers, claim standards conformance or give operational recovery advice.

EM-RSK-04 covers BusinessImpactAnalysis, ContinuityPlan, BackupPolicy, RestoreTest and RecoveryEvidence using the complete WM-ACT-043 Business Continuity / Recovery draft.

Assess this proposal: reuse and complete WM-ACT-043 for the continuity capability. BIA and ContinuityPlan are aggregate-owned releases. A continuity RestoreTest is an exercise event and RecoveryEvidence is a scoped evidence/observation record. Backup / Data Protection Policy is the only identifier-unassigned new-model candidate because it has an independent owner and lifecycle and applies beyond continuity plans. Backup execution and recovery points remain platform observations. Keep policy, execution and restore verification distinct. Separate impact tolerance, recovery objective, contractual commitment and observed outcome. Add a versioned recovery-order artifact, explicit bootstrap dependencies, RTO/MTPD and RPO/tolerable-loss consistency rules, test isolation, fixture limitations and a partial/blocked outcome vocabulary.

Test a synthetic service chain depending on identity, a database and an external signer. Database backups are green; database restore passes at object scope; the signer is unavailable; the recovery point is 12 hours old against a 1-hour RPO. Reject claims that the chain is recovered or that the backup jobs prove RTO/RPO.

Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; BIA/objectives; policy/execution/restore; exercises versus real events; dependencies/order; evidence/time; scenario; at least 10 invariants; minimum model set; blockers. Explicitly decide whether Backup Policy and reusable Restore Verification need one identity, two identities or profile semantics, and why.
