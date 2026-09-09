# WM-XCT-032 - Currency / Monetary Value research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 53 | 11 | 25 | 47 | 199 | 26 | 37 |

Claude researched the model through six independently schema-valid bounded
passes: exact amount and currency identity, precision and rounding policy,
valuation and conversion, governance controls, state operations, and
calculation/projection operations. Their local identifiers are disjoint. The
deterministic merger remapped and deduplicated sources, routed coverage
dimensions, selected the governance-controls service layers and revalidated
the combined structure.

The original amount pass was reduced after transient API capacity errors and a
timeout. Its two bounded replacements completed successfully. The original
governance pass and its first service-only replacement each reached the
provider timeout without a result. No partial output was accepted. Governance
was then separated into controls, state operations and calculation operations;
all three completed and passed local validation.

The first no-tools audit found no critical conflict but identified two
correctable defects: relationship coverage overstated an empty frozen contract,
and a boundary note incorrectly denied all rate derivation while the functions
supported documented cross-rate calculation. The result now marks
relationships as a gap and distinguishes calculation from publication
authority. These changes are recorded in `adjudication-repairs.json`, the
result and manifest hashes were updated, and the repaired result was
independently re-adjudicated with zero critical conflicts.

The final audit retained `mixin` as the best current entry kind while preserving
the registry's `boundary-review-required` signal: the rich concurrency,
supersession and tombstone semantics may ultimately justify a separately
addressable companion pattern. The empty relationship contract, public-page
limits for paywalled standards and live source/version verification also remain
publication holds.

The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. The package visibly retains that single-provider
hold and remains `reviewable-draft`; it is not a final or canonical result.

Published draft:
<https://ver.cy/models/wm-xct-032-currency-monetary-value/>
