# EM-DAT-07 — Analytical Study and Conclusion

## Verdict

**Profile, do not master.** Create an *Enterprise analytical study profile* over four existing reservations; allocate no runtime identifier here.

- **AnalyticalStudy → profile of WM-ACT-036 Research Study**, not WM-ACT-034. ACT-036 already owns question/hypothesis, protocol, population, eligibility, sampling, power, conduct, analysis plan, estimate, finding, limitation and output linkage. The enterprise profile suppresses ethics, participant consent and trial registration, and adds a recommendation binding.
- **AnalysisMethod → reference-only**, reused across studies; raise as a new-model candidate, identifier unassigned, on the EM-DAT-05 Metric Definition precedent. ACT-036 carries the *applied* method and execution; nothing yet masters the reusable method definition.
- **AnalyticalFinding → WM-KNW-007 Claim/Proposition**, bound to its producing ACT-036 study.
- **Recommendation → WM-KNW-007 claim with deontic modality**, explicitly flagged as a declared gap (KNW-007 omits a normative-statement model), never WM-KNW-010 and never WM-ACT-024.

WM-ACT-034 is **rejected as master** and retained only as a source of reusable sampling/generalisation and evidence-quality mechanics.

## Evidence

WM-ACT-034's purpose is criterion-referenced judgement: it *requires* a version-pinned criteria catalogue binding (`de-criteria-source-ref`, `de-criteria-version`, cardinality 1, required), a decision rule with cut scores, and criterion-level outcomes from a bound vocabulary. An analytical study has no criteria catalogue and reaches no conformity verdict; forcing one produces the "fictitious rubric" that ACT-034's own adversarial check warns against. Conversely ACT-036's in-scope list — questions, protocol, design, population, sampling, estimand, estimate, uncertainty, finding, limitation, generalisability — matches EM-DAT-07's scope statement line for line, minus ethics.

WM-KNW-007 supplies precisely what the contour's invariant "вывод имеет область применимости" demands: `subject-and-population-scope` with aggregation level and ecological-inference caution, `spatial-and-temporal-scope`, `conditions-assumptions-and-defeaters`, `quantitative-content-and-measurand`, and `calibrated-confidence-and-likelihood` with a traceable-account pointer. Its truth-aptness gate and claim-type-driven required-field profile give the enforcement point.

## Identity/mastership

Distinct identities, none collapsible:

| Concept | Master |
|---|---|
| study, question, protocol, population, sample, applied method, execution, conduct | WM-ACT-036 |
| reusable analysis method definition | candidate, identifier unassigned |
| observation, measurement | referenced observation/dataset masters via ACT-036 |
| evidence citation | WM-KNW-008 (via KNW-007 REFERENCE) |
| finding, claim, recommendation | WM-KNW-007 |
| report issue, period, cutoff, snapshot | WM-REC-002 (per EM-DAT-06) |
| decision content: alternatives, criteria, selection, rationale | WM-KNW-010 |
| decision occurrence: authority, disposition, effect onset | WM-ACT-024 |
| sampling/generalisation and bias mechanics | WM-ACT-034 (reused, not mastered) |

## Study/method boundary

The **method definition** owns formula, estimator, assumptions, admissible data shape and known failure modes; it is versioned independently and cited by many studies. The **study** owns the *applied* method version pin, estimand, analysis population, preprocessing, software/code version, parameters, environment and execution provenance. Changing the definition never retroactively alters an issued study. A study that departs from its pinned method records a deviation with reason — it does not silently re-pin.

**Execution** (a run) is not the study; **observation** (a measured value) is not evidence for a conclusion until cited; **report** shows results but is a WM-REC-002 issue pinning a definition version, period, cutoff and snapshot, and never substitutes for the finding's justification.

## Finding/claim boundary

An **estimate** lives on ACT-036 (value, interval, test, sensitivity). A **finding** is the KNW-007 claim asserted from it: canonical statement, claim type, polarity, quantification, modality, measurand, coverage interval, population/spatial/temporal scope, assumptions, defeaters, calibrated confidence with scale reference and traceable-account pointer. One study may yield several findings; one finding may be restated (marked restatement, not edit) without becoming a new conclusion. Evidence stays a qualified binding (role, directionality, local weight); appraisal grades remain in WM-KNW-008.

## Causality and alternatives

- **Association** is `claim_type = comparative/empirical`. **Causation** is `claim_type = causal` and triggers a stricter required-field profile: measurand, comparator, aggregation level, design descriptor, competing-explanation note. Absent any of these, the claim cannot leave draft as causal.
- **Assumption vs. observation** is enforced structurally: observations are ACT-036 records; assumptions are KNW-007 `assumption statement` with verification status and defeat condition.
- **Alternative interpretations** are sibling KNW-007 claims over the *same* study, linked by registered conflict edges with conflict type and point of disagreement. Conflict is registered, never adjudicated here.
- **Exclusions** carry a recorded reason and stage (frame, eligibility, sampling, analysis) — silence is not exclusion.
- **Bias and generalisability**: sampling strategy, frame, achieved vs. planned size, missingness, known non-representative areas, and an explicit generalisation statement. Extrapolation beyond the sample must be stated, never implied by silence.

## Recommendation/decision boundary

A Recommendation is a deontic KNW-007 claim: *proposed action, addressee, rationale link to findings, scope, confidence*. It carries **no** deciding authority, **no** disposition code, **no** effect onset, **no** outcome statement, **no** approval activity. Acceptance requires all five, supplied only by WM-KNW-010 (the recommendation enters as one registered alternative among others, including a no-action baseline) and WM-ACT-024 (the occurrence, with authority binding, participants, signature and effect times). Two authority gates therefore separate a recommendation from a decision. Rejecting a recommendation leaves it resolvable with its rejection ground.

## Lifecycle

Method definition: `draft → issued → superseded → withdrawn`.
Study: `planned → conducted → analysed → concluded → superseded | withdrawn` (appends only).
Finding/recommendation (KNW-007): `draft → asserted → superseded | retracted`, supersession-linked.
Revised inputs create a **successor study** and successor findings; predecessors remain resolvable with their original scope and confidence. A retracted finding does not silently invalidate a decision taken on it; WM-ACT-024 records reconsideration separately.

## Scenario

Dataset: support-ticket counts, sampled from one intake channel with opt-in customers.
*Interpretation A*: "Employee productivity declined." *Interpretation B*: "Ticket volume rose after a release changed intake routing and logging."

Both are registered as KNW-007 claims over one ACT-036 study, linked by a conflict edge. A survives none of the gates: productivity has no defined measurand (tickets are workload, not output-per-input); the denominator — eligible interactions — is unknown, so no ratio may be published; the sample frame excludes other channels and non-opt-in customers, and that exclusion is recorded, so generalisation to "the employee" is prohibited; no competing-explanation note exists, so `claim_type = causal` cannot be assigned. A is therefore recorded, at most, as an associational claim bounded to the opt-in single-channel sample, confidence low, with B as a registered alternative and the routing change as a named defeater. **The inference that ticket growth proves a productivity decline is rejected.** Constraints survive; no false causal claim is created.

## Invariants

1. Study, method definition, execution, observation, evidence citation, finding, report issue, recommendation, decision content and decision occurrence have disjoint identities.
2. Every finding pins its study version, method version, population, sample and data snapshot.
3. Every conclusion carries an explicit scope of applicability; silence is never generalisation.
4. Assumption is separated from observation and carries verification status.
5. Causal claim type requires measurand, comparator, design descriptor and competing-explanation note.
6. Association never auto-upgrades to causation.
7. Unknown denominator blocks ratio publication.
8. Exclusions carry reason and stage; sampling carries frame, achieved size and missingness.
9. Competing interpretations coexist as conflict-linked claims; conflict is registered, not resolved here.
10. A report neither establishes nor replaces a conclusion's justification.
11. A recommendation is never an accepted decision; acceptance requires WM-KNW-010 content plus a WM-ACT-024 occurrence with authority, disposition and effect onset.
12. Corrections append successors; issued studies, findings and recommendations are never rewritten.

## Minimal completion shape

Study: question, population definition with inclusion/exclusion, sampling frame and strategy, achieved size, pinned method version, estimand, pinned input snapshot, execution reference, limitations. Finding: canonical statement, claim type, measurand where quantitative, scope triple (population, place, period), assumptions, defeaters, confidence with scale reference, evidence bindings, producing-study reference. Recommendation: proposed action, addressee, deontic modality, supporting finding references, scope, explicit non-acceptance marker. Conflict edge for each alternative interpretation.

## Holds

No canonical completeness or installability is claimed. All four bases are reviewable drafts with `publishableCanonical: false`; WM-ACT-036 and WM-ACT-034 carry single-provider waivers, WM-ACT-036 additionally waives two providers. Every relation in this review is a proposal: WM-ACT-036 records composition as a declared gap, WM-ACT-034's relation ledger is empty with an unratified parent link, WM-KNW-010's ledger registers only two relations, and WM-KNW-007's parent CHILD row is unregistered. Registry `entry_kind` values read `standalone-mm` against research-plane kinds across all five models, and every `review_state` is `boundary-review-required`. AnalysisMethod and Recommendation have no allocated identifiers. Source pins, crosswalks and fixtures remain unverified.
