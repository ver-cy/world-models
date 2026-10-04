# Frozen no-tools semantic audit — EM-KNW-02

Use only this frozen packet. Do not browse, call tools, invent identifiers, mutate registry reservations or grant publication authority.

Disposition: PROFILE over four bases plus identifier-unassigned Evidence Artifact / Source Work candidate. Audit semantics only.

Return at most 600 words with exactly: Verdict (ACCEPT WITH LIMITS, REVISE, or REJECT); Critical findings; Required holds; Scenario result; Identifier decisions.

## Profile candidate

{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-KNW-02",
  "name": "Enterprise Decision, Claim and Evidence",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-KNW-010",
    "WM-REC-010",
    "WM-KNW-007",
    "WM-KNW-008"
  ],
  "constraints": [
    "WM-KNW-007 masters claim identity, scoped statement, asserter, capacity, commitment, calibrated confidence and claim lifecycle; it records assertion rather than truth verdict.",
    "WM-KNW-008 masters each immutable citation act: citing context, cited-source reference, stance, locator, consulted representation, verification and source-status observations; its source descriptor is non-authoritative.",
    "WM-KNW-010 masters decision content: question, alternatives, criteria, append-only evaluation rounds, selection, outcome, rationale, argument, objections and dissent.",
    "WM-REC-010 masters the authentic issued expression, fixation, digest, attestation, issuance, service, redacted expressions, record event history and disposition.",
    "Question, outcome, reasons, options and evidence text duplicated in WM-REC-010 are version-pinned transcriptions of a WM-KNW-010 revision and never independently editable facts.",
    "WM-KNW-010 drops approval-as-owned and references an approval activity or WM-REC-010 instrument; a decision or ADR may exist without a formally issued instrument.",
    "Decision evidence bindings resolve to WM-KNW-008 citation identities; citation type, locator and stance are read-only projections while decision-local argument role remains WM-KNW-010-owned.",
    "Every decision premise and conclusion resolves to a version-pinned WM-KNW-007 claim or an explicit local restatement; WM-KNW-007 never inherits the decision outcome.",
    "Source observation, citation stance, claim assessment and decision-local appraisal remain separately named, timed and mastered and never prove one another.",
    "A citation, link or document reference asserts neither source truth nor claim truth; conflict registration and defeated argument marking are not adjudication.",
    "Alternatives, evaluation rounds, exclusion reasons, objections and attributed dissent are append-only and remain retrievable after reopening, revocation or supersession.",
    "Counter-evidence appends source observations, verification, claim notices and decision appraisal rounds without rewriting citations, claims, rationale, dissent or fixed records.",
    "WM-KNW-010 reasoning hosts decision-bound argument structures; WM-XCT-028 remains a referenced neighbor and is not absorbed.",
    "WM-KNW-010 declares appeal-window rules while WM-REC-010 computes service-based deadlines and owns finality dating.",
    "Every duplicate field has one authoring master; approved content and fixed records change only through explicit successors, never in-place edits."
  ],
  "candidateRevision": 2,
  "references": [
    "WM-XCT-028",
    "WM-ACT-032",
    "WM-REC-001"
  ],
  "holds": [
    "WM-KNW-007, WM-KNW-008, WM-KNW-010 and WM-REC-010 remain non-canonical reviewable drafts.",
    "WM-KNW-010 to WM-REC-010, WM-KNW-007 and approval-activity relationships are absent from the registered relation ledger.",
    "WM-KNW-008 parentage to WM-KNW-007 remains unresolved as navigational versus compositional.",
    "WM-KNW-010 and WM-REC-010 purpose text still overlaps until reciprocal authoring and transcription amendments land.",
    "WM-KNW-008 citation deduplication keys and WM-KNW-010 serial-artifact and dissent sequence identities remain unresolved.",
    "Evidence Artifact / Source Work has independent identity but no registry allocation; no identifier may be guessed here.",
    "Certainty-scheme editions and units of assessment remain unpinned and licensed standards support alignment only.",
    "Executable runtime semantics, package conversion and canonical live verification remain pending."
  ]
}


## Allocation candidate

{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-KNW-02",
  "proposedName": "Evidence Artifact / Source Work",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A source work or evidence item retains identity independently of every claim, citation, decision and consulted representation and can be cited repeatedly across contexts.",
    "versionIdentity": "Corrections, editions, retractions, withdrawals and successor expressions append dated source states or expressions while preserving the identity and provenance of earlier cited forms.",
    "independentLifecycle": [
      "created",
      "issued",
      "corrected",
      "superseded",
      "retracted",
      "withdrawn",
      "preserved",
      "disposed"
    ],
    "mastership": "source-work or evidence-artifact authority"
  },
  "boundary": {
    "owns": [
      "stable source-work or evidence-item identity",
      "source kind, creators, issuing authority and provenance",
      "dated editions, expressions or states",
      "representation and fixity references",
      "correction, supersession, retraction and withdrawal history",
      "canonical external identifiers and identifier provenance",
      "preservation and disposition references"
    ],
    "references": [
      {
        "target": "WM-KNW-008",
        "purpose": "Citation acts, locators, stance and verification"
      },
      {
        "target": "WM-KNW-007",
        "purpose": "Claims assessed or supported in citing contexts"
      },
      {
        "target": "WM-REC-001",
        "purpose": "Document and record manifestations or preserved representations"
      },
      {
        "target": "WM-REC-010",
        "purpose": "Authentic issued decision expressions when used as sources"
      }
    ],
    "excludes": [
      "citation identity, locator, stance or citing-context appraisal",
      "claim truth, confidence or commitment",
      "decision rationale, alternative evaluation or outcome",
      "record authenticity decisions owned by record authorities",
      "automatic propagation of source status into claim truth or decision validity"
    ]
  },
  "objects": {
    "SourceWork": {
      "identity": [
        "sourceWorkId"
      ],
      "required": [
        "sourceKind",
        "titleOrDesignation",
        "authorityRef",
        "status"
      ],
      "optional": [
        "creatorRefs",
        "canonicalIdentifierBindings",
        "successorRefs"
      ],
      "lifecycle": [
        "created",
        "issued",
        "superseded",
        "retracted",
        "withdrawn"
      ]
    },
    "SourceExpression": {
      "identity": [
        "sourceWorkId",
        "expressionId"
      ],
      "required": [
        "issuedAt",
        "contentDigest",
        "status"
      ],
      "optional": [
        "edition",
        "language",
        "supersedesExpressionRef",
        "effectiveFrom",
        "effectiveTo"
      ],
      "lifecycle": [
        "draft",
        "issued",
        "corrected",
        "superseded",
        "retracted"
      ]
    },
    "SourceStatusEvent": {
      "identity": [
        "sourceStatusEventId"
      ],
      "required": [
        "sourceExpressionRef",
        "eventKind",
        "occurredAt",
        "authorityRef",
        "evidenceRef"
      ],
      "optional": [
        "reason",
        "successorExpressionRef"
      ]
    },
    "RepresentationBinding": {
      "identity": [
        "representationBindingId"
      ],
      "required": [
        "sourceExpressionRef",
        "representationRef",
        "contentDigest",
        "validFrom"
      ],
      "optional": [
        "validTo",
        "mediaType",
        "accessRef"
      ]
    }
  },
  "invariants": [
    "A source-work identity is independent of every citation and citing context.",
    "Two citations to the same source remain distinct citation acts.",
    "Every citation pins the consulted source expression or explicitly records that the expression is unresolved.",
    "A mutable URL or cached title never establishes source identity or fixity.",
    "Corrections, retractions and withdrawals append source status history and never rewrite prior citations.",
    "Source retraction does not automatically erase claims, decisions, rationale, dissent or fixed records.",
    "Citation stance and verification remain owned by WM-KNW-008 and are not source properties.",
    "Source status never by itself establishes or disproves the truth of a claim.",
    "Representations carry digest and provenance and do not silently replace the source expression they embody.",
    "External identifiers are scheme- and authority-qualified and may not be treated as globally unique without evidence.",
    "Superseded and retracted expressions remain resolvable for historical interpretation.",
    "Disposition preserves required provenance and cited fixity references."
  ],
  "holds": [
    "Registry identifier allocation is pending and no identifier may be guessed.",
    "Source-work, bibliographic, document, record, publication-edition and evidence boundaries require dedicated reconciliation.",
    "Parent models remain non-canonical and relation ledgers are incomplete.",
    "Citation deduplication must preserve distinct acts while resolving one source expression.",
    "Exact standards editions and public crosswalks remain unpinned.",
    "Package conversion and canonical live verification remain pending."
  ],
  "candidateRevision": 2
}


## Fixtures

{
  "format": "vercy-model-allocation-fixtures/v1",
  "proposedName": "Evidence Artifact / Source Work",
  "cases": [
    {
      "id": "shared-source",
      "kind": "positive",
      "input": "Two decisions cite the same issued source expression through separate locators and stances.",
      "expect": "One source expression and two immutable citation acts remain independently resolvable."
    },
    {
      "id": "source-retraction",
      "kind": "positive",
      "input": "A cited source is later retracted.",
      "expect": "A source status event is appended; citations and decisions preserve history and separately reassess their premises."
    },
    {
      "id": "corrected-edition",
      "kind": "positive",
      "input": "A source publishes a corrected edition.",
      "expect": "A successor expression is linked without changing the digest or identity of the earlier consulted expression."
    },
    {
      "id": "link-equals-proof",
      "kind": "negative",
      "input": "A document URL is treated as proof that the citing claim is true.",
      "expect": "The inference is rejected: the URL is neither fixed source identity nor truth assessment."
    },
    {
      "id": "rewrite-after-retraction",
      "kind": "negative",
      "input": "Retraction causes old citations, dissent and rationale to be deleted.",
      "expect": "Deletion is rejected; prior states remain resolvable and new assessments append."
    },
    {
      "id": "rejected-alternative-reopened",
      "kind": "positive",
      "input": "Counter-evidence makes a previously rejected alternative preferable.",
      "expect": "A new evaluation round and optional reopening preserve the prior ranking, exclusion reason, rationale and dissent."
    },
    {
      "id": "adr-without-instrument",
      "kind": "positive",
      "input": "An ADR records a choice but no formal approval instrument is issued.",
      "expect": "WM-KNW-010 remains valid without WM-REC-010; no approval or record authenticity is inferred."
    },
    {
      "id": "shared-source-distinct-locators",
      "kind": "positive",
      "input": "Two decisions consult one source expression at different locators and with different stances.",
      "expect": "One source expression and two distinct citation acts remain independently resolvable."
    },
    {
      "id": "source-status-not-truth",
      "kind": "negative",
      "input": "A source retraction automatically marks every cited claim false and every decision invalid.",
      "expect": "The inference is rejected; reassessment appends at claim and decision layers."
    },
    {
      "id": "record-edits-decision",
      "kind": "negative",
      "input": "Editing transcription text in an issued approval record changes the authored decision rationale.",
      "expect": "Validation rejects dual authoring and requires a new decision revision and fixed successor expression."
    },
    {
      "id": "merge-citations",
      "kind": "negative",
      "input": "Two citation acts to one source are merged because the source identifier matches.",
      "expect": "Validation rejects the merge because citing context, locator, stance and consulted representation differ."
    },
    {
      "id": "conflict-is-adjudication",
      "kind": "negative",
      "input": "Registering a contradictory claim is treated as resolving the conflict.",
      "expect": "Validation rejects the verdict; conflict and adjudication remain separate."
    },
    {
      "id": "erase-dissent",
      "kind": "negative",
      "input": "Decision reopening deletes earlier objections and dissent.",
      "expect": "Validation rejects deletion; earlier rounds and attributed dissent remain append-only."
    }
  ]
}


## Local evidence

# EM-KNW-02 local synthesis

## Disposition

- Create an **Enterprise decision, claim and evidence profile** over WM-KNW-010, WM-REC-010, WM-KNW-007 and WM-KNW-008.
- Do not create a profile runtime ID.
- Raise **Evidence Artifact / Source Work** as a genuine new-model candidate with identifier unassigned. The four reserved models intentionally do not master the cited item itself.

## Boundary and ownership

WM-KNW-007 masters claim identity, statement, scope, asserter, commitment, confidence and claim lifecycle. WM-KNW-008 masters the reified citation relationship: citing context, cited source reference, stance, locator, consulted representation, verification and source-status observations. A citation is not evidence truth.

WM-KNW-010 masters decision content: question, alternatives, exclusion reasons, criteria, evaluations, selection, conditions, rationale, arguments, objections and dissent. WM-REC-010 masters the authentic issued expression: fixation, signature/seal, issuance, publication/service evidence, record finality timestamps, redacted expressions and records disposition.

Duplicated REC-010 text fields are version-pinned transcriptions of WM-KNW-010 content. They are never independent authoring fields. Content changes create a successor decision and a successor fixed expression.

## Required profile constraints

1. WM-KNW-010 evidence bindings resolve to WM-KNW-008 citation IDs. Locator, stance and citation type remain read-only projections from WM-KNW-008.
2. Every argument premise/conclusion resolves to a pinned WM-KNW-007 claim or is explicitly marked as a local restatement.
3. Observation/source material, citation stance, claim assessment and decision-local appraisal remain separate.
4. Alternative sets, evaluation rounds, objections and dissent are append-only.
5. WM-KNW-010 declares challenge rules; WM-REC-010 owns service events and computed finality dates.
6. Revocation, annulment, reopening or later counter-evidence never erases earlier rationale or fixed expressions.
7. ADR is a lightweight WM-KNW-010 profile and need not create a formal WM-REC-010 instrument unless one is issued.

## Acceptance result

Two decisions may use separate citations to the same source artifact. If that source is later retracted, each citation receives an append-only status observation and verification report. Related claims retain their canonical statements and gain status-notice/conflict references. Each decision rechecks its own premise support and sensitivity. One may reopen and produce a successor decision while the other remains effective. Original outcomes, alternatives, dissent and fixed records remain resolvable.

The negative case fails: a link to a document supplies only a source reference and citation stance. It cannot turn the citing claim into an established fact.

## Evidence Artifact candidate

The cited work or evidence item has identity and lifecycle independent of every claim, citation and decision. It may be cited many times, corrected, retracted, superseded or preserved while all citation acts remain intact. WM-KNW-008 explicitly caches only a non-authoritative descriptor. This proves a missing aggregate boundary, but no registry identifier is allocated, so the candidate remains research-only.

## Holds

All four existing models remain `publishableCanonical: false`. Their relation ledgers do not yet support the proposed binding; WM-KNW-008 deduplication is insufficiently specified; several serial artefact identities are ambiguous; and three bases carry a single-provider waiver. Evidence Artifact requires registry allocation and its own source/bibliographic/record boundary review. This checkpoint is not an installable release.


## Claude study

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


## Grok study

Lucas has not objected. Filing the team review now: PROFILE over the four, held missing source-work aggregate, no invented identifier. **Verdict: PROFILE** over WM-KNW-007, WM-KNW-008, WM-KNW-010 and WM-REC-010. No profile ID. Not REUSE ONLY (ownership collision plus a missing source-work master). Not NEW MODEL for this subject card. No catalogue or runtime identifier is minted.

Source fact: EM-KNW-02 is queued; its candidate types already include Claim, EvidenceArtifact, Argument, Decision and DecisionAlternative. Card invariants already require an authored claim-in-context, that evidence is not automatically true, and that revocation does not erase rationale. Acceptance case is two decisions sharing later-refuted evidence without history rewrite. Negative case is a document link treated as proof. Catalogue candidates are exactly the four named models. A published WM does not complete an enterprise card. EM-COM-04 is the applicable pattern: PROFILE, no new runtime identity.

### Ownership split
Source facts from the published drafts (all `0.3.0-research.1`, reviewable-draft, publication holds open):

- **WM-KNW-007** authors claim identity, scoped statement, asserter, commitment/confidence and claim lifecycle. Quoted: “The model records assertion, not verdicts.” It does not own evidence items, argument graphs, review workflows or truth adjudication. Evidence binds through 008.
- **WM-KNW-008** is a relationship. It authors the citation act: citing context, cited-source reference, stance, locator, consulted representation, verification and source-status observations. It explicitly does not master the cited item. The bibliographic descriptor is a non-authoritative cache. Retraction/correction events are observations, not ownership of the work. Parent link to 007 is held as navigational, not compositional.
- **WM-KNW-010** authors decision content: question, alternatives, criteria, evaluation rounds, selection, rationale, argument, objections and dissent. Relation-ledger hold: REC-010 is unregistered; frozen contract lists only WM-ACT-032 and WM-KNW-008.
- **WM-REC-010** authors the issued record: authentic fixed expression, fixation/digest, attestation, issuance/service, redacted expressions and disposition. Purpose text also lists question, reasons and evidence as if authored there.

Inference: 007 assessment (commitment/confidence) is not a verdict and is not 010’s local appraisal. 008 stance is not either of those. WM-XCT-028 is a neighbor mixin (support-binding, warrant, counter-evidence); it must not be absorbed into 010. WM-MED-003 covers publication-edition, not general evidence items.

Public practice (alignment, not conformance): Toulmin separates claim, warrant and backing; SACM separates Artifact from ArtifactReference; CiTO/Open Annotation type citation stance; ISO 15489 governs record authenticity, not live decision authoring; Nygard/AWS/GDS ADR is written content that is superseded rather than rewritten; GOV.UK treats write-then-submit-for-approval as two acts.

### Correction to WM-KNW-010 / WM-REC-010 overlap
Published 010 lists approval among owned concerns. Published REC-010 purpose lists question/reasons/evidence as authored substance. Both are collisions.

Required correction: 010 drops approval-as-owned and references REC-010 or an approval activity. REC-010 treats any duplicated question, outcome, reasons or options as a version-pinned transcription of a 010 revision — never an independently editable fact. An ADR may exist as 010 content with no REC-010 instrument.

### Evidence Artifact / Source Work
Yes: a genuine missing aggregate. Identifier unassigned. Do not mint one here.

The cited item survives every citation, may support many claims and decisions, and has its own correction, retraction, expression-of-concern and supersession lifecycle. 008 can only cache a descriptor and record an observation pointing at that master. Without a shared work identity, per-citation status copies drift and scenario 1 fails. FHIR-style cited-artifact currentState and SACM Artifact ≠ ArtifactReference require the same split. This is a held finding for later research, not a new model for EM-KNW-02.

### Required constraints
1. Source observation ≠ citation stance ≠ claim assessment ≠ decision-local appraisal.
2. Alternatives, evaluation rounds and dissent are append-only.
3. Conflict registration is not adjudication.
4. Revocation or reopening preserves prior rationale.
5. Every duplicated field has one authoring master.
6. A citation or document link is not proof of truth.
7. 010 may exist without a REC-010 instrument.
8. Do not absorb XCT-028 argument graphs into 010.
9. No invented catalogue or runtime ID.

### Scenario results
1. Two decisions cite one source later corrected or retracted. Effect traces through the shared source-work status (or an 008 observation on that master). Citations, claims, rationale, alternatives, dissent and fixed records stay. New appraisal rounds append. Fails if status is copied per citation with no work master.
2. A document link treated as proof is rejected: 007 records assertion not verdict; 008 stance is not assessment; constraint 6 is explicit. Matches the card negative case.
3. A rejected alternative later becomes preferable: append a new evaluation round; optionally reopen. Prior rejection reasons remain. Matches “preserve rejected alternatives.”
4. An ADR records a choice without a formally issued approval: 010 only. REC-010 absent is valid.

### Publication blockers
- All four remain reviewable drafts (single-provider waiver and/or live source-and-version verification).
- 010 relation-ledger hold: REC-010 unregistered; ownership statements must be withdrawn or the edge registered.
- 008 parent_ids to 007: navigational versus compositional unresolved.
- Candidate mapping depth is index-and-publication-metadata only.
- 010/REC-010 purpose-text overlap is unreconciled in the published drafts.
- Missing source-work aggregate has no assigned ID and must not receive one in this review.
- XCT-028 composition already names a missing source/citation model and a decision-record model; the profile declares neighbors, it does not absorb them.
- Adjacent held cards: EM-KNW-01 (document/carrier) and EM-DAT-07 (analytical conclusion ≠ adopted decision).
- Paywalled ISO 15489 / 23081 / 42010 text was not read at clause level on REC-010; no conformance claim.

Assurance labels used above: observed on catalogue pages and quoted purpose/hold text; inference on the PROFILE composition, the overlap correction and the unassigned-aggregate finding.


## Provider comparison

# EM-KNW-02 provider comparison

Claude and Grok independently select **PROFILE** over WM-KNW-007, WM-KNW-008, WM-KNW-010 and WM-REC-010 with no profile or runtime identifier. Both also identify **Evidence Artifact / Source Work** as an independent missing aggregate whose identifier remains unassigned.

Both providers separate five authorities: source work and its expressions; immutable citation acts; claim assertion and assessment; decision content and local appraisal; and authentic fixed decision records. WM-KNW-010 authors question, alternatives, evaluation rounds, selection, rationale, objections and dissent. WM-REC-010 fixes an authentic expression; any repeated content is a version-pinned transcription. An ADR may exist without a formal issued instrument.

Grok sharpens the collision: WM-KNW-010 must drop approval-as-owned, WM-REC-010 must stop authoring question/reasons/evidence, and WM-XCT-028 remains a neighbor rather than decision-owned argument content. Source correction or retraction appends status observations and reassessment without rewriting citations, claims, rationale, alternatives, dissent or fixed records.

Canonical publication remains held by non-canonical bases, missing relation-ledger edges, unresolved WM-KNW-008 parentage, citation deduplication and dissent identity gaps, the unallocated source-work aggregate, unpinned certainty schemes and incomplete standards crosswalks.
