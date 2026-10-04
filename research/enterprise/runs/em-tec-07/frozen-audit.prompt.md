# Frozen semantic audit prompt — EM-TEC-07

You are the sole frozen semantic auditor for this contour. This audit is run exactly once. Use only the supplied text. Do not browse, call tools, invent identifiers, produce exploit instructions, claim standards conformance or propose publication of blockers.

Audit the reconciled EM-TEC-07 boundary and its allocation/profile/fixture artifacts for internal contradictions, identity or mastership leaks, unsafe inference, underspecified lifecycle/version/time/evidence semantics, non-deterministic fixtures and missing publishability holds. Preserve the intended decision unless the supplied evidence disproves it: reuse WM-SFT-006; profile WM-ACT-034 and WM-ACT-006; keep VEX with WM-SFT-006; retain one identifier-unassigned Exploit Artifact candidate; allocate no runtime/model ID.

Return Markdown with: Verdict; numbered Material defects only; for each defect give exact deterministic remediation; Exact additional fixtures as a JSON array; and a final freeze decision. Be sceptical and concise. If there are no material defects, say so explicitly. Never request another provider run.

## LOCAL SYNTHESIS

```text
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
```

## CLAUDE FROZEN STUDY

```text
# EM-TEC-07 — Уязвимость, затронутость и устранение

## Verdict
Reuse WM-SFT-006 as the vulnerability root; do not create a new vulnerability model. Split `AffectednessAssessment` in two: product/package-version affectedness stays a **contained, source-qualified assertion inside WM-SFT-006**; deployed-instance exposure becomes a **root** realised as a profile of WM-ACT-034. `Remediation` is **not a root**: fix availability is contained in WM-SFT-006, build inclusion in WM-SFT-008, deployment in WM-SFT-009, verification in WM-SFT-009's post-deployment outcome, the work in a WM-ACT-006 profile, and the per-(vulnerability, instance) remediation status is a contained assertion on the exposure root. `ExploitEvidence` splits: public exploitation *signal* is contained in WM-SFT-006; the exploit **artifact/observation** needs one identifier-unassigned new root; the realised event is WM-ACT-020 by reference. No identifiers allocated.

## Evidence
WM-SFT-006 (complete spec, 159 582 bytes, sha256 3d39ea38…) already owns authority-qualified identity, aliases, CWE mappings, affected product/version/configuration assertions with justification, CVSS/EPSS/KEV/SSVC containers, fix and exposure links, supersession and purpose-bound projections. Its own boundary notes separate weakness, product, deployed-asset exposure, advisory/remediation and exploit/incident. Its adjudication accepts "affected product versus deployed exposure" as separate boundaries. WM-SFT-007, ‑008, ‑009, ‑012, WM-ACT-006, ‑020, ‑034 and WM-KNW-007 are all reviewable drafts with boundary-review or single-provider holds; none owns instance exposure, reachability or VEX status.

## Identity/mastership
Vulnerability identity: authoritative source-system identifier qualified by issuing namespace (WM-SFT-006 identity_priority) — CVE is one namespace among OSV, GHSA, vendor and pre-publication local reports. Component/package identity: WM-SFT-007 (registry-of-record key, then purl). Build/release: WM-SFT-008. Deployed instance: WM-SFT-009 (never release tag, digest or environment name). Exposure assessment: its own master identifier (WM-ACT-034 identity priority), never the tuple of CVE + host. Exploit artifact: new root, its own identifier. Mastership rule: one authority per fact; no model copies another's lifecycle.

## Vulnerability/advisory/weakness
Three distinct identities. Weakness class (CWE) is a recurring error pattern, mapped with classifier version, method and confidence — never identity. Advisory groups vulnerabilities, products and remedies and has its own authority; WM-SFT-006 holds it as a typed reference. Vulnerability record identity is source-qualified: aliases, upstream and related are distinct relation semantics and never license a merge. Description, product name, CWE, score, date and digest are barred from canonicalisation.

## Affectedness/exposure
Layer 1 (contained in WM-SFT-006): product-status assertion with range scheme, introduced/fixed/last-affected events, **configuration constraints**, justification and source confidence. VEX-like statuses (affected, not_affected with justification code, fixed, under_investigation) attach here at product scope.
Layer 2 (root, WM-ACT-034 profile): instance exposure — subject = WM-SFT-009 deployed instance, criteria bound to the pinned WM-SFT-006 revision and its version/configuration conditions, evidence = WM-SFT-012 SBOM component presence, WM-SFT-008 build contents, runtime/config observation, reachability determination. Transitive-dependency **reachability** is a criterion with its own evidence and confidence (present → loaded → reachable → reachable-under-attacker-controlled-input), not an inference from presence. SBOM completeness limits and closure "known unknowns" cap the conclusion: unscanned or unknown-completeness returns *undetermined*, never *not affected*.
**Contradiction:** WM-SFT-008 assigns VEX to WM-SFT-012, while WM-SFT-012 explicitly excludes VEX and CSAF authoring. No model owns VEX status. **Contradiction:** WM-SFT-007 `f-affectedness` and `f-remediation-status` keep a local affectedness verdict, exploitability and remediation decision, duplicating WM-SFT-006 and the exposure root. Resolve: WM-SFT-006 owns source-qualified product assertions, the exposure root owns instance conclusions, WM-SFT-007 retains at most a cached verdict marked non-authoritative.

## Severity/risk/priority
Generic severity = CVSS Base (+Threat) with full vector, version, assessor, scope and scoring time, in WM-SFT-006. Exploitation probability (EPSS), known exploitation (KEV) and decision priority (SSVC) are separate, non-interchangeable, time-varying signals in WM-SFT-006. **Environmental risk and remediation priority are instance-scoped** and belong to the exposure root: CVSS Environmental metrics, asset criticality, compensating controls, exposure surface. WM-SFT-006 retains only a reference to that local decision; it must not host environmental scores.

## Exploit evidence/incident
Four separable things: (1) *signal* — KEV inclusion or EPSS probability, contained in WM-SFT-006, with catalogue/model version and scoring date; (2) *exploit artifact* — PoC or weaponised code with independent identity, publication state, maturity and access restriction: **no registered model owns it** → one identifier-unassigned new root, restricted-by-default, with an explicit prohibition on generating exploitation instructions; (3) *exploitation observation against our estate* — an observation referenced by the exposure root, raising exposure confidence; (4) *incident* — WM-ACT-020, requiring its own qualification and declaration decision. Signal ⇏ artifact ⇏ observation ⇏ incident.

## Fix/remediation/verification
Four independently timed facts. Fix availability (fixed version, patch, commit, workaround) — WM-SFT-006 contained reference. Build inclusion — WM-SFT-008 change content and security-fix references, provable by artifact digest and SBOM. Deployment — WM-SFT-009 occurrence installing a pinned release to a target. Instance verification — WM-SFT-009 post-deployment outcome plus a re-run exposure assessment concluding *fixed*. Remediation **work** = WM-ACT-006 profile (authorisation, state, dependencies, acceptance). Closure evidence ≠ task terminal state: a Task reaching `completed` is a work fact; remediation status is an assertion on the exposure root, grounded in cited evidence.

## Time/version/scenario
Distinguish disclosure/publication, modification, exploitation-observation, fix-availability, build, deployment, observation and knowledge times; all RFC 3339 with seconds and explicit offset. Every exposure conclusion is as-of and carries maximum staleness. Version conditions pin range scheme and ecosystem ordering; no cross-scheme ordering is assumed. Supersession: a new exposure assessment supersedes, never overwrites; a rejected, withdrawn or corrected WM-SFT-006 revision must mark dependent exposure assessments **stale** — no propagation mechanism exists today (gap). Privacy/access: exposure records disclose estate weakness and are deny-by-default; embargoed advisories, reporter contacts and exploit artifacts are separately restricted; WM-ACT-034's privacy gap and WM-SFT-009's actor-identifier sensitivity both apply.

## Acceptance scenario
Component C 2.4.1 is *conditionally affected*: WM-SFT-006 asserts affected range < 2.4.3 **only when** feature flag F is enabled. Build B includes C 2.4.3 — WM-SFT-008 records inclusion; this alone changes nothing about exposure. Instance I1 runs the prior release with F disabled → exposure conclusion *not_affected (configuration)*, evidenced by config observation, valid until F changes. Instance I2 runs the prior release with F enabled and C reachable → *affected*; a WM-ACT-006 remediation task is raised. I2 is not yet updated: the task may be closed as "release available", but the exposure root still reports *affected* until a WM-SFT-009 deployment of B to I2 plus verification yields a superseding *fixed* conclusion. Rejected: "CVE in a transitive dependency ⇒ exploitable ⇒ incident" (presence ⇏ reachability ⇏ exploitation ⇏ qualified incident), and "closed ticket ⇒ remediated".

## Invariants
1. CVE is not the only admissible identifier. 2. Every affectedness assertion names version scheme, range and configuration conditions. 3. A closed ticket is not remediation evidence. 4. Product affectedness never implies instance exposure. 5. Absence of scan is *undetermined*, not *not affected*. 6. `not_affected` requires a justification code plus evidence. 7. Severity, exploitation probability, known exploitation and local priority are never the same measure. 8. Fix availability, build inclusion, deployment and verification are four separately evidenced facts. 9. Every conclusion is as-of, scoped and superseded rather than overwritten. 10. No cascade deletion to vulnerabilities, builds, instances, evidence or incidents.

## Minimal model set
Root: WM-SFT-006 (reuse). Root: WM-ACT-034 profile — instance exposure, environmental risk, priority, remediation status. Profile: WM-ACT-006 — remediation task. New (identifier-unassigned): exploit artifact / exploitation observation. References: WM-SFT-007, WM-SFT-008, WM-SFT-009, WM-SFT-012, WM-ACT-020, WM-KNW-007 (contested reachability/attribution claims only, to avoid duplicating WM-SFT-006's assertion containers).

## Holds
WM-SFT-006 is a codex-only reviewable draft with independent review waived; WM-SFT-007/‑008/‑009/‑012/WM-ACT-006/‑020/‑034/WM-KNW-007 carry boundary-review, single-provider, source-pin and relation-ledger holds. No approved outgoing relations exist for WM-SFT-006; required product/package references are unbacked by ledger rows. VEX ownership, reachability ownership, staleness propagation and WM-SFT-007 duplication are unresolved. CVE/NVD/OSV/CSAF/VEX/STIX/CWE/CVSS crosswalks and fixtures are unverified. No claim of canonical completeness, installability or publication readiness.
```

## GROK EXACT RESPONSE

```text
**Verdict.** Conditionally accept. Reuse WM-SFT-006 as the Vulnerability root. Profile WM-ACT-034 as the deployed-instance Exposure Assessment root. Profile WM-ACT-006 as remediation work. Keep fix availability, build inclusion, deployment, and instance verification in their respective masters. Do not mint identifiers. Drafts remain drafts; this review does not claim publication readiness.

**Independent identity and VEX.** Instance exposure requires independent identity: the WM-ACT-034 profile is a first-class conclusion object, not a field on Vulnerability, Component, Package, SBOM, Build, or the instance record. Exploit Artifact requires independent identity as a candidate class only and remains identifier-unassigned; this review assigns no ID. VEX ownership is resolved to WM-SFT-006 source-qualified product/version/configuration affectedness. Instance exposure may cite VEX and must not rewrite it. VEX is not owned by the instance, the WM-ACT-006 ticket, the artifact candidate, or the cyber-incident draft.

**Strongest evidence.** The prescribed test: one WM-SFT-006 vulnerability; component C conditionally affected under a source-qualified configuration predicate; build B already contains the fixed version of C; deployed instance I still runs the old reachable configuration. Four facts require four masters. Collapsing any pair falsifies the others.

**Strongest counterexample.** Treating SBOM or transitive presence of C as exploitability or as a cyber-incident; or treating a closed WM-ACT-006 ticket as proof that I is remediated while I still runs the old reachable configuration.

**Identity/mastership.** WM-SFT-006 is the sole Vulnerability root. Source-qualified affectedness is an internal facet of that root, not a second master. Component/package, build/release, deployment, SBOM, task, assessment, claim, and cyber-incident drafts keep mastership of their own facts. Exploitation observation stays off both the artifact candidate and the vulnerability root. Work identity, status conclusion, and instance verification are three identities.

**Vulnerability/advisory/weakness.** WM-SFT-006 is the product-facing Vulnerability root. An advisory is a sourced claim about that vulnerability; a weakness is a defect class. Neither is the vulnerability identity. Public exploitation signals (known-exploited catalog membership, public-exploit-available assertions) are source-qualified statements on WM-SFT-006 about the vulnerability, not about any instance.

**Affectedness/exposure.** VEX lives on WM-SFT-006: affected / not_affected / fixed / under_investigation plus conditional justification and the configuration/reachability predicate. Conditionally affected is first-class; component presence is not automatic affectedness. Instance exposure is not VEX. The WM-ACT-034 profile owns reachable-in-this-context, environmental risk, local priority, and the instance remediation-status conclusion. Product-level not_affected does not close exposure for an instance running a different reachable configuration. Product-level affected does not create exploitability, observation, or incident. A later fixed build does not rewrite historical VEX and does not change I while I still runs the old reachable config. SBOM/transitive inclusion is inventory, not affectedness and not exposure.

**Severity/risk/priority.** Keep six distinct assertions. CVSS: base/severity cited on WM-SFT-006. EPSS: source-qualified exploit-probability signal, not priority. KEV: public known-exploited catalog membership on WM-SFT-006. SSVC: decision-framework output, not a CVSS rewrite. Environmental risk and local priority: instance-context, WM-ACT-034 profile. None substitutes for another. Public KEV does not set instance priority.

**Exploit evidence/incident.** Public exploitation signals stay on WM-SFT-006. Exploit Artifact is an independently managed candidate with no identifier assigned here. Artifact existence is not observation and not incident. Exploitation observation is a separate assessment/claim fact. Cyber-incident is a separate draft master and requires occurrence evidence. Forbidden inferences: artifact implies observation; observation implies this-instance incident; SBOM edge implies exploitability; affectedness implies incident.

**Fix/remediation/verification.** Fix availability stays with the software/fix master associated to WM-SFT-006. Build inclusion stays with build/release. Deployment stays with the deployment master. Instance verification stays with instance/deployment verification evidence. WM-ACT-006 is remediation work only. WM-ACT-034 may conclude instance remediation-status only from verification evidence, never from ticket state. Build B containing the fix is not I remediated. Closed work is not verified remediation.

**Time/version.** Do not merge clocks: vulnerability published/modified; VEX asserted; fix available; build produced; build deployed; instance still on old version/config; exposure assessment performed; work opened/closed; instance verification performed. Product version ≠ build identifier ≠ deployed instance version/configuration. Assessment time ≠ ticket-close time ≠ verification time.

**Scenario.** Vulnerability V is mastered on WM-SFT-006. Component C is conditionally affected; the predicate is required. Build B includes the fixed version of C. Instance I still runs the old reachable configuration of C. VEX on V/C remains conditionally affected for the old product/version/config. B proves fix inclusion in a build only. I remains exposed under the WM-ACT-034 profile until verification shows otherwise. An ACT-006 ticket may close without changing I. Neither C-in-SBOM nor a transitive of C proves exploitability or creates an incident.

**Invariants.**
1. Vulnerability identity ≠ advisory identity ≠ weakness identity.
2. Product/version/configuration VEX is mastered only on WM-SFT-006 and is source-qualified.
3. Instance exposure requires independent identity (WM-ACT-034 profile) and must not exist only as a field on WM-SFT-006 or the instance master.
4. Affectedness does not imply exposure; exposure does not imply incident.
5. A build containing a fixed version does not imply the deployed instance is remediated.
6. Closed WM-ACT-006 work does not imply verified remediation; ACT-034 status may cite work but is not identical to work state.
7. Transitive/SBOM presence does not imply affectedness, exploitability, or incident.
8. CVSS, EPSS, KEV, SSVC, environmental risk, and local priority are distinct assertions with distinct owners.
9. Public exploitation signal on WM-SFT-006 ≠ Exploit Artifact ≠ exploitation observation ≠ cyber-incident.
10. Fix availability, build inclusion, deployment, and instance verification have separate masters and separate times.
11. Conditionally affected requires an explicit predicate; absence of a predicate must not default to exploited or remediated.
12. Claim objects may transport VEX or assessment assertions but do not master affectedness, exposure, or incident.
13. Exploit Artifact may be independently identified as a candidate class and remains identifier-unassigned.

**Minimum model set** (reuse only): WM-SFT-006 Vulnerability with source-qualified affectedness/VEX and public exploitation signals; component/package draft; build/release draft; deployment/instance draft; SBOM draft; WM-ACT-034 profiled Exposure Assessment; WM-ACT-006 profiled remediation work; task draft if distinct from ACT-006; assessment draft; claim draft; cyber-incident draft; Exploit Artifact as identifier-unassigned candidate only.

**Blockers.** Exploit Artifact has no assigned identifier and cannot be treated as a minted master. Dual-write risk if VEX status is copied onto instance records or tickets. WM-ACT-034 remediation-status can be mistaken for WM-ACT-006 workflow state. Conditional-affectedness predicates and reachability evidence are required by the test and may be underspecified in the drafts. Claim objects must be barred from asserting exploitability or incident from SBOM edges or ticket closure. Identifier discipline: reuse named models only. Draft masters remain drafts.
```

## PROVIDER COMPARISON

```text
# EM-TEC-07 provider comparison

Claude and Grok agree on the core boundary: reuse WM-SFT-006 as the sole Vulnerability root; keep source-qualified product/version/configuration affectedness and VEX there; use a WM-ACT-034 profile as a first-class deployed-instance Exposure Assessment; use WM-ACT-006 only for remediation work; and retain fix availability, build inclusion, deployment and instance verification in their respective masters.

Both reviews preserve the separations among advisory, weakness and vulnerability; product affectedness and deployed exposure; CVSS, EPSS, KEV, SSVC, environmental risk and local priority; public exploitation signal, Exploit Artifact, exploitation observation and incident; and work closure versus verified remediation. Both reject transitive or SBOM presence as proof of exploitability or incident and reject a closed ticket or fixed build as proof that a still-old deployment is remediated.

Grok resolves two open calls. Instance exposure has independent identity as the WM-ACT-034 profile and must not be a field on vulnerability, component, SBOM, build or instance masters. Exploit Artifact also has independent candidate identity but remains identifier-unassigned; no identifier is minted. VEX mastership belongs only to WM-SFT-006 as a source-qualified product/version/configuration assertion. Instance exposure may cite VEX but cannot rewrite it, and VEX is not owned by the instance, remediation task, artifact or incident.

The remaining blockers are structural: prevent dual writes of VEX, prevent conflation of WM-ACT-034 remediation status with WM-ACT-006 workflow state, require explicit conditional predicates and reachability evidence, bar claim carriers from turning inventory edges or work closure into exploitation or incident conclusions, preserve all separate clocks, and keep every referenced draft explicitly non-canonical.
```

## ALLOCATION CANDIDATE

```text
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-TEC-07","proposedName":"Exploit Artifact","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An independently managed proof-of-concept or weaponized-code artifact remains identifiable across vulnerability links, analyses, restrictions and observed uses while its bytes and provenance remain fixed.","versionIdentity":"A byte-level or functional change creates a distinct artifact or immutable successor rendition; metadata and access-policy corrections append versions without rewriting captured content.","independentLifecycle":["reported","quarantined","analyzed","restricted","superseded","withdrawn","disposed"],"mastership":"authorized security-research or threat-intelligence evidence authority"},"boundary":{"owns":["persistent exploit-artifact identity","content digest and immutable rendition reference","acquisition provenance and chain of custody","claimed vulnerability and target mappings","capability classification and analysis status","handling, disclosure and access restrictions","supersession, withdrawal and disposal history","authorized observations of artifact behavior"],"references":[{"target":"WM-SFT-006","purpose":"Vulnerability and public exploitation-signal master"},{"target":"WM-SFT-007","purpose":"Component or package identity"},{"target":"WM-SFT-008","purpose":"Build or release content"},{"target":"WM-SFT-009","purpose":"Deployment identity and outcome"},{"target":"WM-SFT-012","purpose":"Manifest and SBOM evidence"},{"target":"WM-ACT-020","purpose":"Cyber incident boundary"},{"target":"WM-ACT-034","purpose":"Deployment exposure assessment"}],"excludes":["vulnerability, weakness or advisory identity","product affectedness or VEX assertion","deployed-instance exposure or local risk conclusion","public exploitation signal, probability or severity score","estate exploitation observation or incident identity","remediation task, fix, build, deployment or verification fact","generation of exploitation instructions or authorization to execute code"]},"objects":{"ExploitArtifact":{"identity":["exploitArtifactId"],"required":["contentDigest","provenance","handlingClass","status"],"optional":["vulnerabilityRefs","targetRefs","capabilityClass","analysisRefs","successorRef","disposedAt"],"lifecycle":["reported","quarantined","analyzed","restricted","superseded","withdrawn","disposed"]},"ArtifactRendition":{"identity":["exploitArtifactId","renditionId"],"required":["digest","mediaType","storageRef","createdAt"],"optional":["encryptionRef","redactionBasis","supersedesRendition"]}},"invariants":["Exploit artifact identity is distinct from vulnerability, exploitation signal, observation and incident identity.","Every stored rendition is immutable and addressed by a verified content digest.","Acquisition provenance and chain of custody are retained for every artifact.","An artifact link to a vulnerability is a sourced assertion and never proves product or instance affectedness.","Public exploitation signals never prove that a specific artifact exists.","Artifact possession or analysis never proves estate exploitation or incident occurrence.","Restricted handling is the default and access requires explicit purpose, scope and audit.","Artifact records never authorize generating instructions or executing content.","Byte-level or functional changes create a new artifact or explicit successor rendition.","Withdrawal or disposal preserves non-content provenance, decisions and historical references.","Exposure assessment pins the vulnerability revision, deployment evidence and observation cut independently of artifact state.","Fix, build, deployment, task completion and verification remain independently timed and evidenced."],"holds":["Registry namespace and identifier allocation are pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","VEX ownership, reachability contracts and staleness propagation require canonical reconciliation.","Security handling, malware-storage and disclosure controls require specialist approval.","Package conversion and live verification are pending."]}
```

## PROFILE CANDIDATE

```text
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-TEC-07","name":"Enterprise Vulnerability Exposure and Remediation","decision":"PROFILE","newRuntimeId":false,"bases":["WM-SFT-006","WM-ACT-034","WM-ACT-006","WM-SFT-007","WM-SFT-008","WM-SFT-009","WM-SFT-012","WM-ACT-020"],"constraints":["WM-SFT-006 owns source-qualified vulnerability descriptions, aliases, weakness mappings, product affectedness and public exploitation signals.","WM-ACT-034 profiles deployed-instance exposure with pinned deployment evidence, configuration, reachability, environmental risk and priority.","Missing inventory or observation yields undetermined, never not affected.","Severity, exploitation probability, known exploitation, local risk and remediation priority remain distinct.","Fix availability, build inclusion, deployment, task completion and instance verification remain separately evidenced.","Exposure becomes fixed only after a superseding assessment verifies the remediating build and relevant configuration or reachability criteria."]}
```

## FIXTURES

```text
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Exploit Artifact","cases":[{"id":"restricted-poc","kind":"positive","input":"A proof-of-concept is acquired with a digest, provenance and restricted handling policy.","expect":"It receives independent artifact identity without creating an incident or exposure verdict."},{"id":"artifact-successor","kind":"positive","input":"A weaponized variant changes functional behavior and bytes.","expect":"A distinct successor artifact is recorded with lineage."},{"id":"conditional-component","kind":"positive","input":"An artifact targets a component only when feature F is enabled while one deployment has F disabled.","expect":"The artifact link remains separate and the deployment assessment may be not affected by configuration with evidence."},{"id":"signal-proves-artifact","kind":"negative","input":"A KEV or EPSS signal is used to assert possession of a specific exploit artifact.","expect":"The inference is rejected."},{"id":"artifact-proves-incident","kind":"negative","input":"Possession of exploit code is treated as proof that an estate was exploited.","expect":"The incident inference is rejected."},{"id":"transitive-presence-proves-exploitability","kind":"negative","input":"A transitive dependency match plus artifact link is treated as reachable exploitation.","expect":"The conclusion is rejected without deployment and reachability evidence."},{"id":"closed-ticket-proves-fixed","kind":"negative","input":"A closed remediation ticket is used to mark exposure fixed.","expect":"The transition is rejected without deployment and verification evidence."}]}
```
