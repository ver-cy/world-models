# Vercy runtime proof checkpoint 0.4

Date: 2026-09-06  
Status: implemented in the canonical local site and prepared for production  
Site source: `R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\vercy-platform-experience\site`

## Why this checkpoint exists

An external review correctly identified that catalogue breadth had moved ahead
of executable proof. Vercy had templates and governance, but no populated public
Dimension, agent benchmark, scalable deterministic retrieval, strict Dimension
validator, current-truth rule, parallel-write contract, version migration or
MCP surface. This checkpoint makes those gaps explicit and closes their first
bounded implementation before more catalogue breadth is claimed.

## Implemented scope

1. **Complete public example.** Northstar Community Workshop is a fictional,
   fully populated reference Dimension with a January-August timeline, 11 object
   revisions, 13 facts, 10 relations, 8 events, a superseded value and a visible
   contested value. It includes root and model `AGENTS.md`, a model specification,
   an executable runtime fact-path schema and a downloadable archive.
2. **Executable V3 validation.** Dependency-free validation now checks published
   control schemas, immutable record schemas, unique IDs, reference integrity,
   object revision heads, bitemporal intervals, model file resolution, pinned
   specification digest, declared fact paths and units. Failures carry stable
   rule IDs and exit non-zero. It does not certify external truth, legal authority
   or safety.
3. **Retrieval.** `vercy index` builds a replaceable SQLite cache; `vercy query`
   supports text, record type, object, semantic type, relation, event, valid time
   and knowledge time. A synthetic run over 5,000 objects, 5,000 facts and 4,999
   relations passed text, relation and bitemporal assertions.
4. **Current truth.** Facts use valid time plus recording time. Resolution order
   is explicit supersession, authority rank and then an optional same-authority
   tie break. Equal authoritative disagreement is returned as a contested set;
   provenance alone never chooses truth.
5. **Parallel writes.** Runtime records are immutable and uniquely named. A
   separate atomic `.vercy/write.lock` lease serializes local writers and object
   revisions require `--expected-head`. `vercy.lock` is documented as version
   pinning only. Competing heads created on separate Git hosts fail validation
   until an explicit merge revision exists.
6. **Compatibility.** Dimension schema version and skill version are separate.
   `compatibility.yaml` declares supported readers. Migration is dry-run by
   default, rejects ambiguous non-empty legacy registries and records the applied
   0.2/0.3 to 0.4 bridge without rewriting semantic instance facts.
7. **MCP.** A zero-dependency read-only stdio MCP server implements stable
   protocol `2025-06-18`, deterministic `tools/list`, structured tool results and
   four closed-world tools: search, get object, related objects and events.
8. **Evidence.** The paired Claude Sonnet 5 benchmark ran three fresh,
   non-persistent, tool-free trials for each condition. Both Vercy retrieval and
   flat notes scored 15/15. Vercy supplied 43,456 characters versus 103,213
   (57.9% fewer). This is parity with smaller context, not proof of universal
   superiority; cost is not compared because provider caching made order matter.

## Strategic boundary

The proof-first path is now: one core runtime, one maintained reference preset,
one populated Dimension, reproducible measures, and demand-driven catalogue
growth through the existing resolution API. The large catalogue remains a
library and backlog; its size is not itself evidence that the runtime works.

## Remaining work

- reproduce the paired benchmark with other model families and larger fixtures;
- add rollback fixtures and multi-host Git merge simulations;
- complete preset/recipe schemas and independent compatibility tests;
- implement and round-trip-test MongoDB and MCP-database bindings before calling
  them complete;
- add hosted one-click validation only after authentication, abuse and privacy
  boundaries are designed;
- continue model catalogue growth from observed API demand rather than breadth
  targets alone.
