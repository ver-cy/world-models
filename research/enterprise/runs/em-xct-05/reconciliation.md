# EM-XCT-05 — provider reconciliation and bounded candidate

Status: Codex synthesis of two completed independent research studies, 2026-09-21. This is not an implementation audit or installation claim. The original Claude response, original Grok DOCX, mechanical extraction, browser summary and provider manifests are separate evidence. Both received the same public brief; neither received the other's findings. Grok's document identifies its own internal team/model; the browser exposed Heavy, not a independently verifiable backend model ID.

## Agreement adopted

Both providers recommend two independently identified records: **ContextPackageProposal** and **JointDisclosureReview**. The package contains bounded, embedded single-object members. A separately attributed review assesses the exact package, audience, purpose, environment and known prior-release context. This can help a company prepare an exchange or review a dashboard before its own systems authorize and deliver it.

The four registry candidates are dispositioned: DisclosurePolicy uses existing shape/policy concepts by reference; ClassificationAssignment uses the existing classification-binding pattern by reference; RetentionConstraint is deferred to a responsible custodian with explicitly unresolved references; ProjectionContract becomes the narrow original companion. No executable parent import or claim of subtype conformance is made. A new universal WM identity is unnecessary.

First implementation scope: **metadata-only proposal and review validation**. No source values, transformation, serving operation, grant evaluation, classification assignment, inference proof, retention scheduling or deletion engine. Internal metadata and diagnostics require host authorization and can themselves be sensitive. A positive result means only that a declared review is applicable under the supplied trusted snapshot and selected profile.

## Disagreements and corrections

| Issue | Raw proposal | Adopted decision and reason |
|---|---|---|
| Package versus projection | Grok §3.1 restricts the package to one primary object; other objects enter the review. Claude embeds multiple single-object members. | Adopt Claude's containment. The package is an explicitly identified collection, each member identifies one source object. Do not force a dashboard to masquerade as one projection. |
| Domain aggregate versus risk review | Grok's matrix example calls the review the real aggregate. | Reject. A JointDisclosureReview is an assessment record, not a compensation report or another calculated domain aggregate. A source aggregate needs its own identity, owner, calculation and lineage before it can be a member. |
| Circular identities | Grok makes proposal→review mandatory and review→proposal mandatory. | Review references a frozen proposal; the proposal does not contain its future review. Additional reviews can coexist without changing what was assessed. Business links do not become cyclic package imports. |
| Self-referential digest | Claude's suggested digest exclusions omit the digest field itself. Grok leaves canonicalization underspecified. | Hash an explicitly named document with the digest field removed. Include identity, revision, type/version and body. Named restricted JSON encoding, no claim of RFC 8785 conformance. |
| Mutable status and replay | Both studies sometimes equate a replayed proposal with the same current review result. | Immutable content is reproducible; applicability also depends on exact current snapshot, time, withdrawal and governance profile. A review verdict remains historical while its present applicability can change. |
| Conditional approval | Claude permits clearance with conditions that can suppress members. | A condition that changes membership or shape creates a new proposal and a new review. The first validator accepts only an unconditional bounded verdict, or returns an unresolved result; it never silently rewrites the package. |
| Retention delegation | Both correctly report 035 unfinished; Grok facet prose nevertheless labels retention execution delegated to it. | No executable delegation, pin or invented fields for 035. Host-owned references are opaque evidence; a missing schedule is unknown, not no obligation. Hold and schedule do not authorize disclosure or destruction. |
| Evidence identifiers | Grok sometimes reduces classification to scheme/version/code. | Preserve exact binding identity/revision/digest, subject/field and pinned scheme/term context. Reference equality does not establish that an assignment is substantively correct or authoritative. |
| Review independence | Both import an unconditional separate-reviewer constraint from DRB practice. | Profile-controlled segregation of duties. Startup self-review is explicit, not impersonated independent review. More demanding profiles require a different authorized reviewer. No NIST conformance claim. |
| Concurrent change | Both allow a validity window as an alternative to atomic delivery checks. | A bounded age alone does not close the check-to-delivery race. This validator has no delivery operation. Any future serving adapter needs a proved atomic freshness boundary or an explicitly weaker contract. |
| Nested paths | A closed allowlist can still select an entire object subtree. | First prototype accepts only named top-level scalar-leaf declarations from a closed host catalog. No arrays, wildcards, graph expansion or generic JSONPath. Even scalar strings can disclose information; the code proves no privacy property. |
| Recognition/observation facets | Grok treats proposal recognition as unpinned identity delegation and review recognition as not applicable. | Both records have local observation context: source capture, review evidence, assessment scope and timestamps. Host object identity resolution remains external. No undocumented identity-model delegation. |
| Source coverage | Claude missed available 020/DAT-004/KNW-012 bytes. Grok fetched summarized/truncated parent YAML. | Codex compared complete local/live bytes for five available semantic neighbors, read boundary/holds and selected exact findings. These checks do not validate all inherited citations, runtime adapters or production readiness. |
| Purging evidence | Grok calls tombstone destruction usually forbidden. | Unsupported as a universal rule; reject. Record retention/disposal needs the actual custodian and applicable policy. No general legal determination. |
| School classification | Grok labels SP 800-188 a records-disposition source and gives uneven retrieval detail for NARA/Cedar. | Use 800-188 for disclosure/de-identification governance only. The separate Codex source-verification record grounds adopted claims in five directly checked primary sources, including storage-version/hold behavior. No unverified legal or Cedar claim is needed. |

The earlier `claude-study-assessment.md` remains the fuller critique of that provider. This reconciliation does not edit either raw response.

## Frozen design direction for the prototype

The proposal has a qualified Dimension and record identity/revision, author, capture time, audience pin, purpose pin, environment pin, prior-release-context pin, custody-context pin and a finite non-empty ordered member set. Each member carries its own key, one source-object revision/content pin, a source-schema pin, one output-shape pin and a finite non-empty ordered field set with exact classification-binding pins. All members are metadata about the review scope. No payload is loaded or returned.

The review has its own qualified identity/revision, exact proposal pin, reviewer, authority/evidence/method pins, assessment and validity times, verdict, residual-risk note and optional supersession reference. A rejection and an inconclusive assessment are valid historical records. A declared clearance is neither a grant nor a proof of safe inference. Unknown evidence cannot become clearance by default.

The host supplies a separate current snapshot: Dimension, current proposal context and member pins, eligible proposal/review writers, current review-authority pin, withdrawn review pins and the chosen segregation profile. Current reference changes, withdrawal, future/expired review, missing catalog entries, mismatched audience or a rejected/inconclusive verdict prevent an applicable-clearance result. Conflicting active reviews require explicit owner resolution; no last-writer-wins behavior.

Snapshots and authorities are trusted inputs. The reference will not authenticate the caller, prove snapshot completeness, verify source content or perform network I/O. Use a restricted internal caller capability before giving any diagnostic. Recipient-facing uniform-denial integration belongs to the host; merely returning a constant string in a unit test would not prove absence of timing/existence leakage.

## Work remaining

Implement the exact schema, cross-record validator, lifecycle/idempotency rules and synthetic startup, matrix and AI fixtures. Complete whole-object/mastership matrices and all question routes against that code. Run separate frozen Claude and Grok implementation audits. Then select an immutable release ID/version, test native V3 binding, publish and verify the runtime/catalogue. None of those steps is retrospectively completed by these studies.
