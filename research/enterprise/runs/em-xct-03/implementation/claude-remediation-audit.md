# Verdict: **ACCEPT WITH LIMITS**

This covers only the revised candidate as supplied. It is not publication authority.

Both of the earlier blocking findings are resolved in the traced source.

- **Correction freeze.** `semantic()` now builds `retained` from the previous head's immediate refs. A retained pin skips the current-head check but still gets exact-pin, scope, type and pinned-revision-active checks. Indirect Activity inputs use `current=False`. I traced tests 49–52 and they exercise the intended paths.
- **Timestamp-format dependency.** `instant()` is now authoritative for every named timestamp field and for `now`/`knownAt`: ASCII regex fullmatch plus `strptime`. Year `0000`, `:60`, Unicode digits and trailing `\n` all reject. Missing `uri`/`date-time` checkers fail closed.
- **Cross-revision self-derivation.** The walk rejects any transitive pin to the record's own ID. Its `visited` set keeps it terminating, and pins point backwards, so `prior[key]` always resolves. Test 57 traces correctly (records[5] → self-cycle synthesis → rejected).
- **Other claimed fixes, confirmed:**
  - `type(v) is int` walker on revisions.
  - Canonical-byte prefix and replay comparison.
  - `currentCaptureState` exposed in views.
  - Uniform `Read denied` for expired config.
  - `SCHEME` derived from the embedded schema.
  - 8 MiB cap applied inside `encode`.
  - Distinct per-profile Dimension IDs in acceptance.
  - Immutable versioned upstream URLs.
  - No `assert` in production paths.

## Remaining defects, most important first

1. **Medium: a label upgrade can rely on a withdrawn basis.** A ConfidenceAssessment correction keeps its `account`, `activity` and `basis` pins as retained. It can therefore flip `label` from `insufficient`/`limited` to `supported` after the account (or a basis Capture) has been withdrawn or mismatched. No fresh review Activity is required. The view flags `requiresReview`, so it is not silent. It still conflicts in substance with "new reliance on a withdrawn revision is rejected", because a label change is a new judgement, not metadata.
   - **Fix:** require all immediate targets to be current and active when `label` changes, or when the label goes to `supported`. Alternatively, state in the contract that label corrections are exempt.
2. **Medium: a future-dated import can freeze the register.** `validate_ledger`, `import_snapshot`, `validate_snapshot` and `validate_extension` take no `now`. A snapshot containing `recordedAt: 9999-12-31T23:59:59Z` validates. Every later `admit` then fails "Receipts must strictly increase", with no recovery short of rewriting history.
   - **Fix:** add an optional `now` bound (last receipt ≤ `now`) to the import and snapshot paths.
3. **Low–medium: retained pins can swap roles.** The retained set is the union of all of the previous head's refs, not a per-field set. An assessment correction can put its old (possibly superseded) account pin into `basis` without a currency check. The contract says "unchanged immediate pin", but the code implements "any pin previously present anywhere in the record".
   - **Fix:** key the retained set by field.
4. **Low: a new activity can consume a revision before it existed.** A new Activity must pin the current head. That head may be a correction recorded after the Activity's claimed `endedAt`, because the time check uses `obtainedAt` or the producer's `endedAt`, not the input revision's receipt. The activity then claims to have consumed revision-N metadata that did not yet exist. The contract is silent on whether a pin denotes the content or the revision's knowledge.
5. **Low: corrected origin declarations are ignored for independence.** Independence uses the pinned historical `originRef` (a non-anchor field) and still counts withdrawn Captures. A corrected shared-origin declaration stays invisible until the accounts re-pin. The fallback is `unknown`, which is conservative, but the loss of disclosure should be documented.
6. **Low: some denials are not uniform.** An invalid config or invalid `now` raises `Invalid`, not `Denied`, in both `gate` and `admit`. `admit` also validates the record before its authorization check, so an unauthorized writer can distinguish Invalid from Denied. Both are host-internal diagnostics, so this depends on the host returning generic errors.
7. **Low: `validate_snapshot` only checks one hop.**
   - It does not check the previous fact's `recordType`/`path`/value-envelope type beyond the fields listed.
   - It does not reject `factId == previous.factId`.
   - It allows a byte-identical successor, which is a no-op extension.
   - A genesis snapshot with a non-empty history is accepted.
   
   All of these rely on the host's trusted predecessor, as documented.
8. **Spec gap: the digest encoding is not specified for interop.** Digests are Python `json.dumps(sort_keys, compact, ensure_ascii=False)`. For this value domain (ASCII keys, no floats) that output closely matches RFC 8785, but the contract calls it "canonical JSON" without naming the algorithm. Independent implementers cannot reproduce the pins with confidence.
9. **Resource limit: CPU is unbounded.** Each `admit` runs `validate_ledger` twice. That includes full jsonschema validation, where `uniqueItems` over dict pins can be O(n²) with up to 10,000 items, plus per-record transitive closure walks, which are O(n²) on chains. The 8 MiB byte cap does not bound CPU. There is also no segmentation or rollover, so a register approaching 8 MiB becomes permanently append-frozen.
10. **Tree wording: AP-ACT05 "Retain ID".** On relocation this conflicts with `sourceRef` being an immutable Capture anchor. It is presumably meant as the external/source identity, but the wording is ambiguous.

## Static-review and truncation limits

- I did not execute anything. The 62 tests and three native profiles are your report. I only traced the source.
- I did not recompute the supplied hashes.
- The following were not visible to me:
  - `spec.json` fields other than the tree and contract.
  - The full `model-spec.md` (only the diff).
  - `runtime-model.reference.json`, `tool-pins.json` and upstream files.
  - The composer/skill code (`composition`, `bootstrap_dimension`, `write_record`, native `validate_dimension`).
  - The generated `examples/*`.
- The acceptance negative case asserts that native V3 *accepts* a malformed nested value, which demonstrates layer separation, not native correctness.
- I assumed jsonschema behaviour for format-checker registration, `integer` accepting `1.0`, and `uniqueItems` complexity.
- Out of scope, as the brief states: the trusted host (authentication, complete current root, clock, concurrency), IAM, source fetching, truth selection, legal or parent conformance.

## Completeness

- I counted exactly 62 `test_` methods.
- The structure tree has 20 findings, AP-F01–F20. Each has one question, artifact and action, and none are missing.
- The final sentinel `AP-REMEDIATED-62-THREE-DIMENSIONS` is present, so the input was not truncated.

**Recommended before publication:** fix #1 and #2, or record them explicitly as contract limits, and name the digest encoding (#8).
