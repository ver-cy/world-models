Independent review: EM-AI-01 AI System, Agent and Execution

Review of the stated reuse contract only. WM-AI-001/002/004/005 field lists were not in evidence. Public analogs (WIMSE AIMS, SCITT AIR, Entra/Foundry agent identity, OAuth audience/delegation) are challenge material, not substitutes. No identifiers invented. Not canonically complete.

Verdict. Conditional accept of reuse: WM-AI-001 for AI System, WM-AI-002 for durable Agent, WM-AI-005 for immutable configuration revisions, WM-AI-004 for runs. Conditional accept of no new masters named ToolBinding or InferenceEndpoint. Reject the stronger claim that “declared in configuration, vetted on agent, observed on run” is complete. That lifecycle split is right; it is not a typed home for grants with exact scope/audience, serving-contract pins, approval/revocation across revisions, or dual digests. Agent identity stability is load-bearing and is not implied by “reuse WM-AI-002” unless 002 is already an assigned durable subject. Treat reuse as a contract to verify, not as confirmed mastership.

Identity / mastership. Mastership sits on durable principals, not executions. System is the capability envelope. Agent is the durable actor identity: assigned, not derived from config digest, model version, tool set, endpoint URL, grant, or run. Accountable authority is a referenced human, organization, or operator. role=agent grants nothing; identity is not authority. Config revisions and runs are not identity masters.

Challenge to stability: “durable agent” is only true if identity-preserving versus identity-breaking change is written. Default preserving: model-version swap; add/remove tools under a new revision; endpoint-ref change; run-time grant attenuation. Default breaking: change of accountable authority, purpose/mission, or trust domain — those mint a new agent, not a new revision of the same one. Transfer of the same agent to a new operator is a governed exception and must be explicit. Anti-patterns that fail the required scenario: agent-id = hash(config); new agent per model version; session/run as agent; rotating identity on grant or endpoint change; collapsing agent into system. WIMSE/AIMS requires a workload identifier stable for the identity lifetime; Foundry-style agents survive blueprint change. Config digest proves behavior; it must not be identity.

System / model / agent / config / run. Stack is directionally right: System contains agents; Agent is referenced by immutable ConfigRevision; Run observes Agent + revision + resolved model, tools, and endpoints. Agent must not collapse into System. One system, many agents; agents are the subjects of grants and runs.

Gap: the required heading includes model, but the reuse list has no model master. The scenario needs two model versions. Either versions already live on an existing catalog (cite it; do not invent) or they are only pins inside WM-AI-005. If only pins, model identity cannot be queried, approved, recalled, or compared independently of a config blob. ConfigRevision must pin model-version ref, typed tool declarations, endpoint uses, policy/grant refs, and a base digest. Run must record stable agent-id, revision-id, base digest, effective digest, observed tool invocations, observed endpoint resolution, acting authority, and that role=agent contributed no grant.

Tool binding. Declare / vet / observe is the correct lifecycle, not a reason to make binding an opaque blob. Refuse a ToolBinding master only if all hold: (1) WM-AI-005 carries a typed binding list — tool ref, grant ref, declared scope set, declared audience, required approval class — not digest-only text; (2) grants are first-class enough to have identity, exact scope, exact audience, approval lineage, and revocation independent of a config pin; (3) Agent records vetting of those bindings by whom, against which grant; (4) Run observes the used binding — tool, grant-id, scope exercised, audience of the call/token, allow/deny, and whether the call was inside the vetted set.

If grants are only config text, the no-new-model decision fails. A binding that outlives C1→C2, is shared across agents with different scopes, or must be revoked without publishing a new revision has no typed home. Cross-agent inventory (“which agents may write to T3”) then requires parsing every revision. Prefer extending grants over minting a fifth AI master. Per-tool permission, RFC 8707-style audience, standing versus on-behalf-of grants, and approval history that spans revisions must not be lost.

Endpoint. Refuse an InferenceEndpoint master only if runtime/network masters already identify the serving destination (authn, tenancy, region, network identity) and 005 pins the AI serving contract (model-version ref, tokenizer/parser class, context window, tool-call protocol, safety-filter pin, rate class) and 004 observes the resolved endpoint plus serving digest. Network masters usually carry location and TLS, not serving identity. The same URL can serve a different contract after a provider or parser swap. Declared endpoint may be a logical name; the run must record what was actually reached. Declared ≠ observed is allowed and is why dual digests exist. Model versions are not endpoints. The inference surface is a resource the agent authenticates to, not an accountable actor; credentials must not be visible to the model.

Authority / delegation / oversight. Accountable authority remains a referenced human/organization/operator on the agent and is copied onto every run. Standing authority lives there. The agent may hold grants issued by that authority; it may not originate them. Delegation is an explicit, attenuated, audience-bound, revocable grant. Agent-to-agent spawn must nest actor identity and must still terminate at the human/org/operator, not at role=agent. An agent-role attempt to approve, grant, or delegate is inert.

Oversight of material tool actions requires an approval bound to agent, tool, grant, audience, and revision class. Publishing a config is not approval. Effective authorization at action time is the intersection of principal rights ∩ agent-held grant ∩ tool scope ∩ audience ∩ unrevoked approval ∩ effective config. Failure of any term is deny. A grant for T1 must not authorize T3. Revoking a grant disables matching calls without minting a new agent.

Reproducibility. Accept base plus effective configuration digests on the run. Necessary, not sufficient. Base digest: canonical hash of the pinned immutable revision as approved. Effective digest: canonical hash of what actually governed the run after grant intersection, approval constraints, disabled tools, runtime overlays, and resolved serving identity. Without both, “ran as approved” cannot be distinguished from silent drift (model swap between approval and run; tool list change; endpoint failover). Reproducibility is replay of declared plus effective configuration and observed bindings, not replay of model weights. A digest is not reviewable without canonical byte sequence, hash algorithm, domain separation, and a rule for whether grants/approvals sit inside or outside the base digest.

Scenario. Held constant: one System, one Agent A, accountable operator H. Do not invent further identifiers.

C1 pinned: model M1; tools T1, T2; grants with exact scope and audience for T1 and T2; declared endpoint use; approvals on C1 and those grants.

R1 under C1: agent-id remains A; records revision C1, base digest of C1, effective digest of R1; observes T1/T2 invocations with grant-id, scope, audience, decision; at least one allow and one deny; agent-role delegation produces no grant; authority is H; observed serving identity is M1.

C2 pinned: model M2; tools T1, T2, T3; T1/T2 grants reused; T3 grant and approval exist only here.

R2 under C2: agent-id still A; base digest of C2 ≠ base of C1; T3 callable only with T3 grant + audience + approval; if T3 is runtime-disabled or a grant is attenuated, effective digest ≠ base digest and A does not change; observed serving identity is M2 even if the network master is the same.

Must fail: minting a new agent because M2 or because T3 was added; treating base digest as agent-id; H missing on R2; agent-role delegation succeeding; R1 invoking T3.

Invariants.

Agent identity ≠ config digest ≠ model version ≠ endpoint URL ≠ run id.
role=agent grants nothing; accountable authority is a referenced human/org/operator on every revision and every run.
Config revisions are immutable; change produces a new revision.
Run records base and effective digests; mismatch is observable, not silent.
Binding declared ⊆ 005; vetted ⊆ 002; used ⊆ 004 and ⊆ vetted.
Grant names exact scope and exact audience; missing either is malformed.
Endpoint is a reference plus serving-contract pin on 005 and a resolution record on 004.
Effective authorization is the intersection above, never the agent role.
Model/tool/endpoint change is identity-preserving by default; authority/purpose/trust-domain change is not.
Revoking a grant does not change agent identity.

Blockers.

WM-AI-001/002/004/005 field lists and current identity keys are not in evidence; reuse cannot be confirmed.
No stated home for the two model versions the scenario requires.
Digest canonicalization unspecified (bytes, algorithm, domain separation, grants in or out of base).
Grant object identity/lifecycle unspecified; if grants are not first-class, refusing ToolBinding is unsafe.
Runtime/network master serving-contract coverage unspecified; if absent and 005 cannot pin model+parser+limits, refusing InferenceEndpoint leaves a hole.
Identity-preserving versus identity-breaking rules are not written.
No clock rule for in-flight runs versus a newly published revision, or for grant revocation versus config pin.
No specified home for approval objects and delegation-chain/intersection decisions on the run.

Close those without minting ToolBinding or InferenceEndpoint masters if grants, serving-contract pins, dual digests, and identity-stability rules can be extended onto the four reused models. If they cannot, the no-new-model decision does not hold — still do not invent identifiers here.
