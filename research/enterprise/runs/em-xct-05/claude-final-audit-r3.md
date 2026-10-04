# Verdict: **ACCEPT WITH LIMITS** (bounded reviewable-draft reference only)

I found no defect that makes a claimed guarantee unsafe or produces a false positive `applicable-review`. There is one real local defect: the byte bounds are inconsistent across record, envelope and snapshot. It fails closed, but it contradicts the documented bounds and should be fixed or documented before anyone relies on near-cap records. The remaining findings are minor evidence, labelling and placement issues.

This verdict covers only the supplied bytes as rendered. It is not a grant to serve source values, not a privacy proof, and it does not confer or remove the owner's publication authority.

---

## A. Local defects

### D1 (moderate, fails closed): the record byte cap is larger than the cap on any envelope that carries the record

- **Anchors:** `disclosure.py` `MAX_BYTES` and `canonical()`; `validate_native()` calls `canonical(fact)`; `validate_snapshot()` calls `canonical(snapshot)`.
- **Problem:** A proposal is admitted by `seal`/`validate`/`import_records` up to 262,144 canonical bytes. However:
  - **Native storage:** The native fact embeds that whole record in `value`, plus roughly 600–800 bytes of envelope. `canonical(fact)` is held to the same 262,144 cap.
  - **Snapshot:** The snapshot repeats `members` and `context`, and adds catalogs (up to 128 × 512-char actors) and review pins. It is also held to the same cap.
- **Witness:**
  1. Grow the members/fields/bindings of a proposal until `len(canonical(proposal))` is about 262,000. The byte cap binds long before 32×64×8 cardinality, as model-spec acknowledges.
  2. `seal()` and `import_records()` succeed.
  3. `validate_native(native_pair(record, at)[1], …)` raises `Invalid('size')`.
  4. `inspect()` raises `Invalid('size')` from `validate_snapshot` once the catalogs and active pins are non-trivial.
- **Effect:** The record is importable but can never be stored natively or inspected. The claim "Input bounds (256 KiB…) are reference constraints" is inaccurate for the native and inspect paths. Nothing tests this.
- **Minimal fix (either option):**
  - (a) Add a `MAX_RECORD_BYTES` (for example 192 KiB) enforced in `validate()`, and keep `MAX_BYTES` for envelopes and snapshots. Document the snapshot/catalog headroom arithmetic.
  - (b) In `validate_native`, canonicalize the fact with `value` replaced by its digest, and bound the record separately. Also state the snapshot cap explicitly.
  - Either way, add one near-cap test for each path.

### D2 (minor): the installed bundle omits normative host duties that exist only in non-installed docs

- **Anchors:** The `release` in `acceptance.py` installs `spec.json`, `AGENTS.md`, `runtime-model.reference.json`, `disclosure.schema.json` and `disclosure.py`.
- **Problem:** Three things are missing from `spec.json`:
  - The "denied ⇒ host refuses; reference raises `Unauthorized`" semantics, which exist only in `adoption-limits.md`. Meanwhile every `answer_data` in `spec.json` says "lack of read authority remains denied".
  - The rule "native objects must stay `active`; withdrawal lives in the snapshot", which exists only in `bindings/native-v3.md` and `adoption-limits.md`.
- **Dangling references in installed files:**
  - The installed `AGENTS.md` says "Read model-spec.md", which is not installed. The content is embedded in `spec.json` as `contract`, but the file name dangles.
  - The `disclosure.py` docstring points to `review.md`, which is also not installed.
- **Fix:** Append both clarifications to the `spec.json` contract, and point `AGENTS.md` to `spec.json#contract`. Alternatively, install `bindings/native-v3.md` and `adoption-limits.md` as descriptors.

### D3 (minor): acceptance report fields are hard-coded, not measured

- **Anchor:** `acceptance.py` `reports.append` sets `'objects':2`, `'immutableRevisionFacts':3`, `'sameVersionRoundtrip':True` and `'installedCompanionImportReplay':True`. The top-level `'failed':0` is also hard-coded.
- **Mitigation:** The two booleans are guarded by earlier `require()` calls, the counts are corroborated by the native validator's `counts`, and any failure aborts before a report is written.
- **Problem:** `failed` is structural, not a count.
- **Fix:** Emit `len(objects)` and `len(paths)`, and document that `failed` is always 0 because failures abort the run.

### D4 (minor): crosswalk evidence dating and labels are inconsistent

- **Timestamps:** `crosswalk.json` (`checkedAt` 20:48:36) asserts `fullSpecificationBytesCompared: true` for all five parents. The dated byte/parse stage is `adjacent-model-checks.json#exactFiveParentChecks.checkedAt` at 22:06:03.
- **Unsupported metadata:** Crosswalk rows for WM-XCT-002 and WM-XCT-003 assert `status`, `installable` and `researchAssurance`. No supplied evidence supports these, because the initial `models` reconnaissance omits 002 and 003, and `exactFiveParentChecks` records no status fields.
- **Label drift:** The row `relation` for 003, 020, 004 and 012 is `"overlap"`, while `composition.yaml`, `spec.json` and crosswalk `composition` use `selected-semantic-overlap-not-subtype`. The WM-XCT-002 label is consistent everywhere.
- **Fix:** Cite `exactFiveParentChecks` for byte evidence, mark the 002/003 catalogue metadata as asserted, and align the row labels.

### D5 (minor): some negative evidence is missing

No tests cover:
- the `conflicting withdrawn revision` branch (same id/revision, different digest in `withdrawnReviews`);
- the import `record bounds` (>128);
- `review set` >64;
- `proposal scope`;
- the D1 near-cap cases.

The acknowledged gaps (a digest-consistent cycle, and native tests only in acceptance) are fine as documented.

---

## B. Checks that hold (static reasoning)

- **Two-object identity:**
  - `import_records` rejects an identity whose type changes.
  - `inspect` rejects `r['id']==proposal['id']`.
  - `validate_native` binds `objectId` and `objectType` to the type, so one native object cannot carry both types.
- **Immutable revisions:**
  - Same (type, id, revision) with a different digest is rejected.
  - Exact replay is idempotent.
  - A duplicate stored revision is rejected.
  - A failed merge does not mutate the caller's list (deepcopy).
  - `native_fact_id` = H(dimension, id, revision); the fact ID mutation is rejected.
- **Time:**
  - Timestamps are strict `[0-9]` full-match UTC seconds. This correctly compensates for the schema's Unicode `\d` and `$`-before-newline behaviour.
  - Review ordering is enforced as `reviewedAt ≤ validFrom < validTo`.
  - Validity is half-open; the start-inclusive and end-exclusive cases are tested.
  - The distinct exclusion reasons `future-assessment`, `not-yet-valid` and `expired` are all tested.
  - `asOf == now` is enforced.
  - Native ordering is `object ≤ receipt ≤ now` and `declared ≤ receipt`. The isolated negative really isolates the assessment check: the object and receipt are at 10:01:30, the assessment at 10:02:00, and the error string is asserted.
- **Digest encoding:**
  - `json.dumps(ensure_ascii=False, sort_keys=True, separators)` matches the documented escapes: lowercase `\u00xx`, DEL and U+2028 literal, code-point key order.
  - Container and str subclasses are rejected.
  - Integers are bounded to ±(2⁵³−1).
  - The `load()` duplicate-key, float, NaN, BOM and invalid-UTF-8 paths are sound.
  - Not JCS, as stated.
- **Active, superseded and withdrawn sets:**
  - At most one active revision per id.
  - Active and withdrawn sets must be disjoint by (id, revision).
  - The supplied review set must equal the active set.
  - An immediate superseded target that is still active is rejected, with a digest-coherence check.
  - Transitive deactivation is correctly declared a host duty.
- **Conflict and mastership:** Disagreeing eligible verdicts return `conflict`. Ignored negatives stay visible. `mastership-and-rights.yaml` is consistent with the code.
- **Scalar metadata boundary:** There is no payload field. Field names are top-level only and `kind` is scalar. Scalar truth is a host attestation, as stated.
- **Exact pins:**
  - Reference coherence holds per record.
  - Context and members are compared by exact equality.
  - `spec.json`, `composition.yaml`, `crosswalk.json#composition` and `adjacent-model-checks.json` carry the same five version/digest pairs.
  - The hash strings cited in `acceptance-results.json#sourceDigests` and `test-results.json` textually match the file headers.
  - The example digests match the counted pins in acceptance.
- **Five facets:** Both types cover all five canonical facets in `whole-object-coverage.yaml`.
- **24 question routes:** The statistics (4/8/24/24/24/24) match the tree. DR-ACT06 and DR-ACT21 now carry the "inspect() does not perform this check" caveat inside `spec.json`.
- **External policy, classification and custody:** These are opaque pins. WM-XCT-035 is deferred, 038 is a todo, and 005 is legacy. There is no executable delegation. `custodyContext` equality is explicitly not a disposition decision, and `applicable-review` is not claimed to settle a hold.
- **Bounds and migration:** The 128-record whole-register ceiling and the refusal of prototype versions are honestly stated. The version guard is unconditional `RuntimeError` and is tested under `-O`.
- **V3 envelope versus nested validation:** Acceptance mutates the actual stored file, shows the outer V3 validator reports `valid` with no errors, shows the companion rejects it, then restores the file. The 22 negatives per profile match the listed labels. The `boolean-authority-rank` negative is caught correctly: `{'rank':False} == {'rank':0}` in Python, and the explicit `type(...) is int` check is what rejects it.
- **Test count:** I counted 108 `test_` methods, which matches `testsRun`.

## C. Explicit host duties and deferred scope (not defects)

These are correctly disclaimed:
- authentication, IAM and grant evaluation;
- source and pin resolution;
- snapshot completeness;
- actor-to-person binding;
- clock correctness;
- CAS and append-only storage at rest;
- transitive supersession deactivation;
- classification comparability;
- custody, retention and disposal;
- privacy mechanisms;
- automatic V3 dispatch;
- existing-Dimension migration.

The `published` value in the acceptance fixture is scoped as a fixture lifecycle value. `publication-manifest.draft` says `candidate-not-published`. The constructed 10:01:30 and 12:00:00 snapshots are disclosed as not being real history. Those historical answers use records natively stored at 22:06, which is acceptable only because this is disclosed.

## D. Scope of this review

- **Files read:** all 33 supplied files, completely, with no truncation observed.
  - `acceptance-results.json`, `acceptance.py`, `adjacent-model-checks.json`, `adoption-limits.md`
  - `agent-guide.md`, `AGENTS.md`, `bindings/native-v3.md`, `boundary-decision.md`
  - `composition.yaml`, `crosswalk.json`, `disclosure.py`, `disclosure.schema.json`
  - `examples/{ai,matrix,startup}.json`, `invariants.md`, `lifecycle/transitions.md`, `mastership-and-rights.yaml`
  - `migration.md`, `model-fields.md`, `model-spec.md`, `publication-manifest.draft`
  - `README.md`, `requirements.txt`, `research.md`, `review.md`
  - `runtime-model.reference.json`, `source-verification.json`, `spec.json`, `test-results.json`
  - `test_disclosure.py`, `tool-pins.json`, `whole-object-coverage.yaml`
- **Not verified by me:**
  - I recomputed no hashes; I only cross-checked hash strings textually between files.
  - I executed no code. The test and acceptance results are Codex evidence.
  - I did not verify the byte-level identity of `spec.json#contract` with `model-spec.md`; they are visually identical.
  - I have no knowledge of the pinned composer/skill behaviour or bytes, or of the V3 validator semantics.
  - I did not read the parent specifications or check any external URLs.
  - My reasoning assumes CPython `re`/`json` and jsonschema 4.26 behave as I described.
- **Not relied on:** The prior verdicts summarized in `review.md` are unverifiable. I did not rely on them.
