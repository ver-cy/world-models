# Grok memo: Codex boundary decisions before structured synthesis

Provider evidence: exact browser memo `grok.review.md`, 2026-09-21. This file is Codex analysis, not Grok output. Claude has not yet been read. No provider vote is treated as authoritative.

Accepted design contributions:
- Independent case identity scoped to work context and review period; Person, Employment, Membership, Assignment and Organization remain referenced masters.
- Separate versioned rating instrument, evidence quality and attribution, explicit calibration before/after, independent recognition event, and factual correction versus opinion contest.
- Preserve conflicting evidence and correction provenance. Reject a portable intrinsic person score, activity-count scoring, and automatic employment decisions.
- A new employer does not inherit the former employer's confidential review master. Any permissible transfer is a separately authorized, purpose-limited projection.
- HR Open EPM is interchange precedent; SFIA/ESCO are vocabulary and capability neighbors; neither proves appraisal fairness or standard conformance.

Corrections required before accepting Grok's proposed structure:
1. Its table says 0..n employments but exactly one governing employment for every case. Make employment conditional on the employee profile. A contractor, volunteer or pre-incorporation founder must be representable through an explicit work-context/authority reference without fabricating Employment.
2. Its universal RatingScaleVersion=1 and startup 3-4 point scale force quantified grading. A narrative-only or objectives-only profile is valid: scale 0..1; a numeric/ordinal assessment requires exactly one immutable scale version.
3. AssessmentAct 1..n is wrong for an empty draft. Make 0..n, with state-dependent guards for issuance. Objective-free feedback is permitted only under an explicit profile.
4. CalibrationAct 0..1 prevents re-calibration after an appeal. Use an ordered 0..n act history; a session may reference multiple cases, without acquiring ownership of them.
5. Position and membership are not universally single-valued. Work-context bindings carry their own cardinality, role and valid time. Do not collapse concurrent roles.
6. Dates and correction identifiers must distinguish a new revision of the same case from a new case. R1b is a revision/issued-outcome ID, not automatically a second case identity.
7. An attribution share is a claim with a declared denominator and method, not an automatic 50/50 split or evidence of IP ownership. Unknown and disputed shares remain valid; duplicate credit requires an explicit accounting policy.
8. Immutable history is not an unlimited right to retain personal data. Retention, restriction, erasure, legal hold and audit minimization need a governing policy. Do not prescribe globally mandatory content-bearing tombstones.
9. A projection identifies one canonical object. A combined packet for multiple case objects is a context pack of allowed projections, not one Projection with several subjects.
10. The reserved empty interoperability layer is a research hold, not a implemented layer with implied findings.
11. Publication lifecycle and research assurance differ. A schema-valid published reviewable draft may be installable in Vercy. Grok's prohibition on installing unpublished TODO entries is correct, but must not be applied to all published research drafts.
12. Grok claims to have verified several legal/standards details; this is provider-asserted evidence. Keep full-text, jurisdiction, licence and source-version checks explicit. Its relative political remark about application timing is not a fact adopted into the schema.

Direct primary-source checks by Codex:
- HR Open official standards page, Employee Performance Management section, names EPM results, panels and objective plans/results. The current landing page distinguishes 4.6 candidate and 4.5 final releases from the legacy EPM 3.3 package. We have not verified the full EPM XSD or licence for redistribution.
- SFIA 9 LEDA explicitly distinguishes competency assessment from period performance appraisal; use only a reference mapping, not copied copyrighted taxonomy definitions.
- Microsoft Research's SPACE paper abstract rejects single-metric productivity measurement. No algorithm or individual rating scale is taken from it.
- OPM performance cycle supplies a public-sector example of planning, monitoring, development, rating and recognition. It is not universal employment law or a mandated process for startups.
- W3C ORG and PROV-O supply relationship and provenance patterns. Model invariants remain our proposals, not a claim of W3C certification.
- ISO 30414:2025 public abstract concerns organizational human capital reporting. The full standard was not read; no individual appraisal formula is claimed.
- EUR-Lex full-text retrieval returned an anti-bot shell in the Codex web pass. Grok legal paraphrases are not independently text-verified here. Use only jurisdiction-qualified governance hooks and retain specialist legal review as a hold.

Required fixture family: concurrent employments with isolated governing context; narrative-only contractor; disputed attribution; proxy-only rating refusal; correction history; repeated calibration; unauthorized employer transfer; rating-scale drift; denied automation; purpose-limited one-object projection. The fixtures test these specified semantics, not real organizational behaviour or legal compliance.
