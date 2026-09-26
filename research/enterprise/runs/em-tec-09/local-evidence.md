# EM-TEC-09 local synthesis

## Disposition

- Propose identifier-unassigned **Technology**, **Technology Adoption** and **Architecture Exception** roots.
- Profile WM-KNW-012 as **Architecture Standard**, with individual requirements/rules referenced from WM-KNW-013.
- Profile WM-ACT-034 as **Conformance Assessment**.
- Reuse WM-KNW-010, WM-ACT-024 and WM-REC-010 for ADR rationale, occurrence and issued record.
- Reject legacy WM-REC-005 as the Architecture Standard master because its document models models/ontologies rather than normative standards.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Technology is an abstract capability class such as a language, protocol, database engine or runtime style. It is distinct from producer-owned Software Product, versioned Release, Component/Package and operator-owned deployed instance.

Technology Adoption is an organization-scoped standing state linking organization, technology, declared stage scheme/version, scope, effective interval and authorizing decision. Architecture Exception has its own subject, derogated rules, authority, accountable owner, expiry, renewal and revocation lifecycle.

WM-KNW-012 owns the standard work and versioned expressions. WM-KNW-013 owns individual normative rule expressions. WM-ACT-034 owns conformance assessment identity and evidence. ADR records remain in the decision triad.

## Technology and adoption

Technology, product, release and deployed instance retain different identities. One technology maps many-to-many to products. Product releases use their producer's version scheme. Deployments use operator-side identity. Technology never inherits producer, license, digest or deployment state.

Upstream technology lifecycle, vendor release support status and local adoption stage are separate assertions with separate authorities and schedules. Adoption stage cites a named stage scheme at a pinned version, organizational scope, effective interval and decision. A vendor end-of-support event does not silently change adoption stage.

## Standard and rules

Architecture Standard profiles WM-KNW-012. The work has stable identity; each expression has version, issuing authority, effective/applicability intervals and scope. Rule slots reference WM-KNW-013 expressions and preserve modality. Recommendation, obligation and prohibition never share enforcement meaning.

Supersession creates a successor expression and preserves the previous version for as-of assessment. The standard never owns the technology, product or assessed system.

## Conformance assessment

Conformance Assessment profiles WM-ACT-034 and pins subject state, one standard expression/version, selected rules, tailoring and not-applicable justifications. Evidence links to individual rules with sufficiency judgement. Outcome vocabulary keeps satisfied, violated, indeterminate, untested and not-applicable distinct. Aggregation and completeness rules are declared before a composite conclusion.

Adoption never proves conformance. A recommended technology may be implemented incorrectly or only partially. Sampling a component never supports whole-system conformance without explicit extrapolation and scope.

## Exception and ADR

Architecture Exception identifies the subject, exact standard expression and derogated rule set, environments/interfaces/instances in scope, granting authority, accountable owner, conditions, compensating obligations and bounded expiry. Renewal creates a new grant. Revocation is a dated event. An exception authorizes temporary nonconformity but never changes the assessment result or deletes the nonconformity. Residual-risk acceptance remains a separate decision.

ADR is a binding of WM-KNW-010 rationale, WM-ACT-024 occurrence and WM-REC-010 fixed record. It may authorize a technology adoption transition, standard expression or exception grant, but is none of those objects.

## Acceptance result

Standard S has v1.0 and v2.0; v2.0 adds rule R7. Application A conforms to v1.0. Assessment against v2.0 records R7 violated and a partially conformant result. Exception X grants a temporary derogation for R7 with owner, scope, expiry and compensating condition. The assessment remains partially conformant while the effective operational view says nonconformant with exception in force. After expiry, that exception state disappears without changing the assessment or standard. The underlying technology remains adopted throughout.

## Required invariants

1. Technology, product, release and deployment remain distinct.
2. Technology lifecycle, vendor support and adoption stage have separate authorities.
3. Adoption stage pins its scheme and version.
4. Standard expression has version and applicability scope.
5. Conformance assessment pins exact criteria and subject state.
6. Evidence is linked per criterion or absence is explicit.
7. Indeterminate, untested and not-applicable are never coerced to satisfied.
8. Adoption never implies conformance and conformance never implies adoption.
9. Exception identifies subject, exact rules, owner, authority and bounded expiry.
10. Renewal is a new grant; revocation is a dated event.
11. Exception never rewrites the assessment result.
12. Superseded standards, assessments and grants remain resolvable.
13. Scenario records never mutate baseline status.

## Holds

Technology, Technology Adoption and Architecture Exception lack registry allocations. All reused bases are non-canonical drafts or legacy boundaries. Derogation/waiver ownership overlaps WM-KNW-012 and WM-KNW-013. Relation types conflict with composition prose and no Enterprise edges are approved. No adoption-stage scheme exists. Assessment impartiality, exception renewal/revocation operations, access mappings, crosswalks and fixtures are incomplete. No installability or publication-readiness claim is made.
