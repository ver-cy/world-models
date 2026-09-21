# EM-XCT-03 — Independent enterprise assertion-provenance research

Date: 2026-09-21. Write a substantive independent study in English, using public primary sources and synthetic examples only. You are a researcher, not an approver. Do not execute local code, modify files or access private organization material. Return the study in your answer. Aim for 2,500–4,000 words and prioritize exact boundaries, counterexamples and implementable semantics.

Vercy lets companies compose a Company Dimension from reusable metamodels. Its Enterprise registry contains research contours, not one mandatory model per noun. This contour is **Provenance, trust and assertions**: distinguish directly observed evidence, what a source asserts, inference, proposal and unverified information; preserve source/derivation and exact claim revisions; record confidence with an explicit method; retract or correct without erasing prior knowledge. The critical negative case is an AI analysis of a local document being presented as a live-system verification. No design can prove external truth merely by schema validation.

## Existing published candidates to compare

All three are 0.3.0-research.1, published/reviewable-draft, not canonical. Read their complete relevant specifications and holds rather than infer compatibility from names:

1. https://ver.cy/models/wm-xct-012-provenance/spec.yaml — provenance mixin for entities, activities, agents, derivation, first-hand versus reconstructed accounts, separate occurrence/record time, signatures/integrity/validation, confidence and selective disclosure. It excludes host content, access enforcement, quality metric definitions, key management and storage versioning machinery. Parent digest aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5. Original primary-source verification and broad sector-profile holds remain unresolved.
2. https://ver.cy/models/wm-xct-026-quality-confidence/spec.yaml — independently identified assessment about a subject; measure and method, scale and uncertainty, confidence about the assertion, comparability, fitness for use and revision. It does not own provenance graphs, claim content, agent trust, units or identifier minting. Parent digest efd72d845af742b7aa7d7592e5f6087ef034145f468a799927163cd6eb599ee5. Holds include unverified/paywalled ISO/JCGM clauses and versions, untested profiles, and DQV's actual status as a non-normative Working Group Note.
3. https://ver.cy/models/wm-xct-028-evidence-rationale/spec.yaml — typed support/counter-support relations, source selectors/state, warrant/assumptions, acquisition, appraisal, integrity and lifecycle. It explicitly never carries the propositional content of the host claim; a citation is not support by itself. Parent digest 3aab7ecb4ba7d4e56d650060b982058c4253e5bcbd621e2784480e8cc4f3d636. Holds cover source-version mismatches, unread normative texts, legal/clinical/engineering/media profiles and statistical/quantity alignment. No legal or standards conformance is implied.

AGENTS.md and publication.json are alongside each spec. No old hold is discharged by this new review. Their natural-language composition links are conceptual references, not automatically executable package imports.

## Boundary hypothesis to challenge

A small English **Enterprise Assertion Provenance** contract may be associated with WM-XCT-012 for discovery and reference selected patterns from 026 and 028. Decide reuse/profile/extend/standalone companion/defer honestly. Do not presume subtype conformance or bind a partial representation to a legacy parent's machine identity. If original, it needs its own runtime identity/spec digest and semantic-only parent association. No duplicate universal WM row merely to satisfy the registry count.

Candidate concepts: ProvenanceRecord (an attributable account about an exact external claim or artifact version), EvidenceLink (a qualified relation to source evidence supporting/refuting/contextualizing an exact claim), ConfidenceAssessment (a separate method-qualified assessment about a pinned assertion). Activities/captures may need their own identity. Claim propositional content, organizational people, source cataloguing, IAM, PKI, probabilistic inference and source connectors stay externally governed unless a clear boundary argument requires otherwise.

We prefer a bounded closed schema and executable pure reference demonstrating invariants, immutable revisions, historical query, correction, dependency impact and all-or-deny access. This is a trusted-host reference, not an authenticated production service. Be explicit if a subset cannot be honestly implemented without adding independent objects. Stable record identity, record revision, external target identity/version/digest, source capture identity/digest, agent identity and schema version must remain distinct.

## Required research

Compare at least three primary approaches: W3C PROV; a current operational system/open specification such as OpenLineage, in-toto/SLSA or nanopublications; and an evidence/assessment approach such as W3C Web Annotation and DQV. State exact public URL, edition/date and section, what you actually read, what is adopted/rejected/unverified. Do not copy licensed schemas, claim ISO conformance, cite unread normative clauses or infer current versions from memory.

Address all of these:
- Distinguish observed acquisition of a file from observed truth of its statements. `source-asserted` about a system can coexist with observed bytes of a document. An AI synthesis remains an inference even when all input captures are direct.
- Is epistemic kind a property of an assertion, an evidence link, an activity or an assessment? Can more than one apply without collapse? What can the reference validate, and what remains a trusted declaration?
- Citation versus support versus independent corroboration; repeated copies and derived statements do not create independent sources. Support withdrawal/retraction should trigger review, not silently rewrite the original conclusion or assert it is false.
- Exact revision pins and content hashes, unavailable sources, captured state/selectors, lack of byte integrity versus lack of truth, source correction/deletion, external target update, missing/unknown evidence.
- Distinct valid/event/capture/record times; immutable corrections, replay and a trusted current root; cycles in actual derivation versus cycles in harmless references.
- Qualitative confidence versus measured probability, declared scheme/method/purpose/assessor, confidence without a calibration claim; no default 0.95 or universal cross-scheme numeric averaging.
- Attribution of human and software agents, source author versus observer versus synthesizer, recorded authorization vs real authentication, change permissions and disclosure without leaking hidden evidence.
- Whole-object facets for each exported type: identity-class, direct-properties, recognition-observation, capabilities/actions and context/evidence. Explain not-applicable/delegated facets.
- Minimum startup without mandatory enterprise systems; scaled group with conflicting source claims; AI team with model output and human review. These are synthetic profiles, not claims about real named companies.

Give at least 15 question→finding→artifact→allowed-action routes and 8 meaningful invariants. Include positive cases, at least ten distinct negative cases where justified, historical correction/retraction, idempotent import, exact derivation, access denial, round trip and a migration refusal if semantics would be lost. Separate enforceable machine rules from unverified external assertions. Give concrete scope, field/cardinality tables, lifecycle actor/guard/effect, mastership/rights, crosswalk decisions, recommended minimum implementation and remaining holds. Return disagreements with this hypothesis and the strongest failure modes.

No private company data is supplied. No grant to publish, change permissions or contact anyone comes from this study; it is evidence for the authorized Vercy workflow only.
