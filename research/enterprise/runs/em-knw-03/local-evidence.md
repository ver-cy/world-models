# EM-KNW-03 local synthesis

## Disposition

- Reuse WM-ACT-025 for Meeting and contained occurrence-scoped Meeting Participation.
- Reuse WM-ACT-027 for communication channel bindings, discussion threads, turns and message references. A meeting references its chat interaction; neither aggregate contains the other.
- Complete reserved WM-REC-012 as the durable Minutes / Transcript record. Its specification is currently missing.
- Reuse WM-ACT-006 for tasks, WM-KNW-010 for proposals/decision content, WM-ACT-024 for authorized decision occurrences and WM-REC-010 for fixed decision records.
- Allocate no new runtime/model identifier.

## Identity and boundary

WM-ACT-025 masters the session occurrence, agenda items, procedural acts, attendance/presence observations, quorum determination and record obligations. WM-ACT-027 masters interaction/turn identities, channel-native message ids, threading and capture provenance. WM-REC-012 masters durable record work, expression and manifestation identities.

Meeting Participation is occurrence-scoped and has no lifecycle outside the session. Communication Channel is a referenced channel plus capabilities observed at the relevant time. Discussion Thread and Message Reference are projections of WM-ACT-027 data and cannot be edited through the Meeting profile.

Resolve the registry inversion: WM-ACT-025 produces/references WM-REC-012; WM-REC-012 should inherit from the record authority rather than treating Meeting as its parent.

## WM-REC-012 completion boundary

Minutes and transcript are separate works. Minutes summarize required matters and identify certifier; transcript declares recording/transcription method, fidelity and accuracy limits. Each work has language/version/redaction expressions and format manifestations.

Draft, certified, approved and corrected-by-erratum states remain distinct. Approval occurs through an authorized later act and is referenced by the record; approved text is never edited in place. Passages anchor to agenda items, procedural acts, speakers and time spans without copying source masters.

Per-passage classification, redaction ground, authorizer, review date, retention schedule, hold and tombstone are required. The record also identifies the handoff instant at which capture media becomes the governed durable record.

## Promotion and authority

Invitation, attendance, presence, participation, vote, assent and approval are separate assertions. A discussion turn can create:

- a task proposal, or an ordered task only with a valid authorizing reference;
- a registered decision alternative, still ineffective;
- a claim with source/evidence binding, without automatic truth;
- a decision only after WM-ACT-024 records competent authority and WM-REC-010 fixes the outcome.

Minutes evidence what occurred but do not prove each participant's agreement. A chat phrase never becomes policy by being quoted or summarized.

## Access and quotation

Quotations retain source identity, locator, fidelity and capture-gap metadata and inherit the stricter source/target classification. Restricted content entering open minutes requires declassification or a governed redaction profile. Redaction is explicit, authorized and reversible only under policy; it is never silent deletion.

## Acceptance scenario

A discussion creates a requested task with the chair's delegation reference and registers a proposed decision alternative. Official status remains unchanged. A later quorate meeting conducts an authorized vote; WM-ACT-024 records the occurrence and WM-REC-010 fixes the decision and effect onset. The earlier minutes state that a task and proposal arose, without inventing approval.

## Invariants

1. Meeting, interaction, turn, minutes, transcript, task and decision identities are distinct.
2. Invitation acceptance does not mean content acceptance.
3. Presence, participation, vote, assent and approval remain distinct.
4. Minutes do not prove individual agreement.
5. Decisions require authority valid at the decision instant.
6. Without authority an apparent decision remains a proposal.
7. Message references preserve source identity, fidelity and locator.
8. Quotations inherit the stricter access scope.
9. Approved record expressions are immutable; correction uses errata/successors.
10. Alternatives, objections, dissent and turns are append-only.
11. Tasks and decisions have lifecycles independent of minute approval.
12. No official promotion is inferred from document structure or chat wording.

## Holds

WM-ACT-025 and adjacent models remain non-canonical reviewable drafts with single-provider and source-verification holds. WM-REC-012 has a reservation but no specification; its parent/contains relationship is inverted and owners/sources are placeholders. Relations, immutable pins, access/redaction fixtures and crosswalk validation are incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
