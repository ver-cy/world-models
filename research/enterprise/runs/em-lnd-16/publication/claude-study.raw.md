# EM-LND-16 — Knowledge and Decision Landscape

## Verdict
Reuse + profile; **new = no**. EM-LND-16 is a governed enterprise landscape profile over WM-REC-001, WM-KNW-006 and WM-KNW-010, bound to WM-KNW-007, WM-KNW-008, WM-REC-010 and WM-KNW-018, layered on EM-KNW-01 and EM-KNW-02. It masters no subject fact. `KnowledgeLandscape` gets **declaration identity only** (its scope, review, authority and retrieval policies are asserted, not derivable). `DecisionDependencyView` gets **no independent identity**: it is a derived projection; only its closure/query specification and pinned release set are governed, so results are reproducible.

## Evidence
All three targets are `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`. Each `vercy_candidates` entry is `conceptual-candidate` at `index-and-publication-metadata` depth — publication is not crosswalk verification. WM-KNW-006 and WM-KNW-010 carry single-provider waivers; WM-REC-001 is dual-provider with source-verification holds. WM-KNW-010 explicitly excludes claim machinery and evidence items; WM-KNW-008 excludes the cited work itself; WM-KNW-006 assigns scheme membership to the parent. The landscape therefore sits over four masters that already refuse each other's content — the correct precondition for a view, and the wrong one for a new aggregate.

## Identity/mastership
One editable master per assertion; everything else is read-only projection.
- **Record identity, version chain, instantiation, custody, fixity, disposition** — WM-REC-001.
- **Concept identity, delimitation, designations, definitions, deprecation/successor** — WM-KNW-006.
- **Scheme release, membership, in-scheme relations, mappings** — WM-KNW-018 (EM-KNW-01 rule: if an assertion dies with the release, the scheme owns it).
- **Claim statement, scope, calibrated confidence, status** — WM-KNW-007.
- **Citation act: stance, locator, consulted representation, verification, source-status observation** — WM-KNW-008.
- **Decision content: question, alternatives, criteria, rationale, objections** — WM-KNW-010; **fixed issued expression, signature, service, finality** — WM-REC-010.
- **Landscape declaration** — EM-LND-16: `knowledge_scope`, `review_policy`, `authority_policy`, `retrieval_scope`, currently `candidate-not-normative` and requiring promotion or explicit local status.

**Gap:** the evidence *source work* has no registered master (EM-KNW-02 raised Evidence Artifact, identifier unassigned). Where the source is itself a governed record, bind through WM-REC-001; otherwise the landscape carries WM-KNW-008's non-authoritative descriptor and flags the reference unresolved.

## Semantic graph
Typed edges, each owned once: document→concept (classification binding: concept IRI + pinned scheme release; a label never classifies); claim→citation (binding role, stance, direction); citation→source (preferred citation identifier separate from access URI, plus consulted state); decision→claim (premise/conclusion role at pinned claim version); decision→citation (rationale grounding); decision→record (fixed expression); record→record (version/supersession); concept↔concept (broader/related/mapping); decision↔decision (supersession, follow-on).

**Relation ≠ identity.** `broader` is not part-of; `closeMatch` is not transitive and never promotes to `exactMatch`, `owl:sameAs` or record merge; a mapping records correspondence at two pinned releases, not interchangeability. **Evidence ≠ truth.** Citation type is rhetorical; certainty is an externally versioned scheme; no field in WM-KNW-007 may be read or projected as a truth verdict, and the landscape must not aggregate stance, certainty and weight into a score.

## Decisions and impact
Retraction of a shared source: WM-KNW-008 records a **dated status observation** (it does not issue the retraction), sets locator health and may raise contested/drift. The affected set = decisions whose rationale bindings resolve to citations referencing that source at the pinned representation state, traversed to their premise claims. Propagation is **notify-and-recheck, never auto-invalidate**: `dr-rsn-fn-recheck-assumption-and-sensitivity` annotates staleness; only a competent authority transitions status or reopens. Issued WM-REC-010 expressions stay resolvable and unaltered; change proceeds by successor decision and successor fixed expression. A rebutted claim behaves identically: WM-KNW-007 registers conflict **without adjudicating**; dependent decisions show premise support as asserted-stale, with dissent, objections and original rationale preserved append-only.

## Terminology conflict
Equal labels are not equal meanings. Detect via homograph disambiguation evidence — subject field plus delimiting characteristic — and report pairs whose designation matches while intension differs. Merging or resolving on label equality is forbidden. Two live tensions must be decided per Dimension and recorded: SKOS's one-preferred-label-per-language against terminology practice permitting several admitted terms; and the same concept carrying divergent scheme-scoped notations across releases. Output is a finding with both readings and their authorities, never a silent winner.

## Missing source and uncertainty
Three distinct absences, reported separately: a claim with no evidence binding; a citation whose locator does not resolve or lacks a preferred citation identifier; a decision reason with a dangling reference after disposition. Absence is recorded, not inferred — omitted and explicitly-null are different values, and *unknown*, *unsupported* and *refuted* are three states. Coverage is a quality measurement over a pinned release, never a confidence or truth figure.

## Rights and projections
Index identifiers, selectors, digests and permitted labels — not restricted excerpt text. Default is deny for record and excerpt content; existence-level metadata is readable unless a sensitive-item rule restricts existence itself. Redaction produces a new rendition with its own digest; selectors and fixity survive so re-verification stays possible; the source is never overwritten. **Inference non-disclosure:** derived closures, counts, co-citation and summaries can reconstitute withheld content, so every derived result inherits the most restrictive constituent label and any suppression is marked rather than silently dropped. WM-KNW-006's person-naming and licensed-definition exceptions operate below its four declared access scopes — an open amendment hold the profile must state, not paper over.

## Time/version/scenario
Every edge pins a version: claim version, scheme release, record version and expression, consulted representation with access datetime, decision release. Event, effective, observation and ingestion times stay separate, RFC 3339 with seconds and explicit offset; note the divergence between WM-KNW-006's local prohibition of `-00:00` and WM-REC-001's use of it for unknown offset — the Dimension must choose one. Landscape answers are **as-of** queries: as-of-decision-time and as-of-now yield different affected sets, and both must be reconstructable from pinned releases. Scenario is a decision scope qualifier, not a branch of the graph.

## Acceptance scenario
A source cited by two decisions is retracted. Each citation gains its own dated observation and verification report; the source-work reference is not rewritten. Both decisions appear in the affected set with the traversal path shown. One reopens and issues a successor; the other's authority records that it remains effective — the view reports both without deciding. Restricted correspondence cited by one decision is never revealed: its existence, citation identifier and stance may be visible to entitled roles, its excerpt is not.

**Negative case (must fail):** a retrieval summary that paraphrases restricted correspondence is a disclosure, even with no quotation and no link. The generated abstract inherits the correspondence's label, the summary is withheld, and where existence is itself protected the result is absent with the omission marked — not softened, not partially rendered.

## Invariants
1. A semantic relation never establishes identity, equality or merge authority. 2. Evidence carries scope, stance, certainty scheme and consulted state, and never asserts truth. 3. Third-party and personal rights survive indexing, derivation and aggregation. 4. One editable master per assertion; all cross-model views are read-only. 5. History is append-only; retraction and rebuttal never erase rationale, dissent or fixed expressions. 6. Absence is recorded explicitly, never inferred. 7. Identifiers are never reused; disposed nodes leave resolvable tombstones.

## Minimal profile shape
Landscape declaration (four policies, promoted or marked local); pinned release set; edge-type register naming the owning model per type; closure/query specification with an as-of parameter; disclosure-label propagation rule covering derived results; absence-and-uncertainty report shape; loss declaration for every projection. No runtime identifier is minted for `DecisionDependencyView`.

## Holds
Crosswalks unverified at index-and-publication-metadata depth. Single-provider waivers on WM-KNW-006, WM-KNW-010, WM-KNW-007, WM-KNW-008, WM-KNW-018; source/version holds on WM-REC-001. Relation ledgers do not register the required edges (WM-KNW-010 composition-contract hold; WM-KNW-007 argumentation placeholder rejected; WM-KNW-018/WM-XCT-020 parent direction unresolved). Evidence Artifact master unassigned. WM-KNW-006 access-scope amendment and lifecycle downgrade outstanding; WM-KNW-008 deduplication key unbound; timestamp-offset divergence unresolved. The contour's three blocking decisions remain open. This is a research checkpoint: not canonically complete, not installable.
