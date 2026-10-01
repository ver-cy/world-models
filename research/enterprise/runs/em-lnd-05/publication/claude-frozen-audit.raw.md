# Frozen semantic audit — EM-LND-05, candidate revision 2

**Verdict: REVISE.**

The boundary decision (PROFILE over WM-ACT-005 + WM-ACT-029, no new runtime identifier, read-only projection with generated immutable views) is sound and I do not contest it. The reconciliation is nevertheless not admissible as-is: it contains at least two defects that reintroduce the contour's own negative case (double counting) through vectors neither provider examined, one incoherent scenario-discipline field pair, an undeclared outcome/code taxonomy, and unresolved mastership for three of its four allocation and benefit endpoints. Fixtures are unexecuted and, as written, several cannot discriminate the behaviour they claim to test.

---

## 1. Critical findings

### BLOCKING-1 — Deduplication is not selection: baseline and data-date multiplicity double-count money
`costFact.pin` = `[projectId, baselineId, period, currency, priceBase, dataDate]` and `deduplicationKey` = "the complete pin". Deduplication on the complete pin only collapses *the same fact reached by several paths* — the diamond case. It does nothing about legitimately distinct source facts that differ only in `baselineId` or `dataDate`. WM-ACT-005 retains superseded cost baselines deliberately (`a-cost-baseline`, `de-superseded-baseline-ref`) and records `de-actual-cost-to-date` as a data-date series. Under the stated rule, every retained baseline revision and every prior data date for the same project and period survives deduplication and is summed. The portfolio again equals a sum with repeats — the exact negative case — arriving through revision multiplicity instead of path multiplicity. No constraint, code or fixture addresses it.

### BLOCKING-2 — `viewClass` and `scenarioClass` are two fields for one concept, and the discipline rests on their disagreement
`viewClasses` enumerates four values; `DeliveryLandscape.versionAttributes` carries `scenarioClass`; fixtures carry `context.viewClass` *and* `records.scenarioClass`. `scenario-as-actual` triggers refusal by setting `viewClass: authoritative-actuals` alongside `scenarioClass: scenario`, i.e. the refusal is provoked by a field collision rather than by the illegitimate act. `missing-scenario-class` is self-contradictory: it declares `viewClass: authoritative-actuals` in context while asserting `scenarioClass: null`, then expects a required-class refusal. Scenario discipline is the contour's primary safety property and it is currently expressed in two competing fields.

### BLOCKING-3 — Outcome taxonomy is undeclared and conflates blast radii
Fixtures use four outcome kinds (`view-created`, `refusal-record`, `conflict-record`, `omission-record`) and 18 codes. The candidate declares neither the taxonomy nor 16 of the codes. Consequently the scope of a refusal is indeterminate where it matters most: `UNRESOLVED_FINANCIAL_PARENT` must withhold one financial total while the view is still produced (the membership constraint says "yields no financial total"), whereas `SCENARIO_CLASS_REQUIRED` must refuse the whole view. Both are typed `refusal-record`. An implementation cannot derive which.

### BLOCKING-4 — Spec versioning is data-driven, so the projection specification is not stable
`dataDate`, `scenarioClass` and `fiscalPeriod` sit in `DeliveryLandscape.versionAttributes`, identity being `[landscapeId, specVersion]`. Every new data date therefore forces a new specification version, and the constraint set simultaneously places `scenarioClass` and `dataDate` on the *generated view*. The specification/instantiation boundary is crossed in both directions.

### MAJOR-5 — Allocation-axis and benefit endpoints have no master
Constraints assert that every delivery node resolves to a WM-ACT-005 or WM-ACT-029 identity, yet `allocationAxes` declares `Project-Product` and `Project-Team` relations whose non-project endpoints resolve to neither, and no product, team, resource or capacity master is named anywhere. `benefitClaims.master` names **EM-STR-02**, a research contour, not a subject model with a registry id — and two further benefit authorities exist in the frozen dossier (029's `benefit-owner-…-and-attribution-limit`, 005's `de-benefit-claim-ref` for project-accountable benefits) with no precedence rule. `team-overcommit` compares demand against "owner capacity" with no owner model. Three of four axes are mastership-open.

### MAJOR-6 — Benefit facts have no pin and no deduplication key
Cost is pinned and deduplicated; benefit claims are not. "Path multiplicity never multiplies a cost, commitment or benefit fact" is asserted as a constraint with no mechanism behind it for benefits or commitments. The asymmetry is unexplained.

### MAJOR-7 — `fiscalPeriod` and `period` are never reconciled
`financialUniquenessKey` uses `fiscalPeriod`; the cost pin uses `period`. No mapping, no fiscal-calendar pin, no straddle rule. If source periods are monthly and fiscal periods quarterly, the uniqueness constraint and the roll-up are both undetermined, and a project may hold different consolidating parents in different months of one quarter without violating anything stated.

### MAJOR-8 — Uniqueness key omits currency and price base
One consolidating parent per `(projectId, fiscalPeriod, costDimension)` permits facts in EUR and USD, or nominal and real, inside a single consolidating scope. "Money … never summed without an explicit conversion rule" has no corresponding refusal code, and `money-effort-added` tests only EUR + FTE, never EUR + USD. `currency` and `priceBase` also appear as spec version attributes, which silently implies a presentation target and therefore a latent conversion.

### MAJOR-9 — Share bounds constrain sums, not shares; arithmetic is unspecified
`0 <= sum(shares) <= 1` admits a +1.3 share offset by a −0.4 share. Individual shares are unbounded. Separately, `DeliveryView` identity is a digest while share arithmetic is given as ordinary decimals with no numeric domain, scale, rounding or comparison rule — binary floating point makes both the boundary tests and the digest itself implementation-dependent. `explicit-unallocated-remainder` supplies `remainder: 0.1` as an *input*, leaving it unclear whether the remainder is asserted or computed, and what happens when an asserted remainder contradicts `1 − sum`.

### MAJOR-10 — Digest identity has no canonicalization and no manifest field set
"Digest of canonical projection manifest and source pins" names no canonical form, no field ordering, no normalization, no hash algorithm, and does not state whether refusal, omission and conflict records are inside the manifest. If they are outside it, a view that silently dropped a node and a view that recorded the omission are digest-identical. `lifecycle: [created, retained, tombstoned]` combined with `mutable: false` also requires tombstoning to be an entry in an external append-only ledger keyed by digest, which is not stated, and regeneration idempotence (same manifest ⇒ same digest ⇒ no second artifact) is not stated either.

### MAJOR-11 — The no-consolidating-parent case is undefined
The dual-parent conflict is handled. Its mirror — a project with a cost fact and *no* financial-consolidating membership in the period and dimension — appears in neither constraints nor fixtures. Silent exclusion from totals is a reporting defect indistinguishable from correct behaviour.

### MAJOR-12 — Knowledge time was lost in reconciliation
The initial boundary study made `(effective time, knowledge time)` mandatory and defined an as-of-replay view class. The reconciled candidate retains only `dataDate` and drops both. Membership "at most one **active**" is therefore undefined: activity depends on the membership's effective interval (029 owns it; the candidate omits it) evaluated at some knowledge time. Source pins carrying version + digest are a plausible knowledge-time surrogate, but that has to be said, and their completeness made mandatory, or reproducibility after a source correction is unprovable for an artifact asserted to be immutable.

### MINOR-13 — `writes: []` is false as stated
The generator writes `DeliveryView` artifacts. The field means "writes no master records" and should say so.

### MINOR-14 — `DeliveryScope` is a name with no semantics
It carries `kind`, an owner map and `independentIdentity: false`, and nothing else. Either define the projection it denotes or delete the construct and let 005/029 scope be read directly.

### MINOR-15 — Per-root role ambiguity
`roleCardinality` binds one role per assertion but nothing prevents one root from asserting both `financial-consolidating` and `reporting-only` over the same project, period and dimension.

### MINOR-16 — Construct-name drift beyond the frozen contour
The contour freezes `candidate_types` as `DeliveryLandscape` and `DeliveryScope`. The candidate adds `DeliveryView` and `TrackerAdapterBinding`. Both are correctly declared non-identity-bearing, but the extension needs recording as an explicit deviation from the frozen contour rather than passing unremarked.

---

## 2. Required deterministic remediation

Ordered; each is mechanical and closes exactly one finding. Proposed code tokens below are **descriptions of required codes, not allocations** — every token must be allocated by the registry owner.

1. **Split selection from deduplication.** Add a mandatory view-level source-selection rule executed *before* deduplication: for each `(projectId, period, currency, priceBase, costDimension)`, select exactly one `baselineId` by a declared policy (explicit pin, or approved-as-of the view's `dataDate`) and exactly one source `dataDate` (greatest `dataDate ≤ view dataDate`). Non-selected facts are excluded, never summed. Ties, or two baselines approved at the same instant, refuse at fact scope. Then deduplicate on the complete pin. *(BLOCKING-1)*
2. **Unify the class field.** Delete `scenarioClass` from `DeliveryLandscape.versionAttributes`; keep one field on the generated view, valued from the `viewClasses` enum. Restate `scenario-as-actual` as a refused *request* to write scenario-derived values into an actuals-class view. Restate `missing-scenario-class` with the field absent from context. *(BLOCKING-2)*
3. **Declare the outcome taxonomy and close the code enum.** Enumerate the four outcome kinds with definitions, and declare every code with `{outcomeKind, scope ∈ {view, node, fact, claim, commitment}, viewStillProduced: bool}`. Mark all as not-allocated. *(BLOCKING-3)*
4. **Restore the specification/instantiation boundary.** `DeliveryLandscape` versions *parameters and admissible domains* only (`admittedViewClasses`, `admittedCostDimensions`, `rootSet`, `membershipRoleSet`, selection policy, currency/price-base handling rule). `fiscalPeriod`, `dataDate` and the class value become view binding parameters. *(BLOCKING-4)*
5. **Name every endpoint master or refuse.** For each allocation axis and for benefit identity, name the authoritative model and registry id, or declare the axis unresolved and require a node-scope refusal for unresolved axis endpoints. Replace `benefitClaims.master` with a registry-identified subject model and add an explicit precedence rule against 029's attribution-limit element and 005's project-accountable benefit reference. Name the capacity owner for the overcommitment derivation. *(MAJOR-5)*
6. **Pin benefit claims and commitments.** Define a benefit-claim pin (`benefitId, claimantId, claimClass, period, measure, dataDate`) and a commitment pin, each with the same selection-then-deduplication discipline as cost. Add mutual-exclusivity or explicit co-existence semantics for `exclusive-attribution` versus `contribution` on one `(benefit, claimant, period, measure)`, and state whether contribution claims carry a quantity at all. *(MAJOR-6)*
7. **Pin a fiscal calendar.** Declare a total, non-overlapping `period → fiscalPeriod` mapping function with a versioned calendar reference; refuse at fact scope when a source period straddles a fiscal boundary. *(MAJOR-7)*
8. **Extend the uniqueness key or gate the scope.** Either add `currency` and `priceBase` to `financialUniquenessKey`, or add a refusal for heterogeneous currency/price-base inside one consolidating scope absent a named conversion rule with rate source and rate date. Remove the implied presentation currency from the spec. *(MAJOR-8)*
9. **Bound shares individually and fix arithmetic.** `0 ≤ share ≤ 1` per share *and* `0 ≤ Σ ≤ 1` per axis, keyed on the pinned fact identity plus axis (drop the redundant period/dimension re-keying). Mandate exact decimal with a declared scale and rounding mode, exact comparison, no tolerance. Make the unallocated remainder a computed value; refuse when an asserted remainder disagrees. *(MAJOR-9)*
10. **Specify the digest.** Name the canonical serialization (field ordering, number formatting, Unicode and timezone normalization), the hash algorithm, and the exhaustive manifest field list, which must include all refusal, omission and conflict records and all source pins. State regeneration idempotence and move tombstones to an external append-only ledger keyed by digest. *(MAJOR-10)*
11. **Define the zero-consolidating-parent outcome.** Cost excluded from financial totals, surfaced as an explicit unattributed remainder with its own code; never silently dropped. *(MAJOR-11)*
12. **Restore temporal determinism.** Add membership effective intervals and status as referenced 029 attributes; define "active" as effective-interval ∩ fiscalPeriod evaluated against the pinned source versions; state explicitly that complete, immutable source pins are the sole knowledge-time surrogate, or reinstate knowledge time and the as-of-replay class. *(MAJOR-12)*
13. **Housekeeping.** Rename `writes` to a masters-scoped field; define or delete `DeliveryScope`; add a one-assertion-per-`(root, project, fiscalPeriod, costDimension)` rule; record the two added constructs as a declared extension of the frozen `candidate_types`. *(MINOR-13/14/15/16)*
14. **Traceability.** Assign stable ids to all 25 constraints and publish a constraint → code → fixture matrix. There is currently no traceability at all between the constraint prose and the fixture set, which is why several constraints are asserted but unfixtured and several fixtures test codes no constraint mentions.
15. **Remove the residual non-determinism in the constraint text.** "Missing scenarioClass is refused **or unknown**" permits two outcomes; the fixture expects refusal. Narrow to refusal.

---

## 3. Fixture gaps

`executionStatus: not-executed-no-generator`; every identifier, version and digest is a placeholder. Nothing in this pack is verified, and the digest-identity rule is not merely unverified but currently untestable, because no fixture carries an expected digest.

Defective as written: `missing-scenario-class` (contradictory context); `scenario-as-actual` (tests field collision, not the prohibited act); `sum-product-and-team` and `money-effort-added` (the attempt is free prose, not a structured requested projection, so no generator can consume them); `diamond-deduplicated` and `diamond-dual-financial-parent` (membership encoded as path strings such as `X/G/P1` and `G/P1`, which do not distinguish an edge from a path, plus the meta-assertion `sameKey: true` instead of explicit matching `fiscalPeriod` and `costDimension`); `explicit-unallocated-remainder` (remainder as input); `team-overcommit` (demands carry no pins, so "after deduplicating the same commitment fact" is unexercised).

Missing cases, each required: multi-baseline and multi-data-date for one project and period *(BLOCKING-1)*; heterogeneous currency and heterogeneous price base in one consolidating scope; the positive multi-dimension case the constraints assert (one consolidating parent per accounting dimension, never merged); no-consolidating-parent; the nested program-under-portfolio chain, confirming the portfolio consolidates the already-deduplicated program view without re-including the project fact; negative share; share sum exactly 1; share 0 and empty allocation set; membership effective interval partially overlapping the fiscal period; `baseline` and `forecast` view classes, both entirely unfixtured; benefit claim reachable by two paths; mixed claim classes on one benefit; unresolved adapter that *does* carry a source cost fact, to fix whether the fact is omitted or the view refused; view regeneration idempotence and tombstone lifecycle; asserted-vs-computed remainder disagreement; fiscal-period straddle.

The 18 verbatim-duplicated `context` blocks should be hoisted to a shared fixture context with per-case deltas, so that a reviewer can see what each case actually varies.

---

## 4. Identifier discipline

Correct and worth recording: `newRuntimeId: false`; `allocationStatus: not-allocated` with registry-owner note; `LANDSCAPE-PLACEHOLDER` withheld; component, product, team and benefit identity kept reference-only; the candidate's refusal to read the provider comparison as approval of held relation rows.

Defects:

- **`SPEC-V2` in fixtures.** `specVersion` is part of `DeliveryLandscape` identity and is not allocated. Using a concrete-looking token, and one that tracks `candidateRevision: 2`, conflates candidate revision with an unallocated identity component. Must be a placeholder.
- **Host-binding fragment uses `program`.** `vr.wm-act-029#profile/project-program-portfolio-landscape` contains the US spelling while WM-ACT-029's programme/program token normalization is an open hold that explicitly blocks minting artifact identifiers. The token cannot be proposed in this form. The same collision recurs in `DeliveryScope.ownerByRootKind`, whose keys `program` and `portfolio` locally re-encode 029's required profile discriminator instead of referencing it — and 029 holds that a profile change is a supersession with undefined mechanics.
- **Single host binding for a dual-base profile.** The binding is proposed on 029 only, while the profile constrains 005-owned cost-fact pins and selection. Either bind on both bases or state that 005-side constraints separately require 005 registry-owner action. Only one owner action is currently contemplated.
- **Sixteen undeclared codes.** Present only in fixtures, absent from the candidate. See remediation 3.
- **Contour ids used as authorities.** `EM-STR-02`, `EM-WRK-04`, `EM-LND-01`, `EM-LND-10`, `EM-WRK-01` are research-contour identifiers. `EM-STR-02` in particular is cited as a benefit *master*. Contour ids must be labelled neighbour, non-normative, and never occupy a mastership slot.
- **Mixed reference planes.** `bases` carries both `model_id` and `registry_id`; `ownerByRootKind` and `targetModels` use bare `model_id`. Profile-internal references should use registry ids consistently.
- **Key-naming inconsistency inside `benefitClaims`.** `master`, `exclusive-attribution`, `contribution`, `plannedForecastVsRealized` mix a mastership field, two implicit enum members and a discipline rule under inconsistent casing. The claim classes are an enum and should be declared as one, since fixtures already bind `claimClass` to those two values.

No runtime identifier is allocated by this candidate, and this audit allocates none.

---

## 5. Publication decision

**Publication withheld. No promotion, no allocation, no package conversion, no registry mutation, no live verification authorized.**

- The publication ceiling is correctly stated and binds: both bases are `reviewable-draft` with `publishableCanonical: false`, so EM-LND-05 cannot exceed reviewable-draft under any remediation of the findings above.
- **Hard blocker stands:** WM-ACT-029 holds no approved WM-ACT-005 relation rows in the frozen relation ledger. Every membership, traversal, deduplication and consolidation rule in this profile is unverifiable until those rows exist. No amount of fixture work substitutes.
- **Second blocker:** no executable generator exists, so zero fixtures have run and several cannot run as written.
- **Third blocker:** membership roles, the cross-root financial uniqueness key, cross-root deduplication scope and the semantic crosswalk are all unratified on 029. These are the profile's load-bearing constraints and they are additions, not reuse.
- The programme/program normalization hold independently blocks the proposed host-binding token and the root-kind keys.
- ISO 21504, PMI and ISO 42010 remain alignments; no conformance claim is admissible, and 029's own adjudication bars clause-level claims from catalogue abstracts.
- **Provider-review status must be stated precisely.** The two provider studies in this dossier are contour-level boundary opinions. They do not lift WM-ACT-029's single-provider waiver, under which Claude and Grok are recorded as waived for the subject model itself. The candidate should add that hold explicitly alongside the relation-row hold.
- **This audit is not independent external review.** It is one frozen, no-tools semantic pass over a supplied dossier, run exactly once, with no source re-resolution, no execution and no registry access. It cannot discharge the absence-of-external-review hold on either base, and must not be cited as doing so.

Re-audit should be requested only after remediation items 1–4 (the blocking set), item 5 (endpoint mastership), and an executable generator with the fixture corrections above are in place. Items 1 and 2 change what a view *means*, so any fixture pass performed before they land would need to be discarded.
