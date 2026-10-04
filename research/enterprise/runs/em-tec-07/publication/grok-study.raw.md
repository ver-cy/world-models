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
