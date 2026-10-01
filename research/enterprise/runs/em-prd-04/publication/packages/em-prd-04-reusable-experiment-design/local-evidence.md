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
