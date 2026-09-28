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
