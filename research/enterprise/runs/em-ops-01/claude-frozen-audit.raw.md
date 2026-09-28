# FROZEN SEMANTIC AUDIT — EM-OPS-01 (Process, Procedure and Execution)

## 1. Verdict

**REVISE.**

The boundary decision is sound and is accepted unchanged. The reconciled candidates are not. They contain identity, immutability and evidence defects that are individually fixable in one remediation pass but that, as written, make the contour's own negative case (`Обновление инструкции меняет задним числом выполненный процесс`) still reachable, and make the acceptance scenario non-reproducible for any instance that crosses a cutover.

## 2. Reserved-model decision

**CONFIRMED: COMPLETE BOTH RESERVED MODELS.**

- `vr.wm-act-003` completes as the operational-flow aggregate (family, variant, released definition, instance, work item, observed execution, deviation, compensation, cutover, conformance projection).
- `vr.wm-act-009` completes as the authored-knowledge aggregate (method, procedure, immutable edition, applicability, adopter-owned adoption).
- No new catalogue, runtime or spec identifier is created. `ProcessInstance`, `ActivityExecution`, `ProcessMethod` and `ConformanceResult` remain components of the two reserved models; the dossier evidences no independent registrar, no separate mastership and no citability without a resolvable definition edition for any of them.
- Both `0.2.0-legacy` assemblies are preserved immutable and non-installable. Preservation is not endorsement: see D30.

The two candidate identifiers are the only ones this audit authorizes. Identifiers introduced by the candidates that the frozen dossier does not contain are treated as unverified (D28).

## 3–4. Semantic defects, remediation and fixture expectation

### A. Duplicate or unresolvable identity

**D1 — `Edition` identity does not prevent duplicate versions.**
`Edition.identity = [editionId]` with `subjectRef` and `version` merely required. Two distinct `editionId` values may carry the same `(subjectRef, version)`. `ReleasedDefinition` in the sibling model uses a composite key; the asymmetry is unjustified.
*Remediation:* add a uniqueness invariant on `(subjectRef, version)` and on `(subjectRef, contentDigest)`; `editionId` stays the surrogate.
*Fixture:* negative `duplicate-edition-version` — a second edition with an existing `(subjectRef, version)` is rejected.

**D2 — `Edition.subjectRef` is an undiscriminated polymorphic reference.**
An edition may be of a `Method` or of a `Procedure`. WM-ACT-003 pins a field named `methodEditionRef`. Nothing resolves which kind a given pin denotes.
*Remediation:* add `subjectKind ∈ {method, procedure}` to `Edition`; rename the WM-ACT-003 pins to `knowledgeEditionRef/Digest` or constrain them to `subjectKind = method`.
*Fixture:* negative `edition-kind-ambiguous-pin` — a definition pinning a procedure-kind edition through a method-typed pin is rejected.

**D3 — `variantKeyOrNone` cannot resolve a `ReleasedDefinition`.**
`ReleasedDefinition.identity = (processId, variantKey, version)` requires a variant key, but `ProcessInstance` and `StepExecution` are permitted to pin `variantKeyOrNone`. An instance with "none" pins a definition that cannot be keyed.
*Remediation:* make `variantKey` mandatory with a reserved sentinel value for single-variant families; delete `variantKeyOrNone` from both pin sets.
*Fixture:* negative `instance-pins-no-variant` — an instance pinning "none" is rejected; positive `default-variant-resolution` — the sentinel resolves to exactly one released definition.

**D4 — `ConformanceResult` admits duplicate identity for the same input tuple.**
Identity is the opaque `conformanceResultId`, while the reproducibility invariant names `(definitionDigest, methodEditionDigest, traceDigest, ruleSetVersion)`. Two non-equal results over the same inputs can coexist, both immutable, both authoritative.
*Remediation:* define `resultDigest` as a digest over the input tuple plus the emitted measures, excluding `conformanceResultId` and `computedAt`; forbid two results with equal input tuples and unequal measures.
*Fixture:* negative `contradictory-conformance-results`; positive `recompute-is-byte-identical`.

**D5 — Three live identifier surfaces for each model.**
`vercy:world:k3` / `k6` (legacy manifest), `WM-ACT-003` / `WM-ACT-009` (model id), `vr.wm-act-003` / `vr.wm-act-009` (registry id), plus `existing_spec_ref` still pointing at `models/activity-work/K3-*.md` and `K6-*.md` and `legacy_alias` `K3`/`K6`.
*Remediation:* bind `vercy:world:k3`/`k6` permanently to `0.2.0-legacy` and forbid minting any `0.3.x` under them; keep `K3`/`K6` only in `legacy_alias`; record the spec-path rename as a registry action, not a silent edit.
*Fixture:* negative `legacy-id-reuse` — a `0.3.0` assembly declaring `vercy:world:k3` is rejected.

### B. Mutable historical meaning

**D6 — `Procedure` and `ProcedureStep` are not edition-qualified.**
`ProcedureStep.identity = (procedureId, stepKey)`; neither it nor `Procedure` carries an edition binding or digest, while `CompetenceRequirement` correctly keys on `editionId`. Instruction text is therefore mutable in place under a pinned edition. **This alone leaves the contour's negative case reachable** even though the legacy `procedureRevised` event was retired.
*Remediation:* key `ProcedureStep` on `(editionId, procedureId, stepKey)` and require `Procedure` content to be edition-scoped; `Edition.contentDigest` must cover the full procedure and step set it publishes.
*Fixture:* negative `procedure-step-edited-under-released-edition` — rejected; positive `edition-digest-covers-steps` — the digest changes if any step text changes.

**D7 — The pin chain does not close from execution to instruction text.**
A `StepExecution` pins a method edition, but the instructions actually followed live in procedures that are separately editioned (D6). A closed instance can be re-resolved to different instruction text without any pin changing.
*Remediation:* require that a method edition's manifest transitively pins the exact procedure edition ids and digests it incorporates, and that pin resolution is digest-checked end to end.
*Fixture:* positive `closed-pin-chain-replay` — replaying a completed instance after a new procedure edition returns the original instruction text.

**D8 — Immutable records carry mutable status.**
`StepExecution` (`lifecycle: started/completed/failed/compensated`, `status` required), `ProcessInstance` (`status`, `completedAt`, `terminationReason`, `cutoverRefs`), `Deviation.status`, `Compensation.status` and the whole of `WorkItem` are single rows with transitioning state, directly contradicting the invariants "trace records are immutable" and "trace order is append-only".
*Remediation:* declare exactly which objects are immutable events and which are derived current-state projections. Events carry the value at record time; every transition is a new event. `ProcessInstance` status, `StepExecution` status and `WorkItem` status become derived, never authoritative, never stored as truth.
*Fixture:* negative `instance-status-written-directly`; positive `status-derived-from-events`.

**D9 — `compensated` as a `StepExecution` lifecycle value mutates a historical record.**
Marking an already-written execution `compensated` edits history; the `Compensation` object already carries the fact.
*Remediation:* remove `compensated` from `StepExecution.lifecycle`; derive it from the existence of a `Compensation` whose `targetExecutionRef` resolves to it.
*Fixture:* negative `compensation-marks-original` — rejected.

**D10 — `CutoverRecord` may be backdated and has no sequence.**
It carries `effectiveAt` and `recordedAt` but no `eventSequence`, and no invariant forbids `effectiveAt` earlier than already-written trace records. A backdated cutover retroactively reassigns pins of completed steps — the negative case by a second route.
*Remediation:* add `eventSequence`; add the invariant that a cutover binds only records whose sequence is strictly greater than its own and never alters pins already written; require `effectiveAt ≥ recordedAt` of the last trace record or an explicit, separately authorized backdating flag.
*Fixture:* negative `backdated-cutover-repins-closed-steps`; positive `cutover-binds-only-later-steps`.

**D11 — `AdoptionRecord` has no `recordedAt` and permits backdated effectivity.**
`effectiveFrom`/`effectiveTo` exist with no record time. A backdated adoption rewrites which edition "was in force" and desynchronizes the adoption ledger from trace pins.
*Remediation:* add `recordedAt`; forbid `effectiveFrom < recordedAt` unless an explicit authorized backdating record is attached; trace pins always prevail over later adoption arithmetic.
*Fixture:* negative `backdated-adoption-without-authority`.

**D12 — Edition withdrawal may break resolution of historical pins.**
`Edition.lifecycle` includes `withdrawn` with no rule preserving resolvability of a withdrawn edition that closed traces still pin.
*Remediation:* invariant — withdrawal ends recommended and new adoption only; a pinned edition remains permanently resolvable with its digest.
*Fixture:* positive `withdrawn-edition-still-resolves-for-closed-trace`.

### C. False execution evidence

**D13 — Required `methodEditionRef` forces fabricated knowledge pins.**
`ReleasedDefinition.required.methodEditionAdoptionRef`, `ProcessInstance.required.{methodEditionRef, methodEditionDigest, adoptionRecordRef}` and the `required: true` relation to `vr.wm-act-009` make a method edition mandatory. Processes that codify no published method cannot be recorded without inventing an edition and an adoption.
*Remediation:* make knowledge-edition pins zero-to-many at definition, instance and step level; require them only where the definition asserts it operationalizes a method. Downgrade the 003→009 relation to `required: false`.
*Fixture:* positive `method-less-process-instance`; negative `synthetic-edition-to-satisfy-required-pin`.

**D14 — A single method-edition pin per step cannot express multi-method or no-method steps.**
`StepExecution.required` binds exactly one edition, forcing false attribution.
*Remediation:* `knowledgeEditionRefs[]` with paired digests, zero-to-many, mirroring `actRefs`.
*Fixture:* positive `step-realizes-two-editions`; positive `step-realizes-none`.

**D15 — `performerRef` required on every `StepExecution`.**
System-performed steps and steps whose performer evidence was lost cannot be recorded without fabricating a performer.
*Remediation:* permit `performerRef` to be a system actor or absent; absence requires an explicit deviation of kind `performer-unknown`, on the same pattern as the authorization gap.
*Fixture:* positive `execution-with-unknown-performer-and-deviation`; negative `execution-with-unknown-performer-no-deviation`.

**D16 — `Deviation.required.evidenceRefs` contradicts the loss-of-evidence case.**
Fixture `execution-with-deviation` is premised on assignment evidence having been lost, yet evidence references are mandatory. Recorders will attach placeholder evidence.
*Remediation:* allow empty `evidenceRefs` when `evidenceAbsentReason` is present; forbid both empty.
*Fixture:* positive `deviation-with-declared-absent-evidence`; negative `deviation-with-empty-evidence-and-no-reason`.

**D17 — `Deviation.kind` has no closed vocabulary.**
Fixtures depend on `manual-exception` and an authorization-gap kind; nothing enumerates them, so conformance over deviation kinds is not reproducible.
*Remediation:* publish a closed, versioned `deviationKind` enum; reference its version in `ConformanceResult.ruleSetVersion` scope.
*Fixture:* negative `unknown-deviation-kind`.

**D18 — "Rejected until a deviation is appended" is unimplementable in an append-only store.**
Fixture `execution-without-assignment` rejects a write whose remedy is a later append; the execution must either have been accepted first or the pair must be atomic.
*Remediation:* state that the execution and its authorization-gap deviation are written in one atomic append unit; otherwise the gap is a validator finding, not a write rejection.
*Fixture:* replace with negative `atomic-unit-missing-gap-deviation` and positive `atomic-execution-plus-gap-deviation`.

### D. Non-reproducible conformance

**D19 — `ConformanceResult` cannot express a cut-over instance.**
It binds one `definitionRef/digest` and one edition pin, while `mid-flight-cutover` and `compensation-with-cutover` require that two pin regimes remain reproducible within one instance. The fixtures and the object contradict each other outright.
*Remediation:* carry an ordered `pinRegimes[]` (fromSequence, toSequence, definitionRef+digest, editionRef+digest, cutoverRef) and compute measures per regime plus an aggregate.
*Fixture:* positive `conformance-across-cutover` — per-regime and aggregate measures, both reproducible.

**D20 — Digest semantics undefined.**
`contentDigest`, `definitionDigest`, `methodEditionDigest`, `traceDigest`, `resultDigest`, `editionDigest` have no algorithm, no canonical serialization and no mismatch rule. Content addressing is asserted, not achieved.
*Remediation:* pin a digest algorithm and canonicalization per object class; a pin whose digest does not equal the referent's digest is a hard rejection.
*Fixture:* negative `digest-mismatch-on-pin`; positive `canonicalization-stability` (reordered equivalent serializations yield one digest).

**D21 — `computedAt` inside an immutable, reproducible result.**
Reproducibility requires byte-identical recomputation; `computedAt` guarantees difference unless excluded from the digest domain.
*Remediation:* define the digest domain explicitly as inputs plus measures; `computedAt` and identifiers sit outside it.
*Fixture:* covered by `recompute-is-byte-identical` (D4).

**D22 — `supersedesResultRef` can be used to supersede a historical result with a counterfactual.**
The invariant forbids replacement, the field name invites it.
*Remediation:* split into `priorResultRef` (non-superseding, mandatory on `counterfactual = true`) and `supersedesResultRef` (same pin regime, new `ruleSetVersion` only); forbid `supersedesResultRef` when `counterfactual = true`.
*Fixture:* negative `counterfactual-supersedes-historical`.

**D23 — Outcome vocabulary undefined.**
The invariant forbids a "conformance pass" under partial coverage, but no field carries a pass/fail outcome and `coverage`, `fitness`, `alignment` have no value domains.
*Remediation:* enumerate `coverage ∈ {complete, partial, unknown}`, define the numeric domains of `fitness`/`alignment`, and state the derivation rule that no outcome above "inconclusive" may be emitted when coverage ≠ complete.
*Fixture:* strengthen `missing-trace-conformance` to assert the emitted outcome value, not only that it is "never pass".

**D24 — Monotonic ordering exists only on `StepExecution`.**
`eventSequence` is absent from `Deviation`, `Compensation`, `CutoverRecord` and work-item transitions, so `event-correction`'s expectation that "successor is ordered after it" is unprovable across record types, and `traceDigest` has no defined ordering to digest.
*Remediation:* `eventSequence` mandatory on every trace record, strictly monotonic per instance, and the defined sort key for `traceDigest`.
*Fixture:* negative `trace-record-without-sequence`; positive `cross-type-ordering-replay`.

### E. Assignment / execution confusion

**D25 — `WorkItem` is a mutable row masquerading as a lifecycle.**
Six lifecycle states with timestamps for only three (`offeredAt`, `claimedAt`, `expiredAt`); `assigned`, `released`, `completed`, `cancelled` have no recorded time, and `claimed` versus `assigned` versus `released` have no transition rules.
*Remediation:* model transitions as append-only `WorkItemEvent` records with `eventSequence`, reason and actor; `WorkItem.status` becomes derived.
*Fixture:* negative `work-item-status-edited-in-place`; positive `work-item-lifecycle-replay`.

**D26 — `assignmentRef` is optional on `WorkItem` and on `StepExecution` with no linking rule.**
Two independent optional references to the authorizing assignment, with no invariant that an execution's assignment must be the one carried by its work item.
*Remediation:* invariant — where both exist they must resolve to the same assignment; divergence is a deviation.
*Fixture:* negative `execution-cites-foreign-assignment`.

**D27 — `escalationRefs` and `assignmentGapRef` are dangling types.**
Neither an escalation object nor an assignment-gap object exists in either candidate.
*Remediation:* define escalation as a work-item event kind; define the authorization gap as a deviation kind (D17) and drop `assignmentGapRef` or type it to `Deviation`.
*Fixture:* negative `dangling-escalation-ref`.

### F. Unsupported identifiers and release claims

**D28 — Required dependency on identifiers absent from the frozen dossier.**
`vr.wm-act-006` (Task) is a `required: true` relation and `taskRef` is a required field; `vr.wm-org-016` is referenced as well. Neither appears in `registry_reservations`, the relationship ledger, `related_research_contours` or `research_status`. They entered through the Grok study as asserted neighbours (together with `WM-ACT-007`, likewise unevidenced), and the fixture `work-item-task-mastership` elevates one of them to a normative rejection rule. This is an external fact the audit cannot confirm.
*Remediation:* downgrade the 003→006 relation to `required: false`, make `taskRef` optional, and record an explicit hold "external registry ids `vr.wm-act-006` and `vr.wm-org-016` unverified against the reservation registry". Do not mint a local Task master in the interim; a work item with no verified task reference simply carries none.
*Fixture:* re-label `work-item-task-mastership` as blocked-by-hold; add negative `local-task-master-created` (still rejected) and positive `work-item-without-verified-task-ref`.

**D29 — `entryKind` values are unregistered vocabulary.**
Registry reserves `standalone-mm` for both rows; candidates assert `aggregate` and `knowledge-aggregate`, the latter appearing nowhere in the dossier.
*Remediation:* either keep `standalone-mm` or register the new enum with a recorded registry change action; do not introduce a one-off kind for 009 alone.
*Fixture:* negative `unregistered-entry-kind`.

**D30 — Preserving the legacy assemblies preserves their unsupported claims.**
`0.2.0-legacy` carries `muc: "2.0: Conformant"`, `mmas: A1` and wildcard imports (`bpmn`, `cmmn`, `iso-management-systems`, `iso-9001` at `"*"`). The dossier supports none of them. Immutability forbids editing the assemblies; the candidates record no retraction.
*Remediation:* attach an external, versioned claim-retraction note bound to each legacy assembly stating that MUC 2.0, MMAS A1 and all wildcard-import conformance are unverified and non-installable. Never edit the frozen assembly.
*Fixture:* negative `legacy-claim-surfaced-as-conformance`; positive `legacy-retraction-note-resolves`.

**D31 — Candidates carry no imports section at all.**
Wildcards were removed by deletion rather than by declaring pinned alignment-only references. Nothing positively asserts what BPMN/CMMN/ISO relationship is claimed.
*Remediation:* add an `alignments[]` block with pinned source versions and an explicit `claim: alignment-only` marker; absence of a pin means absence of the alignment.
*Fixture:* positive `pinned-alignment-declared`, paired with the existing negative `standards-claim`.

**D32 — Every `*Ref` field is untyped.**
`ownerRef`, `subjectRef`, `authorityRef`, `attestationRef`, `resultRef`, `causeRef`, `resolutionRef`, `remountRef`, `evidenceRuleRef`, `competenceRef`, `adopterRef`, `authorRef` name no target registry. Unverifiable resolution invites silent local mastership of externally mastered things.
*Remediation:* each reference field declares a target registry id or an explicit `external-unmastered` marker with a resolution rule.
*Fixture:* negative `untyped-reference-field`.

**D33 — `CutoverRecord.authorityRef` and `AdoptionRecord.authorityRef` carry no authority rule.**
"Authorized" is asserted throughout the invariants with no statement of who may authorize.
*Remediation:* bind cutover authority to the process owner or a delegation record, and adoption authority to the adopter organization; an unresolvable or out-of-scope authority invalidates the record.
*Fixture:* negative `cutover-by-unauthorized-party`; the existing `adoption-without-attestation` extends to authority scope.

### G. Silently dropped semantics

**D34 — `trigger`, `input_contract` and `output_contract` have no home.**
Present in both the v1 predecessor fields (OPS-01, non-normative) and the 0.2.0-legacy `process` object (`trigger`), absent from `ReleasedDefinition`, with no recorded decision to drop them.
*Remediation:* either add `trigger`, `inputContract`, `outputContract` to `ReleasedDefinition` or record an explicit non-carry decision with rationale. Same treatment for legacy `step` entry/exit conditions and expected duration.
*Fixture:* positive `definition-carries-trigger-and-contracts` (or a recorded non-carry decision referenced by the candidate).

**D35 — Contracts, projections and stewardship are absent from both candidates.**
Both legacy assemblies declared access contracts (`definitionAccess`, `executionMonitoring`, `benchmarkExchange`, `methodAccess`, `adoptionAttestation`, `revisionSubscription`), projections and S1/S2/S4 stewardship. The candidates declare none, so nothing governs disclosure of execution data through aggregate projections, and nothing states method licensing — while a blocking decision explicitly requires confirmation of rights and source mastership.
*Remediation:* restore contract, projection and stewardship sections with the ownership split already agreed (author owns editions, adopter owns adoption records, process owner owns definitions and trace), including de-identification rules for aggregate exchange and licensing terms for method access.
*Fixture:* negative `benchmark-projection-leaks-case-identity`; negative `adoption-without-access-right`.

**D36 — No reconciliation of erasure with append-only immutability.**
`performerRef` identifies people; no retention, tombstone or erasure semantics exist. The first erasure obligation will force a mutation of history or an unresolvable pin — the exact failure the model is built to prevent, and one of the criteria Claude named for a future trace split.
*Remediation:* define tombstoning that removes referent content while preserving record identity, sequence and digest; state that erasure never removes a trace record or changes a digest.
*Fixture:* positive `tombstoned-performer-preserves-trace-digest`.

## 5. Contradictions among dossier, providers, candidates and fixtures

**C1 — Status ledger versus the present artefacts.** `queue_reservation` says `status: queued`, `claude_status: not-started`, `grok_status: not-started`, `boundary_decision: pending`; `research_status` for both models says `claude_status: queued`, `grok_status: queued`, `synthesis_status: blocked-on-providers`. Both provider studies exist and a boundary comparison exists. Either the studies are outside the reservation process or the ledger is stale. The ledger must be updated to provider-complete while `validation_status` stays `not-valid-or-not-run`; nothing here licenses changing `validation_status`.

**C2 — Relationship ledger versus candidate relations.** The ledger holds `WM-ACT-003 COMPOSE WM-ACT-002` ("process is composed of acts"); the candidate states REFERENCE, optional, zero-to-many. The ledger's `REFERENCE → WM-KNW-012` (governing policies) is dropped from the candidate entirely, replaced by an unnamed "external knowledge masters" delegation. Claude flagged both; the comparison did not resolve either and asserts "no contradiction changes the boundary decision". The divergence must be recorded as a proposed ledger amendment, not left implicit.

**C3 — Registry `composition_role` versus candidate.** `vr.wm-act-003` reserves `COMPOSE;REFERENCE` and `default_link_type: TYPED-EDGES`; the candidate declares REFERENCE relations only. `vr.wm-act-009` reserves all three fields empty while the candidate declares two REFERENCE relations. Both rows need reconciliation.

**C4 — Providers on mid-flight rebinding.** Claude permitted later steps to bind a newly adopted edition mid-flight; Grok required an explicit cutover. The comparison adopted the stricter rule. This is correctly resolved and is recorded here only so the weaker Claude rule is not reintroduced during remediation.

**C5 — Grok's neighbour claims are unevidenced.** `WM-ACT-006`, `WM-ORG-016` and `WM-ACT-007` ("already pins a procedure version") are asserted as existing registry neighbours; the frozen dossier contains none of them. The comparison inherited them as settled. See D28.

**C6 — Held cardinality versus a positive fixture.** The 003→002 relation is `zero-to-many pending crosswalk` and is listed under holds, yet fixture `one-step-many-acts` is a positive expectation that two act references are retained. A positive fixture pre-empts a held question; mark it provisional.

**C7 — Required evidence versus the evidence-loss fixture.** `Deviation.required.evidenceRefs` against `execution-with-deviation`. See D16.

**C8 — Single-regime `ConformanceResult` versus the cutover fixtures.** See D19. This is the sharpest internal contradiction: two fixtures demand an output the object cannot represent.

**C9 — Immutability invariants versus mutable status fields.** The invariant sets of both candidates assert append-only immutable records while the object definitions give instances, executions, deviations, compensations and work items transitioning status. See D8.

**C10 — `AdoptionRecord.attestationRef` is both required and optional** in the same object definition, and `adoptionId` is listed both as identity and as a required field. The invariant "every effective adoption has an authority and attestation reference" implies the requirement is conditional on `status = effective`, which the `proposed` lifecycle state contradicts.

**C11 — Definition-level versus instance-level knowledge pins.** `ReleasedDefinition` carries one combined `methodEditionAdoptionRef`; instances and executions carry three separate pins (`methodEditionRef`, `methodEditionDigest`, `adoptionRecordRef`). No invariant ties instance pins to the definition's. An instance may pin a definition and an unrelated edition, producing a false composition claim. Additionally, binding an adoption record at definition level couples an authored definition to one adopter, while adoption is adopter-scoped.

**C12 — Fixture target asymmetry.** `legacy-installability` and `release-gate` target only `WM-ACT-003`, although both holds and both `publishableCanonical: false` / `fixturesExecuted: false` gates apply equally to `WM-ACT-009`. The 009 legacy assembly has no preservation fixture at all.

**C13 — Overlapping adoption is unconstrained.** Nothing forbids two concurrently effective `AdoptionRecord`s for the same adopter and subject with overlapping intervals, making "the effective adoption" at an instant non-deterministic — which the fixture `publication-without-adoption` ("keep the prior effective adoption") presumes to be singular.

**C14 — `localConstraints` versus edition immutability.** An adopter-side free field may narrow or alter a method locally, creating an uncontrolled variant of authored knowledge outside the edition lineage. It must be constrained to narrowing only and digested, or removed.

**C15 — `Procedure.methodId` required** forbids a procedure shared by two methods, forcing duplicated instruction text under two identities — a duplicate-identity pressure the edition model will then propagate.

## 6. Remediation checklist (closed)

1. Fix `Edition` identity: uniqueness on `(subjectRef, version)` and `(subjectRef, contentDigest)`; add `subjectKind`. [D1, D2]
2. Remove `variantKeyOrNone`; mandatory `variantKey` with a reserved default sentinel. [D3]
3. Make `ProcedureStep` and procedure content edition-keyed; `Edition.contentDigest` covers the published step set. [D6]
4. Close the pin chain: method editions transitively pin procedure edition ids and digests; resolution is digest-checked end to end. [D7]
5. Separate immutable events from derived current state across `ProcessInstance`, `StepExecution`, `Deviation`, `Compensation` and `WorkItem`; remove `compensated` from `StepExecution.lifecycle`. [D8, D9, D25]
6. Add `eventSequence` to every trace record including `CutoverRecord` and work-item events; define it as the sort key of `traceDigest`. [D24, D10]
7. Forbid backdated cutover and backdated adoption from repointing written records; add `recordedAt` to `AdoptionRecord`. [D10, D11]
8. Guarantee permanent resolvability of withdrawn editions pinned by closed traces. [D12]
9. Make knowledge-edition pins zero-to-many at definition, instance and step level; downgrade the 003→009 relation to non-required. [D13, D14]
10. Permit system and unknown performers with an explicit deviation kind. [D15]
11. Permit absent deviation evidence with `evidenceAbsentReason`; forbid silent absence. [D16]
12. Publish a closed, versioned `deviationKind` enum. [D17]
13. Restate the authorization-gap rule as an atomic execution-plus-deviation append unit. [D18]
14. Give `ConformanceResult` ordered `pinRegimes[]` so cut-over instances are representable. [D19]
15. Pin digest algorithms and canonicalization for every digest field; digest mismatch is a hard rejection. [D20]
16. Define the `resultDigest` domain excluding identifiers and `computedAt`; forbid contradictory results over one input tuple. [D4, D21]
17. Split `supersedesResultRef` from `priorResultRef`; forbid supersession by a counterfactual. [D22]
18. Enumerate `coverage`, `fitness`, `alignment` domains and the no-pass-under-partial-coverage derivation. [D23]
19. Add the invariant that work-item and execution assignment references must agree; divergence is a deviation. [D26]
20. Define escalation as a work-item event kind and retype or drop `assignmentGapRef`. [D27]
21. Downgrade `vr.wm-act-006` and `vr.wm-org-016` to non-required with an explicit unverified-identifier hold; make `taskRef` optional; re-label the dependent fixture as blocked. [D28, C5]
22. Reconcile `entryKind` with the reserved `standalone-mm` or register the new vocabulary. [D29]
23. Attach external, versioned claim-retraction notes to both `0.2.0-legacy` assemblies covering MUC 2.0, MMAS A1 and wildcard imports; do not edit the assemblies. [D30]
24. Add an `alignments[]` block with pinned sources marked alignment-only. [D31]
25. Type every reference field to a target registry id or an explicit external-unmastered marker. [D32]
26. Define cutover and adoption authority scope; unresolvable or out-of-scope authority invalidates the record. [D33]
27. Restore or explicitly waive `trigger`, `inputContract`, `outputContract`, step entry/exit conditions and expected duration, with a recorded decision. [D34]
28. Restore contracts, projections and stewardship, including de-identification for aggregate exchange and method-access licensing. [D35]
29. Define tombstoning that preserves record identity, sequence and digest under erasure obligations. [D36]
30. Resolve the duplicated `attestationRef` and redundant `adoptionId` in `AdoptionRecord`; gate attestation and authority on `status = effective`. [C10]
31. Tie instance and execution knowledge pins to the pinning definition; move adoption-record resolution to instance scope and split the combined `methodEditionAdoptionRef`. [C11]
32. Add a single-effective-adoption invariant per `(adopter, subject, instant)` or an explicit precedence rule. [C13]
33. Constrain `localConstraints` to digested narrowing, or remove it. [C14]
34. Allow a procedure to serve more than one method, or record the one-method restriction as a deliberate constraint. [C15]
35. Record the `COMPOSE` versus `REFERENCE` divergence on `WM-ACT-002` and the dropped `WM-KNW-012` relation as proposed ledger amendments; reconcile registry `composition_role`, `default_link_type` and `relations_ref` on both rows. [C2, C3]
36. Update `queue_reservation` and `research_status` to provider-complete; leave `validation_status` at `not-valid-or-not-run` and `boundary_decision` recorded as complete-both. [C1]
37. Mark `one-step-many-acts` provisional pending the atomic-act crosswalk. [C6]
38. Extend `legacy-installability` and `release-gate` to `WM-ACT-009` and add a 009 legacy-preservation fixture. [C12]
39. Bind `vercy:world:k3` / `vercy:world:k6` permanently to `0.2.0-legacy`; record the K3/K6 spec-path rename as a registry action. [D5]
40. Execute the full fixture set — declarative status is insufficient — before any change to `fixturesExecuted`, `publishableCanonical`, installability, or any crosswalk, mastership or standards claim. All existing holds on both candidates remain open; this audit lifts none of them.
