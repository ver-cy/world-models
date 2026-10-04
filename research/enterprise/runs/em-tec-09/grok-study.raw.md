Verdict: Conditionally sound. Technology Adoption and Architecture Exception both require independent roots; waiver mastership is resolved to Architecture Exception as the grant record. Identifiers remain unassigned. This review does not claim publication readiness.

Strongest evidence. The required separations are load-bearing. Abstract technology is not a product, release, or deployment. Upstream lifecycle is not vendor support and is not local adoption. Adoption is not conformance. A standard expression is not a rule. An exception is not an assessment result, a nonconformity, or a risk acceptance. Architecture Standard can profile WM-KNW-012 and reference WM-KNW-013 rules. Conformance Assessment can profile WM-ACT-034. ADR can reuse the WM-KNW-010 / WM-ACT-024 / WM-REC-010 triad. The exception fields named in the proposal — subject, exact rules, authority, owner, conditions, bounded expiry, renewal as a new grant — are the minimum needed to keep a waiver auditable. WM-REC-005 is legacy-only and does not model a normative standard.

Strongest counterexample. An application uses a language recommended by the standard and is claimed conformant. The claim fails. Language use is evidence for at most one rule. The same application is assessed against standard v1 and standard v2 and fails other rules in both. A temporary R7 exception covers only the named rule, the named subject, and a bounded period. After expiry the nonconformity stands unless a new grant exists. An approved R7 can exist before reassessment and remain valid after a failed retest until expiry, so it is not an assessment outcome.

Identity and mastership. Technology, Technology Adoption, and Architecture Exception need independent identity. They stay identifier-unassigned. Architecture Standard is a profile of WM-KNW-012, not a new rule root; it references WM-KNW-013 rule identities and does not own them. Conformance Assessment is a profile of WM-ACT-034. ADR is not a fourth root; it reuses the decision triad. Waiver mastership sits with Architecture Exception. Assessment records the evaluation and the nonconformity evidence and may cite the exception. Risk acceptance is a decision outcome and may authorize a grant. Neither assessment nor risk acceptance owns the waiver. Rule drafts that treat exceptions as external masters are consistent with this.

Technology, product, and version. Technology is the abstract capability or class. Product, release, and deployment instance are separate identities. A technology identity does not change because a vendor ships a release or an organization deploys an instance. Version applies to the standard and to the product release, not to the abstract technology root.

Adoption and lifecycle. Technology Adoption is an independent root. It records local selection, scope, effective period, and the split between upstream lifecycle, vendor support, and local support. The decision triad may authorize an adoption, but the adoption state persists after the decision and can change without a new decision, for example when a support window ends. Adoption does not imply conformance. Conformance does not imply adoption.

Standard and rules. The standard is the expression: scope, version, status, and the set of referenced rules. Rules keep their own identity under WM-KNW-013. A recommendation inside a standard is not a mandatory rule and is not a conformance result. Replacing a rule requires a new rule identity or a new version, not a silent edit of the standard text.

Conformance assessment. Each assessment is version-scoped and subject-scoped. One application can hold concurrent assessments against standard v1 and standard v2. A result cites the rules evaluated, the evidence, and the outcome. It does not create, extend, or revoke an exception. Partial evidence, including use of a recommended language, never aggregates to whole-system conformance.

Exception and waiver. Architecture Exception is the independent root and the waiver master. A valid grant identifies the subject, the exact rules waived, the authority, the owner, the conditions, and a bounded expiry. Renewal is a new grant with a new identity. An exception does not erase the nonconformity; it bounds permission to operate despite it. It is not an assessment, not a risk-acceptance record, and not a change to the rule.

ADR. An architecture decision record reuses the decision triad: knowledge, act, and record. It may authorize an adoption or an exception. It does not replace either root. The decision ends; the adoption state and the exception grant continue under their own identities.

Time, version, and scenario. Standard v1 and standard v2 coexist. Assessments are pinned to the version evaluated. R7 is time-bounded. Expiry restores the prior nonconformity unless a new grant is recorded. No back-dating. No extension of the same exception identity.

Scenario. Application A is assessed against standard v1 and fails rule R7 plus two other rules. It is assessed against standard v2 and fails the successor of R7 plus one other rule. A temporary exception is granted for R7 only, with named authority, owner, conditions, and an expiry date. A claims whole-system conformance because it uses the recommended language. The claim is rejected. After expiry, A remains nonconformant on R7 unless a new grant exists. The v2 assessment is unaffected by the v1 exception.

Invariants.

1. Technology identity is independent of product, release, and deployment.
2. Technology Adoption is an independent root, not a role on Technology and not only a decision.
3. Architecture Exception is an independent root and the waiver master.
4. Assessment profiles WM-ACT-034 and does not own exceptions.
5. Standard profiles WM-KNW-012 and references, but does not own, WM-KNW-013 rules.
6. ADR reuses the decision triad and does not replace adoption or exception.
7. Adoption does not imply conformance; conformance does not imply adoption.
8. One subject may have concurrent assessments against different standard versions.
9. Recommended-language use is evidence for at most one rule.
10. An exception names subject, exact rules, authority, owner, conditions, and bounded expiry.
11. Renewal is a new grant, not an extension of the same identity.
12. Expiry ends the grant; the nonconformity stands unless a new grant exists.
13. An exception may precede or outlast the assessment that cited it.
14. WM-REC-005 is not used as a normative standard.

Minimum model set. Technology; Technology Adoption; Architecture Standard as a profile of WM-KNW-012 referencing WM-KNW-013; Conformance Assessment as a profile of WM-ACT-034; Architecture Exception; ADR as a reuse of the decision triad. Product, release, and deployment remain outside the technology root. Risk acceptance remains a decision outcome, not the waiver master.

Blockers. Technology, Technology Adoption, and Architecture Exception are still identifier-unassigned. Rule-to-standard reference cardinality is not
