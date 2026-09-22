Claude responded: EM-XCT-09 R2: Static Delta Audit
Reviewing test coverage for ancestry and cache-path edge cases.

Reviewing test coverage for ancestry and cache-path edge cases.
EM-XCT-09 R2: Static Delta Audit
Scope
Baseline: the complete R1 bodies acknowledged earlier in this conversation (parts 1–10).
Deltas: R2 parts 1–4. Nothing is missing.
Changed files reviewed:
As full JSON values: acceptance-results.json, invariants.json, test-results.json.
As full unified diffs: classification_review.py, test_classification.py, model-spec.md, adoption-limits.md, bindings/native-v3.md, research.md.
spec.json via its two JSON-Patch replacements.
Excluded: the four upstream spec/AGENTS files and the external composer/native-skill code. Those remain unreviewed.
Not done: I executed nothing and computed no hashes. Where I say digests are consistent, I mean the same literal strings appear across the manifest, test results and acceptance results (build 795fae…, evaluator feebd78…, spec 438269…), not that I verified them.
Verdict

ACCEPT WITH LIMITS. No blocker and no regression found.

Closure of R1 defects

B1 (conflicting captures of the same release coordinate): closed.

The snapshot loop now keys every payload by a semantic coordinate: (scheme, version), profile (id, version), assignment (id, revision) or crosswalk (id, version).
It refuses any second payload at the same coordinate whose canonical encoding differs.
The check runs packet-wide, including on unreferenced snapshots.
Re-tracing my R1 counterexample (retired rel-old versus active rel-new, both S/"1") now raises Invalid in the loop, before compile_profile runs. test_conflicting_release_coordinate_across_profiles_is_rejected reproduces that shape.
Captures of the same release under a different version string are distinct releases under the exact-string dialect, so they are not a bypass.

Cached-ancestry bypass: closed.

On a cache hit the code now requires len(stack) + len(cached['ancestry']) <= 8. The uncached path keeps len(stack) < 8.
Trace with base = chain[-2] compiled first: 8 profiles passes (1 + 7); 9 profiles is refused (1 + 8).
A 9-profile chain without a cache hit is refused by the uncached guard.
Self-referential cycles remain impossible, because the parent pin's digest cannot match a digest that includes it.

No regressions from the coordinate check in the shipped examples. All three examples and the fixture helpers use distinct payload IDs and distinct release versions or schemes.

Other adopted items look correct as written:

The duplicate crosswalk-pin guard.
The correction and proposed-assignment notices; notices do not change the top-level outcome.
Concept intervals now report outside-valid-time.
review() validates both the assessment and the combined replay value against the schema and the 1 MiB cap. Schema bounds hold: evidence stays ≤ 64 and alternatives ≤ 512 given the duplicate-pin guard.
The native-v3 text is now accurate: it describes a fact-only validator and states that no authorization is performed.
Nonblocking observations (new or residual)

N1. unsupported is reported as insufficient-context in assignment and migration modes.

A profile with min > 32 sets ready = False.
validate_selection checks ready before anything capacity-specific, so it returns insufficient-context. The emitted question is "provide a conforming source assignment", which no schema-valid assignment (at most 32 values) can ever satisfy.
The top-level outcome also becomes insufficient-context, outranking the PROFILE-CAPACITY unsupported finding.
This is conservative (no false conformance or candidate), but it conflates unsupported with unknown.
Minimal fix: record a capacity_unsupported flag on the compiled profile and return unsupported for it in validate_selection before the ready check.
The same ordering already applied in R1 to incomplete releases, where insufficient-context is correct.

N2. Equal-payload captures under different snapshot IDs bypass the new crosswalk guard.

Coordinate consistency permits identical payloads in distinct capture envelopes, but the crosswalk guard deduplicates by snapshot ID only.
Pinning two captures of the same crosswalk therefore duplicates alternatives and applicable rows.
There is no false candidate, because the set of distinct targets is unchanged, but evidence counts are overstated.
Minimal fix: also refuse repeated payload coordinates among the selected crosswalks.

N3. Profile ancestry compares capture pins, not source coordinates.

Suppose a child names the parent via capture 2 while the packet's baseProfile pins capture 1 of an identical payload.
The baseProfile in target['ancestry'] check then refuses the packet as not a descendant.
This errs toward over-refusal and is safe, but the behaviour should be documented or normalized.

N4. The corrected-revision notice does not stop a migration candidate.

A migration candidate can still be proposed from a selected revision that a captured correction supersedes.
This matches the documented host-selection rule, and the notice makes it visible. The limitation is accepted as stated, not a gate.

N5. Test coverage.

Missing: min > 32 in assignment or migration mode (N1), and the equal-payload duplicate crosswalk case (N2).
test_combined_replay_budget_refuses_without_truncation reaches the cap through specific constructed sizes. I checked it only by static arithmetic and it looks plausible.
Remaining limits specific to R2
Coordinate consistency detects only internal contradictions. It does not authenticate sources, compare different versions, or check that claimed completeness is true.
native_records and replay still accept any self-consistent approval basis. The docs now state this, and grant provenance stays with the host.
The companion still does not validate the object record; that responsibility sits with V3 validation and the host, as now documented.
The author evidence is 60 tests and 3 acceptance runs. It is recorded as author claims only.

This audit grants no publication, installation or host authority.






6 minutes ago