# EM-KNW-03 provider comparison

Claude and Grok agree that EM-KNW-03 introduces no new aggregate. WM-ACT-025 owns Meeting and occurrence-scoped participation, WM-ACT-027 owns communication channels, threads, turns and message lineage, and reserved WM-REC-012 owns durable minutes and transcript records. Minutes and transcript are separate works and never expressions of each other.

The reconciled MeetingParticipation identity is `(meetingRef, participationId)`: it is separately addressable for dual-capacity, attendance and speaker anchors, but is a dependent child of exactly one Meeting and has no independent root, model or runtime identifier.

Grok proposed that an official Decision require an authorized occurrence and approved WM-REC-012 expression. Claude showed that this would make minutes approval a second decision master. The reconciled rule requires the authorized WM-ACT-024 occurrence and WM-REC-010 fixation; approved WM-REC-012 expressions evidence the decision where minutes are required and never condition effect.

Both studies require immutable approved content, explicit correction lineage, strictest-scope quotation, refusal on incomparable access, and no automatic promotion at meeting close. The frozen audit returned REVISE for internal field consistency and coverage. All seven blocking groups and applicable non-blocking findings were remediated once without rerunning the audit. Candidate `0.1.0-candidate.3` has 34 stable invariants and 38 fixtures.
