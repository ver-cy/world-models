# Independent review request: EM-DAT-05 Metric, target and observation

Act as an independent enterprise information-architecture reviewer. This is a public metamodel review; do not request private company data.

Review the proposed **cross-domain Metric Definition** authority for Vercy. Relevant public models:

- WM-XCT-025 Observable Result Fields: https://ver.cy/models/wm-xct-025-observable-result-fields/
- WM-DAT-010 Time Series / Observation Collection: https://ver.cy/models/wm-dat-010-time-series-observation-collection/
- WM-KNW-011 Goal / Objective: https://ver.cy/models/wm-knw-011-goal-objective/
- WM-DAT-007 Data Quality Assessment: https://ver.cy/models/wm-dat-007-data-quality-assessment/
- WM-DAT-002 Official Statistics: https://ver.cy/models/wm-dat-002-official-statistics/
- EM-DAT-05 assignment: https://ver.cy/enterprise/models/em-dat-05/

Catalogue analysis found no published generic Metric Definition master. The closest models have narrower authorities: result fields, observation collections, target commitments, quality assessments and official-statistics products. WM-KNW-011 explicitly excludes metric definitions and references an unassigned measure-definition sibling. WM-DAT-010 treats variable/indicator/measure/unit/population as external. WM-DAT-002 excludes universal indicator catalogues.

Claude therefore selected **NEW MODEL**: a cross-domain Metric Definition aggregate with stable metric identity and immutable definition versions. It would own formula/components, unit and scale references, dimension/additivity declarations, population boundary, method/source bindings, null semantics and facet-level comparability declarations. It would reference rather than own observations, series, targets, goals, procedures, units, populations, quality assessments and reports.

Test these questions:

1. Is there truly an independent aggregate, or should an existing Vercy model own it?
2. Which changes preserve metric identity but require a new definition version?
3. Which fields are portable semantics versus organization-specific KPI policy?
4. How should zero, unknown, not applicable, missing and suppressed remain distinct?
5. How should additivity and population boundaries prevent invalid aggregation?
6. What makes two definition versions comparable, comparable with restatement, or non-comparable?
7. Does the acceptance scenario work: two methods, one missing period and a recalculation without overwriting history?
8. Does the boundary align with SDMX, RDF Data Cube, SOSA/SSN, QUDT or UCUM, and PROV-O without claiming conformance?

Choose exactly one: **REUSE ONLY**, **PROFILE**, **EXTEND**, or **NEW MODEL**. Be sceptical of a new runtime identity, but require an existing owner to have compatible identity, purpose and lifecycle before choosing EXTEND.

Return no more than 1000 English words with these headings:

DECISION
BOUNDARY CHECK
MINIMAL PORTABLE CONTRACT
ACCEPTANCE SCENARIO
STANDARDS ALIGNMENT LIMITS
PUBLICATION RECOMMENDATION

If NEW MODEL, list the smallest viable owned contract and at least eight invariants. Do not assign a numeric WM-DAT identifier; numeric gaps are already reserved and allocation is a registry decision.
