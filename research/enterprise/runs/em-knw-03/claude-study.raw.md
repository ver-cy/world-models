## Verdict

**Reuse and extend; no new model.** EM-KNW-03 becomes an enterprise profile over two reserved bases plus one reserved-but-missing spec:

- **Meeting** and **MeetingParticipation** → WM-ACT-025 (already carries identity/classification, convening basis, invitation state, presence observation, quorum, agenda, conduct, votes, capture, openness). MeetingParticipation is occurrence-scoped and has no identity outside the session: it stays a part of WM-ACT-025, not a sibling model.
- **CommunicationChannel**, **DiscussionThread**, **MessageReference** → WM-ACT-027 (channel classification and capability, endpoint binding, turn record, turn-native identifier, thread/reply relations, delivery evidence, capture provenance).
- **WM-REC-012** is the durable-record owner; its boundary is defined below for later completion.

Do not merge WM-ACT-025 and WM-ACT-027. Both specialise WM-ACT-018, but the discriminators are agenda, quorum, convening authority and record obligation — present in the former, absent by construction in the latter. A meeting references its in-session chat as an interaction; an interaction references a meeting as context. Neither contains the other.

## Evidence

WM-ACT-025 declares WM-REC-012 out of scope for draft/approval/correction/authenticity/disposition, and explicitly states that "approval of the minutes" appears only as an agenda item of a later session. WM-ACT-027 owns turns, threading and channel capability. WM-ACT-024 owns the decision occurrence and authority; WM-REC-010 owns the authoritative decision record; WM-KNW-010 owns decision content, alternatives and rationale; WM-ACT-006 owns task intent, authorising reference and lifecycle. EM-KNW-02 established that a citation supplies a source reference and stance only, never truth.

## Identity/mastership

Session identity, agenda items, procedural acts, quorum determinations and the item-to-record anchor map are mastered by WM-ACT-025. Turn identity, channel-native message identifiers, thread membership and derivation method are mastered by WM-ACT-027. Record identity — work/expression/manifestation, certification, disposition — is mastered by WM-REC-012. MessageReference in the enterprise profile is a read-only projection of a WM-ACT-027 turn identifier plus locator; it is never an authoring surface.

## Meeting/participation

WM-ACT-025 as-is, with the profile adding no elements. Note one registry defect: WM-REC-012 declares `parent_ids: WM-ACT-025` while WM-ACT-025 declares `contains_ids: WM-REC-012`. Resolve to CONTAINS-by-production in one direction only; parenthood belongs to WM-REC-001.

## Channel/thread/message

CommunicationChannel = WM-ACT-027 channel reference plus capability constraints observed at turn time. DiscussionThread = thread reference plus declared derivation method, with cross-channel bridging flagged by confidence. MessageReference = turn identifier, native identifier, locator, author, authored/received times, fidelity level, capture-gap marker. Encrypted channels yield metadata-only references; this is recorded, not treated as a gap.

## Minutes/transcript

WM-REC-012 boundary, sufficient for completion:

- **Durable record identity.** Work identifier for the record owed by one occurrence; expression discriminators for language, version and redaction variant; manifestation for format. Minutes and transcript are **separate works**, not expressions of one another.
- **Draft/approval/correction.** Draft → certified → approved → corrected-by-erratum. Approval is asserted here and referenced as an agenda item by the later session; the earlier session never holds approval state. Corrections are errata or successor expressions; approved text is never edited in place.
- **Transcript versus minutes.** Transcript claims verbatim or machine-generated fidelity with a transcription method and accuracy indicator; minutes claim summary fidelity with required content (persons present, matters discussed, conclusions reached, recorded votes) and a certifying officer.
- **Agenda/time anchors.** Passage-to-item and passage-to-procedural-act anchors resolved against WM-ACT-025 identifiers; offsets/spans for timed text. Anchors are references, never copies of agenda content.
- **Attribution.** Speaker reference, capacity in which they spoke, addressee, and whether attribution was observed, reconstructed or machine-inferred.
- **Quotation.** Locator plus source reference; no content duplication.
- **Access/redaction.** Per-passage classification, redaction marker with ground, authoriser and review date; anonymised public expression linked internally to the full expression.
- **Retention.** Schedule reference, trigger, strictest-applicable-floor rule, hold state, tombstone.
- **Capture hand-off.** Name the instant at which capture media held under WM-ACT-025 become the statutorily retained record owned here.

## Promotion to official objects

| From discussion | To | Required authority / evidence |
|---|---|---|
| Turn | MessageReference | none; identity, fidelity and access class travel |
| Turn | Task (WM-ACT-006) | proposal intent needs none; order intent needs a resolvable authorising reference within delegation limits |
| Turn | Proposal / alternative (WM-KNW-010) | standing to table; registered append-only, status not effective |
| Turn | Official fact (WM-KNW-007 + WM-KNW-008) | competent asserter; citation carries stance and locator only |
| Turn | Decision (WM-ACT-024 → WM-REC-010) | authority basis in force, competence limit satisfied, decision-rule attestation, then fixation |

## Access and quotation

A quotation inherits the **more restrictive** of source and target classification, retains the source reference and locator, and resolves back rather than embedding content. Closed-portion content, blind recipients and accommodation data are excluded from general projections. Redaction is recorded as a marker with ground and authoriser, never as silent removal. Quoting a restricted turn into open minutes requires a recorded declassification or a redaction profile.

## Lifecycle

Meeting occurrence closes → record obligations emitted with content requirement, producer, certifier and anchors → WM-REC-012 drafts, certifies, approves at a later session, corrects by erratum, discloses under its access schedule, disposes under the strictest floor. Tasks and decisions raised in session run their own lifecycles from the moment of creation, independent of minute approval.

## Scenario

A thread produces: (1) a Task at order intent, authorising reference resolving to the chair's delegation, WM-ACT-006 state `requested`, citing the MessageReference; (2) a WM-KNW-010 alternative with WM-ACT-024 intent `proposal`, `doNotPerform` false, no effective status. Official status is unchanged. At a later convened occurrence, an authorised body with attested quorum conducts a vote, WM-ACT-024 records the occurrence, WM-REC-010 issues the fixed record with effect onset; only now does status change. Minutes of the earlier session record that a task and a proposal arose; they do not record an approval. **Negative case fails**: the chat line never becomes policy.

## Invariants

1. Minutes evidence what occurred; they do not prove any individual's agreement.
2. Presence ≠ participation ≠ vote ≠ assent ≠ approval; invitation acceptance is acceptance of an invitation, not of content.
3. A decision has a resolvable authority basis in force at the decision instant; absent that, it is a proposal.
4. A quotation preserves source identity and the most restrictive applicable access scope.
5. Alternatives, objections, dissent, turns and evaluation rounds are append-only.
6. Approved minute expressions are immutable; change is erratum or successor.
7. No promotion is inferred from structure; each requires an explicit authorised act.

## Minimal completion shape

WM-REC-012 needs: record identity and expression discriminators; record-kind code (minutes/transcript/summary); fidelity and transcription method; certification and approval state with certifying officer; anchor map to session items and acts; attribution set; redaction and classification per passage; retention binding with hold and tombstone; capture-media hand-off instant; disposition evidence.

## Holds

WM-ACT-025 is `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, under a single-provider waiver with Grok waived; its sources are unverified live and four coverage dimensions are over-claimed. WM-REC-012 has no spec file. The registry parent/contains inversion, placeholder owners and empty source fields are unreconciled. The three blocking decisions remain open. This review is a boundary opinion on a frozen dossier; it is neither canonically complete nor installable.
