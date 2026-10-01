# Verdict

**PROFILE** — bind EM-KNW-02 to the four reserved candidates with a constraining profile; mint no ID. Nothing in the contour has identity or lifecycle absent from the candidate set: Claim → WM-KNW-007, reified citation → WM-KNW-008, Argument/Decision/DecisionAlternative → WM-KNW-010, issued instrument and approval evidence → WM-REC-010. REUSE ONLY is not defensible because the candidates carry two live collisions (decision content vs. issued record; 010's inline citation bindings vs. 008's whole purpose) that reuse without constraint would resolve by duplication. NEW MODEL is unwarranted — with one exception noted under Gaps, which is a registry allocation, not a decision I take here.

# Boundary and ownership

**Both WM-KNW-010 and WM-REC-010 persist.** They sit on different planes: content vs. carrier. Single master per fact:

| Fact | Master | Other model holds |
|---|---|---|
| Decision question, admissible answers, alternatives, exclusion reasons, criteria, evaluation rounds, ranking, sensitivity | WM-KNW-010 | reference + pinned content version |
| Selected alternative, disposition, outcome statement, effect onset, conditions, divergence explanation | WM-KNW-010 | verbatim rendering, fixed by digest |
| Reasons, argument structure, objections, dissent | WM-KNW-010 | reference to the rendered statement/annex |
| Authentic expression, language versions, corrigenda, manifestation, redacted expression | WM-REC-010 | carrying-record reference only |
| Signature, seal, time-stamp, digest, fixity point, event history | WM-REC-010 | approval-stage binding by identifier |
| Issuance, publication, service, proof of service, computed challenge deadline, `became_final_at` | WM-REC-010 | read as reference; never recomputed |
| Mandate, delegation, quorum attestation, recusal, substantive status (effective/conditional/suspended/revoked/expired/reopened) | WM-KNW-010 | signatory identity and capacity only |
| Record states (captured/fixed/superseded/disposed), custody execution, tombstone | WM-REC-010 | disposition authorisation and hold reference |

The residual dual-truth risk is wording. Resolution: WM-KNW-010 masters the content; WM-REC-010 masters *which expression is authentic* and fixes it. REC-010's `question_text`, `operative_text`, `reasons_text`, `considered_options` are transcriptions carrying a content-version pin, not independent fields. After fixity, content change requires a superseding decision expression and a new record expression — never an edit on either side.

**The four-way epistemic distinction** the contour asks for maps to four different owners, which is why the v1 field `epistemic_status` cannot survive as one field:

- *Observation / source material* — the cited work and the consulted representation. WM-KNW-008 anchors it (capture artifact, digest, memento); the work itself is mastered by an external registry (see Gaps).
- *Citation stance* — WM-KNW-008's reified citation record: stance code, polarity, citation type, locator, certainty binding. A relationship record, never a truth value about the evidence.
- *Claim assessment* — WM-KNW-007: commitment level, calibrated confidence with scale binding, conflict edges registered but not adjudicated, external review references. 007 records assertion, not verdicts.
- *Decision choice* — WM-KNW-010: disposition, selected alternative, premise support status, decision-local appraisal. Distinct from 008's certainty value and never overwriting it.

# Required profile

No new ID. Binding constraints:

1. **Citation collapse.** WM-KNW-010's `dr-rsn-de-evidence-ref` must resolve to a WM-KNW-008 citation record whose citing-context is the reason or premise. `citation-type`, `citation-locator`, `citation-stance` become read-only projections of 008; 010 retains only the reference and the argument role. One locator store.
2. **Claim binding.** Every premise and conclusion slot in 010 resolves to a WM-KNW-007 claim with a version pin, or carries an explicit restatement marker. 007 never learns the decision's outcome.
3. **Argument host.** WM-KNW-010's reasoning area is the designated host for decision-bound argument structures; 007 holds role references only.
4. **Certainty separation.** 008's scheme-bound certainty value is reproduced unchanged with its read time and its scheme's unit of assessment; 010's decision-local appraisal is a separate, separately labelled field. Neither is recomputed from the other.
5. **Status separation.** 010 declares appeal windows as rules; REC-010 computes deadlines from service and owns finality dating.
6. **ADR profile.** Architecture decisions bind a lightweight jurisdictional profile on 010 (baseline optional, statement-of-reasons required, dissent optional) and may omit REC-010 attestation where no instrument is issued.
7. **Single hold register.** Both models reference one hold identifier owned by the records service.

# Invariants

- One authoring master per fact; every duplicate field is a reference or a version-pinned transcription.
- Evidence is never copied into a claim, citation, rationale or decision — only referenced with a locator.
- A citation is a relationship; recording it asserts nothing about the truth of the cited material or of the claim.
- A claim has an identified asserter, a capacity, a commitment level and scope qualifiers; a claim without them cannot leave draft.
- Registering conflict is not resolving it; marking an argument element defeated changes no decision state.
- Alternative sets and evaluation rounds are append-only; every excluded alternative keeps a recorded reason.
- Dissent is preserved as an attributed statement and is never folded into the majority rationale.
- Revocation, annulment or reopening never erases rationale, reasons, objections or superseded expressions.
- Approved content and fixed records are immutable; change means a successor, not an edit.
- Event time, observation time and ingestion time are recorded separately, RFC 3339 with explicit offset.

# Scenario walkthrough

Decisions A and B both cite source S; S is retracted.

1. Two distinct 008 citation records exist (different citing contexts and loci). Each receives an append-only `cited-source-status-observation`: status code, event time at source, observation time here, notice identifier, issuing authority. Stance, locator and excerpt are untouched.
2. `reverify-citation` appends a verification report; locator health and drift flags are set; prior digests survive.
3. WM-KNW-007 claims resting on S receive a status-notice reference and the declared local status effect. Canonical statements are not rewritten; a contradicting claim enters as a conflict edge, unresolved.
4. In each decision, `dr-rsn-fn-recheck-assumption-and-sensitivity` annotates premise support status with a check time; `dr-rsn-fn-record-objection` appends the objection with its counter-evidence binding; a defeated marking applies at argument level only.
5. A new evaluation round (n+1) records contested result statuses. Round n is never edited.
6. Decision A — S was load-bearing, sensitivity shows ranking reversal: reconsideration opened on ground *new evidence*, status transitions to reopened, and any changed outcome arrives as a superseding decision citing A. A's outcome statement, reasons, rejected alternatives and dissent remain retrievable in approved form. Decision B — S corroborative, ranking stable: annotation and a review-trigger entry only; no status change.
7. WM-REC-010: original instruments stay fixed and digest-verifiable; the superseding decision gets its own identifier and expression; event-history entries are appended on both records. Nothing is rewritten.

# Gaps and publication holds

- **Blocking — no registered master for the evidence item/source work.** 007, 008 and 010 all defer it; 008 caches only a non-authoritative descriptor and points at an external bibliographic registry. `EvidenceArtifact` has independent identity and lifecycle, so this is the one genuine new-model candidate — raise to registry allocation; do not mint here.
- **Blocking — 010 relation ledger.** Only the WM-ACT-032 inbound and WM-KNW-008 outbound relations are registered. The REC-010, ACT-024, POL-021 and KNW-007 relations this entire ownership split depends on are unregistered.
- **Blocking — 008 deduplication key undefined.** As written, two decisions citing the same source could be silently merged, which defeats the acceptance scenario directly.
- **Blocking — 010 artefact identity.** Unregistered discriminators for four serial artefacts, and the dissent record's sequence scope is ambiguous (per party vs. per decision). Dissent preservation is not yet name-safe.
- 007's CHILD to WM-KNW-001 is unledgered; its argumentation owner is an open gap for non-decision arguments.
- 010 has no function that records a constituent reason or issues the statement of reasons.
- Certainty-scheme pins unresolvable (ECO has no release version; GRADE dated only "October 2013"); GRADE's unit of assessment is a body of evidence, not one citation.
- Publication status: all four are `reviewable-draft`, `publishableCanonical: false`. 007, 008 and 010 carry the single-provider waiver (Grok waived 2026-08-29T09:06:27Z); every artifact must display it. 010 additionally carries the superseded-source hold (40 CFR 1502.14/1505.2, historical-pattern label only).
- Deferred and not resolved here: approval as an independent object, standing authorisations (licences, permits), and cross-jurisdictional applicability.
