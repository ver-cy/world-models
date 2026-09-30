# EM-TEC-07 local synthesis

## Disposition

- Reuse WM-SFT-006 as the Vulnerability aggregate. No new Vulnerability root is needed.
- Keep product/package-version affectedness as source-qualified assertions inside WM-SFT-006.
- Profile WM-ACT-034 as the deployed-instance **Affectedness / Exposure Assessment** root. It owns contextual exposure, environmental risk, priority and remediation-status conclusions for one deployment subject.
- Profile WM-ACT-006 for remediation work. Fix availability, build inclusion, deployment and verification remain facts in their respective masters.
- Keep public exploitation signals in WM-SFT-006. Propose one identifier-unassigned **Exploit Artifact** candidate for independently managed proof-of-concept or weaponized code. Exploitation observations and incidents remain separate evidence/event records.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Vulnerability identity is qualified by issuing namespace and authoritative identifier; CVE is one possible namespace. Weakness, advisory, component, package, build, deployment, exploit artifact, incident and remediation task retain independent identity and lifecycle.

WM-SFT-006 owns source-qualified vulnerability descriptions, aliases, weakness mappings, product/version/configuration affectedness, generic severity and public exploitation signals. WM-SFT-007 owns component/package identity, WM-SFT-008 build/release content, WM-SFT-009 deployment identity and outcomes, WM-SFT-012 manifest evidence, WM-ACT-006 remediation work and WM-ACT-020 incident identity.

## Product affectedness and deployed exposure

Product-level affectedness records ecosystem/version scheme, ranges, introduced/fixed/last-affected events, configuration conditions, justification, source and confidence. VEX-like statuses are assertions at this scope.

Instance exposure assesses a pinned deployed instance against a pinned WM-SFT-006 revision. Evidence may include SBOM component presence, build content, runtime/configuration observation and reachability analysis. Presence, loading, reachability and attacker-controlled reachability are distinct criteria. Unknown manifest completeness or missing observation yields `undetermined`, never `not affected`.

## Severity, risk and exploit evidence

CVSS base/threat severity, EPSS probability, KEV inclusion and SSVC decision are separate time-varying signals. Instance environmental risk and remediation priority belong to the exposure assessment and cite asset criticality, controls and exposure surface. Generic severity never becomes local risk by relabelling.

KEV/EPSS signal, exploit artifact, estate exploitation observation and incident are four different identities. Signal does not prove an artifact; artifact does not prove estate exploitation; observation does not automatically qualify an incident. Exploit artifacts are restricted by default and never authorize generating exploitation instructions.

## Fix, remediation and verification

Fix availability, build inclusion, deployment and instance verification are independently timed and evidenced. A fixed version or patch reference is not proof it entered a build. Build inclusion is not deployment. Deployment is not verification. A task in terminal state records work status only.

Exposure becomes `fixed` only after the target deployment pins the remediating build and a superseding assessment verifies the relevant version/configuration/reachability criteria. Corrections create successors; withdrawn or corrected vulnerability revisions make dependent conclusions stale.

## Acceptance result

Component C 2.4.1 is affected only when feature F is enabled. Build B contains fixed C 2.4.3. Instance I1 still runs the old release with F disabled and is `not_affected (configuration)` until its observation expires or F changes. I2 runs the old release with F enabled and reachable, so it remains `affected`. Closing its remediation ticket because B exists changes no exposure conclusion. Only deployment of B to I2 plus verification creates a superseding `fixed` assessment. A transitive CVE presence proves neither reachability, exploitation nor incident.

## Required invariants

1. CVE is not the only valid vulnerability identifier.
2. Affectedness states ecosystem/version scheme, range and configuration.
3. Product affectedness never implies deployed-instance exposure.
4. Missing inventory or observation yields undetermined, never not-affected.
5. Not-affected requires a justification and evidence.
6. Severity, exploitation probability, known exploitation, risk and priority remain distinct.
7. Presence, loading, reachability, exploitation and incident remain distinct.
8. Fix availability, build inclusion, deployment and verification remain distinct.
9. Closed remediation work never proves remediation outcome.
10. Conclusions are scoped, as-of and explicitly superseded.
11. Corrected vulnerability revisions stale dependent exposure conclusions.
12. No deletion cascades across vulnerability, component, build, deployment, evidence or incident masters.

## Holds

WM-SFT-006 and adjacent bases are non-canonical reviewable drafts. VEX ownership conflicts between WM-SFT-008 and WM-SFT-012. WM-SFT-007 duplicates affectedness/remediation verdicts. Reachability ownership and staleness propagation are unresolved. WM-SFT-006 has no approved outgoing relation contracts. The Exploit Artifact candidate has no registry allocation. Crosswalks and fixtures for CVE, NVD, OSV, CSAF, VEX, STIX, CWE and CVSS are unverified. No installability or publication-readiness claim is made.

## Frozen semantic audit remediation (2026-09-30)

The sole Claude Opus frozen audit accepted the disposition and reported 17 material binding defects. All 17 were remediated without a rerun. VEX is now exclusively mastered on WM-SFT-006 while conflicting base texts remain explicit holds. The WM-ACT-034 exposure profile now has opaque independent identity, lifecycle, disjoint instance vocabulary, revision pinning, derived staleness, evidence expiry, typed predicates, fixed mastership splits, privacy rules and a normative LS-1…LS-16 invariant set. Exploit Artifact now has deterministic artifact-versus-rendition versioning, product/component target scope, inbound-only estate relations, separate handling and lifecycle axes, disposal semantics and an explicitly pending mastership authority.

The fixture corpus is split into allocation and profile sets with deterministic oracles, fixed time, invariant references, expected statuses and rejection reasons. The candidate remains identifier-unassigned and every named base remains a non-canonical draft.
