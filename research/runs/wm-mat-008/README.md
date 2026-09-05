# WM-MAT-008 - Observation / Measurement Record research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 6 | 13 | 29 | 115 | 3 | 9 |

Claude completed one full web-enabled research pass and the local schema and
semantic validator accepted it. The repository owner explicitly waived Grok
for this queue; no Grok output was fabricated or inferred. A separate no-tools
Claude adversarial audit inspected the compact result without adding facts,
findings or functions. It accepted `event` as the subject-model entry kind,
because identity is anchored on one immutable observation act and a changed
property, procedure or feature means a new observation. Registry
`standalone-mm` remains a separate record-plane classification. The final
synthesis passed validation with no critical conflicts.

The structure covers observation identity, feature of interest, observed
property and measurand, procedure and deployment context, phenomenon/result/
record time, result values and units, absent or censored values, sampling,
uncertainty, metrological traceability, conformity interpretation, quality
flags, provenance, lifecycle, corrections, access, retention and
interoperability profiles. Series, datastreams and collections retain their own
identity and completeness; devices, parties, evidence and storage payloads are
referenced rather than copied.

Open holds include the single-provider waiver, live verification and version
pinning of all 16 sources, cardinalities still grounded in a 2021 draft rather
than the published OMS/ISO 19156:2023 classes, an empty relationship contract,
three artifact-identity defects, and explicit publication of both entry-kind
axes. Further work is required for function coverage, composite source IDs,
registry placement and neighbour links. The result therefore remains
`reviewable-draft`, `publishable` is false, and every public artifact exposes
the waiver and holds. See `comparison.json`, `synthesis-plan.json`,
`adjudication.json`, `source-verification.csv` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-mat-008-observation-measurement-record/>
