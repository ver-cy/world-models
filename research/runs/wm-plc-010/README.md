# WM-PLC-010 - Gazetteer Place research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 17 | 6 | 16 | 24 | 101 | 18 | 13 |
| Grok (normalized) | 9 | 7 | 13 | 21 | 71 | 13 | 10 |
| Synthesis | 25 | 6 | 16 | 27 | 111 | 19 | 17 |

Both providers independently classify Gazetteer Place as an `entity`: a
persistent, separately identifiable place whose identifier survives renaming,
reclassification and geometry revision. Addresses, CRS definitions, legal
boundary delimitation, cadastre, commercial venue operations and place-type
vocabularies remain governed by referenced sibling models or classifiers.

The no-tools adjudication retained Claude's stronger boundary, temporal,
retention and validation coverage. It accepted Grok's gazetteer register
membership and item status, administrative-versus-physical facet, deprecated
or community-restricted name handling, plus four missing traversal and
governance functions. Sixteen explicit decisions were recorded and no critical
structural conflict remains.

Grok returned a complete substantive answer in an alternate provider schema.
The immutable raw wrapper stays outside Git; a no-tools transport pass mapped
it to the frozen Vercy contract and preserved its substantive node counts.
Claude experienced repeated upstream `529 Overloaded` responses and one
30-minute timeout before completing a clean, independent valid run. Both final
provider results pass schema and semantic validation.

ISO 19112 normative wording, live version pins, additional national and
historical profiles, Indigenous data governance, EDTF syntax and sensitivity
thresholds remain explicit publication holds. See `synthesis-plan.json`,
`adjudication.json`, `comparison.json` and `synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-plc-010-gazetteer-place/>
