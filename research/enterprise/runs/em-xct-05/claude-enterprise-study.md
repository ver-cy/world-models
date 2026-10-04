# EM-XCT-05: Disclosure, classification and retention, an independent research study

**Status:** research only. This is not a review of future code, not permission to publish, and not a claim about any real company. All scenarios use synthetic data. Retrieved content was treated as evidence, not as instructions.

---

## 0. Summary

- **I don't recommend one "EM-XCT-05 policy" type.** The four registry candidates map to four different owners. Two already exist as published research models (WM-XCT-003 and WM-XCT-020), one is a `todo` stub (WM-XCT-035), and one is a profile of an existing model, not a new type.
- **The smallest useful original companion should be split into two exported types:**
  - an immutable, content-pinned **ContextPackageProposal** (what would be assembled, for whom, and why);
  - a separate **JointDisclosureReview** bound to that proposal's exact digest.
- **The serving result stays with the host.** The enforced disclosure result (the "serving decision") and its audit record belong to the host. The companion only defines the preconditions the host must check and the evidence it must return.
- **Retention and hold stay out of the companion.** It carries opaque references with explicit `unknown` states. It can raise a restricted *unresolved-disposition* block, but it never selects a date and never deletes anything.
- **A declared review is not an enforced result.** A cleared review is a necessary input to serving, never enough on its own. Every actual read needs a current host authorization inside a single freshness boundary.

---

## 1. Evidence base: what I actually retrieved

| Item | Retrieved? | What I saw | Limits |
|---|---|---|---|
| WM-XCT-002 spec.yaml | Yes, **truncated** | Metadata; purpose; owns / does-not-own lists; boundary table; Bundles 1–2 in full; Bundle 3 up to the first finding of Layer 3.1 (`state-code`, `state-transition-timestamp`, `active-flag`); 19-source registry; coverage decision vocabulary (Permit / Deny / Indeterminate / NotApplicable, with obligations and advice) | The file cuts off inside Layer 3.1. Termination propagation, amendment, precedence, and instrument retention/erasure layers were **not seen**. The page shows `Synthesis SHA256 478f7f04…`, which is not the spec digest `9085d977…` you supplied. **I could not compute or verify either hash**, because my fetch tool returns a model summary, not raw bytes. |
| WM-XCT-003 spec.yaml | Yes, **truncated** | Owns / excludes lists; neighbour table (KNW-012, XCT-038, 005, 020, DAT-004, 004, 002, 001); Bundle 1 (selection, paths, graph extent, treatment, reversibility, record scope, grain, shape algebra); Bundle 2 (template fingerprint, schema drift, encoding, residual side channels); Bundle 3 up to `applicability-conditions`; 22 sources | Cut off mid-sentence ("behaviour when an attribute is unavailable"). **None** of the holds you list (source tiers, untested grain/media profiles, US/EEA-only evidence, owner for identifiability evidence, legal-hold precedence) were visible to me. I carry them forward from your brief. Hash not verified; the page shows `Synthesis SHA256 96a40c5b…`. |
| Parent holds you listed | Partially | For WM-XCT-002 I saw: SRC-005 ISO text paywalled; DPV "not a W3C Standard"; FHIR R5 Consent maturity 2 / Trial Use; SRC-015 publication page only; SRC-019 "Kantara receipt-direction conflict" | The other holds are **preserved from your brief, not independently seen**. |
| WM-XCT-020 | Page and spec, **truncated** | Published, **"Classification Binding"**, 0.3.0-research.1, reviewable-draft. Reified n-ary binding: subject, scheme URI, **scheme version pinned at assignment**, term, role, origin. Non-substantive states: residual, unknown, not-applicable, refused, not-yet-classified. Transitions include downgrade. The binding itself may be sensitive. Holds: confidence semantics, non-EU regimes, multi-label ML, sibling Scheme/Value Set/Mapping models unregistered | Only a synthesis hash (`8672e6ca…`) is shown, with **no spec digest**. So I cite it as a **conceptual reference only**, not as a pinned delegation. Note that WM-XCT-003 calls this model "Sensitivity Classification"; the published name is broader. |
| WM-XCT-035 | Page only | `TODO`, no version, "Specification is planned", scope phrase "Retention trigger, hold, disposition and evidence" | Nothing else. I haven't invented any fields, pins or obligations for it. |
| WM-XCT-005 | Catalogue search | Only a **legacy** entry: "Privacy Aggregation Floor", 0.2.0-legacy, "k-anonymity floors" | No research version found. Not adopted. |
| WM-XCT-038, WM-DAT-004, WM-KNW-012, WM-XCT-001 | **Not located** | — | The catalogue has about 206k entries and search didn't surface them. I treat them as **unavailable**: host binding or deferral, never a dependency. |
| Enterprise companions (authority, evidence, temporal) | Not located | The catalogue does show enterprise-versioned entries, e.g. WM-XCT-036 `0.3.2-enterprise.1` | Referenced as bounded assertion refs only, with no pins. |

### External primary sources

Section numbers marked † came from my fetch tool's summary, not from raw HTML, so they are unverified.

| # | Source | Edition / status | What it gives here |
|---|---|---|---|
| S1 | W3C **ODRL Information Model 2.2** | **W3C Recommendation**, 15 Feb 2018 (`/TR/2018/REC-odrl-model-20180215/`) | Policy `uid` MUST be an IRI; Set / Offer / Agreement; AssetCollection with `refinement`; rules with duty, remedy and consequence; `conflict` = `perm` / `prohibit` / `invalid`, **defaulting to `invalid`** (§2.10†); `inheritFrom` (§2.9†). Evaluation and enforcement are out of scope. |
| S2 | W3C **ODRL Vocabulary & Expression 2.2** | **W3C Recommendation**, 15 Feb 2018 | Actions such as `read`, `distribute`, `aggregate`, `derive`, `anonymize`, `archive`, `delete`. Left operands such as `purpose`, `recipient`, `dateTime`, `elapsedTime`, `count`. `profile` is mandatory when a profile is used. |
| S3 | **DPV 2.3** (W3C DPVCG) | **Community Group report**, 25 Feb 2026: "not a W3C Standard nor … on the W3C Standards Track" | Purpose, Destruct, Erase, Aggregate. **No legal-hold concept found.** DPV 2.1 (16 Mar 2025) was also retrieved and lists StorageDuration and StorageDeletion; the 2.3 summary said those weren't in its index. Meanwhile the DPVCG homepage still lists "v1 (2022)". So there is **edition drift** here, which matches WM-XCT-002's existing hold. |
| S4 | **NIST SP 800-162**, Guide to ABAC Definition and Considerations | Final, Jan 2014, **Update 2 dated 2 Aug 2019**, doi:10.6028/NIST.SP.800-162 | ABAC evaluates subject, object, operation and **environment-condition** attributes against policy. The landing page didn't name PDP/PEP; that decomposition comes from S6. |
| S5 | **NIST SP 800-188**, De-Identifying Government Datasets: Techniques and Governance | Final, **Sep 2023** | Disclosure Review Board; re-identification studies; four sharing models (publish, synthetic, query interface, enclave). **The PDF would not parse**, so I have no section numbers and no differencing quotes. |
| S6 | **OASIS XACML 3.0 Core** | OASIS Standard, 22 Jan 2013 | PAP/PDP/PEP/PIP (§3.1†); Permit / Deny / Indeterminate / NotApplicable; a PEP must deny unless it can discharge every obligation (§2.12†); `MissingAttributeDetail` (§5.58†). |
| S7 | **Cedar** docs, "Authorization" | Live docs, retrieved 2026-09-21, unversioned | Default deny; forbid overrides permit; **a policy that errors is skipped**; diagnostics list the determining policies and errors. |
| S8 | **OPA** docs, "Policy Language" | Live docs, version not shown | "Undefined" is distinct from false; `default` supplies the fallback value. |
| S9 | **AWS S3 Object Lock** user guide | Live docs, retrieved 2026-09-21 | Retention and legal hold are **independent and per object version**; a legal hold "has no expiration date"; a simple DELETE only adds a **delete marker**; compliance mode vs governance mode; variable retention via an event hold. |
| S10 | **Google Cloud Storage "Object holds"** | Updated 2026-09-18 | Event-based vs temporary holds. Releasing an event-based hold restarts the retention clock. Holds don't expire. A held object "cannot be deleted or replaced". |
| S11 | **NIST SP 800-88 Rev. 2**, Guidelines for Media Sanitization | Final, **Sep 2025**, supersedes Rev. 1 | Clear / purge / destroy; sanitization program. Only the landing page was read. |
| S12 | Microsoft Purview, "Learn about retention policies & labels" | Page dated 2026-07-22 | **The primary page was too large to process.** The rules "retention wins over deletion", "longest retention wins" and "explicit beats implicit" come **only from search-result snippets**, so they're secondary and uncorroborated. |

There are four comparison schools:

- **(A) Declarative rights and policy vocabularies:** ODRL, DPV.
- **(B) Attribute-based decision engines:** NIST ABAC, XACML, Cedar, OPA.
- **(C) Statistical disclosure control:** NIST 800-188.
- **(D) Records retention and WORM storage:** S3 Object Lock, GCS holds, Purview, NIST 800-88.

None of them covers "approved card + approved card ≠ approved combination". School A declares, B decides one request at a time, C reasons about releases, and D preserves bytes. That gap is what the original companion is for.

---

## 2. Challenging the provisional boundary

1. **"One companion holding proposal, review, authorization evidence and retention" is too wide.** These have different writers (proposer, reviewer, host PDP, records owner), different lifecycles (immutable request; review that expires; per-read decision; schedule and hold), and different invalidation triggers. Merging them recreates the "one policy field" you asked me to avoid. **Split into Proposal and Review. Serving and retention are host binding or deferral.**
2. **Can the proposal and review be merged?** No. A review must be able to name exactly one proposal digest, be withdrawn without touching the proposal, and be authored by someone other than the proposer. Also, several reviews (for example static and statistical) may apply to one proposal.
3. **Should "joint review" be dropped and left to WM-XCT-005?** No. The only 005 I found is legacy k-anonymity floors. A cohort floor is one possible review *method*, not the review itself. The review must be able to say `cleared` under a named method while asserting no mathematical guarantee.
4. **Is a new universal WM identity needed?** No. The companion's identifiers are scoped to the Dimension and the companion. Meta-Objects keep their canonical identities. Aggregates are ordinary Meta-Objects with their own owner.
5. **Is WM-XCT-003 enough for single-object projections?** Mostly, used as a profile: closed selection, default deny, pinned schema, `grain_class = record-subset`, single-object record scope. The part 003 explicitly excludes (runtime decision, enforcement, classification assignment) must not be patched in by the companion.

---

## 3. Dispositions of the four candidates

| Candidate | Disposition | Rationale | Alternative rejected |
|---|---|---|---|
| **DisclosurePolicy** | **Reuse and split.** Output shape: WM-XCT-003 (pinned `0.3.0-research.1`, sha256:058191fe…, byte identity as verified by Codex, not by me). Permission to read: WM-XCT-002 (pinned `0.3.0-research.1`, sha256:9085d977…). Runtime decision: **host binding**, since WM-XCT-038 wasn't located. Policy governance and lifecycle: **documented deferral**, since WM-KNW-012 wasn't located; the companion records only `policy_ref + policy_version`. | "Disclosure policy" already mixes shape, grant and decision. 003 and 002 already separate them. | A new DisclosurePolicy type would duplicate 003's shape algebra and 002's purpose and grant. |
| **ClassificationAssignment** | **Conceptual reference to WM-XCT-020 Classification Binding**, profiled as follows: scheme version must be pinned; the non-substantive state `unknown` / `not-yet-classified` is admissible and means **fail closed**; a binding revision ref is required per permitted field. Classification **scheme** definition: **documented deferral** (020's sibling Scheme model is unregistered). | 020 already owns reified assignment and downgrade. **No spec digest is published**, so this can't be an executable pin yet. | Embedding a class code in the projection field set, which would make a label act like a grant. |
| **RetentionConstraint** | **Documented deferral** to WM-XCT-035, which is `todo`. The companion holds only opaque **host references** to retention and hold records, each with a state of `referenced` / `none-declared` / `unknown`, per artifact role. | Nothing defensible can be pinned or delegated. The S9–S12 patterns show retention and hold are independent, per version, and conflict-prone, and that belongs to the owning domain. | Designing 035's fields here would invent another team's model. |
| **ProjectionContract** | **Profile of WM-XCT-003**, "SingleObjectProjection": record scope is exactly one canonical Meta-Object and revision; `de-sel-closure-mode = closed`; `de-sel-default-treatment = deny`; `de-drift-strictness = pinned`; recursive-descent and wildcard paths forbidden; `de-enc-omission-representation` must be uniform; `de-res-uniformity-rule` required. **Composite report: separate aggregate.** It is its own Meta-Object with owner, boundary, calculation, purpose and review, projected by its own single-object projection. | Keeps "one projection, one object" as a checkable rule. | A "multi-object projection", i.e. a Projection pretending to cover many objects. |

**New original companion (bounded):** `ContextPackageProposal` and `JointDisclosureReview`. The value type `PackageMember` is embedded in the proposal. **Host binding interface, not exported:** `ServingDecision` and `RecipientResponse`.

---

## 4. Types, identities, lifecycle, fields

Version axes are kept **separate** throughout:

- `companion_schema_version`: the schema of the proposal/review record, e.g. `em-xct-05/0.1.0-research.1`.
- `object_revision`: the source Meta-Object revision.
- `source_schema_version`: the source data schema.
- `policy_version`: the WM-XCT-003 shape.
- `instrument_version`: the WM-XCT-002 grant.
- `classification_binding_revision` and `scheme_version`.
- `status`: the lifecycle state of the record itself.

### 4.1 ContextPackageProposal

Immutable. A change means a new proposal with `supersedes`.

| Field | Card. | Type / time | Notes |
|---|---|---|---|
| `proposal_id` | 1 | Opaque ID minted by the host (ULID) | Lineage handle only. **Not a permission.** |
| `companion_schema_version` | 1 | Semver string | |
| `proposal_digest` | 1 | `sha256:` over the declared canonical form of every field except `proposal_id` and `status` | Integrity and review binding. **Not freshness, not authority.** |
| `dimension_ref` | 1 | Ref | The Company Dimension host. |
| `proposer_ref` | 1 | Party ref | Owned by the party model. |
| `audience` | 1 | `{recipient_refs 1..n \| audience_class_ref 1, legal_entity_refs 0..n}` | Legal-entity audience is explicit (matrix case). |
| `purpose` | 1..n | `{code, scheme_ref, scheme_version}` | Purpose ≠ grant. |
| `members` | 1..n | PackageMember | Ordered; ordinals never reused. |
| `membership_digest` | 1 | sha256 over the ordered member pins | Separately checkable. |
| `value_mode` | 1 | `metadata-only` \| `closed-synthetic` | No live values in v0.1. |
| `access_instrument_refs` | 1..n | `{WM-XCT-002 instrument id, instrument_version}` | Reference only. |
| `authorization_evidence` | 0..n | `{host_evidence_ref, decision ∈ {permit, deny, indeterminate, not-applicable}, host_state_token, observed_at, valid_until}` | Evidence captured **at proposal time**. Never reused for serving. |
| `retention_refs` | 1..n | `{artifact_role ∈ {source, derived-cache, package-output, policy-evidence, backup}, ref?, state ∈ {referenced, none-declared, unknown}}` | Every role must be present. `unknown` is allowed but blocks a `cleared` review for roles the package creates (package-output, policy-evidence). |
| `hold_refs` | 1..n | `{artifact_role, ref?, state ∈ {known-active, known-none, unknown}}` | A hold never authorizes disclosure. |
| `created_at` | 1 | RFC 3339 with offset | |
| `supersedes` | 0..1 | proposal_id | |
| `status` | 1 | `draft → submitted → (withdrawn \| superseded)` | Status sits outside the digest. |

### 4.2 PackageMember (value type)

| Field | Card. | Notes |
|---|---|---|
| `ordinal` | 1 | |
| `meta_object_ref` | 1 | Canonical object ID. Exactly one object. |
| `object_kind` | 1 | `domain-object` \| `aggregate-object`. An aggregate requires `aggregate_decl_ref`. |
| `object_revision` | 1 | Exact. No "latest". |
| `source_schema_ref` / `source_schema_version` | 1 / 1 | Host schema pin (WM-DAT-004 unavailable). |
| `projection_policy_ref` / `policy_version` | 1 / 1 | WM-XCT-003 SingleObjectProjection profile. |
| `template_fingerprint` | 1 | 003 `de-tpl-fingerprint`. |
| `permitted_fields` | 1..n | `{normalized_path, classification_bindings 1..n: {binding_ref, binding_revision, scheme_uri, scheme_version, term}}`. **Closed set.** Metadata items (keys, counts, timestamps, ETags) are listed as fields too. |
| `aggregate_decl_ref` | 0..1 | Owner, boundary, calculation, purpose and own review of the aggregate object. |
| `member_content_digest` | 0..1 | Only for `closed-synthetic` values. |

### 4.3 JointDisclosureReview

| Field | Card. | Notes |
|---|---|---|
| `review_id`, `companion_schema_version` | 1, 1 | |
| `proposal_digest` | 1 | **Exact.** Any change to the proposal makes the review not apply. |
| `membership_digest`, `audience_digest`, `purpose_digest` | 1 each | Redundant on purpose, so the host can tell *why* the review is stale (internal diagnostics only). |
| `reviewer_ref`, `reviewer_authority_ref` | 1, 1 | Authority is an assertion ref (enterprise authority companion, unpinned). The reviewer must not be the proposer. |
| `method` | 1..n | `{kind ∈ {static-human, rule-set, statistical}, method_ref, method_version}` |
| `considered_channels` | 1..n | From a closed list: `subtraction/differencing`, `repeated-release`, `existence`, `count/cardinality`, `ordering`, `error-shape`, `timing`, `linkage-to-prior`. An unlisted channel counts as **not considered**. |
| `prior_release_refs` | 0..n | Earlier packages to the same audience within `lookback`. |
| `verdict` | 1 | `cleared` \| `cleared-with-conditions` \| `rejected` \| `needs-owner` \| `indeterminate` |
| `conditions` | 0..n | e.g. `suppress member k`, `max serving count`. |
| `residual_risk_acceptance_ref` | 0..1 | Mirrors 003 `de-res-accepted-risk`. |
| `guarantee_claim` | 1 | Fixed value `none-mathematical`. The schema rejects any other value. |
| `valid_from` / `valid_until` | 1 / **1** | No open-ended reviews. |
| `concluded_at` | 1 | |
| `status` | 1 | `in-review → concluded → (withdrawn \| expired \| invalidated)` |
| `evidence_refs` | 0..n | Evidence companion refs. |

### 4.4 Ownership (RACI-style)

| Concern | Owner / master | Writer | Reader | Purpose |
|---|---|---|---|---|
| Meta-Object and revision | Domain owner | Domain | Companion (pin only) | Source of truth |
| Projection shape | WM-XCT-003 policy owner | Policy author | Companion, host | Output shape |
| Grant / consent | WM-XCT-002 instrument | Grantor / manager | Host PDP | Permission to read |
| Classification binding | WM-XCT-020 binding authority | Classifier | Companion, host | Label (not access) |
| Retention / hold | Records owner (WM-XCT-035 later) | Records / legal owner | Companion (ref only) | Keep / dispose constraints |
| Proposal | Proposer in the Dimension | Proposer | Reviewer, host | Request |
| Review | Disclosure reviewer | Reviewer | Host (internal) | Combination approval |
| Serving decision and audit | Host (WM-XCT-004 conceptually) | Host PEP | Auditors | Enforcement result |

---

## 5. The five facets per exported type

Delegation to WM-XCT-003 and WM-XCT-002 means the pins in §3. WM-XCT-020 is **conceptual, unpinned**.

| Facet | ContextPackageProposal | JointDisclosureReview | PackageMember |
|---|---|---|---|
| **identity-class** | **Required.** Companion-scoped record; `proposal_id` is lineage, `proposal_digest` is content identity. Not a WM universal identity. | **Required.** `review_id`, bound to exactly one `proposal_digest`. | **Not applicable** as an independent identity: identified by (proposal, ordinal). Object identity is **delegated** to the domain owner. |
| **direct-properties** | **Required**: §4.1 fields. | **Required**: §4.3 fields. | **Required**: §4.2. Shape semantics **delegated** to WM-XCT-003@0.3.0-research.1. Label semantics are a **conceptual ref** to WM-XCT-020 (no pin; blocks execution until a spec digest exists). |
| **recognition-observation** | **Optional.** Only `authorization_evidence` observed at proposal time (`observed_at`, `host_state_token`). **Never** used as serving evidence. | **Required.** `concluded_at`, method versions, and the list of considered channels, i.e. what the reviewer actually looked at. | **Delegated.** Current revision and current classification are observed by the host at serving, not stored. |
| **capabilities-behaviour-actions** | **Required, bounded.** Permitted actions: `submit`, `withdraw`, `supersede`, `validate`. **No** `serve` / `grant` / `delete`. | **Required, bounded.** `conclude`, `withdraw`, `expire`, `invalidate`. The review **cannot** authorize serving on its own. | **Not applicable.** Value type with no behaviour. |
| **context-evidence** | **Required.** `access_instrument_refs` (**delegated** to WM-XCT-002, pinned), `retention_refs` / `hold_refs` (**deferred**: opaque host refs, WM-XCT-035 is todo), authority and evidence companion refs (unpinned). | **Required.** `reviewer_authority_ref`, `evidence_refs`, `residual_risk_acceptance_ref`. | **Optional.** `aggregate_decl_ref`, owned by the aggregate's owner. |

---

## 6. Concrete implementation contract (for a future frozen audit)

```text
validate_proposal(P, registry_pins) -> ValidationReport          # pure, deterministic
  rejects: missing retention/hold role, unknown field path vs pinned template,
           unknown classification (unknown/not-yet-classified), non-pinned revision,
           projection not in SingleObjectProjection profile, aggregate member without decl.

review_applies(R, P) -> Applies | NotApplies(internal_reason)     # pure
  requires R.proposal_digest == digest(P) and R.status == concluded
           and R.verdict in {cleared, cleared-with-conditions} and R.valid_until > now

serve(P_id, request_ctx, host) -> (RecipientResponse, InternalDiagnostic)
  snap := host.snapshot()                   # one atomic freshness boundary
  for each member m: host.current_revision(snap, m) == m.object_revision
                     host.classifications(snap, m) ⊆ m.permitted_fields labels (exact revisions)
                     host.authorize(snap, audience, purpose, m) == permit   # XACML-style value
  review_applies(R, P) evaluated at snap time
  if host has no atomic snapshot: decision.validity = limited(max_age), marked in diagnostic
  RecipientResponse ∈ { Package(exact template output), Unavailable(constant shape) }
  InternalDiagnostic: reason codes, stale pins, missing attributes — never shown to recipient
```

A **declared review artifact** (`JointDisclosureReview`) is a record about a proposal. An **enforced disclosure result** is `serve()`'s output, produced by the host under its own authority and audit. The companion owns the first and specifies preconditions for the second. It owns nothing that executes against live data.

---

## 7. Invariants (testable)

- **I1.** Every PackageMember references exactly one `meta_object_ref` at exactly one `object_revision`. There are no wildcards and no "latest".
- **I2.** `permitted_fields` is closed. A served output containing any path, including a metadata path, not in the set is a violation. Unknown or new source fields are never emitted.
- **I3.** A classification term never appears as an access condition in the companion. Removing every classification binding must never widen the output.
- **I4.** `review_applies(R, P)` is false whenever any of these differ: membership digest, any object revision, audience, purpose, or any `policy_version` / `template_fingerprint`.
- **I5.** `serve()` never returns `Package` without a `permit` from the host for every member, obtained inside the same snapshot (or inside a declared limited validity).
- **I6.** `RecipientResponse.Unavailable` is byte-identical across these cases: object missing, field denied, review stale, grant revoked, hold unknown, classification unknown. It is constant-shape with no counts, names or reasons.
- **I7.** `unknown` never compares equal to `false`, `0`, `none`, `unclassified`, `approved` or `erased`. Any `unknown` on a gating input yields `Unavailable`.
- **I8.** Nothing in the companion changes a retention date, releases a hold, or issues a deletion. The companion's only disposition-related output is `needs-owner`.
- **I9.** `JointDisclosureReview.guarantee_claim == none-mathematical`, and `valid_until` is present.
- **I10.** Two proposals with the same `proposal_digest` get the same `validate_proposal` result. `serve()` results may differ; see the replay counterexample in §12.

## 8. Semantic negatives (what the companion must not be read as)

1. A cleared review **is not** permission to serve.
2. Per-member approval **is not** approval of the combination.
3. A classification code **is not** an access grant, and "unclassified" **is not** "public".
4. A retention condition **is not** authorization to disclose or destroy.
5. An active hold **is not** a perpetual retention rule, and does not survive its own release.
6. A digest match **is not** freshness, currency or permission.
7. A cohort floor or human sign-off **is not** a proof of non-inference.
8. A delete request **is not** executed deletion, and executed deletion **is not** verified disposition.
9. A stop-serving decision **is not** erasure of recipient copies.
10. A Projection over an aggregate **is not** a projection over the aggregate's constituent objects.
11. `unknown` **is not** any of false, zero, unclassified, approved or erased.
12. Immutable past serving evidence **is not** current serving authority.

---

## 9. Routes: Bundle → Layer → Finding → Question → Artifact → permitted Action

**Bundles:**

- **B1 Package Proposal**
- **B2 Joint Review**
- **B3 Serving Boundary** (host binding)
- **B4 Retention and Disposition Interface** (deferral)

| # | Bundle → Layer | Finding | Question | Artifact | Permitted action |
|---|---|---|---|---|---|
| 1 | B1 → Membership | Exact membership | Is every member one object at one revision? | Proposal.members | `validate` (reject if not) |
| 2 | B1 → Membership | Aggregate admission | Is this composite a declared aggregate object? | aggregate_decl_ref | Reject, or require the aggregate's own review |
| 3 | B1 → Shape pins | Profile conformance | Does each projection meet SingleObjectProjection? | 003 policy_version + fingerprint | `validate` |
| 4 | B1 → Shape pins | Schema drift | Does any permitted path fail to resolve, or does an unknown path appear? | Template vs source schema | Reject / new proposal |
| 5 | B1 → Labels | Pinned scheme | Is every field label bound to a pinned scheme version? | permitted_fields.bindings | Reject if unpinned or unknown |
| 6 | B1 → Labels | Multi-scheme | Do all applicable schemes and compartments carry bindings? | bindings set | Reject if any scheme is missing |
| 7 | B1 → Audience/purpose | Purpose declared | Is purpose coded against a pinned purpose scheme? | purpose | `validate` |
| 8 | B1 → Evidence | Instrument reference | Which WM-XCT-002 instrument versions are relied upon? | access_instrument_refs | Record only |
| 9 | B2 → Composition | Differencing | Can a recipient subtract members to isolate an individual metric? | Review.considered_channels | `conclude` with verdict |
| 10 | B2 → Composition | Repeated release | Do prior packages to this audience enable differencing over time? | prior_release_refs | `conclude` / `rejected` |
| 11 | B2 → Validity | Invalidation | Did membership, revision, audience, purpose or shape change? | Digests | Mark `invalidated` |
| 12 | B2 → Validity | Expiry | Has `valid_until` passed? | Review | Mark `expired` |
| 13 | B3 → Freshness | Atomic snapshot | Are grant, revision, labels and holds read from one host state? | host_state_token | `serve` or `Unavailable` |
| 14 | B3 → Response | Denied vs missing | Can the recipient tell denial from absence? | RecipientResponse | Constant-shape `Unavailable` |
| 15 | B3 → Response | Diagnostics split | Where do the internal reasons go? | InternalDiagnostic → host audit | Write internally only |
| 16 | B3 → Caches | Cached copy | Is a cached package still servable after revocation or reclassification? | Cache entry + snapshot | Re-authorize on every read |
| 17 | B4 → Roles | Custody split | Does every artifact role have a retention/hold state? | retention_refs / hold_refs | `validate` |
| 18 | B4 → Conflict | Competing instructions | Hold active and delete requested, or two schedules disagree? | Unresolved-disposition block | Set `needs-owner`; stop-serving only if the host decides |
| 19 | B4 → Disposition | Evidence of disposal | Was disposal executed and verified, and what tombstone remains? | Host ref only | Record the reference; never assert erasure |

---

## 10. Acceptance profiles

### Startup

- **Setup.** One project Meta-Object with fields `name` (public) and `budget` (internal). The proposal has one member at `object_revision = r7`, `permitted_fields = {/name}`, purpose `partner-announcement`, audience one partner.
- **Schema drift.** A new field `/codename` appears. It fails I2 because it isn't in the set, so it's never emitted. Schema version `v3 → v4` makes the template fingerprint mismatch, and the package is `Unavailable`.
- **Denied request.** The partner asks for `/budget`. They get the same `Unavailable` bytes as for a non-existent project (I6). The internal diagnostic records `field-not-permitted`.
- **Review.** The joint review for a single-member package still exists but is trivial: channels `existence` and `error-shape` considered.

### Matrix group

- **Setup.** Two summaries: A is "Division total", B is "Division minus Team X". Each is a separate aggregate Meta-Object with its own owner and projection, and each was individually approved.
- **Proposal.** The proposal puts both into a package for legal-entity audience E2. The review considers `subtraction/differencing`, finds A − B isolates a 2-person team's metric, and returns `rejected` or `cleared-with-conditions: suppress B`.
- **Invalidation.** Any change to membership, B's revision, audience (E2 → E3), purpose, or shape triggers I4, and a new review is needed.
- **Real composite.** A real composite ("Division report") is created as a **new aggregate object** with its own calculation, owner and review. It is not a Projection over A and B.
- **Limit.** Clearing the package doesn't prevent a recipient combining it with **external** data. The review states `none-mathematical`.

### AI organization

- **Setup.** A model-release Meta-Object with public `release_notes` and restricted `eval_details`.
- **Purpose-limited package.** Contains `eval_details` for an auditor with `valid_until = T`.
- **Reclassification.** At T−1 day, eval details are reclassified: a new WM-XCT-020 binding revision. The host sees `binding_revision ≠ pinned`, so new reads, **including reads of cached copies**, return `Unavailable`.
- **Custody.** The earlier serving audit entry stays immutable. It is evidence of what happened, not current authority. Source history, the derived cache, the package output, the review evidence and backups each have a separate `retention_refs` role and possibly different custodians.
- **Recipient copies.** Copies already delivered to the auditor are **not** claimed to be erased. Any obligation to delete or return them sits with WM-XCT-002's duties and termination propagation.

---

## 11. Correction, idempotency, rights, conflict, round-trip, migration and disposal limits

- **Correction.** Proposals and reviews are never edited. A correction is `supersede` (new proposal) or `withdraw` plus a new review. Changing a status never changes a digest.
- **Idempotency.** Submitting the same canonical proposal twice gives the same `proposal_digest`. The host may dedupe but must still mint a lineage ID or return the existing one. `serve()` is **not** idempotent across time, by design.
- **Rights.** The companion holds no grants. Revoking a WM-XCT-002 instrument takes effect at the next `serve()` snapshot. Unauthorized reviewer writes are rejected by the host's authority check, not by the companion.
- **Conflict.**
  - Classification: multiple bindings on one field are all required. A downgrade by one authority doesn't override a binding from another.
  - Policy: ODRL's own default for conflicting rules is `invalid`. The companion takes the analogous stance and treats any unresolved conflict as `Unavailable` / `needs-owner`, not as a winner.
  - Retention: see §12.
- **Round-trip.** Canonical serialization and digest must round-trip across JSON and YAML. A canonicalization scheme must be declared; RFC 8785 JCS is a candidate, **not retrieved in this study**. Encodings are projections of one record; the digest is computed over the canonical form only.
- **Migration.** Changing `companion_schema_version` never re-signs old records. Old reviews bound to old digests simply stop applying. Migration tooling may emit new proposals that reference the old ones via `supersedes`.
- **Disposal limits.** The companion can at most (a) mark a proposal withdrawn and (b) report retention and hold refs.
  - Separate states: stop-serving (host), schedule (records owner), legal hold (legal owner), delete request, execution, verified disposition (e.g. NIST 800-88-style sanitization evidence, host-owned) and minimal tombstone.
  - A tombstone of the proposal and review (IDs, digests, dates, verdict) may outlive the content, subject to its own retention ref.

---

## 12. Strongest counterexamples, and how the boundary holds

| Counterexample | Risk | Response |
|---|---|---|
| **Nested paths and metadata leaks** | `/team` is permitted, so `/team/members[*]/salary` comes along. Array lengths, ETags, `updated_at` or key order leak facts. | Only single-node normalized paths (003 `de-path-normalized-form`); recursive descent is forbidden. A parent path doesn't include its children. Every metadata item is a field in the closed set (I2). |
| **Unknown labels** | New field with no binding is treated as "unclassified", i.e. public. | Unknown and not-yet-classified mean `Unavailable` (I7). |
| **Multiple schemes / compartments** | Field is `public` under scheme S1 but `export-controlled` under S2. | Bindings for **every** applicable scheme are required. Whether compartments combine conjunctively is decided by the host PDP. The companion only proves the labels were pinned. |
| **Joint inference** | A − B isolates an individual. | Explicit review with `subtraction/differencing`. No mathematical claim. The composite becomes its own aggregate object. |
| **Repeated releases** | The same package is released monthly, and the deltas reveal a join or departure. | `prior_release_refs` plus `repeated-release` channel. Rolling releases need a review per release, since each has a new membership digest. |
| **Stale decisions** | Review cleared, then the grant was revoked, but a cached "permit" is still served. | I5: re-authorize inside the snapshot on every read. Without an atomic snapshot, the decision carries `limited(max_age)` and the diagnostic says so. |
| **Replay** | An identical proposal is replayed after revocation. | Same digest, same `validate` result (I10), but `serve()` re-evaluates current state, so the result is `Unavailable`. |
| **Concurrent host updates** | Revision changes between the label check and the grant check. | One `host_state_token` for all checks. On mismatch, retry or `Unavailable`. |
| **Cache and recipient copies** | Reclassification doesn't reach copies already delivered. | Host caches are re-gated. Recipient copies are only covered by WM-XCT-002 duties. **No universal erasure is claimed.** |
| **Competing hold / erase** | Legal hold active while an erasure request is pending, or schedules of 3y and 7y. | Restricted **unresolved-disposition** block → `needs-owner`. No date is picked and no deletion happens. Purview's "retention wins" and "longest wins" (secondary evidence) and S3's rule that a hold outlives retention are **host policies the owner may choose**, not rules imposed by the companion. S10 shows even vendors differ: GCS event holds reset the clock, temporary holds don't. |
| **Classification downgrade** | Downgrade from restricted to public widens old packages retroactively. | A downgrade is a new binding revision, so old proposals no longer apply (I4). It needs a new proposal and review, and old packages are never re-issued automatically. |
| **Denied vs missing** | 403 vs 404, error text, timing or payload size reveal existence. | I6 constant-shape `Unavailable`. **Timing is not fully controllable** by the companion and is recorded as a residual channel that the host must accept or mitigate. |
| **Cedar-style "error means skip"** | A buggy forbid policy is skipped, silently widening access. | Host binding requirement: any evaluation error in a gating policy maps to `Unavailable` (Indeterminate ≠ Permit). |

---

## 13. Minimum useful profile (v0.1 boundary)

- **Value mode:** `metadata-only` or `closed-synthetic`. No live customer values.
- **Exported types:** Proposal, Review. PackageMember is a value type.
- **Profiles:** SingleObjectProjection (of WM-XCT-003) and a pinned-scheme classification profile (of WM-XCT-020, **non-executable until 020 publishes a spec digest**).
- **Host binding:** the `serve()` contract, snapshot, constant-shape response, internal diagnostics.
- **Deferred:** RetentionConstraint (WM-XCT-035), runtime enforcement engine (WM-XCT-038 not located), policy governance (WM-KNW-012 not located), statistical floors (WM-XCT-005 legacy only), classification scheme model.
- **Not claimed:** inference prevention, anonymization, IAM, legal interpretation, live deletion.

---

## 14. Retrieval and verification limits

1. **Hashes not verified by me.** My fetch tool returns model-generated summaries, not raw bytes, so I couldn't hash `spec.yaml`. The published pages show *synthesis* hashes that differ from the spec digests you supplied. That's expected (different artifacts), but it means the byte-level verification rests only on Codex's 2026-09-21 check.
2. **Both Vercy specs were truncated** in my retrieval. WM-XCT-002 ends in Layer 3.1; WM-XCT-003 ends inside `applicability-conditions`. Field names I quote are from summaries and may be paraphrased. The holds, facet sections and later layers of both specs were **not seen**, and parent holds are carried forward from your brief.
3. **WM-XCT-020:** page and spec summary only, truncated, no spec digest. **WM-XCT-035:** confirmed `todo`. **WM-XCT-005:** legacy entry only. **WM-XCT-038, WM-DAT-004, WM-KNW-012, WM-XCT-001** and the enterprise companions were **not located**.
4. **NIST SP 800-188:** the PDF couldn't be parsed, so I have no section numbers. **NIST 800-162, 800-88r2:** landing pages only. **XACML and ODRL section numbers** (†) are unverified against raw HTML.
5. **Microsoft Purview:** the primary page couldn't be processed. The precedence principles come from search snippets and are secondary.
6. **DPV:** edition conflict among 2.1 (2025-03-16), 2.3 (2026-02-25, where `w3id.org/dpv` now redirects) and the DPVCG homepage still showing v1. DPV is a Community Group report, not a standard. ODRL 2.2 is a W3C Recommendation. **No conformance to ODRL, DPV, NIST or XACML is claimed.** No ISO clause is cited.
7. From memory, not retrieved: RFC 8785 as a canonicalization candidate, and the general PAP/PDP/PEP/PIP pattern beyond the XACML summary.
8. No workspace was modified, nobody was contacted, and no publication is authorized.

Sources:
- [WM-XCT-002 spec](https://ver.cy/models/wm-xct-002-access-contract-consent/spec.yaml)
- [WM-XCT-003 spec](https://ver.cy/models/wm-xct-003-projection-disclosure-policy/spec.yaml)
- [WM-XCT-020 page](https://ver.cy/models/wm-xct-020-classification-binding/)
- [WM-XCT-020 spec](https://ver.cy/models/wm-xct-020-classification-binding/spec.yaml)
- [WM-XCT-035 page](https://ver.cy/models/wm-xct-035-retention-disposition/)
- [Vercy models catalogue](https://ver.cy/models/)
- [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
- [ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)
- [DPV 2.3](https://w3c-cg.github.io/dpv/2.3/dpv)
- [DPV 2.1](https://w3c-cg.github.io/dpv/2.1/dpv/)
- [DPVCG](https://www.w3.org/community/dpvcg/)
- [NIST SP 800-162 upd2](https://csrc.nist.gov/pubs/sp/800/162/upd2/final)
- [NIST SP 800-188](https://csrc.nist.gov/pubs/sp/800/188/final)
- [NIST SP 800-88r2](https://csrc.nist.gov/pubs/sp/800/88/r2/final)
- [XACML 3.0 Core](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html)
- [Cedar authorization](https://docs.cedarpolicy.com/auth/authorization.html)
- [OPA policy language](https://www.openpolicyagent.org/docs/policy-language)
- [AWS S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
- [GCS object holds](https://docs.cloud.google.com/storage/docs/object-holds)
- [Microsoft Purview retention](https://learn.microsoft.com/en-us/purview/retention)
- [The Purview Practitioner (secondary)](https://www.thepurviewpractitioner.com/learn/retention-precedence-four-principles)
