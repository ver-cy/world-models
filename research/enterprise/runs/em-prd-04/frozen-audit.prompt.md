# Single frozen semantic audit — EM-PRD-04

You are the sole independent frozen auditor. No tools, browsing, standards claims, identifier invention or registry mutation. This audit runs exactly once and will not be repeated.

Audit the reconciled proposal and artifacts below. Fixed identity decision: reuse WM-ACT-036 Research Study and WM-KNW-009 Hypothesis; complete reserved WM-ACT-022 narrowly as Experiment Run; study-scoped design is an immutable release inside the study; reusable cross-study Experiment Design genuinely needs independent identity but remains registry-unassigned until allocation; Experiment Attempt has stable subordinate identity; Research Finding has instance identity supplied by the composed existing claim/evidence/study bases and mints no new model identity.

Find material internal contradictions, missing fields, unenforceable invariants, lifecycle/version/provenance defects, missingness/result-state conflation and boundary leaks. Known registry/base publication gaps are holds, not artifact defects. Return:
1. Verdict ACCEPT or REVISE.
2. Numbered material defects with exact evidence.
3. Required bounded fixes.
4. One JSON fenced array of additional fixtures with target, id, kind, input, expect and optional expectedCode, covering every defect.
5. Explicit identifier decision.
6. Freeze decision: closed, no rerun.

## local-evidence.md
# EM-PRD-04 local synthesis

## Disposition

- Reuse WM-ACT-036 as the Research Study aggregate and WM-KNW-009 as the Hypothesis master.
- Complete reserved WM-ACT-022 as **Experiment Run**, an occurrence bound to one immutable design release. A reviewable completion candidate is prepared without a new identifier.
- Treat study-scoped **Experiment Design** as a profile/component of WM-ACT-036 protocol/design releases. Raise a cross-study reusable Experiment Design as an identifier-unassigned candidate only when independently governed reuse is required.
- Profile **Research Finding** across WM-ACT-036 findings, WM-KNW-007 claims and WM-KNW-008 evidence bindings. No new finding identity is needed.

## Identity and lifecycle

Study, hypothesis, design, run, attempt, observation, dataset, analysis and finding remain distinct. Hypothesis survives the studies that test it. Released design versions are immutable. Every run has its own orchestration identity and pins exactly one design version. Retry, rerun and correction append new attempts or successors.

WM-MAT-008 masters observations, WM-DAT-001 datasets, WM-KNW-007 claims and WM-KNW-008 citations/evidence links. The Enterprise profile holds only pinned references and declared composition rules.

## Hypothesis, design and run

Preregistered hypotheses freeze their prospective plan, criteria, success and stopping rules before result access. Timing is verified from event clocks. A later formulation is explicitly post-hoc and names the result set that produced it. Reformulation creates a successor hypothesis revision; it never rewrites the original.

The design release pins questions, outcomes, methods, assignment, analysis intent, success criteria and stopping rules. Each run manifest pins design/component revisions, code/dependency digests, configuration, input dataset versions/partitions/digests, instruments, environment, runtime, randomness and calibration/reference materials. Planned-versus-executed deviation is append-only.

## Observation, analysis and finding

No effect and no data are different. Absence has a coded reason and missingness pattern; zero is asserted; censoring retains direction, bound and limit kind. A null-effect finding requires present observations, estimand and stated precision/power.

Analysis plan, execution, estimate, statistical evidence, interpretation and finding remain separate assertions. Each finding references a pinned hypothesis revision, results and evidence, and records uncertainty, applicability and limitations. Supported, unsupported, refuted and inconclusive are source-qualified assessments, never truth flags.

Negative, null and inconclusive outcomes remain separately typed and retained. A negative result may inform a later decision but cannot mutate the decision or disappear as a failed run.

## Acceptance result

Two runs pin the same design but different input snapshots and random seeds. One supports the hypothesis and the other challenges it. Both manifests and earlier failed attempts remain reproducible and distinguishable. The original hypothesis is unchanged; conflict and aggregate assessment are appended. Nothing is deleted or retroactively restated.

## Required invariants

1. Study, hypothesis, design, run, attempt, observation, analysis and finding have distinct identities.
2. Released designs and completed runs are immutable.
3. Every run pins exact design, inputs, environment, code, configuration and randomness.
4. Hypothesis precedes result access or is marked post-hoc.
5. Deviations are append-only and typed.
6. Absence, censoring and zero remain distinct.
7. Findings state uncertainty, applicability and limitations.
8. Negative, null and inconclusive outcomes remain distinct and retained.
9. Run success proves neither validity nor reproducibility.
10. Deletion never cascades across research evidence.

## Holds

WM-ACT-022 now has a reviewable candidate with explicit run, manifest, attempt and deviation structures, six external relation contracts and seven fixtures. WM-ACT-036 and WM-KNW-009 retain their own publication holds, and relations remain candidate-only. Cross-study Experiment Design and Evidence Artifact remain identifier-unassigned. Exact Grok comparison, one frozen semantic audit, package conversion and live verification are still required; no installable release is claimed yet.

## claude-study.raw.md
# EM-PRD-04 — Independent enterprise metamodel review

## Verdict

Create an **Enterprise research, hypothesis and experiment profile** over three reserved models — WM-ACT-036 (Research Study), WM-KNW-009 (Hypothesis), WM-ACT-022 (Experiment / Trial) — plus reference bindings to WM-KNW-007, WM-KNW-008, WM-MAT-008 and WM-DAT-001. No profile runtime identifier and no model identifier are allocated.

Placement of the five candidate types:

- **ResearchStudy** → reuse WM-ACT-036 unchanged (aggregate root of the inquiry).
- **Hypothesis** → reuse WM-KNW-009 unchanged.
- **ExperimentDesign** → profile of the WM-ACT-036 *protocol and design release* (`release-questions-design-and-protocol`) for study-scoped designs. A design reused **across** studies has identity independent of any study and is raised as a new-model candidate, identifier unassigned.
- **ExperimentRun** → WM-ACT-022, which is reserved but **spec-missing**. It cannot be reused; it must be specified as the run occurrence, not as a design/run composite. This is the single blocking specification gap.
- **ResearchFinding** → profile of the WM-ACT-036 finding assertion, projected to WM-KNW-007 as a claim and bound to WM-KNW-008 for evidence. No new model.

## Evidence

WM-ACT-036 (`77ad83b7…`) already owns protocol and design releases, conduct events, collection, analysis plan and execution, bounded findings, limitations, amendment and no-cascade disposition. WM-KNW-009 (`284dcaba…`) already owns proposition, kind, scope, operationalization, predictions, criteria, preregistration with temporal integrity, deviations, source-qualified assessment and revision. Both explicitly externalise the other's masters, so neither needs extension.

WM-ACT-022 supplies only a registry row: `status: candidate`, `review_state: first-pass-reviewed`, placeholder purpose, empty `composition_role` and `default_link_type`, no `existing_spec_ref`, no document. The relation `WM-ACT-036 CONTAINS WM-ACT-022` is `candidate`. WM-ACT-036's own coverage marks composition a **gap** and records that no approved relation rows were supplied.

## Identity/mastership

Four independent identities, four lifecycles:

1. **Study** — WM-ACT-036, sponsor/PI authority, versioned aggregate.
2. **Hypothesis** — WM-KNW-009, persistent versioned proposition; survives every study that tests it.
3. **Design** — immutable released specification; revised by successor release, never edited.
4. **Run** — orchestration-issued occurrence identity; one design, many runs.

Observations master in WM-MAT-008, datasets in WM-DAT-001, claims in WM-KNW-007, evidence/citations in WM-KNW-008. Decision consequence is external (see EM-KNW-02's WM-KNW-010 boundary). The profile stores references and pins, never copies.

## Study/design/run

Adopt the definition→run→assertion separation already adjudicated in EM-DAT-03 (WM-DAT-005 / WM-ACT-053 / WM-DAT-006). Design releases are immutable; a design version pins questions, outcomes, method, assignment, analysis intent, success rule and stopping rule. A run pins exactly one design version plus its own inputs, environment and randomness. Executed-versus-planned divergence is a recorded deviation and reconciliation finding, never a retroactive design edit. Run success is not result validity, and neither is fitness.

## Hypothesis lifecycle

Preregistered hypotheses carry a frozen prospective plan with verified clocks, a registration digest and permitted-deviation rules. Post-hoc hypotheses are admissible only when marked `post-hoc` at formulation, with the result set that generated them named. Timing is derived from clocks, never asserted: a registration whose timestamp does not precede first result access is rejected as prospective. Reformulation creates a successor revision; prior propositions, criteria and assessments stay resolvable. Assessment values — supported, unsupported, refuted, inconclusive — are source-qualified and append-only; none is a truth flag.

## Inputs/provenance/reproduction

The run manifest is immutable and, per WM-ACT-022's future spec, must enumerate: design and component revision; code and dependency digests; configuration and parameter set with secret references only; each input pinned as dataset version or snapshot plus partition and digest (WM-DAT-001); instrument, observer and deployment references (WM-MAT-008); environment and runtime; randomness — seed, generator, draw order, and any declared nondeterminism; calibration and reference materials in force; effective interval; attempt sequence. Any missing element downgrades the claim from reproducible to explainable or partially reproducible. Reproducibility is a property of the manifest, never of a single successful run.

## Observations/missingness

No effect and no data are different records. WM-MAT-008 already forbids expressing absence as zero, blank or unexplained null and requires coded absence, censoring direction, bound and limit kind. The profile inherits this unchanged: a below-detection result is a bounded determination; an uncollected observation is absent with a reason and a missingness pattern; a suppressed value is marked suppressed. A null-effect finding requires observations present, power or precision stated, and estimand declared. A data-gap finding requires the missingness pattern. Conflating them is rejected.

## Analysis/finding

Analysis plan, analysis execution, estimate, statistical evidence, interpretation and finding remain separate assertions (WM-ACT-036). A finding cites its results, names its relation to a pinned hypothesis revision, and carries uncertainty (kind, value, coverage factor and probability), applicability scope and limitations. Significance is not truth, association is not causation, sample size is not generalizability, one study is not reproducibility. Every finding projected as a claim keeps WM-KNW-007 as claim master and binds evidence through WM-KNW-008 with stance and locator.

## Null/negative/inconclusive

Three distinct outcomes, all first-class and all retained: **negative** (effect absent within stated power and estimand), **null** (non-rejection, which never proves the null), **inconclusive** (criteria unmet, data insufficient, or run invalid). Each links forward to a downstream decision by reference only; the decision, its rationale and its authority stay external. A negative result is publishable evidence and a retention obligation, not a deletable failure.

## Time/version/scenario

Keep independent: hypothesis proposal and registration time; design release time; run start, attempt and completion time; observation phenomenon, result and ingestion time; analysis and assessment time; correction time. All RFC 3339 with seconds and explicit offset. Independent version clocks: hypothesis revision, design release, run/attempt sequence, dataset snapshot, finding assertion supersession. Scenario is the hypothesis's declared conditions, assumptions and exclusions; runs record the conditions actually in force.

## Acceptance scenario

Design D v1.3 is released. Run R1 pins D v1.3, inputs A@s41/B@s17, code digest c9, seed 4711; it observes an effect and yields Finding F1 supporting hypothesis H rev 2. Run R2 pins D v1.3, inputs A@s42/B@s19, same code and environment, seed 4712; it contradicts R1 and yields F2, recorded as challenging H rev 2. Both runs remain distinguishable by manifest and reproducible from their pins. R1's earlier failed attempt is retained. H rev 2 is unchanged; a conflict assessment and an inconclusive aggregate verdict are appended. Neither finding is deleted; neither rewrites the other.

## Invariants

1. Study, hypothesis, design, run, attempt, observation, dataset, analysis and finding identities remain distinct.
2. Released designs and recorded runs and attempts are immutable.
3. Every run pins exactly one design version plus inputs, environment, code, configuration and randomness.
4. Hypothesis precedes result access or is marked post-hoc; timing is clock-derived, never asserted.
5. Preregistration deviations and protocol conduct deviations are separate, append-only records.
6. Retry, rerun and correction append successors; nothing is overwritten.
7. Absence, censoring and zero are distinct; absence is always coded.
8. Every finding states uncertainty, applicability and limitations.
9. Negative, null and inconclusive outcomes are retained and separately typed.
10. Run success implies neither validity, fitness nor reproducibility.
11. Deletion never cascades to observations, datasets, hypotheses or findings; tombstones preserve identity.
12. Stopping and success rules are hypothesis-side preregistered criteria, not run-side outcomes.

## Minimal model set

WM-ACT-036, WM-KNW-009, WM-ACT-022 (spec required); referenced: WM-KNW-007, WM-KNW-008, WM-MAT-008, WM-DAT-001. Candidates raised without identifiers: cross-study reusable **ExperimentDesign**; EM-KNW-02's **Evidence Artifact** remains applicable here.

## Holds

WM-ACT-022 has no specification; nothing may be built on it until its design/run boundary is decided. WM-ACT-036 and WM-KNW-009 are single-provider Codex waivers with absence-of-external-review holds; WM-ACT-036 cites a 2021-draft-dependent gap and an unreconciled DataCite 4.6/4.7 delta; WM-KNW-007's parent relation is held as reference. All relation rows are candidate; composition completeness cannot be claimed. All bases are `publishableCanonical: false`. No identifiers allocated, no fixtures run. This is a review checkpoint — not canonical, not complete, not installable.

## grok-study.raw.md
Verdict: Conditionally accept. Reuse WM-ACT-036 and WM-KNW-009, complete reserved WM-ACT-022 narrowly as Experiment Run, and treat study-scoped design as an immutable protocol/design release under the study. Do not leave the cross-study design unassigned. A finding profile of WM-ACT-036 plus WM-KNW-007/008 is a composition rule, not a substitute for instance identity.

Strongest evidence: The proposal refuses deletion of a failed experiment and refuses rewrite of a hypothesis after results, and it requires each run manifest to pin design, inputs, code, configuration, environment, randomness and references. That is enough to keep two contradictory runs, their failed attempts, and the original hypothesis simultaneously addressable.

Strongest counterexample: If the reusable cross-study design stays identifier-unassigned, the two-run test cannot name a stable design master once the same protocol leaves the study. A second failure mode is a finding that is only a mutable profile of the study: contradictory outcomes then collapse into one narrative and the original hypothesis is no longer protected. A protocol change before result access is a real case too; it must be a new immutable release under the same study, not a new study and not an edit.

Identity/mastership: Independent identity is required for Hypothesis (WM-KNW-009; preregistered and post-hoc are separate instances), Experiment Run (complete WM-ACT-022), Research Finding (instance identity even when profiled on 036 plus 007/008), Attempt (stable subordinate identity under the run, so retention is enforceable), and reusable cross-study Experiment Design (assign on promotion, with an explicit derivation link). Independent identity is not required for Research Study (reuse WM-ACT-036) or for study-scoped Experiment Design (immutable, referenceable release mastered by the study). Observation, Dataset and Analysis stay distinct subordinate types; they are not merged into Run or Finding. Study masters scope, releases and the study hypothesis registry. Run masters its manifest and attempts. Finding masters its claim, uncertainty, applicability and limitations, and cites rather than owns runs, datasets and hypotheses.

Study/design/run: One study may issue many immutable design releases. One release may have many runs. Each run binds one input snapshot. Attempts are execution tries under a run; failure does not remove the run. Amendment before result access is a new release under the same study, linked as superseding. After a closed run pins a release, that release cannot change.

Hypothesis lifecycle: A preregistered hypothesis is sealed before result access. A post-hoc hypothesis is a new explicit WM-KNW-009 instance, typed post-hoc, linked as exploratory, never an edit of the sealed one. Contradictory or failed runs do not alter hypothesis text, registration time or identity.

Provenance/reproduction: The closed-run manifest is the reproducibility contract and is append-only. It pins design-release identity and version, input-snapshot identities, code digest, configuration, a controlled environment reference, randomness seed or stream, and references. Free-text environment is not a pin. Correction is a new run or an erratum linked to the original, never an overwrite.

Observations/missingness: Observation is the atomic recorded fact; dataset is a versioned collection boundary; analysis reads dataset versions and does not write observations. Missing, zero, censoring and not-applicable are distinct. Zero is a present value. Censoring stores type and bound, not a substituted number. Missing requires a reason (not collected, lost, withheld, not applicable). None of these is an analysis conclusion.

Analysis/finding: Analysis is a computation over pinned runs and dataset versions, confirmatory or exploratory, and names the hypothesis identity it tests. Finding records the claim, cites analyses and runs, and must record uncertainty, applicability and limitations. It does not replace the hypothesis and does not own the cells.

Negative/null/inconclusive: Failed attempt, no effect, null and inconclusive are four states. No effect means an estimate inside a predeclared negligible region. Null means failure to reject, or support for, a named preregistered null. Inconclusive means insufficient information, including conflicting runs. A failed attempt is none of these. None authorizes deletion or recoding of inputs.

Scenario: Supported. Study S holds immutable design release D1 and sealed hypothesis H1. Run R1 pins D1 and snapshot S1, retains failed attempt A1, yields outcome O1. Run R2 pins D1 and different snapshot S2, yields contradictory O2. H1 and D1 are unchanged. Post-hoc H2, if created, is a new instance. Finding F cites both runs, records uncertainty, applicability and limitations, and may conclude inconclusive across runs or run-specific results. Forbidden: delete A1 or R1, rewrite H1 to fit O2, retcon D1, code missing inputs as zero, or label the pair no effect.

Invariants:
1. A preregistered hypothesis cannot be mutated after result access.
2. A post-hoc hypothesis is a new instance and cannot reuse the preregistered identity.
3. A study-scoped design release is immutable once referenced by a closed run.
4. A closed run manifest is append-only and pins design, inputs, code, configuration, environment, randomness and references.
5. Failed attempts remain retained and queryable.
6. Deleting a failed experiment is forbidden.
7. Two runs may share one design release, differ in input snapshot, and contradict.
8. Missing, zero, censoring, no effect, null and inconclusive are pairwise distinct.
9. A finding records uncertainty, applicability and limitations, and cites contradictory runs when both are in scope.
10. Observation is not a dataset; dataset is not an analysis; analysis is not a finding; finding is not a hypothesis.
11. Result access is logged against hypothesis version before any outcome is readable.
12. Promotion of a study release to a cross-study design creates a new identity with a derivation link, not a silent rewrite.

Minimum model set: Research Study (WM-ACT-036), Hypothesis (WM-KNW-009), Design Release under 036, Experiment Run (WM-ACT-022), Attempt as addressable subordinate, Observation, Dataset, Analysis, Finding as an instance profiled on 036 plus 007/008, and an assigned identity for cross-study Design only.

Blockers: Assign identity to the cross-study design before reuse. Give Finding instance identity so a profile cannot overwrite study or hypothesis. Give Attempt a retention key under the run. Require controlled, referenceable environment and randomness pins. Define the amendment-release relation so protocol change does not rewrite a pinned release or force a new study.

## candidate/candidate.json
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-PRD-04",
  "modelId": "WM-ACT-022",
  "registryId": "vr.wm-act-022",
  "name": "Experiment Run",
  "alternateNames": [
    "Experiment",
    "Trial"
  ],
  "version": "0.1.0-candidate.1",
  "entryKind": "occurrence-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent one governed execution of an immutable experiment design release, including attempt lineage, reproducibility manifest and append-only deviation evidence, without owning study, hypothesis, observation, dataset, analysis or finding identity.",
  "boundary": {
    "owns": [
      "experiment-run identity and lifecycle",
      "immutable run manifest and exact design pin",
      "attempt identities and retry or rerun lineage",
      "planned-versus-executed deviation evidence",
      "orchestration timestamps and status",
      "completion or abort evidence and reproducibility declaration"
    ],
    "delegates": [
      "study and study-scoped design releases to WM-ACT-036",
      "hypothesis identity and revision lifecycle to WM-KNW-009",
      "observations and measurements to WM-MAT-008",
      "input and output dataset versions to WM-DAT-001",
      "analysis or processing execution to WM-ACT-053 when separately performed",
      "claims, citations and findings to WM-KNW-007 and WM-KNW-008"
    ],
    "excludes": [
      "mutable experiment design",
      "truth or support status on a hypothesis",
      "copied observations or dataset contents",
      "analysis plan or finding mastership",
      "deletion of failed attempts",
      "automatic decision or policy effects"
    ]
  },
  "objects": {
    "ExperimentRun": {
      "identity": [
        "experimentRunId"
      ],
      "required": [
        "studyRef",
        "designVersionRef",
        "startedAt",
        "runManifest",
        "status"
      ],
      "optional": [
        "completedAt",
        "abortedAt",
        "successClass",
        "supersedesRunId",
        "correctionReason"
      ],
      "lifecycle": [
        "planned",
        "running",
        "completed",
        "aborted",
        "superseded"
      ]
    },
    "RunManifest": {
      "identity": [
        "manifestDigest"
      ],
      "required": [
        "designVersionRef",
        "componentPins",
        "codePins",
        "dependencyPins",
        "configurationDigest",
        "inputDatasetPins",
        "instrumentPins",
        "environmentPin",
        "runtimePin",
        "randomness",
        "calibrationRefs",
        "createdAt"
      ]
    },
    "ExperimentAttempt": {
      "identity": [
        "attemptId"
      ],
      "required": [
        "experimentRunId",
        "sequence",
        "startedAt",
        "manifestDigest",
        "status"
      ],
      "optional": [
        "completedAt",
        "abortedAt",
        "retryOfAttemptId",
        "resultDatasetRefs",
        "observationRefs"
      ],
      "lifecycle": [
        "started",
        "completed",
        "failed",
        "aborted"
      ]
    },
    "RunDeviation": {
      "identity": [
        "deviationId"
      ],
      "required": [
        "experimentRunId",
        "attemptId",
        "kind",
        "observedAt",
        "plannedValue",
        "executedValue",
        "authorityRef",
        "evidenceRefs"
      ],
      "optional": [
        "reason",
        "impactAssessmentRef",
        "resolutionRef"
      ]
    }
  },
  "relations": [
    {
      "target": "WM-ACT-036",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Resolve the owning study and immutable study-scoped design release."
    },
    {
      "target": "WM-KNW-009",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Pin preregistered or explicit post-hoc hypothesis revisions without changing them."
    },
    {
      "target": "WM-MAT-008",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve observations and measurements produced by attempts."
    },
    {
      "target": "WM-DAT-001",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Pin input and result dataset versions, partitions and digests."
    },
    {
      "target": "WM-ACT-053",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve separate analysis or processing execution evidence."
    },
    {
      "target": "WM-KNW-008",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve evidence and citation bindings used by later findings."
    }
  ],
  "operations": [
    {
      "id": "plan-run",
      "effect": "Create a run pinned to one released design version and draft manifest.",
      "authority": "authorized investigator"
    },
    {
      "id": "start-attempt",
      "effect": "Freeze the manifest and append one attempt.",
      "authority": "authorized investigator or orchestrator"
    },
    {
      "id": "record-deviation",
      "effect": "Append an explicit planned-versus-executed difference.",
      "authority": "authorized recorder"
    },
    {
      "id": "complete-attempt",
      "effect": "Close one attempt and link resulting observations or datasets.",
      "authority": "authorized recorder"
    },
    {
      "id": "abort-attempt",
      "effect": "Close a failed or stopped attempt without deletion.",
      "authority": "authorized recorder"
    },
    {
      "id": "complete-run",
      "effect": "Close the run with retained attempt and manifest evidence.",
      "authority": "authorized investigator"
    },
    {
      "id": "correct-run-record",
      "effect": "Create a successor run record with correction reason while preserving the predecessor.",
      "authority": "study steward"
    }
  ],
  "invariants": [
    "Study, hypothesis, design, run, attempt, observation, dataset, analysis and finding use distinct identities.",
    "Every run pins exactly one immutable released design version.",
    "A completed or aborted run and its frozen manifest are immutable.",
    "Every attempt belongs to exactly one run and has a monotonic sequence.",
    "Retry and rerun append a new attempt or run and never overwrite a failed one.",
    "The run manifest pins code, dependencies, configuration, inputs, instruments, environment, runtime, randomness and calibration evidence.",
    "Every input dataset reference includes immutable version, partition and digest evidence.",
    "Every planned-versus-executed difference is an explicit append-only deviation.",
    "A preregistered hypothesis pin precedes result access; later hypotheses are marked post-hoc with source-result references.",
    "Absence, censoring, zero and no effect are never inferred from run status.",
    "Successful orchestration proves neither scientific validity nor reproducibility.",
    "Contradictory run outcomes remain independently resolvable and do not rewrite the hypothesis.",
    "Negative, null and inconclusive results are retained through external finding records.",
    "Deleting or withdrawing a study never cascades to evidence-bearing completed runs.",
    "Access to a run result cannot exceed access to its contributing design, inputs and observations."
  ],
  "holds": [
    "Exact Grok review and provider reconciliation are pending.",
    "One frozen no-tools semantic audit of the reconciled candidate is pending.",
    "Cross-study reusable Experiment Design remains identifier-unassigned.",
    "Base study, hypothesis and evidence models retain their own publication holds.",
    "Package conversion and live HTTP/runtime/search/package verification are pending."
  ]
}

## candidate/fixtures.json
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-ACT-022",
  "version": "0.1.0-candidate.1",
  "cases": [
    {
      "id": "contradictory-runs",
      "kind": "positive",
      "input": "Two runs pin one design but different dataset snapshots and random seeds; one supports and one challenges the hypothesis.",
      "expect": "Both manifests and outcomes remain distinct and the hypothesis revision is unchanged."
    },
    {
      "id": "failed-attempt-retained",
      "kind": "positive",
      "input": "Attempt 1 fails and attempt 2 succeeds.",
      "expect": "Both attempts remain append-only with retry lineage and separate evidence."
    },
    {
      "id": "rewrite-hypothesis-after-results",
      "kind": "negative",
      "input": "A hypothesis revision is edited after result access to match observations.",
      "expect": "Rejected; create an explicit post-hoc or successor hypothesis revision externally."
    },
    {
      "id": "delete-failed-run",
      "kind": "negative",
      "input": "A failed experiment is deleted after a successful rerun.",
      "expect": "Rejected; failed run remains retained and citable."
    },
    {
      "id": "missing-versus-zero",
      "kind": "negative",
      "input": "No observation exists for one outcome.",
      "expect": "Run records missingness or coverage; it never asserts zero or no effect."
    },
    {
      "id": "design-deviation",
      "kind": "positive",
      "input": "Executed sample size and environment differ from the design.",
      "expect": "Two typed deviations record planned and executed values with authority and evidence."
    },
    {
      "id": "restricted-input",
      "kind": "negative",
      "input": "One input dataset is more restricted than the run summary.",
      "expect": "Run and derived result access retain the stricter evidence ceiling."
    }
  ]
}

## candidate-allocation-offline-reusable-experiment-design/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-PRD-04","proposedName":"Reusable Experiment Design","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An independently governed experimental design remains identifiable across studies and runs while its protocol evolves through controlled releases.","versionIdentity":"Changes to questions, outcomes, methods, assignment, analysis intent, success criteria or stopping rules create immutable design versions; a different experimental objective creates a separate design.","independentLifecycle":["draft","reviewed","approved","effective","superseded","withdrawn","retired"],"mastership":"research-method or experimental-protocol authority"},"boundary":{"owns":["persistent reusable experiment-design identity","research questions and intended outcomes","method and assignment specification","analysis intent and estimands","success, failure and stopping rules","applicability and prerequisite constraints","approval and effective period","version, supersession and retirement history"],"references":[{"target":"WM-ACT-036","purpose":"Research Study aggregate"},{"target":"WM-ACT-022","purpose":"Experiment Run occurrence"},{"target":"WM-KNW-009","purpose":"Hypothesis master"},{"target":"WM-KNW-007","purpose":"Research claim or finding"},{"target":"WM-KNW-008","purpose":"Evidence binding"},{"target":"WM-DAT-001","purpose":"Input and result dataset"},{"target":"WM-MAT-008","purpose":"Observation master"}],"excludes":["study, hypothesis, run, attempt or observation identity","dataset, analysis execution or finding identity","study-scoped one-off protocol component","run configuration, environment or randomness values","evidence artifact or citation identity","truth, reproducibility or publication claim"]},"objects":{"ReusableExperimentDesign":{"identity":["experimentDesignId"],"required":["name","objective","ownerRef","status"],"optional":["successorRef","retiredAt"],"lifecycle":["draft","reviewed","approved","effective","superseded","withdrawn","retired"]},"DesignVersion":{"identity":["experimentDesignId","version"],"required":["questions","outcomes","method","analysisIntent","successCriteria","validFrom","contentDigest","status"],"optional":["assignmentMethod","stoppingRules","applicability","prerequisites","validTo","supersedesVersion"],"lifecycle":["draft","approved","effective","superseded","withdrawn"]}},"invariants":["Reusable design identity remains separate from study-scoped protocol and Experiment Run identity.","Every run pins exactly one immutable design version.","Changing outcomes, method, estimand, success criteria or stopping rules creates a successor version.","A design never owns run inputs, environment, code, configuration or randomness values.","Hypothesis identity remains independent and survives studies that test it.","Preregistered hypothesis and design timing precede result access or are explicitly post-hoc.","Planned-versus-executed deviations append to the run and never mutate the design release.","Run success never proves design validity or reproducibility.","Observation, analysis execution and finding remain separate assertions.","Missing, zero, censored, no-effect, null and inconclusive remain distinct.","Negative and failed outcomes never delete or retire the design automatically.","Retired design versions remain resolvable for historical runs and findings."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","WM-ACT-022 completion and relation contracts require canonical adoption.","Method, evidence and dataset crosswalks require validation.","Package conversion and live verification are pending."]}

## candidate-allocation-offline-reusable-experiment-design/profile-candidate.json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-PRD-04","name":"Enterprise Research Study and Experiment","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ACT-036","WM-KNW-009","WM-ACT-022","WM-KNW-007","WM-KNW-008","WM-MAT-008","WM-DAT-001"],"constraints":["WM-ACT-036 owns Research Study and study-scoped immutable design releases; WM-KNW-009 owns Hypothesis.","WM-ACT-022 is completed narrowly as Experiment Run and pins design, inputs, code, environment, configuration, randomness and references.","Research Finding profiles study findings with WM-KNW-007 claims and WM-KNW-008 evidence bindings without new identity.","Evidence Artifact reuses the EM-KNW-02 candidate rather than creating a duplicate.","Retry, rerun, correction and planned-versus-executed deviation append attempts or successors.","Supported, unsupported, refuted and inconclusive remain source-qualified assessments rather than truth flags." ]}

## candidate-allocation-offline-reusable-experiment-design/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Reusable Experiment Design","cases":[{"id":"two-study-reuse","kind":"positive","input":"Two studies use the same approved design version with different datasets.","expect":"The design is reused while studies, runs, inputs and findings retain separate identity."},{"id":"successor-method","kind":"positive","input":"The analysis intent and stopping rule change for future runs.","expect":"A successor design version is issued and earlier runs keep the old pin."},{"id":"contradictory-runs","kind":"positive","input":"Two runs of one design produce supporting and challenging outcomes.","expect":"Both runs and findings remain without rewriting the design or hypothesis."},{"id":"run-is-design","kind":"negative","input":"Each execution occurrence mints a new reusable design identity.","expect":"The identity duplication is rejected."},{"id":"rewrite-after-result","kind":"negative","input":"Success criteria are rewritten after result access under the same version.","expect":"The mutation is rejected."},{"id":"failed-run-deletes-design","kind":"negative","input":"A failed run removes the design from history.","expect":"The deletion is rejected."}]}

## candidate-allocation-offline-reusable-experiment-design/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}
