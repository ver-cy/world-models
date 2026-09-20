# BOOTSTRAP

Operating instructions for reading and changing this repository. Read this file first; then [manifest.yaml](manifest.yaml); then [sources.yaml](sources.yaml); then walk in the declared order.

## What this repository is

The Vercy world-model catalogue: 111 vendor-neutral meta-models in 15 clusters describing the world of people and events on Earth. Each model is one card under `models/`, described per the Vercy standard (MMAS) with its own bundles and layers, at maturity A1 (Structured).

## Walk order

1. [README.md](README.md): orientation.
2. [Library-Architecture.md](Library-Architecture.md): the catalogue architecture, clusters, conventions, adoption guide. This is the map; read it before any card.
3. [world-models.csv](world-models.csv): the machine register. One row per model; a card exists for every row.
4. `models/`, cluster by cluster in the register's order; within a cluster, cards in ID order.
5. [research/README.md](research/README.md), then the queue and the selected model run only.
6. `publications/`, which contains website-ready projections generated only from validated syntheses.

## Local conventions

- IDs (`P2`, `K8`, `H1`) are stable and never reused. CSNs follow `world.<lowerCamelName>` with bundle and layer segments beneath.
- Each card carries a MUIF manifest block (identity, conformance, bundles, layers, imports); the block must parse as YAML and keep the required keys.
- Bundles and layers are model-specific, designed from the subject matter; a card whose structure looks copied from another card is a defect.
- The catalogue is vendor-neutral: owner archetypes are generic roles; no product, platform or polity doctrine appears in cards.
- No em-dashes or en-dashes anywhere in the corpus; do not introduce them.

## Change rules

- This repository is the System of Record for the catalogue ([sources.yaml](sources.yaml)); edit here, never in a mirror.
- Register and cards must not diverge: adding, renaming or retiring a model updates `world-models.csv` and the card set in the same commit; `Library-Architecture.md` section 3 counts follow.
- A model's status flips `described -> deepened` only when a richer specification or package exists and the card links it.
- Do not renumber existing IDs; new models take the next free number in their cluster.
- Publication lifecycle and research assurance are separate. A validated synthesis with no critical conflict may be labelled `published` while its research state remains `reviewable-draft`; every hold and provider waiver must stay visible. Only a hold-free independently reviewed synthesis may be labelled canonical.
- Generate website packages with `tools/publish_model_research.py`; do not hand-edit files under `publications/`.

## For AI agents

Follow the Agent-Operations recipes of the Vercy standard. Assemble context per task: the architecture document plus the specific cards you work on; do not load the whole catalogue.
