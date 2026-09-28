# Frozen audit request: EM-KNW-03

Independently review only the frozen materials below. No tools or browsing. Return Verdict (ACCEPT / ACCEPT WITH LIMITS / REVISE / REJECT), blocking findings, non-blocking findings, invariant/fixture gaps and exact minimal remediations. Challenge identity, dependent MeetingParticipation, Minutes/Transcript work separation, promotion gates, immutable expressions, anchors, access/redaction, retention and external mastership. Do not invent identifiers or claim publication readiness.

## Candidate
```json
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-KNW-03",
  "modelId": "WM-REC-012",
  "registryId": "vr.wm-rec-012",
  "name": "Minutes and Transcript Record",
  "version": "0.1.0-candidate.2",
  "entryKind": "aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent durable minutes and transcript records produced from a meeting or communication occurrence, with independent work, expression and manifestation identities, certification, approval, correction, passage anchors, access, redaction and retention.",
  "boundary": {
    "owns": [
      "minutes-work and transcript-work identity",
      "language version and redaction expression identity",
      "format manifestation references and fixity bindings",
      "certification approval and erratum lineage",
      "passage anchors to external session items acts turns speakers and time spans",
      "per-passage classification redaction provenance and review date",
      "retention schedule hold tombstone and disposition evidence",
      "capture handoff instant from occurrence media to governed record"
    ],
    "delegates": [
      "meeting occurrence agenda procedural acts presence and quorum to WM-ACT-025",
      "communication channels turns messages threads and capture provenance to WM-ACT-027",
      "task identity authorization and lifecycle to WM-ACT-006",
      "decision content alternatives and rationale to WM-KNW-010",
      "authorized decision occurrence to WM-ACT-024",
      "fixed decision record and effect onset to WM-REC-010",
      "generic record custody fixity and retention authority to WM-REC-001"
    ],
    "excludes": [
      "meeting or communication lifecycle",
      "message payload mastership",
      "task execution",
      "decision authority or legal effect",
      "proof of participant agreement",
      "silent deletion or inferred declassification"
    ]
  },
  "recordWorks": {
    "minutes": {
      "fidelity": "summary",
      "required": [
        "requiredMatterCoverage",
        "personsPresentRefs",
        "conclusionsReached",
        "recordedVoteRefs",
        "certifyingOfficerRef"
      ],
      "cardinalityPerOccurrence": "0..1 official minutes work"
    },
    "transcript": {
      "fidelity": "verbatim-or-declared",
      "required": [
        "transcriptionMethod",
        "fidelityClass",
        "accuracyIndicator",
        "captureGapMarkers"
      ],
      "cardinalityPerOccurrence": "0..n transcript works"
    },
    "rule": "Minutes and transcript are separate works and never expressions of one another; either may exist without the other."
  },
  "expressions": {
    "identity": [
      "workId",
      "expressionId",
      "language",
      "version",
      "redactionVariant"
    ],
    "lifecycle": [
      "draft",
      "certified",
      "approved",
      "corrected-by-erratum",
      "superseded",
      "withdrawn"
    ],
    "immutability": "Approved expressions are immutable; correction creates an erratum or successor expression.",
    "required": [
      "expressionId",
      "workRef",
      "language",
      "version",
      "expressionKind",
      "createdAt",
      "status"
    ],
    "optional": [
      "approvedAt",
      "certificationRef",
      "predecessorExpressionRef",
      "redactionVariantRef",
      "accessScopeRef"
    ],
    "transitionRule": "draft -> certified -> approved; approved is immutable; correction creates erratum or successor; restriction creates overlay or derivative."
  },
  "passageAnchor": {
    "required": [
      "passageId",
      "sourceRef",
      "sourceLocator",
      "anchorType",
      "fidelityClass",
      "classification"
    ],
    "optional": [
      "agendaItemRef",
      "proceduralActRef",
      "turnRef",
      "speakerRef",
      "speakerCapacity",
      "startOffset",
      "endOffset",
      "captureGapRef"
    ]
  },
  "relations": [
    {
      "target": "WM-ACT-025",
      "relation": "REFERENCE",
      "purpose": "Anchor passages and record obligations to meeting occurrence agenda and procedural acts.",
      "required": true
    },
    {
      "target": "WM-ACT-027",
      "relation": "REFERENCE",
      "purpose": "Resolve channels threads turns messages speakers and capture provenance.",
      "required": false
    },
    {
      "target": "WM-ACT-006",
      "relation": "REFERENCE",
      "purpose": "Reference tasks proposed or ordered during discussion without importing task lifecycle.",
      "required": false
    },
    {
      "target": "WM-KNW-010",
      "relation": "REFERENCE",
      "purpose": "Reference proposals alternatives and decision rationale content.",
      "required": false
    },
    {
      "target": "WM-ACT-024",
      "relation": "REFERENCE",
      "purpose": "Resolve the authorized decision occurrence and authority valid at the instant.",
      "required": false
    },
    {
      "target": "WM-REC-010",
      "relation": "REFERENCE",
      "purpose": "Resolve the fixed authoritative decision record and effect onset.",
      "required": false
    },
    {
      "target": "WM-REC-001",
      "relation": "REFERENCE",
      "purpose": "Resolve generic record custody fixity retention and disposition controls.",
      "required": true
    }
  ],
  "operations": [
    {
      "id": "draft-record",
      "effect": "Create a draft minutes or transcript work and expression from declared occurrence sources and capture gaps.",
      "authority": "record producer"
    },
    {
      "id": "certify-record",
      "effect": "Attest fidelity class required-matter coverage and certifier identity.",
      "authority": "authorized certifying officer"
    },
    {
      "id": "approve-expression",
      "effect": "Approve one immutable expression through a referenced authorized later act.",
      "authority": "record approval authority"
    },
    {
      "id": "issue-erratum",
      "effect": "Create an erratum or successor expression linked to the approved predecessor.",
      "authority": "record approval authority"
    },
    {
      "id": "publish-redacted-expression",
      "effect": "Create a governed redaction variant with passage grounds authorizer and review date.",
      "authority": "disclosure or records authority"
    }
  ],
  "invariants": [
    "Meeting, interaction, turn, minutes, transcript, task and decision identities remain distinct.",
    "Minutes and transcript are separate works.",
    "Invitation acceptance does not mean content acceptance.",
    "Presence, participation, vote, assent and approval remain distinct.",
    "Minutes evidence what occurred and do not prove individual agreement.",
    "A decision requires authority valid at the decision instant; absent authority it remains a proposal.",
    "Message references preserve source identity locator fidelity and capture-gap metadata.",
    "A quotation inherits the more restrictive source or target access scope.",
    "Approved expressions are immutable; correction uses errata or successors.",
    "Alternatives objections dissent and turns remain append-only.",
    "Tasks and decisions keep lifecycles independent from record approval.",
    "No official promotion is inferred from document structure or chat wording.",
    "Redaction records passage ground authorizer and review date and is never silent deletion.",
    "Disposition preserves a resolvable tombstone and hold evidence.",
    "MeetingParticipation has occurrence-scoped dependent identity inside exactly one WM-ACT-025 Meeting and is never standing membership.",
    "Channel membership never implies MeetingParticipation, presence or access to minutes or transcript.",
    "DiscussionThread and MessageReference cannot carry official Task or Decision status.",
    "TaskProposal is not Task and DecisionAlternative is not Decision.",
    "Official Decision status requires both an authorized decision occurrence and a fixed approved WM-REC-012 expression.",
    "Minutes work and transcript work have separate identities; either may exist without the other.",
    "Certification and minutes approval record evidence and never mint a Task or Decision.",
    "Quorum and vote attribution resolve through MeetingParticipation, not channel roster or bare Party.",
    "Quote access is the strictest source passage container or quote-site scope; incomparable scope refuses or redacts.",
    "Redaction overlays preserve source, ground, authorizer, review date and lineage.",
    "Meeting close never auto-promotes a proposal, alternative, Task or Decision.",
    "MessageReference edit delete forward and nested-quote provenance remains WM-ACT-027-owned."
  ],
  "holds": [
    "Referenced meeting and communication models remain reviewable drafts.",
    "Candidate relation rows confer no containment mutation promotion or cascade authority.",
    "External transcript and records projections require pinned mappings and do not imply conformance.",
    "Grok accepted completion with conditions; final frozen audit remains to be reconciled.",
    "WM-ACT-025 MeetingParticipation child identity requires reciprocal base-model approval.",
    "Task and decision promotion hooks, certification actor and access-scope comparator require registry approval.",
    "MessageReference edit/delete/forward/nested-quote semantics require WM-ACT-027 completion.",
    "WM-REC-012 parent/contains relation with WM-ACT-025 conflicts with WM-REC-001 parentage and remains held."
  ],
  "disposition": {
    "kind": "complete-reserved-model",
    "newModelId": false,
    "reason": "WM-REC-012 owns durable minutes and transcript works; Meeting, participation, interaction, task and decision identities remain external."
  },
  "meetingParticipationExpectation": {
    "base": "WM-ACT-025",
    "authority": "non-normative neighbor expectation pending base approval",
    "identity": [
      "meetingRef",
      "participationId"
    ],
    "scope": "identified dependent child of exactly one Meeting occurrence; never an independent root or reusable standing membership",
    "required": [
      "partyRef",
      "capacity",
      "effectiveFrom",
      "participationKind"
    ],
    "optional": [
      "effectiveTo",
      "presenceObservationRefs",
      "voteActRefs"
    ],
    "rule": "Invitation, channel membership, presence, participation, vote, assent and approval are pairwise non-implying."
  },
  "communicationExpectation": {
    "base": "WM-ACT-027",
    "authority": "non-normative neighbor expectation",
    "owns": [
      "CommunicationChannel",
      "DiscussionThread",
      "turn",
      "MessageReference"
    ],
    "messageReferenceRule": "Carries source identity, locator, edit/delete/forward/nested-quote provenance, fidelity and access class; never official status."
  },
  "workIdentity": [
    "recordWorkId"
  ],
  "workRequired": [
    "recordKind",
    "occurrenceRef",
    "producerRef",
    "createdAt",
    "retentionBindingRef"
  ],
  "workKinds": [
    "minutes",
    "transcript"
  ],
  "certification": {
    "identity": [
      "certificationId"
    ],
    "required": [
      "expressionRef",
      "certifierRef",
      "authorityBasisRef",
      "certifiedAt",
      "fidelityClass",
      "coverageAssertion",
      "evidenceRefs"
    ],
    "rule": "Certification attests the record and never mints a Decision, Task, Meeting or participation."
  },
  "accessRule": {
    "comparator": "effective quote scope is the strictest of source, passage, container and quote-site scopes",
    "unknown": "If scopes cannot be compared, quotation is refused or redacted; never widened",
    "redaction": "Overlay or derivative expression with passage ground authorizer review date and source lineage; source is never silently deleted."
  },
  "promotionRules": [
    {
      "from": "DiscussionThread turn",
      "to": "TaskProposal",
      "effect": "provisional only; no WM-ACT-006 task identity"
    },
    {
      "from": "DiscussionThread turn",
      "to": "DecisionAlternative",
      "effect": "provisional only; no official decision status"
    },
    {
      "from": "TaskProposal",
      "to": "WM-ACT-006 Task",
      "requires": [
        "authorized task-creation occurrence",
        "delegation or authority reference"
      ]
    },
    {
      "from": "DecisionAlternative",
      "to": "official Decision",
      "requires": [
        "authorized WM-ACT-024 decision occurrence",
        "fixed approved WM-REC-012 expression",
        "authority basis in force"
      ],
      "rule": "order may vary but both must be linked before official status changes"
    }
  ],
  "lineageRule": "Promotion and correction are append-only; source turns, proposals, alternatives, dissent and prior expressions remain addressable."
}
```

## Fixtures
```json
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-REC-012",
  "version": "0.1.0-candidate.2",
  "cases": [
    {
      "id": "chat-task-proposal",
      "kind": "negative",
      "input": "A chat turn asks an employee to investigate but carries no delegation reference.",
      "expect": "Minutes may record a task proposal; no ordered WM-ACT-006 task or official decision is inferred.",
      "expectRule": "INV-001"
    },
    {
      "id": "later-authorized-decision",
      "kind": "positive",
      "input": "A later quorate meeting conducts an authorized vote and issues a fixed decision record.",
      "expect": "The earlier record remains unchanged; WM-ACT-024 and WM-REC-010 supply decision authority and effect onset.",
      "expectRule": "INV-002"
    },
    {
      "id": "minutes-versus-transcript",
      "kind": "positive",
      "input": "One session produces concise minutes and a machine transcript.",
      "expect": "Two separate works are minted with distinct fidelity claims, expressions and manifestations.",
      "expectRule": "INV-003"
    },
    {
      "id": "approved-correction",
      "kind": "negative",
      "input": "A speaker attribution is wrong after minutes approval.",
      "expect": "An erratum or successor expression corrects attribution; approved bytes and prior expression remain resolvable.",
      "expectRule": "INV-004"
    },
    {
      "id": "restricted-quote",
      "kind": "negative",
      "input": "Closed-session content is quoted into a public draft.",
      "expect": "Publication is blocked unless governed declassification or redaction exists; the stricter access scope wins.",
      "expectRule": "INV-005"
    },
    {
      "id": "capture-gap",
      "kind": "negative",
      "input": "An encrypted side channel cannot be captured and only metadata is available.",
      "expect": "The transcript records the capture gap and fidelity limitation; missing content is not fabricated.",
      "expectRule": "INV-006"
    },
    {
      "id": "retention-hold",
      "kind": "positive",
      "input": "Normal disposition date arrives while a legal hold applies.",
      "expect": "Deletion is blocked; hold and schedule remain recorded and any later disposition leaves a tombstone.",
      "expectRule": "INV-007"
    },
    {
      "id": "participation-dependent-id",
      "kind": "positive",
      "input": "One party joins Meeting M twice in different capacities.",
      "expect": "Create two occurrence-scoped participation children; no standing identity",
      "expectRule": "INV-015"
    },
    {
      "id": "channel-member-not-participant",
      "kind": "negative",
      "input": "A channel member never joins the meeting.",
      "expect": "Do not infer participation or presence",
      "expectRule": "INV-016"
    },
    {
      "id": "thread-consensus-not-decision",
      "kind": "negative",
      "input": "A chat thread reaches unanimous consensus.",
      "expect": "Retain a DecisionAlternative only; official status unchanged",
      "expectRule": "INV-017"
    },
    {
      "id": "proposal-not-task",
      "kind": "negative",
      "input": "A turn asks for follow-up without an authorized task creation.",
      "expect": "Retain TaskProposal; no Task identity",
      "expectRule": "INV-018"
    },
    {
      "id": "decision-two-gates",
      "kind": "positive",
      "input": "Authorized decision occurrence and approved fixed expression both exist.",
      "expect": "Permit official status link without changing either master",
      "expectRule": "INV-019"
    },
    {
      "id": "minutes-without-transcript",
      "kind": "positive",
      "input": "Meeting has approved minutes and no transcript.",
      "expect": "Accept one minutes work and zero transcript works",
      "expectRule": "INV-020"
    },
    {
      "id": "transcript-without-minutes",
      "kind": "positive",
      "input": "Captured session has transcript but no official minutes obligation.",
      "expect": "Accept transcript work independently",
      "expectRule": "INV-020"
    },
    {
      "id": "certification-not-decision",
      "kind": "negative",
      "input": "Minutes are certified but no decision occurrence exists.",
      "expect": "Do not mint or activate Decision",
      "expectRule": "INV-021"
    },
    {
      "id": "quorum-from-channel-roster",
      "kind": "negative",
      "input": "Quorum is computed from channel members.",
      "expect": "Reject; resolve occurrence-scoped participation and presence",
      "expectRule": "INV-022"
    },
    {
      "id": "incomparable-access-scope",
      "kind": "negative",
      "input": "Source and quote-site scopes have no comparator result.",
      "expect": "Refuse or redact quote; never widen",
      "expectRule": "INV-023"
    },
    {
      "id": "redaction-no-source-delete",
      "kind": "positive",
      "input": "A later restriction redacts one approved passage.",
      "expect": "Create overlay or derivative; retain source and lineage",
      "expectRule": "INV-024"
    },
    {
      "id": "meeting-close-no-promotion",
      "kind": "negative",
      "input": "Meeting closes with unresolved task and decision proposals.",
      "expect": "Keep proposals provisional",
      "expectRule": "INV-025"
    },
    {
      "id": "message-edit-lineage",
      "kind": "positive",
      "input": "Quoted message was edited then forwarded.",
      "expect": "Resolve WM-ACT-027 edit and forward lineage",
      "expectRule": "INV-026"
    }
  ]
}
```

## Claude study
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


## Grok study
Verdict. Accept with completion conditions. Place Meeting and occurrence-scoped MeetingParticipation under WM-ACT-025; CommunicationChannel, DiscussionThread, turns and MessageReference under WM-ACT-027; complete reserved WM-REC-012 as the durable-record module. MeetingParticipation needs independent identity. Minutes and transcript are separate works. Reject readings that give EM-KNW-03 mastership, treat participation as a (Meeting × Party) link, merge minutes and transcript, or let discussion, meeting close, or minutes certification change official task or decision status.

Strongest evidence. Four authorities stay uncollapsed: WM-ACT-027 interaction; WM-ACT-025 meeting occurrence and participation; WM-REC-012 certified record; separate task and decision authorities. No automatic promotion is the only rule that stops chat agreement from forging official status. Distinct invitation, presence, participation, vote, assent and approval match distinct lifecycles. Quote-inherits-stricter-scope is required once MessageReference can move a restricted turn into a wider minutes audience.

Strongest counterexample. A standing-team thread reaches consensus with no Meeting and no certified WM-REC-012 expression, yet operations treat the thread as binding. The model correctly refuses official status, then fails operationally unless task and decision authorities expose a non-forging provisional state. Failure modes: dummy Meeting laundering chat into WM-REC-012; MessageReference treated as the record; channel reclassified as Meeting. Without independent MeetingParticipation identity, speaker anchors cannot cite a late-joining or dual-role participant separately from Party and channel membership.

Identity / mastership. WM-ACT-025 masters Meeting/Session and MeetingParticipation. MeetingParticipation is independent, bound to exactly one occurrence, not reused, and not standing membership, org-role, channel membership, or a WM-REC-012 speaker label. One party may hold multiple capacities or sequential episodes; votes, anchors and in-meeting attribution need that referent. If published WM-ACT-025 treats participation only as a link, independent identity is still required under WM-ACT-025. EM-KNW-03 mints no second participation id and no parallel Meeting id. WM-ACT-027 masters CommunicationChannel, DiscussionThread and MessageReference. A meeting may use a channel; the channel is not the meeting. WM-REC-012 masters minutes work, transcript work, expressions, certification, per-passage access/redaction and retention. Task authority masters Task; discussion creates only a TaskProposal. Decision authority masters Decision and the authorized decision occurrence; discussion creates only a DecisionAlternative. EM-KNW-03 links these; it does not take mastership.

WM-REC-012 boundary. In: minutes work; transcript work; draft versus approved expressions; certification bound to one WM-ACT-025 occurrence; agenda/time/speaker locators; per-passage access and redaction; retention; citations to MeetingParticipation, MessageReference and agenda items. Out: meeting and participation; channel, thread and MessageReference identity; live invitation, presence, vote, assent and official approval; task and decision authorities. It records and certifies; it does not convene, converse, assign or decide. Approved minutes are not the decision act. Minutes and transcript are separate works. Transcript is descriptive, time/speaker-anchored, correctable, typically stricter. Minutes are the curated official record; the approved expression is the immutable fixed record. Cardinality: 0..1 official minutes work and 0..n transcript works per occurrence; either may exist without the other.

Promotion rules. WM-ACT-027 discussion may create a TaskProposal or DecisionAlternative; precursors have no official status. Only task authority mints a Task. Agenda placement is not a decision. Official decision status changes only when an authorized decision occurrence fires and a fixed WM-REC-012 approved expression exists; both required; order may vary. Thread reactions are interaction evidence, not meeting votes and not official approval, unless decision authority designates that occurrence (default: it has not). Lineage is append-only. Minutes certification records; it does not mint the Decision. Meeting close does not auto-promote. Quorum binds to the decision occurrence and MeetingParticipation identities, not the channel roster.

Access / quotation. Quote access is min(source, passage, container, quote-site) and never widens. Channel membership is not minutes, transcript or decision-record access. Participation does not grant passage-level transcript rights. Redaction overlays the expression; it does not delete the cited discussion, MeetingParticipation or decision occurrence. Quoting a redacted passage yields a redacted or refused quote. An approved expression is immutable; later restriction is an overlay or derivative. Chat quotation of a later official decision stays at chat scope until the quote cites the fixed record.

Scenario. Channel C hosts thread T. A posts a task-proposal turn. B posts a decision-alternative turn cited by MessageReference R2. Invitations issue for Meeting X; invitation is not presence or participation. Meeting X occurs with occurrence-scoped MeetingParticipation identities. Decision authority fires D on the alternative cited by R2; task authority may separately accept the task proposal. Minutes work Minutes_X is created; optional separate transcript work Transcript_X may be created. Approved expression E_min is certified and immutable; anchors cite MeetingParticipation. If E_min quotes via R2, the quote inherits the stricter scope. Readers see proposals in T; official status only from D plus fixed E_min.

Invariants.

1. EM-KNW-03 mints no parallel Meeting identity.
2. Each MeetingParticipation has its own identity, bound to exactly one WM-ACT-025 occurrence.
3. Channel membership is not MeetingParticipation.
4. Invitation, presence, participation, vote, assent and official approval are pairwise non-implying.
5. DiscussionThread and MessageReference cannot carry official task or decision status.
6. TaskProposal is not Task; DecisionAlternative is not Decision.
7. Official decision status requires an authorized decision occurrence and a fixed approved WM-REC-012 expression.
8. Minutes work identity is not transcript work identity.
9. An approved expression is immutable; correction is a new expression or overlay.
10. Quote access equals min(source, thread/channel, cited passage, destination).
11. WM-REC-012 speaker and attendance anchors cite MeetingParticipation, not Party or channel member.
12. Meeting close does not auto-promote precursors.

Minimum completion shape. WM-ACT-025: occurrence-scoped MeetingParticipation identity plus distinct invitation, presence, participation and in-meeting vote acts. WM-ACT-027: MessageReference mastership for edit, delete, forward and nested quote; channel–meeting binding. WM-REC-012: minutes and transcript works; draft and approved expressions; certification; anchors; per-passage access/redaction; retention; corrigendum path. Typed precursor hooks into task and decision authorities. Access-scope comparator. Certification actor. Non-forging provisional states on the external authorities.

Blockers. WM-REC-012 has no specification. Task and decision authorities are external; promotion needs typed hooks not given here. Owner of invitation, presence, vote, assent and official approval is unnamed; they must remain distinct types, not flags on MeetingParticipation. MessageReference edit/delete/forward/nested-quote mastership is unspecified. Stricter-access comparator is undefined. Dual-mastership risk if Meeting and Minutes work are both treated as the record of what was decided. Channel–Meeting binding, corrigendum path, redaction-versus-retention conflict and certification actor are unspecified.
