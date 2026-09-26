# Verdict

EM-TEC-08 is **accepted as a reuse boundary onto WM-SFT-015 (Test Case / Test Result), extended by three typed neighbour references and one genuine gap**. The contour's five candidate types do not map one-to-one onto five new models. Four of them — TestSpecification, TestRun, TestResult, VerificationEvidence — are already governed members of the WM-SFT-015 aggregate: its root is the frozen test-case definition revision, its members are executions, observed outcomes, adjudicated verdicts, captured evidence and the governance record binding them. Defect is **not** in this contour. It belongs to WM-SFT-014, which the dossier's own prior adjudication (EM-TEC-05) already assigns. EM-TEC-08 therefore owns the *linkage and separation rules* between the two, not a Defect type.

Decision: **reuse WM-SFT-015** as the subject model; **reference** WM-SFT-014, WM-ACT-006, WM-REC-006 and WM-SFT-008; **new model required** only for TestEnvironment, which WM-SFT-015 declares out of scope and references with "registry identifier not yet assigned". Boundary decision moves from `pending` to `reuse-plus-one-gap`. Publication remains blocked — see Holds.

WM-ACT-038 is an incorrect parent and must be corrected before EM-TEC-08 publishes.

# Evidence

All from the frozen dossier, no external retrieval.

WM-SFT-015 scope statement: the reusable test case definition is the aggregate root; governed members are "the executions of a specific frozen definition revision, their observed outcomes, adjudicated verdicts and result status, the evidence captured during execution, the assurance signals derived over that evidence, and the governance record". That sentence covers four of the five candidate types verbatim.

Its `out_of_scope` list names "Defect and incident triage, assignment and resolution lifecycle" and "Test environment provisioning, configuration baselining and infrastructure state". Its boundary note for Defect states: "A failing result may cite a defect reference, but defect state never becomes result state inside this model."

WM-SFT-014 scope: "the defect record as an entity: what deviation is asserted, in which product versions and environments, on what evidence, how it is classified and ranked, how its state advances to a recorded resolution". Its `out_of_scope` includes "Test case design and test execution records that supply verification evidence".

Registry state: both WM-SFT-015 and WM-SFT-014 carry `review_state: boundary-review-required`, `status: candidate`. WM-SFT-015 has empty `composition_role`, empty `default_link_type`, empty `relations_ref`. Both have `publishableCanonical: false` and `adjudicationStatus: reviewable-draft`. Both are single-provider Claude-only with Grok waived 2026-08-29T09:06:27Z.

Relations ledger contains `WM-SFT-008 → REFERENCE → WM-SFT-015` ("Build or release references test evidence", review_state candidate) and `WM-SFT-014 → REFERENCE → WM-SFT-013`. It contains **no** edge between WM-SFT-015 and WM-SFT-014, none to WM-ACT-006, none to WM-REC-006 from either.

# Identity/mastership

| Type | Owning model | Identity | Master system |
|---|---|---|---|
| TestSpecification | WM-SFT-015 root | authoritative test case identifier + revision identifier + content digest over canonical serialization; no date component | test/quality management system |
| TestRun | WM-SFT-015 member | execution record identifier issued by harness/CI/test-management; correlation key groups logically equivalent executions across runs; attempt ordinal within retry group | executing platform |
| TestResult | WM-SFT-015 member | not separately identified — the adjudicated verdict is an attribute of the execution record, distinct from observations | same as TestRun |
| VerificationEvidence | WM-SFT-015 member | content digest per artifact; evidence manifest is the integrity boundary — an artifact absent from it is not evidence for that result | artifact store, else digest + execution id |
| Defect | **WM-SFT-014**, not here | master record identifier from the defect system of record; governed global identifier (CVE, OSLC IRI) secondary | defect tracker |

TestResult is deliberately *not* a fifth identified entity. WM-SFT-015 separates observation (what was seen) from adjudication (what verdict an assertor reached over it), and both hang off the execution record. Minting a standalone TestResult identity would fork the attempt series.

Two identity defects in the frozen spec must be fixed before EM-TEC-08 relies on them: the visual-capture artifact admits a capture timestamp into its fallback identity, contradicting WM-SFT-015's own rule that a date is never an identifier; and nine of thirteen serial artifacts have no declared numbering scope. Both are already logged in that model's adjudication as rejected-as-is.

# Specification/run/result/evidence

Expected behaviour versus executable implementation separates cleanly along a line the frozen spec already draws. The definition owns the expectation: objective, preconditions, ordered actions, expected outcomes, the oracle and comparison rule with tolerances, normalization and masking rules. The implementation is external — WM-SFT-015 carries only "a resolvable binding reference plus the contract the implementation must satisfy, so implementation change does not fork the definition". The executable test script is an artifact of a source repository with its own review, build and release lifecycle.

The operational consequence: editing a test script does not create a new definition revision. Editing the expected outcome or comparison rule does. The binding finding asks explicitly what must remain true of the definition when only the implementation changes, and records a semantic-equivalence rule plus the previous binding value.

Run binds to the frozen revision, not to the head. The execution record carries a bound test-case revision reference plus a definition digest, so a later edit of the test case cannot silently change the meaning of a past result. Orphaned bindings are flagged, never repointed.

Result splits into two layers that must not collapse. Observation records the actual value, the comparator and its version, the tolerance applied, and a pointer into the subject. Adjudication records a governed verdict code, the assertor reference, the assertion mode (automatic, manual, semi-automatic) and the supporting basis. A verdict with no assertor is invalid; a pass with no evaluated expectation is rejected by validation.

Evidence is sealed at attempt close: named digests over every artifact, an evidence manifest enumerating them, and an optional signed attestation binding the result to the digest-identified subject with the configuration used. Signing, key custody and verification execution stay outside.

# Defect classification

Four outcomes must be distinguishable without ambiguity. The frozen models support three cleanly and one weakly.

**Product defect** — verdict `failed`, determinism classification `deterministic`, binding digest verified, environment reference resolves and matches the declared applicability. Raises or reproduces a WM-SFT-014 record with `term_of_record = defect`, `deviation_basis` pointing at a WM-REC-006 requirement. Link role on the execution: `raised` or `reproduced`.

**Test defect** — the oracle, comparison rule, tolerance or expected outcome is wrong; the product is conforming. WM-SFT-015 provides the correction path: `correction_reason` includes "oracle defect" as a coded value, and the superseding adjudication replaces the verdict without a rerun because the observations are unchanged. A WM-SFT-014 record may still be raised, but with `anomaly_subject_class = work-product` rather than product, and `affected_product_entry` pointing at the test case revision, not the software. Critically: this path emits no product-defect record.

**Environment failure** — determinism classification `environment-induced`. WM-SFT-015 declares this code explicitly. The execution's environment reference resolves to a configuration item whose state diverged; the verdict is `error` or `blocked`, never `failed`, since no expectation was evaluated. This is where the missing TestEnvironment model bites: without it, environment-induced cannot be evidenced, only asserted.

**Inconclusive / flaky** — the verdict vocabulary carries `inconclusive`, `blocked`, `error`, `not-applicable`, `untested` as first-class values, and WM-SFT-015 forbids silent coercion to pass or fail. Flaky is a property of an *attempt set*, not of any single attempt, and is recorded separately from every attempt's verdict.

The boundary rule EM-TEC-08 must add, because neither model states it: **classification is an adjudication over the attempt set plus the binding, performed by a named role, and it determines which defect model (if any) receives a record.** Test defect and environment failure never create product-defect records. This is the rule the contour's negative case tests.

# Version/environment binding

Subject pinning is strong. The execution carries a subject-under-test descriptor with name and digest (in-toto semantics: subjects matched purely by digest, treated as immutable), cardinality `1..n`, required. WM-SFT-008 supplies the release side — release identifier, artifact descriptor set, authoritative digest algorithm — and the existing REFERENCE edge already points the right way: build references test evidence, and evidence carries the subject digest back.

The rule: **a result is interpretable only against the digest it names.** A release with a different digest is a different subject; the prior result does not transfer, is not inherited, and must not be aggregated into the new release's assurance summary.

Environment pinning is weak, and this is the gap. WM-SFT-015's `tst-exec-de-environment-ref` is cardinality `0..1`, **not required**, and its target is "Test environment / configuration-item model (registry identifier not yet assigned)" — a REFERENCE marked `required: true` to a model that does not exist. The contour's proposed invariant "Run закрепляет объект проверки и среду" (run pins the subject and the environment) is therefore half-satisfied: subject yes, environment no.

EM-TEC-08 must either raise environment cardinality to `1` with a resolvable reference, or accept a reproducibility-completeness classification that marks environment-unpinned runs as non-reproducible. The frozen spec already provides the second option (`tst-exec-q-context-sufficiency` asks for the minimum context set and a reason code per missing element). I recommend requiring the reference and reasoning the absence, not silently permitting it.

# Flaky and inconclusive

The invariant "flaky does not mean passed" holds structurally in WM-SFT-015 and must be carried forward verbatim.

Mechanics: a retry creates a new attempt with the next ordinal and a predecessor link; the earlier attempt is sealed and never mutated, renumbered or deleted. Non-determinism is classified over the attempt set only when binding equality is *proven* by matching definition and parameter digests — differing bindings are not flakiness, they are different tests. The classification records an instability measure with its observation window and denominator, plus the classifying agent and confidence.

Whether the classification may change the reported verdict is itself an adjudicated decision with a named deciding role and a recorded decision record. It is never automatic. Quarantine and suppression are external references; WM-SFT-015 records that a reference exists, not the policy or its enforcement.

Two limits EM-TEC-08 inherits and must publish rather than paper over. First, WM-SFT-015's own coverage marks non-determinism classification as a **gap**: no primary standard normatively defines flaky classification or a flake-rate denominator, and the Maven Surefire flakyFailure/rerunFailure distinction is a harness convention, not a specification. Second, the Surefire projection collapses an attempt series into one element and reports the time of the last successful or first failing run — WM-SFT-015 rejects that collapse, which makes round-tripping through JUnit-style XML asymmetric and lossy in a way that can erase flakiness evidence.

Inconclusive is preserved, not dropped. Silently excluding inconclusive, blocked, aborted or integrity-failed records to improve an aggregate is named a governance defect in the frozen policy set.

# Lifecycle and closure

Three lifecycles run independently and must not be coupled.

*Test case definition*: draft → in-review → approved → active → deprecated → retired. Approval binds to a revision digest and cannot transfer to a successor.

*Execution record*: in-progress → recorded → adjudicated → superseded / withdrawn. Append-only. A correction is a superseding revision citing the record it supersedes with reason, actor and effective time; a rerun is a new attempt, never a correction.

*Defect record* (WM-SFT-014): submitted → triaged → assigned → resolved → verified → closed, with resolution codes fixed, duplicate, not-reproducible, works-as-designed, will-not-fix, superseded. Non-fix outcomes require a recorded justification.

The closure rule EM-TEC-08 must state, and which is the point of the whole contour: **a product defect closes only on a verification outcome recorded against a subject digest that differs from the digest on which the defect was raised, adjudicated by a party in the verifier role.** WM-SFT-014's `fn-record-verification-outcome` and `de-verification-outcome-code` supply the mechanism; WM-SFT-015's `tst-exec-de-link-role` supplies `verified-fixed` as a governed outbound role. Neither model currently states the differing-digest requirement. Without it, re-running an unchanged build and getting a green result would satisfy closure.

Corollary: correcting a test defect changes a test case revision and may supersede an adjudication. It touches no WM-SFT-014 product record, produces no `verified-fixed` link, and cannot advance a defect state. The models already forbid the coupling — WM-SFT-015 states defect state never becomes result state, WM-SFT-014 excludes test execution records — but the prohibition is stated in two places and asserted in neither direction as an invariant. EM-TEC-08 supplies it.

# Scenario

**One defect, several tests.** WM-SFT-014 `de-relation-entry` and `de-attributed-report-count` carry the many-to-one attribution; WM-SFT-015 `tst-exec-de-defect-ref` is cardinality `0..n` with a per-link role. Defect D is cited by executions E1 (TC-A, role `raised`), E2 (TC-B, role `reproduced`), E3 (TC-C, role `reproduced`). Each execution keeps its own verdict and evidence. D's state is D's; none of the three executions inherits it, and D does not close because one of them later passes.

**Flaky run.** TC-B, binding digest B1, subject digest S1: attempt 1 `failed`, attempt 2 `passed`, attempt 3 `passed`. Binding equality proven by matching digests. Attempt set classified `flaky` with instability measure 1/3 over the stated window. Attempt 1 retains verdict `failed` and its evidence, unaltered. The set-level classification does not rewrite it and does not by itself make the set a pass. If D was raised from attempt 1, the flaky classification is not verification of a fix — it is evidence of non-determinism and, arguably, grounds for a second defect of a different kind.

**Re-verification on a different version.** Release R2 published with subject digest S2 ≠ S1. TC-A executed against S2 under definition revision TC-A@r3 (unchanged from r3 used for E1, digest verified). Verdict `passed`, assertor named, mode recorded, evidence sealed with S2 in the attestation subject. Link role `verified-fixed` on D. D may now advance to verified; its `fixed_in_version` records R2. E1's conclusion is untouched: TC-A still failed against S1, and that remains the truthful record for S1.

Three separate conclusions, three separate records, none overwritten. The acceptance scenario holds.

# Invariants

1. An execution binds exactly one frozen definition revision by identifier and digest; a later edit of the definition never changes the meaning of a recorded result.
2. An execution names the subject under test by digest (required) and the environment by reference; where the environment reference is absent, the run is classified non-reproducible with a reason code.
3. Flaky is a property of an attempt set with proven-identical binding, never a verdict; no attempt's verdict is rewritten by a set-level classification.
4. A verdict requires an assertor and a mode; a `passed` verdict requires at least one evaluated expectation and is never inferred from an absent defect, an empty failure list or a zero exit code.
5. Non-binary outcomes (inconclusive, blocked, error, not-applicable, untested) are preserved and reported; coercion to pass or fail is invalid.
6. A defect record contains both the observed and the expected behaviour, and cites the requirement or expectation it deviates from.
7. **Correcting a test case revision, superseding an adjudication, or changing an oracle never transitions a product-defect record.** Only a verification outcome recorded against a differing subject digest, by a party in the verifier role, may advance a defect to verified.
8. Defect state never becomes result state, and result state never becomes defect state; each model holds the other as a typed reference with a role and an assertion time.
9. Execution records and evidence are append-only; corrections supersede with reason, actor and effective time, and superseded revisions remain retrievable.
10. Classification of a failure as product defect, test defect, environment failure or inconclusive is an adjudication over the attempt set plus the binding, by a named role, and determines which model (if any) receives a record.

# Minimal completion shape

To move `boundary_decision` off `pending`:

1. **Correct the parent.** Replace WM-SFT-015's `parent_ids: WM-ACT-038` (see next section) and remove the three CHILD composition entries pointing at it.
2. **Register four relations** absent from the ledger: WM-SFT-015 ↔ WM-SFT-014 (REFERENCE, bidirectional roles: execution cites defect; defect cites verification evidence), WM-SFT-015 → WM-REC-006 (REFERENCE, traceability target), WM-SFT-014 → WM-ACT-006 (REFERENCE, remediation task), WM-SFT-015 → TestEnvironment (REFERENCE, once the model exists).
3. **Raise the TestEnvironment gap** as a new subject model with an assigned registry identifier. It is currently a `required: true` REFERENCE to nothing, and it is load-bearing for environment-failure classification.
4. **Publish invariants 7 and 10** as normative in EM-TEC-08; neither exists in the frozen specs.
5. **Require the environment reference** on the execution record, or publish the non-reproducible classification as the explicit alternative.
6. **Populate WM-SFT-015 registry fields** left empty: `composition_role`, `default_link_type`, `relations_ref`.
7. **Carry both models' publication holds forward** unresolved; EM-TEC-08 cannot clear them.

# Holds

WM-ACT-038 is **Learning Activity / Course Delivery** (NAV.ACT.EDU, parent WM-PER-008, purpose "Instruction, participation and assessment lifecycle"). It is not a generic activity or test-execution parent. WM-SFT-015 inherits from it in four places — the registry `parent_ids`, and three CHILD composition entries claiming it supplies "generic activity framing", "generic activity identity and time framing" and "the generic activity-and-outcome pattern". All four are wrong. The most plausible intended parent is a generic activity model in the ACT domain; WM-ACT-006 (Task) is a candidate but is itself `entry_kind: standalone-mm`, `priority_confidence: low`, and its adjudication flags an unregistered dependency on WM-ACT-021. Do not substitute one unverified parent for another — **raise the correction, propose no replacement without registry review.**

Both WM-SFT-015 and WM-SFT-014 are single-provider Claude-only with Grok waived; no cross-provider corroboration exists for any bundle, finding or entry_kind. Both carry live source verification holds: WM-SFT-015 names at-risk pins on SLSA v1.0 (retired), in-toto test-result predicate v0.1.0 (pre-stable), OpenTelemetry test attributes (development stability), Surefire master-branch XSD, and a 21 CFR Part 11 edition now superseded. WM-SFT-014 names IEEE 1044-2009 as Inactive-Reserved since 2020-03-05 and two undated moving targets.

WM-SFT-015 carries an unresolved citation-integrity hold: `known_omissions` states FDA GPSV statements on independence and record retention were not extracted, yet SRC-009 is cited on three findings covering exactly those subjects. It also carries a duplicate-source hold (SRC-001 and SRC-017 are the same standard under two catalogue URLs, inflating the apparent evidence base) and an artifact-identity hold.

WM-REC-006 has no specification in this dossier, only a registry reservation with `validation_flags: не всегда standalone | resolved-kind=view-candidate`. All requirement-traceability claims in EM-TEC-08 rest on WM-SFT-015's outbound reference, not on a verified target.

I am not claiming canonical completeness for EM-TEC-08 or for any model it reuses, and I am not claiming installability. Every model in this decision is `status: candidate`, `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`.
