# Stream 01 task

Process the 52 exact rows in `SCOPE.csv` in ascending sequence. The first two are
sequence 90 `WM-XCT-037 Dependency / Impact` and sequence 96 `WM-BLT-001
Building / Structure`; the final row is sequence 396 `WM-LIV-020 Microbiome /
Biological Community`.

For each model, freeze the registry boundary, run bounded Claude research only
while holding the global Claude lease, apply transport-only normalization when
needed, create the policy-aware comparison, perform a separate no-tools
adversarial adjudication, synthesize and validate. Generate the full published
package with `AGENTS.md`, `spec.yaml`, card and publication manifest. Publication
status is `published`; research assurance remains `reviewable-draft` with every
hold visible. Stop on any critical conflict or validation failure.

Worker commits may change only this stream's log/state and the assigned model's
research and publication directories. Do not update shared status or planning
files in a worker commit. Push one secret-safe commit per model to
`research/stream-01`.

This stream is also the sole coordinator. Separately from provider work and
only while holding the integration and production leases, it may integrate one
ready model commit from any stream into `feat/mega-model-registry`, regenerate
the shared status, deploy that one package and the rebuilt catalogue import,
run Bitrix migration plus complete HTTP/SEO/AEO/GEO checks, then push. No other
stream may perform those actions.
