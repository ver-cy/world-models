# Verdict: **ACCEPT WITH LIMITS**

This covers the bounded trusted-host draft of Enterprise Assertion Provenance 0.1.0. I found no truncation. Every `FILE` block has its `END FILE` marker, and the final sentinel **`AP-FINAL-69-HOST-CLOCK-FIELD-PINS`** is present. I did not recompute the hash banners and did not execute anything. I counted 69 test methods, which matches the reported count. `spec.json`, `tool-pins.json`, `runtime-model.reference.json`, the upstream files and the examples were not supplied. So I could not check the AP-ACT05 text itself. I could only check that the `Capture` anchors in `ANCHORS` (sourceRef, sourceVersion, obtainedAt, availability, representationDigest and the rest) enforce the stated "new Capture ID" rule. They do.

## Prior fixes: statically confirmed

| Fix | Trace | Result |
|---|---|---|
| Field-keyed retained pins | `retained={(field,encode(p))…}`; every `resolve` call passes its own `field` (`inputs`, `activity`, `evidence`, `account`, `basis`). The source-asserted input check uses `current=False` on the activity's own historical inputs, which is correct | Holds. `test_retained_pin_cannot_change_field` fails as intended with "superseded" |
| Label promotion on correction | `new_judgement` clears `retained` and requires `activity!=old['activity']`. The closure walk requires `pin(head)==p`, an active head, and for Captures `captured` with no `mismatched` integrity | Holds for the correction path. The three new tests trace correctly |
| Future receipts | `import_snapshot`/`migrate`/`validate_snapshot` have keyword-only `now` and pass it to `validate_ledger`. `admit` and `view` pass `now` for both previous and candidate ledgers. `validate_snapshot` also bounds the previous ledger via `validate_extension(...,now)` | Holds |
| Snapshot successor | `previous.recordType=='fact'` and `factId` differs from the successor's | Holds. A byte-identical no-op successor is still allowed, as documented |
| Encoding | `encode` matches the documented vercy-python-json-v1 call exactly. Lone surrogates are rejected via `UnicodeError` | Holds |

## Remaining concrete defects

**D1 (medium; fix before publication or document it): the promotion guard can be bypassed through genesis and basis swaps.** The closure-currency and Capture-state checks run only when `new_judgement` is true, meaning a correction whose label changes to something other than `insufficient`. Two admissible paths reach the same outcome the fix was meant to prevent:

- **New assessment ID.** In the ai-team fixture, first correct the capture to `integrity='mismatched'`. Then admit a genesis `ConfidenceAssessment` with `label='supported'`, reusing the existing review Activity and setting `basis=[pin(capture r2)]`. All immediate pins are current and active, so it is admitted. It relies on a mismatched Capture directly, and on a superseded Capture r1 transitively through the account.
- **Basis swap, label unchanged.** Correct an existing `supported` or `limited` assessment with a new `basis` and the same label and activity. The spec calls this "metadata maintenance", but the judgement now covers different evidence, with no fresh review and no closure check.

`view` still reports these through `sourceGaps` and `changedDependencies`, and truth is still `not-evaluated`. That disclosure is why this is not a BLOCK. Admission is still inconsistent with the invariant the previous round asked for. A minimal patch in the file's own style:

```python
reliance=r['kind']=='ConfidenceAssessment' and r['label']!='insufficient' and (old is None or any(r[f]!=old[f] for f in ['label','basis','activity']))
if reliance:
    retained=set()
    if old is not None and (r['label']!=old['label'] or r['basis']!=old['basis']):
        require(r['activity']!=old['activity'],'Changed reliance judgement needs a fresh review activity')
```

Then gate the closure check on `reliance` instead of `new_judgement`. With this patch, `test_retained_pin_cannot_change_field` would fail earlier, on "fresh review" rather than "superseded". Adjust that test's regex, or give it a fresh review, and add genesis and basis-swap negative tests.

**D2 (low): "fresh" review means a different ID, not a later review.** Any other pre-existing review Activity of the same account satisfies the check, including a duplicate with an identical interval, as in `test_changed_judgement_positive`. Basis pins outside the review's own closure can also have been recorded after the review. A cheap receipt-based tightening would require the new activity's `recordedAt` to be later than `old['recordedAt']` and at least the latest basis head's `recordedAt`. Otherwise, state in the spec that freshness is identity-only.

**D3 (low; usability):** Downgrading `supported` to `limited` counts as "any other label change". When dependencies are stale it is rejected, so the assessor is forced to `insufficient`. This matches the spec wording, but it may not be intended.

**D4 (low):** `import_snapshot`, `migrate` and `validate_snapshot` do not call `config_check`, so an expired or not-yet-valid configuration is accepted at import. `admit` and `view` do enforce validity. Either add the check or list it as a host requirement.

**D5 (low; portability):** The vercy-python-json-v1 description relies on Python's implicit escaping behavior. That includes lowercase `\u00XX` for control characters, `\n` and the other short escapes, and unescaped U+2028/U+2029. Independent adapters need these rules spelled out, or a byte-level test vector that includes control characters.

**D6 (low; declared scope):** A `basis` pin may be an EvidenceLink for a different claim, or a Capture unrelated to the assessed account. Relevance is not checked and stays an assessor declaration. This is worth one sentence in the spec.

## Host integration requirements (not code defects)

These are correctly assigned to the host and consistently documented:

- caller authentication
- the latest trusted complete root and predecessor snapshot
- trusted configuration and clock
- serialized, non-concurrent admission
- generic write-only receipts and errors (for example, `admit` raises schema `Invalid` before the writer `Denied` check, and uses "Access denied" rather than "Write denied" when the configuration has expired)
- pre-parse byte limits
- CPU budgets for quadratic revalidation
- rollover and archive planning
- full native V3 envelope validation
- method and external-claim resolution

`acceptance.py` uses a fixed `now` and offline `validate_extension`. That is appropriate for a synthetic harness, not evidence of live admission.

## Preserved record

The initial BLOCK and both prior ACCEPT WITH LIMITS verdicts stand unchanged. This verdict adds to them and does not rewrite them. It makes no claim of publication readiness, conformance with the parent model or standards, or full enterprise production conformance. I recommend fixing D1 before publication. D2–D6 can be fixed or documented as limits.
