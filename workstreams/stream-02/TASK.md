# Stream 02 task

Process the 52 exact rows in `SCOPE.csv` in ascending sequence. The first two are
sequence 91 `WM-ACT-007 Work Order` and sequence 97 `WM-DAT-002 Official
Statistics`; the final row is sequence 397 `WM-LIV-022 Conservation Status
Assessment`.

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
commit per model to `research/stream-02`. Record the model and completion state
in `LOG.md` before committing, then report the resulting commit hash to stream
01 in the chat response; do not create a second log-only commit for the hash.
