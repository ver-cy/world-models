**VERDICT: ACCEPT WITH LIMITS**

Scope is only the declared EM-XCT-05 metadata-only research prototype `0.0.0-prototype.2`. This is not publication approval, not a native V3 integration, not a production security boundary, and not an installable Vercy release. R1 studies/audits do not approve these bytes. The full Bundle/Layer/Finding/Question/Artifact/Action package is not in this review set.

Team review (Grok / Harper / Benjamin / Lucas), frozen evidence only. Tests were not executed.

---

## Files actually read

From the supplied bundle. No truncation visible in the pasted bytes.

| File | Banner SHA-256 |
|---|---|
| `README.md` | `578f96e4569c5a1667958b1dce60cea721df1b39f5d420926bfb957209555c3b` |
| `disclosure.py` | `7520a07e95fb852a92ef44da41de4776476e42ea27c5d97fac8c80996057d817` |
| `disclosure.schema.json` | `0f390c6b05c7f333ce46294092299c928c4bf4a98d8ac3ca17864e69b8a14f8f` |
| `test_disclosure.py` | `1fc48790035096913a252034e6b103415034ffd397dbb2ecaacd71b678aa3ad0` |
| `test-results.json` | `4528e7b77b200c17c4034549970eedd49b2d98a7b7303cd1247a91fdc299e7f5` |
| `examples/startup.json` | `7dfd4fef96b8e1f5e863c189df76f3da5cace01b76e7723fd79dcfacd86bc995` |
| `examples/matrix.json` | `c59653ee5b6ee1f689917e421a8e570ba5d6d2fb684c0379fdda3fd314577d3c` |
| `examples/ai.json` | `96cfd0fca7f0d6bde799f66c6c3379072020ef4a3a911f3830b884c1757473c0` |

Not in this set: R1 snapshots/audits, Bundle/Layer/Finding/Question/Artifact/Action tree, five facets, mastership contracts, migration maps, native V3 binding tests.

Hash work here is banner-to-`test-results.json` string agreement only (`codeSha256` and `inputHashes` match the four source banners). Example hashes are not in `inputHashes`. Digests were not recomputed.

---

## Tests (Codex evidence, not rerun)

`test-results.json` reports `status=passed`, `testsRun=78`, `failures=0`, `errors=0`, `jsonschema=4.26.0`, Python 3.12.14. Scope string in that file correctly says these are not an external audit, native integration, or privacy/security conformance.

Listed README behaviors have corresponding tests: three profiles, context/source/schema/shape/classification drift, membership/field/order changes, withdrawn/revoked authority, segregation vs startup self-review, half-open window, conflict, incomplete review set, import idempotency/conflict/history, internal supersession, type preservation, capability refusals, malformed JSON, identifier-alias edges, nested-field rejection, round-trip, prototype.1 refusal.

Gaps that are coverage limits, not hidden passes: multi-hop supersession, withdrawn-pin existence, same-second supersession, snapshotDigest reorder stability, mixed-version pair import beyond seal of prototype.1, inspect-result schema freeze.

---

## No in-contract code defect found

No path in the supplied bytes yields `applicable-review` while a still-eligible rejection is in the supplied+active set with matching authority, in-window, and not segregated self-review. That case is `conflict`.

No digest false-accept, identifier-syntax bypass, skipped completeness check, dropped `notServingAuthorization=true`, or silent prototype.1 import was found.

Empty active set + empty reviews is `insufficient-context` / `no-applicable-review`, not clearance.

---

## Defects vs trusted-host duties

Do not invent controls the prototype explicitly refuses to be.

**Explicit trusted-host duties (not defects):**

- `authorize()` in `disclosure.py` is a host assertion (`capability.dimension` + `inspect is True`; import also needs `record is True`). It is not authentication, a signature, or a user request field. Host must authenticate/authorize the Python call separately.
- Dictionary APIs (`seal`, `validate`, `inspect`, `import_records`) are not wire parsers. Host must use `load()` for serialized input.
- Host must construct the snapshot independently. Code only checks exact agreement of proposal pin, context pins, and members. Echoing the caller proposal as `hostSnapshot` cannot be detected. README already says that echo defeats the integration contract. Fixtures and `examples/*.json` are labeled `synthetic-host-internal-only`.
- Host attests the complete current active-review set. Omitting a live rejection from both `reviews` and `snapshot.activeReviews` makes completeness hold on the remainder. That is host attestation failure, not a reference-checker bug.
- Host must bind qualified ASCII actor strings to distinct people. Comparison is exact; no alias resolution.
- Host must resolve external source/schema/shape/classification/audience/purpose/environment/`priorReleases`/`custodyContext` pins. This reference checks agreement, not truth.
- Host must persist, compare-and-swap, and enforce writer role around `import_records()`. The function is an in-memory transactional merge only.
- Host supplies `now`. `inspect` pins it as `at`.
- Host must not forward `inspect` diagnostics to a recipient. `notServingAuthorization` is always `true`.
- No network, serving, HTTP refusal, destruction, or disposition engine exists here.

**In-scope consistency limits (not false grants):**

1. **Shallow supersession in `inspect` vs graph in `import_records`.** Import resolves `review.body.proposal` and `review.body.supersedes`, checks type, same proposal identity, nondecreasing `reviewedAt` (equal times allowed), and acyclic `(id, revision)` edges. Inspect only raises `Invalid('superseded review still active')` when the *immediate* `supersedes` pin is in `activeReviews`. Multi-hop `A → B → C` with `A` and `C` active and `B` omitted is not caught. README already defers this: implement or precisely defer cross-record supersession and source-binding semantics.
2. **`withdrawnReviews` are pin-shaped attestation echoes.** Shape, bound, uniqueness, and disjointness from active are checked. Existence, prior-active history, and proposal identity are not. The list is copied into the answer.
3. **Snapshot and inspect result are unschematized.** Closed 11-key set + `separateReviewer` bool + `canonical(snapshot)` bounds. `snapshotDigest` is an unversioned diagnostic hash of that dict, not a stored record pin.
4. **`coherent[]` in `validate()` / `exact_strings` covers pin-shaped objects only** (`set(x) == {id, revision, digest}`). The record envelope `id` is not reserved. Two *reference* pins with the same id and different rev/digest still fail.
5. **`Invalid` vs status is not a uniform refusal surface.** Declared: uniform HTTP refusal, timing/existence protection, and serving are not implemented.
6. **Canonical form is local restricted JSON, not RFC 8785/JCS.** Sorted keys, compact separators, UTF-8, no Unicode normalization, list order significant. Claim matches code (`canonical`, `hash_body`).
7. **Input bounds are prototype caps, not a tested DoS guarantee.** Documented. `MAX_BYTES=262144`, depth 20, list/object 128, reviews 64, import combined 128.
8. **`custodyContext` / `priorReleases` equality is not retain/serve/destroy permission.** No disposition-state calculation. Matrix residual-risk text is authored reviewer prose; the validator does not discover subtraction risk.
9. **`method`, `evidence`, and `residualRisk` do not affect applicability.** They ride on the sealed review only.
10. **No mixed-version import or migration maps.** Schema `version` const is `0.0.0-prototype.2`. prototype.1 fails `record shape`. No silent reinterpretation.

---

## Challenge of claims

Held as honest, if restated tightly:

- “Tested research candidate” = Codex 78/0/0 on these hashed bytes, not this review’s run.
- “Not an installable Vercy release” / “reserves no public runtime ID” holds even though `format` is `vercy-disclosure-research`.
- Seal computes integrity and local structure; it does not approve content.
- Import does not persist, authenticate object-specific write role, or enforce review authority at write time.
- Clearance is not serving authorization, privacy proof, or inference prevention.
- Reference checks exact agreement, not truth or completeness of host assertions.
- R1 audits stay on their earlier snapshot.
- Before release: complete the metamodel tree, choose an immutable model version through Vercy’s normal pipeline, test native V3 binding, and implement or defer cross-record supersession and source-binding.

Challenged if read as stronger than the code:

- “Host snapshot must pin the current proposal…” is a *duty*. The function accepts any dict that matches. Echo is a process failure.
- “Complete active review-pin set” is attested, not recovered from a store.
- “Fields are scalar leaves of a closed source schema” is a host attestation. Code checks member/field shape and name syntax, not an external schema compiler.
- Actor exact-match is not a NIST control and not distinct-person proof.

---

## Topic-by-topic anchors

**Identity / digest / time.** `canonical`, `load`, `hash_body`, `instant`, `seal`, `validate`. Digest is SHA-256 over canonical bytes with only the top-level `digest` removed. `type(x) is int` / `type(x) is bool` avoids bool-as-int. `load` rejects duplicate keys, floats, nonfinites, exponents, unsafe integers, bad UTF-8, surrogates. Identifiers are exact scheme-bearing printable ASCII; no URI equivalence. Calendar tokens are whole UTC seconds with `Z`; Feb 30, leap seconds, missing offset, and year 0000 fail. Year 0999 parse is tested.

**Incomplete review sets.** `inspect`: `pins(supplied) != active` → `insufficient-context` / `review-set-incomplete`. Extra hidden active pin and extra supplied record both fail completeness. Host omission from *both* lists is a duty failure.

**Conflicts.** Only counted verdicts conflict (`active-review-disagreement`). Two different identities with the same counted verdict are agreement, not votes. Duplicate identity/revision in one call is `Invalid`.

**Caller authority.** `authorize` then inspect/import. Wrong/missing capability is `Unauthorized('unavailable')` before record diagnostics. Capability extra keys are ignored. `inspect is True` is identity-compared, not truthy `1`.

**Schema / path scope.** Fields are top-level names `^[A-Za-z_][A-Za-z0-9_]{0,63}$`. Nested, wildcard, and path-like names fail. `kind` is scalar-only; `object`/`array` rejected. Code uniqueness (member key, field name, binding id) is stricter than schema `uniqueItems`. Snapshot is not in the schema.

**Source / classification references.** Opaque pins. Per-record coherence: one revision/digest per referenced id. Bindings 1–8, duplicate ids in one field fail. External resolution and “scalar leaf of closed schema” are host attestations.

**Retention boundaries.** No destroy/serve path. `custodyContext` is an opaque pin, including any unresolved hold/schedule conflict. Historical inspect answers are not grants; each answer pins its snapshot and `at`.

**Idempotency.** `import_records`: same `(type, id, revision)` + same digest is idempotent; different digest is `immutable revision conflict`; duplicate already in `existing` is `duplicate stored revision`. Caller list is not mutated on failure (`test_immutable_revision_conflict_transactional`). No live-store CAS.

**Supersession.** Seal rejects self-supersession of the same id+revision even with a different target digest. Import allows a new revision of the same review id to supersede a prior revision; does not deactivate the target; does not edit the host active set. Inspect rejects a still-active immediate target. Chain walk and active-set closure are deferred.

**Migration.** prototype.1 is refused. No upgrade/downgrade/reinterpretation. Future release needs explicit mappings and version dispatch.

---

## Adversarial witnesses

- **W1 Echo.** Copy proposal pin/context/members into `hostSnapshot`. `inspect` can return `applicable-review`. Code cannot tell attestation from echo.
- **W2 Active-set lie.** Drop a still-valid rejection from both `activeReviews` and `reviews`. Remaining clearance can pass. Host attestation failure.
- **W3 Multi-hop supersession.** `A` supersedes `B` supersedes `C`; inspect list is `{A,C}`. Immediate-supersedes ∩ active is empty. No `Invalid`.
- **W4 Phantom withdrawn pin.** Never-imported id, valid pin shape, disjoint from active. Copied into `answer['withdrawn']`.
- **W5 Forged capability.** If the host exposes the function, `authorize` accepts any dict matching dimension + `inspect: True`. Diagnostics leak. Declared.
- **W6 Dict path bypassing `load`.** Pre-parsed float dies in `canonical`. Duplicate keys cannot exist in a Python dict. Wire path still needs `load()`.
- **W7 Envelope-id overlay.** Record `id` reused as a nested pin with a different revision. `seal` succeeds. Two reference pins with that clash still fail.
- **W8 NFC vs NFD** in `residualRisk` (or any string) → different digest. Intentional; no normalization.
- **W9 `now == validTo`.** Exclusive end → ignored / `insufficient-context`. Answer binds `at`.
- **W10 prototype.1 in import.** `validate` / schema const fails. No silent mix.
- **W11 Added member/field/reorder.** New proposal digest; old review pin mismatches → `Invalid('review points to another proposal')`, not a reused clearance.
- **W12 Expired rejection + live clearance.** `applicable-review` with `ignored[]` carrying the negative. Matches the documented profile; persistent objections need another profile.

---

## Minimal fixes

Not blocking this prototype-scope accept.

1. README one-liners: `inspect` checks only immediate `supersedes ∩ active`; withdrawn pins are not existence-checked; pin coherence does not reserve the envelope id.
2. Optional small ancestor walk of supplied `supersedes` links against `activeReviews`.
3. Do not add serving, HTTP uniformity, source resolver, anti-echo detector, or disposition calculation in this artifact.

Before any later release: implement or keep the existing explicit deferral of cross-record supersession and source-binding; freeze snapshot/result schemas if those objects become durable; add migration maps; run an audit on the completed metamodel package.

---

**ACCEPT WITH LIMITS** for local research reuse of these frozen bytes as a metadata-only prototype. Do not publish as Vercy, do not treat `applicable-review` as a serve grant, and do not claim this review covers R1, native V3, or the unfinished metamodel tree.