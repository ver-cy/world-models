# Vercy world-model catalogue

A vendor-neutral library of meta-models describing **the world of people and what happens on planet Earth**: land and nature, matter and artifacts, the built environment, work, knowledge, organizations, registries, flows, events, people, and the security layer that gates it all.

Published by the [Vercy](https://ver.cy) project. The catalogue is standalone: bound to no product, no platform and no government program. Any Vercy-conformant Dimension can adopt any subset of it.

## What is inside

| Artifact | What it is |
|---|---|
| [Library-Architecture.md](Library-Architecture.md) | The catalogue architecture: **112 meta-models in 15 clusters**, design commitments, conventions, adoption guide |
| [world-models.csv](world-models.csv) | The machine register: one row per model (id, cluster, purpose, key objects, owner archetype, external standards, status) |
| [models/](models/) | One MMAS-conformant card per model, each with **its own bundles and layers** |

## How each model is described

Every model is described per the Vercy standard, not as prose: a MUIF manifest (identity `vercy:world:<id>`, CSN `world.<name>`, version, declared conformance MMAS A1), the model's own bundle and layer hierarchy designed from its subject matter, the five semantic primitives (Objects, Relationships, Events, Contracts, Projections), composition links to sibling models and external standards (EXTEND, REFERENCE, COMPOSE, MIX-IN, ALIGN), and a neutral stewardship note.

The iron rule holds everywhere: **information from any meta-model is readable only with the permission of its owner** (cluster S carries the machinery: ownership S1, access contracts S2, disclosure policy S3, audit S4).

## The clusters

Planet & Nature (P, 11) · Matter & Artifacts (M, 9) · Built Environment (U, 7) · Activity & Work (K, 12) · Knowledge & Information (N, 12) · Organizations (O, 7) · Registries & Ledgers (R, 6) · Flows & Resources (F, 9) · Events & Phenomena (X, 5) · Security Ownership & Access (S, 8) · Polity (A, 10) · Society (B, 5) · Economy (C, 2) · Civilization (D, 5) · People & Groups (H, 4)

## How to use it in your Dimension

1. **Find it**: the catalogue is registered as `vercy.world-models` in the [Vercy live register](https://github.com/ver-cy/meta-universe/tree/main/06-ecosystem/registry).
2. **Download it**: `git clone https://github.com/ver-cy/world-models` (or vendor a pinned commit into your model's `imports/`).
3. **Read it**: start from [BOOTSTRAP.md](BOOTSTRAP.md); the walk order is declared in [manifest.yaml](manifest.yaml).
4. **Adopt it**: take one model, one cluster or all of it; keep the IDs and CSNs for federation compatibility; bind your own policy where the cards leave stewardship generic.
5. **Federate**: Dimensions that share these CSNs can map their worlds to each other through them.

## Conformance

The repository carries the ARCH-017 traversal contract ([BOOTSTRAP.md](BOOTSTRAP.md), [manifest.yaml](manifest.yaml) with centralized kind rules) and the ARCH-018 mastership register ([sources.yaml](sources.yaml)). This repository is the System of Record for the catalogue; every copy elsewhere is a mirror.

## License

Apache-2.0. See [LICENSE](LICENSE).
