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
