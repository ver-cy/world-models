# Enterprise Assertion Provenance — Independent Research Contour (EM-XCT-03)

**Date:** 2026-09-21  
**Status of this text:** independent research contour for an authorized Vercy workflow. Not an approval, not a grant to publish, not a change of permissions, not contact authority, and not a claim that any schema proves external truth.  
**Method:** public primary sources and synthetic examples only. No private organization material. No local code execution. No licensed schema copied. Unread normative clauses are marked unverified and are not cited as requirements.

---

## 1. Decision on the boundary hypothesis

The hypothesis that a small English **Enterprise Assertion Provenance (EAP)** contract “may be associated with WM-XCT-012 for discovery and reference selected patterns from 026 and 028” is acceptable only as a *semantic* association. It is not acceptable as subtype, profile, or machine-identity bind.

**Recommended disposition: standalone companion.**

| Option | Verdict | Reason |
|---|---|---|
| Reuse 012 as the contract | Reject | 012 is a mixin on *any host subject* (asset, dataset, physical item, statement, agent output). EAP’s grain is an attributable account about an *exact external claim or artifact version*. Different identity-class. |
| Profile 012 | Reject | Profiling inherits 012’s host-subject mixin semantics and its undischarged holds. |
| Extend 012 (child with parent machine identity) | Reject | Task rule: do not bind a partial representation to a legacy parent’s machine identity. `publication.json` has `parent digest: null`; the brief’s parent digests are not present in the published files. |
| Standalone companion + semantic ALIGN/REFERENCE | **Accept** | Own runtime identity and spec digest. ALIGN to 012 patterns. REFERENCE selected 026/028 patterns. No duplicate universal WM row merely to satisfy a registry count. |
| Defer the contour | Reject as a whole; defer listed externals | The contour is needed; PKI, IAM, source connectors, claim ontologies, and inference engines stay external. |

012 already owns derivation, fixity, attestation, first-hand versus reconstructed basis, occurrence/record time, and a thin confidence slot on a host subject. 026 already owns an independently identified, method-qualified assessment about a subject and refuses a default numeric confidence. 028 already owns typed support/counter-support and **explicitly never carries the propositional content of the host claim**; a citation is not support by itself. Binding EAP as a 012 subtype would either duplicate 026/028 or smuggle claim-content into 012.

Natural-language composition links in those three drafts are conceptual references, not executable package imports. No old hold is discharged by this review.

---

## 2. Sources actually read (edition / date / section)

Only these public texts were used. “Read” means the cited pages and sections, not the entire family of each standard.

| Source | Edition / date | URL | What was read | Adopt / reject / unverified |
|---|---|---|---|---|
| WM-XCT-012 Provenance | 0.3.0-research.1, published, `publishableCanonical: false` | https://ver.cy/models/wm-xct-012-provenance/spec.yaml and `publication.json` | Purpose, in/out of scope, neighbor distinctions, identity priority, append-only rule, holds | Adopt patterns: first-hand vs reconstructed, occurrence≠record time, digest-as-binding-not-identity, append-only correction. Reject as parent identity. Holds remain. |
| WM-XCT-026 Quality/Confidence | same version/status | https://ver.cy/models/wm-xct-026-quality-confidence/spec.yaml and `publication.json` | Assertion identity, measure/method/scale, confidence-about-assertion, calibration, exclusions, holds | Adopt ConfidenceAssessment shape. Reject ownership of provenance graphs and claim content. DQV-tier and unread JCGM/ISO holds remain. |
| WM-XCT-028 Evidence/Rationale | same version/status; `synthesisSha256` `0ebeb503…` | https://ver.cy/models/wm-xct-028-evidence-rationale/spec.yaml and `publication.json` | Scope, “never carries propositional content”, citation≠support, integrity≠truth, holds | Adopt EvidenceLink polarity, selector/state, withdrawal-triggers-review. Reject as parent. Unread ISO/SACM texts remain alignment-only. |
| W3C PROV-DM | Recommendation 30 April 2013 | http://www.w3.org/TR/2013/REC-prov-dm-20130430/ | §§5.1–5.4: Entity, Activity, Agent, Generation, Usage, Derivation, Revision, Quotation, PrimarySource, Attribution, Association, Delegation, Invalidation, Bundle | Adopt entity/activity/agent and distinct derivation kinds. Reject as sufficient for epistemic kind, record-time, support polarity, or claim pins. PROV does not specify when a derivation “really” exists. |
| W3C PROV-CONSTRAINTS | Recommendation 30 April 2013 | https://www.w3.org/TR/2013/REC-prov-constraints-20130430/ | C41, C42, C52, uniqueness/ordering; validity of a *graph*, not external truth | Adopt: derivation generation strictly precedes later generation; irreflexive specialization; cycles containing strictly-precedes are invalid. Reject treating constraint satisfaction as truth. |
| OpenLineage | Docs version 1.53.0 (project tag 1 Sep 2026) | https://openlineage.io/docs/spec/object-model | Run / Job / Dataset; RunEvent, JobEvent, DatasetEvent; facets | Adopt run≠job≠dataset identity and “how datasets come into being”. Reject as a claim-truth model. Design-time events are not runs. |
| SLSA | Spec Version 1.2 current; provenance predicate type `https://slsa.dev/provenance/v1` | https://slsa.dev/spec/v1.2/ and https://slsa.dev/spec/v1.0/provenance | Purpose of provenance; `buildDefinition` / `runDetails` / `builder` / `resolvedDependencies` | Adopt “how produced”, builder identity, resolved materials, immutable subject-by-digest. Reject any reading that a passing provenance check verifies statements *inside* the artifact. |
| in-toto Attestation Statement | `_type` `https://in-toto.io/Statement/v1`; framework latest tagged v1.2 | https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md | `_type`, `subject` (digest required), `predicateType`, `predicate` | Adopt authenticated binding of a predicate to digest-identified subjects. Subjects assumed immutable. Reject as proof of document-statement truth. |
| Nanopublication Guidelines | Working draft (page undated) | https://nanopub.net/guidelines/working_draft/ | Three graphs; well-formedness (five distinct URIs; provenance must reference assertion; pubinfo must reference nanopub) | Adopt assertion ≠ provenance-of-assertion ≠ publication-info. The working-draft page itself has no retraction section; `npx:retracts` is treated as related vocabulary, not this page. |
| W3C Web Annotation Data Model | Recommendation 23 February 2017 | https://www.w3.org/TR/2017/REC-annotation-model-20170223/ | Annotation / Body / Target / Motivation; Selectors; TimeState / HttpRequestState; creator ≠ generator | Adopt selector + captured state + cached copy. Motivations are intent, not support polarity. External-resource properties are hints; the remote resource remains the source of truth about itself. |
| W3C Web Annotation Protocol | Recommendation 23 February 2017 | https://www.w3.org/TR/annotation-protocol/ | POST create, PUT overwrite, DELETE | Reject PUT-overwrite as EAP’s revision model (it destroys prior claim text). |
| W3C DQV | Working Group Note 15 December 2016 | https://www.w3.org/TR/2016/NOTE-vocab-dqv-20161215/ | Abstract; QualityMeasurement (`isMeasurementOf`, `computedOn`, `value`); QualityAnnotation ⊑ oa:Annotation with motivation `dqv:qualityAssessment` | Adopt independently identified assessment and refusal of one definition of quality. Reject as a Recommendation and as a confidence/retraction model. 026 already holds the Note-versus-Rec conflict. |

**Not read as normative text (do not cite clauses):** ISO/IEC 27037:2012, ISO/IEC/IEEE 15026-2:2022, ISO/IEC/IEEE 42010:2022, OMG SACM 2.3 PDF, JCGM 100 and 106 full text, ISO/IEC 25012 and ISO 19157-1 licensed enumerations, PREMIS 3.0 full text. Alignment language only.

Digest discrepancy to record, not paper over: the brief’s parent digests (`aa615535…`, `efd72d84…`, `3aab7ecb…`) do not appear in the published `publication.json` files, which report `parent digest: null` and different `synthesisSha256` values. A companion must not treat the brief digests as the parents’ machine identity.

---

## 3. Comparison of three primary approaches

### 3.1 W3C PROV (lineage graph)

PROV-DM is a Recommendation for *how things came to be*: entities with fixed aspects, activities over time, agents bearing responsibility, generation/usage, and derivation with three named specializations — revision, quotation, primary source. A primary source is “produced by some agent with direct experience and knowledge about the topic, at the time of the topic’s study, without benefit from hindsight.” That is the closest PROV comes to first-handness, and it is a *derivation kind*, not an epistemic tag on a sentence. Bundles make provenance-of-provenance an entity.

PROV-CONSTRAINTS police internal consistency (unique generation, generation precedes usage, derivation-generation strictly precedes later generation, irreflexive specialization). A graph can be valid and still describe a lie. PROV “does not attempt to specify the conditions under which derivations exist.”

**Gap for EAP:** no vocabulary for observed versus source-asserted versus inference versus proposal versus unverified; no separate record-time axis; no support/counter-support polarity; no pinned propositional content; no method-qualified confidence.

### 3.2 Operational lineage / attestation (OpenLineage + in-toto/SLSA) and nanopublications

OpenLineage 1.53.0 records that a **Job** in a **Run** used and produced **Datasets**. It “cares how Datasets come into being.” Facets can carry schema, source-code location, SQL, and even data-quality *metrics/assertions* as observations emitted by a job. Design-time `JobEvent`/`DatasetEvent` are not runs. OpenLineage does not model whether a cell in a dataset is a true statement about the world.

SLSA provenance (predicate type `https://slsa.dev/provenance/v1`) attests that a builder executed a `buildDefinition` with resolved dependencies. Purpose: verify the artifact was *built as expected*, or rebuild it. It is not a verifier of claims printed inside the artifact. in-toto Statement v1 binds a predicate to subjects that **MUST** have a digest and are assumed immutable; matching is by digest, not filename.

Nanopublications separate three graphs with five distinct URIs: assertion, provenance-of-assertion, publication-info. That separation is the right *shape* for EAP. The guidelines page does not itself specify retraction.

**Gap for EAP:** these systems prove production, digest binding, or publication packaging. They do not distinguish “we observed these bytes” from “the sentences in those bytes are true of a live system.”

### 3.3 Evidence / assessment (Web Annotation + DQV)

Web Annotation is a typed link: a Body is related to a Target for a Motivation (`commenting`, `assessing`, `linking`, …). Selectors address a part; TimeState/HttpRequestState record the representation that was seen; a cached copy may be kept. Motivations are purpose, not polarity. Protocol PUT overwrites. Properties of external resources recorded on the annotation are hints.

DQV, a Working Group Note, gives QualityMeasurement / Metric / Dimension / QualityAnnotation and says it “does not provide a formal, complete definition of quality.” It has no confidence class, no claim-pin, and no retraction graph. 026 already records the authority-tier conflict of using a Note as a load-bearing shape.

**Gap for EAP:** annotation ≠ support; measurement ≠ confidence-about-a-pinned-assertion; overwrite ≠ immutable revision.

---

## 4. Exact objects and identity rules

EAP needs three exported record types plus one activity type. Claim text, people directories, source catalogues, IAM, PKI, inference engines, and connectors remain external.

### 4.1 Identity classes that must stay distinct

1. `record_id` — stable identity of a ProvenanceRecord / EvidenceLink / ConfidenceAssessment.  
2. `revision_id` — identity of one immutable revision of that record.  
3. `target_id` + `target_version` + `target_digest` — the external claim or artifact version the account is *about*.  
4. `capture_id` + `capture_digest` — the observed acquisition of source bytes.  
5. `agent_id` — referenced, not minted here.  
6. `schema_id` + `schema_version` — this contract’s identity, not the host claim’s.

A content digest is a **binding**, never a substitute identity for a mutable or versioned subject (012 identity priority, adopted). A filename, path, date, or display label is never an identifier.

### 4.2 Exported types

**AssertionPin** (pointer, not a knowledge model). External target identity, version label if any, content digest of the exact bytes or canonical claim text that was seen, optional media type, optional locator. Cardinality of digest: 0..1 with explicit `digest_absent_reason` if missing. EAP does not store the claim ontology.

**CaptureActivity** (own identity). Observed acquisition of a file or stream. Records instrument, agent, occurrence time, record time, bytes digest, selector used, cached-copy locator, and `acquisition_kind = observed-bytes`. It never upgrades itself into “the statements are true.”

**ProvenanceRecord.** An attributable account about one AssertionPin (1..1) at one target digest/version. Carries `account_kind`, derivation edges to other pins or captures, agent roles, the four time axes, and a pointer to current ConfidenceAssessment and EvidenceLinks. Does not embed claim text.

**EvidenceLink.** A qualified relation from a ProvenanceRecord or AssertionPin to a CaptureActivity or external source pin. Polarity: `supports` | `counters` | `contextualizes`. Independence: `same-origin` | `derived-copy` | `independent`. Selector + source state + excerpt fidelity as in 028/OA. A bibliographic citation with no polarity and no captured state is not an EvidenceLink.

**ConfidenceAssessment.** A separately identified, method-qualified assessment *about* a pinned assertion or about a ProvenanceRecord. Value + scale + method + calibration status + assessor + purpose. Not a property crumpled onto the pin.

Activities that generate, revise, retract, or assess these records also have identity (OpenLineage-style run id is an acceptable projection, not the semantics).

---

## 5. Epistemic kind: where it lives, and why it must not collapse

**Finding:** epistemic kind is a property of a *statement-in-role*, not of a file and not of an agent. More than one kind can attach to one pin without collapse.

| Kind | Lives on | What a trusted host may validate | What remains a declaration |
|---|---|---|---|
| `observed-acquisition` | CaptureActivity | Digest matches cached bytes; occurrence/record times well-formed; agent id present | That the capture was authorized in the real world |
| `source-asserted` | EvidenceLink or quoted excerpt | That an excerpt is bound to a capture digest and selector | That the source’s sentence is true |
| `inference` | ProvenanceRecord.account_kind and/or the generating activity | That inputs are cited as captures or pins; that the method id is present | That the inference is correct |
| `proposal` | ProvenanceRecord.lifecycle = proposed | Schema and attribution | Any operational effect |
| `unverified` | default when evidence is absent or integrity failed | That the flag is present | Nothing else |
| `first-hand` vs `reconstructed` | ProvenanceRecord.account_basis (012 pattern) | That the code is from the closed set | The historical fact of presence |

**Required coexistence example (synthetic).** Capture C1 observed bytes of memo M at digest H at 2026-09-01T10:00:00Z. Memo M *source-asserts* “billing cluster X is live-verified.” Analyst agent A2 runs model R v3 and *infers* “cluster X passed verification.” Those three facts may be recorded together. Presenting the inference as a live-system verification is the critical negative case named in the brief. Schema validation of the EAP instance does not observe cluster X.

An AI synthesis remains an inference even when every input capture is `observed-acquisition`. Direct inputs do not change the kind of the output.

---

## 6. Citation versus support versus independent corroboration

- **Citation** names a source. It is a locator. 028: a citation is not support by itself.  
- **Support** is a typed, attributable EvidenceLink with polarity `supports`, a captured state or an explicit `source_unavailable` reason, and a warrant/assumption pointer if the leap from excerpt to claim is not identity.  
- **Independent corroboration** requires `independence = independent` after shared-origin collapse. Two copies of the same memo, or a summary derived from that memo, are not independent sources. OpenLineage inputs that are the same dataset namespace+name, and SLSA resolvedDependencies that share a digest, are the operational analogues.

**Withdrawal.** Retracting or countering an EvidenceLink sets the link’s lifecycle to `withdrawn` and emits a review obligation on every ProvenanceRecord that treated it as current support. It does **not** rewrite the original conclusion and does **not** assert that the conclusion is false. The conclusion remains, flagged `support-weakened`, until a new revision is issued.

---

## 7. Time, revision, integrity, unavailability

Four time axes, all RFC 3339 with explicit offset or Z (012/026/028 pattern):

| Axis | Meaning | Must not be used as |
|---|---|---|
| `event_time` | When the external thing happened | Record ingestion |
| `valid_time` | Interval during which the account is offered as current | Proof of truth |
| `capture_time` | When bytes or a selector-state were acquired | Event time |
| `record_time` | When this revision was written on the trusted host | Event time |

Late records require `late_record=true` and a justification; backdating requires an approver reference. Trusted current root = the unique non-superseded, non-retracted revision per `record_id` visible under the caller’s disclosure view.

**Integrity versus truth.** A matching digest means the bytes are the bytes that were captured. A failing digest means integrity is unknown or broken. Neither fact is the truth of sentences inside the bytes. 028 already states: integrity verification “never asserts that the supported claim is true” and systems must not present a passing check as validation of the claim.

**Unavailable / missing / deleted / updated sources.**

- Source unreachable: EvidenceLink may exist with `source_state = unavailable` and `anchor_absent_reason`.  
- Captured state retained: selector + TimeState + cached copy (OA pattern). The cache is a new CaptureActivity, not a second independent source.  
- Source later corrects or deletes: new CaptureActivity of the correction notice; new EvidenceLink; original capture remains.  
- External target updates: new AssertionPin version/digest; old pin remains; records that pinned the old digest do not silently retarget.  
- Missing evidence: `unverified` + `evidence_absent_reason`. Silence is not corroboration.

**Cycles.** Actual derivation (`wasDerivedFrom` analogue) MUST be acyclic in the PROV-CONSTRAINTS sense (strictly-precedes). Harmless reference cycles (A cites B cites A as bibliography) are allowed if typed `references` and not `derived-from`. The host must distinguish the two edge types.

**Replay.** A historical query by `record_time` or `valid_time` returns the revision that was current then, including later-retracted ones, marked as such. Corrections are new revisions (`supersedes` / `retracts`). In-place mutation of a revision is forbidden.

---

## 8. Confidence

Adopt 026’s separation: measurement uncertainty ≠ confidence-about-the-assertion ≠ conformance verdict ≠ risk.

Rules:

- No default 0.95.  
- No bare number: `confidence_value` requires `scale_ref` + `scale_version` + `method_ref` + `purpose` + `assessor_id` + `calibration_status` ∈ {calibrated, uncalibrated, unknown}.  
- Uncalibrated values MUST NOT be consumed as probabilities.  
- No cross-scheme numeric averaging.  
- Qualitative ordinal grades must be marked ordinal.  
- A ConfidenceAssessment is a new object; revising it does not mutate the ProvenanceRecord it assesses. The record may point at `current_assessment_id`.

What the reference can validate: required fields present, scale registered in the *local* scale table of the trusted host, calibration_status not silently upgraded. What it cannot validate: that the assessor’s number is calibrated in the world.

---

## 9. Agents, authorization, disclosure

Roles on a record, all referenced outward:

| Role | Meaning |
|---|---|
| `source_author` | Who wrote the external artifact (declared, often unverified) |
| `observer` | Who performed CaptureActivity |
| `synthesizer` | Software or human who produced an inference |
| `recorder` | Who wrote the EAP revision |
| `assessor` | Who issued ConfidenceAssessment |
| `authorizer` | Who is *recorded* as permitting the write |

Recorded authorization is not authentication. The trusted-host reference may check that `recorder_id` is in a local allow-list; it cannot prove the person was that agent. Change-permission is an access decision recorded as evidence (012 neighbor: provenance is not the policy engine).

**Disclosure without leaking hidden evidence.** Views are audience-scoped. A redacted EvidenceLink retains placeholder, reason code, redacting party, and that a hidden item exists. Consumers without the evidence body must still see `support-present-but-withheld` rather than an empty support set that looks like “no evidence.” 028 requires self-reported, single-source, and unresolved-conflict flags to surface with the claim, not only inside the support record.

---

## 10. Whole-object facets

For each exported type:

| Facet | ProvenanceRecord | EvidenceLink | ConfidenceAssessment | CaptureActivity |
|---|---|---|---|---|
| Identity-class | record_id + revision_id | link_id + revision_id | assessment_id + revision_id | capture_id |
| Direct-properties | account_kind, basis, times, target pin | polarity, independence, selector, state | value, scale, method, calibration, purpose | digest, instrument, acquisition_kind |
| Recognition-observation | how the pin was matched (anchor-match-rule) | excerpt fidelity / drift status | scale recognition only | byte digest match |
| Capabilities/actions | issue, supersede, retract, flag-review | assert, withdraw, re-appraise | issue, supersede | create; never “verify-live-system” |
| Context/evidence | links + current assessment | capture or unavailable reason | evidence-basis-summary (026) | cached copy locator |

**Not-applicable / delegated.** People registries, rights terms, IAM policy, PKI keys, unit systems, claim vocabularies, connector protocols: delegated. Fitness-for-use and quality-measure registers: delegated to 026. Source catalogue bibliographic fields: delegated. Forensic case files and court procedure: out of scope (028 hold).

---

## 11. Closed field table (minimum)

Cardinalities for a bounded trusted-host schema. Additional fields may exist as opaque extensions; they must not be required to satisfy invariants.

**AssertionPin**

| Field | Card. | Notes |
|---|---|---|
| pin_id | 1 | |
| target_id | 1 | external |
| target_version | 0..1 | |
| target_digest | 0..1 | required unless digest_absent_reason |
| digest_absent_reason | 0..1 | |
| media_type | 0..1 | |
| schema_version | 1 | |

**CaptureActivity**

| Field | Card. | Notes |
|---|---|---|
| capture_id | 1 | |
| acquisition_kind | 1 | closed: observed-bytes |
| capture_digest | 0..1 | |
| cached_copy_ref | 0..1 | |
| observer_id | 1 | |
| capture_time / record_time | 1 / 1 | |
| selector / source_state | 0..n / 0..1 | OA pattern |

**ProvenanceRecord**

| Field | Card. | Notes |
|---|---|---|
| record_id / revision_id | 1 / 1 | |
| pin_id | 1 | |
| account_kind | 1 | observed-account \| source-asserted-account \| inference \| proposal \| unverified |
| account_basis | 1 | first-hand \| reconstructed \| inferred \| asserted-without-evidence |
| derived_from | 0..n | pin or capture; type required |
| agent_roles | 1..n | |
| event/valid/capture/record times | as applicable | record_time required |
| supersedes / retracts | 0..1 / 0..1 | |
| current_assessment_id | 0..1 | |
| evidence_link_ids | 0..n | |
| lifecycle | 1 | proposed \| issued \| superseded \| retracted \| review-required |

**EvidenceLink**

| Field | Card. | Notes |
|---|---|---|
| link_id / revision_id | 1 / 1 | |
| subject_ref | 1 | pin or record |
| capture_or_source_ref | 0..1 | required unless unavailable |
| polarity | 1 | supports \| counters \| contextualizes |
| independence | 1 | |
| warrant_ref / assumptions | 0..1 / 0..n | |
| excerpt + fidelity | 0..1 + 1 if excerpt | |
| withdrawn | 1 | boolean; withdrawal is a revision |

**ConfidenceAssessment**

| Field | Card. | Notes |
|---|---|---|
| assessment_id / revision_id | 1 / 1 | |
| about_ref | 1 | pin or record |
| value + value_kind | 1 / 1 | ordinal \| qualitative \| probability \| interval |
| scale_ref + scale_version | 1 / 1 | |
| method_ref | 1 | |
| purpose | 1 | |
| assessor_id | 1 | |
| calibration_status | 1 | |
| assessment_time / record_time | 1 / 1 | |

---

## 12. Lifecycle: actor / guard / effect

| Action | Actor | Guard | Effect |
|---|---|---|---|
| capture | observer | digest algorithm declared; times well-formed | new CaptureActivity; no claim created |
| pin | recorder | target_id present; digest or reason | new AssertionPin |
| issue record | recorder | pin exists; account_kind set; inference must cite inputs | new issued ProvenanceRecord |
| add support | recorder | capture or unavailable reason; polarity set; citation-only rejected | new EvidenceLink |
| assess | assessor | scale+method+calibration present; no bare number | new ConfidenceAssessment |
| correct | recorder | prior revision exists; new revision_id; supersedes set; old bytes unchanged | history preserved |
| retract record | recorder + recorded authorizer | reason required | lifecycle=retracted; dependents flagged review-required |
| withdraw support | recorder | reason required | link withdrawn; dependents flagged; conclusion not auto-negated |
| disclose | view engine | audience view defined | withheld items placeholdered |
| deny access | view engine | no matching view | empty result, not a rewritten history |
| import | importer | idempotent on (record_id, revision_id, schema_version, body digest) | insert-or-ignore; conflict on same id different digest is reject |
| migrate | operator | semantic losslessness check | refuse if kinds, pins, or revision graph would collapse |

Mastership: the trusted host is master of *its* records and revisions. It is not master of external targets, source authors, or live systems. Rights to read evidence bodies are not rights to mutate history.

---

## 13. Eight invariants (enforceable on the trusted host)

1. **Identity separation.** The six identity classes in §4.1 are pairwise distinct symbols; a digest never replaces `record_id` or `target_id`.  
2. **Immutable revision.** A stored revision body is byte-immutable. Correction = new revision.  
3. **Kind non-collapse.** `observed-acquisition` on a capture cannot be copied onto an inference record as `observed-account` of live-system truth.  
4. **Citation is not support.** An EvidenceLink without polarity and without (capture or unavailable reason) is invalid.  
5. **Shared-origin collapse.** Two links whose captures share `capture_digest` or whose pins share `target_digest` cannot both be `independence=independent`.  
6. **Confidence completeness.** A published assessment has scale, method, purpose, assessor, and calibration_status; uncalibrated ≠ probability.  
7. **Retraction non-erasure.** Retracted/superseded revisions remain queryable in historical mode; current-root queries omit them.  
8. **Derivation acyclicity.** `derived-from` edges form a DAG; `references` edges may cycle. Mixing the types to hide a derivation cycle is invalid.

Machine-enforceable: 1–8 on local data. Not enforceable: external truth, real authentication, unread source content, calibration in the world.

---

## 14. Fifteen question → finding → artifact → allowed-action routes

1. **Q:** Did we observe file F? **F:** CaptureActivity exists with digest H. **A:** C1. **Act:** cite C1 as observed-bytes; do not assert F’s sentences.  
2. **Q:** What does source S claim about system X? **F:** excerpt bound to C1. **A:** EvidenceLink L1 polarity=contextualizes or source-asserted account. **Act:** display as source-asserted.  
3. **Q:** What did the model conclude? **F:** account_kind=inference, inputs C1…Cn, model id. **A:** ProvenanceRecord R1. **Act:** display as inference; forbid “verified live.”  
4. **Q:** Is R1 independently corroborated? **F:** all links share digest H. **A:** independence rewritten to same-origin. **Act:** refuse independent-corroboration badge.  
5. **Q:** What is current confidence in R1? **F:** latest issued assessment A1, scale S, uncalibrated. **A:** A1. **Act:** show grade + “uncalibrated”; forbid treating as p=0.95.  
6. **Q:** Source disappeared. **F:** fetch failed. **A:** L1 revision with source_state=unavailable; cache retained. **Act:** keep cache; mark anchor-drift.  
7. **Q:** Source issued a correction. **F:** new capture C2 of correction notice. **A:** L2 counters or contextualizes; R1 flagged review-required. **Act:** do not mutate R1 body.  
8. **Q:** Target artifact moved to a new digest. **F:** new pin P2. **A:** P2; R1 still pins P1. **Act:** optional new record on P2; no silent retarget.  
9. **Q:** Analyst retracts support L1. **F:** withdrawal revision. **A:** L1 withdrawn; R1 review-required. **Act:** review; do not auto-assert ¬claim.  
10. **Q:** Replay Tuesday’s current root. **F:** revisions with record_time ≤ Tuesday. **A:** historical root. **Act:** return then-current, including items later retracted, marked.  
11. **Q:** Import the same revision twice. **F:** same (id, rev, schema, body digest). **A:** none new. **Act:** idempotent accept.  
12. **Q:** Import same id, different body. **F:** digest mismatch. **A:** reject record. **Act:** deny; do not merge.  
13. **Q:** User without evidence clearance asks “why?” **F:** view hides bodies. **A:** placeholders + support-present-but-withheld. **Act:** deny bodies; do not present “unsupported.”  
14. **Q:** Exact derivation of summary T from memo M. **F:** derived-from edge + quotation kind + shared digest lineage. **A:** R2 derived-from P1. **Act:** allow; independence=derived-copy.  
15. **Q:** Migrate v0 records that stored a bare 0.95 and collapsed AI output into observed. **F:** semantics would be lost. **A:** migration-refusal ticket. **Act:** refuse automated migration.  
16. **Q:** Is this a live-system verification? **F:** no CaptureActivity against the live system; only a local document. **A:** none that could justify the claim. **Act:** deny the verification action.  
17. **Q:** Who may correct R1? **F:** recorded authorizer allow-list. **A:** access decision evidence. **Act:** allow new revision or deny write; history remains.

---

## 15. Negative cases (ten distinct, plus positives)

**Positives (synthetic).** (P1) Observer captures a PDF, digest stored, pin created, source-asserted excerpt linked. (P2) Human assessor issues an ordinal confidence on a named scale with method and `uncalibrated`. (P3) Correction issues revision R1.2 superseding R1.1; both readable. (P4) Idempotent re-import of R1.2. (P5) Historical query returns R1.1 as then-current.

**Negatives.**

1. AI analysis of a local runbook presented as live-system verification.  
2. Schema-valid record treated as proof of external truth.  
3. Two byte-identical copies counted as independent corroboration.  
4. Derived executive summary counted as a second source.  
5. Citation-only row treated as support.  
6. Support withdrawal silently rewriting the conclusion to false.  
7. In-place edit of an issued revision.  
8. Bare confidence 0.95 with no scale/method.  
9. Averaging ordinal grades from two scales into one number.  
10. Passing digest check advertised as “the memo is true.”  
11. PUT-overwrite of annotation-style storage destroying prior claim text.  
12. Access denial returning a forged “no evidence” view.  
13. Cycle in `derived-from` hidden as mutual citations.  
14. Migration that drops `account_kind` or flattens pins into filenames.  
15. Recorded `authorizer` treated as proof of authentication.

---

## 16. Three synthetic profiles (not named companies)

**Minimum startup.** One laptop, no enterprise IAM/PKI. A single recorder is also observer. Allowed: CaptureActivity, AssertionPin, one ProvenanceRecord, optional EvidenceLink to the same capture, optional qualitative confidence with `uncalibrated`. Forbidden: “verified against production,” independent-corroboration badges, numeric probabilities.

**Scaled group with conflicting claims.** Two departments issue source-asserted records about the same `target_id` with different digests (two memo versions). Both records remain. Disagreement is first-class (026: last-writer-wins prohibited). A later inference that picks a winner must cite both pins and declare method; it does not delete the loser.

**AI team with model output and human review.** Pipeline: captures of prompts and retrieved docs (observed-bytes) → model run (inference record, synthesizer = software agent + model version) → human review (new ConfidenceAssessment and/or new record with account_kind remaining inference unless the human performed a *new* observed acquisition of the live system). Human agreement does not change kind from inference to observed.

---

## 17. Crosswalk (semantic only)

| EAP concept | 012 | 026 | 028 | PROV | OA | DQV | OL / SLSA / in-toto | Nanopub |
|---|---|---|---|---|---|---|---|---|
| ProvenanceRecord | ALIGN account/basis/times/fixity | REFERENCE current assessment | REFERENCE links | entity + bundle | — | — | run/job as activity projection | pubinfo + prov graph |
| EvidenceLink | REFERENCE only | — | ALIGN polarity/selector | not modelled as support | ALIGN selector/state; REJECT motivation-as-support | — | materials/inputs ≠ support | — |
| ConfidenceAssessment | thin slot only | ALIGN shape | certainty-scheme pointer | — | assessing motivation ≠ confidence | QualityMeasurement is cousin, not parent | quality facets are job observations | — |
| CaptureActivity | origination activity | — | acquisition | activity + generation of cached bytes | TimeState + cached | — | run producing a dataset copy | — |
| AssertionPin | subject-ref / descriptor | subject-reference | supported-subject-ref | entity id | target source | computedOn | dataset+version / subject digest | assertion graph *pointer*, not content |
| Claim text | out | out | out (explicit) | out | body is not EAP claim store | out | out | assertion graph is *their* store; EAP does not adopt it as host content |

No row is a subtype assertion. No executable import.

---

## 18. Recommended minimum implementation (trusted-host reference)

Implementable without enterprise systems:

- Append-only store keyed by `(type, record_id, revision_id)`.  
- Local tables for closed codes, local confidence scales, and an agent allow-list.  
- Digest function with declared canonicalization.  
- Historical and current-root queries.  
- View filter that placeholders withheld evidence.  
- Import idempotence and same-id-different-digest rejection.  
- Invariant checks 1–8.  
- A single synthetic fixture pack covering the routes in §14.

Do **not** implement: live source connectors, PKI validation beyond recording a signature envelope reference, probabilistic engines, people directories, or any API labelled “verified.”

If a subset cannot be implemented without extra objects: support withdrawal that flags dependents needs a `review-required` flag on ProvenanceRecord (already in the table). Shared-origin collapse needs capture/target digests (already required). No further independent objects are required for the minimum. Adding a live-verifier object would exceed the contour and recreate the critical negative case.

---

## 19. Remaining holds

All holds on 012, 026, and 028 remain. Additional holds of this contour:

- Unread ISO/JCGM/SACM/PREMIS texts stay uncited.  
- Sector profiles (legal, clinical, engineering, media, archival) are untested; GRADE or FRE language must not travel as defaults (028 hold, restated).  
- DQV remains a Working Group Note.  
- Nanopub retraction vocabulary was not specified on the guidelines page that was read.  
- Brief parent digests ≠ published `publication.json` digests; do not treat either set as this companion’s identity.  
- No conformance to PROV, SLSA, OpenLineage, OA, or DQV is claimed. Alignments only.

---

## 20. Disagreements with the hypothesis, and strongest failure modes

**Disagreements.**  
(1) “Associated with WM-XCT-012” must not mean subtype, profile, or shared machine identity.  
(2) 012’s existing confidence/attestation slots are too coarse to *be* ConfidenceAssessment; 026 already separated that object.  
(3) 028 is the right pattern source for EvidenceLink, but EAP must not become a second evidence mixin.  
(4) A new universal WM row minted only to keep a registry count honest would itself be a false identity.  
(5) “Executable pure reference” can enforce invariants on local records; it cannot be an authenticated production service and must not be labelled as one.

**Strongest failure modes.**  
The first is the brief’s own: an AI reading of a captured local document, schema-valid under EAP, presented as live-system verification. The second is integrity theatre: a green digest or SLSA-style builder attestation used as a truth badge for sentences. The third is corroboration inflation from copies and summaries. The fourth is silent rewrite on retraction. The fifth is migration that drops kind, pin, or revision distinctions and then claims continuity.

No design, including this one, can prove external truth by schema validation. The contract’s job is to keep observed acquisition, source assertion, inference, proposal, and unverified information from collapsing into each other, and to keep corrections from erasing what was previously known.
