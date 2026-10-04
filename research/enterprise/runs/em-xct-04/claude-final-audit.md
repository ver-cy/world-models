# Audit verdict: EM-XCT-04-R3, Enterprise Temporal History 0.1.0

**Verdict: ACCEPT WITH LIMITS**, as a reviewable-draft, trusted-host reference.

R2 findings F1–F6 are resolved. F1 and F2 are resolved as explicit adoption limits, and F3–F6 as code, test or wording fixes. I found no regression that breaks a stated invariant (I01–I16) under the trusted-host boundary. I found three new low-severity items:

- **N1:** a consequence of the new predecessor-ordering check that is not documented.
- **N2:** a clock-guard scope that is too narrow.
- **N3:** a small remaining test gap.

None of these blocks a reviewable draft. This verdict does not authorize publication; the owner's standing authorization governs that.

This was a static reading only. I did not execute tests or acceptance, recompute any byte hash, authenticate any receipt, or check composer, skill, native-validator or parent conformance.

## Input completeness

No section appears truncated. The schema closes correctly, tool-pins.json is complete, and every `FILE … END FILE` pair is present.

**Fully read:**
- temporal.py, test_temporal.py, temporal.schema.json
- model-spec.md, spec.json (now with a FILE header and hash), AGENTS.md, acceptance.py
- whole-object-coverage.yaml, mastership-and-rights.yaml, requirements.txt, runtime-model.reference.json
- adoption-limits.md, migration.md, bindings/native-v3.md
- crosswalk.json, tool-pins.json

**Still not supplied:**
- Composer and skill code: `composition.py`, `bootstrap_dimension.py`, `write_record.py`, `validate_dimension.py`, and the rest of the pinned skill tree.
- The `upstream/wm-xct-009-time-calendar/` files.
- test-results.json and the acceptance report.

The native-acceptance evidence depends on this unsupplied code. For example, whether `c.now()` emits second-precision `Z` instants that `instant()` accepts cannot be checked here.

**Internal consistency, not byte-verified:**
- The spec.json `contract` string reads as textually identical to model-spec.md.
- The three `specDigest` values in spec.json match the `sha256` values in crosswalk.json.
- The WM-XCT-009 digest also matches `upstreamFiles/…/spec.yaml` in tool-pins.json.
- The test count matches: 66 carried-over or renamed tests plus 18 `test_snapshot_*` tests plus 2 new tests gives 86. Pass status of these tests and of the 3 native checks is unverified by me.

## Reassessment of R2 findings

| R2 | Status | Basis |
|---|---|---|
| **F1** backdated receipts in a native Dimension | **Resolved as explicit limit** | TH-F10 now reads "this timeline host". model-spec, adoption-limits, migration and native-v3 all state that `knownAt` is the host axis, not native storage. The fixture is described as later storage of synthetic earlier host history. The acceptance report carries `envelopeAuthorityMeaning`. The earlier over-claim ("No source-knowledge bootstrap can insert earlier local receipt times") is gone. It is replaced by "cannot enforce a real-world creation floor". The code still enforces no floor, and that is now the claim. |
| **F2** forward clock excursion bricks the timeline | **Resolved as explicit limit** | Disclosed in four documents with a quarantine/freeze procedure and two recovery routes (verified catch-up, or a new governed timeline identity with disclosed loss of continuity). `test_forward_clock_excursion_needs_external_recovery` demonstrates that both `resolve` and replay-`admit` reject with `Future receipt`. See N1 and N2 for residual scope. |
| **F3** scope check after ledger validation | **Fixed** | `resolve` order is now config → reader/purpose gate → `matching` → `validate_ledger`. `admit` order is config → writer gate → `matching` → `validate_ledger`. `matching` safely handles non-dict and missing-key input (`Missing governed scope`). `test_scope_gate_before_history_diagnostics` covers both paths with a corrupted sequence. I09 still holds: `test_denied_read_before_diagnostics` reaches the gate before `matching`. |
| **F4** asymmetric predecessor validation | **Fixed** | `snapshot_envelope` runs on both `fact` and `previous`. A missing `provenance` or `path` now raises `Invalid` (tested). A retracted state, unit or closed `validTo` on the predecessor is rejected (tested). `Snapshot receipt precedes predecessor` closes the successor-predates-predecessor gap (tested). |
| **F5** no `validate_snapshot` unit tests | **Largely fixed** | 18 direct tests now use `assertRaisesRegex`, so each names the rule that rejected. Messages for previous-envelope failures are now shared with the current envelope. That is acceptable because the same function checks both. Residual gap in N3. |
| **F6** wording and evidence | **Fixed** | Spec now says "scheme-bearing RFC 3986 URIs (fragments are permitted)". This matches the jsonschema `uri` rule, which requires a scheme and permits fragments. Replay now reads "canonically equivalent". AGENTS.md now says "during parsing". The misleading test was renamed to `test_admission_rejects_input_ahead_of_host_clock`. `codeDigest` now hashes raw bytes (`read_bytes()`) with a `sha256:` prefix, so it is comparable to `original_sha256` after stripping the prefix. |

## New findings

### N1 — Low — the forward-excursion lock also applies at the native storage layer, undocumented

The new check `fact['recordedAt']>=previous['recordedAt']`, combined with `fact['recordedAt']<=now` in `snapshot_envelope`, creates the same failure mode as F2 on the native envelope.

Reproduction:
1. Store a native fact with `recordedAt=validFrom='2026-12-31T00:00:00Z'` around a valid ledger. This passes if validated with a matching host `now`.
2. With the correct `now`, the fact itself fails `Invalid snapshot receipt envelope`, whether it is validated as current or as `previous`.
3. Any successor must have `recordedAt ≥ 2026-12-31` and `≤ now`. No valid successor exists until real time catches up.

The disclosures describe "a mistakenly admitted forward receipt" in terms of the inner timeline axis only. The native store is append-only, so the same quarantine/new-identity reasoning applies.

Fix: extend the forward-excursion paragraph to native storage receipts.

### N2 — Low — the clock-skew guard is specified only "before every admission"

`resolve`, `validate_ledger` and `validate_snapshot` all trust `now` as well:
- A backward read clock makes reads fail with `Future receipt`. This is transient, but it is a read outage.
- A forward read clock can select a configuration whose `validFrom` has not yet arrived, or accept a `knownAt` in the real future.

These are host-clock trust issues that are already covered by the general boundary, so this is not a code defect. However, the specific guard wording invites a host to guard only writes.

Fix: say the skew check applies to every call that takes `now`.

### N3 — Low — evidence gap: the append-only branch of `validate_snapshot` has no unit test

`validate_extension(previous['value'], ledger, …)` inside `validate_snapshot` is exercised only by the acceptance `truncation` negative. That negative depends on unsupplied pinned code and asserts only that some `Invalid` was raised.

A direct unit case would close this. For example, `snapshot(f_with_value=self.one, previous=f2)` with the digests recomputed should raise `History rewritten/truncated`.

The other acceptance negatives (`digest`, `subject`, `predecessor`, `cross-Dimension`) still assert no specific message. They are, however, now mirrored by message-specific unit tests.

## Informational, not defects

- **No-op successors are accepted.** `validate_extension` allows `len(new)==len(old)`, so a successor native fact whose ledger is identical to the predecessor's (for example, the result of an `admit` replay) passes. It is consistent with "append-only", but a host may want to avoid duplicate storage facts.
- **Acceptance admits at synthetic times.** acceptance.py calls `admit(..., now=T1/T2)` at run time. This departs from "new admission must call admit with the actual timeline-host time", but it is now explicitly framed as simulating a pre-existing host history. It is acceptable as disclosed.
- **Redundant extension check in native-v3.md.** It instructs calling `validate_extension` after `validate_snapshot`, which already calls it. This is harmless.
- **Previous envelopes are not checked for their own predecessor linkage.** A previous fact's `supersedes` and `previousSnapshotDigest` are not validated, because that needs the grand-predecessor. This is consistent with the documented "immediate predecessor only" limit.
- **Unverifiable crosswalk flag.** crosswalk.json asserts `liveByteEqualityVerified: true` for all parents, and I cannot verify that. The parent holds, including WM-XCT-022's "effective-period finding must ship marked as partial support", are parent publication holds. They apply to this companion only through the semantic-reference relation, which it does not claim as conformance.

## Adoption limits confirmed as explicit, carried over from R2

- Authentication, latest-root selection, serialization, forks, the clock and conflict artifacts are host responsibilities.
- Config errors are raised before the read gate and must be genericized by the host.
- `admit` returns the whole ledger, and the host must not forward it to a write-only caller.
- Replay after writer rotation is denied.
- `reason` content is unenforced.
- Imported never-accepted pins are retained.
- Removed or retracted periods resolve as an indistinguishable `insufficient-context`.
- Erasure, retention and legal hold are absent.
- Imported receipts are unauthenticated.
- Capacity: 8 MiB is likely to bind well before 1000 commits for large snapshots, and even an archive commit may be refused at the ceiling.
- Existing-Dimension migration is deferred.

## Process disclosures the owner should carry into any draft

- **Outstanding Grok code audit.** It has not been submitted, and the contour remains unfinished. Per your instructions, any published draft must say so prominently.
- **No native-toolchain conformance.** The native pass reports (86 tests and 3 native checks) are separately executed claims that I have not reproduced. Native-toolchain conformance is outside this audit because the pinned composer and skill bytes were not supplied.

## What I did not do

I did not:
- Execute any test or acceptance run.
- Recompute any declared hash.
- Verify real-world receipt or clock authenticity.
- Inspect the composer, skill, native validator or upstream WM-XCT-009 bytes.
- Verify WM-XCT-009/021/022 live availability, the crosswalk holds, or parent conformance.
