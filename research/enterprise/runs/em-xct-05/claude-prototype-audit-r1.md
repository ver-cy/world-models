# EM-XCT-05 metadata-only prototype: frozen review

## Verdict: REVISE

The README is mostly candid about its limits, and most of what it says is local behavior is implemented. The problem is a small number of real code defects that contradict invariants the README states: duplicate-field rejection, byte-exact identity, and authorization before diagnostics. There are also a few gaps where a cheap local check is missing. None of this needs a redesign. With fixes R1–R7 below, I would expect **ACCEPT WITH LIMITS** for this declared prototype scope. This is not an authorization to publish and not a claim of native V3 or production fitness.

## Scope of what I read

- **Files read, in full, with no truncation seen:**
  - `README.md`
  - `disclosure.py`
  - `disclosure.schema.json`
  - `test_disclosure.py`
  - `test-results.json`
  - `examples/startup.json`, `examples/matrix.json`, `examples/ai.json`
- **Hashes are not verified.** I computed no SHA-256 values. The only check was internal: `test-results.json` `codeSha256` equals the header hash given for `disclosure.py`.
- **Tests were not run.** The 51-test pass is reported Codex evidence. I did count the 51 test methods, and the count matches the report.
- **No prior-study context was used.** I judged only the bytes supplied here.

---

## Defects

### D1. Python `$` accepts a trailing newline, which breaks identity and the duplicate-field check (medium)

**Anchor:** `disclosure.schema.json`, every `pattern` that ends in `$` (`pin.id`, `author`, `reviewer`, `dimension`, record `id`, `field.name`, `digest`). The schema is enforced through `jsonschema`, which uses `re.search`.

In Python `re`, `$` also matches just before a final `\n`. `[^\s]+` stops before the newline, and `$` still matches there.

**Witnesses:**
- **Duplicate field accepted.** `fields: [{"name":"name",…},{"name":"name\n",…}]` passes the schema. The `validate()` duplicate check sees two distinct names, so both are accepted. The README states "duplicate field" rejection and "named top-level scalar fields"; this contradicts both.
- **Alias identities.** `id: "urn:synthetic:proposal:startup\n"` is a different record identity that renders identically. In `import_records()` the key `(type,id,revision)` treats it as new, and the `types` map can give the alias a different type.
- **Other invisible aliases.** `[^\s]` in Python admits U+200B, U+202E, U+0000 and similar characters. `"urn:x:founder\u200b"` differs from `"urn:x:founder"`, so under a host catalog containing that alias, the `separateReviewer` equality in `inspect()` is bypassed.
- **Cross-dialect drift.** ECMA-262 `\s` and `$` differ from Python's. For example, U+FEFF is `\s` in JS and not in Python. A future non-Python validator would therefore accept a different language, which matters directly for "native V3 binding".

**Minimal fix:**
- Restrict identity-bearing strings to ASCII, e.g. `^[A-Za-z][A-Za-z0-9+.-]*:[!-~]+$`.
- In `validate()`, add a code-side `re.fullmatch` (or reject any string ending in `\n`) for `id`, `dimension`, `author`, `reviewer`, `field.name` and every pin's `id`/`digest`.
- Add tests for `"name\n"` and a zero-width alias.

### D2. `authorize()` passes when both dimensions are missing (low–medium)

**Anchor:** `disclosure.py` `inspect()` first two lines, and `authorize()`.

`dimension = snapshot.get('dimension')` gives `None` when the snapshot is not a dict or has no `dimension`. `capability.get('dimension') != None` is then false, so a capability with no `dimension` key is accepted.

**Witness:** `inspect(tampered_proposal, [], None, {'inspect': True}, now)` passes `authorize()`. It then reaches `validate(proposal)` and raises `Invalid('digest')`, or `Invalid('record shape')`, or with a valid proposal `Invalid('proposal scope')`.

This produces record-content diagnostics before any real Dimension authorization, contradicting "requires a trusted host assertion for Dimension … before inspecting record contents." `import_records(…, dimension=None, {'inspect':True,'record':True})` has the same pattern, but it fails closed later.

**Minimal fix:** in `authorize()`, require `isinstance(dimension, str) and dimension` and require `capability.get('dimension') == dimension` with the same type check. Add a test for `capability={'inspect':True}` with `snapshot=None`.

### D3. Filtered negative verdicts disappear from the result (medium; semantics)

**Anchor:** `inspect()`, the second review loop and the return statements.

Reviews that are ignored (withdrawn, authority mismatch, self-review, or outside the window) are dropped. `ignored` is returned **only** when nothing valid remains.

**Witness:** the active set is {R1 `cleared`, in window; R2 `rejected` by a currently authorized reviewer with `validTo` in the past}. The result is `{'status':'applicable-review'}`, with no trace of the rejection. The same happens when R2's author was later removed from `reviewers`. An expired *rejection* silently becomes non-objection. That conflicts with the README's claim that rejection and expiry "remain distinct".

**Minimal fix:**
- Always return `ignored` as a list of `{pin, reason}`.
- Also choose one of these, and document the choice:
  - (a) an in-authority `rejected`/`inconclusive` review in the active set blocks regardless of its window, or
  - (b) negative verdicts expire, and that is stated explicitly.

### D4. The snapshot does not bind the current proposal revision (medium)

**Anchor:** `inspect()` `required` snapshot keys.

The snapshot pins context, members and the active review set, but not *which proposal revision is current*. Proposal withdrawal or retirement is not modelled. The README's "withdrawal" covers reviews only.

**Witness:** P rev 1 is cleared. P rev 2 is issued with an identical body (for example, a correction of an out-of-band error) and the host intends rev 1 to be retired. Inspecting rev 1 against a snapshot whose `activeReviews` still lists rev 1's review returns `applicable-review`.

Related: `test_added_member_needs_new_review` reseals with the *same* `revision:'1'` and a different digest. `inspect()` never detects that immutable-revision collision. The test fails only because the review's digest pin no longer matches.

**Minimal fix:** add `snapshot['proposal']` (a pin) and require `== pin(proposal)`, returning `stale` otherwise.

### D5. The self-supersession check is effectively dead code (low; misleading)

**Anchor:** `validate()`, review branch: `b['supersedes'] == pin(record)`.

The record's digest covers `body.supersedes`, so matching it means finding a hash fixpoint. The check can never fire in practice. A review that claims to supersede its own `(id, revision)` with any other digest is accepted.

**Minimal fix:** compare `(id, revision)` only. In `inspect()`, also raise `Invalid` when an active review's `supersedes` pin is itself in the active set. That is a cheap local check, needs no graph resolution, and catches the most likely host error.

### D6. Pre-capture reviews are checked inconsistently (low)

**Anchor:** `inspect()`: `review predates proposal` sits *after* the withdrawn, authority and self-review filters.

The same bad record raises `Invalid` when it is in authority and is silently marked `ignored` when it is not.

**Minimal fix:** move the check into the first validation loop. Also add `if not set(active) .isdisjoint(withdrawn): raise Invalid('contradictory snapshot')`. Currently a pin listed in both sets is treated as withdrawn without complaint.

### D7. Reference coherence inside a proposal is not checked (low–medium)

**Anchor:** `validate()`, proposal branch.

- **Same source at two revisions.** Two members may pin the same `source.id` (or `schema.id`) at different revisions or digests: a single proposal asserting two "current" revisions of one object.
- **Same classification at two revisions.** Within one field, `classificationBindings` rejects duplicate `(id, revision)` but allows the same `id` at revisions 1 and 2 together.
- **README mismatch.** The README says "multiple distinct source objects", but duplicate sources are not rejected.

**Minimal fix:** within a proposal, require one `(revision, digest)` per referenced `id` across all pins, and bindings unique by `id`. Alternatively, reword the README to permit these cases.

### D8. Timestamp and number edge cases (low)

- **Platform-dependent timestamps.** `instant()` round-trips through `strftime('%Y')`. As I recall, CPython on glibc does not zero-pad years below 1000, while Windows pads them. If so, a record with `0999-…` validates on one platform and not the other. Please confirm this. **Fix:** build `datetime(int(…))` from regex groups, with no `strftime` round-trip.
- **Wrong exception type for huge integers.** In `load()`, an integer literal longer than 4300 digits (within the 256 KiB cap) raises a plain `ValueError` from Python's int-string limit, not `Invalid`. **Fix:** add `ValueError` to the caught tuple, or use a `parse_int` that length-checks first.

### D9. Migration: validation is locked to one version (medium for lifecycle, deferred-acceptable)

`import_records()` re-`validate()`s every **existing** record against `const` version `0.0.0-prototype.1`. The first version bump makes every stored record unmergeable. Revisions are unordered free strings (`"1"`, `"01"`, `"1 "`, `"10"` < `"2"` lexically) with no predecessor link, so "correction preserves history" gives a set of revisions, not an ordered chain.

**Minimal fix, or precise deferral:**
- dispatch validation by version and never re-validate stored records under a newer schema;
- constrain revision (e.g. `^[1-9][0-9]{0,17}$`) or add a `previousRevision` pin.

### D10. Answers are not bound to their inputs (low–medium)

The result from `inspect()` does not carry the proposal pin, a digest of the snapshot, `now`, or the review pins it counted. The README says "historical answers need preserved snapshots", but nothing ties an answer to the snapshot that produced it.

**Minimal fix:** return `{proposal: pin, snapshotDigest: sha256(canonical(snapshot)), at: now, counted: [pins], ignored: […]}`.

---

## README claims challenged

| Claim | Assessment |
|---|---|
| "duplicate field" rejected; "top-level scalar fields" | Bypassable through D1. |
| "requires a trusted host assertion for Dimension … before inspecting record contents" | False when the dimension is missing (D2). |
| "Rejection … absent/expired review … remain distinct" | Collapsed when a clearance coexists with a filtered rejection (D3). |
| "Proposals may contain multiple distinct source objects" | Distinctness is not enforced (D7). |
| "Input bounds (… 32 members, 64 fields/member)" | Not jointly reachable. 32×64 fields × 1–8 bindings × ~150 B exceeds 256 KiB, so large valid shapes fail as `size`. State the byte cap as the binding limit. |
| "JSON input rejects … invalid UTF-8" | True for `load()`, but untested. `inspect()`/`import_records()` accept Python objects and never go through `load()`, so the host must use `load()`. |
| Test report as evidence | `codeSha256` covers `disclosure.py` only. It does not cover the schema, the tests, Python, or `jsonschema`. A schema change would leave the report hash unchanged. |
| Examples | `matrix`/`ai` reuse `name-only-shape` and `name-classification` for `headcount`/`releaseNotes`, which is misleading even as synthetic data. `matrix` is itself a textbook differencing witness (group vs unit headcount) that is cleared by design. That is acceptable given the README's disclaimer, but the example's `residualRisk` should say so. |
| `trustedCapabilityExample` in serialized examples | Placing it alongside request-shaped data invites exactly the "user request field" misuse the README forbids. Move it out, or label it host-internal. |

Claims I found accurate: the half-open interval, future-capture → `stale`, `reviewedAt ≤ validFrom < validTo`, exact review-set completeness, transactional and idempotent import, type preservation, the "not JCS" disclosure, and `notServingAuthorization=true`.

## Trusted-host duties (not defects, as the README declares)

- **Caller identity.** Authenticate the caller and build `capability`; the module cannot tell a forged assertion.
- **Trusted time.** Supply a trustworthy `now`.
- **Reviewer authenticity.** `reviewer` is self-asserted in a record anyone with write access can seal. A digest is integrity, not authenticity.
- **Complete sets.** Provide complete and correct `activeReviews`/`withdrawnReviews`, and remove superseded reviews.
- **Resolve every opaque pin.** This covers source, schema, shape, classification, authority, custody and prior releases, plus attesting scalar and top-level status.
- **Actor catalogs.** Keep them free of aliases (see D1 for the code-side part).
- **Persistence.** Handle persistence, compare-and-swap, writer role checks, and dangling-reference checks at write time.
- **Serving and retention.** Handle uniform refusal, timing and existence protection, retention, disposition and serving.
- **Operational consequence to document.** A single `authority` pin means any authority revision invalidates *all* prior reviews. That is by design.

## Test evidence

- **Coverage that matches the README.** Profiles, drift, windows, conflict, incompleteness, import and JSON hygiene.
- **Weak assertions.** Many tests use bare `assertRaises(d.Invalid)` and would pass for the wrong reason. `test_added_member…`, `test_added_field…` and `test_reordered…` all actually hit `'review points to another proposal'`. Use `assertRaisesRegex`.
- **Gaps.** No tests cover:
  - D1–D6
  - invalid UTF-8
  - a pin present in both active and withdrawn
  - an active review with an out-of-window rejection alongside a clearance
  - multiple revisions of one review id in the active set
  - a snapshot that echoes the proposal (the README's own warning)

## Minimal revision set to reach ACCEPT WITH LIMITS

- **R1:** ASCII identity patterns plus code-side `fullmatch` (D1).
- **R2:** type-checked, non-empty dimension in `authorize()` (D2).
- **R3:** always return `ignored`, and make a documented decision on negative verdicts (D3).
- **R4:** `snapshot.proposal` pin (D4).
- **R5:** a real self-supersession check, an active-set supersedes check, and an active/withdrawn disjointness check (D5, D6).
- **R6:** the pre-capture check moved before the filters; pin coherence within a proposal (D6, D7).
- **R7:** the report hashes all artifacts and records tool versions; regex-matched test assertions plus tests for the items above.

D8–D10 may be precisely deferred in the README instead of fixed. This review does not cover the metamodel or publication package, which is not yet built.
