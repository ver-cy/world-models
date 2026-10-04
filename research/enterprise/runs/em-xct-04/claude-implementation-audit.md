# EM-XCT-04 Enterprise Temporal History 0.1.0: adversarial semantic audit

This is a static reading only. I did not execute anything, recompute any hashes or check conformance against the parent or production systems. The test counts I cite are reports from the submission, not results I observed.

## Verdict: ACCEPT WITH LIMITS

Under the stated trusted-host boundary, I found no defect that breaks the core claims:

- Receipt order is kept separate from valid time.
- Intervals are half-open.
- Earlier snapshots survive as an exact prefix.
- Replay is bound to the full request.
- The expected-head check stops overwrites.
- The reader and purpose gate runs before the ledger is inspected.
- Pins stay immutable across history.
- Archive is terminal.

Two medium defects (D1 and D2) should either be fixed or written into `adoption-limits.md` before publication. Publication is the owner's decision.

## Input completeness

Both parts arrived. None of the numbered FILE sections looked truncated. Several referenced inputs were never supplied, so I cannot claim a full review of these:

- **`tool-pins.json`:** acceptance depends on it for the composer, skill and upstream digests.
- **`upstream/wm-xct-009-time-calendar/{spec.yaml, AGENTS.md}`:** I cannot compare them with the `specDigest` in spec.json.
- **`crosswalk.json`:** `adoption-limits.md` cites it for parent holds.
- **The native toolchain** (`composition`, `bootstrap_dimension`, `write_record`, `validate_dimension`):
  - I cannot say what native validation accepts.
  - I cannot say how `supersedes`, `status` and `validTo` behave in native reads.
- **Execution outputs** (`test-results.json` and the acceptance report): the 60 tests and three Dimensions are unverified. For reference, I counted exactly 60 `test_*` methods, which matches the claim.
- **spec.json:** supplied as an unlabelled "COMPLETE TREE" block with no filename or original hash. Its statistics (4/8/22/22/22/22) match its contents.

## Implementation defects

### D1 (medium): Archive, and any further correction, is blocked after a pin is retired from config

**Where:**
- `admit` calls `segments(request['segments'], config)` for every operation, including `archive`.
- An archive has to reproduce the prior segments exactly.

**How to reproduce:**
1. Start from `two`.
2. Set `cfg['acceptedSchemas']` to a new v2 pin only.
3. Submit an archive request with the segments copied from `two`.
4. Result: `Unaccepted schema binding`.

Removing a state code from `acceptedStates` has the same effect.

**Claims violated:**
- The lifecycle "empty → open → archived".
- "Archive … freezes further new writes" is meant to be available as a freeze operation.

**Knock-on effect:** Every correction is a complete snapshot. Retiring an old pin therefore forces one of two things:
- keep the deprecated pin accepted forever, or
- restate old effective periods under the new schema.

**Fix:** For `archive`, skip the acceptance check, since exact equality with the prior snapshot is already enforced. Alternatively, document that retired pins must stay accepted until the timeline is archived.

### D2 (medium): History is not bound to its Dimension or scope

**The gap:** The genesis `expectedHead` is `null`, and commit digests do not cover the header. So one timeline's commit chain can be moved under another header, and `validate_ledger` accepts it.

**The native gap:** `validate_snapshot` checks `subjectId == timeline` but takes no expected Dimension. A snapshot whose `ledger['dimension']` names Dimension A can be stored and validated as a fact in Dimension B.

**How to reproduce:** Store `fixture('startup')`'s `first` as the first snapshot fact inside the `group` Dimension, with `subjectId` set to the startup timeline. `validate_snapshot(f, now=NOW)` passes.

**Effects:**
- I01 ("scope/Dimension remain fixed") holds only inside a ledger, not in the native binding.
- Equal commits in different timelines produce equal `commit.digest` values in answers.

**Fix:** Either make the genesis `expectedHead` a digest of the header, or include the header digest in each commit. Also add a `dimension=` argument to `validate_snapshot`.

### D3 (low–medium): A payload revision can be rebound to a different schema or state

**Where:** `value_definitions` binds only `(id, revision) → digest`.

**How to reproduce:** Take q2 and set `segments[0].schema` to an accepted v2 pin while keeping `value('team-a')` r1. The request is admitted. The same past period and the same payload are now interpreted under v2 in the current view.

**Claims affected:**
- I10 and I16 hold literally for old commits only.
- The prose "old segments retain their original pins" reads as though they should hold more broadly.

**Fix:** Either bind the value pin to its schema (and state profile) across history, or state explicitly that rebinding in a new snapshot is allowed.

### D4 (low): `validate_snapshot` is weaker than the spec says

- **Overclaim:** The spec says it checks a "unique successor fact ID". It only checks `factId != previous.factId`, so reusing an older ancestor's ID is not detected.
- **Unchecked envelope fields:** `status`, `validFrom`/`validTo` and `recordedAt` are not checked. I cannot tell whether native reads could make a snapshot expire or look retracted, because native semantics were not supplied.
- **Wrong exception type:** A missing envelope key (for example `provenance.previousSnapshotDigest`) raises `KeyError`, not `Invalid`. It still fails closed, but callers catching `Invalid` will not handle it.

### D5 (low): A full timeline can never be archived

**Where:** `sequence.maximum = 1000` and the 8 MiB ceiling.

**Effect:** A ledger with 1000 commits, or one near 8 MiB, cannot take its archive commit, so it stays open permanently. This is not listed among the overflow and rollover limits.

### D6 (low): Docs and code disagree in small ways

- **Order of checks in `resolve`:** The spec says `resolve` "first checks … reader and purpose permission". In fact `configuration()` runs first. So a denied caller can receive `Current configuration unavailable`, or a schema-violation message that echoes config values. This is contained only if the host keeps diagnostics internal, as AGENTS.md requires.
- **`inputDigest`:** Described as covering "query input", but it is the digest of the ledger only.

## Test and acceptance evidence gaps (not code bugs)

- **Acceptance "truncation" case:** Clearing `commits` makes `snapshotDigest` wrong, so the rejection comes from the digest check, not the prefix check. The acceptance run gives no evidence of prefix enforcement when a truncated snapshot carries a recomputed digest. The unit test `test_no_history_truncation` does cover `validate_extension`.
- **`test_clock_regression`:** It is rejected by the `Future receipt` check. The "Receipt clock moved backwards" branch, which matters for imported ledgers, is never exercised.
- **`test_segment_overflow`:** The duplicated segments would also fail the overlap check, so the test does not isolate the `maxItems` bound.
- **Aliased fixture objects:** The schema and profile dicts are shared between segments and config, and `deepcopy` keeps that sharing. `test_binding_repoint_in_history` depends on it without saying so. It is correct, but fragile.
- **Not tested at all:**
  - archive after pin rotation (D1)
  - cross-Dimension or transplanted snapshot (D2)
  - rebinding a payload to a new schema (D3)
  - reusing an ancestor fact ID (D4)

## Checked and consistent

- **Timestamps:** Strict ASCII grammar, validated with `fullmatch`. `strptime` combined with `datetime` rejects Feb 30 and seconds of 60. Trailing newlines, fractions, offsets and full-width digits are rejected. Lexicographic comparison is valid for this fixed width.
- **Knowledge cutoffs:** `knownAt ≤ now`. A future `validAt` is allowed. Config validity is half-open. Receipts are non-decreasing. `sequence` must be an exact `int` (rejects `bool` and `1.0`). `knownSequence` is bounded, and 0 means before any receipt. The filtered commits always form a prefix, so pinning a sequence gives stable content.
- **Intervals:** End-exclusive. Zero-length, reversed and overlapping segments are rejected. An open-ended segment must be last. Gaps and empty snapshots return `insufficient-context`, with a distinct message before the first receipt.
- **Replay:** Checked before the head and archive guards. It compares the full canonical request and the writer, keeps the first receipt and revalidates the current writer and config. Reusing a revision under a new key is rejected. The input ledger is never mutated.
- **Pins and version grammar:** Pins cannot be repointed, in config or across history. Version strings use the numeric triplet only. The format checker must be present, or validation fails.
- **Snapshot append:** The header is fixed. The exact commit prefix is required. Migration refuses any other version.
- **Answer fields:** Truth, domain validation and transition legality are reported as not evaluated. `archivedAsKnown` and `archiveNow` are kept separate.
- **Declared taxonomy:** Coverage uses the five canonical facets for all six types. Slug, `$id`, registry ID and namespace agree.

## Explicit adoption limits (documented, not defects)

- **Host-only integrations:** The trusted host must supply:
  - the actor, current config, latest root and clock;
  - rejection of stale or forked roots (the library cannot detect an omitted newer root);
  - durable conflict artifacts;
  - raw size limits and duplicate-key rejection before parsing;
  - scope uniqueness;
  - withholding the returned full ledger from write-only callers.
- **Not implemented:**
  - IAM
  - signatures or clock attestation
  - payload or schema validation
  - transition engine
  - erasure, retention or disposal
  - backdated bootstrap
  - existing-Dimension migration
  - capacity claims
- **Withdrawal looks like never-asserted:** A correction that drops a period makes it unknown in the new view. The answer cannot distinguish "withdrawn" from "never asserted", and no contrary-evidence signal is given.
- **Pinned dependencies:** Versions are pinned without hashes. I have not verified jsonschema 4.26.0.
