# EM-LEG-02 Independent Review — External norms and applicability

## Verdict

Reuse **WM-POL-001** as master for external norms. Create an **Enterprise external-requirement profile** over it. No new aggregate for `ExternalRequirement` or `NormVersion`: both are already WM-POL-001 structures (legal work; expression/consolidated view). `ApplicabilityAssessment` is a **profile of WM-ACT-034**, not a new aggregate. `Jurisdiction` is a **referenced external registry**; raise it as an identifier-unassigned candidate only if the Dimension has no place/jurisdiction master — do not mint it here. Boundary decision: **reuse + profile**, no new model IDs issued.

## Evidence

WM-POL-001 already owns legal-work/expression/manifestation/item/source/provision/norm identity, authority and legal basis, citation and version resolution, deontic assertions, lifecycle and amendment lineage, multi-axis time, and priority/derogation/exception/conflict assertions. Its `assess-applicability-as-assertion` function and the `time-applicability-jurisdiction-and-conflict` bundle cover the norm-side scope reading. WM-ACT-034 supplies every field this contour demands: version-pinned criteria binding, pinned subject state, scope and sampling with a generalisation limit, method and mode, evidence linkage, criterion outcomes with rationale, conclusion with decision authority and dissent, validity window with surveillance, assessor competence and impartiality, and a record state machine with correction, appeal and supersession. A second assessment aggregate would duplicate a 28-finding model.

## Identity/mastership

Five layers stay separable and singly mastered:

1. **Legal work** — the norm as an intellectual object, authority-qualified, stable across amendment. Master: WM-POL-001.
2. **Expression / NormVersion** — a dated, language-bound version, original or consolidated. `NormVersion` is an expression identifier, never a new type.
3. **Manifestation / source** — the file, gazette page or register copy, with authentication and copy status; availability is not authority.
4. **Provision** — the addressable fragment (article, paragraph, annex), stably identified across renumbering.
5. **Normalized norm identity** — the organization's stable key for "the same requirement" across amendments, derived from work + provision lineage, never from citation text, URL, title or hash.

`candidate_properties_from_v1.citation` (text) is therefore **candidate-not-normative and rejected as identity**; it is a rendered reference. The organization's interpretable rendering of a provision is a **WM-KNW-012** statement carrying `provision anchor`, `rendering fidelity attestation` and `expression form code` — it is not the norm and must not be stored as normative text.

## Legal source and versions

Every register entry pins work identifier, expression version, manifestation digest and provision locator, plus publisher and copy class (official / consolidated / unofficial translation). Consolidated views are derived artefacts recording applied modifications, cutoff and unresolved conflicts; they never carry the authority of the original act. Amendment, substitution, renumbering and correction are operations with their own authority and effect time. `effective_period` (interval) from LEG-03 is rejected as a single field: it collapses at least four axes.

## Temporal semantics

Six distinct axes, none derivable from another:

- **Publication / promulgation** — the act that makes the text public.
- **Entry into force / commencement** — may be provision-partial, later than publication, or conditional on a further instrument.
- **Efficacy / applicability** — when a provision actually bites on a class of subject; may postdate force or apply retroactively to facts.
- **Compliance / transitional deadline** — *not* a norm axis. It is an obligation due time (WM-XCT-029 `due basis` = event-derived) computed from a norm event plus an offset, with jurisdiction time zone and business-day convention retained.
- **Repeal / supersession / expiry** — with successor resolution; superseded text stays citable.
- **Record / knowledge time** — when the register learned, asserted or corrected the fact; separate from event time, per RFC 3339 with explicit offset.

## Exceptions and transitions

Four mechanisms, kept apart so source authority is not flattened:

- **Source exception** — drafted into the norm itself. Modelled as a provision with its own norm statement plus a typed override/exception edge to the provision it qualifies (WM-POL-001 `priority-override-derogation-exception-and-conflict-assertion`). No granting act exists; nothing is party-scoped.
- **Derogation** — a competent authority relaxes a norm for a class, under a power the norm confers. Source-authored where the enabling provision is cited; the relaxing instrument is itself a legal work.
- **Exemption** — a granted act naming a beneficiary, bounded in time and scope, with a granting authority distinct from the issuer and any compensating obligation (WM-KNW-012 `derogation-and-waiver-declaration`, `derogation-instrument`).
- **Transitional period** — a temporal scope on a provision's applicability, usually paired with a transitional obligation bearing its own deadline.

Prohibited: a boolean `exempt` or free-text `applicability_basis` on the requirement row. Exemption expiry changes the exemption's state, never the norm's version. Non-derogable provisions carry a floor that no exemption or local tightening may cross.

## Applicability assessment

A **profile of WM-ACT-034**, third-party or first-party as declared. Mandatory: pinned norm version **and** provision set; subject/activity/product/market references with pinned state; jurisdiction reference; **facts-as-of** instant, separate from assessment and record times; assessor identity, role, competence and impartiality declaration, with the deciding authority distinguishable from the determiner; reasoning per provision with cited evidence; conclusion type (applies / does not apply / applies subject to conditions / indeterminate); confidence and explicit limitations including the generalisation limit where a sample or a single market was examined; review or expiry instant with surveillance obligation; record status.

Scope split against WM-POL-001: the norm side owns **declared scope as read from the source** (territorial, personal, material, procedural). The assessment owns the **reasoned conclusion for a named subject**. One assessment never edits norm scope, and one norm never asserts a subject conclusion.

## Conflicting interpretations

Conflicting assessments **coexist as separate records**, never as versions of one record. Supersession operates only within a series by the same accountable authority for the same pinned inputs; a differing assessor, market, facts-as-of or norm version yields a new record, not an amendment. Divergence is registered explicitly — recorded alternatives, a named contradiction, a resolution owner and a deciding authority — and each record retains its own evidence and dissent. No engine collapses two conclusions into a majority, average or "current" answer. WM-ACT-034's effective-record flag is unsafe here until the series-root question in its adjudication is settled: two records can each claim effectiveness.

## Jurisdiction

Jurisdiction is a reference into a place/jurisdiction master, resolving territorial, sub-territorial and subject-matter extent, with the competent authority's effective period. `jurisdiction` as a bare code is candidate-not-normative: it cannot express sub-national divisions, extraterritorial connecting factors, or overlapping mandatory rules. Conflicting duties across jurisdictions are recorded as an unresolved conflict with a prevailing-rule basis, not silently resolved.

## Obligations and compliance

Obligations derive from provisions: each **WM-XCT-029** duty pins its source work, expression and provision, and carries obligor, action, conditions, due basis, fulfilment criteria and evidence. Three steps are distinct and none implies the next: **citation** (a reference exists) → **applicability** (a reasoned conclusion that the provision binds this subject) → **compliance** (an assessed state of conduct against each derived obligation, requiring fulfilment evidence and acceptance). The negative case — a statute reference proving corporate conformity — fails at both joins: no pinned applicability conclusion, no obligation-level fulfilment evidence.

## Scenario

A regulation is amended with a future commencement. The register holds E1 (in force) and E2 (published, not yet in force, partial commencement, one provision with a 24-month transitional period). Two market assessments are recorded against E2: Market A concludes "applies, conditions from Art. 7(2)"; Market B concludes "does not apply — activity outside material scope", each with its own facts-as-of, evidence, assessor and limitations. Both stay active; a contradiction record names the divergent provision and a resolution owner. Deriving obligations from E2 before its force instant yields due dates computed from commencement plus the transitional offset, and applicability conclusions dated against E2 do not alter E1's live obligations. Nothing auto-resolves; the model records, it does not decide.

## Invariants

1. A norm entry resolves to a verifiable source: work, expression, manifestation digest, publisher and copy class.
2. Citation text, title, URL, date or hash never identifies a norm.
3. Publication, force, efficacy, deadline, repeal and knowledge time are stored separately.
4. Every assessment pins norm version, provision set, subject, jurisdiction, facts-as-of and assessor.
5. Interpretation is attributable and never stored as the norm's text.
6. Consolidated and translated text is marked non-authoritative unless a competent authority declares otherwise.
7. Exemptions are bounded, beneficiary-scoped and granted by an authority distinct from the issuer.
8. Non-derogable provisions cannot be relaxed by exemption or local tightening.
9. Conflicting assessments coexist; supersession requires same authority and same pinned inputs.
10. Applicability never implies compliance; compliance requires obligation-level evidence.
11. Indeterminate conclusions are representable and never coerced to "does not apply".
12. Expired or superseded norm versions stay citable and are marked historic.

## Minimal completion shape

Register entry: norm work id + expression id + provision locator; issuing authority and legal basis; source manifestation with digest and copy class; six time axes; derived-obligation references; source-exception edges; granted-exemption references; jurisdiction references; normalized norm identity key; record and knowledge time. Assessment record: the eleven mandatory fields above plus status and conflict links. Derived internal rule: WM-KNW-012 statement with provision anchor and fidelity attestation.

## Holds

WM-POL-001 is a codex-only single-provider waiver, `publishableCanonical: false`, with no approved relation rows — all composition remains draft. WM-ACT-034 is Claude-only with an over-claimed access dimension, an empty relation ledger, an unratified parent link and a deferred supersession-chain decision. WM-KNW-012 carries an open boundary review. Jurisdiction lacks registry allocation. Source pins, crosswalks, jurisdiction-specific commencement, treaty and multilingual-authenticity profiles, and applicability fixtures remain unverified. Not an installable release; no canonical completeness claimed.
