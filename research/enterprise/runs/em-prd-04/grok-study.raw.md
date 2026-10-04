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
