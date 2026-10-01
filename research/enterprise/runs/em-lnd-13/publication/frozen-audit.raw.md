## Verdict

The disposition is sustained: **PROFILE, no new runtime/model identifier** is the correct call on this evidence, and the three-way agreement (local synthesis, Claude/Grok reconciliation, candidate JSON) is genuine on that point. The candidate is **not ready to freeze as normative**. The failure is not in the reasoning but in transmission: the synthesis carries twelve invariants and the reconciliation adds three decisions, while `constraints` carries eight items — roughly half the operative safety rules (issued-at, report pins, impact classes, freshness, gap classes, stale propagation, findings integrity) exist only in prose and are enforced nowhere. Two bases are unpublished or unallocated yet load-bearing. Fixtures cover 7 cases against ~20 distinct failure modes, and two of the seven have expectations too weak to discriminate.

Material defects below. No canonical completeness, installability or standards-compliance claim is made or supported.

---

### D1 — Projection identity: publication routing and handle scope unenforced

The reconciliation's two identity rules — a published projection takes identity from an existing WM-DAT-008 Data Product instance rather than a new landscape class, and a reusable handle **cannot own lineage edges** — appear in the provider comparison only. Neither the synthesis nor `constraints` carries them, so the central decision of the contour is untested and unstated normatively.

**Remediation:** add both rules verbatim as constraints.

### D2 — Issued-at pinning absent from the normative artifact

The comparison states the reconciled shape "adopts Grok's explicit issued-at snapshot rule," yet `constraints` never mentions issued-at, and the minimal profile shape records `as-of` without it. As-of (data cutoff) and issued-at (projection instant) are collapsed, so two projections over changed sources at the same as-of are indistinguishable and a citation cannot be held to one observed set.

**Remediation:** add issued-at as a required pin distinct from as-of, bound to an immutable observed set.

### D3 — Append-successor rule is not a constraint

Constraint 3 asserts immutability of released definitions and executions but never states the positive rule that corrections and retries append successors (invariant 10). Immutability without a successor path leaves in-place amendment unaddressed rather than prohibited.

**Remediation:** append "corrections and retries append successors; no in-place amendment of a released definition or issued execution."

### D4 — Lineage edge shape: endpoints not version-addressed; inferred edges unmarked

Both providers agreed on "version-addressed lineage," but constraint 4 requires only a *producer or schema* version — nothing forces the edge **endpoints** to resolve to dataset version/partition rather than name. Name-addressed endpoints reintroduce exactly the inference constraint 5 bars. Separately, the synthesis permits low-confidence inferred edges but no rule types them as inferred or bars them from satisfying a perimeter absence claim.

**Remediation:** require both endpoints to be version/partition-addressed; require `captureMethod=inferred` on inference-derived edges and exclude them from absence and comparability determinations.

### D5 — Impact result classes absent

The reconciliation's explicit split (affected definitions vs. affected concrete issues/runs) has no constraint and no fixture, and the acceptance scenario implies two further classes the comparison does not name: affected findings/claims, and unresolved/coverage. A flat impact list would pass the candidate as written.

**Remediation:** add a constraint enumerating four result classes — affected definitions, affected issues/runs, affected findings/claims, unresolved coverage — and forbid returning an unclassified set.

### D6 — Comparability: verdict set and safe default dropped

The synthesis fixes three verdicts and the critical rule that a **missing verdict means non-comparable**; constraint 6 carries neither. It also narrows "unit/code-system version" to "unit," dropping code-system versioning as a facet. Fixture `kpi-version-change` expects "non-comparable **or** restatement" — a disjunctive expectation cannot discriminate, and on a combined formula-plus-population change the required verdict is non-comparable.

**Remediation:** add the three-verdict enumeration plus default-to-non-comparable; restore code-system version to the facet list; make the fixture assert non-comparable.

### D7 — Report pin set and dashboard citability absent from constraints

The pin set (definition, parameters, period, cutoff, as-of, issue time, input versions/partitions/digests, run) is the basis of citability and exists only in prose. The rule that a live dashboard becomes citable only through a frozen snapshot issue is likewise unconstrained and untested.

**Remediation:** add the full pin set as a constraint and add the dashboard-snapshot rule.

### D8 — Completeness perimeter: scope, time bound and edition pin dropped

The comparison requires the perimeter to be closed, **scoped and time-bounded**, and to cover *the exact issued projection*. Constraint 7 says only "closed versioned." As written, a perimeter whose window predates the issued projection would license an absence claim — the realistic failure, and the one the single existing negative fixture does not reach. The perimeter edition itself is also not required to be pinned into the issued projection.

**Remediation:** restate constraint 7 as closed, scoped, time-bounded, edition-pinned, and covering the issued projection's exact observed set.

### D9 — Freshness unconstrained; run-success scope narrowed; crosswalk supersession unhandled

Freshness appears in the viewpoint shape but in no constraint, despite the synthesis defining four evaluated states (schema, classification, cohort/privacy, snapshot). Invariant 9 bars run success as proof of quality, freshness **and** acceptance, but the fixture tests quality only. Nothing states that a superseded WM-XCT-003 crosswalk edition marks an issued projection stale rather than silently re-resolving it — which would mutate a citable projection.

**Remediation:** add a freshness constraint naming the four states; extend the run-success prohibition to freshness and acceptance; add the crosswalk-supersession-marks-stale rule.

### D10 — Stale/incomplete propagation and gap classes unconstrained

Stale-input and incomplete-input propagation exists only as a derived-finding note in the profile shape, and invariant 8's five distinct classes (unknown, zero, not-applicable, missing, suppressed) have no constraint at all — a projection could render suppressed as zero and pass. Fixture `frozen-report-issues` expects that conclusions "**can** become stale"; a permissive expectation asserts nothing.

**Remediation:** add constraints for the five gap classes and for mandatory stale/incomplete marker propagation to dependent findings; change the fixture expectation to *must*.

### D11 — Findings/claims integrity unconstrained

Invariant 11 (findings retain scope, assumptions, defeaters, evidence; association never auto-promotes to causation) has no counterpart in `constraints` and no fixture, despite the profile narrowing WM-DAT-006 specifically to paths terminating in claims.

**Remediation:** add the finding-record requirement, including defeaters, as a constraint.

### D12 — Rights inheritance not pinned at issue time

Constraint 8 covers inheritance, withholding and non-enforcement, but not the reconciliation's "rights stamp": policy version and fingerprint are not required to be pinned into the issued projection. Without that pin, a later policy change retroactively alters what an already-cited projection reveals, defeating both immutability and the withheld-never-absent rule.

**Remediation:** require policy version and fingerprint pinned at issued-at; re-evaluation yields a successor projection, never mutation.

### D13 — Unresolved and unallocated references carried as resolved bases

`bases` lists WM-REC-002 flatly, while `holds` records it as having no published specification; Metric Definition is identifier-unassigned under EM-DAT-05 yet invariant 6 and constraint 6 depend on metric-definition-version identity; WM-DAT-006 perimeter semantics are unreconciled yet constraint 7 depends on a versioned perimeter that base may not supply. Three constraints are therefore unsatisfiable as written.

**Remediation:** partition `bases` into resolved and conditional, move WM-REC-002 to conditional, and mark the metric-facing invariants and constraint 7 as gated on EM-DAT-05 and WM-DAT-006 respectively. Do not mint substitute identifiers.

### D14 — No base-to-master mapping

The synthesis names ten master families (catalog record, data product, dataset/version, distribution, schema/contract version, pipeline definition/deployment/run/attempt, lineage assertion, metric definition version, observation, report definition/issue, analysis method/study, finding/claim) against ten base identifiers, with no stated mapping. From the frozen evidence alone, report issue, pipeline run/attempt, observation and analysis study cannot be traced to any base — so "separate mastership" (constraint 2) is unverifiable.

**Remediation:** add an explicit per-family → base-identifier mapping using only the ten listed identifiers; where no base covers a family, record it as a hold.

### D15 — Holds are stale and inconsistent across artifacts

Candidate `holds` states "Independent Grok review … remain pending" although the provider comparison is present and reconciled, and omits the synthesis's own "No fixtures were run." A reader cannot tell which holds are current.

**Remediation:** sync holds to the frozen state — Grok review complete and reconciled; frozen audit in progress; no fixtures executed.

### D16 — Fixture coverage and expectation strength

Seven cases cover invariants 3, 5, 9 (partially), 12 and the version-successor path. Uncovered: invariants 1, 6, 7, 8, 10, 11, plus issued-at, impact classes, comparability default, perimeter scope/edition, crosswalk supersession, rights pinning — and, most significantly, the contour's own decision (no minted identity, handle owns no edges). No case carries a verdict code or a validation-shape id, so pass/fail is prose-judged; two expectations are hedged (D6, D10). Coverage is unverified in any case, since no fixture has been executed.

**Remediation:** bind every case to a validation shape id and a discrete expected verdict code; replace hedged expectations with *must*; add the cases below.

---

## Exact additional fixtures required

Twenty cases, in `vercy-enterprise-profile-fixtures/v1` form (`id · kind · input → expect`):

1. `projection-mints-identity` · negative · A published landscape projection is assigned a new landscape-class identity → rejected; identity must resolve to an existing WM-DAT-008 Data Product instance.
2. `handle-owns-lineage-edge` · negative · A reusable projection handle is recorded as owner or producer of a lineage edge → rejected.
3. `issued-at-missing` · negative · A projection is cited without issued-at and an immutable observed set → rejected as non-citable.
4. `as-of-versus-issued-at` · positive · Two projections share one as-of but differ in issued-at over changed sources → two distinct citable issued projections; the earlier is not re-resolved.
5. `definition-amended-in-place` · negative · A released metric definition v1 formula is edited in place → rejected; a successor version is required.
6. `retry-alters-issued-report` · negative · A pipeline retry rewrites the pinned inputs of an already-issued report issue → rejected; a successor issue is required.
7. `observation-two-definitions` · negative · One observation is bound to two metric definition versions → rejected.
8. `lineage-endpoint-unversioned` · negative · A lineage edge endpoint is addressed by dataset name only → rejected; endpoints must be version- or partition-addressed.
9. `inferred-edge-supports-absence` · negative · A low-confidence inferred edge set is used to satisfy a completeness-perimeter absence claim → rejected.
10. `impact-result-classes` · positive · Traversal of a v1→v2 metric change → four separately labelled result sets (affected definitions, affected issues/runs, affected findings/claims, unresolved coverage); a flat unclassified list is rejected.
11. `comparability-verdict-missing` · negative · A same-title cluster with no reconciliation verdict is reported comparable → rejected; the default verdict is non-comparable.
12. `code-system-version-change` · negative · Identical formula and population with a changed unit/code-system version is verdicted comparable → rejected; at minimum comparable-with-restatement.
13. `live-dashboard-cited` · negative · A live dashboard is cited as evidence for a claim without a frozen snapshot issue → rejected.
14. `report-pin-incomplete` · negative · A report issue lacking cutoff or input digests is treated as citable or reproducible → rejected.
15. `perimeter-scope-mismatch` · negative · An absence claim is made inside a perimeter whose scope or time window does not cover the issued projection → rejected.
16. `perimeter-edition-unpinned` · negative · An absence claim references a completeness perimeter with no edition pin → rejected.
17. `crosswalk-edition-superseded` · positive · The WM-XCT-003 crosswalk edition is superseded after issue → the issued projection is marked stale; mappings are not silently re-resolved.
18. `run-success-not-freshness-or-acceptance` · negative · A successful run is treated as proof of freshness or of acceptance → rejected (extends the existing quality-only case).
19. `gap-class-collapse` · negative · A projection renders suppressed or not-applicable as zero or missing → rejected; the five classes remain distinct.
20. `stale-input-propagation` · positive · Metric v2 supersedes v1 after a conclusion was pinned to Issue A → the conclusion **must** carry a stale-input marker and its text **must** remain unrewritten.
21. `incomplete-input-propagation` · positive · A missing v2 observation is recorded as a coded gap → the dependent finding **must** carry an incomplete-input marker naming the gap code.
22. `finding-without-scope` · negative · A finding is admitted without scope, assumptions, defeaters and evidence → rejected.
23. `rights-policy-unpinned` · negative · An issued projection omits the policy version and fingerprint → rejected.
24. `rights-relaxation-mutates-issue` · negative · A later policy relaxation reveals a previously withheld segment within the same issued projection → rejected; a successor issue is required.
25. `withheld-recoverable-by-difference` · negative · Two aggregate projections differ such that a withheld segment is recoverable → rejected absent cohort/privacy control binding.
26. `unallocated-metric-reference` · negative · The profile asserts a resolved Metric Definition identifier while EM-DAT-05 is unassigned → rejected; the dependency remains a hold.
27. `unpublished-base-resolved` · negative · WM-REC-002 is treated as a resolved base → rejected; it remains conditional pending publication.
