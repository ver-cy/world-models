# Stream 03 task

Process the 52 exact rows in `SCOPE.csv` in ascending sequence. The first two are
sequence 92 `WM-ACT-014 Health Care Delivery` and sequence 98 `WM-ECO-001 Market
/ Exchange`; the final row is sequence 398 `WM-SPC-003 Astronomical
Observation`.

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
commit per model to `research/stream-03` and record its hash for stream 01.
