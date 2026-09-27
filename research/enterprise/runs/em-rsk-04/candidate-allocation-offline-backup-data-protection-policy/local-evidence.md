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
