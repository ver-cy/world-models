# Independent review request: EM-KNW-02 Decision, claim and evidence

Review this Enterprise metamodel boundary independently. Use public provenance, argumentation, records, decision and evidence practice where useful. Distinguish source facts from design inference. Do not invent a Vercy catalogue/runtime identifier.

Existing candidates:

- WM-KNW-007 Claim / Proposition masters claim identity, scoped statement, asserter, commitment/confidence and lifecycle.
- WM-KNW-008 Evidence / Citation masters an identifiable citation relationship: citing context, cited-source reference, stance, locator, consulted representation, verification and source-status observations. It explicitly does not master the evidence item itself.
- WM-KNW-010 Decision / Rationale masters decision content: question, alternatives, criteria, evaluations, selection, rationale, argument, objections and dissent.
- WM-REC-010 Decision / Approval Record masters an authoritative issued record, fixation, attestation, issuance/service, redacted expressions and record disposition.
- All four are published research specifications but remain reviewable drafts with publication holds.

Proposed decision: **PROFILE** over the four candidates, no profile ID. WM-KNW-010 is the authoring master for decision content; WM-REC-010 is the master for which fixed expression is authentic. Any duplicated question/outcome/reasons/options text in the record is a version-pinned transcription, never an independently editable fact.

Proposed additional finding: **Evidence Artifact / Source Work** is a genuine missing aggregate candidate, identifier unassigned. The cited item survives every individual citation, may support many claims/decisions, and has its own correction/retraction/supersession lifecycle. WM-KNW-008 caches only a non-authoritative descriptor.

Test:

1. Two decisions cite the same source; it is later corrected or retracted. Trace effect without rewriting citations, claims, rationale, alternatives, dissent or fixed records.
2. A link to a document is incorrectly treated as proof that a claim is true.
3. A rejected alternative later becomes preferable after counter-evidence.
4. An ADR records a choice without a formally issued approval instrument.

Check separation among source observation, citation stance, claim assessment and decision-local appraisal. Check that alternatives/evaluation rounds/dissent are append-only; conflict registration is not adjudication; revocation/reopening preserves rationale; and every duplicated field has one authoring master.

Return at most 1000 words with: Verdict (REUSE ONLY / PROFILE / NEW MODEL); ownership split; correction to WM-KNW-010/WM-REC-010 overlap; whether Evidence Artifact needs an independent aggregate; required constraints; scenario results; publication blockers.
