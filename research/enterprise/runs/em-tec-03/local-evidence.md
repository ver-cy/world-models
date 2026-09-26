# EM-TEC-03 local synthesis

## Disposition

- Complete reserved WM-SFT-003 as the independent, versioned logical **API / Interface Contract**. Its revision or API version is part of the contract's immutable revision series, not a separate model.
- Create no model for ExchangeEvent. Addressed exchanges use WM-REC-003 Message; other occurrences use WM-ACT-015 Occurrence / Event, with references to the contract revision, binding and integration.
- Keep payload meaning and constraints in WM-DAT-004 Data Schema / Data Contract, referenced from WM-SFT-003.
- Keep logical connectivity, address and exposure in reserved WM-SFT-018 Network / Endpoint. EndpointBinding is an effective-dated dependent relation between a contract revision and an endpoint/environment.
- Treat **Integration** as an identifier-unassigned candidate. It has independent identity, accountability and lifecycle across contract revisions and endpoint changes, but no registry allocation exists.
- Allocate no runtime or model identifier.

## Identity and mastership

| Subject | Identity and master |
|---|---|
| Logical interface contract | WM-SFT-003 contract key; contract registry |
| Contract revision / API version | Contract key plus immutable version designation; Git / CI/CD |
| Consumer pin | Consumer, contract and exact revision, with effective period |
| Integration | Own governed key; service/integration register; unassigned candidate |
| Endpoint binding | Contract revision, WM-SFT-018 endpoint, environment and effective period |
| Exchange occurrence | WM-REC-003 or WM-ACT-015 identity; message store / observability |
| Payload schema | WM-DAT-004; data steward |
| Network endpoint | WM-SFT-018; service owner / CMDB |

A contract defines the stable logical surface and governance. A published revision is immutable and declares its compatibility mode. A consumer pin names exactly one revision; unpinned resolution must expose the revision actually selected. Pins drive impact analysis and sunset notices.

Integration is a producer-consumer relationship with purpose, direction, delivery semantics, owners and data scope by reference. It survives contract revision and endpoint changes and may compose several contracts. EndpointBinding changes on the infrastructure cadence and never creates a new contract or integration.

## Compatibility and migration

Compatibility is assessed against the declared mode and relevant historical range. Removing an operation or required element, narrowing a type outside an allowed promotion, adding a read-required element without a default, or changing existing meaning is breaking even if syntax validates. Every candidate revision needs a compatibility result or bounded exception, impact analysis against consumer pins, notice requirements and successor/sunset information when retiring a revision.

## Acceptance scenarios

Changing an API URL creates a new effective-dated endpoint binding and retires the old binding. The contract revision, schema, consumer pins and Integration identity remain unchanged.

Changing payload semantics incompatibly at the same URL creates a new contract revision and corresponding WM-DAT-004 schema revision, compatibility evidence, consumer impact analysis and migration/re-pinning work. The endpoint binding may remain unchanged.

## Invariants

1. Each endpoint binding names one environment and one effective period.
2. Address change alone does not increment contract revision.
3. Contract revision alone does not create a new Integration identity.
4. Integration identity survives revision and binding changes.
5. Each consumer pin names exactly one contract revision.
6. Payload schema is defined once in WM-DAT-004 and referenced.
7. Published contract revisions are immutable.
8. Publication requires an owner, compatibility mode and resolvable schema reference.
9. Exchange occurrences reference the contract revision, binding and Integration; they do not replace them.
10. A syntactic compatibility pass is necessary but insufficient.

## Holds

WM-SFT-003 now has a reviewable completion candidate with immutable revisions, consumer pins, compatibility assessments, endpoint bindings, four external relations and seven fixtures. WM-SFT-018 still lacks a current specification and Integration remains identifier-unassigned. WM-DAT-004 retains its own canonical holds; exact Grok comparison, one frozen semantic audit, package conversion and live verification remain required. This checkpoint makes no canonical completeness or installability claim yet.


## Supporting WM-SFT-018 completion candidate

The reserved Network / Endpoint boundary now owns stable logical endpoint identity plus effective-dated address, connectivity, exposure and zone-membership assertions. Software-system identity stays in WM-SFT-002, runtime/resource identity in WM-SFT-010, contract semantics in WM-SFT-003 and observed traffic in WM-SFT-017. Address reassignment, blue-green migration, URL change, declared-versus-observed reachability, secret rejection and historical resolution are covered by seven fixtures.
