Independent review is aligned across the published drafts. Final verdict and the seven required points follow.

**1. VERDICT: PROFILE**

WM-ACT-021 Service Case / Ticket `0.3.0-research.1` is the host aggregate. EM-COM-04 does not need a second case root.

REUSE ONLY is too thin: the contour requires a written requester-presence distinction and a pinned many-cases-to-one-incident relation that 021 states but does not ratify. NEW MODEL is refused: 021 already owns case identity, classification, requester/submitter/represented-party, intake, triage, state and assignment history, case-local communication/evidence indexes, applied commitments, outcome, closure and reopening. Inquiry and service request are profile-bound case types, not new masters. CaseInteraction belongs to WM-ACT-027; CaseResolution is an assertion inside 021; WM-REC-009 is the intake record that hands off into a case. Minting CustomerCase beside Service Case would manufacture the second aggregate the brief forbids.

**2. Anonymous mode: profile-level semantic gap**

021 allows explicit unknown on the requester slot. It does not distinguish identified, unknown/missing, withheld-by-requester, and anonymous-by-policy. That is not a free local code list. Unknown is an epistemic gap that may later be filled. Anonymous-by-policy and withheld-by-requester are governed absences: they forbid party-minting from the inquiry, constrain outbound communication, and make customer acceptance unobtainable. The profile must name that distinction and the behavioral guards. Do not freeze Claude’s four labels as catalogue vocabulary; local codes are allowed if the guards travel with them. This is not grounds for a new aggregate.

**3. Coverage of merge, many-to-one incident, and the three assertions**

Merge and history. Function `link-or-merge-case` creates a typed relation or merge while preserving aliases; effects require predecessor identities and history to remain resolvable. The duplicates/merge/originating-subject finding is the continuity artifact. Total-order interleaving of merged threads is an adoption note, not a missing type.

Many inquiries, one incident. 021’s boundary: a case is a handling aggregate; the underlying incident, defect or problem keeps its own identity and lifecycle. Originating-subject and remedy/root-cause bindings already point outward. Cardinality is not ratified because the outgoing sibling ledger is empty. The profile pins REFERENCE `0..n` cases → `0..1` incident/problem. The EM-COM-04 negative case stands: one hundred complaints must not mint one hundred incidents.

Resolution, closure, acceptance. Frozen effects: a resolved case is not automatically accepted, closed, compliant or factually corrected; each assertion has separate authority and evidence. `resolve-close-or-cancel-case` records outcome and completion separately. Closure-cancellation-and-acceptance is its own artifact. This matches the contour invariant that closure does not prove customer agreement.

**4. Sibling references and holds**

| Target | Intended edge | Hold |
|---|---|---|
| WM-ACT-027 Communication Interaction | INDEX / REFERENCE from case to interaction; 027 owns turns, delivery evidence, permission-decision refs | 027 treats outbound permission-basis as required, with an unresolved-basis marker. 021 only indexes threads. Bind requiredness in the profile; do not copy payloads. |
| WM-ACT-007 Work Order | REFERENCE case → work order | 007 owns remedy-execution authority. Work complete ≠ case resolved. |
| WM-KNW-014 Issue / Problem | REFERENCE, many cases to one problem | Frozen 014 composition declares required CHILD to 021 and describes 021 as change-request/work-item parent. 021 is a service-case aggregate, not an action parent. Direction and target-kind contradiction. Unsettled registry hold. Prefer REFERENCE both ways; never let 014 reparent 021. |
| WM-REC-009 Application / Request Record | REFERENCE request → case at handover | Adjacent intake record, not a competing case. |
| Party / product / SLA / knowledge | REFERENCE as already drafted in 021 | Outgoing ledger unapproved; all sibling IDs remain provisional. |

**5. Minimum publishable artifact**

An EM-COM-04 → WM-ACT-021 mapping/adoption binding is sufficient. No executable code.

The binding should pin: case-type profile `inquiry | service-request`; requester-presence mode plus `acceptance-obtainable`; merge chronology note; distinct resolution / acceptance / closure; REFERENCE `case → incident/problem` (`0..n`:`0..1`); REFERENCE `case → work-order`; INDEX `case → communication-interaction`. Invariants from the enterprise card travel with the binding: requester or anonymous mode; closure ≠ agreement; several inquiries may share one incident.

**6. Publication blockers versus visible limits**

Blockers for canonical publication of the profile as settled truth: `publishableCanonical=false`; Codex-only single-provider waiver; empty outgoing relation ledger; WM-KNW-014 CHILD/target-kind contradiction; unverified clause/field mappings to ISO 10002, Jira, Zendesk, Dynamics.

Visible limits that do not block a research PROFILE: reviewable-draft assurance; sector vocabularies deferred; merge-thread total-order as an adoption note; 027 permission requiredness as a sibling bind; no claim of execution, field-level audit, or standards conformance.

**7. Five adversarial fixtures**

1. Mass outage. One hundred inquiries, one problem, one work order, per-case communications. Pass only if exactly one incident/problem exists and each case keeps its own resolution, acceptance and closure.
2. Anonymous-by-policy whistleblower. No requester party minted. Outbound contact constrained. Customer acceptance marked unobtainable. Contrast with unknown/missing requester, which remains fillable.
3. Chronology merge. Two repeat inquiries merged. Predecessor case IDs and thread timestamps stay resolvable. Fail if identity collapses or history is rewritten.
4. Resolved-not-accepted. Agent records resolution; requester rejects; case stays open. Fail if resolution implies closure or acceptance.
5. Registry-contradiction probe. A problem record must not become CHILD of a service case. Work-order completion must not flip case resolution or acceptance. Fail if 014’s CHILD text is treated as settled or if 007 state is copied onto 021.
