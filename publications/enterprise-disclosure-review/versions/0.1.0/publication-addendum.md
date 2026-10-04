# Publication limits recorded after the final freeze

This is Codex publication bookkeeping and a restrictive adoption notice, added after the 33-file R3 audit freeze. Claude and Grok did not review this addendum or the supplementary boundary-check script. Their exact responses and scope remain preserved. No frozen code, schema, specification or test file was changed after review.

## Capacity preflight is mandatory

The 262,144-byte limit applies independently to each canonical record, native fact envelope and complete host snapshot. A valid record is not guaranteed to fit its enclosing fact or an inspection snapshot. The maxima are not simultaneously achievable. Before admitting a record, the host must validate the intended complete envelope and complete current snapshot as well as the record; catch Invalid and treat failure as unavailable/insufficient capacity. Do not silently truncate fields, reviewers, history or context to fit. The reference ships no reserved-headroom algorithm, rollover or enterprise-scale store.

Codex reproduced this limit against the unchanged release code: a 262,040-byte proposal imports successfully but its native envelope and a sufficiently populated snapshot fail closed with size. A 116,632-byte proposal succeeds with that same expanded actor catalogue. These are witnesses, not universal safe-size thresholds. See post-audit-boundary-results.json. Future growth in the snapshot can still invalidate a previously fitting record.

## Native installation is a subset of the full package

The synthetic composer installs five operational files. That subset does not include all adoption documentation. Before using it, the host/agent must obtain and pin the complete versioned ZIP and publication manifest, including this addendum, bindings/native-v3.md, adoption-limits.md and review.json. The installed spec.json contains the model-spec.md text as its contract property; read that property if the standalone Markdown is absent. The disclosure.py docstring's review.md is in the full ZIP, not the installed subset.

“Denied” in question-answer guidance means the host refuses the action. The reference raises Unauthorized instead of returning a denied status. Native storage objects must remain active for this version to validate their historical facts; withdrawal/retirement of review applicability is a separately governed snapshot change. An applicable-review diagnostic does not settle grants, classification comparability, custody holds or delivery. These remain mandatory host checks before serving.

## Evidence interpretation

acceptance-results.json is emitted only after every assertion succeeds; failed is structurally zero because any failure aborts rather than writing a misleading success report. Its object/fact counts are fixture constants corroborated by the included native validator counts, not a general monitoring metric. The supplementary report exercises the previously untested withdrawal conflict, register/review-count and Dimension guards without changing the frozen 108-test suite.

The earlier crosswalk timestamp and later five-parent byte-check timestamp are distinct evidence events. The latter is a fresh repeat comparison, not the first possible reading. Initial adjacent runtime reconnaissance is retained as history. Parent catalogue status/assurance assertions are comparison metadata, not independently ratified production or standards readiness. The overlap relation on a parent row and selected-semantic-overlap-not-subtype in composition describe broad relation versus selected usage; neither asserts subtype compatibility. WM-XCT-002 is explicitly a boundary reference with no selected findings.

This is a bounded reviewable draft for synthetic-tested metadata review. Broad EM-XCT-05 remains partial. Use a separately reviewed production adapter and capacity design for a large company; publication itself establishes neither their existence nor their readiness.
