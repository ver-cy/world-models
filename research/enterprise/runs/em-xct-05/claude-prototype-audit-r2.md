# EM-XCT-05 `0.0.0-prototype.2`: independent frozen review (no tools)

**Verdict: REVISE (narrow).** The core applicability logic fails closed on every path I traced, and I found no route to `applicable-review` that bypasses pinning, authority, window or completeness checks. The verdict is REVISE, not ACCEPT WITH LIMITS, because two README claims are contradicted by the code (D1, D2). Both fixes are small. With D1–D3 fixed or explicitly disclosed, I would expect ACCEPT WITH LIMITS for this research scope. This review does not authorize publication and makes no native V3 or production claim.

## Files read and truncation

I read all 8 supplied files in full: `README.md`, `disclosure.py`, `disclosure.schema.json`, `test_disclosure.py`, `test-results.json`, and `examples/startup.json`, `matrix.json` and `ai.json`. None was truncated; every `<file>` block closes normally.

I could not recompute any SHA-256. I checked only that the header hashes match `test-results.json` `inputHashes` textually, and they do for all four inputs. The example files are outputs and are not hashed in the report. I counted 78 `test_*` methods, which matches `testsRun: 78`. Test results are Codex-reported, not executed by me.

## Defects

### D1 (medium): segregation silently discards the author's own objections
**Anchor:** `disclosure.py:inspect`, the `elif snapshot['separateReviewer'] and rb['reviewer']==b['author']` branch.

The self-review exclusion applies to every verdict, not only `cleared`.

**Witness** (profile with `separateReviewer=True`):
- R1: reviewer is the author, verdict `rejected`, authorized and in window.
- R2: another reviewer, verdict `cleared`.
- Result: `applicable-review`, with R1 listed under `ignored` and reason `self-review`.

Segregation of duties exists to prevent self-approval, not self-objection. The README says negatives stop contributing only "outside their declared windows or current authority". Self-authorship is neither, so this is undisclosed suppression.

**Minimal fix:** apply the exclusion only when `rb['verdict']=='cleared'`, so a self-rejection or self-inconclusive verdict counts and yields `conflict`. Alternatively, disclose it as a deliberate profile choice. Add a test either way.

### D2 (medium): snapshot validation is incomplete and happens after early returns
**Anchor:** `disclosure.py:inspect`, the nested `pins()` function and the ordering of the `result()` early returns.

There are three problems:

1. **Pin sets are not full-string checked.** `pins()` checks only the JSON Schema `$defs/pin`. Under jsonschema's Python `re.search`, `$` also matches before a trailing `\n`. The reported pass of `test_newline_field_alias` with message `exact identifier syntax`, rather than `record shape`, confirms the schema accepts such values.
   - **Witness:** `withdrawnReviews=[{id:'urn:synthetic:review:startup\n', revision:'1', digest:<same>}]` with the real pin still in `activeReviews`.
   - The overlap check passes, the answer is `applicable-review`, and it echoes the alias.
   - The disjointness invariant is meant to catch exactly this host mistake (withdrawn but not removed from active), and the alias evades it.
   - This contradicts the README claim "Code uses full-string matching in addition to JSON Schema patterns".
2. **Malformed snapshot data can appear in a well-formed answer.** `activeReviews`, `withdrawnReviews` and `authority` are not validated before the `stale` and `insufficient-context` early returns.
   - **Witness:** `withdrawnReviews="garbage"` plus a proposal-pin mismatch returns `{'status':'stale', …, 'withdrawn':'garbage'}` instead of raising `Invalid`.
   - A malformed `authority` makes every review fall into `ignored` with reason `authority`. That fails closed but is misdiagnosed.
3. **Snapshot invariants are checked only on supplied reviews, or too narrowly.**
   - "One active revision per identity" is checked only on the supplied reviews. If the snapshot has two revisions of one ID active but only one is supplied, the result is `review-set-incomplete`, not an invalid-snapshot error.
   - Overlap is compared by full canonical pin. The same `(id, revision)` with different digests in the active and withdrawn sets goes undetected.

**Minimal fix:** immediately after `authorize`, validate the whole snapshot with a closed `snapshot` `$def` plus the same full-match identifier walk used in `validate`. Check that active IDs are unique and that overlap is empty on `(id, revision)`. Only then take the early returns.

### D3 (low–medium, claim gap): `now` is caller-asserted and not bound to snapshot time
**Anchor:** `disclosure.py:inspect`, the `now` parameter and `result()['at']`.

**Witness:** evaluate today's snapshot with `now` set to last week. The review windows are judged at last week, but authority is judged by today's catalog. The answer then pins `at` from one time and `snapshotDigest` from another, which is incoherent as a historical answer.

The README presents `at` as "evaluation time" but never says it must come from a trusted clock or match the snapshot's as-of time.

**Minimal fix:** add `asOf` to the snapshot and require `now == asOf`. Alternatively, state this explicitly as a trusted-host duty.

### D4 (low): the canonical encoding cannot be reproduced outside Python
**Anchor:** `disclosure.py:canonical`, the README's "Identity" section and the schema's `residualRisk`.

The digest depends on `json.dumps` escape behaviour, which the README does not specify:
- `\u00XX` with lowercase hex for C0 controls;
- short escapes such as `\n` and `\t`;
- DEL, U+2028 and U+2029 emitted raw;
- key order by code point.

`residualRisk` accepts any of these characters. A native V3 or other reimplementation can therefore compute a different digest for the same record. This matters for migration.

**Fix:** specify the escaping rules, or restrict `residualRisk` to a printable character set. Add golden vectors that contain a control character and U+2028.

### D5 (low): unreachable check, and a test that does not hit it
**Anchor:** `disclosure.py:validate`, the `'conflicting binding pin'` branch.

The branch cannot be reached:
- Same ID with a different revision or digest is caught first by `incoherent reference pin`.
- Identical pins are caught first by schema `uniqueItems`.

`test_same_binding_revision_conflict` asserts only `Invalid`, so it actually exercises the coherence check. **Fix:** remove the branch or rename it, and make the test assert the message.

### D6 (low): the import cap conflicts with the "complete master set" contract
**Anchor:** `disclosure.py:import_records`, `len(existing)+len(incoming)>128`.

Internal pin resolution needs the complete local set, but that set can never exceed 128 records. Splitting it breaks resolution.

The README lists 128 as a generic list/object bound. It does not list this 128-record store cap, the 64-review limit or the 64-pin limits. **Fix:** document all of these caps as prototype limits.

### D7 (low, hardening): container subclasses are accepted
**Anchor:** `disclosure.py:canonical`, the `isinstance(x,str|list|dict)` checks.

`int` is checked with `type(...) is`, but `str`, `list` and `dict` subclasses pass.

**Witness:** an in-process `str` subclass as `reviewer` that serializes as `urn:evil:x`, so its digest is correct, but whose `__eq__` returns True against catalog entries. It passes `rb['reviewer'] in snapshot['reviewers']`.

The README does say dictionary APIs are not wire parsers, so this falls partly under host duty. The fix is still one line: use `type(x) is` for all JSON types.

### D8 (low): version and report hygiene
- `VERSION` is not tied to the schema's `const`, so the two can drift. **Fix:** assert they are equal when the module loads.
- `test_disclosure.py` writes the report before the examples, and records no hashes for the examples. **Fix:** write the report last and include example hashes.

### D9 (trivial)
`seal()` on a non-dict raises `AttributeError` rather than `Invalid`, because `hash_body` runs before `validate`.

## Misleading or overbroad claims

- **"Metadata-only":** `residualRisk` holds up to 2048 characters of free text. Real reviewers will describe the risk, which can quote source values. That text is immutable: a correction preserves the old revision permanently. This is a retention boundary the README should name. Author and reviewer IDs are also personal data.
- **Diagnostics visibility:** the `stale` and `proposal-author` early returns never evaluate reviews. An active rejection is therefore absent from `counted` and `ignored`. The README's visibility claim is scoped to the clearance case; say so explicitly.
- **Acyclicity:** the README presents acyclic supersession as a validated property. In practice, digest pinning makes cycles computationally infeasible, so the cycle loop is defensive and untestable. That is not a defect, but acyclicity should not be counted as tested behaviour.
- **Supersession forks:** two reviews may supersede the same target, and supersession may cross proposal revisions under the same identity. Both are consistent with the README's "implement or precisely defer" item, but they are currently unspecified.
- **Self-reference:** a proposal can pin its own ID, for example as `priorReleases`. This is harmless but unchecked.

## Verified as behaving as claimed (by reading)

- Authorization precedes record inspection, and `Unauthorized('unavailable')` is uniform.
- The digest covers the whole record minus the top-level `digest`, with domain separation provided by the closed key sets.
- Review sets must equal the active set exactly: nothing can be omitted or added, and duplicates are refused.
- Validity is the half-open window `[validFrom, validTo)`, with `capturedAt ≤ reviewedAt ≤ validFrom` enforced.
- Different eligible verdicts produce `conflict`, and expiry never grants clearance.
- Import is transactional: `existing` is deep-copied and never mutated.
- Re-importing the same revision and digest is idempotent, a conflicting revision fails, and an identity cannot change type.
- `load` rejects duplicate keys (including after unescaping), floats, NaN and Infinity, oversized integers, lone surrogates and invalid UTF-8.
- `prototype.1` is refused, and there is no implicit migration.

## Trusted-host duties (declared; not defects)

- Authenticating and authorizing callers; the capability dict is an assertion, not a credential.
- Snapshot truth and completeness, including that external pins resolve, that fields are scalar top-level leaves, and custody and hold state.
- Binding actor strings to distinct people.
- Compare-and-swap persistence and write-role checks.
- Uniform refusal and timing protection.
- Preserving snapshots so historical answers can be reproduced.
- Recording withdrawal provenance. Withdrawal exists only as snapshot state, not as an immutable record.
- Once D3 is addressed, supplying `now` from a trusted clock.

## Missing tests to add with the fixes

- Self-rejection under segregation (D1).
- A newline alias in `withdrawnReviews`, and malformed snapshot sets with early returns (D2).
- Two active revisions in the snapshot while only one is supplied.
- Golden digest vectors containing control characters and U+2028 (D4).
- Supersession forks and supersession across proposal revisions.
