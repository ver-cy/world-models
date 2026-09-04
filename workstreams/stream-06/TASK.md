# Stream 06 task

Process the 52 exact rows in `SCOPE.csv` in ascending sequence. The first two are
sequence 95 `WM-ACT-023 Public Health / Epidemiology` and sequence 101
`WM-FLW-004 Goods Movement / Logistics`; the final row is sequence 401
`WM-OBJ-024 Robot / Autonomous Machine`.

For each model, freeze the registry boundary, run bounded Claude research only
while holding the global Claude lease, apply transport-only normalization when
needed, create the policy-aware comparison, perform a separate no-tools
adversarial adjudication, synthesize and validate. Generate the full published
package with `AGENTS.md`, `spec.yaml`, card and publication manifest. Publication
status is `published`; research assurance remains `reviewable-draft` with every
hold visible. Stop on any critical conflict or validation failure.

Change only this stream's log/state and the assigned model's research and
publication directories. Never update `research/status.csv`, shared plans,
tools, another stream, the site mirror or production. Push one secret-safe
commit per model to `research/stream-06` and record its hash for stream 01.
