# WM-SFT-001 - Software Product research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 15 | 7 | 14 | 26 | 95 | 26 | 9 |
| Grok (normalized) | 10 | 5 | 9 | 20 | 63 | 20 | 16 |
| Synthesis | 22 | 7 | 14 | 30 | 107 | 30 | 15 |

The no-tools adjudication classified Software Product as an `aggregate`.
Release records, bills of materials, advisories, deployed-instance records and
configuration snapshots have independent lifecycles, authors and retention
duties, but remain interpretable only when anchored to one governed product
identity. The producer-side and operator-side ownership slices therefore form
an internal seam of the aggregate rather than separate product identities.

Claude was retained as the structural base. Accepted Grok additions cover
family, edition, channel and SKU identity; SWID and CoSWID tag types;
composition-completeness evidence; advisory remediation, restart and fix
entitlement; and release withdrawal as an operation. Seventeen decisions were
recorded and no critical conflict remains. Component packages, licence
instruments, vulnerability definitions, runtime infrastructure and full AISMM
assemblies remain sibling or alignment concerns.

Both provider runs used the same frozen contract and clean input commit
`9b918ff13391cc42bbcfffa9b3f91f737f623bd0`. Grok returned substantive content
using non-canonical field names and types. The raw wrapper remains outside Git;
a no-tools pass normalized only the contract shape, retained the same structural
counts, made no semantic repairs and required no cross-grain identifier
repairs. Both provider results and the synthesis pass schema and semantic
validation.

Live source and version reconciliation, direct CISA PDF table extraction,
five-profile validation, clause-level SWID confirmation and explicit
paywalled-standard limitations remain publication holds. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-sft-001-software-product/>
