# Frozen Semantic Audit — EM-PEO-03 (Competencies and Qualifications)

**Auditor:** single independent frozen auditor. Sources: the frozen dossier only. No external facts, no new identifiers.

---

## 1. Verdict

**REVISE.**

The architecture is sound and the boundary discipline is unusually strong — the definition/holding split, the mapping-is-not-identity rule, the current-as-query rule and the no-allocation posture are all correct and should survive revision unchanged. The dossier is nonetheless not acceptable as frozen, for four structural reasons, each of which alone would collapse a required distinction:

- `ScaleLevel` does not exist as an object, yet `levelRef`, `sourceLevelRef` and `targetLevelRef` are required fields in two models. The entire level layer is dangling.
- `expired` and `revalidated` are stored assertion statuses, which directly contradicts the model's own rule that currency is derived at an as-of instant and never stored.
- Revocation and withdrawal carry no effective time and no retroactivity scope, so no as-of query over supporting artifacts can be computed correctly.
- `personRef`, `asserterRef`, `authorityRef` and `ownerRef` have no mastering model anywhere in the set, and no hold records that absence.

Add to that one fixture that the schema cannot satisfy (`deprecated-successor` requires two successors against a singular `successorConceptRef`), and the freeze is premature.

---

## 2. Minimum model set and the no-allocation decision

**Minimum model set: CONFIRMED IN SHAPE, REJECTED AS COMPLETE.**

Confirmed as correct decomposition:

- **WM-PER-009 completed definition-only** — correct. A scheme-mastered concept has identity, lifecycle and authority independent of every holding; folding levels or holdings in would destroy the import/mastership rule.
- **Proficiency Scale as a separate new model** — confirmed. It passes the identity test independently: different mastership (scale authority ≠ scheme authority), reuse across many concepts and across assessment methods, and its own version lineage. Nesting it inside WM-PER-009 would make every scale change a scheme release and would make cross-scheme scale reuse impossible.
- **Person Capability Assertion as a separate new model** — confirmed. It is the only object with a person subject; keeping it out of both WM-PER-009 and WM-ACT-034 is what prevents definition-holding collapse and act-claim collapse. Its lifecycle (supersession, revocation, decay) is genuinely independent of both.
- **Reuse of WM-ACT-034, WM-PER-008, WM-XCT-017, WM-PER-013, WM-ORG-004 without new identifiers** — confirmed. None of these needs a sibling; the competency-specific surface is a profile, not a model.

Rejected as complete — three named gaps:

1. **No party/person mastership target.** `personRef`, `asserterRef`, `authorityRef`, `ownerRef` point nowhere. Either the person and organization models must be named in the `references` lists, or a hold must state that person/party mastership is unassigned and every such ref is unresolvable. As frozen, the set silently assumes a model it does not name.
2. **The WM-ACT-034 competency-assessment profile is asserted in prose only.** The provider comparison names it; the dossier contains no profile object. That profile is where result-to-level binding and non-level outcomes must live. Until it is written, the set has no surface on which an assessment result becomes a levelled claim, and the `missing-not-zero` and `multiple-methods-scales` fixtures have no host.
3. **No delegate target for course/learning activity.** Every model *excludes* course completion, but nothing in the set *owns* it. An exclusion with no delegate is an unresolved boundary, not a closed one.

**No new identifier allocated now: CONFIRMED.**

This is the right call and is internally consistent: WM-PER-009's registry record is recorded as missing, no approved relation rows exist, and both candidates are explicitly `allocationState: unassigned` with null identifiers. Allocating against an unverified registry state would create exactly the kind of identifier debt this contour is meant to avoid.

One condition attaches. WM-PER-009's `delegates` block delegates to "an identifier-unassigned Proficiency Scale candidate" and "an identifier-unassigned Person Capability Assertion candidate" — by prose, not by address. A reserved completion whose delegations are unaddressable is not reviewable. Assign each candidate a stable pre-allocation slug scoped to this contour (e.g. `candidate:EM-PEO-03/proficiency-scale`, `candidate:EM-PEO-03/person-capability-assertion`), use it in every delegate and reference, and record that the slug is a review handle that carries no registry claim and must be rewritten on allocation.

---

## 3–4. Defects, remediation, fixture expectations

Each defect states the collapse it enables, the exact remediation, and one fixture expectation.

### A. Definition identity and lineage (WM-PER-009)

**D1 — `conceptType` is outside identity.**
*Collapse:* skill/competency. Identity `(schemeId, releaseId, conceptId)` does not carry type, so a release can re-issue the same code with a flipped type and every historical reference silently changes meaning.
*Remediation:* declare `conceptType` immutable across a concept lineage; add invariant "conceptType is fixed at first issue; a type change requires a new conceptId plus a mapping, never an in-place edit."
*Fixture:* `concept-type-immutable` (negative) — release r3 re-issues `C-1` with `conceptType` changed from `skill` to `competency`; rejected, migration path is new code plus mapping.

**D2 — no stable lineage key across releases.**
*Collapse:* history. With `releaseId` inside identity and no declared lineage key, "the same concept in r1 and r3" is not expressible, so deprecation, successors and pinned-release resolution have no anchor.
*Remediation:* declare `(schemeId, conceptId)` as the scheme-local stable code and `(schemeId, conceptId, releaseId)` as the version-pinned address; require `conceptId` unique per scheme across all releases and never reused.
*Fixture:* `lineage-across-releases` (positive) — `C-1` in r1, r2, r3 resolves as one lineage with three pinned versions and never merges with `C-2`.

**D3 — singular `successorConceptRef` cannot express a split.**
*Collapse:* history, definition. The `deprecated-successor` fixture demands two narrower successors; the schema permits one.
*Remediation:* replace with `successorConceptRefs[]`, each carrying `relationKind ∈ {replaced-by, split-into, merged-into}` and `guidanceOnly: true`; add invariant "successor guidance never re-points existing references and never implies equivalence."
*Fixture:* `deprecated-split-two-successors` (positive) — one deprecated concept, two successor refs, both resolvable; a finalized assessment pinned to the deprecated version still resolves to it.

**D4 — terminal states carry no timestamps and no resolvability guarantee.**
*Collapse:* history. `deprecated`, `retired`, `withdrawn` exist with `deprecatedAt` optional, no `retiredAt`, and no rule that withdrawn releases remain readable.
*Remediation:* require `deprecatedAt` when status is deprecated and `retiredAt` when retired; add invariant "deprecated, retired, superseded and withdrawn concepts, releases, compositions and mappings remain permanently resolvable; withdrawal marks not-for-new-use, never deletion."
*Fixture:* `withdrawn-release-resolvable` (positive) — a withdrawn release still resolves for a pinned historical assessment and is flagged not-for-new-use.

**D5 — issued releases are never declared immutable.**
*Collapse:* definition, history. `contentDigest` is required but no invariant binds it; only the operation prose says "immutable."
*Remediation:* add invariant "an issued release is immutable; any change requires a new `releaseId` with `supersedesReleaseId`; `contentDigest` covers all concepts, labels, definitions and compositions in the release and is verified on read; a digest mismatch is an error, never a silent repair."
*Fixture:* `issued-release-immutable` (negative) — a label edit inside an issued release is rejected; a tampered payload surfaces a digest mismatch rather than resolving.

**D6 — `version` and `releaseId` relationship undefined.**
*Collapse:* definition. A required `version` field alongside an identifying `releaseId` invites references pinned by version string.
*Remediation:* define `version` as a non-identifying human-readable label; add invariant "a version label never substitutes for `releaseId` in any reference."
*Fixture:* `version-label-not-a-ref` (negative) — a reference pinned by `"v2"` alone is rejected as unresolvable.

**D7 — labels have no language-tag discipline.**
*Collapse:* definition, mapping. `preferredLabels` is required but multiplicity per language is unconstrained, so a scheme can carry two competing preferred labels in one language and cross-scheme label matching becomes noisier than the mapping rule assumes.
*Remediation:* require a BCP-47 tag on every label; add invariant "at most one preferred label per language tag; an untagged label is invalid; alternative labels are never identity and never mapping evidence on their own."
*Fixture:* `two-preferred-labels-same-language` (negative) — rejected.

**D8 — `conceptTypes` omits knowledge and behaviour.**
*Collapse:* definition. `compose-competency` composes "knowledge skill and behaviour references" against a vocabulary of `[skill, competency]` only.
*Remediation:* choose one — extend `conceptTypes` to `[skill, competency, knowledge, behaviour]`, or restate the operation as composing scheme concepts of any declared type. Add invariant "composition components are version-pinned concept refs within a declared scheme release."
*Fixture:* `composition-components-pinned` (negative) — a `componentRef` lacking `releaseId` is rejected.

**D9 — `CompetencyComposition` has a required `status` and no lifecycle.**
*Collapse:* history. A status with no vocabulary and no supersession path means composition changes overwrite.
*Remediation:* add lifecycle `[draft, issued, superseded, withdrawn]` and `supersedesCompositionId`; add invariant "superseded compositions remain resolvable and previously pinned references are never re-pointed."
*Fixture:* `composition-supersede` (positive) — a revised composition creates a successor; the predecessor and everything pinned to it still resolve.

**D10 — `evidenceRefs` on scheme-level objects is unconstrained.**
*Collapse:* privacy. `CompetencyComposition` and `ConceptMapping` accept `evidenceRefs` with no restriction, so person-level assessment evidence can be attached to a shareable, scheme-scoped, digest-published object.
*Remediation:* add invariant "scheme-level `evidenceRefs` reference only authority, provenance or methodological sources; a reference to person data, an assessment result or an assertion is invalid at definition scope."
*Fixture:* `no-person-evidence-on-definition` (negative) — a mapping citing a person's assessment result as justification is rejected.

### B. Concept mapping

**D11 — `ConceptMapping` has no `validFrom`.**
*Collapse:* history, overclaim. `issuedAt` plus an optional `validTo` is an interval with no declared start; effectivity and issuance are conflated.
*Remediation:* require `validFrom` and keep `issuedAt` as transaction time (see D23).
*Fixture:* `mapping-interval-complete` (negative) — a mapping with `validTo` and no `validFrom` is rejected.

**D12 — no non-reversibility and no non-transitivity invariants for concept mappings.**
*Collapse:* mapping. The Proficiency Scale candidate carries both rules; WM-PER-009 carries neither, so the weaker-governed layer is the concept layer — the opposite of what the boundary claims.
*Remediation:* mirror both invariants: "concept mappings are non-reversible unless an independent reverse mapping exists" and "concept-mapping transitivity is never inferred."
*Fixture:* `concept-map-transitive-not-implied` (negative) — mappings A→B and B→C exist; A→C is not produced and no consumer may synthesize it.

**D13 — `purpose-qualified-equivalent` invites identity merge.**
*Collapse:* definition, mapping. The strength name reads as equivalence; the only guard is one fixture.
*Remediation:* rename to `equivalent-for-declared-purpose`; require non-empty `purpose` and non-trivial `semanticLoss` for that strength specifically; add invariant "no strength value licenses identity merge, deduplication, substitution or reporting outside the declared purpose."
*Fixture:* `purpose-equivalent-not-dedup` (negative) — a deduplication job merges two concepts on a purpose-qualified mapping; rejected, both concepts persist.

**D14 — `semanticLoss` is unstructured and can be asserted empty.**
*Collapse:* mapping, overclaim. "Declared loss" satisfied by `false` or `"none"` defeats the invariant it is meant to enforce.
*Remediation:* structure as `{kind ∈ {scope, granularity, context, assessment-basis, authority}, residualDescription}` with `residualDescription` required and non-empty; forbid a `none` value.
*Fixture:* `loss-must-be-described` (negative) — `semanticLoss: "none"` and empty residual are both rejected.

**D15 — no referential integrity between mapping endpoints and pinned releases.**
*Collapse:* mapping. `sourceConceptRef` need not belong to `sourceSchemeReleaseRef`.
*Remediation:* add invariant "each endpoint concept must exist in its pinned scheme release; a self-mapping within one release is invalid."
*Fixture:* `mapping-ref-mismatch` (negative) — source concept from r1 pinned against release r2; rejected.

**D16 — mapping authority can be read as target-scheme endorsement.**
*Collapse:* overclaim. A locally issued crosswalk to an external scheme can be published as that scheme's position.
*Remediation:* add `endorsedByTargetAuthority: boolean` defaulting to false; add invariant "a mapping without target-authority endorsement is never presented, labelled or exported as the target scheme's position or as certification against it."
*Fixture:* `unendorsed-map-not-endorsement` (negative) — an unendorsed local→external mapping rendered as "certified against" the external scheme is rejected.

### C. Proficiency Scale

**D17 — `ScaleLevel` does not exist.**
*Collapse:* scale, assessment, assertion. `orderedLevels` is an undefined blob; `levelRef`, `sourceLevelRef` and `targetLevelRef` reference an unmodelled object across three models.
*Remediation:* add `ScaleLevel` with identity `(proficiencyScaleId, version, levelId)` and required `ordinal`, `code`, language-tagged `labels`, `descriptor`; add invariant "ordinals form a total strict order, unique and contiguous within a version; `levelId` is version-scoped and never reused with different meaning."
*Fixture:* `level-ref-resolves-in-version` (negative) — a `levelRef` minted in v1 used with `scaleVersionRef` v2 is rejected.

**D18 — the identity invariant names a scale scheme that no field carries.**
*Collapse:* scale. "Scale identity is scale scheme, scale id and immutable scale version" against object identity `[proficiencyScaleId]` with only an `ownerRef`.
*Remediation:* pick one — add a `scaleSchemeRef` namespace component to identity, or restate the invariant as "scale identity is `proficiencyScaleId` plus immutable version; `ownerRef` is mastership, not identity."
*Fixture:* `same-name-different-owner` (negative) — two scales named "Proficiency 1–5" under different owners remain distinct and are never reconciled by name.

**D19 — `measurementLevel` sits on the scale while `versionIdentity` says changing it makes a version.**
*Collapse:* scale, assessment. A field that cannot vary by version cannot trigger a version; and with no vocabulary, ordinal and interval semantics are indistinguishable.
*Remediation:* move `measurementLevel` to `ScaleVersion` as required, with vocabulary `[nominal, ordinal, interval, ratio]`; add invariant "a change of measurement construct creates a new scale; a change of measurement level within one construct creates a successor version and never reinterprets finalized results."
*Fixture:* `measurement-level-change` (negative) — reinterpreting an ordinal scale as interval under the same `proficiencyScaleId` is rejected; a new scale is required.

**D20 — nothing forbids arithmetic on ordinal levels.**
*Collapse:* scale, assertion. Without this rule, averaging, summing, gap-size arithmetic and cross-scale ranking are all permitted, which is the most common route to a merged score.
*Remediation:* add invariant "levels of a non-interval scale are never averaged, summed, differenced or numerically ranked, within or across scales; gap analysis compares only within one version or through a pinned mapping."
*Fixture:* `no-ordinal-arithmetic` (negative) — averaging level 2 and level 4 to yield level 3 is rejected; so is a cross-scale numeric ranking.

**D21 — missing, indeterminate and not-applicable have no representation.**
*Collapse:* assessment, assertion. The invariant forbids collapsing them to zero, but the only available encoding is absence, which collapses all three into one another and into not-yet-assessed.
*Remediation:* define `nonLevelOutcome ∈ {not-assessed, indeterminate, not-applicable, declined}` recorded on the assessment profile and carried on the assertion when no level is claimed; add invariant "a non-level outcome is never a level, never zero, never the lowest level, and never a gap of computed size."
*Fixture:* `indeterminate-distinct-from-not-assessed` (negative) — a report bucketing indeterminate together with not-assessed, or either as zero, is rejected.

**D22 — scale-level and version-level lifecycles overlap.**
*Collapse:* scale. `effective` and `superseded` appear on both `ProficiencyScale` and `ScaleVersion` with no precedence, so effectivity has two contradictory homes.
*Remediation:* reduce the scale lifecycle to custodial states `[draft, active, retired]`; keep `[draft, approved, effective, superseded, withdrawn]` on the version; add invariant "effectivity is a version property; a retired scale keeps every version resolvable."
*Fixture:* `retired-scale-versions-resolvable` (positive) — after retirement, historical assertions and assessments still resolve against their pinned version.

**D23 — `nonReversible` is a settable field contradicting an absolute invariant.**
*Collapse:* mapping. `nonReversible: false` is representable and would negate the rule.
*Remediation:* drop the field; non-reversibility is a fixed semantic of every mapping. If retained for explicitness, constrain it to constant `true`.
*Fixture:* `nonreversible-false-rejected` (negative) — a mapping asserting `nonReversible: false` is rejected; reversal requires an independently issued reverse mapping.

**D24 — `interpretation` sits on the version, but the invariant scopes interpretation to levels.**
*Collapse:* scale. "Level identity and interpretation exist only inside one scale version" has no per-level interpretation field to land on.
*Remediation:* carry `interpretation` on `ScaleLevel` (optional) and keep version-level `applicability` for scope-of-use.
*Fixture:* `level-interpretation-version-scoped` (negative) — a v1 level descriptor reused to interpret a v2 result is rejected.

### D. Temporal model (all three models)

**D25 — three incompatible temporal vocabularies; bitemporality is claimed but absent.**
*Collapse:* history, assessment, assertion. `ConceptMapping` has `issuedAt` with no `validFrom`; `ScaleMapping` has `validFrom` with no issuance time; only the assertion carries both `recordedAt` and `validFrom`. No object outside the assertion can answer "what was known then."
*Remediation:* adopt one triple everywhere — `recordedAt` (transaction time, required), `validFrom`/`validTo` (valid time, `validFrom` required), and `observedAt` where an observation exists. Apply to scheme release, concept, composition, concept mapping, scale version, scale mapping and assertion.
*Fixture:* `as-of-two-axes` (positive) — a query with both valid-at and known-at returns the mapping as it was known at that time, not the latest issue.

### E. Person Capability Assertion

**D26 — `expired` is a stored status.**
*Collapse:* infers current competence; breaks as-of. A stored time-dependent flag contradicts the model's own rule that currency is derived and never stored, and it corrupts backdated queries — an assertion valid on the as-of date reads `expired` today and is wrongly excluded.
*Remediation:* remove `expired` from the stored lifecycle, leaving `[proposed, active, superseded, withdrawn, revoked]`; derive expiry from `validTo` at the as-of instant.
*Fixture:* `expired-is-derived` (negative→positive pair) — an as-of query inside the validity interval returns the assertion even though it has since lapsed; no stored flag is consulted.

**D27 — `revalidated` is a stored status.**
*Collapse:* history. Either revalidation extends `validTo` in place — a history rewrite the model forbids — or it mints a successor, in which case the status is redundant and ambiguous.
*Remediation:* remove `revalidated`; model revalidation as a successor assertion with `supersedesRef` and `basis: revalidation`, leaving the predecessor's interval untouched.
*Fixture:* `revalidation-creates-successor` (positive) — the predecessor's original `validTo` is unchanged and still resolvable; the successor carries the new interval.

**D28 — revocation and withdrawal carry no effective time and no retroactivity scope.**
*Collapse:* history, as-of correctness, overclaim. Whether a revocation voids the claim from inception or only forward is undecidable, so every as-of query touching a revoked assertion is unsound.
*Remediation:* add `revokedAt`, `revocationEffectiveFrom`, `revocationScope ∈ {ab-initio, prospective}`, `reasonCode`, `revokedBy`; add invariant "revocation never deletes; an ab-initio revocation makes the assertion unusable as support for every as-of instant while the record and its lineage remain resolvable and auditable."
*Fixture:* `ab-initio-revocation` (negative) — an as-of query predating the revocation no longer returns the assertion as support, yet the record, its evidence pointers and its supersession history still resolve.

**D29 — `assertionKind` is unconstrained against asserter, assessment and evidence.**
*Collapse:* assurance laundering; breaches the disjointness invariant. Nothing prevents `self-assessed` with a foreign `asserterRef`, `assessed` with no `assessmentRef`, `evidence-backed` with empty `evidenceRefs`, or `self-assessed` with `assurance: verified`.
*Remediation:* add invariants — `self-assessed` ⇒ `asserterRef = personRef` and assurance restricted to self-declared; `assessed` ⇒ `assessmentRef` required and `asserterRef ≠ personRef`; `evidence-backed` ⇒ `evidenceRefs` non-empty and each artifact status resolvable; `third-party-attested` ⇒ `asserterRef` is an external party with a declared relationship. No promotion path between kinds without a new assertion.
*Fixture:* `self-assessed-with-foreign-asserter` (negative) — rejected; a `self-assessed` assertion bearing `assurance: verified` is rejected on the same rule.

**D30 — the kind vocabulary is not orthogonal.**
*Collapse:* assurance, evidence. `assessed` and `evidence-backed` overlap — an assessment is evidence — so a single-valued field forces an arbitrary choice and the "disjoint" invariant cannot hold in fact.
*Remediation:* split into two required axes: `assertionKind` (who asserts: self, manager, assessor, external party) and `basis` (self-report, assessment act, artifact evidence, direct observation). Disjointness applies per axis; both are always visible in any disclosure.
*Fixture:* `assessed-and-evidence-backed` (positive) — one assertion records `basis: assessment-act` with supporting artifacts; no duplicate assertion is invented and neither axis is hidden.

**D31 — `observedAt` is claimed in `owns` but absent from the schema.**
*Collapse:* infers current competence. Without observation time, `recordedAt` stands in for when the capability was seen, and decay is computed from the wrong clock.
*Remediation:* add optional `observedAt` (or an observation window); add invariant "observation time never substitutes for `recordedAt` or `validFrom`; where present, decay and currency are computed from observation time."
*Fixture:* `observation-before-record` (positive) — an assertion observed in March and recorded in June computes decay from March and remains distinguishable on both axes.

**D32 — validity interval required by invariant, open end undeclared by schema.**
*Collapse:* infers current competence. `validTo` optional with no rule leaves open-ended assertions indistinguishable from unbounded ones.
*Remediation:* state explicitly that an absent `validTo` means open-ended-until-superseded, not indefinite validity; add invariant "an open-ended assertion still requires evidence coverage and artifact status at the as-of instant to support a current query."
*Fixture:* `open-ended-not-permanent` (negative) — an open-ended assertion whose sole supporting credential has lapsed does not support a current query.

**D33 — `decayRule` and `revalidationRule` have no effect boundary.**
*Collapse:* history, infers competence. A decay rule could be implemented as a level rewrite or an auto-generated lower assertion.
*Remediation:* add invariant "decay affects only derived currency and confidence at query time; it never mutates a stored level, never writes a lower level, and never creates an assertion."
*Fixture:* `decay-does-not-downgrade` (negative) — decay elapsing produces no new record and no level change; the assertion simply stops supporting a current query.

**D34 — no prohibition on merged scores or rankings.**
*Collapse:* assessment, scale, assertion. WM-PER-009 excludes "merged current score," but the merge would occur here, and the assertion model has no such invariant. The `multiple-methods-scales` fixture asserts "no merged score exists" with nothing behind it.
*Remediation:* add invariant "multiple assertions are never merged into a single level, score, index or ranking; a consumer may select one under a declared and disclosed policy, but the selection is a query result and is never stored as an assertion."
*Fixture:* `no-merged-score` (negative) — combining a manager-review assertion and a work-sample assertion into one composite level is rejected; the selection policy must be named in the response.

**D35 — absence is not declared to mean unknown.**
*Collapse:* infers current competence; discrimination risk. Nothing prevents a screening consumer from treating "no assertion" as "not competent."
*Remediation:* add invariant "absence of an assertion means unknown, never absence of capability; any process that treats missing data as failure must declare that treatment in its disclosure record."
*Fixture:* `absence-is-unknown` (negative) — a staffing filter scoring a person as non-qualifying purely on a missing assertion is rejected unless the treatment is declared.

**D36 — privacy model is a single sentence with no mechanism.**
*Collapse:* privacy. One invariant asserts purpose-bound least-privilege disclosure, but there is no purpose field, no lawful basis, no sensitivity class, no retention rule, no consent reference, and `evidenceRefs` may point at special-category material (health, disability accommodation, disciplinary evidence) surfaced through a capability query.
*Remediation:* add `purposeOfProcessing`, `disclosurePolicyRef`, `sensitivityClass`, `retentionRule` and `consentRef` (required for self-declared and third-party-attested evidence); add invariants — evidence content is referenced, never inlined; special-category evidence is never resolvable through a capability query; every disclosure records the requesting purpose and the fields released.
*Fixture:* `purpose-bound-projection` (negative) — a staffing-purpose query requesting accommodation-related evidence is rejected and the attempt is logged.

**D37 — immutability and erasure/rectification are unreconciled.**
*Collapse:* privacy vs history. "Never rewrites history" and a data subject's erasure or rectification right cannot both be satisfied without a declared mechanism, and the dossier declares none.
*Remediation:* define tombstoning — erasure removes payload and evidence pointers while retaining the identifier, lifecycle and audit trail; rectification mints a successor with `basis: rectification`; add invariant "redaction is itself a recorded act; it never erases the existence of prior versions, and a redacted assertion can never support a current query."
*Fixture:* `erasure-tombstone` (positive) — after erasure the identifier resolves to a tombstone, the supersession chain remains intact, and the assertion no longer supports any current-evidence query.

### F. Cross-model reference integrity

**D38 — no mastering model for `personRef`, `asserterRef`, `authorityRef`, `ownerRef`.**
*Collapse:* person assertion, definition authority. Four required fields across three models reference objects that the set neither owns nor delegates.
*Remediation:* name the person and party/organization models in each `references` list, or record an explicit hold that person and party mastership is unassigned and every such ref is unresolvable until assigned.
*Fixture:* `dangling-party-ref` (negative) — an assertion whose `asserterRef` resolves to no declared mastering model is rejected at validation, not accepted as free text.

**D39 — no reference grammar; three key vocabularies for the same thing.**
*Collapse:* every pinning invariant. WM-PER-009 pins by `releaseId`, the scale by `version`, the assertion by `definitionVersionRef` and `scaleVersionRef`. Nothing defines what a `*Ref` contains, so "version-pinned" is unverifiable.
*Remediation:* define one ref shape — `{model, schemeOrScaleId, id, releaseOrVersion, digest?}` — require every `*Ref` to use it, and require a version or release component on every cross-model reference.
*Fixture:* `unpinned-ref-rejected` (negative) — a `definitionVersionRef` carrying only a concept code, with no release component, is rejected.

**D40 — lifecycle states unreachable by any declared operation; two candidates declare no operations at all.**
*Collapse:* history, authority. WM-PER-009 has no `withdraw-release`, `retire-concept` or `withdraw-mapping`; the scale and assertion candidates declare no operations, so every transition in their lifecycles is undocumented and unattributed.
*Remediation:* declare one operation per lifecycle transition with its authority, for all three models — including scheme withdrawal, concept retirement, mapping withdrawal, scale version approval/effectivity/supersession/retirement, and assertion proposal/activation/supersession/withdrawal/revocation.
*Fixture:* `no-undeclared-transition` (negative) — a status change with no corresponding declared operation and authority is rejected.

**D41 — WM-PER-009 `relations` omits two models its own `delegates` names.**
*Collapse:* qualification, licence boundary. `delegates` sends qualifications to WM-PER-008 and licences to WM-PER-013, but `relations` lists only WM-ACT-034, WM-ORG-004 and WM-XCT-017.
*Remediation:* add non-required `REFERENCE` relations to WM-PER-008 and WM-PER-013 with purposes matching the delegation, or remove them from `delegates` and state where they are governed.
*Fixture:* `delegation-has-relation` (negative) — a delegation target absent from `relations` is flagged as an unclosed boundary.

### G. Validation and publication overclaim

**D42 — provider convergence is positioned as support.**
*Collapse:* overclaims validation. The comparison narrates agreement between two providers; nothing in the holds states that agreement is not verification, so downstream readers may cite it as such.
*Remediation:* add hold "agreement between providers is not verification; no invariant, boundary or fixture in this dossier has been executed, reviewed by a domain authority, or registry-approved."
*Fixture:* `convergence-not-validation` (negative) — a downstream record citing the provider comparison as validation evidence is rejected.

**D43 — fixtures assert unverified external facts.**
*Collapse:* overclaims validation. `same-number-different-scale`, `lossy-directional-map`, `reverse-not-implied`, `mapping-no-translation`, `multiple-methods-scales` and `cross-scheme-label-match` assert concrete external content ("SFIA v8 level 4", "SFIA 4", an ESCO preferred label) while the holds state that all external scheme details require pinned source verification.
*Remediation:* rewrite these fixtures with placeholder schemes (`EXT-SCHEME-A rN`, level `L4`), or annotate each with `dependsOnPinnedSource: unpinned` and bar them from acceptance evidence until the source release is pinned by digest.
*Fixture:* `external-fixture-unpinned` (negative) — a fixture naming an external scheme release without a pinned digest is not counted as passing evidence.

**D44 — reserved-ID metadata asserted while the registry record is recorded as missing.**
*Collapse:* overclaims publication. `sourceFacts` states the WM-PER-009 spec is missing, yet the completion asserts `name`, `registryId`, `entryKind` and `purpose` as if reconciled against a registry record.
*Remediation:* add hold "the registry record for WM-PER-009 was unavailable; name, entry kind, purpose and boundary here are proposed reconstructions pending registry confirmation and may be superseded by the reserved record."
*Fixture:* `reserved-name-unconfirmed` (negative) — publishing the reconstructed name as the registered name of `vr.wm-per-009` is rejected while the hold stands.

**D45 — the WM-ACT-034 competency-assessment profile is asserted in prose and absent from the dossier.**
*Collapse:* assessment, scale, assertion. There is no declared surface binding an assessment result to a scale version and level, and no home for non-level outcomes; three fixtures presuppose it.
*Remediation:* write the profile as a declared artifact of this contour — required `definitionVersionRef`, `scaleVersionRef`, `levelRef` or `nonLevelOutcome`, `assessedAt`, `methodRef`, `assessorRef` — and state explicitly that it allocates no identifier and inherits WM-ACT-034's holds.
*Fixture:* `assessment-result-binding` (positive) — a finalized result pins definition release and scale version together, or records a non-level outcome; a result carrying a level without a scale version is rejected.

---

## 5. Contradictions

Internal contradictions, stated as pairs. Each must be resolved by choosing a side, not by adding prose.

| # | Contradiction | Resolve toward |
|---|---|---|
| X1 | Fixture `deprecated-successor` requires two successors; `successorConceptRef` is singular | the fixture (D3) |
| X2 | Fixture `same-label-different-type` says distinctness comes from "type and stable code"; identity is `(schemeId, releaseId, conceptId)` and excludes type; the invariant names a third vocabulary ("scheme, scheme-local code, immutable definition version") | one identity statement (D1, D2) |
| X3 | `compose-competency` composes knowledge and behaviour; `conceptTypes` is `[skill, competency]` | extend the vocabulary or restate the operation (D8) |
| X4 | Scale invariant "identity is scale scheme, scale id and version"; object identity is `[proficiencyScaleId]` with no scheme field | the object, with the invariant restated (D18) |
| X5 | `measurementLevel` on the scale; `versionIdentity` says changing it creates a version; `identityTest` says a different construct creates a separate scale | move the field to the version (D19) |
| X6 | `nonReversible` is a required settable field; the invariant makes non-reversibility absolute | the invariant; drop or fix the field (D23) |
| X7 | Assertion lifecycle stores `expired`; the invariant forbids a stored currency flag | the invariant (D26) |
| X8 | Assertion lifecycle stores `revalidated`; `versionIdentity` says a new validity interval creates a successor | the successor rule (D27) |
| X9 | `owns` claims "observation time"; no `observedAt` field exists | add the field (D31) |
| X10 | Invariant requires "a validity interval"; `validTo` is optional with no open-end semantics | declare open-ended semantics (D32) |
| X11 | `ConceptMapping` requires `issuedAt` and no `validFrom`; `ScaleMapping` requires `validFrom` and no issuance time; bitemporality is claimed for the set | one temporal triple (D11, D25) |
| X12 | WM-PER-009 `delegates` names WM-PER-008 and WM-PER-013; `relations` omits both; the scale references WM-PER-008 but not WM-PER-013 while the assertion references both | align delegates with relations (D41) |
| X13 | WM-PER-009 excludes "merged current score"; the assertion model, the only place a merge can occur, has no such invariant, while its fixture asserts one | add the invariant (D34) |
| X14 | Holds require pinned verification of ESCO/SFIA/CTDL/CLR/Open Badges/VC; fixtures assert concrete SFIA and ESCO content as ground truth | genericize the fixtures (D43) |
| X15 | `sourceFacts` records the WM-PER-009 spec as missing; the completion asserts registered name, entry kind and purpose with no hold covering them | add the hold (D44) |
| X16 | Lifecycles include `withdrawn` and `retired` states; no operation reaches them, and the two candidates declare no operations at all | declare the transitions (D40) |
| X17 | The assertion invariant declares the four kinds disjoint; `assessed` and `evidence-backed` overlap by construction | split the axes (D30) |
| X18 | "Changing … creates a successor and never rewrites history" coexists with an unmodelled erasure/rectification obligation implied by the privacy invariant | define tombstoning (D37) |
| X19 | The scale invariant scopes interpretation to levels; `interpretation` is a version-level optional field | move it to the level (D24) |
| X20 | Provider comparison narrates convergence as if it strengthened the result; every hold states nothing is verified | add the non-validation hold (D42) |

---

## 6. Closed remediation checklist

Complete and closed. Nothing outside these 25 items is required for this contour to be re-frozen; each item is verifiable against the revised dossier.

1. Declare the concept lineage key `(schemeId, conceptId)` and the pinned address `(schemeId, conceptId, releaseId)`; fix `conceptType` as immutable across a lineage. *(D1, D2, X2)*
2. Replace `successorConceptRef` with `successorConceptRefs[]` carrying `relationKind` and `guidanceOnly`. *(D3, X1)*
3. Require `deprecatedAt` and `retiredAt`; add the universal resolvability invariant for deprecated, retired, superseded and withdrawn objects across all three models. *(D4, D9, D22)*
4. Add the issued-release immutability and digest-verification invariant; define `version` as a non-identifying label. *(D5, D6)*
5. Require BCP-47 language tags and one preferred label per tag. *(D7)*
6. Resolve `conceptTypes` against `compose-competency`; require version-pinned composition components; add a composition lifecycle with supersession. *(D8, D9, X3)*
7. Restrict scheme-level `evidenceRefs` to authority and provenance sources; forbid person, assessment and assertion references at definition scope. *(D10)*
8. Add `validFrom` to `ConceptMapping`; adopt the single temporal triple (`recordedAt`, `validFrom`/`validTo`, `observedAt`) across scheme release, concept, composition, both mapping objects and the assertion. *(D11, D25, D31, X11)*
9. Mirror the non-reversibility and non-transitivity invariants onto concept mappings. *(D12)*
10. Rename `purpose-qualified-equivalent` to `equivalent-for-declared-purpose` and add the no-merge/no-dedup/no-substitution invariant. *(D13)*
11. Structure `semanticLoss` with a required non-empty `residualDescription`; forbid a `none` value. *(D14)*
12. Add endpoint referential integrity for both mapping objects and forbid self-mapping within one release. *(D15)*
13. Add `endorsedByTargetAuthority` and the no-implied-endorsement invariant. *(D16)*
14. Add the `ScaleLevel` object with version-scoped identity, ordinal totality and per-level `interpretation`. *(D17, D24, X19)*
15. Resolve scale identity against its invariant; keep `ownerRef` as mastership only. *(D18, X4)*
16. Move `measurementLevel` to `ScaleVersion` with a closed vocabulary and the construct-versus-version rule. *(D19, X5)*
17. Add the no-ordinal-arithmetic invariant. *(D20)*
18. Define `nonLevelOutcome` and the never-zero/never-lowest/never-a-gap invariant. *(D21)*
19. Collapse the scale lifecycle to custodial states; make effectivity a version property. *(D22)*
20. Remove or constrain `nonReversible`. *(D23, X6)*
21. Remove `expired` and `revalidated` from the assertion lifecycle; model revalidation as a successor; add `revokedAt`, `revocationEffectiveFrom`, `revocationScope`, `reasonCode`, `revokedBy` with the never-delete invariant. *(D26, D27, D28, X7, X8)*
22. Split `assertionKind` into kind × basis; add the kind/asserter/assessment/evidence consistency invariants and the no-promotion rule. *(D29, D30, X17)*
23. Declare open-ended validity semantics; bound decay to derived currency only; add the no-merged-score and absence-is-unknown invariants. *(D32, D33, D34, D35, X13)*
24. Add the privacy mechanism (`purposeOfProcessing`, `disclosurePolicyRef`, `sensitivityClass`, `retentionRule`, `consentRef`, reference-not-inline, special-category exclusion, disclosure logging) and the tombstone/rectification reconciliation. *(D36, D37, X18)*
25. Close the reference and publication gaps: name or hold person/party mastership; define one `*Ref` grammar with mandatory version pinning; declare an operation per lifecycle transition in all three models; align `delegates` with `relations`; write the WM-ACT-034 competency-assessment profile as a declared, identifier-free artifact; add the non-validation, unpinned-external-source and unconfirmed-reserved-record holds; assign pre-allocation review slugs to both unassigned candidates. *(D38–D45, D41, X12, X14, X15, X16, X20, and the §2 condition)*

Every fixture expectation named in §3–4 must be present in the revised fixture sets before re-freeze, and must remain labelled declarative and unexecuted until package conversion and live verification are complete.
