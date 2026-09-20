# WM-BLT-006 - Facility research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude (ID repair) | 21 | 6 | 13 | 26 | 105 | 25 | 10 |
| Grok (normalized) | 12 | 8 | 14 | 26 | 85 | 26 | 9 |
| Synthesis | 31 | 6 | 13 | 31 | 121 | 30 | 13 |

Both providers independently classify Facility as an `aggregate`: a governed
functional collection with its own operational identity that references, but
does not remaster, Site, Building, Space, System, Equipment or Asset objects.
Site containment is conditional, and the registry's Facility-contains-Building
relationship is retained while the inverse IFC subtype mapping is documented
as an interoperability conflict.

The no-tools adjudication retained Claude's stronger neighbour boundaries,
bitemporal governance, disclosure, retention and crosswalk-loss coverage. It
accepted Grok's facility eligibility test, occupancy authorization, alleged
versus adjudicated compliance status, facility-scale fire and life safety and
post-occupancy evaluation, plus three missing functions. Fourteen explicit
decisions were recorded and no critical structural conflict remains.

Claude's complete answer reused two question IDs in distinct parent findings;
the deterministic transport repair namespaced only those IDs and preserved all
text and counts. Grok returned a complete alternate provider schema; a
no-tools pass mapped it to the frozen Vercy contract. Raw wrappers remain
outside Git and both final provider documents pass schema and semantic checks.

EPA FIDS and IFC version pins, clause-level ISO verification, unparsed FRPP and
FIDS field details, non-US and civil-infrastructure profiles, and the five
narrowly sourced Grok additions remain explicit publication holds. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-blt-006-facility/>
