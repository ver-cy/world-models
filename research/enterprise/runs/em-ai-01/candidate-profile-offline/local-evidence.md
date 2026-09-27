# EM-AI-01 local synthesis

## Disposition

- Reuse WM-AI-001 for AI System, WM-AI-002 for durable AI Agent definition, WM-AI-005 for immutable Prompt / Agent Configuration revisions and WM-AI-004 for individual inference or agent runs.
- Do not create new models for ToolBinding or InferenceEndpoint. ToolBinding is a declared/standing/invoked relation across configuration, agent and run. InferenceEndpoint is a typed reference to the software runtime/network endpoint boundary, declared in configuration and observed in a run.
- Extend WM-AI-005 so each tool grant identifies the exact authorization scopes and resource audience it consumes.
- Extend WM-AI-004 so a run pins both base configuration revision digest and effective configuration digest when overlays or variants apply.
- Keep model artifact/product, tool service and endpoint/runtime identity in their existing external masters.
- Allocate no runtime or model identifier.

## Identity and mastership

AI System is the governed unit of accountability and use context. Model artifacts and software products remain referenced siblings. AI Agent is a durable actor/role definition with autonomy, goals, tool surface and delegation constraints. Configuration is a content-addressed immutable operational revision. Run is one bounded execution and references the agent plus exactly one effective configuration.

Configuration, run, model, agent, endpoint and tool service never mint each other's identifiers. Dates, hostnames, endpoints, trade names and trace IDs are correlation or attributes, not keys.

## Tool and endpoint bindings

ToolBinding has three views:

- configuration grant: tool contract/schema digests, server, scopes, audience, effect class and gates;
- standing agent capability: vetted descriptor digest and reapproval-on-drift policy;
- run invocation: call ID, arguments, result, error class and authorization/approval evidence.

The tool/service itself stays mastered outside these records. A tool call is permitted only by the intersection of configuration grant, agent binding, delegated scope and token/resource audience.

InferenceEndpoint is declared by a configuration and observed by a run, including requested and responding model, serving region and runtime address. Its identity belongs to the runtime/network endpoint master; changing the endpoint does not change agent or configuration identity unless configuration content itself changes.

## Authority, delegation and oversight

The accountable subject is always a referenced human, organization or operator. An AI agent is not automatically a human or legal person. `role=agent` is never an authorization input.

Authority enters through a recorded delegation grant, bounded scope, resource audience, validity window, non-delegable exclusions and per-request policy decision. Every delegation hop narrows or preserves authority and remains within a maximum depth.

Oversight is expressed at system, agent and configuration levels and evidenced at run time, including the decision, decider and information shown. Destructive or open-world tools require the configured gate and cannot rely on vendor annotations as trusted authorization.

## Reproducibility scenario

One Agent A uses configurations C1 and C2 for model versions M1 and M2 and tools T1 read-only, T2 destructive and T3 open-world. Each run pins the effective configuration digest, requested/responding model, tool catalogue snapshot, grants/scopes, ordered trajectory, approvals and outputs. T2 calls retain human-approval evidence; T3 remains narrowed to its resource scope. A sub-run records its delegation chain. Model changes create configuration successors while Agent A keeps its identity.

## Invariants

1. Configuration ID and Run ID are distinct.
2. Delegated authority is never broader than the grantor's authority; exclusions and depth limits persist.
3. An AI subject is not created as a human or legal person.
4. Effective tool authority is the intersection of all applicable grants and audiences.
5. Every run pins exactly one immutable effective configuration digest.
6. Agent identity is stable across model changes; configuration identity changes.
7. Endpoint is declared/observed here but mastered elsewhere.
8. Role labels do not grant authority.

## Holds

Endpoint and tool/service references must be reconciled with WM-SFT-018/010, WM-SFT-003 and service boundaries; the AI-01/03/04/07 field-level crosswalk is incomplete; all four base models retain source-pin, ISO, deprecated MCP and development-telemetry holds; per-tool scope and overlay-digest extensions need multi-profile validation and fixtures. This checkpoint makes no canonical completeness, installability or publication claim.
