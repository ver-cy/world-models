# Frozen audit — EM-KNW-03 / WM-REC-012 `0.1.0-candidate.2`

**Verdict: REVISE.**

The disposition is right and I would not relitigate it: complete the reserved `WM-REC-012` as the durable-record owner, mint no new model id, keep Meeting/participation in WM-ACT-025 and channel/thread/turn in WM-ACT-027, keep minutes and transcript as separate works. The architecture survives challenge. The artifact does not: it carries one cross-model overreach that contradicts its own invariant set, one relation constraint that is unsatisfiable for a case its own fixtures assert, a boundary that simultaneously owns and delegates the same concerns, an identity level claimed in `purpose` and `boundary` but never defined, an unresolvable fixture rule-ID scheme, and a known blocker from the Grok study dropped without a hold. These are field-level defects, not redesign; `candidate.3` should clear them.

Nothing below asserts publication readiness, and I introduce no identifiers.

---

## Blocking findings

**B1 — INV-019 contradicts INV-011 and exceeds candidate authority.**
`invariants[19]` states official Decision status requires *both* an authorized decision occurrence *and* a fixed approved **WM-REC-012** expression. `invariants[11]` states tasks and decisions keep lifecycles independent from record approval. `boundary.delegates` assigns "fixed decision record and effect onset" to WM-REC-010, and fixture `later-authorized-decision` resolves effect onset through WM-ACT-024 + WM-REC-010 with no minutes expression in the loop. As written, a decision validly fixed in WM-REC-010 is denied official status until a minutes expression is approved — WM-REC-012 becomes a precondition of decision effect, which is exactly the dual-mastership the Grok study flagged and the Claude study forbade. `holds[2]` also says relation rows confer no promotion authority, yet INV-019 imposes a gate on two external masters.

This is inherited unreconciled: the Grok study asserts the two-gate rule; the Claude study asserts lifecycle independence. `candidate.2` imported both.

*Remediation (choose one, state it in `promotionRules`):* replace the second gate with "fixation by the decision-record authority (WM-REC-010)"; then add a scoped successor invariant — "where a minutes obligation exists, the approved WM-REC-012 expression evidences the decision and does not condition its effect." If instead the registry intends minutes-gating, delete `invariants[11]` and record the reversal against the Claude study in `holds`. Do not ship both.

**B2 — `relations[WM-ACT-025].required: true` is unsatisfiable for transcript-only records.**
`purpose` admits records produced "from a meeting **or** communication occurrence"; `recordWorks.transcript.cardinalityPerOccurrence` is `0..n`; fixture `transcript-without-minutes` accepts a transcript for a captured session with no minutes obligation. But WM-ACT-027 is `required: false` and WM-ACT-025 is `required: true`, so every transcript work must resolve a Meeting — which licenses precisely Grok's "dummy Meeting laundering chat into WM-REC-012" failure mode, and the candidate has no invariant or fixture against it.

*Remediation:* type `workRequired.occurrenceRef` with a sibling `occurrenceKind ∈ {meeting, interaction}`; change WM-ACT-025 to `"required": "conditional"` with `condition: "occurrenceKind = meeting"`, WM-ACT-027 likewise for `interaction`; add invariant "exactly one occurrence authority resolves per work; a Meeting is never minted or asserted by WM-REC-012 to host a record" plus a negative fixture.

**B3 — `boundary.owns` and `boundary.delegates` claim the same concerns.**
`owns` includes "retention schedule hold tombstone and disposition evidence" and "format manifestation references and fixity bindings"; `delegates` sends "generic record custody fixity and retention authority" to WM-REC-001. Both cannot hold. `workRequired.retentionBindingRef` shows the intended reading (bind, don't master), but `owns` overrides it textually.

*Remediation:* rewrite the two `owns` entries as "binding of this record's works to a WM-REC-001 retention schedule, and hold/tombstone/disposition **evidence references**" and "manifestation identity and the binding to WM-REC-001 fixity". Authority stays external.

**B4 — Manifestation identity is claimed and never defined.**
`purpose` and `boundary.owns` assert work/expression/**manifestation** identities; the candidate defines `workIdentity`, `workRequired`, `expressions` — and no manifestation structure. Format, media type and fixity binding have nowhere to live, so `restricted-quote`, fixity and disposition cannot be evaluated at the byte level the fixtures presume ("approved bytes … remain resolvable" in `approved-correction`).

*Remediation:* add a `manifestations` object — `identity: ["expressionRef","manifestationId"]`, `required: ["format","createdAt","fixityRef"]`, `rule: "fixity and custody resolve through WM-REC-001; manifestation never alters expression identity."`

**B5 — Approved-expression immutability contradicts the declared lifecycle.**
`expressions.immutability` says approved expressions are immutable, but `lifecycle` carries `corrected-by-erratum`, `superseded` and `withdrawn` as states of the expression, and `transitionRule` defines no transitions into the last two. Setting an approved expression's status to `superseded` or `withdrawn` is a mutation of an object declared immutable, and no operation issues those transitions (`operations` stops at erratum and redaction).

*Remediation:* scope immutability explicitly — "immutability binds expression content, identity and approved manifestations; status and lineage are append-only events recorded against, not inside, the approved expression." Extend `transitionRule` to `approved -> superseded` (on successor approval) and `approved -> withdrawn` (authorized act only, never expiry). Add `withdraw-expression` to `operations` with its authority, and a `dispose-record` / `apply-hold` operation — fixture `retention-hold` currently tests behaviour no operation provides.

**B6 — Fixture `expectRule` identifiers do not resolve; seven are stale.**
`invariants` is a bare string array with no ids, so `INV-nnn` can only resolve positionally. Positionally, `INV-015`…`INV-026` match by content (12/12). `INV-001`…`INV-007` all mismatch: they were authored against a seven-invariant predecessor set and now point at content sitting at positions 12, 6, 2, 9, 8/23, 7, 14 respectively. A conformance runner reading this file today mis-scores seven of twenty cases.

*Remediation:* give every invariant an explicit `id` (do not rely on array order), then repoint the seven stale cases: `chat-task-proposal`→"no official promotion inferred"; `later-authorized-decision`→"decision requires authority at the instant"; `minutes-versus-transcript`→"minutes and transcript are separate works"; `approved-correction`→"approved expressions immutable"; `restricted-quote`→strictest-scope; `capture-gap`→"message references preserve … capture-gap metadata"; `retention-hold`→"disposition preserves tombstone and hold evidence".

**B7 — A Grok blocker was dropped without a hold: redaction versus retention.**
The Grok study lists "redaction-versus-retention conflict" among its blockers. `candidate.2` contains no rule, invariant, fixture or hold for it. The two owned mechanisms actively collide: `accessRule.redaction` guarantees the source is never deleted and preserves lineage; `invariants[14]` permits disposition that leaves only a tombstone. Nothing says what a legal hold does to a redaction review date, or what disposition of a source expression does to overlays that cite it.

*Remediation:* add invariant — "a hold suspends both disposition and redaction review expiry; disposition of a source expression preserves overlay lineage and tombstone resolvability; redaction never substitutes for disposition and disposition never effects declassification" — plus one fixture (`hold-during-redaction-review`). If the conflict is to stay unresolved, it must at minimum appear in `holds`; silence is the defect.

---

## Non-blocking findings

**N1 — Speaker anchors may bind to bare Party.** Grok invariant 11 ("speaker and attendance anchors cite MeetingParticipation, not Party or channel member") is absent. `passageAnchor.optional` carries `speakerRef` and `speakerCapacity` as untyped free optionals; `invariants[22]` constrains only quorum and vote attribution. This defeats the late-joining / dual-capacity case that justified dependent participation identity in the first place. Also, re-asserting `speakerCapacity` beside `speakerRef` duplicates a WM-ACT-025-mastered attribute. *Fix:* rename to `participationRef` for meeting-sourced passages, derive capacity from it, and extend `invariants[22]` to speaker and attendance anchors.

**N2 — `invariants[8]` and `invariants[23]` restate the same rule at different arity** (two-place "source or target" vs four-place "source passage container quote-site"). `accessRule.comparator` uses the four-place form. *Fix:* delete `invariants[8]`; keep 23.

**N3 — "Overlay" is used but never modelled.** `accessRule.redaction` and `invariants[24]` permit an "overlay **or** derivative expression"; `expressions` knows only expressions, and `redactionVariant` appears in `identity` while `redactionVariantRef` appears in `optional`. Two mechanisms, one defined. *Fix:* define overlay as a typed artifact with its own identity, or collapse to derivative expression and delete the term.

**N4 — Expression identity is underdetermined and inconsistently named.** `identity` lists `workId` and `redactionVariant`; `required` lists `workRef` and omits `redactionVariant`. An identity component that is not required cannot discriminate. `expressionKind` is required and never enumerated. *Fix:* align `workId`/`workRef`, make `redactionVariant` required with an explicit `none` default, enumerate `expressionKind`.

**N5 — `approve-expression` has no data field.** The operation approves "through a referenced authorized later act"; `expressions.optional` offers `approvedAt` and nothing to hold the act. *Fix:* add `approvalActRef` and `approvalAuthorityBasisRef`, required when `status ∈ {approved, superseded, withdrawn}`.

**N6 — Certifying officer is mastered twice.** `recordWorks.minutes.required.certifyingOfficerRef` sits at work level while `certification.required` masters `certifierRef` at expression level; `coverageAssertion` likewise duplicates `requiredMatterCoverage`. *Fix:* drop both work-level duplicates; resolve through the certification of the approved expression. Also name `expressions.optional.certificationRef` as the derived inverse to stop divergence.

**N7 — `cardinalityPerOccurrence: "0..1 official minutes work"` is unenforceable.** No `officiality` discriminator exists on the work, no invariant states the constraint, no fixture tests a second official minutes work. *Fix:* define official as "has at least one approved expression", add the invariant, add a negative fixture.

**N8 — `invariants[22]` and fixture `quorum-from-channel-roster` legislate a delegated concern.** Quorum is WM-ACT-025-owned; WM-REC-012 cannot "reject" a quorum computation. *Fix:* recast as a record-scoped rule — "a quorum statement recorded in a WM-REC-012 expression resolves through MeetingParticipation and is never derived from a channel roster" — and restate the fixture expectation accordingly. Alternatively move it into `meetingParticipationExpectation` as a neighbor expectation, where the candidate's held status is honest.

**N9 — Party/actor authority has no relation row.** `producerRef`, `certifierRef`, `personsPresentRefs`, `speakerRef` and `partyRef` all point at an unnamed master. *Fix:* add a relation row for the registry's party/actor authority; the id must come from the registry, not from this audit.

**N10 — `kind: positive|negative` is undefined and applied inconsistently.** `approved-correction` and `capture-gap` are labelled `negative` but expect permitted behaviour (issue an erratum; record a gap), while `redaction-no-source-delete` — structurally the same shape — is `positive`. *Fix:* define `negative = the operation is refused or no status is inferred`, then relabel those two.

**N11 — Transcript correction has no authority.** `issue-erratum` is reserved to "record approval authority", but transcripts may exist with no approval authority at all (`transcript-without-minutes`). *Fix:* give the transcript work its own correction authority, or state that transcript correction falls to the producer under certification.

**N12 — `holds[3]` is now spent.** "Grok accepted completion with conditions; final frozen audit remains to be reconciled" is discharged by this audit and must be replaced in `candidate.3`, not carried forward.

---

## Invariant gaps

After B6's repointing, the covered set is {2, 6, 7, 8, 9, 12, 14} ∪ {15…26}. **Six invariants carry no fixture at all:**

| Position | Invariant | Missing case |
|---|---|---|
| 1 | identity distinctness | no case; also omits work/expression/manifestation and Meeting-vs-Channel distinctness (Grok's "channel reclassified as Meeting") |
| 3 | invitation acceptance ≠ content acceptance | no case |
| 4 | presence/participation/vote/assent/approval pairwise distinct | only partially reached via `channel-member-not-participant` |
| 5 | minutes do not prove individual agreement | no case — this is the model's headline claim |
| 10 | alternatives, objections, dissent, turns append-only | no case, and `lineageRule` is untested |
| 11 | task/decision lifecycles independent of record approval | no case; see B1 |

**Missing invariants** (content asserted elsewhere in the dossier or in `excludes`, never stated as an invariant):

- `excludes` bars "inferred declassification", but no invariant requires declassification to be an explicit authorized act. Time passage or an elapsed review date must not widen scope. Add invariant + fixture.
- Grok invariant 1 — "EM-KNW-03/WM-REC-012 mints no parallel Meeting or participation identity" — survives only inside `certification.rule`. Promote it; it is the anti-laundering rule behind B2.
- `boundary.owns` claims "capture handoff instant from occurrence media to governed record" (also in both studies' completion shapes) with no field, invariant or fixture. Add `captureHandoffAt` + `captureSourceRef` to `workRequired` for transcript kind, plus a fixture fixing the instant at which WM-ACT-025 capture media become the retained record.

---

## Fixture gaps

1. **No negative counterpart to `decision-two-gates`.** Only the both-gates-present case exists. The one-gate case is the whole point of the rule — and note its expected outcome is currently *unspecifiable* until B1 is resolved. Add `decision-one-gate-only` after B1, in both directions (occurrence without fixed record; fixed record without occurrence).
2. **Six fixtures assert behaviour of held neighbours** — `participation-dependent-id`, `channel-member-not-participant`, `quorum-from-channel-roster`, `decision-two-gates`, `later-authorized-decision`, `message-edit-lineage` — and `incomparable-access-scope` depends on a comparator `holds` says is unapproved. The fixture schema has no way to say so, so these read as passing conformance. *Fix:* add `status: "hold-dependent"` and `dependsOnHold` to `vercy-world-model-fixtures/v1` and mark all seven.
3. **No case for a second official minutes work** (N7).
4. **No case for a redacted passage quoted onward** — Grok's "quoting a redacted passage yields a redacted or refused quote" has no fixture; `restricted-quote` covers only the closed-session source.
5. **No case for chat laundering through a minted Meeting** (B2).
6. **No case for withdrawal or supersession** of an approved expression (B5).
7. **No case for hold interacting with redaction review** (B7).
8. **`chat-task-proposal` mixes a permission and a refusal** in one expectation ("minutes may record a task proposal; no task inferred"). Split into two cases so a runner can score them separately.

---

## Challenges upheld without change

Stated plainly so `candidate.3` does not churn them:

- **Identity.** Three-level record identity, minutes and transcript as separate works, and "never expressions of one another" are correct and survive both studies. The `workIdentity: ["recordWorkId"]` root is right — the record outlives the occurrence.
- **Dependent MeetingParticipation.** The candidate's `identity: ["meetingRef","participationId"]` genuinely reconciles the Claude reading (a dependent part, no standing identity) with the Grok requirement (separately addressable for dual-capacity and late-join). Dependent ≠ unreferenceable. The reciprocal-approval hold is correctly placed. Do not reopen; do close N1, which is what makes the addressability load-bearing.
- **Promotion gates.** `promotionRules` with provisional-only `TaskProposal`/`DecisionAlternative`, "order may vary but both must be linked", and `meeting-close-no-promotion` correctly answer Grok's strongest counterexample — chat consensus never forges status. The only defect is B1's second gate naming the wrong master.
- **Access and quotation.** Strictest-of-four with explicit refusal on incomparability, never widening, is the right shape; `accessRule.unknown` is the part most models omit.
- **External mastership.** `holds[2]` (no containment/promotion/cascade authority from relation rows) and the parent/contains inversion held rather than resolved are both correct restraint. One improvement, non-blocking: `holds[8]` should name the intended direction — WM-REC-001 as sole parent, WM-ACT-025 ↔ WM-REC-012 as REFERENCE only — so the registry reconciliation is a check, not a fresh decision.

---

## Minimal path to ACCEPT WITH LIMITS

B1 (pick a reading and delete the loser) · B2 (typed `occurrenceKind`, conditional relations, anti-minting invariant) · B3 (rewrite two `owns` entries) · B4 (`manifestations` block) · B5 (scope immutability; add the three missing operations) · B6 (invariant ids; repoint seven fixtures) · B7 (redaction/retention invariant or an honest hold) · the six uncovered invariants get one fixture each · the seven hold-dependent fixtures get marked. N1 and N9 should ride along; the rest can follow.

That yields `0.1.0-candidate.3` — reviewable, internally consistent, and still not publishable: WM-REC-012 has no specification file, WM-ACT-025 and WM-ACT-027 remain reviewable drafts, and the comparator, certification actor, promotion hooks and registry parentage all remain held.
