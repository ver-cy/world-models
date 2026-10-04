# WM-SFT-007 - Software Component / Package research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 19 | 6 | 13 | 27 | 109 | 27 | 10 |
| Grok (normalized) | 16 | 5 | 12 | 14 | 61 | 8 | 7 |
| Synthesis | 32 | 6 | 13 | 29 | 117 | 27 | 12 |

The no-tools adjudication classified Software Component / Package as an
`entity`. It is the versioned distributable unit with both project-level
coordinates and release-level identity. Product composition, SBOM documents,
build runs, vulnerability records and installed occurrences remain sibling
models; only their typed references and evidence-bearing verdicts cross this
boundary.

Claude was retained as the structural base. Accepted Grok additions supply the
component type and software-purpose classification and instantiate the missing
SBOM reference and relationship-completeness edge. Fifteen decisions were
recorded and no critical conflict remains. Ecosystem-specific coordinate and
version grammars, registry lifecycle policies and personal-data handling remain
deferred research rather than inferred structure.

Both provider runs used the same frozen contract and clean input commit
`98293814a49c5e862599ada87b67346060a65ccc`. Grok returned substantive content
using a non-canonical response envelope. The raw wrapper remains outside Git; a
no-tools pass normalized only the contract shape, made no semantic repairs and
required no cross-grain identifier repairs. Both provider results and the
synthesis pass schema and semantic validation.

Live source and version reconciliation, direct CISA/NTIA field-table evidence,
validation across Maven, npm, PyPI, Debian/RPM, Go and OCI, independent
SWHID/gitoid/OmniBOR verification, current Cyber Resilience Act clause checks
and a primary-source privacy policy remain publication holds. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-sft-007-software-component-package/>
