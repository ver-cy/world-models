# EM-XCT-01: Enterprise identity links. Bounded independent study memo

**Status:** research proposal, not a publication. I ran no tests, changed no files and published nothing.

## 0. What I actually read

All sources were read through a fetch tool that turns each page into markdown and returns a summary written by a smaller model. The quotations below are what that tool returned. **They need to be checked against the raw bytes before anyone cites them normatively.**

| Source | URL / section | How much was inspected |
|---|---|---|
| WM-XCT-011 spec | ver.cy/models/wm-xct-011-identifier-scheme/spec.yaml | **Partial.** Bundles 1–2 had field-level detail (layers 1.1–1.4, 2.1–2.3). The document cut off inside Bundle 3 ("Assignment, State and Continuity"). The last field id visible was `de-registration-revised-at`. For assignment records I saw only their outline: assigner, evidence, effective period, use modifier `usual/official/temp/secondary/old`. I did not see the state vocabulary codes. |
| WM-XCT-011 AGENTS.md | …/AGENTS.md | Header only: version, reviewable-draft, "do not claim canonical completeness while `researchAdjudication.publicationHolds` is non-empty", "preserve source references, master-system identity and access rules". |
| WM-XCT-036 spec | …/wm-xct-036-alias-same-as-mapping/spec.yaml | **Partial.** Scope and exclusion statements, plus the identity layer fields `assertion_id`, `envelope_version`, `host_record_ref`, `supersedes_ref`, `structural_key`. Invariant: "a change to any claim-bearing field is made by issuing a successor envelope… never by editing in place." It cut off inside the identity layer. |
| WM-XCT-036 landing page | …/wm-xct-036-alias-same-as-mapping/ | **Partial.** I saw 8 of the 27 bundles declared in the metadata and 20 layer ids. It listed nine relation kinds (`identifier-alias`, `historical-identifier`, `referent-replacement`, `exact-semantic-match`, `close-match`, `equivalent-in-context`, `probable-entity-match`, `not-same-assertion`, `strict-identity`) and value-state codes (`asserted`, `derived`, `absent`, `explicitly unknown`, `undetermined`, `unassessed`). It did not give a clean lifecycle-state enumeration or the definitions of the relation kinds. It cut off at `als-prop-find-warrant-confidence`. |
| WM-XCT-036 AGENTS.md | …/AGENTS.md | Header only. |
| WM-XCT-040 README | …/wm-xct-040-model-composition-resolution/README.md | Summary level: exact pins (version + SHA-256 + size of spec and AGENTS.md), `requires` vs `references`, semantic-only vs native-binding readiness, nested snapshots needing a closed data schema plus a separate domain validator, new Dimensions only. Snapshot-binding rules were not visible. |
| OWL 2 Structural Specification | w3.org/TR/owl2-syntax/ §9.6.1 SameIndividual, §9.6.2 DifferentIndividuals, §9.5 HasKey | The section summaries only. |
| SKOS Reference | w3.org/TR/skos-reference/ §10.1, §10.3 (S42, S44, S45), §10.6.8 | Mapping section only. |
| RFC 7643 (SCIM Core Schema) | rfc-editor.org/rfc/rfc7643 §2.2, §3.1, §4.1.1, §4.1.2 | Those sections. The emails schema in §8.7.1 was not visible. |
| RFC 3986 | §1.2.2, §6.1, §6.2.1–6.2.4 | Those sections. |
| RFC 5321 | §2.4 (local-part case) | That paragraph. |
| PROV-DM | w3.org/TR/prov-dm/ §5.1.1, §5.1.3, §5.1.8, §5.2.2, §5.5 | Definitions only. |
| W3C Reconciliation Service API v0.2 | w3.org/community/reports/reconciliation/CG-FINAL-specs-0.2-20230410/ §4.1, §4.2 | Candidate and query structures. This is a Community Group report, **not a W3C Recommendation**. |
| OpenRefine manual | openrefine.org/docs/manual/reconciling | The sections on matching, bulk match and discarding judgments. |

I did not consult ISO standards, FHIR R5 directly, SSSOM, or the private research branch cited by the models. FHIR and SSSOM appear here only through WM-XCT-036's own citations.

## 1. Verdict in one paragraph

The proposed shape is basically right: a **profile of WM-XCT-036**, with identifier qualification delegated to **WM-XCT-011**, and no new model. It has one flaw that decides the design. **The resolution status (`candidate / contested / accepted / unknown`) is not a property of a single assertion.** It depends on the whole set of assertions touching an identifier or subject, the policy, and two points in time. A snapshot bound to a single assertion therefore cannot honestly carry that status.

The status also does not need its own mutable aggregate. My recommendation is to define **IdentityResolution as a deterministic, non-persisted query contract**: a pure function over (bindings, assertions, policy, valid-time, knowledge-time) that returns an explanation. Human adjudication of a contest is recorded as **another IdentityAssertion** from an adjudicating authority, not as a resolution record. A persisted resolution aggregate should wait until someone needs cached or materialised views, and then it should be a derived artefact with a digest of its inputs.

The profile should use a **star topology**. Every link runs from a qualified source identifier to a Dimension-local subject reference, and the profile has no identifier-to-identifier links. The only derivation this allows is one hop ("A and B both point at P"). Unbounded transitive closure never has to happen.

## 2. Five things that must not be conflated

| Concept | What it is | Source anchor | In this profile? |
|---|---|---|---|
| **Global logical equality** | `owl:sameAs` / SameIndividual. Everything true of one individual becomes true of the other. Symmetric and transitive, with no context. | OWL 2 §9.6.1 | **No.** Never stored or exported. |
| **Mapping assertion** | An identified claim by an issuer, for a purpose, within a Dimension and a time window, that two references are related by a named relation. SKOS keeps `closeMatch` non-transitive "to prevent compounding errors", while `exactMatch` is transitive (S45). | SKOS §10.1, §10.3; WM-XCT-036 scope | **Yes.** This is IdentityAssertion, with a contextual relation (`equivalent-in-context`), not `strict-identity`. |
| **Match candidate** | Output of a matcher: an id, a score and a boolean `match` meaning the service "considers this candidate good enough". The client decides. OpenRefine: "human judgment is required to review and approve". | Reconciliation API §4.2; OpenRefine manual | **Only as evidence.** Imported candidates become assertions in `proposed` state and never activate by themselves. |
| **Resolver decision** | The answer to "what does identifier X denote, as of (v, k), under policy π?" | None of the sources defines this. It is our construct. | **Yes, as a derived query** (§5.4). |
| **Destructive merge** | Endpoint records are rewritten or collapsed into a golden record and one side's identity is lost. | Excluded by WM-XCT-036 | **Out of scope.** No reversible contract has been shown. |

**The trap:** OpenRefine's "also use the same identifier for all other cells containing the same original string (two checkmarks)" is exactly the operation that would merge two different "J. Smith"s or two users of one shared mailbox. The profile must make that operation impossible to express as a single act. Each binding needs its own assertion.

## 3. Boundary table (decision per candidate)

| Candidate | Decision | Reason |
|---|---|---|
| **IdentifierBinding**: a source system's qualified identifier (scheme, issuer, tenant scope, as-received and canonical value) assigned to a source-local record for a period | **Profile of WM-XCT-011** (the Bundle 3 assignment record, plus layer 1.3 fields `canonical-identifier-value`, `as-received-identifier-value`, `permitted-comparison-level`) | WM-XCT-011 already owns qualified assignment, effective period, reuse and reassignment. **Hold:** I could not read the Bundle 3 field ids, so the mapping is only outlined. |
| **IdentityAssertion**: "binding B denotes Dimension subject P, valid [v1, v2), under warrant W" | **Profile of WM-XCT-036** that restricts relation kinds, endpoint shape and lifecycle | WM-XCT-036 owns the envelope, issuer, purpose, Dimension, time, evidence, dispute, retraction and conflict recording. The profile narrows it; it does not extend it. |
| **Negative assertion** ("B does *not* denote P"; "P1 ≠ P2") | **Profile of WM-XCT-036** (`not-same-assertion`) | This is what blocks collapse on a shared name or mailbox. DifferentIndividuals (OWL 2 §9.6.2) is the logical analogue, but here the claim is contextual. |
| **IdentityResolution** | **Derived query contract inside the profile. Persisted aggregate deferred.** | See §1. A status that depends on a set of assertions cannot live on one assertion, and storing it mutably would add a second, drifting source of truth. |
| **Adjudication of contested links** | **Reuse IdentityAssertion**, issued by an adjudicating authority, with an `adjudicates` reference set | This keeps a single claim type. WM-XCT-036 "records conflicts without resolving them", so a decision has to be a new claim. |
| **Warrant / authorization to assert** | **Reference only.** The warrant is an external record the profile checks for validity. The profile never grants or enforces access. | WM-XCT-036 excludes authorization decisions. Checking that a *warrant exists* is evidence, not enforcement. |
| **Subject (Person, ServiceAccount)** | **Out of scope, reference only** | Minted by a person/agent model. WM-XCT-011 also excludes "the referent itself". |
| **Matching engine** | **Out of scope** | Excluded by both WM-XCT-011 and WM-XCT-036. |
| **Merge, split, reassignment of endpoints** | **Out of scope** | No reversible contract. A split is expressed by retracting spokes and asserting new ones to P2; P is never rewritten. |
| **Global sameAs export** | **Out of scope** | It would turn contextual claims into context-free equality (OWL 2 §9.6.1). |

## 4. Source-backed design principles

1. **Qualify before comparing.** RFC 3986 §6.1 aims to "minimize false negatives while strictly avoiding false positives". WM-XCT-011 layer 1.3 has `permitted-comparison-level`. A binding value is compared only within its scheme and issuer, and only at the level the scheme declares.
2. **Normalize per source, never universally.** RFC 5321 §2.4: "The local-part of a mailbox MUST BE treated as case sensitive." SCIM `externalId` is `caseExact: true` (RFC 7643 §3.1). Lowercasing is allowed only where the scheme says so. Examples are the RFC 3986 host (§6.2.2), a Git host's login rule if documented, or ARK's rules as cited in WM-XCT-011. There is no Unicode folding and no "same email means same person".
3. **Keep source authority separate from assertion authority.** SCIM `id` is "unique… as defined by the service provider… non-reassignable". `externalId` uniqueness "is controlled by the client" and is **not enforced by the server** (§3.1). So the source system is authoritative for *which record* the identifier names. It is not authoritative for *which person* stands behind that record. The Dimension's identity steward is the assertion authority.
4. **Identification does not grant access.** RFC 3986 §1.2.2: "access to the resource is neither guaranteed nor implied." Resolving a link discloses nothing about the endpoint's attributes.
5. **Records are immutable; supersede or invalidate them instead of editing.** PROV-DM §5.1.1 (entities have fixed aspects), §5.2.2 (revision), §5.1.8 (invalidation is "the start of the destruction, cessation, or expiry"). This matches WM-XCT-036's successor-envelope rule. Retraction is an invalidation event on a retained entity, not a deletion.
6. **A matcher's `match: true` is not a decision.** Reconciliation API §4.2. Scores are service-specific: "each service calculates scores differently" (OpenRefine). Scores are stored as uncalibrated evidence.

## 5. Minimum schema and lifecycle

### 5.1 IdentifierBinding (profile of WM-XCT-011 assignment)

| Field | Card. | Notes |
|---|---|---|
| `binding_id` | 1 | Deterministic: a hash of (`scheme_ref`, `issuer_ref`, `tenant_scope`, `canonical_value`, `assignment_start`, or `assignment_start_unknown`). Makes imports idempotent. |
| `scheme_ref` | 1 | WM-XCT-011 `scheme-registry-key` |
| `issuer_ref` | 1 | The issuing system instance, e.g. HR tenant or Git host org |
| `tenant_scope` | 1 | Subsidiary, org or workspace. Never inferred. |
| `as_received_value` | 1 | Exact bytes as received |
| `canonical_value` | 1 | Only by the scheme's `canonicalization-rule-set` |
| `referent_kind_claimed_by_source` | 0..1 | e.g. `user-account`, `service-account`, `mailbox`, `commit-author-string`. This is the source's claim, not ours. |
| `assignment_valid` | 1 | `[from, to)`, each end with a value-state: `asserted`, `absent`, `explicitly-unknown` |
| `source_record_ref` | 1 | Pointer to the immutable source evidence |
| `recorded_at` | 1 | Knowledge time |
| `content_digest` | 1 | Separates a re-import (same digest, no-op) from a conflicting revision |
| `disclosure_class` | 1 | The binding may itself be personal data |

### 5.2 IdentityAssertion (profile of WM-XCT-036 envelope)

| Field | Card. | Notes |
|---|---|---|
| `assertion_id` | 1 | Disjoint namespace (WM-XCT-036 invariant) |
| `supersedes_ref` | 0..1 | Successor-envelope chain |
| `dimension_ref` | 1 | Scope. No cross-Dimension effect. |
| `purpose` | 1 | e.g. `workforce-identity-linking` |
| `source_endpoint` | 1 | A `binding_id` or a subject reference (the latter only for negative subject-subject assertions) |
| `target_endpoint` | 1 | Dimension subject reference P, with a subject kind (`person`, `service-account`, …) |
| `relation` | 1 | Profile enum: `equivalent-in-context` (denotes, positive), `not-same-assertion` (negative), `probable-entity-match` (candidate only, never activates). All other WM-XCT-036 kinds are excluded, `strict-identity` above all. |
| `valid_time` | 1 | `[from, to)` with a value-state on each end |
| `issuer_ref` | 1 | The assertion authority, a person or role |
| `warrant_ref` | 1 unless relation = `probable-entity-match` | External authorization record: its own period and status |
| `authority_rank` | 1 | Taken from policy at issuance. Needed to decide equal-authority conflicts. |
| `evidence_refs` | 1..n | For `equivalent-in-context`, this must include at least one piece of non-matcher evidence |
| `confidence` | 0..1 | With `method_ref`. Treated as uncalibrated unless calibration is referenced. |
| `adjudicates` | 0..n | Assertion ids this decision resolves |
| `recorded_at` | 1 | Knowledge time |
| `disclosure_class` | 1 | |

**Cardinalities.** A binding has 0..n assertions. At a given (v, k), under a given policy, a binding has **at most one accepted positive target**; if more than one survives, the result is `contested` (invariant I4). A subject may have many bindings (star). Negative assertions can occur 0..n times.

### 5.3 Lifecycle (append-only events on the assertion)

`proposed → active → {disputed ↔ active} → {retracted | superseded | expired}`

- **`active` is a derived status.** It is gated by the warrant being valid at `recorded_at` and not disputed, and by the evidence rule being met. An assertion that fails the gate stays `proposed` and never turns active by itself.
- A lifecycle event is a separate immutable record: `event_id`, `assertion_id`, `kind`, `actor`, `reason`, `recorded_at`, `effective_from`. A retraction is a PROV-style invalidation. It removes the assertion from views with knowledge time ≥ `recorded_at`. Views with an earlier knowledge time still see it.
- **Correction** (the valid time was wrong) is done with `superseded` plus a successor envelope. It is never an in-place edit.
- **Tombstone** exists only for legally mandated erasure. It removes the payload and keeps `assertion_id`, the event chain and the reason, so history queries report "redacted" rather than silently changing. This depends on a disclosure/erasure policy that sits outside this profile.

### 5.4 IdentityResolution (derived query contract)

`resolve(binding | subject, valid_at v, known_at k, policy π, requester_dimension d) → {status, targets[], supporting[], opposing[], excluded[{assertion, reason}]}`

1. Take the assertions in Dimension `d` with `recorded_at ≤ k`, no invalidating event at or before `k`, and `v` inside `valid_time`.
2. Drop any assertion whose warrant is not valid at its `recorded_at` or is disputed at `k`. Record each one in `excluded` with the reason.
3. Positive assertions naming a single target, with no active negative against that target → `accepted`.
4. Two or more distinct targets at the highest `authority_rank` present, or a positive and a negative at equal rank → `contested`. An `adjudicates` assertion of higher rank decides the contest.
5. Only `probable-entity-match` present → `candidate`.
6. Nothing present → `unknown`. This is not "no link"; negative knowledge comes only from `not-same-assertion`.

The function is deterministic, has no side effects and discloses nothing beyond the ids of assertions in the same Dimension.

## 6. Invariants

- **I1. Qualification.** No binding exists without `scheme_ref`, `issuer_ref` and `tenant_scope`. Values are compared only within the same (scheme, issuer, tenant) and only at the scheme's permitted comparison level.
- **I2. No universal normalization.** `canonical_value` must be derivable from `as_received_value` by the scheme's declared rule set. Any other transformation is invalid.
- **I3. Endpoint non-mutation.** No IdentityAssertion event changes a binding, a subject or a source record. Retracting every assertion leaves the endpoints byte-identical.
- **I4. Functional resolution.** An `accepted` result has exactly one target; anything else is `contested` or `unknown`. The resolver never picks one of several equal-rank targets silently.
- **I5. Candidates are inert.** `probable-entity-match`, a matcher score, a shared email or name, or a Git author string can never on its own produce `accepted`.
- **I6. Warrant gate.** A positive assertion whose warrant is expired, revoked or disputed at `recorded_at` never becomes active.
- **I7. Append-only history.** For every k₁ < k₂, `resolve(…, known_at=k₁)` gives the same result whether it runs before or after later events.
- **I8. Idempotent import.** Importing an identical payload twice produces no new record. A different payload under the same natural key produces a conflicting-revision record and never an overwrite.
- **I9. Dimension confinement.** An assertion affects only resolution in its own `dimension_ref`. A cross-Dimension reference yields no endpoint attributes and no access.
- **I10. Subject-kind integrity.** A binding whose source `referent_kind` is `service-account` cannot be accepted onto a `person` subject, and the reverse also holds, unless an explicit override assertion with a stated reason exists. Even then it gets its own negative-case review.
- **I11. No closure beyond one hop.** The profile allows no identifier-to-identifier or subject-to-subject positive links. "A ≡ B" is only ever derived as "A→P and B→P, both accepted at (v, k)".

## 7. Semantic-negative cases (all must be rejected or yield the stated non-`accepted` result)

1. HR `E1042`@SubA and HR `E1042`@SubB are linked because the value is equal. **Rejected (I1).** The tenant scopes differ.
2. `J.Smith@corp.example` and `j.smith@corp.example` are canonicalized to the same value although the scheme does not declare local-part case-insensitivity. **Rejected (I2, RFC 5321 §2.4).**
3. A Git author string "Jane Doe" becomes an accepted link to Person P on a score of 0.97. **Result is `candidate` (I5).**
4. A shared mailbox `ops@` is linked to two Persons. **Result is `contested` (I4)**, and with a `referent_kind` of `mailbox` the policy should prefer a `not-same-assertion`.
5. Service account `ci-bot` in Git is accepted onto the human who created it, because they share an email. **Rejected (I10, I5).**
6. An assertion is issued under a warrant that expired the day before. **It stays `proposed` (I6).**
7. The warrant is disputed after issuance. **At a knowledge time after the dispute, the assertion is excluded with reason `warrant-disputed`. Earlier knowledge-time queries are unchanged (I7).**
8. Retraction implemented as a row delete. **Invalid (I7).** A historical query would change.
9. Correcting a valid-time end date by editing the envelope. **Invalid.** It must be a successor envelope (WM-XCT-036).
10. A link in Dimension D1 causes Dimension D2's resolver to return Person P's HR attributes. **Invalid (I9, RFC 3986 §1.2.2).**
11. An absent `valid_to` stored as `9999-12-31`, or an unknown `valid_from` stored as epoch. **Invalid.** Use the value-states `absent` or `explicitly-unknown`.
12. An `unknown` result read as "different person". **Invalid.** Only `not-same-assertion` carries negative knowledge.
13. Re-importing the same HR export creates duplicate bindings. **Invalid (I8).**
14. A rehired employee number reassigned to a new hire, with the old period's links extended to the new hire. **Invalid.** A different `assignment_start` gives a different binding (I1, I8).
15. Exporting accepted links as `owl:sameAs`. **Invalid.** The profile has no export path for this (OWL 2 §9.6.1 semantics).

## 8. Scenario traces (synthetic)

**S1. Startup.** Bindings: `hr:acme-hris/acme/E7` (from 2025-03-01), `git:gh/acme-org/u:jdoe-acme`, `it:linear/acme-ws/usr_9f`. The steward S has warrant W1, the "identity steward" role, valid 2025-01-01 → open. S issues A1, A2 and A3 as `equivalent-in-context` to `person:acme/P-001`. The evidence is the onboarding ticket plus the IdP provisioning log. At k=2026-02-01, `resolve(git binding)` → `accepted`, P-001.

On 2026-03-10 S finds that the Linear account `usr_9f` belongs to a contractor who shares a display name with P-001. S records a retraction event on A3 and a new A4: `not-same-assertion` between `usr_9f` and P-001.
- `resolve(linear, known_at=2026-03-01)` → `accepted`, P-001, supported by A3. History is retained.
- `resolve(linear, known_at=2026-03-11)` → `unknown`, with A3 in `excluded: retracted` and A4 in opposing.

No binding or Person record was touched, and no ERP or MDM system is involved. The setup needs three binding rows, four assertion rows and one event.

**S2. International group.** HR `E1042` exists in both `hr:group-hris/SubA` and `hr:group-hris/SubB`. They are distinct bindings (I1), linked to P-A and P-B respectively.

P-A leaves SubA on 2024-06-30 and is rehired on 2025-02-01 under a new number, `E3310`. SubA reassigns `E1042` to P-C from 2025-09-01. That gives two bindings for `SubA/E1042` (assignment starts 2019-… and 2025-09-01), each with its own assertion.
- `resolve(SubA/E1042, valid_at=2024-01-01)` → P-A.
- `resolve(SubA/E1042, valid_at=2025-10-01)` → P-C.
- P-A's star now holds `E1042(old)` and `E3310`.

The mailbox `finance@subA` is linked by SubA's steward to P-A and by the group steward, at equal rank, to P-D. The result is `contested`, with both assertions listed. A later higher-rank `adjudicates` assertion issues `not-same-assertion` for both links and classifies the mailbox as shared.

A link from the group Dimension to a SubB Dimension subject returns only ids. SubB's HR attributes are not disclosed (I9).

**S3. AI organization.** `git:gh/ai-org/u:train-bot` has source `referent_kind: service-account`. A matcher proposes it for Person P-7 because the commit email equals P-7's email: `probable-entity-match`, score 0.99. The result is `candidate`. An attempt to accept it is rejected by I10. The correct model is a `service-account` subject SA-3 with a separate ownership relation, which belongs to a different model.

A steward whose warrant W9 expired on 2026-05-31 issues an assertion on 2026-06-02. It stays `proposed` (I6). A reissue under a new warrant W10 activates. W10 is then disputed on 2026-07-01. Queries with known_at ≥ 2026-07-01 exclude the assertion (`warrant-disputed`); earlier ones still show it.

## 9. Competing approaches and tradeoffs

| Approach | Strength | Why it is not the first profile |
|---|---|---|
| **owl:sameAs graph with a reasoner** | Standard, and gives closure for free | Context-free, transitive equality. One wrong link merges clusters and retraction needs truth maintenance. Both models exclude closure. |
| **MDM golden record with survivorship** | Operationally familiar | A destructive merge. It rewrites endpoints, fails I3 and makes reversal lossy. |
| **SCIM-style `externalId` on the Person** | Trivial | One slot per client. The server does not enforce uniqueness (RFC 7643 §3.1). There is no evidence, time or dispute. |
| **Pairwise identifier-to-identifier links (SSSOM-like)** | Direct and matcher-friendly | Needs closure to answer "who is this?" and turns every error into a cluster merge. The star keeps the blast radius to one spoke. |
| **Persisted cluster / resolution aggregate** | Fast reads and a stable cluster id | A second source of truth that drifts, and bitemporal views have to be re-materialised. Defer it; allow it later as a digest-pinned derived cache. |
| **Star of contextual assertions to a Dimension subject (recommended)** | Reversible per spoke, bitemporal, explainable | Needs a subject to be minted *before* linking (a bootstrapping cost). A "subject split" means re-pointing many spokes, which is noisy but lossless. |

There is also a competing definition of **"accepted"**. The strict reading is "at least one active positive and no active opposition". The looser reading is "a majority weighted by rank". I recommend the strict reading plus explicit adjudication. The looser reading hides disagreement, and hidden disagreement is exactly what an identity steward needs to see.

## 10. Five whole-object facets

| Facet | IdentifierBinding | IdentityAssertion | Resolution result |
|---|---|---|---|
| **Identity** | Deterministic `binding_id` from the natural key | `assertion_id`, disjoint namespace | Not an object. Identified by the (inputs, policy, v, k) tuple. |
| **Temporality** | Assignment valid time + `recorded_at` | Valid time + `recorded_at` + event times | Evaluated at (v, k) |
| **Authority / mastership** | Mastered by the source system (issuer) | Mastered by the Dimension identity steward (warrant) | Mastered by nobody; derived |
| **Lifecycle** | Immutable; superseded by a conflicting revision | proposed / active / disputed / retracted / superseded / expired / tombstoned (restricted) | None |
| **Disclosure** | `disclosure_class`; personal data | `disclosure_class`. The link itself reveals cross-system correlation. | Only ids from the same Dimension. Never grants attributes. |

## 11. Questions (research contour)

1. Does WM-XCT-011 Bundle 3 already have an assignment-start field fit for use in the natural key? It wasn't visible.
2. Is WM-XCT-036's `equivalent-in-context` defined as "denotes the same referent within the context", or as concept-level equivalence?
3. Does WM-XCT-036 allow an endpoint that is a *binding* rather than a bare identifier locator?
4. Is the warrant checked at `recorded_at` only, or continuously? This memo proposes issuance time, plus explicit dispute for later problems.
5. Who ranks authority, and is rank a property of the warrant or of the policy?
6. Can an adjudication itself be contested? This memo says yes: a higher rank or another adjudication.
7. How are tombstones for erasure reconciled with I7? The proposal is for history queries to report "redacted".
8. Is `referent_kind` the source's claim, or a Dimension classification?
9. Where do subjects get minted, and by which model?
10. What minimum evidence does a positive link need? One non-matcher item, or two?
11. Should `unknown` be split into `never-assessed` and `assessed-no-link`?
12. How is a Git author string with no account qualified? Its scheme is the repository, and it is not an identifier with assignment semantics.
13. Does the policy object belong to WM-XCT-036 (warrant/conflict) or to a separate governance model?
14. Can SubB legitimately assert about a group-level subject? That is a cross-Dimension issuer.
15. What is the retention period for superseded envelopes?
16. Is there a need to bound the valid time on `not-same-assertion`, for example "different until rehire"?
17. How are bulk imports of legacy merges represented without auto-activation?
18. Does WM-XCT-040's companion validator run the resolve function, or only the record invariants?

## 12. Migration

- **Legacy `person.email` / `person.github_login` columns:** generate bindings, then generate `proposed` assertions with evidence `legacy-column` and the issuer set to the migration job. Nothing activates until a steward re-issues under a warrant.
- **Legacy MDM merges:** record each merged pair as a `proposed` assertion with evidence `legacy-merge:<id>`. Do not unmerge the source.
- **Existing WM-XCT-036 envelopes:** these are valid if their relation falls within the profile's three kinds and their endpoints can be bound. Envelopes using `strict-identity` are rejected, not coerced.
- WM-XCT-040 applies to new Dimensions only. Existing Dimensions need a manual composition.

## 13. Minimum executable profile and publication form

- **Form:** "EM-XCT-01 Enterprise Identity-Assertion Profile". It is a **profile** that `requires` WM-XCT-036@0.3.0-research.1 and WM-XCT-011@0.3.0-research.1, pinned by SHA-256 and size through WM-XCT-040. It is not a new model and does not add to the catalogue count.
- **Readiness:** semantic-only at first. Native binding comes later, only for the two record types, with closed schemas.
- **Executable core:** three closed record schemas (binding, assertion, lifecycle event); a companion validator for I1, I2, I3, I6, I8, I10 and I11; a reference `resolve()` implementation for I4, I5, I7 and I9. Section 7's 15 negative cases and section 8's 3 traces become fixtures, not yet executed.
- **Status:** reviewable-draft.

## 14. Unresolved holds

- **H1.** I read WM-XCT-011 and WM-XCT-036 only in part (see §0). The field mappings to Bundle 3 and to WM-XCT-036's lifecycle and relation definitions are **unverified**.
- **H2.** Relation-kind semantics for `equivalent-in-context`, `not-same-assertion` and `probable-entity-match` come from an id list, not from their definitions.
- **H3.** WM-XCT-036's historical Claude-only waiver and its 108 unverified sources remain. This bounded study does not fix them.
- **H4.** The SCIM emails schema characteristics (§8.7.1) were not visible.
- **H5.** Primary sources were read through a summarizing tool. Quotations need verbatim checks.
- **H6.** The Reconciliation API is a Community Group report and is non-normative.
- **H7.** The erasure/tombstone interaction with I7 needs a disclosure-policy owner.
- **H8.** Subject minting and service-account ownership are owned by other models that were not examined.

## 15. My main design objections

1. **"Resolution returns a status" cannot sit on a single-assertion snapshot.** Binding status to one assertion misstates `contested` and `accepted`, which are properties of a set. Either keep resolution as a derived query, as recommended here, or accept a separate derived aggregate. A hybrid is not honest.
2. **A mapping to a "canonical subject" is still equality in disguise.** The star limits the damage, but a derived "A ≡ B" view is a one-hop closure. The profile must say so openly and keep that view from ever leaving the Dimension.
3. **Reusing WM-XCT-036 imports its unresolved breadth.** The profile's narrowing is only as trustworthy as the parent definitions I could not fully read. Publication should wait for H1 and H2.
4. **Warrant checking comes close to authorization.** Checking warrant validity is evidence handling, but a policy engine that ranks authority is governance logic that neither model owns. It needs a named owner, or it will be smuggled into the validator.
5. **Rehire and reassignment rely on assignment-start data that source systems often don't have.** Without a reliable start date, the natural key degrades, and `explicitly-unknown` starts risk producing false-positive idempotence. This needs field evidence from real HR exports, used under synthetic substitution.
6. **Split is "out of scope", but its alternative isn't free.** Retract-and-reassert is lossless but gives no atomic, auditable "this was one operation". A later study may need a grouping event, which is not a merge primitive.

**Sources:**
- [WM-XCT-011 spec](https://ver.cy/models/wm-xct-011-identifier-scheme/spec.yaml) · [AGENTS.md](https://ver.cy/models/wm-xct-011-identifier-scheme/AGENTS.md)
- [WM-XCT-036 spec](https://ver.cy/models/wm-xct-036-alias-same-as-mapping/spec.yaml) · [AGENTS.md](https://ver.cy/models/wm-xct-036-alias-same-as-mapping/AGENTS.md) · [landing page](https://ver.cy/models/wm-xct-036-alias-same-as-mapping/)
- [WM-XCT-040 README](https://ver.cy/models/wm-xct-040-model-composition-resolution/README.md)
- [OWL 2 Structural Specification](https://www.w3.org/TR/owl2-syntax/)
- [SKOS Reference](https://www.w3.org/TR/skos-reference/)
- [RFC 7643](https://www.rfc-editor.org/rfc/rfc7643.html) · [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html) · [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321.html)
- [PROV-DM](https://www.w3.org/TR/prov-dm/)
- [W3C Reconciliation Service API v0.2 (CG report)](https://www.w3.org/community/reports/reconciliation/CG-FINAL-specs-0.2-20230410/)
- [OpenRefine: Reconciling](https://openrefine.org/docs/manual/reconciling)
