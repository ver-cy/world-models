# R3 supplementary review: adoption documents and publication addendum

## 1. Method and input completeness

I did one manual static read of the supplied fragments in this conversation, with no tools or browsing. I cross-checked each document against the `spec.json`, `action_bundle.py`, schema, installer and acceptance sources from the previous round. For completeness I summed the declared fragment lengths against the manifest byte counts, allowing for non-ASCII characters I could identify, and checked every fragment seam for continuity. I did not compute any hashes or run anything.

| File | Fragments | Length check | Seams |
|---|---|---|---|
| README.md | 2/2 | 6,806 chars + 4 bytes (two em dashes) = 6,810, matches manifest | `are m`/`andatory` continuous |
| model-spec.md | 4/4 | 20,193 chars + 7 bytes (`→`, `±`, `−`, `–`) = 20,200, matches manifest | all three continuous |
| adoption-limits.md | 1/1 | 2,749, matches manifest | n/a |
| requirements.txt | 1/1 | 19 (`jsonschema==4.26.0\n`), matches manifest | n/a |
| model-fields.md | 7/7 | 6×6000 + 2,802 = 38,802, matches manifest | all six continuous |
| bindings/native-v3.md | 1/1 | 2,092, matches manifest | n/a |
| publication-addendum-r3.md | 2/2 | 6,063 chars; no byte count supplied, so not length-checkable | `pa`/`rtially` continuous |

Nothing is truncated or elided, so this is not INPUT INCOMPLETE. The addendum is a new file outside the R3 frozen manifest. I can only confirm that its display is internally complete, not that it matches its stated hash.

## 2. Verdict

**Accept-with-explicit-limits, with no remaining release blockers from this document set.**

None of the documents contradicts the code on any behavior the code actually implements. None of them promotes the candidate/simulationOnly lock to publication status: `native-v3.md` and the addendum both say explicitly that it is not publication evidence.

The addendum accurately discloses the items I asked for:
- **Capacity:** the finite, shared event budget (about 3,333 pending submissions or 2,500 first commits), no quotas or rollover, and the revocation row reserving no execution capacity.
- **External duties:** host authority, standing, authentication, time, isolation, rate limits and continuity.
- **Caller projections:** they are limited, and receipts disclose `beforeLabels` and `afterLabels`.
- **Validator gap:** a backdated administrative row can pass archive validation.
- **Test gaps:** the vacuous newline half, missing edge tests, the absent native runtime inventory, and SQL-seeded capacity tests.

It also closes my earlier findings as disclosures:
- M1 (cross-table clock) and M3 (retired-key cancel) are disclosed as they behave in code.
- S1 through S7 are disclosed, with the S2 caller-access point fully covered.
- T1, the T2 generated-ID-collision and backdating gaps, and M2 are disclosed or listed as further work.

Items under "Further work" are correctly framed as future work, not as existing code.

## 3. Remaining minor findings (non-blocking wording fixes)

**D1. The addendum overstates the validator.** Its History section says archive replay checks "per-table times". In `history._validate`, only policy rows and events are checked as monotonic within their own tables. Definition `recorded_at` and revision-0 resource `recorded_at` are only bounded by the cut clock and by use-time checks (`definition_at`, `precondition`).
- *Fix:* change it to "policy and event times are monotonic within their tables; definition and resource creation times are bounded only by the cut clock and by use-time checks."

**D2. The installed README has dangling references, and "all adoption documentation" is overstated.** The README and `adoption-limits.md` claim each installation includes all adoption documentation. However, the installed README's "Package and review state" section points to files the nine-file installer does not copy: `model-fields.md`, `whole-object-coverage.yaml`, `mastership-and-rights.yaml`, `composition.yaml`, `crosswalk.json`, `invariants.md`, `migration.md` and `review.json`. The addendum mentions only `review.json` and itself.
- *Fix:* add one addendum sentence saying that the installed README references further package documents that are not installed, and that they should be consulted from the released package.

**D3. Three `model-fields.md` descriptions are imprecise.**
- `intent.resourceId` and `Scope.resourceId` say "Existing … resource". In fact admission does not require the resource to exist: it ends as `rejected-precondition`, as `test_later_resource_creation…` shows.
- `Rule.issuerId` reuses the event-issuer text ("Host that asserts/captures the event"). This conflates it with the policy issuer, which the spec says is a different role.
- `Pin.revision` mentions "a host sequence in auxiliary storage", which nothing in the code implements.

**D4. `model-fields.md` claims to be the complete field contract but omits two schema cardinalities.** `Policy` is an array of 0 to 128 Rules, and there is a top-level `Labels` definition; neither has an entry. The snapshot, manifest and resource-row structures are also absent. They are validated in code rather than in the schema, so this is a completeness wording issue rather than a contradiction.

**D5. Stale and duplicated text.**
- The README and `adoption-limits.md` still begin a paragraph "R2 adds…" in an R3 candidate.
- `adoption-limits.md` is a verbatim copy of the README's limits section, which invites drift.
- `native-v3.md` says "The installed tests demonstrate…". It is more accurate to say the acceptance workflow runs the installed companion.

**D6. The T2 snapshot-level newline gap is not listed.** The addendum lists the missing generated-ID-collision and backdating tests. It does not mention the absence of a snapshot-level newline test, for example an `eventId` ending in `\n` inside a history.

## 4. Consistency spot checks (all consistent)

- **model-spec.md vs spec.json:** `model-spec.md` matches the `spec.json` scope text.
- **Retired-key cancel:** the addendum's claim that it returns `key-retired` to a current reader without a new event matches `cancel`, which calls `_out(c, r, readable)` before any try.
- **Field tables vs schema:** the tables match `action.schema.json` for ActionDefinition, ActionRequestSnapshot, Intent, all seven Events, Pin, DefinitionRef, Scope and Rule. This covers closure, patterns, bounds and nullability. The claim "afterRevision = beforeRevision+1" matches the history `receipt-effect` check.
- **Pinned versions:** `requirements.txt` (`jsonschema==4.26.0`) and the README's Python 3.12 match the unit report (3.12.14).
- **Native binding procedure:** the documented order (objects before events, cut stored inside the Dimension, nested validation required in addition to the outer pass) matches `acceptance.py`.

## 5. Release recommendation (no authority claimed)

With this addendum included, the frozen R3 candidate has no document-level release blockers. D1 and D2 are worth fixing in the addendum wording before publication. D3 through D6 can wait for the next pinned revision.

Adding the addendum changes the package file set even though the code is unchanged. The release manifest and review input therefore need to pin its bytes.

The remaining gates are outside this review:
- Grok's independent R3 result.
- Executed source, bundle and native reports against the frozen hashes.
- The unseen `profile-manifest.json`, `publication-manifest`, and the final `review.json` disposition.
- Live publication verification.