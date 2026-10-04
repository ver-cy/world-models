# Independent review request: EM-DAT-06 Report definition and release instance

Act as an independent enterprise information-architecture reviewer. This is a public metamodel review; do not request private company data.

Vercy has a reserved but unpublished entry **WM-REC-002 Report / Statement**: a governed factual or analytical statement issued for an audience and reporting period. Review whether EM-DAT-06 should complete this reserved model.

Relevant public models:

- WM-REC-001 Document / Record: https://ver.cy/models/wm-rec-001-document-record/
- WM-ACT-044 Content Publication: https://ver.cy/models/wm-act-044-content-publication/
- WM-ACT-053 Data Processing Job / Pipeline Run: https://ver.cy/models/wm-act-053-data-processing-job-pipeline-run/
- WM-XCT-003 Projection / Disclosure Policy: https://ver.cy/models/wm-xct-003-projection-disclosure-policy/
- WM-MED-003 Publication / Edition: https://ver.cy/models/wm-med-003-publication-edition/
- EM-DAT-06 assignment: https://ver.cy/enterprise/models/em-dat-06/

Local and Claude analysis selected **COMPLETE RESERVED MODEL**. WM-REC-002 would own report-definition versions and issued report statements. It would reference processing runs, record artifacts, publication operations, publication editions and disclosure-policy versions without duplicating their lifecycles.

Test:

1. Does a report definition have identity and lifecycle independent from processing runs and record artifacts?
2. Should one aggregate own both reusable definition versions and issued statement instances?
3. Which fields make an issue reproducible: parameters, input snapshots, reporting period, cutoff, as-of basis, run evidence, metric/query bindings, disclosure tuple and artifact references?
4. How should corrected inputs create a successor issue without overwriting the published predecessor?
5. How must aggregation and suppression remain bound to the exact disclosure-policy version?
6. Are report issue, processing run, artifact, publication case and edition correctly separated?
7. Is a dashboard definition a report-definition profile, while a live view remains ephemeral until snapshotted as an issue?
8. Which parts are portable semantics rather than BI-tool configuration?

Acceptance scenario: issue a report; correct an upstream fact; issue a successor; retain and explain both versions; suppress a sensitive slice under the pinned policy version; remain explainable after the dashboard changes.

Choose exactly one: **REUSE ONLY**, **PROFILE**, **COMPLETE RESERVED MODEL**, or **NEW MODEL**. Do not allocate another identifier unless you prove WM-REC-002 has a different purpose.

Return no more than 1000 English words with headings:

DECISION
BOUNDARY CHECK
MINIMAL PORTABLE CONTRACT
DASHBOARD DISPOSITION
ACCEPTANCE SCENARIO
HOLDS AND PUBLICATION RECOMMENDATION
