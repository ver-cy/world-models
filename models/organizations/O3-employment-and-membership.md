# O3 Employment & Membership

This meta-model describes the bilateral relations between persons and organizations: employment in its many forms, membership in associations and communities, the roles held within these relations, and their agreed terms and lifecycle. It is its own model because the relation is jointly owned by two parties and must stand independently of both the person model and the organization model it connects.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:o3"
  csn: world.employment
  version: 0.2.0
  displayName: "Employment & Membership"
  description: "Bilateral employment and membership relations between persons and organizations, with roles, terms and lifecycle."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.employment
bundles:
  - csn: world.employment.relation
    displayName: "Relation"
    layers:
      - world.employment.relation.employmentRelation
      - world.employment.relation.membershipRelation
  - csn: world.employment.terms
    displayName: "Terms"
    layers:
      - world.employment.terms.roleAssignment
      - world.employment.terms.conditions
  - csn: world.employment.lifecycle
    displayName: "Lifecycle"
    layers:
      - world.employment.lifecycle.commencement
      - world.employment.lifecycle.interruption
      - world.employment.lifecycle.separation
imports:
  - source: esco
    version: "*"
  - source: hr-open
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `relation` | The fact of the person-organization bond | `employmentRelation`: paid work relations of any kind · `membershipRelation`: belonging to associations, communities and clubs |
| `terms` | What was agreed within the bond | `roleAssignment`: roles held, with occupation references · `conditions`: term dates, capacity, place of work, notice |
| `lifecycle` | How the bond begins, pauses and ends | `commencement`: start and probation · `interruption`: leave and suspension · `separation`: end of relation and its cause |

## Objects

- `employment`: a relation of work between a person and an organization; key attributes: kind, start date, end date, status.
- `membership`: a relation of belonging; key attributes: membership class, admission date, standing.
- `roleAssignment`: a role held within a relation; key attributes: role reference (occupation code or internal role), position link, validity.
- `engagementTerm`: the agreed terms; key attributes: term dates, renewal rule, notice period.
- `workCapacity`: the time commitment; key attributes: full-time fraction, schedule pattern, validity.
- `interruptionRecord`: a leave or suspension; key attributes: kind, start, end, effect on standing.
- `separationRecord`: the end of a relation; key attributes: date, initiating side, cause category.

## Relationships

- `employment` -> engages -> `world.person` (n:1): the person side of the relation (H1).
- `employment` -> with -> `world.organization` (n:1): the organization side of the relation (O1).
- `membership` -> admits -> `world.person` (n:1): the member, joined to an organization kept in O1.
- `roleAssignment` -> heldWithin -> `employment` (n:1): the relation in which the role is exercised; membership roles bind the same way.
- `roleAssignment` -> occupies -> `establishedPosition` (n:1): the post in `world.organizationalUnit` (O2) the role fills.
- `employment` -> resultedFrom -> `placement` (n:1): the labor market placement in `world.laborMarket` (O6) that produced it.
- `separationRecord` -> closes -> `employment` (1:1): the terminal record of a relation.

## Events

- `employmentCommenced`: a work relation began.
- `membershipAdmitted`: a person was admitted to membership.
- `roleAssigned`: a role was taken up or relinquished within a relation.
- `termsAmended`: agreed terms or capacity changed.
- `interruptionStarted`: a leave or suspension began.
- `interruptionEnded`: the relation resumed.
- `engagementSeparated`: an employment or membership ended.

## Contracts

- `bilateralRecordMirror`: both parties hold and see the identical relation record; joint facts change only by mutual events.
- `engagementVerification`: third party confirmation of existence, role and dates with minimal disclosure, on the person's consent.
- `workforceStatistics`: aggregate anonymized reporting of relations for statistics consumers.

## Projections

- `careerHistory`: the person's chronological view of own relations and roles; omits organization-internal notes.
- `workforceRoster`: the organization's view of current staff and members with roles; omits the person's history at other organizations.
- `verificationCertificate`: existence, role and dates only; omits terms, capacity and cause of separation.

## Composition

- REFERENCE `world.person` (H1): the person party of every relation.
- REFERENCE `world.organization` (O1): the organization party of every relation.
- REFERENCE `world.organizationalUnit` (O2): role assignments occupy established positions.
- COMPOSE `world.laborMarket` (O6): a confirmed placement there composes the initial employment record here.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): joint ownership and access grants over the bilateral record.
- MIX-IN `world.auditTrail` (S4): audit facets on all lifecycle events.
- imports: esco (REFERENCE): occupation and skill codes used in role references.
- imports: hr-open (ALIGN): HR data interchange shapes for relations and roles.

## Stewardship

Each relation is a bilateral record jointly owned by the person and the organization; each side grants access to its own view and joint facts change only by mutual events, per the S1/S2 models of this catalogue.
