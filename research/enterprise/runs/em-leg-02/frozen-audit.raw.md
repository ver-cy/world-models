# Frozen semantic audit — EM-LEG-02

## Verdict

**Conditional hold — not publishable.** The reconciled decision (no new model/runtime ID, WM-POL-001 as sole identity master, WM-ACT-034 profile, external jurisdiction reference) is semantically sound and internally consistent across the three artifacts. The defects are not in the disposition; they are in **transmission loss** between `local-evidence.md` / `provider-comparison.md` and `profile-candidate.json`, and in **fixture coverage**: 12 invariants, 7 cases, roughly half the invariants untested.

## Defects

**D1 — Grok's four strengthenings are not in the profile constraints.** `provider-comparison.md` records commencement as provision-scoped (not stored once on NormVersion), pairwise distinctness including assessment facts-as-of and performed-at, immutability of issued assessment pins with explicit named supersession only, and four separate claims. None appear as constraints. The profile is weaker than the decision it encodes.

**D2 — Time-axis constraint is under-specified.** The constraint lists six axes but omits facts-as-of and performed-at, which `local-evidence.md` treats as assessment-owned and distinct from norm axes. Nothing forbids a single NormVersion-level commencement date; `future-amendment` only implies provision scoping ("effective for each provision and time").

**D3 — Exception / derogation / exemption / transition separation is absent from the profile.** Invariants 9 and 10 have no corresponding constraint and **zero** fixtures. The rejections stated in the synthesis (boolean exemption flag, free-text applicability basis, expiry mutating the norm version, non-derogable floors) are unexecutable.

**D4 — Citation dropped from the four-claim separation.** The constraint reads "Applicability, obligation and compliance remain separate claims" — three of four. Grok's "applicability must not instantiate a duty" and "compliance must not be stored on the assessment" are unrepresented; only the reporting-level inference is tested.

**D5 — Assessment immutability and supersession are untested.** Invariant 8 (same accountable series and equivalent pinned inputs) and invariant 6 (indeterminate/disputed first-class) have no fixture. `majority-resolution` covers only implicit merge.

**D6 — Jurisdiction has no executable contract.** "A bare jurisdiction code is insufficient" and the key-as-of contract are asserted in prose and deferred to a hold; no negative fixture rejects a bare code, and no fixture exercises overlap or extraterritorial connecting factors.

**D7 — Unexplained bases.** `WM-XCT-009` and `WM-XCT-010` appear in `bases` with no constraint, no fixture and no mention in either narrative artifact. Their mastership contribution is undetermined.

**D8 — Provenance contradiction inside the frozen set.** `provider-comparison.md` documents a completed Grok review; `profile-candidate.json` holds list "Independent Grok review … pending"; `local-evidence.md` holds cite a "single-provider" gap. One of these is stale. Not resolvable from the frozen inputs.

**D9 — Weak identity negative.** Invariant 2 names citation text, URL, title, date and hash; `url-as-norm-id` tests only URL.

## Minimal remediation

1. Add four constraints mirroring Grok: provision-scoped commencement; eight pairwise-distinct temporal axes (six legal + facts-as-of + performed-at); issued pins immutable, replaceable only by explicit named supersession within the same accountable series; citation / applicability / obligation / compliance as four claims.
2. Add one constraint for exception / derogation / exemption / transition separation, carrying invariants 9–10.
3. Restate the jurisdiction hold as an enforceable key-as-of reference contract, still without allocating an identifier.
4. Either justify `WM-XCT-009` / `WM-XCT-010` with constraints or remove them from `bases`.
5. Reconcile D8 and correct whichever artifact is stale.
6. Add a per-case field binding each fixture to the invariant and constraint it exercises.

## Required fixtures

Negative: `normversion-single-commencement`; `assessment-pin-mutation`; `cross-series-supersession`; `boolean-exemption-flag`; `exemption-expiry-mutates-norm`; `bare-jurisdiction-code`; `applicability-instantiates-duty`; `compliance-stored-on-assessment`; `hash-as-norm-id`; `deadline-from-publication-date`; `derogation-without-enabling-authority`.

Positive: `indeterminate-conclusion`; `disputed-conclusion-with-deciding-authority`; `repealed-version-remains-citable`; `non-derogable-floor-survives-derogation`; `facts-as-of-differs-from-performed-at`; `overlapping-jurisdiction-hierarchy`.

## Publication disposition

Hold. Clear D1–D4, D7 and D9 plus the corresponding fixtures for an internal reviewable draft. D5, D6 and D8, together with the pre-existing base-model gaps (relation ledger, immutable source pins, jurisdiction master binding, specialist review of multilingual authenticity and treaty commencement), gate any canonical or installable claim.
