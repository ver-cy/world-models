# Frozen semantic audit — EM-LEG-03, candidate revision 2

## Verdict

**REVISE.**

The **PROFILE** decision itself is **affirmed**: nothing in the contour requires an identity or lifecycle that the WM-KNW-012 statement aggregate (work → dated expression → rule slot → manifestation, plus registered derogation, precedence and lifecycle) does not already root. The duplicate direction on WM-ORG-019 is also affirmed, as a proposal only. Revision is required because the reconciled artifacts contain (a) one cross-artifact contradiction about what an acknowledgement can pin, (b) an operation presupposed by the resolution constraints that no declared function surface owns, (c) a decision field that pre-empts its own gating test, (d) fixtures that are not fixtures, and (e) a hold set that drops four blockers that both boundary studies raised.

**Audit scope and limits.** Judged only against the material in this prompt. The frozen dossier attests exactly two models (WM-ORG-019, WM-KNW-012) plus the composition targets named inside them. Every other identifier used by the candidates is unverifiable here. This is one frozen pass by one auditor sharing a provider family with one of the two boundary studies; it does not constitute independent multi-provider review and must not be recorded as closing either parent's single-provider hold.

## Findings

### A. Identity and lifecycle integrity

**F1 (blocking) — "Consolidated text is a derived projection" contradicts the parent and breaks acknowledgement pinning.** `ownedSemantics.policyVersion` demotes consolidated text to a derived projection. WM-KNW-012 declares the consolidated point-in-time expression as a `serial: true` artifact with its own identity strategy — a dated, citable rendering. Meanwhile the allocation candidate requires every communication event to pin an exact `policyExpressionRef` plus `expressionDigest`. An unidentified projection cannot be pinned; an identified expression can. The two artifacts cannot both be right.

**F2 (blocking) — expression identity and manifestation integrity are conflated.** `expressionDigest` is a manifestation property (bytes, rendering, language). WM-KNW-012 keeps work / expression / manifestation distinct, and its multilingual-authenticity gap is explicitly deferred. As written, an acknowledgement of a translated rendering and of the authentic-language expression are indistinguishable at the record level, while `locale` sits as an *optional* field on the acknowledgement.

**F3 (material) — scope adoption is an unsourced construction carried as settled.** Claude's study names this the profile's one real construction obligation: WM-KNW-012's `inherit-from` and policy-set containment are statement-to-statement, never statement-to-organisational-scope. The reconciled candidate asserts `policyAdoption` semantics and an adoption constraint with no corresponding hold recording that the construct has no source-grounded structure in the parent.

**F4 (material) — the contour's first question is blocked by an unrecorded parent gap.** "Who may adopt and revoke a rule?" cannot be answered while WM-KNW-012 carries multi-step delegation of rule-making authority as declared deferred research. `holds` mentions only "delegated-**recipient** semantics" — a communication concern, not delegated adoption authority. Two different gaps, one of them missing.

**F5 (material) — the contour's own proposed invariant is half-covered.** The dossier requires "a rule has an adopting body **and a term**." Constraint 1 covers authority, mandate, decision and in-force instant; nothing covers efficacy end, review term, or the parent's explicit adjudication that *review due is not expiry*. The v1 candidate field `review_due` is dropped without record.

**F6 (material) — event lifecycle enumerations disagree, and one state is a category error.** `identityTest.independentLifecycle` lists eight states; `objects.PolicyCommunicationEvent.lifecycle` lists five. `acknowledged` appears only in the former — and placing it on the event state directly re-creates the conflation the invariants forbid (delivery, opening, reading and acknowledgement are distinct; acknowledgement is owned by `AcknowledgementAct`). `retained` and `disposed` are retention-class states, not communication states.

**F7 (material) — no state expresses "unknown," yet an invariant depends on it.** `status` is required with no stated domain; `DeliveryAttempt.outcome` likewise. Invariant 12 forbids promoting unknown status to success, but no enumerated value can hold "unknown," which is precisely how fail-open creeps in.

**F8 (material) — supersession does not say what happens to attached acknowledgements.** "A corrected communication record supersedes rather than mutates the prior event" plus `supersedesEventRef` leaves an existing `AcknowledgementAct` pointing at a superseded event with no rule about whether its pinned expression follows the correction.

### B. Policy resolution correctness

**F9 (blocking) — the resolution constraints presuppose an operation no declared function owns.** Composing "global floor + local tightening + matching bounded derogation, minus non-derogable violations" into one effective rule set is not WM-KNW-012's `resolve-point-in-time-expression`, which returns an expression reference plus a gap/ambiguity report. The parent's adjudication records its function surface as incomplete with additions barred under the single-provider mode. So fixtures `bounded-team-exception`, `expired-exception` and `unknown-applicability` cannot be satisfied by any operation declared anywhere in the frozen evidence.

**F10 (blocking) — "never a decision" is missing from the constraint set.** Both studies state that resolution returns one rule set or an explicit unresolved report and never a permit, deny or compliance conclusion. The reconciled constraints say only that unknowns yield unresolved. Given that the contour's negative case is exactly an illegitimate compliance inference, the strongest available guard has been dropped in reconciliation.

**F11 (material) — the revalidation window is undefined.** "Floating adoption resolves to the new in-force expression while local tailoring is revalidated rather than rewritten" specifies no state between the successor's in-force instant and completed revalidation. Either the un-revalidated tightening silently applies, or it silently disappears. Both are fail-open in one direction.

**F12 (material) — fail-closed handling for unresolved references was dropped.** WM-KNW-012 makes `unresolved reference handling code` a required element; Claude's required profile pins it to fail-closed for prohibition slots. Nothing in the reconciled constraints carries it.

**F13 (material) — no distinctness requirement between granting authority and beneficiary.** WM-KNW-012 asks for that distinctness assertion; Claude states it as invariant 2. Constraint 9 requires only "authority." Self-granted derogations are therefore well-formed under the profile as written.

**F14 (minor) — compensating obligation is silently promoted without stating the escape.** The parent element is `0..n`. The profile requires a reference. Claude's formulation permits an explicit "none" plus reason. The candidate states neither the promotion nor the escape.

### C. Duplicate retirement safety

**F15 (material) — the residue inventory is incomplete.** Grok names three non-duplicate residues in WM-ORG-019; the retirement preconditions address two (control/implementation mapping, communication/acknowledgement). The third — organisational purpose and risk-motivation framing (`policy-scope.rationale`: objective, riskRef) — has no disposition and no home. Retirement as specified drops it.

**F16 (material) — the machine-interpretation layer is unmapped.** `policy-mapping.validation` (fixtures) and `policy-mapping.executionBoundary` (permission, adapter, preconditions, rollback) have no counterpart data element in WM-KNW-012's standard-alignment surface. The "ten of twelve layers duplicate" claim is not field-level evidenced — consistent with the unratified crosswalk, but the two unmapped members must be named, not absorbed.

**F17 (material) — proposed state is asserted as state.** `duplicateRetirementProposal.state: "deprecated-pending-rehome"` reads as effective while its own preconditions are unmet, and no hold records that even the deprecation marking on a published reviewable draft requires registry authority.

**F18 (minor) — the parent's unsettled entry kind is not held.** WM-KNW-012 carries `boundary-review-required` and a contested entity→aggregate reclassification, and Claude's study makes the retirement *depend* on that boundary review. `holds` says only that both parents are non-canonical drafts.

### D. Acknowledgement / control separation

**F19 (material) — the flagship fixture asserts behaviour no in-scope model owns.** `acknowledgement-not-control` expects "the control write is rejected." Neither candidate owns a control register or a rejection point; the profile holds that the control-register owner is unresolved. What this contour can assert is the *absence of any path*, plus an external obligation on the control authority.

**F20 (material) — nothing binds the acknowledging actor to the intended recipient.** `AcknowledgementAct.actorRef` and `PolicyCommunicationEvent.recipientRef` are unrelated fields. With delegated-recipient semantics unvalidated, an assistant's acknowledgement is silently the recipient's.

**F21 (minor) — the policy-side storage prohibition has no negative fixture.** Constraint 12 forbids WM-KNW-012 storing per-recipient receipt or control state; every fixture tests the control *write*, none tests the storage leak.

### E. Fixtures

**F22 (blocking) — these are prose expectations, not fixtures.** No pinned instants (WM-KNW-012 requires RFC 3339 with seconds and explicit offset), no identifiers, no input records, no expected result shape, no distinction between "rejected at write" and "resolved as unresolved." `bounded-team-exception` says "effective at t" with no *t*; `weaken-nonderogable-floor` and `old-expression-exception` each accept two different outcomes ("rejected **or** unresolved") and so cannot fail. `wm-act-027-reuse` is `kind: "review"` — a decision gate, not an executable case.

**F23 (material) — uncovered constraints.** No case for: an adoption declaring neither floating nor pinned; missing mandate or adoption decision; a mutable URL or "latest" alias offered as proof of what was communicated; unit-level recipient not implying member receipt; unknown delivery status not promoted; recorded unresolved conflict with escalation route; retention and disposal.

### F. Registry discipline

**F24 (blocking) — `decision: "NEW MODEL"` pre-empts the test that gates it.** The same object states `allocationState: "unassigned-pending-reuse-test"` and "Allocate only if that test fails." Grok's position is explicitly *no new catalogue ID in this review*. The dossier rule is "no new ID without independent identity/lifecycle **and registry allocation**." A recorded NEW MODEL decision is a pre-authorisation the contour does not hold.

**F25 (material) — mastership names no owner.** `"policy communication and acknowledgement record authority"` is a role description, not a resolvable authority — so it cannot satisfy the retirement precondition that this residue "has an explicit owner."

**F26 (material) — six consumed identifiers are unattested in the frozen dossier.** WM-ACT-027, WM-XCT-027, WM-PER-001, WM-ORG-001, WM-ORG-002, WM-ACT-040, and the contour reference "EM-RSK-01" appear nowhere in the frozen evidence. The allocation candidate's `boundary.references` present three of them as settled reference targets with purposes.

**F27 (material) — WM-ACT-027 and WM-XCT-027 are one character apart and carry opposite roles** (candidate reuse host vs. mixin that must never be read as the control register). Nothing in the artifacts guards against transcription collapse.

**F28 (minor) — an unrecorded provider divergence.** Claude scopes the acknowledgement allocation *outside* EM-LEG-03 as a separate request; the allocation candidate carries `contourId: EM-LEG-03`. The dossier's `candidate_types` support keeping it in contour, so the outcome is defensible — but the provider comparison omits the divergence entirely, and the rename/rescope from the contour's `Acknowledgement` to `Policy Communication Event` is unrecorded.

**F29 (minor) — dropped holds.** Absent from the reconciled set: alignments (ISO 37301, COSO, XACML, OPA, ODRL, Akoma Ntoso, ELI, PROV-O, SBVR) are alignments and not conformance claims; ISO 37301 paywalled/unverified on the parent; source-resolution and version-pinning hold; timestamp-rule verification hold; the not-legal-advice framing both studies carry.

## Required deterministic remediation

Each item is a single mechanical edit; none requires new research, and none may mint an identifier.

1. **F1** — Restate `ownedSemantics.policyVersion`: "A policy version is an immutable dated expression of one policy work. A consolidated expression is a governed, citably identified rendering produced from applied modifications; it is neither a new work nor a mutation of any prior expression."
2. **F2** — Split the pin: require `policyExpressionRef` (expression identity), `manifestationRef` (the rendering communicated) and `manifestationDigest`; rename `expressionDigest` accordingly. Promote `locale` to required on `AcknowledgementAct` and add the invariant "an acknowledgement of a translated manifestation does not assert acknowledgement of the authentic-language expression."
3. **F3** — Add hold: "The statement-to-organisational-scope adoption construct has no source-grounded structure in WM-KNW-012; it is a profile construction obligation, not a ratified parent capability."
4. **F4** — Add hold: "Multi-step delegation of rule-making authority is declared deferred research on WM-KNW-012 and blocks the contour question 'who may adopt and revoke'." Keep the delegated-**recipient** hold separate and distinctly worded.
5. **F5** — Add constraints: "Review due is a profile field that never terminates in-force status or efficacy"; and "Every adoption records either a bounded efficacy interval or an explicit open-ended declaration with its basis." Re-attach the v1 `review_due` field as `candidate-not-normative`.
6. **F6** — Make `identityTest.independentLifecycle` identical to `objects.PolicyCommunicationEvent.lifecycle`. Remove `acknowledged` (owned by `AcknowledgementAct`). Move `retained` / `disposed` to a `retentionState` enumeration distinct from communication state.
7. **F7** — Enumerate `status` as exactly the event lifecycle plus `unknown`, and `DeliveryAttempt.outcome` as `{delivered, failed, unknown}` — where `unknown` is terminal until externally evidenced and never promoted.
8. **F8** — Add invariant: "An acknowledgement resolves the expression and manifestation of the exact event record it references; superseding an event never re-points an existing acknowledgement, and a superseding acknowledgement must reference the same `communicationEventRef`."
9. **F9** — Declare the effective-rule-set composition explicitly as a profile-level read operation with inputs (work reference, instant, subject scope) and exactly two output shapes (one rule set, or an unresolved report with cause and escalation route), and add hold: "This operation is not present in WM-KNW-012's declared function surface; its addition is a required parent revision."
10. **F10** — Add constraint: "Resolution returns a rule set or an explicit unresolved report, never a permit, deny, compliance or control-effectiveness conclusion."
11. **F11** — Add constraint: "Between a successor expression entering force and completed revalidation, affected local tailoring resolves as `pending-revalidation`, which yields unresolved for the affected slots and is never treated as either applied or withdrawn."
12. **F12** — Add constraint: "Unresolved-reference handling is declared per rule slot and is fail-closed for prohibition slots."
13. **F13** — Amend constraint 9: the exception's granting authority must be recorded and asserted distinct from the beneficiary.
14. **F14** — State the promotion explicitly: the parent's `0..n` compensating obligation is raised to required-one, satisfied either by a reference or by an explicit `none` with a recorded reason.
15. **F15** — Add a fourth retirement precondition: organisational purpose and risk-motivation framing is either carried as profile metadata on the base or given an explicit external owner.
16. **F16** — Add hold naming `policy-mapping.validation` and `policy-mapping.executionBoundary` as members with no identified counterpart in the base's alignment surface, pending the field-level crosswalk.
17. **F17** — Split into `currentState: "published-reviewable-draft"` and `proposedState: "deprecated-pending-rehome"`, and add hold: "No registry mutation, including the deprecation marking, is authorised by this contour."
18. **F18** — Add hold: "WM-KNW-012 carries `boundary-review-required` and a contested entity-to-aggregate reclassification; the WM-ORG-019 retirement depends on that review."
19. **F19** — Restate the fixture expectation as: "No mapping exists by which the acknowledgement can reach control execution or effectiveness; the fixture asserts the absence of that path," plus a recorded external obligation on the unresolved control authority to reject such a write.
20. **F20** — Add invariant: "An acknowledgement by a party other than the intended recipient is either rejected or recorded as delegated with an explicit delegation reference; it is never silently attributed to the recipient."
21. **F22** — Rebuild every case with: pinned RFC 3339 instants carrying explicit offsets, named placeholder record keys local to the fixture set, an input record, and exactly one expected outcome. Replace each "rejected **or** unresolved" with the single outcome the constraint requires. Remove `wm-act-027-reuse` from the fixture set and record it as the decision gate it already is.
22. **F23** — Add cases for the seven uncovered constraints listed above.
23. **F24** — Change `decision` to `REUSE-TEST-PENDING` and add: "No new-model decision is recorded until the reuse test resolves and registry authority approves."
24. **F25** — Replace `mastership` with a named resolvable authority or the explicit value `unresolved`, and mark the corresponding retirement precondition unmet.
25. **F26** — Re-type every identifier not attested in the frozen dossier as `unverified-reference`, with `purpose` retained and `status: "pending registry resolution"`. Add hold: "Seven identifiers consumed by these artifacts are unattested in the frozen dossier."
26. **F27** — Add an explicit note that the reuse-host candidate and the mixin-that-is-not-the-control-register are two distinct identifiers differing only in their middle segment, and that collapsing them is a correctness failure.
27. **F28** — Record in the provider comparison that one study scoped the communication allocation outside this contour while the dossier's `candidate_types` retains it inside, and record the rename from the contour's `Acknowledgement` to `Policy Communication Event` as a rescope.
28. **F29** — Restore the five dropped holds verbatim in substance: alignment-not-conformance; paywalled parent source; source resolution and version pinning; timestamp-rule verification; standards alignment is not legal advice.

## Identifier discipline

Held: no profile identifier is minted; `newRuntimeId: false` is consistent with `bases`; `modelId` and `registryId` are null; the retired duplicate's identifier is preserved as an alias rather than reassigned; no candidate invents a control-register or acknowledgement identifier.

Not held: `decision: "NEW MODEL"` is a pre-authorisation of allocation (F24); seven identifiers are asserted as reference targets without attestation in the frozen evidence (F26); a proposed registry state is presented as effective (F17); two near-identical identifiers with opposite roles carry no anti-collision note (F27).

No identifier is coined anywhere in this audit, and the six unattested references are neither validated nor rejected here — only downgraded to unverified.

## Publication decision

**Publication: denied. No package conversion, no live verification, no canonical publication, no registry mutation — including the WM-ORG-019 deprecation marking.**

What this audit does authorise: the **PROFILE** decision over WM-KNW-012 with no profile and no runtime identifier, and the conditional-retirement *direction* for WM-ORG-019 as a proposal, both as reviewable-draft content.

Path forward: apply all 28 remediation items, emit candidate revision 3, and keep the publication holds visible with the four restored blockers (parent boundary review, delegation of adoption authority, unsourced scope-adoption construct, unattested references) added to the existing seven. Revision 3 still requires the field-level crosswalk ratification, the named control-register owner, the reuse-test outcome, canonical fixtures, and genuinely independent second-provider review — which this single frozen pass does not supply.
