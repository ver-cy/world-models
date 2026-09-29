You are the sole frozen independent semantic auditor for EM-TEC-08. Use no tools. Review the reconciled direction and current candidates for identity, lifecycle, ownership, result containment, defect classification, temporal/version binding, environment semantics, privacy, fixtures and accidental new IDs. Return verdict; blocking defects; non-blocking defects; exact remediation; required fixtures; publication disposition. Do not invent allocations.


## Claude study
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


## Grok study
# Grok frozen study — EM-TEC-08

Source conversation: https://grok.com/c/69e64116-df78-4832-81de-9a0f1c38f16f?rid=0a47981e-5787-457b-9153-2037d496e522

Verdict: conditional accept as a research direction, not a completed crosswalk. No new identifier.

Mastership: WM-SFT-015 owns test specification, run, observation/result adjudication and sealed VerificationEvidence. WM-SFT-014 owns product Defect. WM-REC-006 is an external requirement/expected-behavior reference. WM-ACT-006 owns remediation work. WM-SFT-008 owns exact subject artifact/release identity. Withdraw erroneous WM-ACT-038 parent and do not guess a replacement.

TestResult is not a new aggregate root, but containment cannot mean one verdict field on a suite run. Each observation/result fragment needs stable run-scoped identity (run + attempt/slot or existing execution-record identity). Defect links, retry membership and evidence point at fragments. A suite run may contain many fragments. Retry sets group immutable attempts.

Expected behavior/oracle is separate from executable automation binding. TestRun pins specification revision, implementation binding, exact subject digest, immutable environment pin, actor/tool, times and attempt ordinal. Raw comparison is immutable; adjudication is later and superseding, never rewriting raw observation. VerificationEvidence is sealed and digest-addressed; it is neither run, suite rollup nor release gate.

Adjudication classes are product defect, test defect, environment failure, and inconclusive/flaky. Only product defect opens/updates WM-SFT-014. Pass is not inferred from absence of defect. Flaky is an attempt-set property under identical bindings and does not mean passed. Each retry remains. Unresolved flaky/inconclusive cannot close a product defect or satisfy VerificationEvidence.

Defect, run, task and release lifecycles are independent. Task done does not imply fixed; resolved does not imply verified. Fixed verification requires a later subject digest than the failing digest, exact environment pin and product-linked passing fragments. Same digest, environment failure, unresolved flaky set or repaired test cannot verify a product fix. Reopen preserves prior closure history.

Test Environment remains identifier-unassigned. Do not promote it to WM-SFT-010: test fixtures, device farms, seeded data and lab rigs differ from generic runtime. Yet identity grain is unresolved (snapshot digest versus named pool plus as-of), as are baseline mutability, failure attachment and shared versus ephemeral mastership. Until resolved, use a required immutable environment pin/value object rather than a mastered type or allocation.

Scenario: S1/S2 fail on digest D1 and env E and support one Defect; S3 has fail/pass/fail retry set and is flaky context, not proof. Remediation yields D2 != D1. Rerun on D2 and pinned E-prime. Evidence may verify S1/S2; residual S3 flake neither reopens the Defect nor proves regression. Oracle correction reclassifies/withdraws rather than claims a product fix.

Blockers: run-fragment identity unspecified; Test Environment identity unresolved; replacement parent unassigned; test-defect home unconfirmed; WM-REC-006 lacks full spec; WM-SFT-015 crosswalk/source-pin/artifact holds remain. Do not claim canonical completeness.


## Provider comparison
# Provider comparison — EM-TEC-08

Claude and Grok agree on reuse: WM-SFT-015 owns test definitions, executions, observations, adjudication and evidence; WM-SFT-014 owns Defect; WM-ACT-006 owns remediation; WM-SFT-008 owns exact tested artifacts; WM-REC-006 remains a reference; WM-ACT-038 parentage must be withdrawn without guessing a replacement. Both reject a separately mastered TestResult and require exact subject/environment pins, immutable attempts, explicit flaky/inconclusive handling and evidence-based closure on a later digest.

Grok sharpens TestResult containment: a run must contain stable result fragments, not only a rollup verdict, and links/evidence/retry sets point to fragments. It also challenges the Test Environment proposal: keep the name identifier-unassigned, but until identity grain and mastership are proven represent the environment as a required immutable pin/value object and do not advance the allocation package.

The reconciled disposition completes reserved WM-SFT-015 and WM-SFT-014 research candidates, removes the WM-ACT-038 parent assumption, retains Test Environment as an unassigned research question, and holds canonical publication. No runtime or model ID is created.


## WM-SFT-015 candidate
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-TEC-08",
  "modelId": "WM-SFT-015",
  "registryId": "vr.wm-sft-015",
  "name": "Test Case / Test Result",
  "version": "0.1.0-candidate.1",
  "entryKind": "test-evidence-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "sourceSpecSha256": "3e1df50b24b6659fe5bec661cdbe8b425e75667443bddb9598de4bfb3d7ac4f7",
  "purpose": "Represent immutable reusable test-case revisions, executions, observations, adjudicated results and sealed evidence while referencing requirement, release, defect and environment masters.",
  "boundary": {
    "owns": [
      "test-case identity and immutable definition revisions",
      "preconditions inputs ordered actions expected outcomes oracle tolerances and postconditions",
      "execution attempts pinned to exact definition revision and subject digest",
      "observed outcomes distinct from adjudicated verdicts",
      "retry and nondeterminism classification",
      "sealed execution evidence and result supersession",
      "aggregate governance access retention and provenance"
    ],
    "delegates": [
      "requirement and acceptance-criterion identity to WM-REC-006",
      "build release and tested-artifact identity to WM-SFT-008",
      "defect triage resolution and closure to WM-SFT-014",
      "runtime environment identity to WM-SFT-010 while Test Environment remains an unassigned specialization",
      "remediation work to WM-ACT-006"
    ],
    "excludes": [
      "learning-activity inheritance from WM-ACT-038",
      "test plan campaign suite or cycle lifecycle",
      "requirement risk release or defect mastership",
      "environment provisioning or configuration baseline ownership",
      "source-code test-script repository lifecycle",
      "automatic release-gating decision"
    ]
  },
  "objects": {
    "TestCaseDefinition": {
      "identity": [
        "testCaseId",
        "revision"
      ],
      "required": [
        "objective",
        "preconditions",
        "inputs",
        "actions",
        "expectedOutcomes",
        "oracle",
        "comparisonRule",
        "contentDigest",
        "status"
      ],
      "optional": [
        "requirementRefs",
        "automationBindingRef",
        "applicability",
        "dependencies"
      ],
      "lifecycle": [
        "draft",
        "reviewed",
        "approved",
        "deprecated",
        "retired"
      ]
    },
    "TestExecution": {
      "identity": [
        "executionId"
      ],
      "required": [
        "testCaseRevisionRef",
        "subjectArtifactRef",
        "subjectDigest",
        "environmentRef",
        "startedAt",
        "executorRef",
        "resolvedParameters",
        "status"
      ],
      "optional": [
        "endedAt",
        "attemptOfRef",
        "runnerRef"
      ],
      "lifecycle": [
        "scheduled",
        "running",
        "completed",
        "aborted",
        "invalidated"
      ]
    },
    "ObservedOutcome": {
      "identity": [
        "observationId"
      ],
      "required": [
        "executionRef",
        "observedValue",
        "observedAt",
        "method",
        "sourceRef"
      ],
      "optional": [
        "unitRef",
        "normalization",
        "confidence"
      ],
      "lifecycle": [
        "recorded",
        "superseded-by-correction"
      ]
    },
    "ResultAdjudication": {
      "identity": [
        "adjudicationId"
      ],
      "required": [
        "executionRef",
        "verdict",
        "resultStatus",
        "adjudicatorRef",
        "adjudicatedAt",
        "basisRefs"
      ],
      "optional": [
        "nondeterminismClass",
        "supersedesAdjudicationId",
        "reasonCode"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ]
    },
    "EvidenceManifest": {
      "identity": [
        "evidenceManifestId"
      ],
      "required": [
        "executionRef",
        "items",
        "sealedAt",
        "contentDigest",
        "custodianRef"
      ],
      "optional": [
        "redactedExportRefs",
        "retentionRef"
      ],
      "lifecycle": [
        "open",
        "sealed",
        "superseded",
        "disposed"
      ]
    }
  },
  "verdicts": [
    "passed",
    "failed",
    "inconclusive",
    "blocked",
    "not-executed"
  ],
  "relations": [
    {
      "target": "WM-REC-006",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve immutable requirement and acceptance-criterion revisions."
    },
    {
      "target": "WM-SFT-008",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Resolve exact build or release artifact identity and digest."
    },
    {
      "target": "WM-SFT-014",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Raise reproduce or verify defects without sharing lifecycle state."
    },
    {
      "target": "WM-SFT-010",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Resolve runtime environment identity while a Test Environment specialization remains unassigned."
    },
    {
      "target": "WM-ACT-006",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve remediation or follow-up work without turning results into tasks."
    }
  ],
  "operations": [
    {
      "id": "publish-test-revision",
      "effect": "Issue an immutable definition revision with oracle and exact expected outcomes.",
      "authority": "test owner"
    },
    {
      "id": "execute-test",
      "effect": "Run one frozen revision against an exact subject digest and environment.",
      "authority": "authorized runner"
    },
    {
      "id": "record-observation",
      "effect": "Append raw observed outcomes with method and time.",
      "authority": "execution recorder"
    },
    {
      "id": "adjudicate-result",
      "effect": "Compare observations through the declared oracle and record a verdict.",
      "authority": "authorized adjudicator"
    },
    {
      "id": "classify-retry-set",
      "effect": "Classify deterministic flaky environment-failure or inconclusive behavior across attempts.",
      "authority": "test authority"
    },
    {
      "id": "seal-evidence",
      "effect": "Seal a content-addressed evidence manifest for downstream assurance.",
      "authority": "evidence custodian"
    }
  ],
  "invariants": [
    "Every execution references exactly one immutable test-case revision.",
    "Every execution identifies an exact tested subject and content digest.",
    "Every execution references the environment in which observations were produced.",
    "Observed outcome and adjudicated verdict are distinct records.",
    "A verdict names the oracle comparison rule tolerance and evidence basis used.",
    "Passed failed inconclusive blocked and not-executed remain distinct.",
    "Retry attempts never overwrite prior observations or adjudications.",
    "Flakiness is classified across attempts and never inferred from one result alone.",
    "Defect state never becomes test-result state and test-result state never becomes defect state.",
    "A passing result on an unchanged digest cannot by itself verify a defect fixed.",
    "Requirement traceability pins the exact requirement revision.",
    "Environment failure does not become product failure.",
    "Evidence items are content-addressed and corrected only by supersession.",
    "Release gating consumes evidence by reference and never rewrites test history.",
    "Access redaction retention and disposal preserve manifest integrity and provenance."
  ],
  "holds": [
    "Exact Grok review and provider reconciliation are pending.",
    "One frozen no-tools semantic audit of the reconciled candidate is pending.",
    "Test Environment remains identifier-unassigned; WM-SFT-010 is only the current runtime reference.",
    "The frozen 33-source specification retains source-pin and clause-verification holds.",
    "Package conversion and live HTTP/runtime/search/package verification are pending."
  ]
}


## WM-SFT-015 fixtures
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-SFT-015",
  "version": "0.1.0-candidate.1",
  "cases": [
    {
      "id": "one-case-two-builds",
      "kind": "positive",
      "input": "One immutable test revision executes against release digests A and B.",
      "expect": "Two executions and evidence sets reference one definition revision and distinct subjects."
    },
    {
      "id": "flaky-retry-set",
      "kind": "positive",
      "input": "Three attempts on the same digest produce pass fail pass.",
      "expect": "All attempts remain; aggregate is classified flaky rather than overwritten passed."
    },
    {
      "id": "environment-failure",
      "kind": "negative",
      "input": "Execution aborts because the environment is unavailable.",
      "expect": "Result is blocked or inconclusive, not product failed."
    },
    {
      "id": "wrong-oracle",
      "kind": "negative",
      "input": "Observations are valid but the expected comparator is incorrect.",
      "expect": "Supersede the adjudication or definition; do not alter raw observations."
    },
    {
      "id": "defect-many-tests",
      "kind": "positive",
      "input": "Several executions cite the same defect with raised reproduced and verified-fixed roles.",
      "expect": "Execution verdicts and defect state remain independently governed."
    },
    {
      "id": "requirement-rebaseline",
      "kind": "negative",
      "input": "A requirement changes after a test execution.",
      "expect": "Historical execution remains pinned to the original requirement and test revisions."
    },
    {
      "id": "sealed-evidence-redaction",
      "kind": "positive",
      "input": "A public export redacts sensitive attachments.",
      "expect": "Original sealed manifest remains intact and export records derivation and omissions."
    }
  ]
}


## WM-SFT-014 candidate
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-TEC-08",
  "modelId": "WM-SFT-014",
  "registryId": "vr.wm-sft-014",
  "name": "Defect / Bug",
  "version": "0.1.0-candidate.1",
  "entryKind": "entity",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "sourceSpecSha256": "9700505b3d284903cd28a7b40a435107f227b4066cf3818cac1a800e1f54ef87",
  "purpose": "Represent an independently identified software defect record, its affected version and environment scope, evidence, classification, triage, resolution and verified closure without owning work assignment, corrective change, test execution or incident lifecycle.",
  "boundary": {
    "owns": [
      "defect-record identity and duplicate resolution",
      "deviation basis and terminology binding",
      "affected product version and environment assertions",
      "observation reproduction and evidence references",
      "defect classification severity impact and priority assertions",
      "defect state triage resolution verification and closure",
      "typed defect-to-defect relations and append-only history"
    ],
    "delegates": [
      "generic remediation work assignment and scheduling to WM-ACT-006",
      "corrective software change lifecycle to WM-SFT-013",
      "test specification execution result and evidence to WM-SFT-015",
      "requirement and expected-behaviour identity to WM-REC-006",
      "service incident restoration to WM-ACT-019"
    ],
    "excludes": [
      "inheritance from service case WM-ACT-021",
      "test execution or result state",
      "software change authoring review build release or deployment",
      "service incident response and restoration",
      "feature or enhancement requests without asserted deviation",
      "CVE or advisory publication lifecycle"
    ]
  },
  "objects": {
    "Defect": {
      "identity": [
        "defectId"
      ],
      "required": [
        "systemOfRecordRef",
        "masterRecordId",
        "termOfRecord",
        "deviationBasis",
        "affectedScope",
        "state",
        "reportedAt"
      ],
      "optional": [
        "globalIdentifiers",
        "duplicateOfRef",
        "severityAssertions",
        "priorityAssertions",
        "resolvingChangeRef",
        "verificationRefs"
      ],
      "lifecycle": [
        "submitted",
        "triaged",
        "assigned",
        "resolved",
        "verified",
        "closed",
        "withdrawn"
      ]
    },
    "AffectedScopeAssertion": {
      "identity": [
        "scopeAssertionId"
      ],
      "required": [
        "defectRef",
        "subjectArtifactRef",
        "versionRange",
        "scopeStatus",
        "assertedAt",
        "authorityRef"
      ],
      "optional": [
        "environmentRef",
        "justification",
        "supersedesAssertionId"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ]
    },
    "SeverityAssertion": {
      "identity": [
        "severityAssertionId"
      ],
      "required": [
        "defectRef",
        "scaleRef",
        "value",
        "assessorRef",
        "assessedAt",
        "rationale"
      ],
      "optional": [
        "vector",
        "supersedesAssertionId"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ]
    },
    "ResolutionAssertion": {
      "identity": [
        "resolutionAssertionId"
      ],
      "required": [
        "defectRef",
        "resolutionCode",
        "decidedAt",
        "authorityRef",
        "justification"
      ],
      "optional": [
        "resolvingChangeRef",
        "fixedInVersionRefs",
        "supersedesAssertionId"
      ],
      "lifecycle": [
        "proposed",
        "effective",
        "superseded",
        "withdrawn"
      ]
    },
    "VerificationAssertion": {
      "identity": [
        "verificationAssertionId"
      ],
      "required": [
        "defectRef",
        "verificationRunRef",
        "subjectDigest",
        "outcome",
        "verifierRef",
        "verifiedAt"
      ],
      "optional": [
        "evidenceRefs",
        "supersedesAssertionId"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ]
    }
  },
  "relations": [
    {
      "target": "WM-ACT-006",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve remediation tasks assignments and scheduling without inheriting Task identity."
    },
    {
      "target": "WM-SFT-013",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve the corrective software change and fixed-in versions."
    },
    {
      "target": "WM-SFT-015",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve test execution and verification evidence."
    },
    {
      "target": "WM-REC-006",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve expected behaviour requirements and acceptance criteria."
    },
    {
      "target": "WM-ACT-019",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve related service incidents while preserving separate lifecycles."
    }
  ],
  "operations": [
    {
      "id": "report-defect",
      "effect": "Create a defect with source identity affected scope and evidence.",
      "authority": "defect system of record"
    },
    {
      "id": "triage-defect",
      "effect": "Classify confirm prioritize and assign remediation references.",
      "authority": "authorized triage authority"
    },
    {
      "id": "assert-affected-scope",
      "effect": "Append affected not-affected fixed or under-investigation scope.",
      "authority": "product authority"
    },
    {
      "id": "record-resolution",
      "effect": "Record resolution code justification and corrective change references.",
      "authority": "defect owner"
    },
    {
      "id": "verify-resolution",
      "effect": "Record independent verification against an exact later subject digest.",
      "authority": "verifier role"
    },
    {
      "id": "close-defect",
      "effect": "Close only after resolution and required verification or justified non-fix disposition.",
      "authority": "closure authority"
    }
  ],
  "invariants": [
    "Defect identity is issued by the designated system of record and is independent of title date severity or affected version.",
    "Duplicate records remain resolvable and point to one surviving canonical record without deletion.",
    "A defect asserts deviation from an explicit requirement specification or adjudicated expectation.",
    "Affected scope assertions identify exact product or artifact versions and their assertion time.",
    "Severity and priority are distinct revisioned assertions with named scales.",
    "CVSS or another severity score never becomes work priority by implication.",
    "Defect state never becomes test-result state and test-result state never becomes defect state.",
    "A failing test may raise or reproduce a defect but does not prove root cause.",
    "A corrective change reference does not execute or complete the change lifecycle.",
    "Resolved is not verified and verified is not closed unless the state policy permits it.",
    "Verified-fixed requires evidence against a subject digest different from the digest on which the defect was raised.",
    "Non-fix dispositions require recorded justification and authority.",
    "Service restoration does not close the underlying defect.",
    "Reopening retains prior closure resolution and verification history.",
    "Confidentiality embargo retention and redaction rules preserve evidence integrity and reference resolution."
  ],
  "holds": [
    "Exact Grok review and provider reconciliation are pending.",
    "One frozen no-tools semantic audit of the reconciled candidate is pending.",
    "The embedded source specification has source-pin and clause-verification holds.",
    "Test Environment remains identifier-unassigned in EM-TEC-08.",
    "Package conversion and live HTTP/runtime/search/package verification are pending."
  ]
}


## WM-SFT-014 fixtures
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-SFT-014",
  "version": "0.1.0-candidate.1",
  "cases": [
    {
      "id": "one-defect-many-tests",
      "kind": "positive",
      "input": "Three test runs raise and reproduce one defect.",
      "expect": "One defect identity references all executions; each result keeps its own state."
    },
    {
      "id": "same-build-green",
      "kind": "negative",
      "input": "A retry on the unchanged defective build passes once.",
      "expect": "Defect cannot be verified fixed because the subject digest did not change."
    },
    {
      "id": "different-build-verification",
      "kind": "positive",
      "input": "An independent verifier passes tests on a later release digest.",
      "expect": "A verification assertion may advance the defect toward closure."
    },
    {
      "id": "test-oracle-defect",
      "kind": "negative",
      "input": "The expected result was wrong while product behavior conforms.",
      "expect": "Correct the test specification; do not create or close a product defect by implication."
    },
    {
      "id": "service-restored-defect-open",
      "kind": "negative",
      "input": "Service is restored by rollback while the software fault remains.",
      "expect": "Incident may close; defect remains open with remediation references."
    },
    {
      "id": "duplicate-report",
      "kind": "positive",
      "input": "Two trackers report the same deviation.",
      "expect": "Both identifiers remain resolvable and one is marked duplicate of the canonical defect."
    },
    {
      "id": "will-not-fix",
      "kind": "positive",
      "input": "Authority accepts a non-fix disposition with rationale.",
      "expect": "Resolution is retained with justification; it is not represented as verified fixed."
    }
  ]
}


## Test Environment allocation candidate
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-TEC-08","proposedName":"Test Environment","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed test environment remains identifiable across test runs and subject releases while its reproducible configuration and baseline evolve through controlled revisions.","versionIdentity":"Changes to runtime topology, services, dependencies, data fixtures, configuration, tooling or isolation controls create immutable environment-baseline versions.","independentLifecycle":["planned","provisioned","qualified","available","degraded","suspended","retired"],"mastership":"test infrastructure or environment-management authority"},"boundary":{"owns":["persistent test-environment identity","purpose and permitted test classes","environment topology and resource boundary","versioned configuration and dependency baseline","fixture and seed-data bindings","toolchain and harness bindings","isolation, access and reset controls","qualification, availability and retirement history"],"references":[{"target":"WM-SFT-015","purpose":"Test specification, run, result adjudication and verification evidence"},{"target":"WM-SFT-014","purpose":"Defect master and classification"},{"target":"WM-REC-006","purpose":"Requirement and acceptance-criterion revision"},{"target":"WM-ACT-006","purpose":"Remediation work"},{"target":"WM-SFT-008","purpose":"Tested build, release or artifact identity"},{"target":"WM-SFT-010","purpose":"Runtime or compute-environment resources"}],"excludes":["test specification, run, observation, verdict or evidence identity","defect, requirement, task, build or release identity","production runtime identity or deployment outcome","individual fixture content or dataset mastership","test-result classification or product-quality conclusion","access authorization beyond environment policy binding"]},"objects":{"TestEnvironment":{"identity":["testEnvironmentId"],"required":["name","purpose","ownerRef","status"],"optional":["successorRef","retiredAt"],"lifecycle":["planned","provisioned","qualified","available","degraded","suspended","retired"]},"EnvironmentBaseline":{"identity":["testEnvironmentId","baselineVersion"],"required":["topology","configuration","dependencyPins","validFrom","contentDigest","status"],"optional":["fixtureRefs","toolchainRefs","isolationControls","resetProcedureRef","validTo","supersedesVersion"],"lifecycle":["draft","qualified","effective","superseded","withdrawn"]}},"invariants":["Every reproducible test run references one exact environment baseline or records a reason for missing environment evidence.","Environment identity remains separate from production deployment and runtime identity.","Configuration, dependency, fixture, toolchain or isolation changes create a new immutable baseline.","A test environment never owns test specification, run, verdict, defect or release identity.","Environment qualification is scoped to declared test classes and never proves product quality.","Environment failure is an attributable adjudication supported by environment evidence.","A zero exit code, empty failure list or absence of defects never implies a passed test.","Flaky classification requires an attempt set with identical definition, parameters, subject digest and relevant environment baseline.","Environment degradation never silently rewrites prior run results.","Fixture limitations and representativeness remain explicit in every affected run.","Access, isolation and reset controls are versioned and auditable.","Retired baselines remain resolvable for historical evidence and rerun analysis."],"holds":["Registry namespace and identifier allocation are pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Environment cardinality and missing-environment fallback require normative decisions.","WM-SFT-015 parentage, relation rows and WM-REC-006 target validation remain unresolved.","Package conversion and live verification are pending."]}


## Test Environment fixtures
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Test Environment","cases":[{"id":"pinned-baseline-run","kind":"positive","input":"A run pins test revision, subject digest and qualified environment baseline.","expect":"The run is reproducible and each master remains distinct."},{"id":"environment-induced-failure","kind":"positive","input":"A dependency outage in the pinned environment blocks the test.","expect":"The attempt is classified environment failure or blocked with evidence, not product defect."},{"id":"flaky-attempt-set","kind":"positive","input":"Identical definition, subject and environment produce failed, passed and passed attempts.","expect":"All attempts remain and the set is classified flaky without rewriting verdicts."},{"id":"missing-environment-passes","kind":"negative","input":"A run with no environment evidence is declared reproducible and passed from exit code zero.","expect":"Both claims are rejected."},{"id":"environment-change-same-baseline","kind":"negative","input":"Toolchain and fixture changes are written into the same effective baseline.","expect":"The mutation is rejected and a successor baseline is required."},{"id":"test-repair-closes-product-defect","kind":"negative","input":"Changing the oracle advances a product defect to verified.","expect":"The transition is rejected."},{"id":"unchanged-build-verifies-fix","kind":"negative","input":"A pass on the original failing subject digest is used to verify the product fix.","expect":"The verification claim is rejected."}]}
