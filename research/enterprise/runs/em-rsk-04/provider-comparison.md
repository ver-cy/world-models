# EM-RSK-04 provider comparison

Claude and Grok agree that WM-ACT-043 owns BIA and ContinuityPlan releases, RestoreTest is an exercise event, RecoveryEvidence is scoped observation/evidence, and Backup / Data Protection Policy is the sole identifier-unassigned new-model candidate. Policy, platform execution observations, reusable restore verification, test occurrence and evidence remain distinct.

Grok sharpens the boundary: Backup Policy and reusable Restore Verification require two identities, but only Backup Policy is a new model. Restore Verification is a reusable WM-ACT-043-owned specification instantiated by RestoreTest and must never profile Backup Policy. A versioned recovery-order artifact belongs to a ContinuityPlan release; tests pin its version and explicit bootstrap dependencies.

Impact tolerance, recovery objective, contractual commitment and observed outcome are separate claims. RTO <= MTPD and RPO <= tolerable loss apply only to the same aggregate, scope and release pair. Green jobs do not prove either objective. Evidence scope and time bound every claim; isolation and fixture limitations cap it. Outcomes include pass, partial and blocked, and any unmet required dependency forbids chain-recovered.
