# EM-XCT-05 `0.0.0-prototype.3` — frozen metadata-only review

**Verdict: ACCEPT WITH LIMITS**

This is a local research prototype, not a release, not a production security boundary, and not a native Vercy V3 integration. This review does **not** authorize publication, installable packaging, or production use. R1/R2 audits are not in this package and do not approve these bytes. The full metamodel / publication tree is not present, so this is not a final audit.

No contract-breaking defect was found in the declared prototype scope: no silent clearance of an eligible opposing verdict, no digest aliasing, no identifier-equivalence claim that the code then violates, no idempotent merge that mutates history.

---

## Files actually read

All bytes came from the supplied package. No execution, no web, no extra files.

| File | SHA-256 as supplied | Truncation |
|---|---|---|
| `README.md` | `1088e0c4969c94e191ee7b02e0c261198e240d4db0d90d20fd793b0648e3cbb6` | none |
| `disclosure.py` | `f77140d098b99a1d88f230425a1e9c12781b38c7b68b686dab77410f1bcf8d9f` | none |
| `disclosure.schema.json` | `e581e0ab252a7c8c9e5000a056cddea3ab167dbbc5db97e8c36148ccd17ef687` | none |
| `test_disclosure.py` | `282b89b6af653d29ec9a48688d4d21d8024d85fe6b4c332704a74c1731d64ed8` | none |
| `test-results.json` | `b345585228d4e9d0ddeacd84cb33e490e0f8e6e6caca1ef6930e4de36e8024bc` | none |
| `examples/startup.json` | `76f2caa35724e9722ddb95552480ba108c673e905a01537baed202eee8c0fced` | none |
| `examples/matrix.json` | `c193663e719232048118b10cabe6b8d72c60f73e2944d7fc1a6d40fbe3f22d20` | none |
| `examples/ai.json` | `e647cb2189b1930a50a1829ca29dca6bc13374e1b62788307ba41c9febc9d11a` | none |

Those hashes are internally consistent with `test-results.json` `codeSha256` / `inputHashes` / `exampleHashes`. **Tests were not run here.** The report (`status: passed`, `testsRun: 90`, `failures: 0`, `jsonschema: 4.26.0`, CPython 3.12.14) is Codex evidence from one environment, not an independent replay.

---

## What holds on the supplied bytes

Anchors: `disclosure.py` `canonical`, `load`, `hash_body`, `seal`, `validate`, `exact_identifiers`, `authorize`, `validate_snapshot`, `inspect`, `import_records`; `disclosure.schema.json` `$defs.{pin,proposal,review,snapshot}`.

- Sealed records are digest-bound: SHA-256 over the documented local restricted JSON of the record with only the top-level `digest` removed. Encoding is **not** RFC 8785/JCS. Golden vector `test_golden_encoding_controls_and_separator` matches the stated C0 / quote / backslash / literal U+2028 rules.
- `canonical()` uses `type() is`, not `isinstance()`, so container/string subclasses cannot spoof actor equality.
- `load()` rejects duplicate keys, invalid UTF-8, floats / NaN / Infinity / exponent syntax, unpaired surrogates, and integers outside the safe range. Dictionary APIs are not wire parsers.
- Identifiers are exact printable-ASCII grammar plus `re.fullmatch`. No URI case-fold, percent-decode, NFC, or alias resolution. Hidden characters (`\n`, ZWSP, RLO, NUL, BOM) are refused.
- Proposal-body pin coherence is keyed by `id → (revision, digest)` across nested `{id,revision,digest}` objects. That matches “one consistent revision/digest per referenced ID across the proposal.”
- `inspect()` status taxonomy is distinct: `stale`, `insufficient-context`, `conflict`, `rejected`, `inconclusive`, `applicable-review`, plus `Invalid` / `Unauthorized`. Every answer hard-sets `notServingAuthorization=true`.
- Empty or incomplete active sets are never clearance. Eligible disagreeing verdicts become `conflict`. Author rejection / inconclusive still counts under segregation and will conflict with another reviewer’s clearance.
- `import_records()` is a pure transactional merge: same `(type,id,revision)+digest` is idempotent; digest mismatch fails; type cannot change; internal proposal / supersession pins must resolve; supersession is acyclic and nondecreasing in `reviewedAt`; self-supersession is refused at `validate()`.
- Schema + code together lock path scope: field names are scalar identifiers, not `owner.email` / `*` / `/notes/title` / `notes[0]`; `kind` cannot be `object` or `array`; there is no source-value payload field.

---

## Defects vs trusted-host duties

No in-scope **code defect** was found that breaks a claim the README actually makes. The following are **explicit host duties**. They are limits, not invented controls.

| Duty | Anchor | What the reference does *not* do |
|---|---|---|
| Authenticate / authorize the caller | `authorize()` | Capability is a host assertion dict (`inspect is True`, optional `record is True`). Not a token, signature, or request field. |
| Build the snapshot from host state | `inspect()` equality on `snapshot.proposal`, `context`, `members`, `activeReviews` | Equality is not independent origin. Echoing the caller’s proposal as the snapshot is accepted if the bytes match. |
| Enumerate the complete active review set | `inspect()` `supplied-pin-set == active-pin-set` | Code cannot see a review the host omitted from both `activeReviews` and `reviews`. |
| Deactivate transitive superseded ancestors | `inspect()` `canonical(rb['supersedes']) in active` | Immediate edge only. Omitted intermediates cannot be recovered. |
| Bind actor strings to distinct people | exact `in` on `proposalAuthors` / `reviewers` | No alias / role / directory resolution. |
| Resolve source / schema / shape / classification / custody pins | pins compared, never fetched | Host attests that fields are scalar leaves of a closed schema and that pins resolve. |
| Supply `now` as a real evaluation instant | `validate_snapshot()` `instant(asOf)==instant(now)` | Binds declared time only. Does not attest clock accuracy. |
| Pass the complete local master set into import | `import_records()` 128-entry cap | Partitioning away internal references is undefined. |
| Persist, CAS, and write-authorize | `import_records()` docstring | No database, no object-specific writer role, no review-authority check at write. |
| Redact / retain / destroy | none | No disposition engine. Immutability ≠ retain-forever. |
| Serve or refuse over HTTP | none | No uniform refusal, no timing / existence protection. |
| Not forward `inspect()` answers | `result()` | Answers carry pins, ignored verdicts, and withdrawn pins. |

Do **not** add HTTP uniformity, redaction, a source resolver, a disposition calculator, persistent-objection semantics, or real authentication inside this prototype. Those would invent controls outside the declared scope.

---

## Claim challenges

1. **“An active review cannot immediately supersede another still-active review.”**  
   True only for the immediate `supersedes` pin (`inspect()` second loop). A chain `R3→R2→R1` with `active={R1,R3}` is not raised. That yields conflict or double-count if both remain eligible; it does not silently drop a negative that is actually supplied. The README already admits the transitive hole.

2. **“Merely echoing the caller’s proposal as the host snapshot defeats the integration contract.”**  
   Operational contract only. The code tests equality, not provenance.

3. **`format: "vercy-disclosure-research"`**  
   Local research syntax. It is not a public runtime ID and not evidence of native V3 integration. R1/R2 “refused by R3” is only the version `const` on proposal/review, not a dedicated legacy detector.

4. **`applicable-review` is not a serving grant.**  
   Enforced only by the boolean and the README. A confused integrator can still treat the status as authorization. The prototype cannot stop that.

5. **“Snapshot `asOf` must equal evaluation `now`.”**  
   Holds as parsed-instant equality. It does not prove the observations came from that instant.

6. **`reviewedAt <= validFrom < validTo`**  
   Extra local rule in `validate()`, stronger than the Contract paragraph that only names `[validFrom, validTo)` and “assessment cannot predate capture.” Conservative, not a lie; it is under-documented.

7. **A passed Codex suite is not an external audit, privacy proof, or metamodel completion.**  
   `test-results.json` `scope` already says this. Do not promote it.

---

## Adversarial witnesses

**W1 — omitted live rejection (host attestation).**  
Host leaves a current rejection out of both `activeReviews` and `withdrawnReviews`, supplies only a clearance. `inspect()` returns `applicable-review`. The reference never saw the objection. Duty: complete active set.

**W2 — echo snapshot.**  
Caller-built `hostSnapshot` that copies `proposal.body` context/members plus a forged capability `{dimension, inspect: True}` is accepted if shape-valid. Examples warn (`fixtureKind`), code does not enforce origin.

**W3 — fabricated `asOf`/`now`.**  
Any in-window pair that is internally consistent yields a dated answer. Clock is not attested. Historical answers require a preserved snapshot and current read permission; the function cannot know whether that snapshot is genuine.

**W4 — transitive ancestor left active.**  
`R3.supersedes=R2`, `R2.supersedes=R1`, `active=[R1,R3]`. No `Invalid('superseded review still active')`. If verdicts differ → `conflict`; if they agree → that status. Over-count, not silent drop.

**W5 — request-shaped capability.**  
`authorize()` is the first gate and fails closed on missing dimension / `inspect is not True`. If this function is exposed on a network with caller-supplied `capability` + `snapshot` + `reviews`, the caller obtains internal diagnostics (ignored verdicts, withdrawn pins, snapshot digest). Timing / existence protection is unimplemented.

**W6 — `residualRisk` free text.**  
`examples/matrix.json` review body stores an explicit subtraction narrative. Nothing detects or redacts it. `inspect()` does not copy `residualRisk` into the answer; the review record still holds it.

**W7 — membership change with mixed pins.**  
New proposal digest + updated `snapshot.proposal` + old reviews → `Invalid('review points to another proposal')`, not `stale`. Fail-closed, operationally sharp. Locked by `test_added_member_needs_new_review`, `test_added_field_needs_new_review`, `test_reordered_members_changes_pin`.

**W8 — import replay bound.**  
`len(existing)+len(incoming)>128` rejects even an idempotent replay that would not grow the store. Documented cap; no silent corruption.

**W9 — expired negative + live clearance.**  
`test_expired_negative_preserved_in_report`: status `applicable-review`, rejected review remains in `ignored[]` with `reason=outside-window`. Matches the stated profile. Persistent objections need a different reviewed profile — do not invent one here.

**W10 — snapshot pin coherence.**  
`validate_snapshot()` calls `exact_identifiers(snapshot)` with `coherence=False`. Two snapshot pins may share an `id` with different `revision`/`digest` (e.g. `authority` vs `context.audience`). Proposal-body coherence still holds on the sealed proposal. Low severity; host-attested catalog.

---

## Limits that travel with ACCEPT

1. No publication, no installable Vercy release, no native V3 / production integration claim.
2. Capability, snapshot, actor catalogs, withdrawn provenance, source/classification/custody resolution, and evaluation time are trusted-host assertions.
3. Transitive supersession deactivation is host-only.
4. Snapshot schema (`$defs.snapshot`) has no `format`/`version` const. Mixed-generation but shape-compatible snapshots would pass `validate_snapshot()`.
5. Prototype caps: 256 KiB, depth 20, 32 members, 64 fields, 64 reviews / active pins / withdrawn pins / actor-catalog entries, `len(existing)+len(incoming) ≤ 128`. These are not a tested DoS guarantee.
6. `residualRisk`, actor IDs, diagnostic pins, and past revisions need their own access and custody controls. The code neither detects nor redacts them.
7. `priorReleases` / `custodyContext` equality is not permission to retain, serve, or destroy.
8. R1/R2 refusal is version-const only. No migration mapping exists; do not reinterpret stored bytes.
9. Tests are Codex evidence. This review did not rerun them and did not recompute digests of the example fixtures.
10. `inspect()` results are restricted internal diagnostics. They are not a recipient-facing grant.

---

## Optional minimal fixes (not gates)

Only if this snapshot is revised before the next freeze. None of these are required to accept the declared prototype.

1. In `inspect()`, walk `supersedes` edges among **supplied** reviews and reject if an ancestor pin is also in the active/supplied set. Still cannot recover an omitted intermediate; do not pretend otherwise.
2. Call `exact_identifiers(snapshot, coherence=True)` in `validate_snapshot()`.
3. Add `format` + `version` consts to `$defs.snapshot` so mixed-generation snapshots fail closed.
4. Document `reviewedAt <= validFrom < validTo` in the README Contract section.

Do not implement redaction, HTTP uniformity, source resolution, disposition, or real authn in this artifact.

---

**ACCEPT WITH LIMITS** for research-candidate `0.0.0-prototype.3` as a frozen metadata-only reference. Keep it off production paths. A later Bundle / Layer / Finding / Question / Artifact / Action package, native V3 binding, and an immutable published model version need their own review.
