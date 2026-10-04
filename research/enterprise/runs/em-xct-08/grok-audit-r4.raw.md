**ACCEPT WITH LIMITS**

Severity: Medium operational residual / Low contract. No High implementation breaker in the patched reducer against the accessible R3 baseline.

## Input completeness

Accessible for this delta audit:
- All 30 R3 body-supplied files from this conversation.
- Complete 8-part R3→R4 unified diff plus added `benchmark.py`, `benchmark-results.json`, `environment-report.json`.
- END MARKER `SYNC-R4-DELTA-20260922` present.

Not accessible as bodies (correctness not inferred from hashes):
- Eight inventory-only names: `parent-comparison.md`, `provider-roles.json`, `research-adjudication.md`, `research.md`, `source-verification.json`, `upstream/wm-xct-012-provenance/{AGENTS.md,publication.json,spec.yaml}`.
- Composer, native writer, and parent runtime implementations listed in `tool-pins.json`.

Reconstruction limit, not a missing-file blocker: the R3 `sync.schema.json` body arrived minified; the R4 hunk is a pretty-printed `maxItems` 2000→128 change and would not apply as a textual patch onto that transported body. Semantic R4 schema is still readable from `build_schema.py` (`events` cap 128) plus that field. Do not treat transported R3 schema bytes as proven R4 file bytes.

No tools, no execution, no browsing, no independent hash verification. Author `test-results.json` (98 passed), `acceptance-results.json` (3 profiles), and `benchmark-results.json` are supplied evidence only. `review.json` / `review.md` remain pending bookkeeping, not acceptance. Research assurance remains reviewable-draft. This verdict does not authorize publication.

## Issue dispositions

**H1 — intake-only attested completion: CLOSED**

R3 allowed an intake-only writer, after an attester opened a `source-snapshot` / `visibilityCovered` round, to admit a new terminal page and error-free-seal it to `complete=true`.

R4 rechecks current `attest-coverage` at:
- `round-open` (already R3) when `consistency=='source-snapshot'` or `visibilityCovered`;
- first admission of a new `terminal` page on such a round (`apply` `commit` path, after exact-retry short-circuit);
- `round-seal` when `errors` is empty on such a round.

Intake-only still may supply nonterminal pages and may seal with nonempty error evidence (`complete` forced false). Exact retry of an already-committed terminal batch still returns the original ack under intake and does not re-evaluate attestation. Orphan close remains: explicit intake grant plus nonempty errors; admin still has no implicit intake.

Covering tests in the patch: `test_intake_only_cannot_complete_attested_snapshot`, `test_revoked_attester_cannot_terminally_commit_or_successfully_seal`, `test_visibility_attestation_gate_applies_to_best_effort_too`, `test_attested_multi_page_intake_then_authorized_completion`. No remaining intake-only path to `complete=true` on an attested round was constructed from the patched reducer.

**M1 — nondeterministic availability: CLOSED**

R3 `assess_rounds` collected intervening availability from matching `scopeId` only and took list tail order (`unavailable[-1]`), which followed dictionary iteration of `state['batches']`.

R4 filters `scopeId` **and** `purpose`, then selects `max(..., key=lambda p: (p['sequence'], p['ordinal']))`. Other-purpose deletions no longer suppress absence. Encode/import roundtrip is asserted to preserve the chosen operation (`inaccessible` over earlier `source-deleted` / `removed-from-scope` in the new test).

**Cross-scope pins / ID collisions: CLOSED as documented disclosure**

`mapping_outcome` now requires `definition.scopeId ==` intake scope. A second filter-scope with the same qualified lineage is `unmapped`, not an inherited pin. `test_source_kind_change_cannot_reuse_mapping` was updated from `active-pin-suspended` to `unmapped`. The kind-mismatch branch is now tautological (same scope) and harmless.

Activation: another scope already holding an active lineage+purpose yields `DENIED`; a same-scope duplicate active claim is still `Invalid`. Mapping or round ID reuse across scope/purpose yields `DENIED` before the identity `require`. A governance move requires current map rights in both scopes: retract the old claim, activate a separately proposed new one. Historical pins stay on the receiving-scope mapping that existed at admission.

Global mapping/round identifiers and active-lineage reservations can still reveal unavailability versus a fresh successful proposal. Receipt IDs still expose register-wide sequence. That is disclosed in `adoption-limits.md` / `model-spec.md`, not eliminated.

## Other R4 interactions with unchanged baseline

Capacity is a deliberate withdrawal, not a silent shrink: `MAX_EVENTS=128`, `MAX_BYTES=512KiB`, `MAX_TRANSPORT_BYTES=8MiB`, `MAX_CONFLICTS=32`, `MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH=4`, native schema `maxItems` 128. R3 2000-event / 8 MiB candidate caps are withdrawn. Full-history replay and per-event full-state digests remain; work can be quadratic under the writer lock.

`decode` enforces raw transport size first; `encode` still enforces canonical 512 KiB. Pretty-printed or ASCII-escaped JSON larger than canonical may import if under 8 MiB. Deep `RecursionError` becomes `Invalid('nesting too deep')` and `inspect_import` returns a structured `LossReport`. An interrupted 0-byte bootstrap file is refused on open, not overwritten (`open('xb')` → `FileExistsError`); host picks a new path.

AI dataset scope now uses `urn:synthetic:scheme:dataset-key` in `fixtures.py` and `examples/ai-team.json`. Example archives, `acceptance-results.json`, and reported `buildId` `sha256:b782bbca6c4b5bcc9344dde998d88486c1635ce45a00fbcf6bb7bb179af25cd6` are author-updated together; those hashes were not recomputed here.

`environment-report.json` records CPython 3.12.14, SQLite 3.53.1, and dependency versions on Windows. `requirements.txt` still pins only `jsonschema==4.26.0`. Recording a version is not pinning executable bytes.

`acceptance.py` is unchanged. Synthetic `publicationStatus: published` remains installation metadata, not production publication.

Control/surrogate checks moved to compiled regexes; classification is equivalent to R3’s per-character loops.

Unchanged and still sound from R3: buildId binding, per-event `outcomeDigest`, compact conflicts, scoped occurrence correction, admin without implicit intake/map/read, non-resumable archives, conservation, closed-epoch COMMIT refusal.

## Required changes

None required for ACCEPT WITH LIMITS.

Optional, not conditions of this verdict:
- State in release review that shipped `sync.schema.json` identity versus `build_schema.py` was checked in the author’s tree, because this conversation cannot reconstruct those exact bytes from the minified R3 body plus the pretty-printed hunk.
- Note that `mapping_outcome`’s source-kind inequality is now dead after the same-scope filter.

## Missing meaningful tests

Residuals only:
- Exact retry of a committed terminal page after attest-coverage revocation (allowed by spec; untested).
- Map grant present in only one of two scopes during a stewardship move.
- Round predecessor purpose mismatch (predecessor check remains scope-only).
- Live SQLite `busy` distinguished from `DENIED` (documented as a host operational error).

Several R3 gaps are now covered in the patch: multi-page attested completion, `removed-from-scope` / `inaccessible` ordering, grant exclusive end, month=13, source-nonreuse + steward spoof, native `/` registerId, empty bootstrap, deep import, generator-vs-shipped identity (in the author’s tree).

## Residual adoption limits

Host duties unchanged in kind: authenticate actors; verify source/steward declarations; supply current catalogue/policy/clock; keep the evidence store; prove current owned SQLite; wrap privileged `archive` / `assess_rounds` / `historical_cut` / `native_*` (the native helpers still take no actor); classify secrets that look like identifiers; allocate collision-resistant mapping/round IDs; coordinate dual-scope stewardship for moves; reserve budget for attested closure.

Deferred: live connectors, IAM, distributed exactly-once, writable resume, quarantine resolution, EFA/EAP adapters, partitioned streams, production-scale indexing, universal bitemporal remapping, cross-register comparison, power-loss/lying-hardware certification.

Hard reference budgets are now 128 events, 512 KiB canonical archive, 8 MiB raw transport, 32/4 compact conflicts. One author near-limit run reports 128 events, 517105 canonical bytes (98.63%), archive ~1.411s, receipt ~1.374s, two-process exact-retry ~3.914s, zero busy timeouts in that run. That is not an SLA, statistical benchmark, or certification of the withdrawn 2000/8MiB envelope. SQLite busy/lock errors can still occur and are not authorization refusals.

Hashes pin installed source+schema bytes and journal self-consistency. They do not prove source authenticity, secret safety, or latest-owned-store continuity. Original R3 stores need their original code/schema; there is no migration.

Delta/static/no-tools scope: this verdict is an independent reading of the 30 R3 bodies plus the supplied R4 diffs and added files. It is not a rerun of tests, native composition, or the benchmark, and it does not inspect the eight hash-only files or external toolchain.