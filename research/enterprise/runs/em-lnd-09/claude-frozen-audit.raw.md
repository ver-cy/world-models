**Verdict:** ACCEPT WITH LIMITS

**Critical findings**

1. *Digest under-pins evidence.* Clause 8 pins agreement/expression, obligation, as-of, lens, policy decision, disclosure shape and graph-engine revision — but not the record authority identity or the evidence-reference revision. With clause 2's open alternative ("WM-REC-001 **or the applicable record authority**"), the same projection key can resolve different E reference sets. The key is access-safe but not fully deterministic as written.
2. *Record-authority resolution unspecified.* No rule states who determines the applicable authority when it is not WM-REC-001. Evidence mastership is therefore ambiguous at the edges, though never claimed by WM-XCT-029.
3. *Profile/projection mastership unstated.* Agreement, duty and edge mastership are unambiguous (ECO-006 / XCT-029 / XCT-029 associations). The owner of the profile definition, disclosure shape and graph-engine contract is named nowhere.
4. *Read-only vs. cycle surfacing (clause 4).* Surfacing decomposition cycles to WM-ACT-034 must be an out-of-band signal. If it writes a marker, flag or assessment edge into the projection, clauses 1 and 4 conflict.
5. *Hiding can leak or imply (clause 9).* Hiding a node while retaining its typed edges yields dangling edges that disclose the hidden node's existence; "never fabricate" forbids placeholder substitutes. No closure rule is given. Likewise, clause 6 forbids computing a legal winner, but ordered graph layout can imply precedence.
6. *Deadline determinism (clause 5).* Calendar, timezone and clock basis for due assessment are unpinned, so boundary-case overdue results are not reproducible from the digest.
7. *Dual naming (clauses 1, 10).* "Contract Landscape" and "Obligation Network" name one artifact. No identity is created, but the pair invites later registration as two entries.

No contradiction renders a held profile unsafe. Survival (clauses 3, 7) is coherent: expiry ends the agreement lifecycle only, surviving duties retain historical source references, evidence stays addressable under its authority, and nothing is deleted, remastered or disclosed more broadly (clause 9).

**Required holds**

- H1: Pin record-authority identity and evidence-reference revision in the digest; fail closed when absent.
- H2: Specify the record-authority resolution rule; forbid WM-XCT-029 from mastering evidence content.
- H3: Name the master of the profile definition, disclosure shape and graph-engine contract.
- H4: State that cycle surfacing is non-mutating and produces no projection artifact.
- H5: Add a disclosure closure rule — hidden nodes hide incident edges; no placeholders; rendering order carries no precedence semantics.
- H6: Pin calendar/timezone/clock basis for deadline evaluation; mark overdue as derived-at-read, never stored as authoritative.
- H7: Declare the digest lens-scoped; cross-lens digest inequality is not evidence of content difference.
- H8: Fix one canonical profile name with "Obligation Network" as a declared rendering mode.

**Scenario result**

Passes with holds. At t_after the authorized lens correctly shows A expired, C and R in force, typed dependencies intact and E referenced under shape control; the non-party is denied; nothing is deleted or remastered. Reproducibility of the E reference set is not yet guaranteed (H1, H2).

**Identifier decision**

`newRuntimeId=false` confirmed. No hidden aggregate: Landscape and Network are one projection, grouping nodes are identity-less rendering constructs, and no profile-level or portfolio master is created.
