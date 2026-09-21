# Enterprise Assertion Provenance 0.1.0: Static Implementation Audit

## Verdict: **BLOCK** (narrow, remediable)

I found no critical flaw affecting safety, truth inference or disclosure:
- Truth is never evaluated.
- The reader gate runs before any diagnostic.
- Human review cannot promote an epistemic kind.
- Independence is never inferred from distinctness.
- The companion keeps its own identity.

Two problems still block acceptance:
- **F1:** A stated correction capability fails in the main dependency-change scenario.
- **F2:** Timestamp ordering can be bypassed when the format checker is not installed.

Fixing F1 and F2, or narrowing the spec text to match the code, would support ACCEPT WITH LIMITS. This review grants no publication authority. The acceptance harness's `publicationStatus:'published'` and `compatibility.decision:'accepted'` are synthetic candidate metadata, not a publication decision.

## Input completeness

- **Markers:** END OF PART 01-contract, 02-code and 03-native are present, as is `FINAL SENTINEL: AP-FROZEN-IMPLEMENTATION-20260921`.
- **Reviewed:** `model-spec.md`, `provenance.schema.json`, `provenance.py`, `test_provenance.py`, `acceptance.py`, `runtime-model.reference.json`, `AGENTS.md` and `test-results.json`.
- **Not provided, not reviewed:**
  - `spec.json` (normative tree, received as a summary only) and `tool-pins.json`
  - `upstream/` (WM-XCT-012) and `examples/*.json`
  - composer and skill code (`composition`, `bootstrap_dimension`, `write_record`, `validate_dimension`)
  - the facet, rights, migration and crosswalk documents
- **Hashes:** I could not recompute the SHA-256 values without tools. They are taken as stated.

---

## Findings, ranked by severity

### F1: High. A correction is treated as new reliance, so downstream records freeze after any upstream correction

`validate_ledger` runs `semantic()` on every `correct` row. `semantic()` then:
- resolves every ref, including immutable anchored refs such as `Activity.inputs` and `EvidenceLink.evidence`, and
- requires each ref to be the **current head** (`pin(heads[id])==p`).

The source-asserted branch also re-resolves the generating Activity's Capture inputs.

**Reproduction** (startup fixture, traced):
1. Correct the Capture: `add(g, revision(g['records'][0], integrity='mismatched'))`. This is accepted and is the same step `acceptance.py` performs.
2. Correct the Activity's notes: `add(g, revision(g['records'][1], notes=['operator note']))`. This raises `Invalid('New link to inactive or superseded revision')`. Because `inputs` is an anchor, the Activity can never be corrected again, only withdrawn.
3. Correct the account's limitations to record the mismatch: `add(g, revision(g['records'][2], limitations=[..., 'Upstream integrity mismatch']))`. This fails in the source-asserted branch (`resolve(capture r1)`).
4. Correct the EvidenceLink's rationale: this fails. `evidence` is anchored, so the link is permanently frozen.
5. Create a new source-asserted account from the existing acquisition Activity: this fails.

**Contradicted text:**
- "The record can be withdrawn or its notes corrected" (Activity).
- "Selector/rationale corrections retain versions."
- "Label/basis corrections are explicit revisions." A ConfidenceAssessment freezes once its account is corrected.
- I09: the reviewer response that I09 calls for is blocked.

The only workaround is to create a duplicate Activity (new ID, same interval, `inputs=[capture r2]`). That contradicts "a new execution gets a new ID": one execution would then carry two identities. The failure is fail-closed; no data is corrupted.

**Fix:** Apply the active/current requirement only to refs that are new or changed relative to the previous revision. Unchanged anchored refs need only exact-pin resolution. Add tests for steps 2–4.

### F2: Medium, blocking in degraded environments. Record timestamps compare raw strings and rely on an optional format checker

`instant()` checks only `now` and `knownAt`. Every record and config time is validated by:
- the schema `pattern`, which uses `re.search`, and
- `FormatChecker` `date-time`, which is silently skipped if `rfc3339-validator` is not installed.

All ordering checks compare raw strings.

- **Unicode digits:** Python's `\d` matches Unicode digits. Suppose `startedAt='2026-09-21T08:00:00Z'` and `endedAt='2026-09-21T0١:00:00Z'` (Arabic-Indic `١`, meaning 01:00). As strings, `startedAt<=endedAt` passes because `'١'` > `'8'`, and `endedAt<=recordedAt` also passes. The record is admitted even though it violates "startedAt ≤ endedAt".
- **Invalid calendar values:** Without the format checker, values like `2026-99-99T99:99:99Z` pass. `test_bad_calendar` passes only because the dependency happened to be present.
- **Trailing newline:** `$` also matches before a trailing `\n`, so the pattern accepts timestamps ending in a newline. This gives the same instant two representations with different digests. I could not determine statically whether the installed RFC 3339 validator rejects it.

**Fix:**
- Apply an ASCII-strict `instant()` (`re.fullmatch`, `[0-9]`) to every timestamp field and compare `datetime` values.
- At import, assert that `FormatChecker().checkers` contains `date-time` and `uri`, and fail closed if not.

`AGENTS.md` does declare the dependency, but the code does not enforce it.

### F3: Medium. Numbers are not canonical, and the prefix check uses Python equality rather than byte or digest equality

jsonschema treats `1.0` as an `integer`, while `encode` serializes it as `1.0`. A `revision` or pin `revision` of `1.0` therefore passes validation but produces a different digest.

**Reproduction:**
1. `cand=deepcopy(fixture()); cand['records'][3]['revision']=1.0`. This is the last row, with no dependents.
2. `validate_extension(fixture(), cand, config())` returns `True`, because `1.0==1` and the genesis check passes.
3. Yet `digest(cand['records'][3])` differs from the original digest, and `inputSliceDigest` changes.

Any externally held pin to that row, such as an envelope `snapshotDigest`, no longer matches.

Separately, pins `{revision:1}` and `{revision:1.0}` both resolve to the same target, so one reference can have two encodings. This undermines I02 and I04 exactness. `test_prefix_rewrite_and_truncation` covers truncation only, not rewriting.

**Fix:** Require `type(x) is int` for revisions, and compare prefixes by `encode()` or per-row digest.

### F4: Medium. A correction can create an identity-level self-derivation

The ai-team fixture traces as follows:
1. Create synthesis `S2` with `inputs=[pin(inference r1)]`.
2. Correct the inference: `revision(inference, activity=pin(S2))`.
3. Both steps are accepted. `activity` is not an anchor, and `S2` is an active, current synthesis.

The pin graph stays acyclic, so I08 holds literally. At the identity level, however, the account is now "generated by" an activity that consumed the same account. This is circular support. As a side effect, `closure(inference r2)` always contains `inference r1`, which is not the head, so `requiresReview` can never clear except by withdrawal.

This conflicts with "Corrections also cannot introduce self-reference". Tests cover only the unresolved-self-pin case.

**Fix:** Reject any account correction whose new `activity` closure contains the account's own ID.

### F5: Medium. The reason for a dependency change is not shown in the view

`sourceGaps` is evaluated on the **pinned** Capture revision only. After the acceptance correction (`integrity='mismatched'` on the head):
- the view reports only a generic `changedDependencies` entry (a new pin with `state:'active'`), and
- no `sourceGaps` entry appears.

The view does not return Captures, so an authorized reader cannot see that the current head is integrity-mismatched. The spec text ("mismatched Capture bases") is literally satisfied, but this conflicts with "missing semantic context should be visible".

**Fix:** Add `currentAvailability` and `currentIntegrity` for the heads of changed Captures.

### F6: Low–Medium. Test coverage gaps

These tests pass, but not for the reason they suggest:

| Test | What it actually covers | What is left untested |
|---|---|---|
| `test_assessment_scheme_and_review` | 3 of 4 subcases (`scheme`, `assessor`, `method`) fail on **"Identity anchor changed"**, because `revision()` is used | The `Unknown confidence scheme pin`, `reviewer/method mismatch` and `actor==assessor` checks are never exercised at genesis, so the I10 scheme pin is untested |
| `test_prefix_rewrite_and_truncation` | Truncation | In-place rewrite (see F3) |
| `test_no_future_or_self_reference` | An absent pin | Self-reference introduced through a correction (see F4) |
| `test_bad_calendar` | Behaviour that depends on the environment (see F2) | Behaviour when the format checker is missing |

### F7: Low. Envelope digests are written but never checked

`acceptance.py` writes `provenance.snapshotDigest` and `previousSnapshotDigest` into native facts. No shipped function checks either value against `value` or against the previous fact.

A tampered snapshot can still pass both native validation and companion validation if the edit is companion-consistent, for example rewriting the rationale of a head row that has no dependents. Such tampering is caught only by `validate_extension` against a trusted previous root, and that root is out of scope. The fix is to provide a `validate_envelope(fact, prior_fact)` helper, or to state that these fields are advisory.

### F8: Low. The write path exposes oracles, so the host must return generic responses

- `admit` validates the record schema before checking authorization, so the response distinguishes `Invalid` from `Denied`.
- The replay lookup matches on `(id, revision)` across **all kinds and scopes**. A Capture writer in scope S can therefore learn whether an arbitrary ID exists, from any type or scope, by whether the write is rejected or accepted.

This is documented as the host's responsibility and is only partly mitigable, because opaque IDs may still be guessable.

### F9: Low. The scheme pin's ID and revision are literals

In `SCHEME`, `id` and `revision:1` are hard-coded while `digest` is computed. They should come from `x-confidenceScheme`, so that drift is detected.

### F10: Low (info). Different denial messages from `gate`

`gate` returns `Denied('Access denied')` when the config has expired and `Read denied` when the reader is not cleared. This lets a caller who is not a reader tell the config state apart. It is acceptable only if the host maps both to one response, which the spec requires.

### F11: Info. Performance and bounds

- Each `admit` fully revalidates the ledger twice, with schema, digests and semantic checks, so a sequence of admissions costs O(n²).
- There is no aggregate byte bound: each record allows up to 10,000 notes of 4,000 characters.

The practical ceiling is therefore well below the declared 10,000 records.

### F12: Info. Conflicting external claim pins are invisible

Accounts that pin the same `(claim id, revision)` with different digests are matched only by exact pin. A reader querying one digest gets no signal that the other exists. This is consistent with exact pinning; a conflict indicator is an optional enhancement.

### Informational notes on acceptance and docs

- `acceptance.py` requires non-`-O` mode, while `AGENTS.md` says `-O` is not needed. There is no contradiction for `provenance.py`, but the difference should be stated.
- Laundering: an internal inference can be captured as a file and re-asserted as `source-asserted`. The Capture then has no link back to the internal account. This is consistent with declaration semantics (a source asserted it) and is a candidate for a deferred derivation link, not a defect.

---

## Focus areas that trace correctly

| Area | Result |
|---|---|
| **Provenance versus truth** | `truth:'not-evaluated'` and `permissions:'not-inferred'` are always returned. `context-available` requires only an active account that is not `unverified`, as documented. |
| **Exact pins** | `pin(target)==p` covers id, revision and digest, plus scope, active state and current head. New reliance on superseded or withdrawn revisions is rejected. Withdrawal skips semantic checks and its content cannot change. |
| **Past knowledge** | `knownAt` produces a receipt prefix. The historical view is byte-equal to the pre-correction view (the test traces this). |
| **Local graph** | Every ref resolves to an earlier receipt, so the pin graph is acyclic. The closure walk is iterative. Input times are checked; unknown times are not invented. |
| **Reader gate** | `gate` runs before `knownAt`, claim and ledger parsing. A non-reader receives no IDs, counts or contrary-evidence signals. |
| **Current rights and replay** | The grant, `writer==actor` and `recordedAt==now` are rechecked on replay. An identical payload is a no-op that keeps the first receipt. A conflicting replay is rejected without mutation. |
| **Kind versus review** | `epistemicKind` is an anchor. A review adds only an attributed ConfidenceAssessment. Observed requires live-observation over `live-api` Captures of the observed target. |
| **Citation and support** | `relation` is an anchor, so a `cites` link cannot be upgraded to `supports`. Opposing evidence links coexist. |
| **Independence** | Only shared bytes or a shared declared origin produce `known-shared-origin`; everything else is `unknown`. |
| **Native versus companion** | The companion uses its own model ID, namespace, binding ID and runtime `modelId`, and does not impersonate WM-XCT-012, which is installed semantic-only. The acceptance harness shows that native validation accepts an invalid nested snapshot while the companion rejects it, consistent with I12. |

## Tests traced statically (not executed)

- I counted 48 `test_*` methods, matching the `testsRun: 48` reported in `test-results.json`.
- Every test traces to a pass if `rfc3339-validator` is present; without it, `test_bad_calendar` would fail.
- The caveats in F6 apply.
- I traced the three acceptance profiles only as far as the companion calls, including the correction to `10:01:00Z` against the ai-team receipts `10:00:01`–`10:00:08`. Native composer and skill behaviour is outside what I received.

## Evidence limits

- This is static reading only. I executed, fetched and searched nothing, and modified no files.
- Library-behaviour claims in F2 about jsonschema's `pattern`/`search`, `1.0` as an integer, and the regex flags in `rfc3339-validator` come from recall of the libraries, not inspection of the installed versions.
- The locally executed test and acceptance results were supplied by you. I did not reproduce them.
