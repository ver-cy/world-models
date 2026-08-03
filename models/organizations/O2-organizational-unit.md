# O2 Organizational Unit

This meta-model describes the internal anatomy of an organization: units, their hierarchy and reporting lines, the mandates and established positions inside them, and how the structure changes over time. It is its own model because internal structure evolves on the organization's own cadence, is governed by the parent organization rather than by registrars, and is consumed by employment, charters and procurement without needing full organizational identity semantics.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:o2"
  csn: world.organizationalUnit
  version: 0.2.0
  displayName: "Organizational Unit"
  description: "Internal units, hierarchy, reporting lines, mandates, positions and headcount of an organization."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.organizationalUnit
bundles:
  - csn: world.organizationalUnit.structure
    displayName: "Structure"
    layers:
      - world.organizationalUnit.structure.unitDirectory
      - world.organizationalUnit.structure.hierarchy
  - csn: world.organizationalUnit.mandate
    displayName: "Mandate"
    layers:
      - world.organizationalUnit.mandate.remit
      - world.organizationalUnit.mandate.establishedPositions
  - csn: world.organizationalUnit.evolution
    displayName: "Evolution"
    layers:
      - world.organizationalUnit.evolution.reorganization
      - world.organizationalUnit.evolution.staffingSnapshot
imports:
  - source: w3c-org
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `structure` | What units exist and how they nest | `unitDirectory`: units, their kinds and names Â· `hierarchy`: containment and reporting lines, including dotted lines |
| `mandate` | What each unit is for and who sits in it | `remit`: delegated mandate and scope of each unit Â· `establishedPositions`: posts, grades and the headcount plan |
| `evolution` | How the structure changes | `reorganization`: acts that create, merge, move or disband units Â· `staffingSnapshot`: recorded headcounts over time |

## Objects

- `unit`: an internal organizational unit; key attributes: name, kind reference, validity period, status.
- `unitKind`: a classifier of units (department, branch, committee, team); key attributes: scheme, code, description.
- `reportingLine`: a directed reporting relation between units; key attributes: kind (administrative, functional), validity.
- `unitMandate`: the remit assigned to a unit; key attributes: scope text, source delegation, validity.
- `establishedPosition`: a post seated in a unit; key attributes: title, grade, occupancy status, validity.
- `headcountSnapshot`: a dated headcount measurement; key attributes: date, filled count, established count, basis.
- `reorganizationAct`: a decision that reshapes structure; key attributes: decision date, effective date, affected units, kind.

## Relationships

- `unit` -> belongsTo -> `world.organization` (n:1): every unit resolves to its parent organization (O1).
- `unit` -> partOf -> `unit` (n:1): structural containment forming the hierarchy.
- `unit` -> reportsTo -> `unit` (n:m): reporting lines, possibly distinct from containment.
- `unitMandate` -> assignedTo -> `unit` (n:1): the remit a unit carries.
- `establishedPosition` -> seatedIn -> `unit` (n:1): where a post lives.
- `headcountSnapshot` -> measures -> `unit` (n:1): a dated staffing measurement of one unit.
- `reorganizationAct` -> reshapes -> `unit` (n:m): the units a reorganization creates, merges, moves or disbands.

## Events

- `unitEstablished`: a new unit was created within the organization.
- `unitRenamed`: a unit's name or kind changed.
- `unitReparented`: a unit moved to a different parent in the hierarchy.
- `unitsMerged`: two or more units were combined.
- `unitDisbanded`: a unit ceased to exist.
- `mandateAssigned`: a remit was assigned to or withdrawn from a unit.
- `headcountRecorded`: a staffing snapshot was taken.

## Contracts

- `orgChartDisclosure`: structure-only access for partners, auditors or counterparties.
- `aggregateStaffingReport`: periodic anonymized headcount statistics without position detail.
- `reorganizationNotice`: advance notice of structural change to affected parties.

## Projections

- `orgChart`: hierarchy, unit names and reporting lines; omits mandates and headcount.
- `mandateRegister`: which unit may do what internally; omits staffing data.
- `staffingTrend`: headcount time series at an aggregation level; omits unit detail below a disclosure threshold.

## Composition

- REFERENCE `world.organization` (O1): the parent organization whose structure this is.
- REFERENCE `world.charter` (O4): unit mandates trace to powers delegated under the charter.
- REFERENCE `world.employment` (O3): role assignments there fill established positions here.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): ownership and access grants over structure data.
- MIX-IN `world.auditTrail` (S4): audit facets on reorganization and mandate events.
- imports: w3c-org (EXTEND): organizational unit and reporting semantics specialized by this model.

## Stewardship

The parent organization owns the structure record; units have no standing of their own. Access is granted by the parent organization under the S1/S2 models of this catalogue.
