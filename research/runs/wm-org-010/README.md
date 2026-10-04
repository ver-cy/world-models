# WM-ORG-010 - Legal Entity Registration research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 19 | 7 | 15 | 28 | 114 | 20 | 11 |
| Grok (normalized) | 12 | 6 | 12 | 17 | 57 | 16 | 7 |
| Synthesis | 28 | 7 | 15 | 29 | 118 | 21 | 12 |

Both providers independently classify Legal Entity Registration as an
`entity`: the durable, authoritative registration identity and lifecycle of a
legal person, distinct from the broader operational Organization model.
Ownership, capital and securities, statistical enterprises, tax assessment and
sector licensing remain sibling responsibilities.

The no-tools adjudication retained Claude's stronger cross-jurisdictional
boundary and accepted Grok's legal-personality and capacity contribution.
EU-specific EUID/BRIS structures were deferred to a regional profile rather
than embedded in the universal core. Registrar-side formation operations were
rejected because this model observes and operates over authoritative registry
records; it does not silently assume the role of the registration authority.

Claude contained two safe cross-grain local-ID collisions. They were repaired
deterministically by prefixing the affected data-grain identifiers. Grok's
initial wrapper contained an incomplete transport envelope; a no-tools
normalization pass reconstructed the structured result without adding research.
The normalized identity priority already named an authoritative register or
court number and received the explicit `master-system` label required by the
semantic contract. Both normalized provider results pass schema and semantic
validation.

No critical structural conflicts remain. Primary-source retrieval, version-pin
reconciliation, the applicable EU interconnection regulation, wider
jurisdiction profiles and several legal-effect claims remain explicit
publication holds. See `synthesis-plan.json`, `adjudication.json`,
`comparison.json` and `synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-org-010-legal-entity-registration/>
