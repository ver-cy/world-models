# EM-KNW-03 local synthesis

## Final disposition

- Complete the existing reservation `WM-REC-012` as **Minutes and Transcript Record**.
- Allocate no new model or runtime identifier.
- Reuse WM-ACT-025 for Meeting and its dependent occurrence-scoped MeetingParticipation children.
- Reuse WM-ACT-027 for channel, thread, turn, MessageReference and capture provenance.
- Reuse WM-ACT-006, WM-KNW-010, WM-ACT-024 and WM-REC-010 for Task and Decision semantics.

## Reconciled boundary

Minutes and transcript are separate durable works with independent expression and manifestation identities. A record work binds to exactly one typed occurrence authority: Meeting or interaction. WM-REC-012 never mints a Meeting to host a transcript. Approved expression content and manifestations are immutable; correction, supersession and withdrawal are append-only governed events.

MeetingParticipation is identified by `(meetingRef, participationId)` and remains a dependent child, never a new root. Meeting-sourced speaker, attendance, vote and quorum statements resolve through it rather than a bare Party or channel roster.

An official Decision requires an authorized WM-ACT-024 occurrence and WM-REC-010 fixation. Minutes may evidence the result but never condition its effect. TaskProposal and DecisionAlternative never become Task or Decision through wording, certification, approval or meeting close.

Quotation applies the strictest source, passage, container and destination scope. Incomparable scope refuses or redacts. Holds suspend disposition and redaction-review expiry. Redaction does not declassify or replace disposition; disposition preserves tombstone and lineage.

## Evidence

Grok Heavy returned **Accept with completion conditions**. One Claude Opus high no-tools frozen audit returned **REVISE** while upholding the architecture. The findings were remediated once without rerunning the audit. Candidate validation passes with 34 explicit invariants and 38 fixtures.

## Publication holds

WM-REC-012 remains a reviewable research candidate because its canonical specification is absent and neighboring models, reciprocal MeetingParticipation semantics, access comparator, actor authority and registry parentage still require approval. No blocker is published as canonical semantics.
