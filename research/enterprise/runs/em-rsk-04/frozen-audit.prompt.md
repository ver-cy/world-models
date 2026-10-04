# Frozen audit prompt — EM-RSK-04

Audit only the frozen material below. Use no tools and no outside knowledge. Do not invent identifiers or claim standards compliance. Return a concise verdict and only material defects, each with the smallest remediation. Check identity/mastership, the two-identity/one-new-model decision, BIA/plan releases, recovery-order and bootstrap pins, policy/execution/verification separation, objective consistency, evidence scope/time, exercise isolation, fixture limitations, outcome vocabulary and traceability. End with exact additional fixtures. This is the one frozen audit; do not request a second audit.

## LOCAL EVIDENCE
```
# EM-RSK-04 local synthesis

## Disposition

- Reuse and complete WM-ACT-043 as the Business Continuity / Recovery aggregate.
- Treat **Business Impact Analysis**, **Continuity Plan**, continuity **Restore Test** and **Recovery Evidence** as aggregate-owned releases, events or observations. They do not require independent model identities inside this contour.
- Treat **Backup / Data Protection Policy** as an identifier-unassigned new-model candidate. It has an independent owner and lifecycle, applies beyond continuity plans and is executed by platform systems.
- Keep backup execution records and recovery points with the backup/platform observation source. WM-ACT-043 references them.
- Keep restore verification structurally distinct from policy. A continuity restore test is an exercise event in WM-ACT-043; a reusable cross-domain restore-verification contract may later justify its own profile after registry allocation.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

WM-ACT-043 owns continuity capability identity and lineage, BIA releases, approved recovery objectives, strategy and plan releases, readiness assertions, exercises, activations, continuity-mode observations, recovery verification, reconstitution and closure. Service, activity, system, dataset, person, facility, supplier, contract, incident, risk, dependency, observation and SLO masters remain external.

Impact tolerance, recovery objective, contractual commitment and observed outcome are four different assertions. Dependency membership and recovery order are also separate: the order is a versioned derived artifact with predecessor constraints, parallel branches, prerequisite criteria, source graph version and completeness declaration.

## BIA and objectives

A BIA release binds scope, method version, impact categories, severity over time, maximum tolerable disruption, rationale and approval. Each RTO, RPO, capacity or minimum-service objective names its subject, scope qualifier, degraded level, pinned BIA release, verification method and feasibility basis.

RTO must not exceed maximum tolerable disruption unless an explicit exception and residual-risk acceptance exists. RPO must not exceed tolerable data loss under the same rule. Targets never become outcomes merely because they are approved.

## Policy, backup and restore

Backup policy, backup execution and restore verification have different owners and identities. A policy defines protection scope, schedule, copy and placement rules, retention, immutability or isolation, encryption and key custody, verification cadence and exceptions. A job record reports execution and a recovery point. Restore verification pins the policy version, recovery-point identity and digest, isolated target, tool versions, fixture version, criteria and observation method.

A green backup job proves only its declared write-time checks. It does not prove restorability, dependency order, RTO, RPO, minimum service or production-scale behavior. RPO is measured from disruption time to recovery-point time. RTO is measured to verified minimum-service acceptance, not file restoration.

## Exercises, dependencies and evidence

Exercises remain bounded observations under declared assumptions, injects, safety controls and fixture limitations. They do not prove real-event capability. Production restoration is an activation, not a test. Restoration, recovery, reconstitution and closure remain separate states.

Recovery order explicitly includes bootstrap dependencies such as identity, network, DNS, key and secret recovery. Cycles require a declared break point and fallback. A chain result cannot omit an unavailable required dependency.

Released analyses, strategies, plans, exercise results and recovery evidence are append-only. Corrections create successors. Outcome vocabulary includes verified, verified-with-limitations, failed, blocked-by-dependency, indeterminate-insufficient-observation and not-attempted.

## Acceptance result

Synthetic service S depends on identity A, database D and signing supplier X. Thirty green backup jobs exist for D. D restores from a recovery point twelve hours old into an isolated environment and passes object-level checks; A restores; X is unavailable. D is `verified` only at object scope, while the chain is `blocked-by-dependency`. A one-hour RPO is breached and RTO is not attained because minimum service is unavailable. S stays in continuity mode and closure is refused.

## Required invariants

1. Tolerance, objective, commitment and outcome remain distinct.
2. Every recovery objective names scope, degraded level, pinned inputs and verification method.
3. RTO is bounded by maximum tolerable disruption or an accepted exception.
4. Policy, backup execution and restore verification have separate identities and owners.
5. Backup-job success never proves restorability, RTO or RPO.
6. RPO uses recovery-point time; RTO ends at verified service acceptance.
7. Recovery order is versioned and carries a completeness declaration.
8. Identity and key recovery are first-order dependencies.
9. Synthetic tests declare representativeness and limits.
10. Production restoration is an activation, not a test.
11. Exercise, activation, restoration, recovery, reconstitution and closure remain distinct.
12. Partial, blocked and indeterminate outcomes are first-class.
13. Released plans and evidence are immutable and explicitly superseded.
14. Referenced masters never transfer ownership into WM-ACT-043.
15. Activation, disclosure, risk acceptance and disposal require explicit authority.

## Holds

WM-ACT-043 is published only as a non-canonical reviewable draft. Composition and interoperability remain gaps. The WM-ACT-008 parent and WM-ACT-042 reference are unapproved. The specification lacks a backup-policy object, recovery-order artifact, RTO/MTPD consistency rule, outcome vocabulary, test-isolation rules, fixture limits and explicit key-recovery dependency. Provider-waiver and timeout records conflict. The Backup / Data Protection Policy candidate has no allocated identifier. No installable release, standards conformance or publication readiness is claimed.


## Provider reconciliation

# EM-RSK-04 provider comparison

Claude and Grok agree that WM-ACT-043 owns BIA and ContinuityPlan releases, RestoreTest is an exercise event, RecoveryEvidence is scoped observation/evidence, and Backup / Data Protection Policy is the sole identifier-unassigned new-model candidate. Policy, platform execution observations, reusable restore verification, test occurrence and evidence remain distinct.

Grok sharpens the boundary: Backup Policy and reusable Restore Verification require two identities, but only Backup Policy is a new model. Restore Verification is a reusable WM-ACT-043-owned specification instantiated by RestoreTest and must never profile Backup Policy. A versioned recovery-order artifact belongs to a ContinuityPlan release; tests pin its version and explicit bootstrap dependencies.

Impact tolerance, recovery objective, contractual commitment and observed outcome are separate claims. RTO <= MTPD and RPO <= tolerable loss apply only to the same aggregate, scope and release pair. Green jobs do not prove either objective. Evidence scope and time bound every claim; isolation and fixture limitations cap it. Outcomes include pass, partial and blocked, and any unmet required dependency forbids chain-recovered.

```
## PROVIDER COMPARISON
```
# EM-RSK-04 provider comparison

Claude and Grok agree that WM-ACT-043 owns BIA and ContinuityPlan releases, RestoreTest is an exercise event, RecoveryEvidence is scoped observation/evidence, and Backup / Data Protection Policy is the sole identifier-unassigned new-model candidate. Policy, platform execution observations, reusable restore verification, test occurrence and evidence remain distinct.

Grok sharpens the boundary: Backup Policy and reusable Restore Verification require two identities, but only Backup Policy is a new model. Restore Verification is a reusable WM-ACT-043-owned specification instantiated by RestoreTest and must never profile Backup Policy. A versioned recovery-order artifact belongs to a ContinuityPlan release; tests pin its version and explicit bootstrap dependencies.

Impact tolerance, recovery objective, contractual commitment and observed outcome are separate claims. RTO <= MTPD and RPO <= tolerable loss apply only to the same aggregate, scope and release pair. Green jobs do not prove either objective. Evidence scope and time bound every claim; isolation and fixture limitations cap it. Outcomes include pass, partial and blocked, and any unmet required dependency forbids chain-recovered.

```
## ALLOCATION CANDIDATE
```json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-RSK-04","proposedName":"Backup / Data Protection Policy","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed protection policy remains identifiable across continuity plans, protected subjects and backup executions while its approved controls evolve through versions.","versionIdentity":"Changes to scope, schedule, copy placement, retention, isolation, encryption, key custody, verification cadence or exception rules create immutable effective-dated versions.","independentLifecycle":["draft","reviewed","approved","effective","suspended","superseded","retired"],"mastership":"data protection or platform resilience policy authority"},"boundary":{"owns":["persistent protection-policy identity","protected scope and classification rules","backup schedule and recovery-point rules","copy count, placement, isolation and immutability controls","retention and disposal rules","encryption and key-custody requirements","restore-verification cadence and acceptance policy","exception, approval, supersession and retirement history"],"references":[{"target":"WM-ACT-043","purpose":"Business continuity capability, plan, exercise and recovery evidence"},{"target":"WM-ACT-008","purpose":"Plan-release boundary where applicable"},{"target":"WM-ACT-042","purpose":"Recovery or resilience activity boundary under review"},{"target":"WM-XCT-037","purpose":"Dependency and recovery-order evidence"},{"target":"WM-SFT-016","purpose":"Reliability objective and observed outcome separation"}],"excludes":["backup job execution or recovery-point observation","restore test or production restoration event","business impact analysis or continuity plan identity","service, dataset, system, key or storage identity","RTO, RPO, tolerance or contractual commitment mastership","incident activation, recovery, reconstitution or closure decision"]},"objects":{"BackupDataProtectionPolicy":{"identity":["backupDataProtectionPolicyId"],"required":["name","ownerRef","status"],"optional":["successorRef","retiredAt"],"lifecycle":["draft","reviewed","approved","effective","suspended","superseded","retired"]},"PolicyVersion":{"identity":["backupDataProtectionPolicyId","version"],"required":["protectionScope","scheduleRules","retentionRules","verificationCadence","validFrom","contentDigest","status"],"optional":["copyPlacementRules","isolationRules","immutabilityRules","encryptionRequirements","keyCustodyRequirements","exceptionRules","validTo","supersedesVersion"],"lifecycle":["draft","approved","effective","superseded","withdrawn"]}},"invariants":["Policy, backup execution and restore verification retain separate identities and owners.","Every backup execution and restore verification pins the effective policy version.","A green backup job proves only its declared write-time checks.","Backup success never proves restorability, dependency order, RTO, RPO, minimum service or production-scale behavior.","Policy versions are immutable and corrections create successors.","Protected scope, exclusions and approved exceptions are explicit.","Retention, disposal, isolation, encryption and key custody rules remain independently auditable.","Restore verification declares recovery point, digest, isolated target, tool versions, fixtures, criteria and observation method.","RPO is measured from disruption time to recovery-point time and is not owned by the policy.","RTO ends at verified minimum-service acceptance and is not inferred from file restoration.","Unavailable bootstrap dependencies can block chain recovery despite successful object restoration.","Production restoration is an activation and never reclassified as a test."] ,"holds":["Registry namespace and identifier allocation are pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","WM-ACT-043 composition, recovery-order and objective-consistency rules require completion.","Reusable cross-domain Restore Verification remains a separate boundary question.","Package conversion and live verification are pending."]}

```
## PROFILE CANDIDATE
```json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-RSK-04","name":"Enterprise Business Continuity and Recovery","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ACT-043"],"constraints":["Business Impact Analysis, Continuity Plan, continuity Restore Test and Recovery Evidence remain aggregate-owned releases, events or observations.","Impact tolerance, recovery objective, contractual commitment and observed outcome remain distinct assertions.","Recovery order is versioned with predecessor constraints, parallel branches, bootstrap dependencies, source graph pin and completeness declaration.","RTO cannot exceed maximum tolerable disruption and RPO cannot exceed tolerable data loss without explicit exception and accepted residual risk.","Exercises declare assumptions, isolation and fixture limitations and never prove real-event capability.","Restoration, recovery, reconstitution and closure remain separate states with partial, blocked and indeterminate outcomes."],"holds":["WM-ACT-043 remains non-canonical and its composition and interoperability gaps block publication.","WM-ACT-008 and WM-ACT-042 relation approvals remain pending."]}

```
## FIXTURES
```json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Backup / Data Protection Policy","cases":[{"id":"pinned-policy-restore","kind":"positive","input":"A database restore pins policy version 4, recovery point digest, isolated target, tools and fixtures.","expect":"The verification is reproducible and remains distinct from the policy and backup job."},{"id":"blocked-service-chain","kind":"positive","input":"Database and identity restore, but an external signer is unavailable.","expect":"Object restores may be verified while the service chain is blocked by dependency."},{"id":"rpo-breach","kind":"positive","input":"The usable recovery point is 12 hours old against a one-hour RPO.","expect":"The RPO is breached even if object-level restoration succeeds."},{"id":"green-job-proves-recovery","kind":"negative","input":"Thirty green backup jobs are used to assert service recovery and RTO attainment.","expect":"The inference is rejected."},{"id":"file-restore-equals-rto","kind":"negative","input":"RTO stops when files are restored before minimum service is accepted.","expect":"The measurement is rejected."},{"id":"test-equals-production","kind":"negative","input":"A synthetic exercise is treated as proof of real-event capability.","expect":"The claim is rejected without declared representativeness and limits."},{"id":"policy-owns-execution","kind":"negative","input":"The policy record is mutated for every backup job execution.","expect":"The ownership and identity merge is rejected."}]}

```
