# Follow-up audit — Enterprise Assertion Provenance 0.1.0 (remediated)

**Verdict: ACCEPT WITH LIMITS**  
**Publication authority: not granted.**  
This is a static review of the revised candidate only. It is not parent/PROV/SLSA conformance, not a publication decision, and not ratification of the synthetic `publicationStatus: "published"` stamp in `acceptance.py`.

Previous Claude **BLOCK** (correction freeze; timestamp-format dependency) and previous Grok **ACCEPT WITH LIMITS** (H1 current-head applied to unchanged pins; M4 same-id self-derivation) are **closed in this source** by a contract change plus matching code and tests. They are not papered over. Remaining items below are leftover host/bounds edges, not those defects under a new name.

---

## Completeness and truncation

| Marker | Status |
|---|---|
| Revised `provenance.py`, `provenance.schema.json`, `test_provenance.py`, `acceptance.py`, `AGENTS.md` | present, not mid-file truncated |
| Exact `model-spec.md` diff | present |
| Full 20-question structure tree | present (4 bundles / 8 layers / Q01–Q20) |
| `whole-object-coverage.yaml` | present (JSON body, `.yaml` name) |
| Final sentinel `AP-REMEDIATED-62-THREE-DIMENSIONS` | present |

**Not in this payload / not independently reviewed:**
- full revised `model-spec.md` as a single file (only the diff; prior full spec is the base)
- `spec.json` fields other than the supplied tree/contract
- `examples/*.json`, `tool-pins.json`, `runtime-model.reference.json`, `test-results.json`, upstream bytes
- SHA-256 banners (labels, not recomputed here)
- the reported “62 pass / 3 native profiles pass” runs (traced, not executed)

Prompt attachment 97,505 bytes. No missing section inside the listed artifacts.

---

## What the remediation actually changed

The implementers kept metadata correction instead of forbidding it. The revised graph rule is now:

- **Unchanged immediate pins** on a correction resolve the exact historical revision.
- **New or replaced immediate pins** must name an already-admitted **active current head** in the same scope.
- **Activity input history is not rewritten** when a later account cites that activity.
- **Transitive closure must not contain any revision of the record’s own ID.**

That is what the code now does.

```text
retained = {encode(p) for p in refs(old)}   # empty on genesis
resolve(p):
  exact pin + same scope
  cited-row state == active          # historical create/correct rows stay active
  if encode(p) not in retained:      # or current=True
      pin(heads[id]) == p            # live head only for new/changed refs
```

Withdrawal still skips `semantic()`. View still reports changed/withdrawn dependencies, and a changed Capture now also carries `currentCaptureState.{availability,integrity}` next to the cited pin.

---

## Closed findings (do not reuse the old BLOCK/H1/M4 write-up)

**H1 / Claude correction-freeze — fixed**

| Sequence | Result in this source |
|---|---|
| Capture `C` rev1 → EvidenceLink/Account/Activity pin `C` or the acquisition → correct `C` integrity to `mismatched` → correct Activity notes, account limitations, link rationale **without changing pins** | admits (`test_correct_unchanged_historical_dependencies`) |
| ai-team inferred account corrected (limitations) → assessment label → `insufficient` **retaining** `account=pin(A rev1)` | admits; view `requiresReview` (`test_correct_assessment_after_account_correction`) |
| Change the immediate activity pin back to a superseded revision | `Invalid` (`test_changed_dependency_pin_requires_current_head`) |
| Brand-new link to a stale capture head | still `Invalid` (`test_new_reliance_on_superseded_revision_rejected`) |

A fresh review of a **new** account revision still needs a new review Activity and a new assessment (`account` is an identity anchor). That is the revised spec sentence, not a leftover freeze.

**M4 / cross-revision self-derivation — fixed**

`A` rev1 → synthesis `S` with `inputs=[pin(A rev1)]` → correct `A.activity=pin(S)` raises `Invalid("Self-derivation across revisions")` (`test_cross_revision_self_derivation`). The walk is `refs(r)` then `refs(prior[key])`, rejecting any `p['id']==r['id']`. Versioned pins remain backwards-only via `prior` + monotone receipts.

**Timestamp / integer / prefix BLOCK items — fixed**

- `instant()`: `re.fullmatch(r'[0-9]{4}-...Z')` then `strptime` calendar. Unicode digits, trailing newline, Feb 30 reject (`test_ascii_calendar_and_newline_strict`, `test_bad_calendar`).
- `FormatChecker` must expose `uri` and `date-time` or the companion fails closed (`test_missing_format_support_fails_closed`).
- Every key named `revision` must satisfy `type(v) is int` (rejects `1.0` and `bool`) (`test_fractional_revision_encoding_rejected`).
- Replay and `validate_extension` prefix/header compare `encode()` bytes, not Python `==` (`test_actual_prefix_rewrite_rejected`).

**Other stated remediations — present in source**

- `source-asserted` walks `Activity.inputs` with `current=False` (`test_new_account_can_describe_existing_event_with_changed_input`).
- `SCHEME` id/revision taken from `SCHEMA['x-confidenceScheme']`; digest is still `digest(that object)`.
- `gate()` remaps config-window `Denied` to `Denied("Read denied")` (`test_uniform_read_denial_when_config_expired`).
- `encode()` cap 8 MiB (`test_json_size_bound`). Host preparse remains host-side.
- `validate_snapshot` checks `recordType/path`, `subjectId == dimension:provenance-register`, `snapshotDigest`, `previousSnapshotDigest`, `supersedes` (`test_snapshot_digest_and_predecessor`). Native V3 stays separate.
- Example minting uses `urn:synthetic:dimension:{startup,group,ai-team}`. Parent `sourceUrl` is under `.../enterprise-assertion-provenance/versions/0.1.0/upstream/wm-xct-012-provenance/`, not the parent’s own publication URL.
- Runtime identity remains `vr.profile.enterprise-assertion-provenance` with “no parent subtype.”

I01–I16 hold under the documented host assumptions (auth, current complete root/config, receipt clock, no concurrent mutation). `view` still emits `truth: "not-evaluated"` and `permissions: "not-inferred"`. Review still does not promote `inferred` → `observed`. Reader gate still runs before ledger/claim/`knownAt`.

---

## Remaining defects and limits

### HIGH — host API, not an I-invariant break

**H2. `admit()` still validates the record before the writer grant and still returns the full ledger.**

Order remains: `config_check` → kind → `validate(record)` → grant → `recordedAt==now`. An unauthorized caller who sends a closed-schema violation can still see `Invalid("Schema mismatch")` / `Unknown record type` instead of `Denied("Write denied")` if the host forwards exceptions. The function still returns `candidate` / `previous`.

Spec + AGENTS still require the host to give write-only callers only a receipt or a generic rejection. That wrapper is not in the library. This is the same operational tension as the prior H2; it is **not** a regression of the correction-freeze fix. I11 still holds on `view` (gate first).

### MEDIUM

**M1. Independence is still only an overlap signal.**  
`known-shared-origin` vs `unknown`. The group fixture still shares default `representationDigest` (`sha256:`+`c`×64) and default `originRef`, and only changes `sourceRef`. Distinct files/sources/IDs never prove independence. Easy to over-read; matches the spec.

**M3. Acquisition modes are still tighter than the “at least one” sentence.**  
`file-acquisition` / `live-observation` still require **all** inputs to be matching captured Captures. The contract diff did not touch that prose. Tighter, not looser. No extra epistemic permission.

### LOW — documented bounds

- Unauthorized + malformed `now` / bad config schema still raises `Invalid` inside `config_check`; only `Denied("Access denied")` is remapped to `Read denied`. Trusted-host clock/config.
- `import_snapshot` / `validate_ledger` / `validate_snapshot` do not prove the supplied previous root is the host’s latest. `validate_extension` accepts any valid prefix, including a skipped newer head if that head is not the `previous` argument.
- `validate_snapshot` is companion pin/lineage only. Native V3 remains separately required. acceptance still shows native `valid` + companion `Invalid` on a poisoned nested `representationDigest`.
- 8 MiB is on `encode()` output. `json.loads` in `load()` has no byte cap. Host must preparse (stated).
- Qualitative-reliance scheme only. Process-local digest of the schema sidecar.
- Serial one-record-per-second host clock; no IAM, fetch, PKI, or durable concurrency.
- `context-available` includes `proposed`. Not a rely verdict.
- URIs stored opaque; no normalize/alias merge.
- `whole-object-coverage.yaml` is JSON text under a `.yaml` name. Facets add no rights.
- Structure-tree actions confer no authority; unknown answers stay `insufficient-context`.
- acceptance `publicationStatus: "published"` is still synthetic candidate-installation metadata; `researchAssurance` remains `reviewable-draft`.

---

## Tests traced (not executed)

Claimed `testsRun: 62`. Method count traces as original 48 + 14 new = 62.

**New methods (remediation coverage):**
`test_correct_unchanged_historical_dependencies`, `test_correct_assessment_after_account_correction`, `test_new_account_can_describe_existing_event_with_changed_input`, `test_changed_dependency_pin_requires_current_head`, `test_ascii_calendar_and_newline_strict`, `test_missing_format_support_fails_closed`, `test_fractional_revision_encoding_rejected`, `test_actual_prefix_rewrite_rejected`, `test_cross_revision_self_derivation`, `test_current_capture_failure_visible`, `test_assessment_genesis_semantic_guards`, `test_snapshot_digest_and_predecessor`, `test_uniform_read_denial_when_config_expired`, `test_json_size_bound`.

**Prior suite still present** (truth/permissions, shared vs unknown origin, review does not rewrite inferred, cites default, role split, write deny/grant/rotation, gate-before-malformed-ledger, purpose/expiry, replay retain/rights/conflict, past `knownAt` equality, withdraw/terminal/content freeze, immutable digest, no claim carryover, file≠live, inference≠observed, live target, unverified limitations, unavailable gaps, closed schema, exact pin, self-ref at genesis, cross-scope, stale new link, calendar/clock, prefix truncation, dimension header, numeric label, scheme/reviewer/method, import/migrate, reject-does-not-mutate).

Native harness traced: three profiles; distinct dimension IDs; admission replay through installed companion digest; `validate_snapshot` + digest tamper reject; nested malformed value companion-rejected while native stays valid; truncation rejected by `validate_extension`. Not executed here.

---

## Evidence limits

Static reading of this payload only. No search, fetch, execution, hash recomputation, or artifact mutation. Host authentication, current-root freshness, and concurrency are outside the reference. Synthetic examples only. Missing semantic context is left unknown.

---

**ACCEPT WITH LIMITS** on this exact revised candidate.  
H1 and M4 are remediated. Do not treat the companion as a public service, a truth engine, or a published parent profile. The host must still wrap `admit()` with generic write-only receipts and must still pass `validate_snapshot` plus native V3 against the trusted latest predecessor.
