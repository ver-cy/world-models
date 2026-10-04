# WM-LIV-023 Codex source notes

The synthesis treats `Clinical / Biological Specimen` as one identifiable
physical material entity. A database row, accession, barcode, label, container,
storage position or digital representation can describe or locate the specimen
but is not the specimen itself. The source organism, person, body site,
environment, collection event, analysis, result and repository retain separate
master identities.

FHIR R5 Specimen anchors clinical exchange in identifier, accession, status,
type, subject, collection, processing, container, parent and request links. Its
Trial Use maturity and clinical scope prevent it from becoming a universal
mastership model. ISO 20658, ISO 15189 and WHO laboratory quality guidance
cover pre-examination, patient matching, collection, labeling, acceptance,
transport, storage and disposal. ISO 20387, NCI and ISBER extend quality and
governance to biobanking and research repositories. Licensed or advisory text
must be pinned rather than copied into the open specification.

SPREC 3.0 shows why preanalytical history is first-class: ischemia, delays,
centrifugation, fixation, storage temperature and related factors can change
fitness for a downstream purpose. Quality, integrity, purity, contamination and
sufficiency are therefore method-, time- and purpose-qualified observations,
not timeless properties inferred from a specimen label.

MIABIS, NCBI BioSample and GA4GH Phenopackets cover complementary biobank,
archive and clinical-genomics views. Darwin Core 2026, GGBN and MIxS add
biodiversity, environmental and sequence-context profiles. OBI separates
material entities and processing from investigations, assays and data. No one
projection has universal specimen boundaries, required attributes or lifecycle.

Every collection or material transformation is append-only. A split, aliquot,
pool, extract, culture or fixed derivative receives a new specimen identity and
retains all inputs, outputs, method, actor, clocks and quantity effects. Pools do
not erase contributor identity. Current location does not establish custody;
custody does not establish ownership or permitted use.

WMA Taipei, the Nagoya Protocol and GDPR demonstrate that human, genetic and
biodiversity specimens carry different consent, lawful-basis, permit,
benefit-sharing, withdrawal, access, transfer and retention rules. PROV-O, DQV
and ODRL provide provenance, quality and policy projections. RFC 3339 provides
second-precision clocks with explicit offsets, and RFC 8785 provides
deterministic JSON canonicalization.
