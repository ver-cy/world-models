# EM-XCT-05 `0.0.0-prototype.3`: frozen no-tools review

**Verdict: ACCEPT WITH LIMITS** for the declared scope: a metadata-only research prototype, not publishable and not integrated. I found no path where caller-supplied bytes can produce `applicable-review` when the host is honest and the import invariants hold. I did find several low-severity code defects, a few README claims that go beyond the code or the executed evidence, and one gap in version binding. D1–D4 should be fixed before the next frozen snapshot. If the README claims flagged in §3 are cited as verified behaviour without those fixes, the verdict for that use becomes REVISE.

## 0. Basis

- **Files read in full:** `README.md`, `disclosure.py`, `disclosure.schema.json`, `test_disclosure.py`, `test-results.json`, `examples/startup.json`, `examples/matrix.json` and `examples/ai.json`. No truncation was visible, and each file closed properly.
- **Hashes:** I cannot compute SHA-256 without tools. I only checked that the stated file hashes agree with `test-results.json` `inputHashes`/`exampleHashes`. They agree.
- **Tests:** I counted 90 `test_*` methods, which matches `testsRun: 90`. I did not run anything, so the pass result is Codex-reported evidence only.
- **Prior context:** I have no access to the earlier R1/R2 study artifacts. Nothing below relies on them.

## 1. Defects

**D1 – The version self-check disappears under `python -O`** (`disclosure.py`, module level `assert all(...)`)
- *Witness:* run with `-O`, or with `PYTHONOPTIMIZE=1`, after editing the schema `version` const. The module loads silently, contradicting the README claim "The code version is checked against both record schema constants on module load."
- *Impact:* low, because the schema const still enforces the version on records.
- *Fix:* replace the assert with `if not all(...): raise RuntimeError('schema/version mismatch')`.

**D2 – `inspect`'s superseded-review check matches the digest exactly, so it is bypassable without import** (`disclosure.py:inspect`, `canonical(rb['supersedes']) in active`)
- *Witness:* review B has `supersedes = {id:A, revision:'1', digest:<wrong>}`, and `activeReviews = [pin(A), pin(B)]`. `validate(B)` passes, the membership test misses, and both reviews are counted. If both are cleared, the result is `applicable-review`.
- The README says inspect "additionally rejects ... a still-active superseded target". The code only does this when the digests match exactly. Import would catch the mismatch, but `inspect` does not require that import ran.
- *Fix:* index active pins by `(id, revision)`. Raise `superseded review still active` on an identity/revision match, and raise `incoherent supersession pin` if the digests differ.

**D3 – `inspect` does not re-check the identity-type invariant**
- *Witness:* a review record with `id == proposal['id']` and `revision:'2'`, listed as active. `inspect` validates and counts it. `import_records` would reject it with `identity changes type`.
- *Fix:* in the review loop, raise if `r['id'] == proposal['id']`. Alternatively, state in the README that `inspect` trusts this import invariant, alongside the transitive-supersession caveat.

**D4 – Neither the snapshot nor the answer binds a schema or evaluator version** (`disclosure.schema.json#/$defs/snapshot`, `inspect.result`)
- Records carry `format`/`version`. Snapshots and answers do not.
- *Witness:* a preserved prototype.3 answer carries `snapshotDigest` and pins, but nothing records which reference semantics produced it. A shape-compatible snapshot from another version would be accepted as-is.
- This undercuts the README's position on historical answers and "no automatic mixed-version".
- *Fix:* add `format`/`version` consts to the snapshot schema, and add `'evaluator': VERSION` to every answer.

**D5 – A future-dated assessment looks the same as an expired review** (`inspect` window test)
- `reviewedAt > now` is never checked. Because `reviewedAt ≤ validFrom`, such a review falls into `outside-window`, the same reason an expired review gets.
- *Witness:* this is already executed evidence. In `test_future_review`, `now=10:00:30Z` and `reviewedAt=10:01:00Z`, and the result reports `outside-window`.
- A record claiming an assessment after the pinned evaluation instant is an evidence anomaly, not an expiry.
- *Fix:* add a reason `future-assessment` (or raise `Invalid`), and split `outside-window` into `not-yet-valid` and `expired`.

**D6 – The same host fault is classified two different ways**
- If a still-active superseded review belongs to another revision of the same proposal, the caller cannot supply it, because that raises `review points to another proposal`.
- The result is therefore `insufficient-context`/`review-set-incomplete`. The same-revision case raises `superseded review still active` instead.
- Both outcomes fail closed, but the diagnostic misleads.
- *Fix:* document that `activeReviews` is scoped to the pinned proposal revision. Optionally, reject any snapshot active pin whose record is shown to target a different proposal.

**D7 – Coherence over-restricts legitimate evidence** (`exact_identifiers(coherence=True)` applies across the whole record)
- *Witness:* a review whose `evidence` cites an earlier revision of the proposal it reviews (for example, a diff baseline). This raises `incoherent reference pin`.
- *Fix:* either scope coherence to proposal members and bindings, or document that one revision per ID applies across all roles in the record, including evidence.

## 2. Retention and scale boundary (documentation defect)

`import_records` requires the complete local master set, requires every internal pin to resolve, and caps the total at `len(existing)+len(incoming) ≤ 128`. This has two consequences the README does not spell out:

- **Partial disposal breaks the store.** Suppose the host disposes of a proposal, or a superseded review, while keeping a review that references it. From then on, every import raises `unresolved internal pin`, including idempotent replays.
- **The cap is permanent.** A dimension can never hold more than 128 records in total. The README calls disposal "a separately governed host operation", but omits both points.

*Fix:* state that disposal must be closed under internal references, removing referencing reviews together with their targets or tombstoning them, and that disposal is incompatible with this import contract as written. Also state that the cap is a hard per-dimension lifetime limit.

## 3. Claims that go beyond the evidence

| README claim | Status |
|---|---|
| Import validates "nondecreasing assessment times", same-proposal supersession, no duplicate stored revision, and no review predating its proposal | The code is present, but no test exercises `supersession time reversal`, `supersession crosses proposal identity`, `duplicate stored revision`, or the import-side `review predates proposal`. Say "implemented, not test-evidenced", or add the tests. |
| Inspect "rejects ... a still-active superseded target" | True only for exact digest matches (D2) and for same-proposal-revision targets (D6). |
| "ignored negatives remain visible" | This holds for authority and window exclusions. A *withdrawn* rejection is visible only as a pin in `withdrawn`, without its verdict. Say so. |
| "Code version is checked ... on module load" | Not under `-O` (D1). |
| Input bounds list | It omits the 4096-code-point string cap in `canonical()`. Depth and list/object cardinality bounds are implemented but untested; only the byte cap is tested (`test_input_bound`). |
| `test_actor_catalog_cannot_be_substring` | This actually tests that the schema rejects a string where a list is expected. It shows only indirectly that a substring match cannot happen. Rename the test or add a list-based case. |

## 4. Trusted-host duties (not defects, and correctly declared)

The host is responsible for:

- Authenticating and authorizing the caller. `capability` is an unauthenticated dict, and a str subclass or a lying host defeats `authorize`.
- Clock accuracy.
- Completeness of the active and withdrawn sets. Omitting an objection yields a clearance.
- Resolving external pins, and the scalar/closed-schema truth of member declarations.
- Deactivating transitive superseded ancestors, and resolving supersession forks.
- Binding actor strings to distinct people. For example, `URN:synthetic:founder` and `urn:synthetic:founder` pass segregation as different actors.
- The authority, catalog and withdrawal changes that can neutralize an objection. These show up in `ignored`, but they are host-controlled.
- Choosing a maximum validity horizon. `validTo` is unbounded.
- Write-time role enforcement, compare-and-swap persistence, uniform refusal and timing, redacting `residualRisk`, and access control over diagnostics.

The README states each of these. The prototype has no control for any of them, and none should be inferred.

## 5. Confirmed by reading

- **Caller cannot substitute records.** Caller-supplied proposal and reviews are digest-bound to host pins: `snapshot['proposal'] == pin(proposal)`, and the supplied pin set must equal the active set exactly.
- **Canonical encoding** matches the README: code-point key order, lowercase `\u00xx` escapes, literal DEL and U+2028, no floats, safe-integer range, and rejection of str/dict/list subclasses and surrogates.
- **Newline and trailing-`$` handling:** the Python `re.search` weakness of the schema patterns is closed by full matching everywhere a pattern applies. That covers ids, revisions, keys, names, digests, actor catalogs, and all timestamps via `instant`. Its ASCII `[0-9]` also closes the Unicode `\d` gap in the schema.
- **Time rules:** the review interval is half-open and `reviewedAt ≤ validFrom < validTo`. Self-supersession is rejected by identity and revision. Import is transactional (`existing` is unchanged when it raises) and idempotent for the same revision and digest.
- **Early exits:** `reviewsEvaluated=false` is set correctly on early stale or context exits. Caller-supplied reviews are not validated on those paths, which is acceptable because no verdict analysis happens.

## 6. Out of scope

I am not auditing the metamodel or publication package, and I am not making any claim about native V3 behaviour, privacy, inference resistance, NIST conformance, or cross-language digest compatibility. This review does not authorize release.
