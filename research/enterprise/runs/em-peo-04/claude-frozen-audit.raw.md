# FROZEN SEMANTIC AUDIT — EM-PEO-04 (candidateRevision 2)

## 1. Verdict

**REVISE.**

The two-root decomposition and the no-allocation posture are sound. The dossier fails on representability: a large share of its strongest invariants (seat cap, approval attribution, stage-release pinning, retention, outcome) have no field in `objects` that could carry them, so they are unfalsifiable prose rather than model content. Five named constituents of the hiring chain have no declared owner anywhere in the dossier.

## 2. Minimum model set and allocation decision

**Confirmed — no new identifier now.** `modelId`, `registryId` are null, `allocationState` is `unassigned`, `newRuntimeId` is false, and no placeholder identifier is used anywhere in the dossier. This is correct and must hold at minimum until (a) WM-ORG-008 has an actual spec, and (b) approved relation rows exist for WM-ORG-008 and WM-ACT-039 (`sourceFacts.relations` says none do).

**Confirmed — both new roots are justified.**
- *Recruitment Requisition* passes the identity test independently of WM-ORG-008: `standing-no-opening` demonstrates an authorization that exists with zero openings, so it cannot be a profile over Opening; it outlives openings, campaigns and fills; mastership is workforce-demand authority, not applicant tracking.
- *Candidacy* passes independently of WM-PER-001 (role, not identity), WM-ACT-039 (per-person participation, not process design) and WM-ORG-008 (survives the opening and exists without one).

**Rejected — the set is not complete.** Five constituents named in the audit scope have no owner in any model, profile or exclusion:
- **Posting** — declared "a dependent artifact, not an allocated root," but no host is named. Requisition explicitly excludes "posting publication identity"; Candidacy does not mention it; no base is assigned. Publication is therefore untraceable.
- **Selection decision** — profile constraint says it "remains an authorized record," but **WM-REC-010 is absent from `profile.bases`** and is cited only by Requisition for *approval*. No model owns selection.
- **Recommendation** — asserted distinct from score and decision, owned by nothing.
- **Assignment** and **Contract** — excluded by both roots, absent from bases, not declared out-of-contour with a deferral. `WM-ORG-005` covers Employment only, yet "Placement is downstream Employment plus Assignment."

Also unresolved: `WM-ORG-016` appears once, in `recruitmentRequisition.holds`, and nowhere else — no base, no reference, no source fact.

## 3–4. Defects, remediation, fixture expectations

### A. Identity coverage

**A1 — Posting has no owner.** Publication acts (channel, jurisdiction, content version, publish/withdraw times) cannot be recorded, so "Opening or posting closure never silently closes the requisition" dangles on an unmodelled thing.
*Fix:* declare Posting a dependent artifact of WM-ACT-039 with a local (non-root) identifier, required `channel`, `contentReleaseRef`, `jurisdiction`, `publishedAt`, `withdrawnAt`, and a reference to at most one asserted Opening; add to Candidacy `optional.postingRef` as provenance only.
*Fixture:* `posting-multichannel-withdrawal` — one opening published to two channels, one withdrawn — *expect:* two posting artifacts with distinct withdrawal times, opening and requisition unchanged, neither posting acquiring root identity.

**A2 — Selection decision unhomed; WM-REC-010 missing from bases.**
*Fix:* add `WM-REC-010` to `profile.bases`; add a profile constraint that selection decisions are WM-REC-010 records with required `actorRef`, `authorityRef`, `decidedAt`, `candidacyRef`, `reason`; add `optional.selectionDecisionRefs` to Candidacy.
*Fixture:* `selection-decision-has-owner` — a rejection is recorded with no decision record — *expect:* rejected; status alone may not carry a selection outcome.

**A3 — Recommendation unhomed.**
*Fix:* declare Recommendation a WM-ACT-039 process result with `recommenderRef`, `basisRefs`, `recommendedAt`, explicitly non-binding.
*Fixture:* `recommendation-is-not-decision` — a panel recommendation is recorded and no decision follows — *expect:* valid state; candidacy does not advance to `selected`.

**A4 — Assignment and Contract unhomed and not deferred.**
*Fix:* add an explicit out-of-contour declaration naming the intended owning contour, or add holds; do not leave them only as exclusions.
*Fixture:* `downstream-out-of-contour` — an accepted offer is asked to produce an assignment inside EM-PEO-04 — *expect:* rejected as out of contour, with the deferral cited.

**A5 — Dangling `WM-ORG-016`.**
*Fix:* either add it to `sourceFacts` with its reservation status and the reason it is coupled to this contour, or remove the mention.
*Fixture:* `no-unsourced-identifier` — dossier lint over every identifier token — *expect:* every identifier appears in `sourceFacts` or `bases`.

**A6 — Derived vacancy has no derivation contract.** "Derived vacant capacity never creates an asserted opening" is unfalsifiable without stated inputs and a non-persistence rule.
*Fix:* define the projection as `WM-ORG-004` authorized capacity minus active `WM-ORG-005` employments and accepted-not-started offers, at an instant; state it is never stored as an entity and never referenced by `openingRefs`.
*Fixture:* `derived-vacancy-not-referenced` — a projection result is stored and cited in `openingRefs` — *expect:* rejected.

### B. Seat authority

**B1 — No authorized seat cap field.** `requestedHeadcount` is a *request*; the cap invariant and `seat-cap-overrun` reference an authority that has no representation, so requested headcount will be used as authority.
*Fix:* add required-on-approval `authorizedSeatCap` distinct from `requestedHeadcount`; forbid cap presence before `approved`.
*Fixture:* `requested-is-not-authorized` — a draft with `requestedHeadcount` 3 is treated as authorizing 3 seats — *expect:* rejected; no cap exists before approval.

**B2 — No cap-change history or attribution.** The boundary claims "attributable cap-change history"; no field carries it.
*Fix:* add `capChangeHistory[]` with `previousCap`, `newCap`, `decisionRef` (WM-REC-010), `actorRef`, `validFrom`, `recordedAt`; cap changes only via appended entries.
*Fixture:* `cap-raise-without-decision` — cap moves 2→3 with no decision reference — *expect:* rejected.

**B3 — No fill accounting.** "Partial fill preserves remaining authorized headcount explicitly" — no `remainingHeadcount` or derivation rule exists.
*Fix:* define `remainingHeadcount = authorizedSeatCap − consumedSeats` as a stated derivation, and define `consumedSeats` (see B4); require `partially-filled` iff `0 < consumedSeats < authorizedSeatCap`.
*Fixture:* `partial-fill-arithmetic` — cap 2, one fill — *expect:* status `partially-filled`, remaining 1, both derivable from recorded facts.

**B4 — Cap arithmetic double-counts.** "Non-cancelled fills plus outstanding accepted offers" leaves an accepted offer that has become an employment countable twice; `fillRefs` is untyped (Employment? Assignment? an event?).
*Fix:* type `fillRefs` as WM-ORG-005 employment references; define `outstanding accepted offer` as accepted, not cancelled, and not yet converted to a referenced employment; `consumedSeats = |non-cancelled fills| + |outstanding accepted offers|`.
*Fixture:* `accepted-offer-then-employment` — an accepted offer converts to employment — *expect:* consumed seats stay 1 across the conversion.

**B5 — No aggregation path from requisition to offers.** Offers hang off Candidacy; Requisition has no offer visibility and `openingRefs` is optional, so the cap invariant cannot be evaluated on the Requisition.
*Fix:* make `requisitionRef` required on Candidacy whenever a requisition exists in the effort scope, and declare Candidacy→Requisition the authoritative direction for cap aggregation; Requisition-side `openingRefs`/`campaignRefs`/`fillRefs` become derived indexes.
*Fixture:* `cap-evaluable-from-requisition` — cap 1, two accepted offers under two candidacies on different openings of one requisition — *expect:* rejected at the requisition, not only per-opening.

### C. History and versioning

**C1 — No version identity and no backward link.** Both roots claim immutable versions but carry only `successorRef`; there is no version identifier distinct from the entity identifier and no predecessor.
*Fix:* add `versionId` (identity `[entityId, versionId]`) and `predecessorRef` to both objects; entity id is stable across versions.
*Fixture:* `version-chain-traversal` — three versions with the middle one queried — *expect:* both neighbours resolvable from the middle version.

**C2 — Corrections are not attributable.** Invariants demand "attributable successors"; no actor field exists.
*Fix:* add required `recordedBy` to both objects and required `correctionReason` on any successor whose `validFrom` precedes its `recordedAt`.
*Fixture:* `unattributed-correction` — a backdated headcount correction with no `recordedBy` — *expect:* rejected (strengthens `recorded-time-correction`).

**C3 — `approved` and `funded` states are unbacked.** `approvalDecisionRefs` is optional in every state, so "Approved need is an attributable decision record and never the requisition identity" collapses into a status flag.
*Fix:* conditionally require at least one `approvalDecisionRef` for `approved`, `funded`, `open`, `partially-filled`, `filled`.
*Fixture:* `approved-without-decision` — status set to `approved`, no decision reference — *expect:* rejected.

**C4 — Funding has no authority or commitment field**, while an invariant insists a budget reference is not a substitute for one.
*Fix:* add `fundingAuthorityRef` and `fundingCommitmentRef`; require at least `fundingAuthorityRef` for `funded`.
*Fixture:* `budget-as-funding` — `funded` justified by `budgetRef` alone — *expect:* rejected.

**C5 — No transition matrix; reopening is unguarded.** Nothing prevents `closed → open` or `cancelled → open`, which silently reuses spent authority.
*Fix:* publish the legal transition set; make `cancelled` and `closed` terminal; reuse requires a new requisition citing `predecessorRef`.
*Fixture:* `closed-reopened` — a closed requisition returns to `open` — *expect:* rejected; a successor requisition is required.

**C6 — Candidacy outcome is not representable.** A hired candidacy and an abandoned one both end `closed`; `offered` is listed after `rejected`/`withdrawn` with no ordering semantics; offer-declined-by-candidate is indistinguishable from withdrawal.
*Fix:* declare the lifecycle an unordered state set; add required-on-close `outcome` ∈ {hired, not-selected, declined-by-candidate, withdrawn-by-candidate, withdrawn-by-employer, lapsed} plus `outcomeReason` and `outcomeDecisionRef`.
*Fixture:* `hired-vs-closed` — one hired and one abandoned candidacy both close — *expect:* distinguishable by `outcome` without consulting Employment.

**C7 — Bidirectional references with no authoritative direction** (`openingRefs`/`campaignRefs`/`fillRefs` vs Candidacy's `requisitionRef`/`openingRef`/`campaignRef`) permit divergent histories.
*Fix:* per C5/B5, declare the child-to-parent direction authoritative and all parent-side collections derived.
*Fixture:* `reference-divergence` — a candidacy names requisition R, R's derived index omits it — *expect:* the index is wrong, not the candidacy.

**C8 — "Historical requisitions remain resolvable after closure" has no mechanism against disposition.** Purged candidacy artifacts leave dangling references.
*Fix:* require tombstones on disposition — reference resolves to `{disposed, disposedAt, dispositionBasis}` — never to absence.
*Fixture:* `disposed-reference-resolves` — a decision cites a purged CV — *expect:* reference resolves to a tombstone; no dangling reference and no restored content.

### D. Candidacy scope and process

**D1 — Direct contradiction on scope.** Invariant 1 ("One candidacy binds one person, **one opening, one recruitment process** and an interval") contradicts `scopeRule`, invariant 13, and the profile's internal-mobility constraint; `processRef` is also merely optional.
*Fix:* restate invariant 1 as "one person, one recruiting-effort scope and an interval," with the scope satisfied per `scopeRule`.
*Fixture:* `no-opening-candidacy-valid` — internal mobility with `campaignRef` only — *expect:* accepted, and invariant 1 does not reject it.

**D2 — `scopeRule` is prose only**; all four scope fields sit in `optional`.
*Fix:* add `requiredOneOf: [requisitionRef, openingRef, processRef, campaignRef]` to the object.
*Fixture:* `scopeless-candidacy` — all four absent — *expect:* rejected by a structural rule, not commentary.

**D3 — Stage occurrences are unrepresentable.** The boundary owns "stage-occurrence history pinned to process release"; no field exists.
*Fix:* add `stageOccurrences[]` with `stageDefinitionRef`, required `processDesignReleaseRef`, `occurredAt`, `outcome`, `actorRef`.
*Fixture:* `stage-without-release-pin` — a stage occurrence with no release pin — *expect:* rejected (makes `three-candidates` and the pinning invariant testable).

**D4 — No `offerRef` despite the `offered` state** and a declared WM-ECO-021 reference.
*Fix:* add `optional.offerRefs` (immutable WM-ECO-021 versions, append-only); require ≥1 for `offered`.
*Fixture:* `offered-without-offer` — status `offered`, no offer reference — *expect:* rejected.

**D5 — Uniqueness has no interim guard for no-opening paths.** Invariant 16 defers to a hold, so duplicate active internal candidacies are currently permitted by omission.
*Fix:* adopt an interim rule — at most one active candidacy per `(person, declared effort scope)` — and keep the hold for the canonical form.
*Fixture:* `duplicate-active-no-opening` — two active candidacies for one person on one internal campaign — *expect:* rejected under the interim rule.

### E. Privacy

**E1 — `personRef` is required at `sourced`, forcing a Person anchor from unverified sourcing data.** This is also the one item the provider comparison credits to Claude ("provisional Person linking") that did not survive reconciliation. Combined with "never merge on name, email or birth date," the model has no legitimate way to hold a sourced lead.
*Fix:* permit a provisional pseudonymous subject reference with `linkConfidence` and `linkEvidenceRef`; promotion to a WM-PER-001 anchor requires recorded authorized evidence; provisional links never merge.
*Fixture:* `sourced-lead-no-person-mint` — a sourced lead with only a public profile URL — *expect:* provisional subject created; no WM-PER-001 anchor minted and no merge.

**E2 — Notice optional, rights route absent.** Invariant requires "purpose, controller, lawful basis, notice and rights route are explicit"; `noticeVersion` is optional and no rights-route field exists.
*Fix:* make `noticeVersion` required whenever the subject has been contacted or has submitted; add required `rightsRouteRef`.
*Fixture:* `submitted-without-notice` — a submitted candidacy with no notice version — *expect:* rejected.

**E3 — No data classes on documents or declarations**, so `purge-keeps-lineage` ("CV material is minimized or purged") cannot be evaluated.
*Fix:* require a `dataClass` tag per document and declaration (identity, contact, CV-biography, special-category, monitoring, evidence-of-decision) and bind disposition rules to classes.
*Fixture:* `classless-document` — a document bound with no `dataClass` — *expect:* rejected; disposition must not fall back to "retain all."

**E4 — No separation of special-category and monitoring data from selection-visible data.** The fairness constraint assumes it; nothing enforces it.
*Fix:* forbid `dataClass` ∈ {special-category, monitoring} from appearing in assessment or decision inputs; store under a separate controller purpose with its own basis.
*Fixture:* `monitoring-data-in-assessment` — a diversity-monitoring declaration cited as assessment input — *expect:* rejected.

**E5 — No retention clock or disposition state.** "Close, withdrawal or fill starts retention" has no `retentionStartAt`, `dispositionDueAt` or `dispositionState`; artifacts in external stores have no disposition path.
*Fix:* add those three fields, set `retentionStartAt` on the triggering transition, require `legalHoldRef` to suspend without altering `outcome`, and require artifact-store disposition receipts.
*Fixture:* `hold-suspends-not-alters` — legal hold lands on a closed candidacy past due — *expect:* disposition suspended, `outcome` and `dispositionDueAt` unchanged, hold attributable.

**E6 — No recipient, processor or transfer record.** Agencies, background-check vendors and cross-border transfers are unrecordable while the dossier holds "cross-company reuse" open.
*Fix:* add `disclosures[]` with `recipientRef`, `purpose`, `lawfulBasis`, `transferMechanism`, `disclosedAt`.
*Fixture:* `undisclosed-vendor-share` — a CV is sent to a screening vendor with no disclosure entry — *expect:* rejected.

**E7 — No sourcing provenance.** The lifecycle begins at `sourced` with no `sourcedFromRef`, `sourceChannel` or notice deadline.
*Fix:* require `sourceChannel` and `sourcedFromRef` when the candidacy originates at `sourced`, plus a `noticeDueAt` derived from the jurisdiction profile.
*Fixture:* `sourced-without-provenance` — a sourced candidacy with no origin — *expect:* rejected.

**E8 — Talent pool is unrepresentable.** "Standing requisition does not authorize an indefinite talent pool" cannot be enforced because pool membership has no field; pooling will hide inside `closed`.
*Fix:* model pool membership as a separate purpose-scoped consent record with its own `lawfulBasis`, `expiresAt` and renewal act; never inferred from a closed candidacy.
*Fixture:* `closed-candidacy-as-pool` — a closed candidacy is re-surfaced for a new opening without a pool consent — *expect:* rejected; a new scoped submission or consent is required.

### F. Fairness

**F1 — Adverse outcomes need no attributable human decision-maker, and automated decisions are unflagged.** "Score, recommendation and decision remain distinct" does not prevent an automated rejection recorded as a bare status change.
*Fix:* require `outcomeDecisionRef` with `actorRef` and `reason` for `rejected` and employer-side withdrawal; add `automatedDecision` flag with `humanReviewRef` required when true.
*Fixture:* `automated-rejection-unreviewed` — a scoring rule sets status `rejected` with no actor or review — *expect:* rejected (extends `score-is-decision` from inference to recording).

**F2 — Disposition can destroy fairness-audit evidence.** The preserved set in `purge-keeps-lineage` and the closure invariant is "Person, Decision, Employment"; assessment results are not in it, yet the profile requires fairness audit over "attributable decisions **and assessment results**."
*Fix:* add assessment results and stage outcomes to the minimum preserved set, retained in a decision-evidence data class separate from biography.
*Fixture:* `purge-keeps-assessment` — CV disposition on a rejected candidacy — *expect:* assessment results and stage outcomes survive; biography material does not.

**F3 — Fairness-audit access is unbounded.** Nothing limits audit use of retained decision evidence, so audit becomes a re-identification channel.
*Fix:* declare fairness audit a distinct purpose with pseudonymised access by default and recorded justification for re-identification.
*Fixture:* `fairness-audit-reidentifies` — an audit query returns identified candidate biographies — *expect:* rejected absent a recorded re-identification justification.

### G. Validation and publication claims

**G1 — The profile block omits `canonicalPublishable` and `holds`**, unlike both candidates, so it reads as publishable.
*Fix:* add `"canonicalPublishable": false` and inherit the union of both candidates' holds plus the base-draft hold.
*Fixture:* `profile-publication-guard` — the profile is exported as canonical — *expect:* rejected while `canonicalPublishable` is false or any hold is open.

**G2 — The profile claims to narrow a base that has no spec.** `sourceFacts.WM-ORG-008` says spec and source are missing; `constraints[0]` is stated in the present tense ("is narrowed to … and no longer owns …").
*Fix:* restate as a conditional requirement on WM-ORG-008 authoring, not an accomplished narrowing.
*Fixture:* `narrow-missing-base` — the narrowing constraint is cited as satisfied — *expect:* rejected until a WM-ORG-008 spec exists.

**G3 — References assert relation contracts that do not exist.** `sourceFacts.relations`: no approved relation row covers WM-ORG-008 or WM-ACT-039, yet both candidates list them as boundary references with purposes.
*Fix:* mark every reference `contractState: "provisional"` until an approved relation row exists.
*Fixture:* `unapproved-relation-used` — a reference without an approved relation row is treated as binding — *expect:* rejected; provisional only.

**G4 — Invariants are unnumbered and fixtures cite none.** No fixture can be traced to the rule it exercises, and the audit trail cannot cite a rule.
*Fix:* assign stable ids (`REQ-INV-01…18`, `CAND-INV-01…22`); add `rules: [...]` to every fixture; require every invariant to be covered by ≥1 fixture.
*Fixture:* `invariant-coverage-lint` — coverage check over both sets — *expect:* no invariant lacks a fixture and no fixture lacks a rule id.

**G5 — Fixtures are worded as executable outcomes** ("The transition is rejected") while `sourceFacts.runtime` states they are not executable tests — an overclaim of validation.
*Fix:* label the fixtures block `"executable": false` and reword expectations as normative semantic expectations, not observed results.
*Fixture:* `fixture-claim-guard` — fixture outcomes are reported as test results — *expect:* rejected; conformance requires an executable harness that does not exist.

**G6 — `two-seat-request` presumes the resolution of an open hold.** The hold says "Opening quantity versus seat-level identity requires canonical governance," but the fixture asserts two seats produce two openings.
*Fix:* split into a distinguishable-seats case (two openings) and an interchangeable-seats case (one opening, quantity 2), and mark both provisional under the hold.
*Fixture:* `interchangeable-seats-quantity` — two interchangeable seats under one opening, quantity 2 — *expect:* accepted provisionally, cap arithmetic unchanged at 2.

## 5. Contradictions

1. **Candidacy scope** — `invariants[0]` binds "one opening, one recruitment process"; `scopeRule`, `invariants[12]`, and `profile.constraints[9]` make both optional. Invariant 1 would reject `internal-mobility-scope` and `internal-mobility-no-opening`, which the same dossier marks positive. *(D1)*
2. **Approved need** — "Approved need is an attributable decision record and never the requisition identity" vs. `approved`/`funded` states reachable with `approvalDecisionRefs` absent, which makes status the approval. *(C3, and `approval-decision-not-root` is thereby only half-guarded)*
3. **Seat authority** — four cap invariants and `seat-cap-overrun` against an object that has no cap field; `requestedHeadcount` is the only quantity present and it is a request. *(B1)*
4. **Funding** — "Budget reference never substitutes for funding authority or commitment" vs. a `funded` state whose only available backing is the optional `budgetRef`. *(C4)*
5. **Downstream creation** — Requisition `references[WM-ORG-005].purpose` = "Employment created downstream" reads as a creation relation, while `excludes` bars employment and `invariants` bar approval from creating it. Purpose text must be "employment resulting from this authorization, referenced not owned." *(B4)*
6. **Base narrowing** — the profile narrows WM-ORG-008 in the present tense; `sourceFacts` says its spec and source are missing, and no relation row covers it. *(G2, G3)*
7. **Validation status** — fixtures assert acceptances and rejections; `sourceFacts.runtime` says they are not executable tests. *(G5)*
8. **Boundary vs. object** — Candidacy `owns` stage-occurrence history, controller/purpose/basis/notice, retention/hold/disposition triggers, withdrawal and outcome; `objects.Candidacy` provides fields for none of stage occurrences, rights route, disposition state, or outcome. The same mismatch holds for Requisition's "authorized-seat cap and attributable cap-change history." *(D3, E2, E5, C6, B1, B2)*
9. **Disposition vs. fairness** — the preserved set on disposition is Person, Decision, Employment; fairness audit is defined over decisions *and assessment results*, which are not preserved. *(F2)*
10. **Sourcing vs. person minting** — `sourced` is the first lifecycle state and `personRef` is required, so every sourced lead mints or resolves a Person anchor, while merge on name/email/birth date is forbidden and biography retention is restricted. *(E1)*
11. **Unsourced identifier** — `WM-ORG-016` in Requisition holds has no entry in `bases`, `references` or `sourceFacts`. *(A5)*
12. **Bases vs. references** — WM-REC-010 is a load-bearing reference for approval but is not among `profile.bases`, so `sourceFacts.bases` ("all relevant bases remain reviewable drafts") does not cover it; its status is unknown. *(A2)*
13. **Open hold vs. asserted fixture** — the seat-level identity hold is open while `two-seat-request` asserts one of its two possible resolutions. *(G6)*

## 6. Remediation checklist (closed)

1. Add `WM-REC-010` to `profile.bases` and its status to `sourceFacts`; home the selection decision and recommendation there or in WM-ACT-039. *(A2, A3)*
2. Home Posting as a dependent artifact of WM-ACT-039 with channel, content release, jurisdiction and publish/withdraw times. *(A1)*
3. Declare Assignment and Contract out-of-contour with a named owning contour or explicit holds. *(A4)*
4. Resolve or remove `WM-ORG-016`. *(A5)*
5. Specify the derived-vacancy projection's inputs, instant semantics and non-persistence. *(A6)*
6. Add `authorizedSeatCap` (required from `approved`), `capChangeHistory[]` with decision and actor, and the `remainingHeadcount` derivation. *(B1, B2, B3)*
7. Type `fillRefs` to WM-ORG-005, define "outstanding accepted offer," and state the non-double-counting seat formula. *(B4)*
8. Make `requisitionRef` required on Candidacy when a requisition exists, declare child→parent the authoritative direction, and make parent-side collections derived. *(B5, C7)*
9. Add `versionId`, `predecessorRef`, required `recordedBy`, and `correctionReason` on backdated successors to both objects. *(C1, C2)*
10. Conditionally require approval decision references for `approved` and later states; add `fundingAuthorityRef` and `fundingCommitmentRef` and require the former for `funded`. *(C3, C4)*
11. Publish the requisition transition matrix; make `cancelled` and `closed` terminal; route reuse through a successor requisition. *(C5)*
12. Declare the candidacy lifecycle unordered and add required-on-close `outcome`, `outcomeReason` and `outcomeDecisionRef`. *(C6)*
13. Require disposition tombstones so every historical reference resolves without restoring content. *(C8)*
14. Restate candidacy invariant 1 in terms of recruiting-effort scope and encode `requiredOneOf` for the four scope fields. *(D1, D2)*
15. Add `stageOccurrences[]` with a required `processDesignReleaseRef`, and `offerRefs` required for the `offered` state. *(D3, D4)*
16. Adopt the interim uniqueness rule for no-opening paths while keeping the governance hold. *(D5)*
17. Introduce the provisional pseudonymous subject reference with link confidence and evidence, and forbid merge without authorized evidence. *(E1)*
18. Require `noticeVersion` on contact or submission and add `rightsRouteRef`. *(E2)*
19. Require `dataClass` on every document and declaration and bind disposition to classes. *(E3)*
20. Bar special-category and monitoring classes from assessment and decision inputs and hold them under a separate purpose and basis. *(E4)*
21. Add `retentionStartAt`, `dispositionDueAt`, `dispositionState`, artifact-store disposition receipts, and hold-suspension semantics that leave `outcome` untouched. *(E5)*
22. Add `disclosures[]` covering recipients, processors and transfer mechanisms. *(E6)*
23. Require sourcing provenance and a notice deadline for candidacies originating at `sourced`. *(E7)*
24. Model talent-pool membership as a separate expiring consent, never inferred from a closed candidacy. *(E8)*
25. Require an attributable decision with actor and reason for every adverse outcome, plus an automated-decision flag with human review. *(F1)*
26. Extend the minimum preserved set on disposition to assessment results and stage outcomes as decision evidence. *(F2)*
27. Define fairness audit as a distinct purpose with pseudonymised access by default and recorded re-identification justification. *(F3)*
28. Add `canonicalPublishable: false` and inherited holds to the profile block. *(G1)*
29. Restate the WM-ORG-008 narrowing as conditional on that base being authored, and mark all references to WM-ORG-008 and WM-ACT-039 `contractState: "provisional"` pending approved relation rows. *(G2, G3)*
30. Assign stable invariant ids, bind every fixture to rule ids, and require full invariant coverage. *(G4)*
31. Mark the fixtures block non-executable and reword expectations as normative semantic expectations. *(G5)*
32. Split `two-seat-request` into distinguishable-seat and interchangeable-seat cases, both marked provisional under the seat-identity hold. *(G6)*
33. Increment to `candidateRevision` 3, keep `allocationState` `unassigned` with null `modelId`/`registryId`, replace the "one frozen semantic audit is pending" hold with "frozen audit returned REVISE at revision 2; 32 remediation items open," and re-submit for a second frozen audit before any allocation or publication.

End of checklist.
