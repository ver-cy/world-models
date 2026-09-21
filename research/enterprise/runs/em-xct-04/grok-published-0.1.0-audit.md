# Frozen independent static implementation audit — EM-XCT-04 0.1.0

**Verdict: ACCEPT**

Reviewable-draft companion. The supplied Python reference, closed schema, synthetic tests, native snapshot adapter, and adoption docs are consistent with the bounded trusted-host contract. Declared non-goals are absent and are not treated as defects. No high- or medium-severity implementation defect was found that falsifies I01–I16 against that contract.

This is a no-tools paper audit of transport-concatenated text. Hashes are identifying declarations only. Tests, digests, upstream bytes, the live URL, and the native production engine were not executed or verified.

---

## Files actually read

Assembled from parts 1–4. No other file is in the supplied corpus.

| File | Completeness |
|---|---|
| `temporal.py` | Complete (part 1) |
| `test_temporal.py` | Complete (part 1) |
| `temporal.schema.json` | Complete after join. Part 1 cut inside `$defs.ledger.scope.properties.predicate` after `maxLength: 512`. Part 2 resumes at the closing `}` and `"context"`. |
| `model-spec.md` | Complete (part 2) |
| `spec.json` | Complete after join. Part 2 cut mid-word in the embedded `contract` string (`"version or"`). Part 3 resumes `"der never proves compatibility"`. |
| `AGENTS.md` | Complete (part 3) |
| `acceptance.py` | Complete after join. Part 3 cut mid-statement `skill`. Part 4 resumes `=Path(skill).resolve()`. |
| `whole-object-coverage.yaml` | Complete (part 4) |
| `mastership-and-rights.yaml` | Complete (part 4) |
| `requirements.txt` | Complete (part 4) |
| `runtime-model.reference.json` | Complete (part 4) |
| `adoption-limits.md` | Complete (part 4) |
| `migration.md` | Complete (part 4) |
| `bindings/native-v3.md` | Complete (part 4) |
| `crosswalk.json` | Complete (part 4) |
| `tool-pins.json` | Complete (part 4) |
| `host-integration-notes.md` | Complete (part 4) |
| `audit-supplement.py` | Complete (part 4) |
| `audit-supplement-results.json` | Complete (part 4) |

**Not supplied / not reviewed:** composer tree, skill tree, `upstream/` WM bodies, live `https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/`, native V3 engine, `test-results.json`.

Transport join points were reconstructed on paper. The assembled schema, spec.json, and acceptance.py look structurally complete. They were not independently JSON-parsed.

---

## Contract check (required topics)

### Loss of scope — matches I01

`matching()` (`temporal.py`) requires exact equality of `dimension`, `timeline`, and `scope` against current config. Each commit stores `scopeDigest = digest(header without commits)`; `validate_ledger` rejects a transplanted chain (`History transplanted to another scope/header`). `validate_extension` rejects any header change. `empty()` copies scope by `deepcopy`.

Witness: `test_transplanted_history_rejected`, `test_scope_mismatch`, `test_scope_gate_before_history_diagnostics`, `test_three_profiles`.

This is consistency against a trusted predecessor, not authentication. Docs say so.

### Wrong historical answers — matches I03, I05, I14, I15

`resolve()` selects the last commit with `recordedAt <= knownAt` and, if supplied, `sequence <= knownSequence`, then the first segment covering `validAt`. `sourceRecordedAt` never chooses knowledge order. Pre-receipt and uncovered valid-time produce distinct `missing` strings. Empty snapshot and gaps return `insufficient-context`, not false. `truth` / `domainValidation` / `transitionLegality` are hard-coded unevaluated.

Witnesses: `test_bitemporal_as_known` vs `test_bitemporal_corrected`; `test_source_time_does_not_backdate_receipt`; `test_same_second_sequence`; `test_zero_sequence_cut`; `test_gap_unknown`; `test_empty_snapshot_is_not_false`; `test_no_implicit_truth_or_transition`.

Instant-only cutoffs include every commit in that second; a later same-second commit can change the answer. Spec requires pinning the returned commit sequence. That is specified behavior, not a wrong-answer bug.

### Half-open valid intervals — matches I04

`segments()`: `validFrom < validTo` when `validTo` is not null; previous `validTo` must be non-null and `<=` next `validFrom` (open interval must be last; adjacent legal).  
`resolve()`: `validFrom <= validAt and (validTo is None or validAt < validTo)` → `[validFrom, validTo)`.

Witnesses: `test_exact_half_open_boundary`, `test_before_correction_boundary`, `test_open_interval_not_last`, `test_zero_interval`, `test_reverse_interval`, `test_overlap`. Config window is the same half-open shape: `validFrom <= now < validUntil`.

### Record-time ordering — matches I03

`validate_ledger`: contiguous `sequence == i`; `recordedAt <= now`; non-decreasing `recordedAt`; `sourceRecordedAt <= recordedAt` when present; genesis operation must be `record`. `admit()` stamps `recordedAt=now` and `writer=actor`. Caller-supplied receipt fields on the request are extra keys and fail the closed schema (`test_forged_receipt_request_rejected`).

String comparison is safe only because `instant()` admits exactly `YYYY-MM-DDTHH:MM:SSZ` after `strptime` calendar check. That matches the spec’s “never round or infer zone” rule.

### Idempotency and concurrency — matches I07, I08

`admit()` checks current writer, then scans keys **before** expected-head and archive guards. Same key + `encode(request)` equal + stored `writer == actor` returns `deepcopy(ledger)` unchanged, including after the head moved and after archive. Different request or writer → `Conflicting replay`. New writes require `expectedHead == digest(last commit)`. Reused revision fails on the post-append `validate_ledger` pass.

The function is pure. Durable serialization, latest-root selection, and the restricted conflict artifact are host duties (`model-spec.md` Writes section; `AGENTS.md`). Not library defects.

### Migration / state pins — matches I10, I12, I16

`configuration()`: `(id, version) → digest` stable across `acceptedSchemas` and state profiles; unique `(profile, axis)`; no duplicate codes. `validate_ledger`: value `(id, revision)` and binding `(id, version)` stable across the whole history. `segments(..., config, retained)`: exact `encode(s)` in the preceding snapshot may keep retired pins; a new or resegmented interval is a new use.

`migrate()` accepts only `target == '0.1.0'` and returns `json.loads(encode(ledger))`. Other versions refuse. There is no in-place rewrite path.

Witnesses: `test_binding_repoint_in_history`, `test_payload_revision_repoint`, `test_new_schema_version_does_not_rewrite_old`, `test_retained_segments_after_pin_retirement`, `test_changed_interval_is_new_use_of_retired_pin`, `test_archive_after_schema_retirement`, `test_lossless_roundtrip`, `test_downgrade_rejected`.

### Current authorization boundaries — matches I09

Current config only: one writer, current readers and purposes, current half-open policy window. Historical writer attribution is stored and not re-authenticated (`validate_ledger` docstring). Current read rights apply to old history. No partial redaction. That is the declared boundary, not IAM.

### Denial diagnostics — matches I09

`resolve()`: `configuration(config, now)` → reader/purpose else `Read denied` → `matching` → `validate_ledger` → query instants.  
`admit()`: `configuration` → `actor == writer` else `Write denied` → `matching` → `validate_ledger` → `shape(request)`.

Witness: outsider + ledger `{'secret':'invalid'}` + `validAt='bad'` → `Read denied` (`test_denied_read_before_diagnostics`). Denied is never an unknown-fact answer.

Specified exception: configuration errors precede the gate (e.g. expired policy → `Current configuration unavailable`). Spec and `AGENTS.md` require the host to convert those to generic endpoint errors and to withhold the full ledger / detailed `Invalid` from write-only callers. **Host duty, not a library bug.**

### Malformed native imports / snapshot prefix — matches I06, I13

`snapshot_envelope()` is independent of the predecessor: required keys, path `temporal.timeline.snapshot`, inner `validate_ledger`, dimension and timeline-subject match, `status=='asserted'` / `unit is None` / `validTo is None`, `validFrom==recordedAt<=now`, last inner receipt `<=` outer receipt, `snapshotDigest==digest(ledger)`.

`validate_snapshot()` additionally requires a trusted previous (external): genesis has no predecessor; otherwise both envelopes are checked, storage time is non-decreasing, `factId` differs and `supersedes==[previous.factId]`, `previousSnapshotDigest==digest(previous['value'])`, then `validate_extension`.

`validate_extension` requires identical headers and an exact commit-prefix (`History rewritten/truncated`). Equal-length successor (same inner ledger, new fact) is an allowed no-op extension; notes say the host should avoid duplicate storage facts.

Host receipt and native storage time stay distinct. Acceptance text and `test_snapshot_later_native_storage_does_not_rewrite_host_time` encode later native storage of a pre-existing inner history. Synthetic January/February inner receipts do not claim the Dimension existed then.

Paper witnesses that fail closed: rehashed truncated successor → `History rewritten/truncated`; future outer receipt as current or previous → `Invalid snapshot receipt envelope`; outer before inner tip → `Snapshot precedes inner receipt`; wrong dimension/path/subject/digest/predecessor. `audit-supplement.py` constructs the truncated-prefix and forward-envelope cases; `audit-supplement-results.json` is an unverified declaration, not execution proof.

Delegated: if the host passes a non-latest ancestor **and** the successor envelope is rewritten to that ancestor, `validate_extension(ancestor, current)` can pass. Spec: trusted previous selection is external; validators cannot detect an omitted newer root.

### Bounded input limits

`shape()`: `len(encode(x)) <= 8 MiB`, then Draft 2020-12 `$defs[kind]`, then `walk()` for instants, integer `sequence`, digest grammar, version grammar. Schema caps: 1000 commits, `sequence` 1..1000, 100 segments, URI/reason/code lengths, 100 readers/purposes/pins. Overflow refuses; no truncation. At 1000 commits even archive is refused — documented; no reserved archive slot.

Raw request-size limits before parse, and duplicate-key rejection in the input parser, are host duties. `load()` is the trusted-fixture loader.

### Unresolved product claims

The package does **not** claim parent subtype, ISO/SCXML/OWL-Time conformance, source truth, transition legality, payload validation, signatures, clock attestation, IAM, erasure, or existing-Dimension migration.

Aggressive **declarations** that this audit does not treat as proven:

- `crosswalk.json` `liveByteEqualityVerified: true` for WM-XCT-009/021/022 — parent bytes are not in this corpus.
- `acceptance.py` sets `publicationStatus: 'published'` on synthetic releases while `researchAssurance` remains `reviewable-draft`.
- Catalogue “native installation checks” refers to the harness existing, not to a verified production engine run.

`spec.json` `runtimeImports` is empty; semantic references are `selected-pattern-alignment-not-subtype`. `crosswalk.json` claim text is `narrower/overlap, never exactMatch or subtype`. That matches the code boundary.

### Forward clock / poisoned history — adequately bounded as host duty

Detection is fail-closed and has no repair API:

- Inner: `recordedAt <= now` and non-decreasing, on every `validate_ledger` path (`admit`, `resolve`, `migrate`, `snapshot_envelope`).
- Outer: `recordedAt <= now`; successor `recordedAt >= previous.recordedAt`.
- `migrate` cannot strip or rewrite receipts.
- `validate_extension` rejects truncation and prefix rewrite.

Witness: `test_forward_clock_excursion_needs_external_recovery` — admit at `2026-12-31T00:00:00Z`, then read/write at `NOW` → `Future receipt`.

Not implemented, and documented as not implemented: skew guard against an independent reference; quarantine primitive; governed new-timeline identity; catch-up helper. `host-integration-notes.md` correctly widens the guard to **every** `now`-taking call (reads and snapshot validation included). A forward `now` can accept a future cutoff or future-valid policy; a backward `now` can create a read outage. That is why the host must wrap the clock.

A poisoned immutable history cannot be silently repaired. Recovery is catch-up under current policy or a separately governed new identity that discloses continuity loss. That is the bound the contract promises. Missing recovery API is a declared non-goal, not a defect.

---

## Severity-ranked findings

No High or Medium implementation defects against the stated contract.

### Low — implementation nits (optional 0.1.1; not REVISE-forcing)

**L1. Native envelope is presence-typed, not closed.**  
Anchor: `snapshot_envelope()` in `temporal.py`. Required-key `all(k in fact)` only; extra keys pass; `factId` / `supersedes` types are not locally checked.  
Classification: delegated if native V3 already validated the outer fact (`bindings/native-v3.md`, I13). Residual only if `validate_snapshot` is called standalone.  
Minimal repair: closed-field + URI/array type checks on the envelope in a new version.

**L2. `empty(config)` can raise `KeyError` rather than `Invalid`.**  
Anchor: `empty()` vs `configuration()`. Public helper assumes a shaped config.  
Minimal repair: call `configuration` (needs `now`) or raise `Invalid` on missing keys.

**L3. Scheme-bearing URI is format-mediated.**  
Anchor: `temporal.schema.json` `format: uri` + `minLength` 3..512; `shape()` requires a `uri` format checker; `walk()` has no scheme regex. Spec prose requires scheme-bearing RFC 3986.  
Classification: residual on `rfc3986-validator==0.1.1` (unverified here). Missing checker fail-closes.  
Minimal repair: local scheme-before-`:` check if that guarantee must not depend on the plugin.

**L4. Duplicate schema surfaces.**  
Anchor: root schema in `temporal.schema.json` vs `$defs.ledger`; `shape()` uses `$defs` only. Inlined segment/binding copies rather than `$ref`. `spec.json` `contract` duplicates `model-spec.md`.  
Minimal repair: root `$ref: #/$defs/ledger`; `$ref` shared defs.

**L5. Conflated snapshot receipt diagnostic.**  
Anchor: `snapshot_envelope()` — `validFrom != recordedAt` and `recordedAt > now` share `Invalid snapshot receipt envelope`. Cosmetic.

**L6. Test-name imprecision.**  
Anchor: `test_admission_rejects_input_ahead_of_host_clock` — rejects existing T1 receipt vs `now=2026-01-09`, not the new request body vs clock. Behavior is still correct.

### Informational — declared trusted-host duties (not defects)

**I1.** Clock authenticity, skew bound on every `now`-taking call, quarantine/freeze, governed new identity after poison, latest-root selection, durable serialized persistence, duplicate-key / pre-parse size limits, write-only response wrapping, genericizing configuration errors, native closed envelope + global fact-id uniqueness, conflict artifact store, retention/erasure, existing-Dimension migration. Documented in `model-spec.md`, `AGENTS.md`, `adoption-limits.md`, `migration.md`, `bindings/native-v3.md`, `host-integration-notes.md`.

**I2.** `crosswalk.json` `liveByteEqualityVerified`, `tool-pins.json` composer/skill/upstream hashes, `acceptance.py` `publicationStatus: published`, `audit-supplement-results.json` passed/digest — identifying declarations, not verified in this audit.

**I3.** `model-spec.md` states the skew guard “before every admission”; `host-integration-notes.md` expands it to every `now`-taking call. Align the spec sentence in a doc-only revision.

---

## Guarantees vs code

I01–I16 as written in `model-spec.md` are implemented in `temporal.py` for the library’s slice. Host-owned pieces named in the same spec are not silently implemented. The code does not invent signatures, anti-rollback storage, origin authenticity, domain truth, transition legality, or a security boundary.

Native V3 fixture validation in `acceptance.py` is representative binding evidence only. It is not a claimed deployed-engine integration.

---

## Scope and limits of this no-tools static audit

- Corpus: the nineteen files listed above, reconstructed from four transport parts. Join points noted. No other file was read.
- Not done: execution of `test_temporal.py`, `acceptance.py`, or `audit-supplement.py`; recomputation of any SHA-256; JSON Schema meta-validation; audit of `jsonschema` / `rfc3986-validator` / `rfc3339-validator` behavior beyond what the source requires; fetch of `https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/`; inspection of composer, skill, or upstream WM bytes; verification of the native production engine.
- `audit-supplement-results.json` and pin files were treated as untrusted declarations.
- Adversarial witnesses are paper constructions from the supplied source and tests, not runtime traces.
- Previous reviewers’ opinions were not supplied and were not used. `host-integration-notes.md` was read as part of the frozen corpus, not as an external verdict.
- Publication authority: none. This ACCEPT is an implementation-vs-stated-contract judgment on a reviewable draft. Findings that need code changes require a new version; the immutable 0.1.0 text should not be overwritten.

**ACCEPT.** Residual work is host integration and optional low-severity hygiene in a later version, not a correctness failure of the frozen 0.1.0 reference.