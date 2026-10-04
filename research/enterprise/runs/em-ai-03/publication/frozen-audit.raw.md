# Frozen semantic audit — EM-AI-03

## Verdict

**Decision preserved; artifact set not freezable as written.**

The intended disposition survives the evidence and is confirmed: reuse WM-AI-003 for one bounded evaluation occurrence carrying distinct applied-plan, run and result roles; reuse WM-AI-009 for the benchmark contract; reuse WM-AI-008 for the dated safety judgement; reuse WM-AI-010 as incident-report feedback and trigger evidence only; profile Deployment Decision across WM-KNW-010 / WM-ACT-024 / WM-REC-010; keep Reusable Evaluation Protocol and Standing Deployment Authorization Instrument identifier-unassigned with no present independent identity; allocate no catalogue, model or runtime identifier. Nothing in the three studies disproves this, and Grok's stronger claim that neither candidate *needs* independent identity is unsupported — it argues present absence, not permanent absence.

The artifacts, however, contain contradictions that would freeze semantics the studies explicitly reject: the profile revokes records it elsewhere declares immutable, asserts mastership through relations its own holds call unapproved, declares its constraint set exhaustive while omitting four binding invariants, carries no rights or time semantics, uses unmastered referents as pinned keys, and ships fixtures that are not deterministically decidable. Both candidate files contain one mastership leak and assert governance authorities that do not exist in frozen form.

## Material defects

**1. "Invalidates" contradicts immutability and non-extension; the transfer path is deleted.**
Profile constraint 6 and invariant 11 make a dataset, scorer, configuration, environment, context, intended-use or population change *invalidate* the prior evaluation, assessment and authorization. The local synthesis holds E1 immutable and D1 merely non-extending to C2; Grok retains the old score "only as historical measurement"; the DA candidate allows "scope proof … or explicit non-applicability". As written, a change of context would retroactively revoke an authorization that remains validly in force for its own unchanged context, and invariant 9's absolute non-transfer contradicts local invariant 12 and Claude's "re-run or explicitly justified as transferable".

*Remediation (exact):* replace profile constraint 6 with "Dataset, scorer, configuration, environment, context, intended-use or population change ends the transferability of prior evidence and removes prior authorization from effect for the changed scope only; prior evaluation, assessment and issued records remain immutable and remain valid within their own pinned scope." Replace invariant 9 with "Scores do not transfer across dataset, configuration, context, intended use or population except under a dated, authorized transfer justification that names the delta and its construct impact." Replace invariant 11 with "A change in context, intended use or population places the changed scope outside prior authorization; silent carry-forward is rejected and the unchanged scope is unaffected." Append invariant 23: "Prior records remain immutable and valid within their pinned scope; change removes transferability, not validity."

**2. Dataset-snapshot mastership is asserted through an unapproved relation, and the three-level split is collapsed.**
Profile constraint 2 and the EP candidate assign the evaluated snapshot to WM-DAT-001. Both studies record that WM-AI-009's WM-DAT-001 edge is unapproved, so the constraint rests on an unenforced relation. Claude distinguishes three levels — benchmark release, benchmark dataset snapshot (item set, digests, sampling, hidden-test controls), source dataset master — and Grok collapses the middle level into WM-DAT-001. Under the collapsed reading, hidden-test controls and item digests have no master at all.

*Remediation (exact):* replace profile constraint 2 with "WM-AI-009 owns the benchmark contract and the benchmark dataset snapshot definition, including item set composition, item digests, sampling and hidden-test controls; WM-DAT-001 owns the source dataset master; WM-AI-003 pins release, snapshot digest, split designation and contamination-check result. Replacing the snapshot creates a new evaluation occurrence." Add hold: "WM-AI-009→WM-DAT-001 relation is unapproved; snapshot-versus-source mastership is a publication blocker."

**3. The WM-AI-003 role split is asserted, not specified; invariant 2 and the `role-ordering` fixture are undecidable.**
Grok blocks acceptance "until the role split inside WM-AI-003 is explicit". The profile names three roles but supplies no within-occurrence keys, no per-role time and authorship, no run-completion state and no run cardinality. The studies disagree in kind — Claude says "three distinct records", Grok says "roles … not separate masters and not a fused attribute bag". Whether a harness-failure retry is a second run inside the occurrence or a new occurrence is unstated, and the local synthesis separately records evaluation-instance master identity as a gap. The `role-ordering` fixture pins three timestamps but no run state or authorship, so it cannot be decided.

*Remediation (exact):* add profile constraint "Within one WM-AI-003 occurrence, applied plan, run and result are append-only sub-records keyed by (occurrenceRef, role, sequence), each carrying its own recordedAt, actor and state; the plan is sealed at planSealedAt before any run begins; a run carries state in {started, completed, failed, aborted}; a result exists only for a run in state completed; a retry with byte-identical pins is a new run sequence inside the same occurrence; any pin delta requires a new occurrence." Amend fixture `role-ordering` pins with `"planSealedAt": "2026-01-01T00:00:00+00:00"`, `"runState": "completed"`, `"runSequence": 1`, `"planActor": "A"`, `"runActor": "B"`, `"resultActor": "C"`, and add `"expectedCode": "ROLE_ORDER_VALID"`. Add hold: "evaluation-occurrence master identity remains a gap; occurrenceRef is a declared descriptor, not an allocated identifier."

**4. Additive correction and rescoring are dropped; scorer change has two contradictory destinations.**
The local synthesis requires rescoring to create an additive successor preserving the original score, scorer version, actor and reason; Claude agrees. Grok makes any scorer delta a new occurrence, and profile constraint 6 adopts that. The profile invariant set contains no additive-correction rule at all (invariant 8 covers only decision rationale), so a rescore can be read as a permitted in-place update or as a mandatory new occurrence.

*Remediation (exact):* append invariant 20: "Corrections and rescoring are additive; the original value, scorer version, actor, time and reason are preserved and never overwritten." Add profile constraint "Rescoring the same sealed plan, run and pinned inputs with a changed scorer version produces an additive successor result inside the same occurrence, citing the superseded result; a change to any other pin requires a new occurrence."

**5. Threshold pre-registration and post-hoc disclosure are absent from the profile.**
Both studies and local invariant 4 require thresholds registered before results are observed and an authorized change record disclosing prior result visibility. The profile carries ordering of plan/run/result but no threshold rule, so a post-hoc threshold move is unconstrained.

*Remediation (exact):* append invariant 21: "Thresholds and the applied plan are registered before any result is observed; a later change requires an authorized, dated change record disclosing prior result visibility and does not amend the original result."

**6. `constraintsAreNonExhaustive: false` is asserted while four binding invariants are missing.**
The profile declares its constraint set complete but omits local invariants 7 (absence of metric is not absence of risk), 8 (split labels do not prove non-contamination) and 9 (evidence is revision-bound and goes stale by rule), and omits the time-instant distinctions that all three studies require. Declared exhaustiveness makes these omissions binding gaps rather than deferrals.

*Remediation (exact):* append invariant 16 "Split labels never prove non-contamination; non-overlap requires declared contamination evidence."; invariant 17 "Absence of a metric is not absence of risk."; invariant 18 "Evidence is revision-bound and becomes stale by a declared rule; stale evidence is marked stale and is not silently carried."; invariant 19 "Event, observation, ingestion, approval, publication and effective times are distinct RFC 3339 instants with explicit offset." Keep `constraintsAreNonExhaustive: false` only after these additions are applied.

**7. Rights, confidentiality and personal-data semantics are absent from the profile.**
Only the EP candidate mentions protected items. The profile requires population and disaggregation pins and incident evidence citation without any rule on dataset or benchmark licence and redistribution, hidden-test item disclosure, confidential incident content, or minimum subgroup size for disaggregated reporting — while admitting it is not publication-ready.

*Remediation (exact):* append invariant 22: "Benchmark and dataset rights, licence and redistribution terms are declared before use; protected benchmark items, hidden-test content, confidential incident content and personal data are excluded from published artifacts; disaggregated results are reported only at or above a declared minimum subgroup size." Add matching profile constraint and hold "rights and confidentiality clearance for benchmark items, dataset snapshots and incident content is unresolved and is a publication blocker."

**8. Unmastered referents are used as pinned, change-detectable keys.**
Deployment context has no frozen master (both study holds), the incident occurrence has no master (only the report does), and the evaluation occurrence has no master identity. Yet profile constraints make context, intended use and population pinned keys whose change drives invalidation, and the fixtures pin `"contextBefore": "internal-assist"`, `"incident": "I1"`, `"observation": "O1"`, `"D1@1"` as if they resolved. Nothing declares these labels fixture-local, which is an identity-leak surface.

*Remediation (exact):* append invariant 24: "Deployment context, intended use, population, incident occurrence and evaluation occurrence are declared descriptors with no allocated identifier; they are never used as resolvable identifiers." Add to every fixture file `"labelScope": "fixture-local synthetic labels; not registry, model, catalogue or runtime identifiers"`. Add hold "no frozen deployment/endpoint or incident-occurrence master exists; context and incident pins are descriptors pending a master."

**9. Known blocking overlaps and unapproved-relation holds are missing from the profile's holds, and the gate-versus-authorization rule is unarbitrated.**
All three inputs record the WM-AI-003 / WM-AI-009 protocol-and-metric ownership overlap and the three-way decision overlap (WM-AI-003 approval/waiver, WM-AI-008 acceptance, the triad). The profile addresses neither in its constraints and records neither in its holds, and it never mentions the waiver whose expiry it inherits as a reassessment trigger. Claude additionally records WM-AI-010's edges and WM-AI-003's incident/risk siblings as unapproved or unregistered, while profile constraint 8 routes incident evidence mastership through exactly those edges.

*Remediation (exact):* add profile constraint "WM-AI-009 owns metric definitions and the benchmark-level protocol contract; WM-AI-003 owns only the applied protocol instance and may narrow but never redefine the contract or a metric definition." Add profile constraint "A WM-AI-003 gate decision, approval or waiver governs evaluation acceptance only; deployment authorization arises solely from WM-KNW-010 rationale, WM-ACT-024 act and WM-REC-010 instrument; waiver expiry is a reassessment trigger and never extends authorization." Append invariant 25: "A WM-AI-003 gate approval or waiver is not a deployment authorization." Add holds: "WM-AI-003/WM-AI-009 protocol and metric overlap is arbitrated by constraint but the base drafts are unreconciled."; "WM-AI-010 relations and WM-AI-003 incident/risk siblings are unapproved or unregistered; constraint 8's mastership routing is unenforced."

**10. The EP candidate boundary claims a contract that WM-AI-009 masters.**
`boundary.owns` includes "required task, metric, scorer and threshold contract" — the exact content the profile assigns to WM-AI-009 — while `boundary.excludes` omits metric definition ownership. Even unassigned, this records a mastership leak and pre-empts defect 9's arbitration.

*Remediation (exact):* in the EP candidate replace that `owns` entry with "protocol-level selection and binding of externally mastered task, metric, scorer and threshold definitions", and append to `excludes`: "metric definition mastership", "benchmark task contract mastership", "threshold definition mastership".

**11. `decision: "NO NEW MODEL"` contradicts the recorded conditionality.**
Both candidates pair a terminal "NO NEW MODEL" with `conditionsUnmet`, `allocationState: "unassigned"` and a conditional framing that the local synthesis and Claude require. Grok's "neither conditional candidate needs independent identity" is the permanent reading and is not supported by the evidence, which shows only present absence.

*Remediation (exact):* in both candidates keep `"decision": "NO NEW MODEL"` and add `"decisionScope": "this checkpoint only"`, `"conditional": true`, and `"reopenCondition": "evidence of a lifecycle, approval and mastership independent of one evaluation occurrence or one issued decision record"`. Add hold "Grok's claim that this candidate can never require independent identity is rejected; absence is present-tense."

**12. Candidate mastership asserts authorities that exist in no frozen model.**
EP names "AI evaluation-method governance authority" and DA names "competent deployment-authorization authority" as mastership, while the holds concede the frozen deployment/endpoint authority is a gap. This is unsafe inference presented as settled mastership.

*Remediation (exact):* in both candidates set `"mastership": null` and add `"mastershipHold": "no frozen governance master exists for this candidate; mastership is unresolved and may not be inferred."`

**13. Candidate objects cannot express their own invariants.**
EP `boundary.owns` claims "approval lineage" but `EvaluationProtocolRevision` has no approval field. DA claims "issuing authority and competence evidence" and an invariant that revocation records actor, authority, time and reason, yet the object has only `authorityRef` and no revocation fields; `DeploymentAuthorizationInstrument` has no `currentRevisionRef` (EP has one) and no rule naming the authoritative revision; `AuthorizationRevision` carries no status.

*Remediation (exact):* add to `EvaluationProtocolRevision.required`: `"approvalRef"`, `"approvedAt"`, `"approvedBy"`. Add to `DeploymentAuthorizationInstrument.required`: `"currentRevisionRef"`. Add to its `optional`: `"revokedBy"`, `"revokedAt"`, `"revocationReason"`, `"revocationAuthorityRef"`, and append invariant "Exactly one revision is authoritative at any instant; superseded revisions remain resolvable." Add to `AuthorizationRevision.required`: `"status"`. Add to the same candidate an invariant "Revocation is recorded only with actor, authority, time and reason present."

**14. Both allocation fixture files are nondeterministic, miscite invariants and are undifferentiated.**
The two files are byte-identical but for `candidateName`, so neither tests its own candidate. `unassigned-candidate-not-referenceable` cites invariant 1 in each file, but neither candidate has an invariant forbidding reference to an unassigned candidate, and `expectedCode: "UNASSIGNED_CANDIDATE_REFERENCE"` maps to no rule. `future-independent-lifecycle` is labelled `positive` while expecting a hold, pins nothing, describes an unspecified "future proposal", cites DA invariant 2 (authority naming) which is irrelevant, and carries no `expectedCode` — it is not decidable.

*Remediation (exact):* append to both candidates' invariants: "An unassigned candidate is not referenceable as an identified model and no identifier may be allocated, inferred or guessed." Re-cite `unassigned-candidate-not-referenceable` to that invariant's number in each file. Replace `future-independent-lifecycle` with the deterministic cases supplied below, and add the candidate-specific negative cases supplied below.

**15. Stale holds, and invariant 14 collides with the profile's own unversioned base pins.**
All three artifacts hold "Independent Grok review complete; frozen semantic audit pending"; this audit runs once and that string must not freeze as pending. Separately, invariant 14 ("Missing or unversioned pins block result acceptance") is scope-ambiguous against `basePins` where every `version` and `digest` is null with `verification: "unverified-current-draft"` — read broadly, the profile blocks itself with no distinct code.

*Remediation (exact):* in all three artifacts replace that hold with "Frozen semantic audit complete; material defects recorded and remediation pending; no further provider run is required or permitted." Replace invariant 14 with "Missing or unversioned result pins block acceptance of that result." Add profile hold "basePins carry null version and digest; unversioned base pins block profile publication under code BASE_PIN_UNVERSIONED and are distinct from result-pin acceptance."

## Exact additional fixtures

Invariant numbers below refer to the amended profile invariant list (existing 1–15 plus appended 16–25) and, for allocation cases, to each candidate's invariant list after defect 14's append.

```json
[
  {
    "appliesTo": "profile-fixtures.json",
    "id": "prior-records-remain-valid-in-scope",
    "kind": "positive",
    "invariants": [23, 11],
    "pins": {
      "datasetBefore": "D1@1",
      "datasetAfter": "D1@2",
      "contextBefore": "internal-assist",
      "contextAfter": "external-customer-action",
      "priorAuthorizationScope": "internal-assist",
      "labelScope": "fixture-local synthetic labels; not registry, model, catalogue or runtime identifiers"
    },
    "input": "After the dataset snapshot and context change, the prior evaluation, assessment and issued instrument are inspected for their original scope.",
    "expect": "Accepted; prior records remain immutable and remain in force for internal-assist, and are non-transferable to external-customer-action.",
    "expectedCode": "PRIOR_RECORD_SCOPE_PRESERVED"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "context-change-revokes-unchanged-scope",
    "kind": "negative",
    "invariants": [11, 23],
    "pins": {
      "contextAdded": "external-customer-action",
      "priorAuthorizationScope": "internal-assist",
      "priorAuthorizationStatus": "effective"
    },
    "input": "The arrival of a new deployment context is used to set the prior authorization for the unchanged context to invalid.",
    "expect": "Rejected; change removes transferability to the new scope and never revokes the unchanged scope.",
    "expectedCode": "SCOPE_REVOCATION_OVERREACH"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "silent-authorization-carry-forward",
    "kind": "negative",
    "invariants": [11, 6],
    "pins": {
      "instrumentScope": "internal-assist",
      "requestedContext": "external-customer-action",
      "scopeProofRef": null
    },
    "input": "The issued instrument is applied to the new context with no scope proof and no successor instrument.",
    "expect": "Rejected; a new rationale, authorized act and issued instrument are required.",
    "expectedCode": "AUTHORIZATION_SCOPE_NOT_PROVEN"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "rescore-additive-successor",
    "kind": "positive",
    "invariants": [20, 2],
    "pins": {
      "occurrenceRef": "E1",
      "planSealedAt": "2026-01-01T00:00:00+00:00",
      "runSequence": 1,
      "runState": "completed",
      "scorerBefore": "S@1",
      "scorerAfter": "S@2",
      "originalResultRetained": true
    },
    "input": "The same sealed plan, run and pins are rescored with a later scorer version.",
    "expect": "Accepted as an additive successor result citing the superseded result, with original value, scorer version, actor, time and reason preserved.",
    "expectedCode": "RESCORE_ADDITIVE_SUCCESSOR"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "rescore-overwrites-original",
    "kind": "negative",
    "invariants": [20],
    "pins": {
      "occurrenceRef": "E1",
      "scorerBefore": "S@1",
      "scorerAfter": "S@2",
      "originalResultRetained": false
    },
    "input": "A rescore replaces the stored original score in place.",
    "expect": "Rejected; corrections are additive and the original is never overwritten.",
    "expectedCode": "RESULT_IMMUTABILITY"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "post-hoc-threshold-change",
    "kind": "negative",
    "invariants": [21, 4],
    "pins": {
      "planSealedAt": "2026-01-01T00:00:00+00:00",
      "resultAt": "2026-01-02T01:00:00+00:00",
      "thresholdChangedAt": "2026-01-03T00:00:00+00:00",
      "changeRecordRef": null,
      "priorResultVisibilityDisclosed": false
    },
    "input": "A pass threshold is lowered after the result is observed, with no authorized change record.",
    "expect": "Rejected; thresholds precede results and a later change requires an authorized dated record disclosing prior result visibility.",
    "expectedCode": "THRESHOLD_PRECEDENCE_VIOLATION"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "run-retry-within-occurrence",
    "kind": "positive",
    "invariants": [1, 2],
    "pins": {
      "occurrenceRef": "E1",
      "runSequence": 2,
      "runState": "completed",
      "priorRunState": "failed",
      "pinDelta": "none",
      "planMutated": false
    },
    "input": "A harness failure is retried with byte-identical pins against the sealed plan.",
    "expect": "Accepted as a second run sequence inside the same occurrence with the plan unchanged.",
    "expectedCode": "RUN_RETRY_WITHIN_OCCURRENCE"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "run-retry-with-pin-delta",
    "kind": "negative",
    "invariants": [2, 4],
    "pins": {
      "occurrenceRef": "E1",
      "runSequence": 2,
      "pinDelta": "inferenceConfiguration",
      "planMutated": false
    },
    "input": "A retry changes the inference configuration inside the existing occurrence.",
    "expect": "Rejected; a pin delta requires a new occurrence with a newly sealed plan.",
    "expectedCode": "NEW_OCCURRENCE_REQUIRED"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "split-label-as-contamination-proof",
    "kind": "negative",
    "invariants": [16],
    "pins": {
      "splitLabel": "test",
      "overlapEvidence": null,
      "canaryCheck": null,
      "holdoutExposureCount": null
    },
    "input": "A split label is offered as proof of non-contamination.",
    "expect": "Rejected; non-overlap requires declared contamination evidence.",
    "expectedCode": "CONTAMINATION_UNPROVEN"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "absent-metric-as-absent-risk",
    "kind": "negative",
    "invariants": [17],
    "pins": {
      "harmCategory": "declared-in-scope",
      "metricRef": null
    },
    "input": "A harm category with no metric is reported as carrying no residual risk.",
    "expect": "Rejected; absence of a metric is not absence of risk and must be recorded as an unmeasured limitation.",
    "expectedCode": "METRIC_ABSENCE_NOT_RISK_ABSENCE"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "stale-evidence-carried",
    "kind": "negative",
    "invariants": [18],
    "pins": {
      "resultAsOf": "2026-01-02T01:00:00+00:00",
      "declaredStalenessInterval": "P90D",
      "assessmentAt": "2026-06-01T00:00:00+00:00",
      "staleMarked": false
    },
    "input": "An assessment cites a result beyond its declared staleness interval without marking it stale.",
    "expect": "Rejected; stale evidence is marked stale and is not silently carried.",
    "expectedCode": "EVIDENCE_STALE"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "conflated-time-instants",
    "kind": "negative",
    "invariants": [19],
    "pins": {
      "observedAt": "2026-01-02T01:00:00+00:00",
      "ingestedAt": "2026-01-02T01:00:00+00:00",
      "effectiveAt": null,
      "offsetDeclared": true,
      "singleTimestampSubmitted": true
    },
    "input": "A result submits one timestamp for observation, ingestion and effect.",
    "expect": "Rejected; event, observation, ingestion, approval, publication and effective instants are recorded distinctly.",
    "expectedCode": "TIME_SEMANTICS_UNDERSPECIFIED"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "hidden-test-item-disclosure",
    "kind": "negative",
    "invariants": [22],
    "pins": {
      "itemClass": "hidden-test",
      "publishedContent": "item-text-and-expected-output"
    },
    "input": "Hidden-test item content is embedded in a published profile artifact.",
    "expect": "Rejected; protected benchmark items stay outside published artifacts and are cited by digest reference only.",
    "expectedCode": "PROTECTED_ITEM_DISCLOSURE"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "dataset-rights-undeclared",
    "kind": "negative",
    "invariants": [22],
    "pins": {
      "datasetSnapshot": "D1@2",
      "licenceRef": null,
      "redistributionTerms": null
    },
    "input": "A dataset snapshot is bound to an evaluation with no declared licence or redistribution terms.",
    "expect": "Rejected; rights are declared before use.",
    "expectedCode": "DATASET_RIGHTS_UNDECLARED"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "subgroup-below-declared-minimum",
    "kind": "negative",
    "invariants": [22, 12],
    "pins": {
      "disaggregationFactor": "declared",
      "subgroupSampleSize": 3,
      "declaredMinimumSubgroupSize": 30
    },
    "input": "A disaggregated result is reported for a subgroup below the declared minimum size.",
    "expect": "Rejected; report suppression or aggregation is required and the limitation is recorded.",
    "expectedCode": "SUBGROUP_MINIMUM_NOT_MET"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "context-label-as-identifier",
    "kind": "negative",
    "invariants": [24],
    "pins": {
      "contextLabel": "external-customer-action",
      "usedAs": "resolvable-master-identifier"
    },
    "input": "A deployment-context label is treated as a resolvable master or catalogue identifier.",
    "expect": "Rejected; no deployment or endpoint master is frozen and the label is a declared descriptor.",
    "expectedCode": "UNMASTERED_REFERENT_AS_IDENTIFIER"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "incident-occurrence-identity-claim",
    "kind": "negative",
    "invariants": [24, 10],
    "pins": {
      "reportRef": "I1",
      "usedAs": "incident-occurrence-master-identity"
    },
    "input": "A WM-AI-010 report reference is used as the master identity of the incident occurrence.",
    "expect": "Rejected; WM-AI-010 masters the reporting case only and the occurrence has no frozen master.",
    "expectedCode": "INCIDENT_OCCURRENCE_UNMASTERED"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "gate-approval-as-authorization",
    "kind": "negative",
    "invariants": [25, 6, 7],
    "pins": {
      "gateDecision": "WM-AI-003 waiver granted",
      "knwRef": null,
      "actRef": null,
      "recRef": null
    },
    "input": "An evaluation gate approval or waiver is presented as deployment authorization.",
    "expect": "Rejected; authorization requires WM-KNW-010 rationale, WM-ACT-024 act and WM-REC-010 instrument.",
    "expectedCode": "GATE_NOT_AUTHORIZATION"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "two-authoritative-assessment-revisions",
    "kind": "negative",
    "invariants": [6, 8],
    "pins": {
      "assessmentRef": "A1",
      "authoritativeRevisions": 2
    },
    "input": "Two WM-AI-008 revisions are marked authoritative at the same instant.",
    "expect": "Rejected; exactly one revision is authoritative at any instant and superseded revisions remain resolvable.",
    "expectedCode": "SINGLE_AUTHORITATIVE_REVISION"
  },
  {
    "appliesTo": "profile-fixtures.json",
    "id": "unversioned-base-pin-publication",
    "kind": "negative",
    "invariants": [14],
    "pins": {
      "basePinVersion": null,
      "basePinDigest": null,
      "verification": "unverified-current-draft",
      "requestedState": "canonicalPublishable=true"
    },
    "input": "The profile is proposed for publication with null base versions and digests.",
    "expect": "Rejected; unversioned base pins block profile publication and canonicalPublishable and installable remain false.",
    "expectedCode": "BASE_PIN_UNVERSIONED"
  },
  {
    "appliesTo": "allocation-fixtures (Reusable Evaluation Protocol)",
    "id": "protocol-text-reuse-without-governance",
    "kind": "negative",
    "invariants": [1],
    "pins": {
      "protocolTextDigest": "identical",
      "occurrences": 2,
      "independentVersioning": false,
      "independentApproval": false,
      "allocationState": "unassigned",
      "modelId": null
    },
    "input": "Identical protocol text applied in two evaluation occurrences is offered as proof of independent protocol identity.",
    "expect": "Rejected; verbatim reuse without independent versioning and approval leaves the applied protocol WM-AI-003-contained and allocates nothing.",
    "expectedCode": "NO_INDEPENDENT_IDENTITY"
  },
  {
    "appliesTo": "allocation-fixtures (Reusable Evaluation Protocol)",
    "id": "protocol-claims-metric-mastership",
    "kind": "negative",
    "invariants": [6],
    "pins": {
      "claimedOwnership": "metric definition",
      "externalMaster": "WM-AI-009",
      "allocationState": "unassigned"
    },
    "input": "The candidate asserts ownership of metric, task-contract or threshold definitions.",
    "expect": "Rejected; those definitions retain WM-AI-009 mastership and the candidate may only select and bind them.",
    "expectedCode": "MASTERSHIP_LEAK"
  },
  {
    "appliesTo": "allocation-fixtures (Standing Deployment Authorization Instrument)",
    "id": "single-issued-record-as-standing-instrument",
    "kind": "negative",
    "invariants": [1],
    "pins": {
      "issuedRecords": 1,
      "holderRef": null,
      "renewalTerms": null,
      "validityBeyondOccurrence": false,
      "allocationState": "unassigned",
      "modelId": null
    },
    "input": "One issued WM-REC-010 instrument with no holder, renewal or validity beyond the decision occurrence is offered as a standing authorization.",
    "expect": "Rejected; without persistence beyond the issued record there is no independent identity and nothing is allocated.",
    "expectedCode": "NO_INDEPENDENT_IDENTITY"
  },
  {
    "appliesTo": "allocation-fixtures (both candidates)",
    "id": "candidate-mastership-asserted-without-frozen-master",
    "kind": "negative",
    "invariants": [1],
    "pins": {
      "mastership": "asserted governance authority",
      "frozenMasterExists": false,
      "allocationState": "unassigned"
    },
    "input": "The candidate declares a governance or authorization authority as its mastership.",
    "expect": "Rejected; mastership is null and held while no frozen master exists.",
    "expectedCode": "CANDIDATE_MASTERSHIP_UNRESOLVED"
  },
  {
    "appliesTo": "allocation-fixtures (both candidates)",
    "id": "identifier-inferred-from-sequence",
    "kind": "negative",
    "invariants": [1],
    "pins": {
      "allocationState": "unassigned",
      "modelId": null,
      "registryId": null,
      "inferenceAttempt": "next free identifier in contour series"
    },
    "input": "An identifier is inferred for the candidate from registry sequence or contour position.",
    "expect": "Rejected; no identifier may be allocated, inferred or guessed at this checkpoint.",
    "expectedCode": "UNASSIGNED_CANDIDATE_REFERENCE"
  },
  {
    "appliesTo": "allocation-fixtures (both candidates)",
    "id": "allocation-request-with-complete-conditions",
    "kind": "negative",
    "invariants": [1],
    "pins": {
      "independentLifecycleEvidence": "supplied",
      "independentMastershipEvidence": "supplied",
      "reuseEvidence": "supplied",
      "registryReviewCompleted": false,
      "allocationState": "unassigned"
    },
    "input": "A proposal supplies lifecycle, mastership and reuse evidence and requests allocation at this checkpoint.",
    "expect": "Rejected at this checkpoint; the candidate stays held and unassigned until registry review completes and records the allocation.",
    "expectedCode": "ALLOCATION_REQUIRES_REGISTRY_REVIEW"
  }
]
```

## Freeze decision

**Disposition frozen. Artifact set not frozen.**

The decision is frozen exactly as intended and is not reopened: WM-AI-003 with distinct applied-plan, run and result roles; WM-AI-009 benchmark; WM-AI-008 safety assessment; WM-AI-010 incident-report feedback and trigger evidence only; the WM-KNW-010 / WM-ACT-024 / WM-REC-010 decision triad as profile; both conditional candidates identifier-unassigned with no present independent identity; no catalogue, model or runtime identifier allocated. Grok's blockers are accepted in substance except its permanent denial of candidate identity and its collapse of the benchmark dataset snapshot into WM-DAT-001, both of which are rejected above.

Freeze of the fifteen artifacts is withheld until every remediation in this report is applied verbatim; all remediations are deterministic and require no further provider run, and none is requested. On application, the contour freezes at `status: "held"`, `canonicalPublishable: false`, `installable: false`, `allocationState: "unassigned"`, with the publication blockers in defects 2, 7, 9 and 15 recorded as open. No installability, standards-conformance or publication-readiness claim is made, and no blocker is proposed for publication.
