# WM-PER-010 - Contact Point / Party Profile research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Channels pass | 17 | 3 | 7 | 13 | 52 | 6 | 5 |
| Preferences pass | 12 | 3 | 6 | 13 | 62 | 2 | 5 |
| Governance pass | 16 | 3 | 7 | 13 | 59 | 6 | 11 |
| Synthesis | 39 | 9 | 20 | 39 | 173 | 14 | 21 |

The monolithic Claude result was rejected because two local identifiers were
duplicated. The bounded workflow therefore used three structurally disjoint
passes with the prefixes `cp-chan-`, `cp-pref-` and `cp-gov-`. The preferences
pass was regenerated once after the first no-tools audit found ambiguous
ownership of suppression state. The corrected model treats a party-stated
contact-avoidance preference as non-legal local state, keeps legal objections
and suppression in an external communication-restriction registry, and fails
closed when that registry cannot be resolved. Any external restriction takes
precedence and a local preference can only narrow the allowed options.

All three parts passed the complete provider schema and semantic validator.
The deterministic merger remapped source identifiers, rejected duplicate IDs
and questions, routed coverage dimensions to explicit owners and produced a
separately validated synthesis. The final no-tools audit found no critical
conflict and reclassified the subject-model kind from `mixin` to `aggregate`,
with the party-scoped Contact Profile as aggregate root. The frozen registry
plane still records `mixin`; reconciling that value is an explicit hold.

The repository owner explicitly waived Grok for this queue. No Grok output was
fabricated or inferred. Publication holds also cover live source/version
verification, unresolved ownership overlap with WM-XCT-024, missing frozen
relationship bindings, registry review of the entry-kind change, and duplicate
or inconsistent source registrations. The source count is therefore a count of
records in the evidence pack, not a claim of 39 distinct settled authorities.
The package remains `reviewable-draft`, `canonical_publishable` is false, and
every public artifact exposes the waiver and holds.

Published draft:
<https://ver.cy/models/wm-per-010-contact-point-party-profile/>
