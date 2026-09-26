# WM-KNW-014 relation correction audit

## Decision

Replace the former `WM-KNW-014 CHILD WM-ACT-021` interpretation with the candidate relation `WM-KNW-014 REFERENCE WM-ACT-021`.

## Boundary evidence

- An issue or problem owns discrepancy identity, causal analysis, recurrence, disposition and acceptance state.
- A service case owns requester interaction, assignment, service workflow and case closure.
- A case may expose or track a problem, but neither aggregate contains the other and neither lifecycle inherits from the other.
- The EM-COM-04 Claude and Grok studies independently preserved problem/incident separation from the service-case lifecycle.

## Corrected artifacts

- `tools/build_unified_registry.py`: removes `WM-ACT-021` from the WM-KNW-014 parent source field.
- `planning/VERCY-UNIFIED-MEGA-REGISTRY.csv`: clears `parent_ids` and points to the typed relation ledger.
- `planning/VERCY-MODEL-RELATIONS.csv`: adds the candidate non-owning reference.
- `synthesis.result.json`: changes composition from required `CHILD` to optional `REFERENCE` and removes parent-language claims.
- `adjudication.json`: records the accepted candidate boundary and retains canonical relation approval as a publication hold.

## Versioning rule

The existing `0.3.0-research.1` package remains historical evidence. The corrected package must receive a new version; its bytes must not silently replace the old version in immutable history.

## Verification

`validate_model_research.py` passes with no schema or semantic errors after the correction. The candidate relation remains non-canonical until the relation ledger is approved through the registry governance path.
