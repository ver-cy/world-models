# Verdict

**Reuse the four existing models; do not create new masters for ToolBinding or InferenceEndpoint.** EM-AI-01 is a *contour* over WM-AI-001 (AI System), WM-AI-002 (AI Agent), WM-AI-005 (Prompt/Agent Configuration) and WM-AI-004 (Inference/Agent Run). Each of the five separations the brief demands already has exactly one home in that set, and the two candidate types (`ToolBinding`, `InferenceEndpoint`) decompose without residue into findings that already exist across WM-AI-005, WM-AI-002 and WM-AI-004. Two narrow **extends** are required (below). The boundary decision is *reuse + extend*, adjudicable now; it is not publication-ready, and nothing here should be read as canonical completeness or as an installable specification.

# Evidence

All four `vercy_candidates` carry `mapping_status: conceptual-candidate` and `evidence_depth: index-and-publication-metadata`. All four specs are `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, each with unresolved publication holds (EUR-Lex re-verification, ISO 403s, MCP sampling deprecated, OpenTelemetry GenAI at Development stability). That supports a *boundary* decision at conceptual level and forbids a crosswalk claim: the field-level mapping from EM-AI-01's `candidate_properties_from_v1` (AI-01, AI-03, AI-04, AI-07) into named findings has not been executed here and remains a hold.

# Identity/mastership

Mastership is already split cleanly and must stay split:

- **WM-AI-001** — system master identifier (registration entry as typed alias); `candidate_master_systems` "model registry" maps to WM-SFT-004, not here.
- **WM-AI-002** — agent identifier; explicitly forbids transient in-memory instance ids as identity.
- **WM-AI-005** — configuration identifier + immutable revision digest over canonical form.
- **WM-AI-004** — run identifier; trace-id, conversation-id and config digest are correlation, never identity.

No node in this contour may mint an identifier owned by another. Dates, trade names, endpoints and hostnames are excluded as keys by all four artifact rules.

# System/model/agent/configuration/run

Five distinct objects, five distinct identities:

1. **AI system** (WM-AI-001) — the governed unit of accountability; composes model artifacts and may expose agents.
2. **Model artifact / product** — WM-SFT-004 (artifact internals, weights, training provenance) and WM-SFT-002 (software product packaging). Both are *outside* the contour and referenced only.
3. **Agent role** (WM-AI-002) — durable actor definition: autonomy level, goals, tool surface, delegation.
4. **Immutable configuration version** (WM-AI-005) — instruction blocks, decoding parameters, tool grants, scopes, oversight gates, frozen under one digest.
5. **Run** (WM-AI-004) — one bounded execution referencing agent + configuration digest.

The load-bearing constraint: a run references, never redefines. WM-AI-004's boundary notes already enforce this against all three neighbours.

# Tool binding

`ToolBinding` is **not** a new type. It is one relation observed at three tenses, already modelled:

- **Declared/authorised** — WM-AI-005 `tool-grant-and-schema-binding`: tool name + granting server reference + input/output schema digests captured at release + denylist + disambiguation prefix.
- **Standing capability** — WM-AI-002 `tool-and-resource-bindings`: effect class, vetting decision, descriptor digest, re-approval on drift.
- **Invoked** — WM-AI-004 `find-tool-call-record`: call id, arguments, result, protocol-vs-execution error, annotations.

The tool's own definition, operator and hosting stay with the external tool/service sibling (WM-AI-002 records this sibling as having *no registry identifier in the supplied extract* — an unresolved boundary, not a licence to invent one).

**Extend #1 (WM-AI-005):** requested authorization scopes are currently justified per *server binding*, not per *tool grant*. Bind each tool grant to the scope(s) and resource audience it consumes, so least-privilege is checkable per tool rather than per server.

# Endpoint

`InferenceEndpoint` is likewise **not** a new master, and must not duplicate a runtime/endpoint master. It appears in three already-existing places: declarative in WM-AI-005 (`server-binding-and-authorization-scope`: endpoint, transport, scopes, secret handle), observational in WM-AI-004 (`find-model-and-provider-binding`: provider name, server address, serving region, requested-vs-responding model), and as deployment placement in WM-AI-001 (`de-integration-interface`, `de-processing-location`). Endpoint identity belongs to a runtime/service master that is **not present in this dossier**; no identifier may be invented for it. Treat as a typed reference with an unresolved target — a blocking hold, not a new node.

# Authority/delegation/oversight

The accountable subject is a human, organisation or operator resolved by reference: WM-AI-001 operator roles (provider/deployer/importer/distributor), WM-AI-002 `own-accountable-org` and `dlg-principal-ref` into WM-PER-003, WM-AI-004 `de-initiating-principal` and `de-accountable-deployer`. The agent record carries delegation edges, not personhood: WM-AI-002's parent link to WM-PER-003 is a specialisation of a responsibility-bearing actor, and its conflicts register already rejects agent legal personhood.

The negative case — `role=agent` conferring unlimited authority — is defeated structurally, not by policy text: authority enters only through (a) a recorded delegation grant with scope, non-delegable exclusions and validity window, (b) an audience-bound credential, and (c) a per-request policy decision point. A `role` field is nowhere an authorisation input.

Oversight is three-layer: system-level measures and intervention mechanisms (WM-AI-001), agent-level stop mechanism, competence and intervention log (WM-AI-002), configuration-level gates with reviewer disclosure fields (WM-AI-005), evidenced per run (WM-AI-004 `art-oversight-decision-record`, including what the decider was *shown*).

# Reproducibility

Each run pins: configuration revision digest, requested *and* responding model identifiers, tool catalogue snapshot digest, granted scopes and resource indicators, ordered step trajectory, and an explicit reproducibility class. When a model version changes, the pinned `target-model-identifier` changes, the canonical digest changes, and a new configuration revision is released — the agent identity is unaffected.

**Extend #2 (WM-AI-004):** where overlays or variants apply, record both the base revision digest *and* the effective-configuration digest from WM-AI-005's composition graph. Without it, a run under an overlay is not reconstructable. (WM-AI-005 already carries this as deferred research.)

# Scenario

Illustrative labels, not identifiers. Agent **A**; models **M1**, **M2**; tools **T1** read-only, **T2** destructive, **T3** open-world.

- A is one WM-AI-002 record. Configuration **C1** pins M1; **C2** pins M2 — two revisions, two digests, two evaluation evidence sets, one agent.
- All three tools are granted in both revisions; T2 carries a confirmation gate and T3 a narrowed scope, per locally assigned risk class (vendor annotations are untrusted claims).
- Run R1 (C1, T1) → digest C1, scopes, one tool call, no gate. R2 (C1, T2) → same digest, human approval record with presented arguments. R3 (C2, T3) → digest C2, responding model recorded separately from requested. R4 (C2, T2+T3, sub-run) → delegation chain with depth and narrowed scope at each hop.
- Falsification: if R3 and R1 shared a configuration identity, or if A's identity changed with the model, the separation has failed.

# Invariants

1. Configuration ID ≠ run ID; neither mints the other's identity.
2. Delegated authority ⊆ granting principal's authority; non-delegable set preserved at every hop; depth bounded.
3. An ai-subject is never created as a human or legal person; the accountable subject is always a referenced human/organisation/operator.
4. Effective tool authorisation = configuration grant ∩ agent binding ∩ delegated scope ∩ token audience; runtime may narrow, never widen.
5. Exactly one immutable configuration revision digest per run; content change ⇒ new revision, never in-place edit.
6. Agent identity is stable across model versions; a model change produces a new configuration revision.
7. Endpoint is declarative on configuration and observational on run; neither is its master.
8. `role` is never an authorisation input.

# Minimal completion shape

- **WM-AI-001**: system master id; agent-surface edge enumerating linked WM-AI-002 records.
- **WM-AI-002**: agent id; accountable org; autonomy level; delegation grant with non-delegable exclusions; tool bindings with effect class + descriptor digest.
- **WM-AI-005**: revision digest; pinned model; per-tool grant with scope and audience; oversight gates; autonomy/budget caps.
- **WM-AI-004**: run id; agent ref; configuration digest (+ effective digest); responding model; tool call records; scopes used; oversight decisions; terminal state.

# Holds

Unresolved endpoint and tool/service master identifiers; field-level crosswalk of AI-01/03/04/07 properties into named findings; the four models' own publication holds (source re-verification, ISO clause text, deprecated MCP sampling, Development-stability telemetry keys); multi-profile validation of the two extends. Boundary decision is adjudicable; publication is not.
