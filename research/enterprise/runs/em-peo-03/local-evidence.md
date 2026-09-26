# EM-PEO-03 local synthesis

## Disposition

- Complete reserved WM-PER-009 as the definition master for scheme-scoped Skill and Competency concepts.
- Treat Skill and Competency as distinct typed profiles sharing one governance pattern, not aliases or separate roots.
- Propose identifier-unassigned **Proficiency Scale** and **Person Capability Assertion** roots.
- Profile Competency Assessment on WM-ACT-034.
- Reuse WM-PER-008 for Qualification and WM-XCT-017 for Credential, with WM-PER-013 as the professional-licence profile.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Skill/competency definition, scale version, mapping assertion, person capability assertion, assessment event/result, evidence, qualification definition/award, licence, credential and role expectation remain distinct.

Scheme authorities master definitions and scales. Assessors master assertions. Awarding bodies, issuers and regulators master awards, credentials and licences. HR systems master local records and assertions, never external scheme definitions.

## Skill and competency definitions

WM-PER-009 must own scheme/version-qualified concept identity, language-tagged labels, definition, concept type, composition, context, applicability, deprecation, successor lineage and lossy crosswalks.

Skill denotes an atomic ability. Competency composes knowledge, skill and applied behaviour in a context. Both use the same identity/lifecycle pattern but preserve type semantics. Human competency never shares identity with WM-KNW-005 AI-agent instruction packages.

## Scales and mappings

A Proficiency Scale is reused across concepts and evolves independently. It owns a versioned ordered level set, descriptors, measurement level and successor lineage.

Mappings pin source and target scheme/scale versions, authority, direction, purpose, strength and semantic loss. ESCO, SFIA and local levels never gain exact equivalence merely because labels or numbers match.

## Person capability assertions

A Person Capability Assertion states that one person holds one competency at a level on a scale, according to an asserter, basis and interval. It pins competency and scale versions, evidence, assurance and revalidation/decay rules.

It remains external to the person master and assessments. Self-declared, assessed, credential-derived and observed bases stay distinct.

## Assessment and evidence

Competency Assessment profiles WM-ACT-034: pinned criteria, method, coverage, outcome scale, decision rule, evidence linkage, criterion results, conclusion, assessor competence, impartiality, review, validity and immutable finalization.

Self-assessment is a first-party assessment profile and never becomes verified evidence. Missing, indeterminate and not-applicable results never collapse to zero.

## Qualification, credential and licence

WM-PER-008 already separates participation, completion, achievement, qualification definition, personal award, credential and recognition. WM-XCT-017 owns issued credential identity, secured representation, verification, status, expiry, suspension, revocation and renewal. WM-PER-013 specializes professional licences.

Issuance, technical verification, current validity and present competence are separate judgements. Expiry never destroys historical issuance.

## Role and course boundary

WM-ORG-004 owns competency and credential requirements for a position. A requirement is not an assertion about an occupant. Course completion records participation/completion and never establishes proficiency or expertise.

## Acceptance result

“Secure code review” is assessed by a manager on local 1–5 scale v2 at level 4 and independently by work sample on an SFIA-aligned scale at level 4. Both results remain final and distinct. Their mapping is partial and purpose-limited, with declared loss; equal numerals imply no equivalence. An expired certificate retains its issuance fact but creates no current-competence assertion. Scale v3 supersedes v2 without rewriting prior results.

## Required invariants

1. Definition is not holding.
2. Concept identity is scheme/version-qualified.
3. Level is meaningless without a scale version.
4. Assessment states scale, method, assessor and date.
5. Final results are not recomputed against later scales.
6. Self-declared and verified assertions stay distinct.
7. Mappings declare loss and never invent exact equivalence.
8. Course completion never implies proficiency.
9. Credential expiry preserves issuance history.
10. Credential validity is not current competence.
11. Role expectation is not a person assertion.
12. Human competency and agent instruction never share identity.
13. Missing assessment is unknown, not zero.

## Holds

WM-PER-009 now has a reviewable completion candidate for scheme-scoped definitions, composition and lossy mappings, with three external relation contracts and seven fixtures. Its purpose and owner no longer conflate a person capability assertion with a system function. Proficiency Scale and Person Capability Assertion remain unallocated. ESCO, SFIA, CTDL, CLR, Open Badges and VC crosswalks still require pinned verification; exact Grok comparison, one frozen semantic audit, package conversion and live verification remain required. No installability claim is made yet.
