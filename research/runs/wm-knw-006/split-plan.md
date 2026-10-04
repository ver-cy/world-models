# WM-KNW-006 bounded Claude research plan

The normal monolithic Claude pass timed out three times (Opus twice, Sonnet
once).  The repository owner authorized a bounded split on 2026-09-02.

The three passes are deliberately non-overlapping at the structural level:

1. `core` owns concept identity, designation/term, meaning and usage.
2. `relations` owns schemes, semantic relations, mappings and interoperability.
3. `governance` owns lifecycle, provenance, quality, roles, access and all
   canonical service-layer rules.

Every pass must satisfy the complete provider schema and local validator.  The
deterministic merger stable-unions sources and assigned structure, keeps the
model boundary from `core`, keeps service layers from `governance`, and fails
on identity mismatches, duplicate IDs/questions, unresolved citations or any
final validation error.  The normal single-provider no-tools adjudication is
still required after the merge.

Coverage is routed by `coverage-plan.json`: every checklist dimension comes
from its designated subject owner rather than concatenating three partial
checklists. Plain-text `SRC-###` tokens are remapped together with structured
`source_refs`; an unknown token fails the merge.

The final no-tools audit identified two narrow service-policy inconsistencies
after the provider parts were frozen. `service-layer.patch.json` records the
deterministic additions to the identity ladder and access exceptions. The
merger accepts only those two append-only fields, hashes the patch and validates
the complete result again; the patch cannot alter subject structure or sources.
