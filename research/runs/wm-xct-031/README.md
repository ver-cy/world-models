# WM-XCT-031 - Localization / Language research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 32 | 7 | 16 | 31 | 136 | 16 | 22 |

Claude researched the model through three independently schema-valid bounded
passes: language/locale identity and negotiation, translation resources and
fallback, and governance/service rules. Their local identifiers are disjoint;
the deterministic merger remapped and deduplicated sources, routed coverage
dimensions, selected governance service layers and revalidated the combined
structure.

The initial monolithic provider run ended in a transient API error and its
single retry stalled without producing a result. No raw or partial output was
accepted. Bounded passes completed successfully. The first corrective no-tools
audits on Opus encountered transient empty-stderr provider exits; a Sonnet
no-tools audit completed against the same schema and evidence. The adjudicator
was also corrected to read frozen registry context from the base split-pass
prompt instead of silently treating that context as absent.

The first successful audit identified source duplication, weak-identity,
authorization-boundary, serial-naming, disclosure-grain and evidence-tier
defects. Those repairs are recorded in `adjudication-repairs.json`, the result
and manifest hashes were updated, and the corrected result was independently
re-adjudicated. The final audit found no critical conflict and retained
`mixin`: a localization binding has host-dependent weak identity and does not
own localized content, translation memories, termbases, person preferences,
geography, authorization enforcement or records disposition.

The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. Publication holds retain the owner-authorized
single-provider notice, live verification of 32 source/version pins, the
declared retention/privacy/security/negotiation gaps and the currently empty
structured relationship contract. The package remains `reviewable-draft` and
`canonical_publishable` is false.

Published draft:
<https://ver.cy/models/wm-xct-031-localization-language/>
