# Verdict: **ACCEPT WITH LIMITS** (bounded reviewable-draft reference only)

I found no local defect that breaks the core claims: two-type identity, immutable merge, digest binding, exact-pin applicability, active/withdrawn disjointness, verdict conflict, or `notServingAuthorization`. The defects below are small. Three are evidence or doc labelling issues that should be fixed before publication. The rest are for the next code revision, and fixing them will change pinned digests.

This verdict does not grant serving or privacy assurance. It neither confers nor removes the owner's publication authority.

---

## Read scope

I read all 31 supplied files completely, and none were truncated:

- **Reports and harness:** acceptance-results.json, acceptance.py, test-results.json, test_disclosure.py, tool-pins.json
- **Docs:** adoption-limits.md, agent-guide.md, AGENTS.md, bindings/native-v3.md, boundary-decision.md, invariants.md, lifecycle/transitions.md, migration.md, model-fields.md, model-spec.md, README.md, research.md
- **Metadata:** composition.yaml, crosswalk.json, mastership-and-rights.yaml, publication-manifest.draft, requirements.txt, runtime-model.reference.json, source-verification.json, whole-object-coverage.yaml
- **Code and schema:** disclosure.py, disclosure.schema.json, spec.json
- **Examples:** examples/ai.json, examples/matrix.json, examples/startup.json

Two files are referenced but absent: `review.md` (cited by the disclosure.py docstring and by model-spec.md / spec.json `contract`) and `adjacent-model-checks.json` (cited by crosswalk.json `otherNeighbors`).

I compared spec.json's `contract` and `invariants` strings with model-spec.md and invariants.md by reading. They look identical, but I did not compare them byte by byte.

---

## Local defects and contradictory claims

| # | Anchor | Witness | Minimal fix |
|---|---|---|---|
| L1 (code, low) | `disclosure.py:validate_native`, `fact.get('authority')!={'source':writer,'rank':0}` | `authority={'source':WRITER,'rank':False}` is accepted, because Python evaluates `False==0` as true. I don't know whether the V3 envelope rejects a boolean rank. | Add `type(fact['authority'].get('rank')) is int`, or compare `canonical()` bytes. |
| L2 (evidence gap) | `acceptance.py`, mutation `storage-before-assessment` | Setting recordedAt to 2020 also breaks `object_at<=recorded`, because the object is stored at `at`. So the `declared<=recorded` check is never isolated by any executed negative. | Add a case where both the object and fact are recorded at `2026-09-21T10:01:30Z` against the corrected review (reviewedAt 10:02). Also add isolated negatives for validFrom≠recordedAt, unit, validTo, status, `provenance.source`, `obj.state` and `obj.accessClass`. |
| L3 (evidence label) | acceptance-results.json `historicalAndCurrentAnswers` / `clockMeaning`; native-v3.md "preserves an earlier assessment" | Both answers have `at: 2026-09-21T12:00:00Z`. Both snapshots were built at run time (`fixture()` plus a deepcopy), so they are not "preserved". They also describe contradictory states at the same instant: rev1 is active in one, rev2 in the other, even though rev2 was reviewedAt 10:02. | Relabel them as "two synthetic alternative snapshots", or give them distinct `asOf` values (for example 10:01:30 for the old one and later for the current one). |
| L4 (doc contradiction) | crosswalk.json `composition.semanticReferences` | It lists `vr.wm-xct-035`, which has no version or digest. composition.yaml and spec.json give an exact pinned set of five, and the ID forms also differ (`vr.wm-xct-002` vs `WM-XCT-002`). | Move 035 to a `deferredTargets` list and align the ID form. |
| L5 (doc) | crosswalk.json WM-XCT-002 row | `selectedFindingIds: []`, yet `semanticReading` says "selected exact findings/fields read". | State "boundary-only reference, no finding selected", or list the findings. |
| L6 (completeness) | disclosure.py docstring; model-spec.md / spec.json contract; crosswalk.json | `review.md` and `adjacent-model-checks.json` do not exist in the package. | Add both before publication. Neither is covered by the pinned spec, code or crosswalk digests, so this needs no re-pin. |
| L7 (claim precision) | invariants.md #14; native-v3.md "immutable" | The harness itself overwrites a stored fact in place (`paths[-1].write_bytes`) and the V3 validator stays valid. A correctly resealed replacement of an unreferenced leaf revision keeps the same `factId` and passes both `validate_native` and `import_records`. Only an independent snapshot pin detects it. | Reword #14 as holding "within a supplied register". State that at-rest append-only/CAS storage is a host duty. |
| L8 (route vocabulary) | spec.json: every `answer_data` "…remains denied"; DR-ACT06 and DR-ACT21 "Return insufficient-context" | `inspect()` has no "denied" status (it raises `Unauthorized`). It never evaluates scheme comparability or custody conflicts. With equal opaque pins it can return `applicable-review` while a custody hold is unresolved. | For now, add a note in adoption-limits.md. In the next spec revision, mark these as agent/host answer states, not `inspect()` outputs. |
| L9 (lifecycle gap) | `validate_native` requires `obj.state=='active'` | If a host retires a native object, all its historical facts fail nested validation, and full-register import is then blocked. | Document that native objects must stay active (retirement is a snapshot-level change), or define the accepted states. |
| L10 (nits) | model-spec.md; README.md; schema | model-spec says "both record schema constants", but the code checks three, including the snapshot. README presents the catalogue URL as live while the manifest says `candidate-not-published`. The format constant `vercy-disclosure-research` is permanent in 0.1.0 digests. | Wording only. |

---

## Checked and found consistent

- **Two-object identity:** enforced in four places:
  - `import_records` type lock
  - the `inspect` check that a review ID does not collide with the proposal ID
  - `validate_native` checks on objectType and path
  - `native_fact_id` over Dimension, id and revision
- **Time:** all record and snapshot timestamps go through `instant()`, which uses `[0-9]` with a full match. This compensates for jsonschema's Unicode `\d` and for `$` matching before a trailing newline; identifier fields have the same full-match compensation. Validity is half-open, and the four exclusion reasons are distinct and ordered as documented.
- **Digest encoding:** the golden vector matches the documented escaping rules. Subclasses, surrogates, floats, duplicate keys and unsafe integers are rejected.
- **Active, superseded and withdrawn sets:**
  - IDs are unique and active/withdrawn overlap is checked by (id, revision).
  - The supplied reviews must equal the active set.
  - Immediate supersession is refused, including when the digest is forged.
- **Conflict handling:** disagreement returns `conflict`, never a silently chosen winner. Ignored negative verdicts stay visible.
- **Scalar metadata boundaries:** field names are single top-level names, field kinds are scalars, and classification bindings are required (1–8).
- **Pins:** reference coherence holds within a record.
- **Structure:** all five facets are present for both types. There are 24 routes, and the counts match (4 bundles, 8 layers, 24 of each element).
- **Bounds and migration:** honestly stated, including the effective 128-record ceiling and no cross-version path.
- **Envelope vs nested validation:** explicitly separated, and outer validity of an invalid nested fact is demonstrated.
- **Tests:** test_disclosure.py contains exactly 108 test methods, which matches `testsRun`.
- **Hash cross-consistency:** the file-header hashes, the test report input and example hashes, the acceptance `sourceDigests`, and the proposal and rev1 review digests in examples vs acceptance all agree textually.

---

## Explicit trusted-host duties (accepted as declared)

These are declared host responsibilities, not defects:

- **Transitive supersession.** Witness: with C superseding B, which supersedes A, an active set of {A, C} counts A.
- **Snapshot independence.** The fixtures echo the proposal, and this is disclosed.
- **Actor alias binding.** `URN:synthetic:founder` and `urn:synthetic:founder` are compared as different strings, which lets someone bypass segregation. This is disclosed.
- **Clock accuracy.**
- **Complete register and write-path bound.** The native writer does not enforce the 128 limit, so the host must run `import_records` before appending, as the harness does.
- **Authentication and IAM.**
- **Explicit companion calls.** V3 does not dispatch them.
- **Contested generic fact resolution.**

Recommended for a future version: withdrawing a rejection currently yields `applicable-review` with only an unattributed withdrawn pin. Consider adding withdrawal actor/reason pins to the snapshot, and an `ignoredNegative` flag to the answer.

## Deferred domain scope (not demanded)

The following are out of scope for this reference and I am not asking for them:

- classification comparison
- retention and disposition (035/038)
- grant evaluation
- source resolution
- privacy mechanisms
- concurrency
- existing-Dimension migration
- the parent-model publication holds, which remain the parents' responsibility

---

## Unverified scope

- **Nothing executed:** I did not run code or tests, recompute any hashes, or execute any native reports.
- **Toolchain and V3:** I did not verify the pinned composer/skill bytes or the V3 envelope schemas, and I made no inference about their behaviour, including whether rank is integer-typed.
- **jsonschema 4.26.0:** its semantics are assumed from general knowledge.
- **External material:** I did not open external URLs, parent specs or provider studies.
- **Pass results:** the claimed passes rest on Codex-executed reports, not on my execution.
