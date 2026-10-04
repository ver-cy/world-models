# Verdict

**PROFILE**, for both halves, with no identifier allocated.

- **Company** → profile over **WM-ORG-001** (constrained Organization view). No independent identity.
- **EnterpriseGroup / GroupMembership / BusinessBoundary / BrandAssociation** → profile over **WM-ORG-012**, with an alignment pointer in WM-ORG-001. A reusable group-boundary profile is expressible over WM-ORG-012 without a new model; a split trigger is stated below and is not currently met.

Not REUSE ONLY: the profile must add a kind vocabulary, perimeter-scope constraints and prohibition rules that neither spec states. Not COMPLETE RESERVED MODEL: no reserved model exists here. NEW MODEL CANDIDATE is held in reserve behind the split trigger, unallocated.

# Evidence state

Both targets are `reviewable-draft`, `publishableCanonical: false`. WM-ORG-001 is dual-provider with seven publication holds and a seam deferral; WM-ORG-012 is a single-provider Codex waiver with no independent external review and no executable schema, fixtures or source pins. Registry `mapping_status` for both is `conceptual-candidate`; WM-ORG-012's `evidence_depth` is index-and-publication-metadata only. Selected findings are a keyword projection; the SHA-256 and byte counts pin the full specs, which I have not read. This verdict is therefore a boundary disposition, not a crosswalk confirmation.

# Identity and boundary

Company fails the independent-identity test. Its v1 candidate fields land entirely inside WM-ORG-001: `business_name` → name-kind trading/DBA in `name-forms-and-validity`; `purpose` → `declared-purpose-and-scale`; `industry` → `activity-and-statistical-classification`; `operating_scope` → `locations-sites-and-channels` plus `statistical-unit-alignment`. WM-ORG-001 already admits companies, NGOs, branches, funds, sole proprietors and informal collectives under one subject with `entity-category` and `legal-personality-flag` as applicability switches. "Company" is that subject filtered to commercial legal forms — a constrained view, not a new lifecycle. The business/legal-person question ("when are they one object?") is answered by the existing category plus personality flag, not by a second identity.

Separation the profile must keep explicit, each already carried by one of the two specs: legal entity (`entity-category`, formation, standing); business organization (declared purpose, activity, presence); brand (name-kind, and WM-ORG-001 excludes trademark rights); franchise network (WM-ORG-012 collaboration scope); management perimeter (WM-ORG-012 scope dimensions); accounting consolidation perimeter (`controlBasis.accountingStandard`); ownership/control graph (`control-interest`, BODS interests); statistical enterprise group (`statistical-unit-type` + `statistical-register-ref`, alignment only). Eight distinct perimeters, no shared key.

EnterpriseGroup likewise fails independent identity today. It has no formation act, no registration standing, no filing obligations and no succession of its own — only a name, a basis, a purpose and an interval over a member set. That is a purpose-qualified projection, and WM-ORG-012 already models exactly that shape: `participant-roles.arity` carries `arrangementRef`, `participantSet` and `pairwiseLoss`, and the scope statement requires retained membership context for multi-party arrangements.

# Group membership and perimeter contract

The required five elements map onto WM-ORG-012 without gaps:

- **basis** → `recognition-basis.basis` (instrumentRefs, jurisdiction) + `control-interest.controlBasis` (type, definition, accountingStandard)
- **purpose** → `relation-identity.kind` (scheme, version, code, exclusions) + `relation-identity.scope` (dimensions, values, parallelRelationshipRefs)
- **effective interval** → `relationship-time.validTime`, with `knowledgeTime` and `closure.meaning` separating real-world end from record retirement and from correction
- **evidence** → `assertion-evidence` (source, recordRef, retrievedAt, validation; plus `dispute` and `absence` reason codes)
- **authority** → `recognition-basis.positions` (claimant, capacity, counterpartyPosition) + `relationship-stewardship` (master, steward, reviewDue)

`boundary_basis` and `consolidation_basis` become constrained values of `kind` and `controlBasis`; `effective_period` is `validTime`; `group_name` is a label on the arrangement, non-identifying and non-resolving. The perimeter is a derived set: membership records are the facts, the boundary is a query at a declared `asOf` using `graph-interpretation.derivation` (inputRefs, ruleVersion, outputKind), reproducible separately from asserted data.

# Brand/rebranding/succession

WM-ORG-012's recognition finding already asks for evidence "rather than merely common branding, a shared address or an unverified marketing statement" — the negative case is anticipated in the source spec. The profile hardens this into a prohibition: a brand edge carries `controlBasis.type = not-asserted` and may never appear in a consolidation or control derivation input set. WM-ORG-001's `external-affiliation-and-accreditation` supplies the parallel organization-side rule that affiliation is neither ownership nor control.

Rebranding: a name change is a `lifecycle-event-records` entry with a `former-name-entry` and `continuity-decision = identity preserved`. No new organization record, no identifier reassignment, no membership change unless the basis itself changed. Merger, split and sale route through `succession-and-continuity` (predecessor/successor refs, transition cardinality, rule applied). Memberships do not auto-transfer across a split: each successor's membership must be re-asserted with its own basis, interval and evidence.

# Mastership reconciliation

WM-ORG-001's adjudication retained organization-side control endpoints only, and its deferred item explicitly says to re-test the seam "at sibling registration time." WM-ORG-012 is now registered. The trigger has fired, so the profile must assign mastership rather than leave both sides asserting.

Proposed split: WM-ORG-012 masters the relationship fact — `relationship-type-code`, `relationship-period`, `relationship-quantifier` and BODS interest quantum are duplicates of `control-interest` and `relationship-time` and must be demoted in WM-ORG-001 to a non-authoritative, derived endpoint index. WM-ORG-001 retains `reporting-exception-reason`, which is an organization-side reporting obligation about the organization, not a relationship fact. WM-ORG-001's `record-stewardship-and-change-authority` already carries "Master copy system" per field group, so this declaration needs no new structure.

Registry inconsistency to resolve first: `vr.wm-org-012` records `parent_ids: WM-ORG-001` while the spec's own boundary note says "a relationship is not either organization" and its composition edge is REFERENCE. Structural parentage would make a perimeter owned by one member, contradicting the third proposed invariant.

# Invariants

1. Basis, purpose, effective interval, evidence and authority are all required on every membership; any missing one is recorded as a typed `absence` reason, never as an empty value.
2. A brand association or shared name is never admissible evidence of control, legal identity or consolidation, and is excluded from derivation inputs.
3. A perimeter assigns no mastership over any member fact; membership confers no authority to bind a member.
4. Statistical or consolidation units never drive merging or splitting of organization records (carried forward from WM-ORG-001 verbatim).
5. Rebranding preserves organization identity; only an explicit `continuity-decision` may create or terminate a subject.
6. Parallel memberships under different bases coexist via scope dimensions and never overwrite one another.
7. Derived perimeter edges are labelled, time-stamped and reproducible; asserted and derived are never merged.

# Scenario walkthrough

**Negative.** Three organizations share one brand. Collapse is blocked at four independent points: `entity-resolution-and-duplicates` requires comparison evidence, method, confidence and an explicit `resolution-decision`, and a brand string is not a scheme-qualified identifier; `name-kind` separates trading from legal name across three registry entries; the statistical-alignment prohibition forbids merge; and WM-ORG-012 rejects common branding as recognition evidence. Existing structure blocks the case — no new model is needed to prevent it.

**Acceptance.** Franchise network: star graph of brand-licence edges, `controlBasis` not asserted, no accounting standard, `boundary.excludedAuthorities` recording that franchisees cannot bind the franchisor. Holding group: DAG of consolidation edges with accounting standard, interest value with denominator, class and `asOf`, and distinct relationship/accounting/filing periods. A franchisee that is also a subsidiary appears in both graphs as parallel relationships, distinguished by scope. Rebranding the network changes name forms and brand-edge scope; it creates no organization and moves no member between perimeters.

# Profile or candidate shape

Profile artifacts, none normative: a governed `boundary_basis` code list (legal-control, accounting-consolidation, management, brand-licence/franchise, statistical, contractual-alliance) with mutual exclusions; a required-element constraint over the five membership fields; the seven invariants as machine-checkable rules; a per-field-group mastership declaration for the WM-ORG-001/WM-ORG-012 seam; and the two scenario fixtures above as acceptance tests.

**Split trigger** — promote to a new model candidate only when a perimeter (a) holds a registry-issued identifier with its own standing and filing obligations as a party in the adopting Dimension, not merely an alignment pointer; or (b) bears facts attaching to no membership and no member, such as group-level statements, obligations or succession; or (c) must occupy an endpoint in WM-ORG-012, whose endpoints are organization references today. The statistical enterprise group's register-assigned unit identifier is the nearest miss and stays alignment-only under WM-ORG-001.

# Gaps and publication holds

No legal effect, canonical status, approved relation or installability is claimed here; this is a reviewable boundary opinion over draft inputs. Blocking holds: WM-ORG-012 has no independent external review, no source pins and no fixtures, so the profile cannot be published as evidenced; the seam reconciliation changes WM-ORG-001 and reopens its adjudication; the registry `parent_ids` conflict must be resolved; trademark and brand rights are out of scope of both specs and point to an unidentified brand/IP model; franchise-specific and jurisdictional control definitions remain adopter-owned; and the full crosswalk against the pinned 301,830-byte and 95,392-byte specs has not been performed.
