I've read the three candidate specs and the primary sources. Now I'm writing the study.

# EM-XCT-03: Enterprise Assertion Provenance, an independent research study

**Date:** 2026-09-21 · **Role:** researcher, not approver · **Inputs:** public sources and synthetic examples only · **Status of output:** evidence for the authorized Vercy workflow. This study does not discharge any existing hold, and it grants no permission to publish or to contact anyone.

---

## 0. Verdict

I recommend a **standalone companion contract** called "Enterprise Assertion Provenance (EAP)". It gets its own runtime identity and spec digest. Its link to WM-XCT-012 is **semantic and for discovery only**. It *references patterns* from 026 and 028 and doesn't import them.

I reject the other options for these reasons:
- **Profile of 012.** A profile can only narrow a parent, not remove its required fields. 012 makes `subject-descriptor` (with digest set), `validation-outcome` (1) and `confidence` (1, `high|medium|low|unknown`) required. It also defines `high` as "first-hand contemporaneous record with cryptographic proof". That merges byte integrity with epistemic confidence, which is exactly the collapse this contour has to prevent. An EAP record would have to either fabricate those values or redefine them. Both break conformance.
- **Extension of 028.** 028 requires `has-probative-tendency`, `is-of-consequence`, `rationale-text`, `inference-mode-code`, `residual-conflict-flag` and `custody-gap-flag` on every support record. Those fit legal evidence. On a routine enterprise link they would force made-up values.
- **Reuse of 026.** 026's confidence layer (`confidence-target`, `confidence-scale-ref`, `calibration-status`, `evidence-basis-summary`) is the closest match. But it sits inside a quality assertion that requires `dimension-ref`, `measure-ref` and `result-value`. Confidence *about a pinned assertion* is not a quality measurement of a subject.
- **Defer.** Deferring would leave the critical negative case (AI analysis presented as live verification) without a machine rule.

**The three-concept hypothesis is not enough to implement honestly.** Invariants about observation, synthesis, independence, idempotent import and replay need two more independent objects: **Capture** (identified, digested acquired bytes) and **Activity** (observation, acquisition, synthesis, review or import, with its own identity). They also need a **Ledger** with a trusted current root. That makes six closed types in total. Section 4 explains why each one is needed.

---

## 1. What I actually read, and its limits

All pages were fetched through a summarizing web reader. **I did not receive raw bytes.** So I have not verified any file digest, and I quote only short spans that the reader returned verbatim.

| Source | URL | Edition/date as stated | What I read | Use |
|---|---|---|---|---|
| WM-XCT-012 | ver.cy/models/wm-xct-012-provenance/spec.yaml, publication.json, AGENTS.md | 0.3.0-research.1, generated 2026-08-22, synthesis SHA256 `06b28867…2225` | Bundles 1–3; time, integrity/attestation, lifecycle and exclusions; the 2 publication holds | Semantic association only |
| WM-XCT-026 | …/wm-xct-026-quality-confidence/spec.yaml, AGENTS.md | 0.3.0-research.1, generated 2026-08-23, synthesis `f244c50f…46ed4` | Bundles 1–3, invariants 1–12, exclusions | Confidence pattern (scale binding, calibration status, no cross-scale averaging) |
| WM-XCT-028 | …/wm-xct-028-evidence-rationale/spec.yaml, AGENTS.md | 0.3.0-research.1, generated 2026-08-23, synthesis `0ebeb503…dab4dd3` | Bundles 1–2 in detail; Bundle 3 only as an outline ("implicit continuation") | Selector/state, drift status, polarity, carryover pattern |
| W3C PROV-DM | https://www.w3.org/TR/prov-dm/ | REC 2013-04-30 | §5.1.1–5.1.5, 5.1.8, 5.2.1–5.2.4, 5.3.1–5.3.4, 5.4.2, 5.5.1–5.5.2 | Entity/Activity/Agent split; Bundle = provenance of provenance; Quotation and PrimarySource |
| in-toto Statement v1 | https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md | "v1", no date seen | Statement fields; "Subject artifacts are matched purely by digest"; subjects "assumed to be immutable" | Digest-pinned subject |
| SLSA Build Provenance | https://slsa.dev/spec/v1.2/build-provenance | v1.2, "Approved" | buildDefinition/runDetails; externalParameters "untrusted… MUST be verified downstream"; consumers "MUST accept only specific signer-builder pairs" | Trusted-declaration boundary |
| Nanopublications | https://nanopub.net/guidelines/working_draft/ ; https://nanopub.readthedocs.io/en/latest/publishing/retraction.html | Guidelines: working draft. Python library docs (search listing says 1.2.11) | Assertion/provenance/pubinfo graphs; trusty URIs; "you can never edit nor delete it. You can however retract"; retraction valid if "signed with the same public key" | Append-only retraction; assertion vs provenance vs publication-info split |
| OpenLineage | https://openlineage.io/docs/spec/object-model ; …/run-cycle | Docs site 1.53.0 | Run/Job/Dataset; client-generated `runId` (UUIDv7 recommended); START/RUNNING/COMPLETE/ABORT/FAIL/OTHER; events "accumulative" | Activity identity; client-supplied idempotency key |
| W3C Web Annotation | https://www.w3.org/TR/annotation-model/ | REC 2017-02-23 | §3.3.5 motivations (`assessing`, `questioning`, `describing`); §4 SpecificResource; §4.2 selectors; §4.3 State/TimeState (`sourceDate`, `cached`); `creator` vs `generator` | Selector+state on Capture; author vs serializer |
| W3C DQV | https://www.w3.org/TR/vocab-dqv/ | **WG Note** 2016-12-15, not a REC | §4.1–4.3, 4.7–4.9, 4.14; "Subclassing between DQV and… PROV has not been explicitly stated" | Pattern only. It is non-normative, so no conformance is claimed |

**Not read / unverified:** ISO 19157, JCGM 100/200, ISO/IEC 27037, SACM, CiTO 2.8.2, C2PA 2.4, the full text of FHIR Provenance, and the full detail of 028's Bundle 3. I cite none of their clauses.

**Digest discrepancy (new hold H-1).** The brief gives parent digests (`aa615535…`, `efd72d84…`, `3aab7ecb…`). They differ from the synthesis SHA256 values in publication.json. The two may measure different things (spec.yaml bytes vs synthesis). I could not hash the bytes, so **EAP must not record any of these as a verified parent digest.** It should record the association as `{registry-id, version, digest-as-supplied, digest-verification: unverified}`.

---

## 2. Primary approaches compared

| Approach | Key idea | Adopt | Reject | Unverified |
|---|---|---|---|---|
| **PROV-DM** | Entity/Activity/Agent; Derivation needs an underpinning activity; Bundle as entity | Separate Activity identity; `wasQuotedFrom` ≠ `hadPrimarySource`; provenance-of-provenance via ledger entries | Using PROV as a validity oracle. PROV explicitly helps "trust judgements" and does not decide truth. Also rejected: open-world partial descriptions as the store | Whether PROV-Constraints fits EAP's closed-world checks. I did not re-read PROV-Constraints |
| **in-toto / SLSA** | Digest-pinned subject; predicate typed by URI; builder trust is an explicit consumer policy | Digest-only matching of captures; `predicate-type`-like `schema-version`; "external parameters are untrusted" → EAP's trusted-declaration column | Treating a signature as proof of content truth. A SLSA provenance proves "a particular build platform produced" artifacts, and only under a trusted builder | DSSE envelope details (not read) |
| **Nanopublications** | Assertion / provenance / publication-info as separate graphs; immutable trusty URIs; retraction by new publication from the same key | Separating claim content from its provenance from its record metadata; append-only retraction; no deletion | Same-key-only retraction as the only authority model (enterprises need a delegated reviewer) | Working-draft status of the guidelines; there is no normative retraction text in the guidelines I read |
| **OpenLineage** | Client-minted `runId`, accumulative run events | Client idempotency key for imports; activity status | Accumulative merge for evidence. EAP revisions are whole snapshots so replay stays deterministic | Out-of-order semantics (not stated in the pages I read) |
| **Web Annotation** | SpecificResource = source + selector + state; `creator` ≠ `generator` | Selector + `source-state-time` + cached-copy on Capture; author ≠ observer ≠ serializer | Treating motivation `assessing` as a confidence method | n/a |
| **DQV** | QualityMeasurement / Metric / Dimension; QualityAnnotation | Nothing normative. It's a WG Note | Binding ConfidenceAssessment to dimension/metric | n/a |

---

## 3. Epistemic kind: where it lives

**Finding: epistemic kind is not a single property.** Putting it in one place forces a collapse. There are four independent axes, each on a different object:

| Axis | Lives on | Values | Validatable? |
|---|---|---|---|
| **Acquisition mode**: how the bytes were obtained | Capture (and its producing Activity) | `fetched-by-recorder`, `received-from-party`, `generated-by-activity`, `unavailable` | Partly. `generated-by-activity` requires an `activity-ref` of kind `synthesis`. The fetch itself is declared |
| **Observation object**: what was observed | Activity (kind `observation`/`acquisition`) | `observed-object-ref` (+ version if known), `observed-object-class` ∈ {`live-system`, `document`, `dataset`, `human-statement`} | Consistency only. Whether a live system was actually touched is a **trusted declaration** |
| **Link stance**: how a capture bears on a claim | EvidenceLink | `role` ∈ {`direct-observation-of-claimed-state`, `source-statement`, `inference-input`, `context`}; `polarity` ∈ {`supports`, `counters`, `contextualizes`} | Yes, structurally (see invariants I-3 to I-5) |
| **Record basis**: the recorder's standing for the claim | ProvenanceRecord | `observed`, `source-asserted`, `inferred`, `proposed`, `unverified` | Yes, as a function of its links and activities. The reference computes the **maximum permitted** basis and rejects anything stronger |

Confidence is a fifth thing. It is an **assessment about a pinned record revision**, never a basis value.

**Coexistence without collapse (synthetic).** Engineer E fetches `policy.pdf` from the shared drive, and the bytes are hashed.
- Capture C1 is `fetched-by-recorder`, digest `sha256:ab…`. The *acquisition* is observed.
- The PDF says "MFA is enforced on system S". EvidenceLink L1 from C1 to claim K ("S enforces MFA", rev 3) has role `source-statement`. So record R1 is `source-asserted`, and its author is the PDF's author, not E.
- An AI activity A2 (kind `synthesis`) reads C1 and outputs "S is compliant". Record R2 must be `inferred`. **All of A2's inputs being direct captures doesn't change this.**
- Only an Activity of kind `observation` with `observed-object-class = live-system` and `observed-object-ref = S`, producing Capture C3 (for example, an exported config) that is linked with role `direct-observation-of-claimed-state`, permits basis `observed`. Even then "observed" means *declared observed by agent X via activity Y at T*. It never means "true".

**The critical negative case, as a rule.** A record gets basis `observed` only if at least one non-withdrawn link has role `direct-observation-of-claimed-state` and all three of these hold:
1. The link's capture was produced by an Activity of kind `observation`.
2. That activity's `observed-object-ref` equals the claim's declared `about-ref`.
3. The activity is not of kind `synthesis`.

Separately, any record whose producing activity is `synthesis` is capped at `inferred`. The AI-of-local-document case fails both conditions: the observed object is a document, and the producer is synthesis. It is **denied**, not downgraded silently. The caller must resubmit with `inferred`.

---

## 4. Scope and closed schema (EAP 0.1.0-research)

**In scope:** records about **exact external claim revisions**; captures; activities; evidence links; confidence assessments; ledger/root; derived views (history, impact, corroboration).

**Out of scope (external):** claim propositional content, including its valid time; people/org registry; source cataloguing; IAM/authentication; PKI/keys; probabilistic inference engines; connectors; artifact (non-claim) provenance, which stays with 012.

**I disagree with the hypothesis here:** "about an exact external claim *or artifact version*" merges two things. For an artifact there is no proposition to be observed, asserted or inferred, so the basis axis becomes meaningless. v0.1 should be claim-only.

**Why each extra object is needed:**
- **Capture:** independence, drift and idempotency need an identity and digest that isn't a link.
- **Activity:** the synthesis and observation rules need something that has a kind and an observed object.
- **Ledger:** replay and the trusted current root need an ordered, hash-chained log.

### 4.1 Identities that must stay distinct

`record-id` (stable) ≠ `revision` (integer) ≠ `revision-digest` ≠ `claim-ref`/`claim-version`/`claim-digest` ≠ `capture-id` ≠ `content-digest` ≠ `agent-ref` ≠ `activity-id` ≠ `schema-version` ≠ `ledger-seq`/`root-digest`. Ids are opaque. A digest is never used as a record id, and an id is never parsed for meaning.

### 4.2 Field tables (all objects are immutable per revision; M = machine-checked, D = trusted declaration)

**Capture**
| Field | Card | Check |
|---|---|---|
| capture-id | 1 | M unique |
| content-digest `{alg, value}` | 0..1 | M format. Absent ⇔ `integrity = none` |
| integrity | 1 | M ∈ {`digest-verified-at-capture`, `digest-declared`, `none`} |
| acquisition-mode | 1 | M enum; `generated-by-activity` ⇒ producing activity is `synthesis` |
| produced-by-activity | 1 | M reference exists |
| source-locator | 0..1 | D (URL, path, system id) |
| selector | 0..n | M shape (text-quote / position / fragment / data-position) |
| source-state-time | 0..1 | D, RFC 3339 with offset |
| captured-at | 1 | D, RFC 3339 |
| derived-from-captures | 0..n | M acyclic |
| declared-origin | 0..1 | D, opaque origin key used for independence; absent ⇒ unknown |
| availability | 1 | M ∈ {`retained`, `not-retained`, `source-unavailable`, `deleted-by-policy`} |

**Activity**
| Field | Card | Check |
|---|---|---|
| activity-id | 1 | M |
| kind | 1 | M ∈ {`observation`, `acquisition`, `synthesis`, `review`, `import`} |
| observed-object-ref / -class / -version | 0..1 each | M required iff kind=`observation`; D content |
| performed-by (agent-ref, agent-kind ∈ {person, software, organization}) | 1..n | D |
| on-behalf-of | 0..1 | D |
| software-identity {name, version, digest?} | 0..1 | M required if any performer is software |
| inputs (capture-ids / record-revision pins) | 0..n | M exists; acyclic |
| started-at / ended-at | 0..1 each | M start ≤ end |
| status | 1 | M ∈ {`completed`, `failed`, `aborted`} |

**ProvenanceRecord** (one revision)
| Field | Card | Check |
|---|---|---|
| record-id, revision, revision-digest | 1 each | M. Revision = prior+1; digest over canonical form |
| schema-version | 1 | M exact match |
| claim {ref, version, digest?} | 1 | M ref+version required; digest optional but recorded as absent |
| about-ref | 1 | D (declared subject of the claim, e.g. system S) |
| claim-author (source author) | 0..1 | D |
| recorded-by (authenticated principal) | 1 | **Host-supplied**, never caller-supplied |
| declared-asserting-agent | 1 | D |
| basis | 1 | M ≤ computed maximum (§3) |
| generated-by-activity | 0..1 | M; `synthesis` ⇒ basis ≤ `inferred` |
| status | 1 | M ∈ {`active`, `corrected`, `retracted`} |
| supersedes-revision / correction-reason | 0..1 / 1 if revision>1 | M |
| access-scope | 1 | M, opaque scope token |

**EvidenceLink** (one revision)
| Field | Card | Check |
|---|---|---|
| link-id, revision | 1 | M |
| record-id + record-revision pin | 1 | M exists |
| capture-id | 1 | M exists |
| role, polarity | 1 each | M enum; `direct-observation-of-claimed-state` requires an `observation` activity on `about-ref` |
| asserted-by | 1 | D |
| state | 1 | M ∈ {`active`, `withdrawn`} with reason |
| access-scope | 1 | M |

**ConfidenceAssessment**
| Field | Card | Check |
|---|---|---|
| assessment-id, revision | 1 | M |
| target record-id + revision pin | 1 | M. **Never an unpinned record** |
| scheme {ref, version} | 1 | M registered scheme. The scheme declares value type (ordinal/probability/interval/label) and whether aggregation is permitted |
| value | 1 | M typed by scheme; no default |
| method-ref, purpose, assessor | 1 each | M present; D content |
| calibration | 1 | M ∈ {`no-calibration-claim`, `calibration-claimed`}; `calibration-claimed` requires `calibration-evidence-ref` |
| basis-note | 0..1 | D |

**LedgerEntry**: `seq`, `prev-root`, `entry-digest`, `object-type`, `object-id`, `revision`, `recorded-at` (host clock), `recorded-by`, `import-key?`. The new root is H(prev-root ‖ entry-digest). The current root is **trusted** only as far as the host that holds it. The reference can prove internal consistency but cannot prove the log wasn't forked.

---

## 5. Invariants (machine-enforced)

1. **I-1 Immutability.** No write mutates a stored revision. Correction = new revision + ledger entry. Ledger replay reproduces byte-identical canonical state and the same root.
2. **I-2 Distinct identity.** `record-id`, `revision-digest`, `claim-digest`, `capture-id`, `content-digest`, `agent-ref` and `schema-version` never collide by role. A write that copies one into another's slot, such as a content digest used as record-id, is denied.
3. **I-3 Basis ceiling.** Stored basis ≤ `maxBasis(links, activities)`, using the order `observed > source-asserted > inferred > proposed > unverified`. `observed` needs the rule in §3. `source-asserted` needs ≥1 active `source-statement` link. `inferred` needs a producing activity or ≥1 `inference-input` link.
4. **I-4 Synthesis cap.** `generated-by-activity.kind = synthesis` ⇒ basis ∈ {`inferred`, `proposed`}.
5. **I-5 Pinning.** Every link and assessment pins an exact record revision. Every record pins claim ref+version. There are no "latest" references in stored objects.
6. **I-6 Acyclic derivation.** The graph over `Capture.derived-from`, `Activity.inputs → outputs` and `record → generated-by → inputs` is a DAG. `context` links and cross-record "see-also" references may form cycles and are excluded from the check.
7. **I-7 Conservative independence.** Two supporting captures count as independent only if (a) their derivation closures are disjoint, (b) both have `declared-origin`, (c) the origins differ, and (d) their content digests differ. Anything else counts as `not-independent` or `independence-unknown`, never `independent`.
8. **I-8 Confidence discipline.** There is no default value. Aggregating two assessments requires the same scheme+version and a scheme that declares an aggregator. Across schemes, the result is **deny**.
9. **I-9 Non-silent withdrawal.** When a link or capture is withdrawn or retracted, the dependent records keep their stored basis and status. A derived `review-required` view lists them. The system never auto-writes `retracted` or "false" onto a claim.
10. **I-10 Idempotent import.** The key is `(source-system, source-object-id, source-revision)`. Same key and same canonical digest → no-op, returning the existing ids. Same key and a different digest → deny `import-conflict`.
11. **I-11 All-or-deny.** A read returns a whole object or a uniform `not-found-or-denied`. A derived view (impact, corroboration, basis explanation) is denied if **any** object it depends on is outside the caller's scope. It is never computed over a visible subset.
12. **I-12 Host-bound recorder.** `recorded-by` and `recorded-at` come from the trusted host call context. A caller-supplied value is ignored and the attempt is logged.

**Trusted declarations (not enforceable by the reference):** that an observation touched the live system; `source-state-time`; `captured-at` accuracy; `declared-origin`; agent kinds and on-behalf-of; the assessor's competence; that a digest was computed at capture rather than later; software identity; the fork-freedom of the ledger.

---

## 6. Time model

| Time | Owner | Meaning |
|---|---|---|
| valid time | **External claim** | When the proposition holds. EAP pins the claim version, which carries it |
| event/occurrence (`started-at`/`ended-at`) | Activity | When observation or synthesis happened (D) |
| `source-state-time` | Capture | The state of the source the bytes represent (Web Annotation TimeState analogue) |
| `captured-at` | Capture | When bytes were acquired (D) |
| `recorded-at` | LedgerEntry | Host clock. Defines total order together with `seq` |

**As-of query.** `asOf(record-id, T)` returns the highest revision whose ledger `recorded-at ≤ T`. The query takes **record time**, not valid time. Asking "what did the claim say was true at T" is the claim system's query, not EAP's.

---

## 7. Citation vs support vs corroboration; source changes

- **Citation:** a `context` link. It never raises the basis (I-3).
- **Support:** a `supports` link with role `source-statement` or `direct-observation-of-claimed-state`.
- **Corroboration:** ≥2 support links that are independent under I-7. Three copies of the same PDF share a digest and collapse to one. A summary derived from the PDF shares a derivation closure and so is not independent. Two vendor reports with no declared origin are `independence-unknown`.

**Failure distinctions:**

| Situation | Representation | Not the same as |
|---|---|---|
| Source now unreachable | Capture `availability = source-unavailable`; retained bytes still count | Claim falsified |
| No digest ever taken | `integrity = none` | Evidence untrue. It only means the bytes can't be re-verified |
| Digest mismatch on re-fetch | New Capture with a new digest; old one unchanged; drift noted | Old link invalid |
| Source author publishes a correction | New Capture plus a `counters` link, or withdrawal of the old link; the record goes into `review-required` | Automatic record retraction |
| Source deleted by policy | `availability = deleted-by-policy`; digest and metadata kept if policy allows | Erasing the ledger entry |
| External claim gets a new version | Existing records stay pinned to the old version. The impact view lists them as `claim-superseded`. New records need a new pin | Carrying over |
| Evidence missing | Record basis `unverified` | `proposed` (that means intent, not absence) |
| Evidence unknown | No link, and the record states it | An empty link list presented as "none needed" |

---

## 8. Agents, authorization and disclosure

There are three distinct roles: **claim-author** (who said it, for example the PDF's author), **observer/acquirer** (Activity performer) and **synthesizer** (performer of a `synthesis` activity, often software plus the human it acted on behalf of). **`recorded-by`** is a fourth thing: the principal the host authenticated.

The reference **records authorization decisions it was given**. It does not authenticate. Any claim that a person "signed" something is D unless an external PKI result is linked as a Capture.

**Change rights (per scope):**
- `record-writer` can create and correct records.
- `evidence-writer` can create links and captures.
- `assessor` can create assessments.
- `reviewer` can withdraw links and retract records.
- Only the original `declared-asserting-agent` or a `reviewer` may retract (a nanopub-like rule with delegation).

**Disclosure:** all-or-deny (I-11). The existence of hidden evidence must not leak through counts, basis explanations, independence verdicts or error text. Hence the uniform denial and the denial of derived views.

---

## 9. Whole-object facets

| Type | identity-class | direct-properties | recognition-observation | capabilities/actions | context/evidence |
|---|---|---|---|---|---|
| Capture | Immutable entity; id ≠ digest | §4.2 | Digest re-check, selector resolution (drift) | create, mark-availability (new ledger entry, not a mutation of bytes metadata) | produced-by Activity; derived-from |
| Activity | Occurrence; id client-mintable (UUIDv7-style) | kind, performers, times, inputs | Observed-object is D; the reference only checks presence | create, end-status | Inputs are pinned captures and revisions |
| ProvenanceRecord | Revisioned account; stable id + revisions | §4.2 | **Not applicable**: the reference cannot observe claim truth. Recognition is limited to claim-pin match | create, correct, retract, as-of read | Links; generated-by |
| EvidenceLink | Revisioned relation | role, polarity, pins | Delegated to Capture's digest | create, withdraw | Capture |
| ConfidenceAssessment | Revisioned assessment | scheme, value, method, purpose, assessor | **Not applicable**; calibration evidence is delegated | create, revise, compare (same scheme only) | calibration-evidence-ref |
| LedgerEntry | Append-only position | seq, digests, host time | Root recomputation | append (host only), replay | prev-root |

---

## 10. Lifecycle (actor / guard / effect)

| Transition | Actor | Guard | Effect |
|---|---|---|---|
| create record | record-writer | I-3, I-4, I-5, claim pin present, scope write-right | rev 1, ledger append |
| correct record | record-writer | prior rev is head; reason given; I-3 re-evaluated | rev n+1 `supersedes`; prior kept; old assessments flagged `stale-target` in views |
| retract record | declared-asserting-agent or reviewer | reason | new rev `retracted`; nothing deleted; dependents appear in impact |
| withdraw link | evidence-writer / reviewer | reason | link rev `withdrawn`; dependent records go into `review-required` (I-9). Their basis is **not** rewritten, but a *new* correction would face the lower ceiling |
| create assessment | assessor | I-8, pinned target exists and is visible | rev 1 |
| import | importer | I-10 | no-op / create / deny |
| export | any reader | I-11 over the whole closure | canonical bundle + root |

---

## 11. Mastership

| Data | Master | EAP's role |
|---|---|---|
| Claim content, valid time, claim versions | Claim/knowledge system | Pin only |
| Agents, orgs | Party/IAM | Opaque refs |
| Source catalogue | Catalogue | Locator only |
| Capture bytes | Evidence store (optional) | Digest + availability |
| Records, links, assessments, ledger | **EAP** | Master |
| Keys, signatures | PKI | A verification result may be a Capture |
| Confidence schemes | Scheme registry (could be a small EAP-local table) | Reference + version |

---

## 12. Routes (question → finding → artifact → allowed action)

| # | Question | Finding | Artifact | Allowed action |
|---|---|---|---|---|
| 1 | Was S's MFA *observed* live? | basis=`observed` requires an observation activity on S | Record + Activity + Capture | Show "declared observed by X at T via A". Never "verified" |
| 2 | Is this AI conclusion a verification? | synthesis ⇒ ≤`inferred` | Record, Activity(kind=synthesis) | Label inferred; route to human review |
| 3 | What does the source say vs what did we see? | separate link roles | Links L(source-statement), L(direct-observation) | Show both side by side |
| 4 | Are these two reports independent? | I-7 | Corroboration view | Report `independent` / `not-independent` / `unknown` |
| 5 | What did record R say on 2026-09-01? | as-of by record time | Ledger replay | Read |
| 6 | Why was R changed? | correction reason | Rev n+1 | Read (if in scope) |
| 7 | Source retracted. What's affected? | I-9 | Impact view | Open review tasks. Do not auto-retract |
| 8 | Claim moved to v4. Is our record current? | I-5 pin | Impact `claim-superseded` | Create a new record pinned to v4 |
| 9 | Can I trust this PDF's bytes? | integrity field | Capture | Re-hash if retained. Integrity ≠ truth |
| 10 | How confident are we, and by what method? | I-8 | Assessment | Show scheme/method/purpose/assessor |
| 11 | Average confidence across teams? | cross-scheme | none | **Deny** |
| 12 | Re-running the importer? | I-10 | Ledger import-key | No-op |
| 13 | Show the evidence for R to an auditor without scope on L2 | I-11 | none | Deny the derived view uniformly |
| 14 | Is the exported bundle intact? | root recomputation | Export + root | Accept if roots match; the host trust in the root is still D |
| 15 | Who wrote vs who observed vs who synthesized? | §8 roles | Record + Activities | Read |
| 16 | Can a 012 `confidence: high` be imported? | no scheme/method | none | **Refuse migration** |
| 17 | Missing evidence for a claimed control? | basis `unverified` | Record | Flag the gap. Don't rate confidence as if evidence existed |

---

## 13. Test cases (synthetic)

**Positive**
- **P1** Direct live observation → `observed`.
- **P2** PDF bytes fetched plus a source-statement link → `source-asserted`, while the capture is `digest-verified-at-capture`.
- **P3** AI synthesis over P1 and P2 → `inferred`. A human review activity then creates a *new* record by the reviewer. It is still `inferred`, or it becomes `observed` only if the reviewer performs their own observation.
- **P4** Correction rev 2 keeps rev 1, and as-of queries return each revision correctly.
- **P5** Idempotent import runs twice → one object.
- **P6** Export → import into an empty store → identical root (round trip).

**Negative (each must deny with a specific code)**
- **N1** AI-over-local-document stored as `observed` → `basis-exceeds-ceiling`.
- **N2** `observed` link where the activity's observed object (document D) ≠ `about-ref` S → `observation-object-mismatch`.
- **N3** Link pinned to an unpinned or "latest" record → `unpinned-reference`.
- **N4** Content digest used as record-id → `identity-role-collision`.
- **N5** Derivation cycle C1→C2→C1 → `derivation-cycle`. (A `context` cycle is allowed.)
- **N6** Assessment with no scheme, or value `0.95` with no method → `confidence-incomplete`.
- **N7** Aggregating an ordinal scheme with a probability scheme → `cross-scheme-aggregation`.
- **N8** Import with the same key and a different digest → `import-conflict`.
- **N9** Caller-supplied `recorded-by` differs from the host principal → ignored + audit entry. The object is created only if the other guards pass.
- **N10** Corroboration requested where one link is out of scope → `not-found-or-denied`, with the same text as for a truly missing object.
- **N11** Retraction by a non-author, non-reviewer → `not-authorized`.
- **N12** Updating rev 1 in place → `immutable`.
- **N13** `calibration-claimed` without evidence → `calibration-unsupported`.
- **N14** Three identical-digest copies counted as corroboration → reported as `not-independent`.

**Historical:** withdrawing link L1 after R1 was `source-asserted` leaves R1 rev 1 unchanged. R1 appears in `review-required`. A reviewer's rev 2 must meet the new ceiling (`unverified` if no other support), with reason "support withdrawn". The claim itself is never marked false.

**Migration refusal:** importing a 012 assertion with `account-basis: contemporaneous` and `confidence: high` is refused. "Contemporaneous" concerns origination of a subject, not observation of a claim's truth, and "high" has no scheme or method. Mapping them would invent semantics. The allowed alternative is to import it as a Capture of the 012 document (the bytes) with a `source-statement` link. That gives a record with basis `source-asserted` whose `claim-author` is the 012 asserting agent.

---

## 14. Synthetic profiles

- **Minimum startup.** One host process, a local JSON ledger, no IAM (a host-configured single principal), no evidence store (`availability = not-retained` is allowed and digests are still kept), and one built-in ordinal scheme `eap:ordinal-3@1` with `aggregation: none`. Required: Capture, Activity, Record, Link. Assessment is optional.
- **Scaled group with conflicting claims.** Two subsidiaries' CMDBs assert different MFA states for S. Both become `source-asserted` records on the *same* claim pin, with different `claim-author`s. Contradiction is a derived view, not an overwrite. One live observation adds an `observed` record. EAP does not choose a winner; resolution is a reviewer's new record or an external decision system. Independence is `unknown` unless the CMDBs declare origins.
- **AI team.** A model output is always a synthesis Activity with `software-identity` (name/version/digest if known) and `on-behalf-of` a human. Human review is a separate `review` activity. Approval does **not** promote the basis. The UI must say "AI-inferred, human-reviewed". The model's own self-reported confidence is an assessment with `no-calibration-claim` unless calibration evidence exists.

---

## 15. Recommended minimum implementation (pure reference)

1. Canonical JSON (sorted keys, UTF-8, no floats in identity-bearing fields) with SHA-256 revision digests.
2. `apply(state, command, hostCtx) → (state', ledgerEntry) | Deny(code)` as a pure function. Guards I-1 to I-12.
3. `replay(ledger) → state, root`. The test is `replay(export(s)) == s`.
4. Queries `asOf`, `impact(captureOrLinkOrClaimPin)`, `corroboration(record-rev)`, `maxBasis(record-rev)`, each wrapped in a visibility closure check.
5. The test suite from §13.

This is a **trusted-host reference**. It is not a production service: no authentication, no fork detection, no key custody.

---

## 16. Disagreements with the hypothesis

1. Three concepts are not enough. Capture, Activity and Ledger are required (see §4).
2. "Record about a claim **or artifact**" should be claim-only in v0.1.
3. The EvidenceLink should target a **Capture**, not a "source". A source without captured state can't be pinned.
4. "Refuting" overclaims. Use `counters`: it's a relation, not an adjudication.
5. The 012 association must carry an explicit **non-mapping notice** for 012's `confidence` and `validation-outcome`.
6. The supplied parent digests are unverified and don't match the published synthesis digests (H-1).

## 17. Strongest failure modes

- **Declaration laundering:** an agent declares an `observation` activity it never performed. Schema validation cannot catch this. The mitigations are an external attestation as a Capture, plus UI wording that attributes the observation to its declarer.
- **Claim identity drift:** the claim system mutates content without bumping the version, so pins stop meaning anything. Record `claim-digest` whenever possible.
- **Rendered vs raw bytes:** the digest is taken over a normalized rendering, so re-verification fails spuriously. Declare the digest target.
- **Hidden common origin** inflates corroboration. I-7 defaults to unknown.
- **Derived-view leakage**, through counts, error timing or text.
- **"Verified" in the UI or in exports.** The biggest real-world risk. Ban the word.
- **Confidence misuse** as a risk score or pass/fail gate.
- **Trusting the host clock and the root** beyond a single host.

## 18. Remaining holds (new; none of the old holds are discharged)

- **H-1** Parent digest mismatch/unverified.
- **H-2** Raw-byte verification of all three specs (I only saw them through a summarizer).
- **H-3** 028 Bundle 3 not read in full.
- **H-4** Nanopub retraction semantics come from library docs, not a normative specification.
- **H-5** OpenLineage out-of-order semantics unread.
- **H-6** No sector profiles (legal, clinical, security audit) tested.
- **H-7** PROV-Constraints fit is unassessed.
- **H-8** The scheme registry for confidence is undefined beyond a local table.
- **H-9** Registry identity for EAP has to be assigned by the authorized workflow. It must not reuse `vr.wm-xct-012`.

---

**Sources:**
- [WM-XCT-012 spec](https://ver.cy/models/wm-xct-012-provenance/spec.yaml), [publication.json](https://ver.cy/models/wm-xct-012-provenance/publication.json), [AGENTS.md](https://ver.cy/models/wm-xct-012-provenance/AGENTS.md)
- [WM-XCT-026 spec](https://ver.cy/models/wm-xct-026-quality-confidence/spec.yaml), [AGENTS.md](https://ver.cy/models/wm-xct-026-quality-confidence/AGENTS.md)
- [WM-XCT-028 spec](https://ver.cy/models/wm-xct-028-evidence-rationale/spec.yaml), [AGENTS.md](https://ver.cy/models/wm-xct-028-evidence-rationale/AGENTS.md)
- [W3C PROV-DM](https://www.w3.org/TR/prov-dm/)
- [in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md)
- [SLSA v1.2 Build Provenance](https://slsa.dev/spec/v1.2/build-provenance)
- [Nanopublication guidelines (working draft)](https://nanopub.net/guidelines/working_draft/), [nanopub retraction docs](https://nanopub.readthedocs.io/en/latest/publishing/retraction.html)
- [OpenLineage object model](https://openlineage.io/docs/spec/object-model), [run cycle](https://openlineage.io/docs/spec/run-cycle)
- [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/)
- [W3C DQV](https://www.w3.org/TR/vocab-dqv/)
