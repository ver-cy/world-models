# Additional ownership and delegation comparison

EM-XCT-07 research note, 22 September 2026. This is Codex analysis, not a completed Claude study or a joint approval. Exact retrieved files and their hashes are in `ownership-comparison-pins.json`.

## Decision for the provisional first increment

Do not create a second DelegationMandate master. Refer to a host-owned, versioned authority basis where the host supports one; retain a separate, freshly evaluated execution decision for every attempt. A referenced mandate, owner label, signature-shaped field or prior decision is not authorization. The bounded example can demonstrate a direct represented-principal relationship in trusted synthetic policy; it cannot claim credential verification or general delegation-chain validation.

An Enterprise Fact Authority WriteGrant cannot be reused as an action execution grant. Its scope is admission of a source's observations for a particular scope and predicate. Calling both concepts a write permission would erase the semantic boundary that the existing code enforces.

## Evidence and read scope

- [WM-XCT-001 Ownership / Stewardship](https://ver.cy/models/wm-xct-001-ownership-stewardship/spec.yaml), 0.3.1-enterprise.1, SHA-256 `fa942556a3f460729db2e94b24d1efd4d33ee2e5fb0b1deed3ce040756acf474`: read its full model boundary, composition, sixteen declarative functions, publication metadata and holds, agent instructions and Enterprise companion declaration. Read the complete findings `delegation-mandate-scope` and `mandate-verification-revocation`, including questions, data and artifacts. This is a selected additional comparison, not a claim to have freshly read all thirty-one findings, all source texts or all legal domains in the current ownership release.
- [Enterprise Fact Authority](https://ver.cy/models/wm-xct-001-ownership-stewardship/profiles/enterprise-fact-authority/0.1.0/spec.json), 0.1.0, SHA-256 `cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582`: read the full model-spec, boundary decision, executable authority.py, closed JSON schema, whole-object coverage, mastership and rights, composition, crosswalk, migration, adoption limits, review and agent guide. Inspected the test inventory and actual fixtures/tests for ownership versus writing, stewardship versus governing, source rank versus write grant and replay. The existing test report says 53 tests; these tests were not rerun during this comparison. Downloaded acceptance files were pinned, but not exhaustively reread or rerun here.
- Twenty-one exact public files matched their canonical local counterparts. Retrieval is not itself reading or validation. Full predecessor reviews of WM-XCT-002 and WM-XCT-029 are separately documented in `parent-comparison.md`; do not generalize their completed read scope to WM-XCT-001.

## Semantic overlap and limits

| Existing concept | Existing meaning and behavior | EM-XCT-07 treatment |
|---|---|---|
| Control assertion | Time-bounded, source-backed, contestable holding/control over another object; legal, beneficial, custodial, administrative and technical modalities are distinct. | External basis reference. Neither a copy of the control register nor an assertion of legal validity. |
| Delegation mandate | Named powers bounded by an issuing control position, time/purpose/object extent and explicit subdelegation limits. Retains delegate and represented party attribution. | Reuse as a possible external authority-basis concept; no duplicate master in the first increment. |
| Mandate verification record | Evidence of what a relying party checked, when, against which status source and with which result; revocation effective and publication times can differ. | An action attempt may reference this evidence. Current authorization is still a host obligation; the reference is not a capability token. |
| `verify-delegated-authority` | Declarative verification procedure and artifact requirements; the ownership boundary explicitly excludes runtime policy evaluation and enforcement. | No executable import or claim that Vercy already verifies an arbitrary mandate chain. |
| FactAuthority | Accountable party for values in an exact scope/predicate, governed by trusted configuration. | Optional reference for the affected data; not permission to execute an action on it. |
| StewardshipAssignment | Identified part of a FactAuthority revision with operational duties such as resolving conflicts. | No implicit execution or subdelegation power. A steward may also have a separate host grant, but role coincidence proves nothing. |
| MastershipRule | Relative source precedence in selecting supported observations. | Never a permission, nor proof that a source is true. |
| WriteGrant | An identified part authorizing named writers to admit observations from one source in an exact authority scope, with time/evidence constraints. | Do not widen to modifying resources, calling APIs or acting on behalf of a company. |
| TrustedConfiguration | External trusted governance/read root with scoped governors, readers, purposes and validity. Caller-provided JSON cannot establish trust. | Reuse the explicit host-trust principle, not the same schema for unrelated action grants. |
| FactObservation | Immutable revision history of source assertions; writer changes may be authorized without changing source/subject identity. | Action outcome observations are Event profiles with their own meaning. They do not replace this value authority register. |

The ownership prose assigns runtime permission evaluation to an access neighbor, whereas the actual WM-XCT-002 release is expressly limited to READ/DISCLOSE. Therefore the two parent descriptions do not establish a shipped general execution authority service. This is a boundary gap to implement or defer explicitly, not an inheritance shortcut.

Fact Authority's native register is a real governance aggregate, not a template to create artificial aggregate hosts for every action. Its historical 0.1.0 documents predate the standalone catalog projection now visible at `/models/enterprise-fact-authority/`. Preserve those immutable historical bytes; distinguish the old packaging statement from today's catalog visibility. Its semantic ownership basis pins 0.3.0 even though the current associated ownership publication is 0.3.1-enterprise.1.

## Consequences for identity and current rights

1. The immutable request contains the intended actor, represented principal, executor, exact definition revision, resource revision, purpose and ordered parameters. A retry binds that intent. The authority decision's fresh timestamp or policy revision must not alter the intent digest.
2. A request may retain an external basis reference as historical context. The host must verify the current standing and non-widening scope at the execution boundary. A different current decision can authorize a retry of the same intent; an invalidated basis can deny it.
3. Current execution and result disclosure are separate. Ownership and a prior execution decision do not grant read access to cached receipts, diagnostic differences or existence probes.
4. An executor's receipt is evidence of the bounded operation, not automatic discharge of an obligation. A corrected observation changes knowledge, not the effect that occurred.
5. A startup can use the same party in several roles. A matrix example must evidence a unit's representation independently of an employee's title. An AI proposal carries no power until an authenticated host accepts a scoped request and authorizes execution.

## Explicitly deferred

Arbitrary-depth subdelegation, impersonation, collective or substitute legal capacity, cross-organization authority discovery, cryptographic credentials, offline revocation grace rules, rights adjudication and distributed policy/effect transactions remain outside the first synthetic implementation. A later mandate adapter requires its own whole-parent comparison, primary-source checks, schemas, negative tests and independent audits.
