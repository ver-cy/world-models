# Vercy research consolidation, 2026-09-06

## Decision

The six-way manual research partition is retired. It increased coordination
cost, left stale leases and branch-local state, and produced a large number of
prepared prompts without provider-complete specifications. The canonical
`feat/mega-model-registry` branch is again the only write and publication line.

No former branch or dirty worktree was deleted. They preserve provider failures,
pre-research dossiers and branch history for selective reuse. They are not live
queues and must not receive new writes.

## Reconciliation result

At audit time the canonical queue contained 401 subject models:

- 90 were already valid and published;
- `WM-XCT-037 Dependency / Impact`, completed by stream 01, was already present
  in the canonical line;
- `WM-ACT-014 Health Care Delivery` and `WM-ECO-001 Market / Exchange` were the
  only additional provider-complete, adjudicated and valid stream results;
- those two results were revalidated and imported without the obsolete stream
  log/state mutations, bringing the canonical total to 92;
- 309 models remain incomplete;
- streams 02, 04, 05 and 06 completed no model;
- the hundreds of other run directories are preparation dossiers, prompts,
  timeouts or partial outputs, not publishable research.

There was no semantic model conflict requiring rollback. The conflict was
operational: six competing state machines around one provider and one
production target. Retiring the five worker lanes and returning to the clean
canonical branch removes it without discarding evidence.

## Preserved former state

The former worktrees remain under
`R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\vercy-workstreams`.
Their remote branches also remain. Approximate untracked prepared material at
the audit point was 1 file in stream 01, 58 in stream 02, 54 in stream 03, 53 in
stream 04, 52 in stream 05 and 52 in stream 06. Read a model-specific dossier
only when that model reaches the front of the canonical queue.

## Resume point

The next incomplete row is sequence 91, `WM-ACT-007 Work Order`. Sequence 92
and 98 are already complete because their valid stream results were salvaged.
After sequence 91, always select the next lowest incomplete sequence.

## Scale strategy

Millions of individually hand-researched deep specifications would be slow,
expensive and misleading. Vercy therefore uses three truthful catalogue tiers:

1. curated deep Vercy meta-models with Bundle, Layer, Finding and Question
   structure;
2. externally governed schemas, ontologies, standards and classifiers indexed
   with provenance and alignment state;
3. deterministic domain profiles generated from those classifiers and
   materialized as complete Vercy packages on demand.

The next architecture task is to make tiers 2 and 3 searchable through the
same API and catalogue while preserving source licence, version, hierarchy and
the distinction between a curated specification and a generated profile.

## First scale implementation

API version 1.1.0 now implements the first tier-3 discovery boundary. When no
local model reaches score 0.55, `/api/v1/models/search/` sends only the public
concept name and language to Wikidata `wbsearchentities`. Returned QIDs are
labelled `generated-profile`, `external-profile-candidate` and
`installable=false`; they include source and CC0 provenance and can enter the
normal UUID materialization queue. Local curated models remain authoritative
and rank first. No private need description, questions, properties, examples,
client identity or Dimension data is sent to Wikidata.
