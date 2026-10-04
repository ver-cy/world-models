# Frozen Semantic Audit — EM-LND-01, candidate revision 2

## Verdict

**REVISE.**

The boundary decision is sound and I affirm it: PROFILE over WM-ORG-002/003/004/016, no new catalogue or runtime identifier. The three constructs pass the identity/lifecycle test in principle, and the axis-scoping of cardinality and acyclicity correctly resolves the contour's mis-quantified single-manager invariant. That is not what fails.

What fails is the part the candidate claims as its strongest contribution: **deterministic snapshot identity**. The declared digest tuple does not cover all inputs that determine snapshot content, has no declared algorithm or canonicalisation, and is therefore collision-admitting. Two axes claim the same source edge set with no discriminating predicate. Two cardinality rules refuse legal structures. One fixture contradicts another. And no fixture in the suite is executable, because none declares the pins, axis set or rule versions on which its own expected outcome depends.

---

## Findings

Severity: **B** blocking (candidate cannot be accepted), **M** material (must be fixed before publication), **m** minor.

### Deterministic snapshot identity

**F1 (B) — The digest is under-determined and admits collisions.** Identity is `digest(landscapeId, axisId, ruleVersion, worldTime, recordTime, sourceVersions, sourceDigests, generatorVersion)`. It omits `specVersion`, `organizationPerimeter` and `scenarioClass` — all three of which the candidate itself declares to be *identity* components of `OrganizationLandscape`, and all three of which change snapshot content (which node and edge kinds, which correspondence rules, which units are in perimeter). Two generations under different landscape spec versions, same axis rule version and same pins, produce the same digest over different content. That is a second source of truth by digest collapse, and it defeats the candidate's own constraint that snapshots are never overwritten: an identity collision is an overwrite in all but name.

**F2 (B) — No digest algorithm, no canonical serialisation, no field ordering.** `digest(...)` is written as prose. `sourceVersions` and `sourceDigests` are collections with no declared ordering; `worldTime` and `recordTime` are RFC 3339 instants with no declared normalisation, so `2026-10-01T00:00:00+00:00`, `2026-09-30T20:00:00-04:00` and `...Z` are the same instant with three digests. Fixture `same-pins-same-digest` is therefore not merely untested but *undecidable* — the property it asserts has no definition to test against. WM-ORG-002 and WM-ORG-016 both flag the unknown-offset `-00:00` case; the candidate inherits that hazard silently.

**F3 (B) — View parameters that change content are absent from identity and digest.** Both provider studies list root unit, maximum depth and disclosure class as composed-view parameters. The candidate carries none of them, yet retains `disclosed` in the snapshot lifecycle. Either the profile generates whole-perimeter, single-disclosure-class snapshots only — which must be stated as a constraint — or root, depth and disclosure class are digest inputs. Currently a depth-2 and a depth-unbounded snapshot of the same pins share a digest.

**F4 (M) — Partial snapshots are an undeclared artifact class.** Fixture `optional-source-omission` returns `snapshot-created-partial`, an outcome that appears nowhere in the constructs, the lifecycle or the digest. The constraint says "the snapshot records the omission" without naming the field. Because an omitted source contributes no pin, a partial snapshot can only be distinguished from a complete one if the digest encodes the resolved pin map *keyed by source with explicit omission markers*, rather than concatenating present pins. Absent that, a partial snapshot may be composed by reference in place of a complete one.

### Identity and lifecycle

**F5 (M) — `OrganizationLandscape` identity conflates designator, version and version contents.** `axisSet` and `organizationPerimeter` are determined by `(landscapeId, specVersion)`; including them in the identity tuple permits two distinct identities agreeing on landscapeId and specVersion but disagreeing on axis set, which is a broken functional dependency. It also contradicts the candidate's own lifecycle claim that the spec is *versioned* — if specVersion is identity, nothing persists across versions to be versioned.

**F6 (M) — `disclosed` is not a lifecycle state.** Disclosure is a repeatable event that neither precludes retention nor is preceded by a single predecessor state. As written the state machine is ill-formed (is a disclosed snapshot still retained?), and there is no disclosure-class parameter, suppression rule, or statement that grants are issued by S2 and audit facets by S4 — which Claude's study required explicitly.

**F7 (M) — `tombstoned` conflicts with mandatory digest preservation.** The candidate requires that a later correction "preserves the old digest," and the bases require retention-driven disposition that "reduces the reconstruction horizon." Tombstoning is never defined, so it can silently destroy the record the bitemporal-correction constraint requires to survive.

**F8 (M) — Refusal has no artifact class.** "A required source that cannot reconstruct the requested pair causes a **refused snapshot** with source and horizon diagnostics" is self-contradictory: an immutable digest-identified artifact that was never generated. Six fixtures expect `refused` with codes, so refusal records exist, carry diagnostics, and are presumably retained — with what identity, under whose retention, is undeclared. A digest over content cannot identify an artifact with no content.

**F9 (m) — `axisId` versus `axisCode`.** The digest names `axisId`; the construct's identity names `axisCode`. One of the two is an unbound term. The four axis names in the `axes` block are already functioning as codes but are not declared as a governed, versioned profile-level code list, so `axisId` is not resolvable.

### Axis semantics

**F10 (B) — Functional and supervisory axes claim the same source edge set with no discriminator.** Both list "WM-ORG-004 post reporting" as a source. Grok's study restricted supervisory to "the supervisory type" and functional to "functional or professional kind"; the candidate dropped the type predicate from both. The same post-to-post edge therefore projects onto two axes non-deterministically, and whether "exactly one effective supervisor per assignment" holds depends on a classification the profile does not perform. The governing vocabularies exist in the bases and are unused: WM-ORG-002 `reportingLineType`, WM-ORG-016 `reporting_line_type_code`.

**F11 (B) — Administrative cardinality refuses the root.** "One parent per unit per interval" has no exception for the hierarchy root, which WM-ORG-002 models as `parentUnitRef` cardinality `0..1`. As written, every conformant administrative snapshot is refused.

**F12 (B) — Supervisory cardinality refuses legitimately unsupervised assignments.** "Exactly one per assignment and axis after precedence" refuses the top of the reporting structure. WM-ORG-016 models `reports_to_ref` as `0..n`.

**F13 (M) — Supervisory precedence has no tie-breaker and no refusal code.** Claude's study states the outcome as "WM-ORG-016's precedence rule resolves **or** `validate-structure-graph` blocks." The candidate keeps the resolution and drops the block. Two concurrent edges of equal precedence on one assignment have no defined outcome.

**F14 (M) — The functional-axis parameter has no default.** `"hierarchy": "profile parameter"` with `"default": "DAG when hierarchy=true"` states the consequence of `true` and never states what the parameter defaults to. Separately, "hierarchy" is used to mean "acyclicity required" while the administrative axis uses it to mean single-parent tree; the union-graph constraint is phrased in terms of this overloaded word. This is also the live provider disagreement (Claude: cycles forbidden on functional; Grok: parameterised) — resolved in Grok's favour without recording the adjudication.

**F15 (M) — The project axis carries two heterogeneous edge kinds under one rule version.** Membership (bipartite, acyclicity inapplicable) and team nesting (acyclicity applicable, cardinality ≤1 parent, or prohibited under the Scrum and secret-team profiles WM-ORG-003 publishes side by side) cannot share one axis-scoped cycle rule. The candidate declares no nesting cardinality or cycle rule at all, and does not carry forward WM-ORG-003's declared, unmergeable vocabulary conflict.

**F16 (M) — The administrative axis does not bind to a named hierarchy.** WM-ORG-002 governs *concurrent* named hierarchies (`hierarchyIdentifier`, `hierarchyEdge` qualified by hierarchy, `isCodmReportingHierarchy`), and its deferred research leaves ERP cost/profit/funds-centre hierarchies unresolved. "WM-ORG-002 containment" is ambiguous whenever more than one containment hierarchy exists.

**F17 (M) — The unit-level reporting extension declaration is dropped.** Both studies require it: `org:reportsTo` binds Agents and Posts, so unit-to-unit reporting publishes as a declared non-conformant extension with a mapping rule, per WM-ORG-002 `standardExtensionNote`. The candidate's hold covers the *conformance claim* but no constraint requires the marker on the projected edge.

### Source mastership

**F18 (B) — The pin constraint presupposes a capability three of four bases do not evidence.** "Generation pins every constituent source version and digest" is asserted as operative. Only WM-ORG-002 exposes `structureVersionId` plus `contentDigest` — and that digest is cardinality `0..1`, **required false**. WM-ORG-003, WM-ORG-004 and WM-ORG-016 expose record instants and effective windows, not versions-with-digests. The constraint is currently unsatisfiable, and fixture `floating-source-version` tests only the "latest" case, never pin-present-digest-absent.

**F19 (B) — Composing source-local snapshots by reference breaks bitemporality on WM-ORG-003.** The candidate says "the landscape snapshot composes them by reference." WM-ORG-003's `team-hierarchy-snapshot` identity strategy is "containing organization identifier plus snapshot observation time" — a single-clock artifact, not addressable by a `(worldTime, recordTime)` pair. Claude's study explicitly required reconstruction from assertions rather than from that artifact. Composing it makes the digest non-reproducible and violates "one world-time and record-time pair applies to every required source."

**F20 (M) — The candidate is not pinned to the artifacts it was derived from.** `bases` lists model_ids only: no registry_ids, no `synthesisSha256`. All four values are available in the dossier. Claude's study required pinning them as immutable refs.

**F21 (M) — The no-copy constraint is under-scoped and untestable.** It names Person and organizational-unit facts only; teams, posts and assignments are equally referenced-not-copied. No reference shape (`{model_id, identifier, scheme}` plus a declared label set) and no loss/fidelity manifest are declared, so "never copied" cannot be checked. Both studies required the manifest.

**F22 (M) — Derived and out-of-scope facts are unstated.** WM-ORG-002 records informal/shadow structure and de facto reporting as an open gap, so the view shows asserted edges only; WM-ORG-004 keeps vacancy derived and never stored; IFRS 8 segment determination and statistical units stay out. None of this is carried into constraints.

### Bitemporal consistency

**F23 (B) — Fixture `mixed-time` contradicts fixture `future-reorg-before`.** `mixed-time` refuses a case whose only stated defect is that an assignment's world-time validity (2026-10-01) is later than the requested world time (2026-09-28). That is a future-effective fact — exactly the pattern `future-reorg-before` accepts as `PRE_REORG_STRUCTURE`. The constraint actually being tested is a *request-level* prohibition on per-source time pairs; the fixture encodes per-source *data* timestamps. As written, a conformant implementation must both accept and refuse the same structure.

**F24 (M) — Fixture `correction-new-record-time` is underdetermined.** It gives one `recordTime` (2026-09-28, after the correction at 2026-09-20) and never states SNAP-OLD's record time. Without a record time earlier than the correction, `new-digest-old-preserved` cannot be distinguished from `same-digest`. The governing constraint also mis-states agency: a correction does not create a snapshot; a generation request at a later record time does.

**F25 (M) — No interval boundary convention is declared.** `future-reorg-before` uses 2026-09-30T23:59:59 against `effectiveAt` 2026-10-01T00:00:00 — dodging the boundary by one second rather than pinning it, at a granularity that hides sub-second cases. WM-ORG-016 flags inclusive-versus-exclusive end as open; WM-ORG-002 asks about gaps and overlaps.

**F26 (m) — The horizon is treated as single-axis.** Retention-driven disposition reduces the *record-time* reconstruction horizon (WM-ORG-002 `apply-disposition`), not only the world-time reach. The composed horizon as the intersection of required-source horizons (Claude invariant 5) is not published.

### Scenario discipline

**F27 (M) — Fixture `hypothetical-scenario` conflates two independent rules.** Refusal is correctly triggered by `scenarioClass: hypothetical`, but the fixture also carries `sourceAct: null` and a future world time, inviting implementers to refuse *all* future world times lacking a recorded act. A future world time beyond every recorded act is authoritative and must project the latest recorded state; no positive fixture establishes this.

**F28 (m) — The no-leak invariant is missing.** Claude invariant 6 — scenario-marked facts never appear in an authoritative view and vice versa — is vacuous today but must be written now so the planning extension cannot leak later.

### Fixtures

**F29 (B) — No fixture is executable.** Not one case declares `landscapeId`, `specVersion`, `axisSet`, `ruleVersion` or the source pins. `same-pins-same-digest` asserts `samePins: true` without stating the pins. Every expected outcome in the suite depends on parameters the suite does not supply. This is an illustrative catalogue, not a conformance suite, and the candidate's claim that fixture checks gate publication cannot be discharged against it.

**F30 (M) — Coverage gaps against declared constraints.** Missing negative cases: administrative multi-parent in overlapping intervals; functional cycle with `hierarchy=true`; functional cycle with `hierarchy=false` (positive); project nesting cycle; unresolved supervisory precedence; untyped reporting edge; snapshot overwrite on regeneration; pin present but digest absent; record-time horizon exhausted; person-attribute copied into a view. Missing positive cases: future world time beyond all recorded acts; exclusion exactly at `validTo`; a reorg with distinct decision, effective and record times proving `decisionTimestamp` is ignored (a named constraint with zero coverage).

**F31 (m) — `matrix-separate-axes` inherits a provider error.** Claude's walkthrough placed supervisor S2 on the *project* axis; the candidate correctly confines supervision to the supervisory axis. The fixture's `projectEdge` should be explicitly labelled a membership edge, and the correction recorded as an adjudication, or readers will reconstruct the error.

---

## Required deterministic remediation

Each item is a mechanical edit to candidate revision 3. No item requires new research.

**R1.** Replace the snapshot identity expression with a fully enumerated, algorithm-bearing definition:

```
digestScheme: "vercy-landscape-snapshot-digest/v1"
algorithm: "sha-256"
canonicalisation: "JCS (RFC 8785) over the manifest object below"
inputs (all required, in this order):
  digestScheme, algorithm, landscapeId, specVersion, organizationPerimeter,
  scenarioClass, axisId, ruleVersion, requestParameters{root, maxDepth, disclosureClass},
  worldTime, recordTime, sourcePins[], generatorVersion, completeness
sourcePins[]: ordered lexicographically by sourceId; each entry
  {sourceId, required:bool, state:"pinned"|"omitted", version|null, digest|null, digestAlgorithm|null}
completeness: "complete" | "partial"
timeNormalisation: RFC 3339, converted to UTC, "Z" suffix, nanosecond precision, "-00:00" forbidden
```

If root, maxDepth and disclosureClass are out of scope for revision 3, delete them from `requestParameters` **and** add the constraint "snapshots cover the whole declared perimeter at a single disclosure class; sub-tree and depth-limited views are not in scope." Do not leave them unmentioned. (F1, F2, F3, F4)

**R2.** Set `OrganizationLandscape.identity: ["landscapeId", "specVersion"]`; demote `organizationPerimeter`, `axisSet` and `scenarioClass` to governed attributes of that version; delete the duplicate `scenarioClass` sibling field. (F5)

**R3.** Replace the snapshot lifecycle with `["created", "retained", "tombstoned"]`. Model disclosure as a repeatable event class with `{snapshotDigest, disclosureClass, grantRef, at}`, and add the constraint: "suppression parameters are declared by this profile; grants are issued by S2 and audit facets by S4." Define tombstoning as: payload removed, digest + manifest + pin map retained and resolvable, disposition authority recorded; add "a tombstoned snapshot continues to satisfy digest-preservation obligations." (F6, F7)

**R4.** Introduce a `SnapshotRefusal` construct: identity `(landscapeId, specVersion, axisId, ruleVersion, worldTime, recordTime, requestNonce)`, not a content digest; payload carries refusal code, failing sourceId, requested pair and declared horizon. Replace every occurrence of "refused snapshot" with "refusal record." (F8)

**R5.** Rename `axisId` → `axisCode` throughout the digest, and add a profile-level governed code list `axisCodes: [administrative, functional, project-membership, project-nesting, supervisory]` with a `codeListVersion`. These are profile constants, not runtime identifiers. (F9, F15)

**R6.** Add an `edgePredicate` to every entry in every axis `sources` list, drawn from the bases' own vocabularies, and add the constraint: "an edge whose line type is absent or unclassified is refused with `UNTYPED_REPORTING_EDGE`; no edge projects onto more than one axis." Functional takes `reportingLineType ∈ {functional, professional}` (solid or dotted); supervisory takes `reportingLineType = supervisory` plus WM-ORG-016 `reporting_line_type_code`. (F10, F17 marker)

**R7.** Restate cardinalities: administrative → "at most one parent per unit per interval; exactly one root; orphans refused"; supervisory → "at most one effective supervisor per assignment per axis after precedence; zero is permitted and recorded." (F11, F12)

**R8.** Add "supervisory precedence that does not resolve to a single effective edge is refused with `SUPERVISOR_PRECEDENCE_UNRESOLVED`; the profile never selects arbitrarily," and pin the precedence rule to a WM-ORG-016 rule version. (F13)

**R9.** Split the functional parameter into `acyclicityRequired: bool (default false)` and `parentCardinality: "unbounded"` and delete the word "hierarchy" from the functional axis and from the union-graph constraint. Record the Claude/Grok disagreement as an explicit adjudication in favour of parameterisation, with the hold retained. (F14)

**R10.** Split `project` into `project-membership` (many-to-many, acyclicity inapplicable, never hierarchy) and `project-nesting` (at most one parent, acyclic, may be prohibited by profile), and carry WM-ORG-003's Scrum-prohibition / one-parent / nested-group conflict forward verbatim as three side-by-side declared profile constraints with the instruction not to merge them. (F15)

**R11.** Bind the administrative axis to a named `hierarchyIdentifier` with the WM-ORG-002 `isCodmReportingHierarchy` flag surfaced, and add a hold: the axis register cannot close while WM-ORG-002 defers ERP cost/profit/funds-centre hierarchies and the unit↔site association. (F16)

**R12.** Add the constraint: "every projected edge whose subject is an organizational unit carries WM-ORG-002's `standardExtensionNote` declaring the departure from `org:reportsTo` with its mapping rule." (F17)

**R13.** Mark the pin constraint non-implementable pending source capability: "source version-and-digest pinning is satisfiable today only for WM-ORG-002, and there only where `contentDigest` is present. For WM-ORG-003, WM-ORG-004 and WM-ORG-016 no version-with-digest contract exists; generation against them is blocked until a scoped EXTEND supplies one. A declared pin substitute, if later adopted, appears in the manifest as `state:"substituted"` with a visible fidelity marker." Add fixture `pin-without-digest` → refused `SOURCE_DIGEST_UNAVAILABLE`. (F18)

**R14.** Replace "composes them by reference" with: "the landscape snapshot reconstructs from bitemporal source assertions. Composition of a single-clock source artifact is forbidden; WM-ORG-003's `team-hierarchy-snapshot` is keyed by observation time alone and must not be composed." (F19)

**R15.** Expand `bases` to carry, per base, `model_id`, `registry_id` and `synthesisSha256` as immutable refs — the four values are in the dossier and must be transcribed exactly, not recomputed. (F20)

**R16.** Extend the no-copy constraint to persons, units, teams, posts and assignments; declare the reference shape `{model_id, identifier, scheme}` plus a closed display-label set; require a loss/fidelity manifest and a non-reimportable marking on every snapshot. Add fixture `person-attribute-copied` → refused `REFERENCE_ONLY_VIOLATION`. (F21)

**R17.** Add constraints: asserted edges only, informal and de facto reporting excluded as a declared source gap; vacancy and other derived values never stored on a snapshot; IFRS 8 segment determination and statistical units out of scope. (F22)

**R18.** Rewrite `mixed-time` as a request-level violation — `asOf` supplying per-source pairs, e.g. `perSourceAsOf: {"WM-ORG-002": ..., "WM-ORG-016": ...}` → refused `MIXED_TIME_PAIR` — and add a positive case in which a single pair contains a future-effective assignment fact, included or excluded purely by world-time comparison. (F23)

**R19.** Rewrite `correction-new-record-time` with both record times stated: `SNAP-OLD.recordTime = 2026-09-19T00:00:00Z`, `SNAP-NEW.recordTime = 2026-09-28T12:00:00Z`, identical `worldTime = 2026-09-01T00:00:00Z`, correction recorded `2026-09-20T00:00:00Z`; expect distinct digests, both retained and resolvable. Restate the constraint as: "a generation at a record time at or after a recorded correction yields a different digest; the earlier digest remains retained." (F24)

**R20.** Declare half-open intervals `[validFrom, validTo)`, RFC 3339 with explicit offsets, `-00:00` forbidden. Set `future-reorg-before.worldTime` to the boundary-adjacent instant at declared precision and add a case at exactly `validTo` demonstrating exclusion. (F25)

**R21.** Declare each source's horizon as a bitemporal rectangle `{worldFrom, worldTo, recordFrom, recordTo}` and the composed horizon as their intersection over required sources; add fixture `record-time-horizon-exhausted` → refused `SOURCE_HORIZON_UNAVAILABLE`. (F26)

**R22.** Strip `sourceAct` from `hypothetical-scenario` so refusal turns solely on `scenarioClass`; add positive `future-beyond-recorded-acts` → `snapshot-created` / `LATEST_RECORDED_STATE`; add the invariant that scenario-marked and authoritative facts never appear in one another's views. (F27, F28)

**R23.** Promote the fixture format to `v3` and require every case to declare `landscapeId` placeholder role, `specVersion`, `axisSet`, `ruleVersion` per axis, `generatorVersion`, `digestScheme` and a complete `sourcePins[]` map. `same-pins-same-digest` must enumerate the identical pin maps for GEN-1 and GEN-2. No case may leave any digest input or rule parameter implicit. (F29)

**R24.** Add the eleven missing cases enumerated in F30, and relabel `matrix-separate-axes.projectEdge` as a membership edge with the Claude-study correction recorded as an adjudication. (F30, F31)

**R25.** Add these holds, which the evidence supports and the candidate omits: WM-ORG-003 single-clock artifact composition hazard; absence of a version-and-digest contract on three of four bases; WM-ORG-002 named-hierarchy binding unresolved; the four inherited base ceilings stated specifically (ISO clause text unverified, unit-grain staffing extension-grade, private-sector matrix forms unvalidated, EU/US regional scope must be stated on the face of any draft); disclosure-class and suppression parameters unratified.

---

## Identifier discipline

**Permitted and correctly used in revision 2.** `contourId: EM-LND-01`, `candidateRevision`, the four base `model_id` values, and the dossier's four `registry_id` values — all pre-existing in the frozen dossier. `newRuntimeId: false` is correct and must stay. The absence of concrete `landscapeId`, `axisCode`, `ruleVersion` and snapshot digest *values* in the axes block is correct discipline, not an omission, and revision 3 must preserve it.

**Required additions that are not minting.** Transcribing the four `synthesisSha256` values (R15) copies existing values; it allocates nothing. Declaring the `axisCodes` code list (R5) and the `digestScheme` string (R1) creates *profile-level governed constants*, which are part of the specification, not runtime identifiers for instances — permitted. Declaring a `codeListVersion` and `digestScheme` version label is likewise specification content.

**Forbidden, and to remain forbidden through revision 3.** No registry ID for EM-LND-01. No concrete landscape, axis-instance or snapshot identifier. No computed snapshot digest value, including in fixtures — fixtures state digest *equality and inequality relations*, never digest literals. No `structureVersionId` values for any base.

**One correction to carry forward.** Claude's study proposes hosting the profile at `vr.wm-org-002#profile/landscape-organizational-structure`. That is a **proposal, not an allocation**, and I do not ratify it. Revision 3 should record it as `proposedHostBinding` with `allocationStatus: "not-allocated"`, because the profile currently has no declared host and therefore `landscapeId` has no namespace — but the binding requires registry action under the dossier's rule that no new ID issues without independent identity/lifecycle and registry allocation, and hosting a four-model profile on one of its four bases is itself a decision the registry owner must take, not an auditor.

---

## Publication decision

**HOLD. No publication, no package conversion, no canonical status, no identifier allocation.**

Independent of the findings above, the candidate's own holds are sufficient to bar publication: all four bases are `publishableCanonical: false` / `reviewable-draft`, and a profile cannot exceed the ceiling of its sources. The findings add a second, independent bar — F1–F3, F10–F12, F18–F19, F23 and F29 are each individually blocking, and F1 and F29 together mean the candidate's central claim of deterministic, fixture-verified snapshot identity is not currently supported by its own text.

Specific release gates, all of which must close before any publication decision is retaken:

1. Revision 3 incorporating R1–R25, with F1–F3, F10–F12, F18–F19, F23 and F29 closed in full.
2. Source pin contracts ratified, or generation explicitly blocked for WM-ORG-003/004/016 pending a scoped EXTEND (R13).
3. Semantic crosswalk confirmed beyond index-and-publication-metadata depth for WM-ORG-002/003/004 — only WM-ORG-016 is boundary-reviewed, and three of four bases rest on publication metadata alone.
4. Fixture suite v3 executed, with recorded results, against a generator declaring `digestScheme` and `generatorVersion`.
5. Registry decision on host binding, taken by the registry owner.
6. Bases reaching canonical status, or an explicit, scoped decision to publish the profile as a reviewable draft inheriting every base ceiling verbatim.

**On the re-audit.** This frozen audit is now spent. Revision 3 changes the digest scheme, the axis code list, two cardinality rules, the construct set (adding `SnapshotRefusal`) and the fixture format — that is a materially different artifact, not an erratum, and it must not be published on the strength of this pass. A second frozen semantic audit must be separately authorised and must be given revision 3, fixtures v3 and the executed fixture results together. I make no publication authorisation here and none is implied by the affirmation of the PROFILE boundary.
