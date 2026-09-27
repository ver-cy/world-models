# EM-AI-01 local synthesis

## Disposition

- Reuse WM-AI-001 for AI System, WM-AI-002 for durable AI Agent definition, WM-AI-005 for immutable Prompt / Agent Configuration revisions and WM-AI-004 for individual inference or agent runs.
- Do not create new models for ToolBinding or InferenceEndpoint only when external grant/approval and runtime/network masters prove the identity and lifecycle conditions stated by the reconciled profile.
- Keep WM-SFT-004 as the referenced model-artifact master; configuration pins its immutable version and the run observes the resolved version.
- Extend WM-AI-005 so each tool grant identifies the exact authorization scopes and resource audience it consumes.
- Extend WM-AI-004 so a run pins both base configuration revision digest and effective configuration digest when overlays or variants apply.
- Keep model artifact/product, tool service and endpoint/runtime identity in their existing external masters.
- Allocate no runtime or model identifier.

## Identity and mastership

AI System is the governed unit of accountability and use context. Model artifacts and software products remain referenced siblings. AI Agent is a durable actor/role definition with autonomy, goals, tool surface and delegation constraints. Configuration is a content-addressed immutable operational revision. Run is one bounded execution and references the agent plus exactly one effective configuration.

Configuration, run, model, agent, endpoint, grant and tool service never mint each other's identifiers. Model-version, tool-set, endpoint-reference and runtime attenuation changes preserve Agent identity. Accountable-authority, purpose or trust-domain changes create a new Agent by default unless an explicit governed transfer preserves it. Dates, hostnames, endpoints, trade names and trace IDs are correlation or attributes, not keys.

## Tool and endpoint bindings

ToolBinding has three views:

- configuration grant: tool contract/schema digests, server, scopes, audience, effect class and gates;
- standing agent capability: vetted descriptor digest and reapproval-on-drift policy;
- run invocation: call ID, arguments, result, error class and authorization/approval evidence.

The tool/service itself stays mastered outside these records. A tool call is permitted only by the action-time intersection of principal rights, an independently identified unrevoked grant, agent binding, declared tool scope, delegated scope, exact audience, approval and effective configuration. The observation records the grant and approval revisions, invocation and revocation-effective times, allow/deny result and one deterministic UTC ordering rule.

InferenceEndpoint is declared by a configuration and observed by a run, including requested/responding model, serving region, runtime address and serving digest. Its identity belongs to the runtime/network endpoint master only if that master identifies the destination and the configuration pins the serving contract. URL equality is not serving identity.

## Authority, delegation and oversight

The accountable subject is always a referenced human, organization or operator. An AI agent is not automatically a human or legal person. `role=agent` is never an authorization input.

Authority enters through a recorded delegation grant, bounded scope, resource audience, validity window, non-delegable exclusions and per-request policy decision. Every delegation hop narrows or preserves authority and remains within a maximum depth.

Oversight is expressed at system, agent and configuration levels and evidenced at run time, including the decision, decider and information shown. Run authority equals the Agent's governed authority unless an effective governed transfer is cited. Destructive or open-world tools require the configured gate and cannot rely on vendor annotations as trusted authorization.

## Reproducibility scenario

One Agent A uses configurations C1 and C2 for WM-SFT-004 model versions M1 and M2 and tools T1 read-only, T2 destructive and T3 open-world. Each run pins derived, non-identifying SHA-256 digests over canonical bytes using `vercy.ai.config.base.v1` and `vercy.ai.config.effective.v1` domains, plus model, tools, authorization decisions, endpoint resolution, approvals and outputs. R1 cannot invoke T3. Revocation blocks later calls without rewriting earlier observations. Model changes create configuration successors while Agent A keeps its identity.

## Invariants

1. Configuration ID and Run ID are distinct.
2. Delegated authority is never broader than the grantor's authority; exclusions and depth limits persist.
3. An AI subject is not created as a human or legal person.
4. Effective tool authority is the intersection of all applicable grants and audiences.
5. Every run pins one immutable configuration revision plus derived, non-identifying base and effective digests.
6. Agent identity is stable across model changes; configuration identity changes.
7. Endpoint is declared/observed here but mastered elsewhere.
8. Role labels do not grant authority.

## Holds

External grant/approval and endpoint masters must prove the conditional relation contract; endpoint and tool/service references require reconciliation with WM-SFT-018/010, WM-SFT-003 and service boundaries; the AI-01/03/04/07 field-level crosswalk is incomplete; all four base models retain source-pin, ISO, deprecated MCP and development-telemetry holds; per-tool scope, serving-contract and digest extensions need multi-profile validation. Grok reconciliation and the frozen audit are complete. This checkpoint makes no canonical completeness, installability or publication claim.
