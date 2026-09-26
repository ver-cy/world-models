# EM-TEC-08 local synthesis

## Disposition

- Reuse WM-SFT-015 as the aggregate for TestSpecification, TestRun, TestResult adjudication and VerificationEvidence.
- Keep Defect in WM-SFT-014, Requirement/acceptance criterion in WM-REC-006, remediation work in WM-ACT-006 and tested release/artifact identity in WM-SFT-008.
- Treat TestResult as an adjudicated result attached to one TestRun rather than a separately mastered entity.
- Add an identifier-unassigned **Test Environment** candidate because environment configuration/baseline has independent identity and lifecycle and is required for reproducibility and environment-failure classification.
- Correct WM-SFT-015's parent link to WM-ACT-038. That model is Learning Activity / Course Delivery, not a generic testing parent. Do not guess a replacement before registry review.
- Allocate no runtime or model identifier.

## Identity and mastership

TestSpecification identity is an authoritative test-case key plus revision and canonical-content digest. TestRun has an execution key issued by the harness or test-management system and binds a frozen specification revision, exact subject digest and environment reference. TestResult is the observed outcome plus attributable adjudication on that run. VerificationEvidence is sealed by an evidence manifest and content digests. Defect keeps the defect tracker's independent key and lifecycle.

Expected behavior, oracle, comparison rule, tolerances and masking belong to the TestSpecification revision. Executable scripts are external implementation artifacts referenced through a binding. Script changes preserving the semantic contract do not change the specification revision; expectation or oracle changes do.

## Result and defect classification

Observation and verdict remain distinct. A verdict records assertor, mode, comparator/version and basis. `passed` requires an evaluated expectation and cannot be inferred from a zero exit code, empty failure list or absence of a defect.

Classification over the attempt set and binding distinguishes:

- product defect: deterministic failure against a verified subject and applicable environment;
- test defect: incorrect expectation, oracle, comparison rule or tolerance;
- environment failure: environment-induced error or block, requiring environment evidence;
- inconclusive/flaky: retained non-binary or attempt-set classifications, never silently passed.

Flaky is a property of an attempt set with proven-identical definition, parameters, subject and relevant environment. Every attempt retains its verdict and evidence. JUnit-style projections that collapse retries are explicitly lossy.

## Lifecycle and closure

Test specifications, runs/adjudications and defects have independent lifecycles. Corrections supersede adjudications; reruns create new attempts. Test repair can supersede a test adjudication but cannot advance a product defect.

A product defect may reach verified only through an attributable verification outcome against a different subject digest from the one on which it was raised, with the verifier role and evidence recorded. Fixing a test script, changing an oracle or obtaining a pass on the unchanged defective build does not satisfy this rule.

## Acceptance scenario

One defect is raised by one test and reproduced by two others. A retry set for one test contains failed, passed and passed attempts and is classified flaky without rewriting any attempt. A later run against release digest S2, distinct from failing digest S1, uses the pinned test revision, passes with sealed evidence and references the defect as `verified-fixed`. The defect may then advance to verified; all earlier conclusions remain true for S1.

## Invariants

1. A run binds one frozen specification revision by key and digest.
2. A run names the subject by digest and the environment by reference; missing environment makes reproducibility incomplete with a reason.
3. Flaky is an attempt-set classification, never a verdict.
4. Every verdict has an assertor and mode; pass requires an evaluated expectation.
5. Inconclusive, blocked, error, not-applicable and untested remain distinct.
6. A defect records observed and expected behavior and cites its requirement/expectation.
7. Test correction never transitions a product defect.
8. Defect state and result state never become each other.
9. Runs and evidence are append-only; corrections preserve predecessors.
10. Failure classification is an attributable adjudication that determines whether any defect record is created.

## Holds

Test Environment lacks registry allocation; WM-SFT-015 has the incorrect WM-ACT-038 parent and missing relation rows; WM-REC-006 lacks a verified target specification; WM-SFT-015 and WM-SFT-014 retain single-provider, source-pin, citation and artifact-identity holds; environment cardinality and non-reproducible fallback need a normative decision. This checkpoint makes no canonical completeness, installability or publication claim.


## Supporting WM-SFT-014 completion candidate

The frozen sixteen-source Defect specification is preserved as source evidence and normalized into an independent entity. Defect references Task, Software Change, Test, Requirement and Incident masters; it no longer inherits from Service Case. Verification-fixed requires a different subject digest from the one on which the defect was raised. Seven fixtures cover multi-test attribution, unchanged-build false closure, later-build verification, test-oracle defects, restoration without remediation, duplicates and will-not-fix.
