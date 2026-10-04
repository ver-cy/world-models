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
