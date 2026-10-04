# Audit verdict: EM-XCT-04-R2, Enterprise Temporal History 0.1.0

**Verdict: ACCEPT WITH LIMITS**, as a reviewable-draft, trusted-host reference.

I found no defect in the executable core that breaks a stated invariant (I01–I16) under the documented trusted-host assumptions. I did find one material claim/fixture mismatch (F1), one undocumented unrecoverable failure mode (F2), several low-severity implementation inconsistencies, and a real test-evidence gap (F5). F1 and F2 should be corrected in documentation before publication. That decision belongs to the owner; I cannot grant publication.

This was a static reading only. I did not execute anything, recompute any byte hashes, or check parent or production conformance.

## Supplied-input completeness

Both parts arrived and no file section appears truncated. These are fully reviewed: temporal.py, test_temporal.py, temporal.schema.json, model-spec.md, AGENTS.md, acceptance.py, whole-object-coverage.yaml, mastership-and-rights.yaml, requirements.txt, runtime-model.reference.json, adoption-limits.md and migration.md.

Not supplied, so claims that depend on them are unreviewed:
- **Prior audit list D1–D6.** It is not in this conversation. I reassessed against your revision summary, not against the original defect text.
- **spec.json.** A tree was supplied, but without a FILE header or hash, so I cannot tie it to the bytes acceptance.py hashes. Its internal statistics (4/8/22/22/22/22) are consistent.
- **crosswalk.json**, which adoption-limits.md cites for parent holds.
- **tool-pins.json and upstream/wm-xct-009-time-calendar/**.
- **Composer and skill code**: `composition`, `bootstrap_dimension`, `write_record`, `validate_dimension`. All native-acceptance evidence depends on these.
- **test-results.json and the acceptance report.** The 66-test count matches the file (I counted 66 `test_` methods). Pass status is unverified.

## Reassessment of the stated revisions

| Revision claim | Static finding |
|---|---|
| scopeDigest binds each commit to the header | Holds. It is checked per commit in `validate_ledger`, and the head chain digests include it. The test covers dimension, timeline and scope transplant. It is consistency, not authentication (documented). |
| Native check needs the expected Dimension | Holds for both the fact and its predecessor (`validate_snapshot`). |
| Unchanged segments may keep retired pins | Holds. A segment is exempt only if it exactly equals a segment of the immediately preceding snapshot. Archive after retirement works. A changed interval requires current pins (tested). |
| Rebinding is a new interpretation | Allowed only with accepted pins. Nothing structural marks it; the `reason` content is unenforced (limit). |
| Capacity-limited archival, config diagnostics before the read gate | Documented and consistent with the code. |
| Immediate-only predecessor ID check | Documented, but see F4 for an asymmetric validation gap. |
| Truncation negative recomputes the digest | Holds. Rejection comes from `validate_extension`. |
| Cross-Dimension, imported clock regression, 101-segment non-overlapping case | Present. See F6 about the older `test_clock_regression`. |

## Findings

### F1 — Medium — claim/fixture mismatch: backdated receipts reach a native Dimension

`validate_snapshot(fact, previous=None)` accepts a genesis snapshot whose inner commits carry any past `recordedAt`, as long as each is ≤ the fact's `recordedAt`. `admit` also accepts any host-supplied `now` inside config validity.

acceptance.py demonstrates the problem itself:
1. It bootstraps a fresh Dimension at run time (≥ 2026-09-21).
2. It installs `first` with inner receipt T1 = 2026-01-10.
3. `resolve(knownAt='2026-01-31T00:00:00Z')` then reports `team-a` as recorded, for a Dimension that did not exist then.

A direct reproduction: build a ledger with `admit(..., now='2019-06-01T00:00:00Z')` and a config valid from 2019, wrap it as a genesis fact, and `validate_snapshot` accepts it.

Claims this contradicts:
- TH-F10: "What had **this Dimension** recorded by a cutoff?"
- TH-ACT19: "refuse backdated bootstrap"
- model-spec: "No source-knowledge bootstrap can insert earlier local receipt times"

The code enforces nothing here; it is pure host discipline, and the shipped fixture violates it.

Fix, either or both:
- State that `knownAt` is the timeline host's receipt axis, not the native Dimension's.
- Add an explicit host-supplied installation floor to genesis `validate_snapshot`, and generate acceptance receipts after bootstrap.

### F2 — Medium — undocumented limit: one forward clock excursion bricks the timeline

Reproduction:
1. `admit(two, q3, cfg, actor=writer, now='2026-12-31T00:00:00Z')` succeeds, because config is valid until 2027-01-01.
2. `resolve(..., now=NOW)` then raises `Future receipt`, and so does every later `admit(..., now=NOW)`.

Reads and writes stay dead until real time passes the bad receipt. By then the config (expiring 2027-01-01) is nearly expired. Rollback is forbidden by migration.md, and truncation is rejected.

The spec says only "Clock regression rejects." It never says a single bad receipt makes the timeline unrecoverable within the contract.

Fix: document this explicitly and require a host guard (e.g., `now ≤ trusted_reference + skew`) plus an operational recovery path.

### F3 — Low — implementation: scope matching runs after full ledger validation (I09 ordering)

In both `resolve` and `admit`, `validate_ledger` runs before `matching`. Reproduction:
- Use the reader and config for scope A.
- Pass a ledger for scope B that contains, say, a payload repoint.
- The caller receives `Payload revision repointed`, a diagnostic about B, instead of `Wrong governed scope`.

This requires a host root-selection error, but the fix is trivial: run `shape(ledger,'ledger')`, then `matching`, then chain validation.

### F4 — Low — implementation: predecessor validation in `validate_snapshot` is asymmetric

A genesis predecessor gets a full envelope check. A non-genesis predecessor gets only `validate_ledger` plus path/subject/digest checks. Reproduction:
- Take `f2` and set `status='retracted'`, `unit='kg'`, `validTo` non-null, or `recordedAt` earlier than its inner receipt.
- It is still accepted as `previous` for an `f3`.
- A non-genesis `previous` missing `provenance` or `path` raises `KeyError`/`TypeError` rather than `Invalid`.

None of these envelope checks needs the grand-predecessor, so they could run unconditionally.

There is also no fact-to-predecessor time ordering. In acceptance, set `f2.recordedAt = validFrom = '2026-02-10T00:00:00Z'` while `f1.recordedAt` is the September run time: it is accepted, so the successor predates what it supersedes. This is not claimed, but it is a gap to state or close.

### F5 — Medium — evidence gap: `validate_snapshot` has no unit tests

None of the 66 tests calls `validate_snapshot`. These branches are therefore exercised only via acceptance.py, which depends on unsupplied pinned code, or not at all:
- `Incomplete snapshot envelope`
- `Unsupported snapshot envelope state`
- `Invalid snapshot receipt envelope`
- `Snapshot precedes inner receipt`
- `Unexpected predecessor`
- `Wrong previous native Dimension`
- `Wrong previous timeline binding`
- `Previous snapshot digest mismatch`
- `Wrong previous snapshot digest`

Acceptance negatives also assert only that some `Invalid` was raised, not which rule rejected the input. The "invalid nested snapshot" case does reach `shape` before the digest check, so it happens to test the intended rule.

The native-binding claim (I13) is therefore not independently evidenced by the supplied executable material.

### F6 — Low — documentation and evidence mismatches

- **Absolute URIs.** The spec says "absolute URIs", but jsonschema's `uri` format (rfc3986 `URI` rule) accepts fragments, e.g. `urn:x:y#f`. RFC 3986 absolute-URI excludes them.
- **Replay equivalence.** The spec says "byte-equivalent request"; the code compares canonical re-encodings.
- **AGENTS.md wording.** "Duplicate-key rejection before parsing" should say *during* parsing.
- **`test_clock_regression`.** It actually fails on `Future receipt` in the input ledger. A receipt regression is unreachable through `admit`, since receipt = `now` and prior receipts must be ≤ `now`. Only the new imported-ledger test hits the `moved backwards` branch. The label is misleading; behavior is fine.
- **`codeDigest` in test-results.json.** It is the sha256 of the JSON-quoted, newline-normalized source text. It is not comparable to `original_sha256`. acceptance.py's `sourceDigests` are raw-byte hashes and are comparable.

## Adoption limits confirmed as explicit, not bugs

- Stale or forked roots, serialization, and omitted newer roots are the host's responsibility. `admit` on a stale root forks silently.
- Replay after writer rotation returns `Write denied`, not "already applied". Replay after pin retirement succeeds (pins are not rechecked).
- Config errors are raised before the read gate, and the host must genericize them.
- `admit` returns the whole ledger, and the host must not forward it to a write-only caller.
- Removed or retracted periods resolve as an indistinguishable `insufficient-context`, with no contrary-evidence signal. Erasure, retention and legal hold are absent.
- `reason` content, including removal and rebinding justification, is unenforced.
- Imported ledgers may carry never-accepted pins that can then be retained indefinitely.
- **Capacity.** The 1000-commit ceiling is illusory for full snapshots. At roughly 600 bytes per canonical segment (my estimate, not measured), 100-segment snapshots hit 8 MiB at around 140 commits. After that, even archive is refused (documented).
- Leap seconds, offsets, fractions, fullwidth digits and trailing newlines are rejected. Pattern `$` leniency is backstopped by `fullmatch` in `instant` and in the digest/version checks.

## What I did not do

I did not run the tests or acceptance, recompute hashes, inspect composer, skill or native-validator behavior, or verify WM-XCT-009/021/022 alignment or the crosswalk.
