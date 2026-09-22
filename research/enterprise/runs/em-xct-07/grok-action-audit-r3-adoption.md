## Method and input completeness

**Method.** Static comparison of this supplement to the already-reconstructed R3 implementation (`action_bundle.py` 9/9, schema, tests, installer, `spec.json`) and to the prior implementation verdict. No tools, no execution, no raw-hash verification of displayed text.

**Fragments actually seen**

| File | Claimed | Seen | Concatenable? |
|---|---|---|---|
| `README.md` | 2 | 2 | Yes (`m` / `andatory`) |
| `model-spec.md` | 4 | 4 | Yes |
| `adoption-limits.md` | 1 | 1 | Yes |
| `requirements.txt` | 1 | 1 | Yes (`jsonschema==4.26.0`) |
| `model-fields.md` | 7 | 7 | Yes (mid-token splits) |
| `bindings/native-v3.md` | 1 | 1 | Yes |
| `publication-addendum-r3.md` | 2 | 2 | Yes (`pa` / `rtially`) |

No fragment uses ellipses or a missing banner. **Not INPUT INCOMPLETE** for the files this supplement claims.

Other originally hash-listed companions (`whole-object-coverage.yaml`, `mastership-and-rights.yaml`, `composition.yaml`, `invariants.md`, comparison notes) are outside this packet; they are not required to complete *this* adoption/addendum review.

---

## Consistency with frozen spec/code

Narrative in `model-spec.md` matches the `spec.json` scope text already checked against the executor/history/native bodies: dual exact scopes, withheld disclosure, pending denial vs denied committed replay, expiry only on dispatch/cancel, retired-key dispatch/lookup without a new try, observe withheld when retired, one local label replacement, 10k caps and policy row 9999, caller projections omit `sequence`/`controlSequence`, `verify_export` is internal closure not authenticity.

`model-fields.md` closed shapes and end-anchored ID/token/hash/URI patterns match `build_schema.py` / `action.schema.json`. Receipt `afterRevision = beforeRevision+1` matches `dispatch`. Event `kind` payloads match `PAYLOADS`.

`requirements.txt` matches README’s pinned `jsonschema==4.26.0`. Admin vs caller surface in README matches the code (`create` / `set_policy` / `add_*` / `retire_*` / `snapshot` vs `dispatch` / `lookup` / `cancel` / `observe`).

**Non-contradictory tightness (not a code defect):** README’s “each attempt requires current execute permission” is coarser than `dispatch`, which writes delivery+try for any remaining right and returns `current-execution-denied` when execute is absent. Spec, model-spec, and the addendum state the precise endpoint rules.

**Addendum claims that match code, not future work:**
- Shared event budget; one right can exhaust it; no quotas.
- `cancel` on a retired key returns `key-retired` + retained receipt to a reader and writes no event; `observe` on retired is withheld.
- Receipt projection includes `beforeLabels`/`afterLabels` of the shared resource.
- History checks per-table times and event order; it does **not** enforce one interleaved monotonic clock across all admin tables. That is a real validator limit, correctly labeled as such rather than as a new check that exists now.
- Nine-file installer does not install `review.json` or this addendum.
- 69+69 is the same suite twice; SQL-seeded 10k rows are not 10k API calls; newline-on-intent is not independently discriminating; generated-ID collision and cross-table backdating lack dedicated tests.

Do not treat the “Further work” list (stronger cross-table clocks, extra edge tests, parse oversized-integer normalization, multi-cut native, quotas) as present behavior.

---

## Publication posture and required disclosures

The documents **do not** promote `candidate` / `simulationOnly` to published. README defers disposition to `review.json`. `bindings/native-v3.md` and the addendum say the fixture lock is not publication, candidate URLs must not replace pinned bytes, and WM-XCT-040 composition is still unsupported.

Required themes are explicit in README + `adoption-limits.md` + addendum:

- finite 10k / ~3,333 pending / ~2,500 first-commit budget; host rate/admission is mandatory and absent;
- host authentication, standing, time, isolation, continuity;
- limited caller projections vs privileged archives;
- archive validators ≠ authenticity or latest cut;
- test and validator gaps (backdated admin row, hardware, timing, some R3 edges);
- no erasure, no distributed exactly-once, no mandate registry.

---

## Remaining release blockers vs limits

No **new implementation blocker** appears from these texts. They describe the same bounded fixture already reviewed.

**Verdict for the candidate WITH this addendum: accept-with-explicit-limits.**

Conditions that stay outside the code and must travel with any package:

1. Ship the addendum and `review.json` with the full review set; they are not among the nine installed Dimension assets.
2. Keep the lock `candidate` / `simulationOnly` until a separate `profile-manifest.json` / `review.json` decision.
3. Do not read archive pass + matching epoch as restore-to-dispatch.
4. Treat receipt label disclosure and non-global admin clocks as accepted host/disclosure limits, not as fixed confidentiality or history-authenticity properties.
5. Acknowledged missing tests and validator tightening remain **future pinned revisions**, not silent claims about this freeze.

No publication authority is given or implied.