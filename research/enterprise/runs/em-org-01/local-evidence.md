# EM-ORG-01 local synthesis

## Disposition

- Define **Company** as a constrained profile of WM-ORG-001 Organization.
- Define **Enterprise Group / Business Boundary** as a purpose-qualified profile over WM-ORG-012 Inter-organizational Relationship with endpoint references to WM-ORG-001.
- Create no new model ID. A separate group subject remains an unassigned candidate only if it later gains independent standing, obligations, statements or succession that cannot attach to memberships or members.

## Identity and boundary

A company uses the existing organization identity and lifecycle. Commercial purpose, business name, industry and operating scope narrow WM-ORG-001; they do not create a parallel Company identity. Legal person, business actor, brand, statistical unit and group perimeter remain distinct views.

An enterprise group is a dated, purpose-specific perimeter over organizations. Management, accounting consolidation, ownership/control, statistical enterprise, franchise and contractual-alliance perimeters can coexist and must not share an implicit boundary. The label of a group is descriptive and cannot resolve identity.

## Membership contract

Each membership requires:

- a versioned boundary kind and explicit purpose;
- member and role references;
- valid time and knowledge time;
- recognition/control basis and governing instrument where applicable;
- evidence, claimant capacity and counterparty position;
- source master, steward and review date;
- typed absence or dispute status when facts are unknown or contested.

The materialized group boundary is a reproducible query over membership assertions at an `asOf` time. It records input references and rule version. Derived membership is never merged with asserted membership.

## Mastership reconciliation

WM-ORG-012 should master relationship kind, period, quantifier, direction, endpoint roles and interest/control facts. WM-ORG-001 should retain only organization-side derived indexes and its own reporting exceptions. The current registry `parent_ids: WM-ORG-001` for WM-ORG-012 conflicts with the specification's reference boundary and must be resolved before publication; a relationship cannot be structurally owned by one endpoint.

## Invariants

1. Shared brand, name, site or affiliation never proves identity, ownership, control or consolidation.
2. Membership requires basis, purpose, interval, evidence and authority.
3. A perimeter grants no authority over member facts and cannot bind a member.
4. Different boundary kinds coexist as parallel scoped graphs.
5. Rebranding preserves organization identity.
6. Merger, split, sale and succession require explicit continuity decisions; memberships do not transfer silently.
7. Statistical and consolidation units never merge or split organization masters.
8. Derived perimeters remain labelled, dated and reproducible.

## Scenario result

Three organizations sharing one brand remain three organization identities. A franchise network forms brand-licence edges with no inferred control. A holding group forms a separate accounting/control graph with its own standard, period and evidence. An organization may occur in both graphs. Rebranding changes name history and brand association while preserving organization and membership identity unless the underlying basis changes.

## Holds

Both bases remain non-canonical reviewable drafts. WM-ORG-012 lacks independent external review, executable nested schemas and fixtures. Relationship mastership requires a WM-ORG-001 seam revision, the registry parent conflict remains unresolved, and trademark/brand rights plus jurisdiction-specific franchise/control rules are outside these models. This checkpoint is a profile boundary, not an installable release.
