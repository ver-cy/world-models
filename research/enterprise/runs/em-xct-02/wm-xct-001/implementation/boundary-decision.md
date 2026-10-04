# Boundary decision

**Decision: a separately versioned companion contract, associated with WM-XCT-001 for discovery, with pattern alignment and explicit non-conformance. No new universal WM identifier.** This does not turn fact-type meaning or the truth of values into property ownership. The sole native snapshot subject is an explicitly identified governance-register aggregate in one Dimension, not a predicate or a company.

Claude recommends a WM-XCT-001 application profile; Grok objects that `controllable-object-anchor` excludes abstract predicates and that mastership is outside the control record. Direct byte inspection confirms that exclusion. We accept Grok's objection to subtype semantics: the package reuses named patterns but does not assert that FactAuthority is a ControlRecord. Its public location is an association, not inheritance. WM-XCT-002 explicitly excludes write/modify/delete permissions; our WriteGrant is an original, bounded reference construct, not a claimed implementation of 002. WM-XCT-012 supplies an alignment pattern for assertions, not automatic provenance conformance.

Both researchers distinguish independent assignment identity from party identity. Each StewardshipAssignment, MastershipRule and WriteGrant therefore has a stable URI independent of authority and party. The reference binding versions these records within authority snapshots. A party/source or owning authority change needs a new part ID, with prior rows retained. This is a limited document binding: standalone assignment revisions, cross-authority portability and distributed updates remain deferred, rather than claimed complete. References to a part must carry its ID plus containing authority revision and digest.

| Candidate | Boundary and lifecycle | Owner/source | Disposition and loss |
|---|---|---|---|
| FactAuthority | Appointment accountable for **values** of one scoped single-valued predicate; active/retracted; changes by immutable revision | Scoped governance publisher under a deployment trust anchor; appointment evidence | Bounded original contract aligned to 001. Definition authority is only an external reference, never inferred |
| Stewardship | Identified operational assignment with duties and valid term; recognition depends on active authority | Governance publisher, appointment evidence; party not inferred from model author | Identified nested document record `StewardshipAssignment`. Independent revision stream deferred |
| MastershipRule | Identified source preference for a scope/term, priority lower-is-preferred | Governance publisher, rule evidence | Keep registry name; narrower precedence-only semantics. No write permission or confidence implied |
| WriteGrant | Identified current submission right for named actors attributed to a source | External authenticated host + scoped governor | New reference construct, no 002 equivalence or production enforcement claim |
| FactObservation | Identified source assertion about subject/predicate, asserted/retracted; source+writer+subject stable | Named source via writer; retained evidence | Narrow 012-inspired carrier, not the target object or full provenance graph |
| AuthorityRegister | Stable canonical aggregate for one Dimension, explicit boundary, computed query view | Deployment operator maintains storage; governor owns governance facts; each source owns its assertions | JSON/native snapshot binding, with mandatory companion; not a new subject universe |
| Definition authority, policy administration service, identity/party, legal rights | Own meanings and independent lifecycles | External owners | References/deferred; do not auto-create from these records |

The minimum needs one trusted configuration, one active authority, one source rule, one separate write grant and one observation. Zero stewards is representable and yields an explicit empty route. No mandatory HRIS, ERP or organizational hierarchy. Several authorities may coexist in the archive; overlapping operative authorities return `authority-contested`, never last-writer-wins.

## Runtime boundary after frozen audit

The reference binding installs the companion under `vr.profile.enterprise-fact-authority@0.1.0` using its own specification digest. WM-XCT-001 is semantic-only, binding=null. Hosting URLs remain associated with 001 for discovery but the machine identity no longer claims the parent defines this register type. Source writer is per-revision attribution; the source and subject are stable lineage anchors.
