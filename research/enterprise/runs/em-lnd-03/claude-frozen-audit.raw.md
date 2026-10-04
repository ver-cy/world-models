# Frozen Semantic Audit — EM-LND-03

**Verdict: REVISE**

No new identifier and no unsafe construct, but two internal inconsistencies in the reconciliation text must be corrected before even a held reviewable profile is coherent.

## Critical findings

1. **FTE class contradiction (¶5 vs ¶8).** The canonical worked example takes employment-level ratios (0.6 at A, 0.5 at B — WM-ORG-005 facts) and reports the 1.1 total as *allocated supply FTE* from WM-ORG-016. ¶5 forbids exactly this cross-class substitution. Either the example's inputs are assignment allocations, or the output is employment FTE. As written the normative example violates the normative rule.
2. **Headcount naming collision.** ¶4 names "legal headcount"; ¶8 introduces "legal relationship headcount" and "employer headcount". These are two grains (party-scoped vs release-scoped) under three labels. Unnamed or multiply-named aggregates are the precise failure mode ¶5 exists to prevent.
3. **Anchor mastership undeclared.** ¶8 requires cross-employer anchor deduplication; ¶9 forbids emitting anchors. Neither states that the anchor is *derived from* WM-PER-001 identity resolution and non-registrable. Without that, the engine mints a de facto identity key internally — the profile's weakest seam.
4. **Cross-employer disclosure gap.** Consolidated distinct-employed-persons = 1 against relationships = 2 discloses that the person holds employment elsewhere. ¶9 lists affiliation patterns and linkability but does not bind consolidation to an access scope authorizing *both* employers under WM-XCT-002.
5. **No release-level temporal comparability rule.** ¶4 sets time convention per measure; nothing governs combining differently-conventioned measures in one cross-tab or delta.
6. **Population membership of non-employees unstated.** ¶7 excludes contractors from host legal headcount but does not say whether they enter "unique persons".

## Required holds

- H1 — Restate ¶8 with an explicit FTE class label and source object; do not reuse 1.1 across classes.
- H2 — Adopt one canonical headcount name per grain in the measure register; retire the variants.
- H3 — Declare anchors as WM-PER-001-derived, non-registrable, non-emitted, engine-scoped.
- H4 — Require consolidated measures to fail closed absent access to every contributing employer.
- H5 — Add a release-level time-convention reconciliation rule for cross-tabs and deltas.
- H6 — State the unique-persons inclusion predicate for contractors, agency workers and vacancies.

Mastership itself is unambiguous: ¶2 disclaims all masters; Scope masters rules, Landscape masters results, WM-XCT-002/003 master access and disclosure. Pins (¶3) plus fail-closed are sufficient for replay once H1/H2 remove measure ambiguity.

## Scenario result

Correct semantics: one unique person; two active legal employment relationships; employer headcount 1 for A and 1 for B; consolidated distinct employed persons 1; employment FTE 1.1, uncapped across employers. Allocated supply FTE is a separate measure, computed only from WM-ORG-016 assignments, never equated to 1.1 by default. Identity, allocation and non-clipping are preserved; privacy is preserved only with H4.

## Identifier decision

`newRuntimeId=false` upheld. Scope ids and Landscape fingerprints remain non-registrable citation artifacts; no person, party, employment, assignment, position or organization key is created. Conditional on H3, no hidden identifier is introduced. No publication authority granted.
