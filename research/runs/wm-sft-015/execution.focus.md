Research only test execution, result and evidence for WM-SFT-015 Test Case /
Test Result.

- Use the exact registry identity and output `entry_kind` `aggregate`.
- The `model` block must describe the complete combined WM-SFT-015 boundary,
  not merely this split pass. Include definition/design, execution/results,
  assurance and governance as in scope while limiting this result's structure,
  functions and evidence gathering to execution and result concerns.
- Cover execution/result identity; binding to an exact test-case revision;
  run, suite/campaign, build/release, environment and actor/tool references;
  start/end/observation/ingestion times; parameter values; actual outcomes;
  pass/fail/error/blocked/skipped/inconclusive semantics; per-step outcomes;
  comparison details and tolerances; logs, screenshots, traces and attachments;
  integrity/digests; retries and attempts; flaky/non-deterministic evidence;
  defect links; supersession/correction and reproducibility context.
- Preserve the difference between observed facts and an adjudicated result.
  Do not let a rerun overwrite earlier evidence, do not infer pass from absence
  of a defect, and do not identify a result by a date, status or test-case ID
  alone. Use master-system IDs first and RFC 3339 timestamps with seconds and
  an explicit offset or `Z`.
- A build/release only references test evidence (the existing WM-SFT-008 ->
  WM-SFT-015 relation). Do not copy release, defect, environment, identity,
  authorization or audit-log lifecycles into this model.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight distinct question kinds.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `tst-exec-`.
- Limit functions to executing, recording, adjudicating, retrying, comparing
  and exporting results/evidence. Provide complete schema-valid service_layers
  and coverage objects, but keep them concise; the merger takes canonical
  service layers from `governance`.
- Prefer stable primary result formats and first-party specifications such as
  JUnit XML documentation/schema, TAP, SARIF where applicable, W3C test
  metadata/results and official testing standards. Label ecosystem conventions
  as projections rather than universal semantics.
