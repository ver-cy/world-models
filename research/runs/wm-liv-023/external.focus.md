# WM-LIV-023 bounded external research focus

Produce one complete schema-valid result for `WM-LIV-023 Clinical / Biological
Specimen`.

Treat the root as one identifiable physical material specimen or derived
specimen. Keep it distinct from donor or source organism, patient, anatomical
site, collection event, procedure, request, accession record, label, barcode,
container, storage position, observation, assay, laboratory analysis, result,
dataset, consent, permit, material-transfer agreement and repository holding.
Every collection, aliquot, split, pool, extraction, culture, fixation or other
material transformation must preserve typed parent-child lineage and quantity
accounting; a derived specimen receives its own identity.

Cover authoritative and local identifiers, aliases and master system; specimen
kind and profile; physical composition, material type, tissue or substance,
taxon, anatomy and source context; quantity, mass, volume, concentration,
dimensions and units; collection actor, method, body site or location, device,
procedure, time, reason and protocol; received and accessioned time; containers,
additives, preservatives and seals; processing, derivation, pooling, aliquoting
and chain of custody; storage position, temperature, atmosphere, light, humidity
and duration; transport legs, packaging, dangerous-goods and cold-chain events;
availability, reservation, depletion, consumption, destruction and disposition;
preanalytical variables including ischemia, delay, centrifugation, fixation and
freeze-thaw cycles; observations, quality measurements, contamination, volume
or integrity sufficiency, nonconformance and acceptance or rejection; provenance,
audit, correction, duplicate reconciliation, access, consent, lawful basis,
benefit sharing, retention and loss-aware projections.

Retain `WM-LIV-002 Organism Individual` as a common source reference, not a
universal parent. Retain `WM-LIV-024 Biobank / Sample Repository` as the holder
or collection context and `WM-MAT-007 Laboratory Analysis` as a downstream
reference. Do not let any repository, analysis or observation own the specimen.

Support human clinical, veterinary, plant, microbial, environmental,
biodiversity, food and research profiles. Do not infer donor identity, disease,
diagnosis, consent, ownership, fitness for use or absence of contamination from
a specimen type or label. Do not equate current location with custody, custody
with ownership, quality with intrinsic truth, unavailable with destroyed, or
pool membership with loss of contributor identity.

Target 24 official primary sources, 6 bundles, 12 layers, 24 findings, 72
questions, 24 artifacts and 10 functions. Prefer HL7 FHIR R5 Specimen, ISO
20658:2023, ISO 15189:2022, ISO 20387:2018, WHO laboratory quality guidance,
NCI and ISBER biospecimen practices, SPREC 3.0, MIABIS, NCBI BioSample, GA4GH
Phenopackets 2 Biosample, Darwin Core 2026, GGBN, MIxS, OBI, WMA Taipei,
Nagoya Protocol, GDPR, PROV-O, DQV, ODRL, RFC 3339 and RFC 8785. Pin versions
or access dates and expose licensed, changing, jurisdictional and profile limits.
