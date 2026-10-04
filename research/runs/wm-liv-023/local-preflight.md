# WM-LIV-023 local preflight

- Sequence: 180
- Registry ID: `vr.wm-liv-023`
- Registered name: `Clinical / Biological Specimen`
- Registry kind: `standalone-mm`
- Candidate subject kind: `entity`
- Registered parent: `WM-LIV-002 Organism Individual`
- Incoming candidate relation: `WM-LIV-024 Biobank / Sample Repository CONTAINS WM-LIV-023`
- Outgoing candidate relation: `WM-LIV-023 REFERENCE WM-MAT-007 Laboratory Analysis`

## Boundary decision

The root is one identifiable physical material specimen or derived specimen.
It is not its donor or source organism, collection event, container, request,
accession record, observation, assay, analysis, result, dataset, consent record
or repository holding. A parent-child derivation creates a new specimen identity
and never overwrites the parent.

The source may be an organism, person, body site, environmental location,
material entity, product or another specimen. The registered organism parent is
therefore retained as a common but not universal reference. Clinical, research,
veterinary, biodiversity, environmental and food profiles must be explicit.

## Primary hazards

- swapping patient, donor or source identities;
- treating an accession, barcode, label or container as specimen identity;
- losing split, pool, aliquot, extraction or transformation lineage;
- confusing planned collection with actual collection;
- inventing source, diagnosis or consent from sample metadata;
- ignoring temperature, ischemia, preservation, transport or freeze-thaw history;
- treating measured quality as permanent intrinsic quality;
- disclosing human, genetic, location or endangered-species context;
- destroying or consuming material without authority and auditable quantity change.
