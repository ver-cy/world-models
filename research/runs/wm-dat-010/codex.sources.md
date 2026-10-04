# WM-DAT-010 Codex source record

Accessed 2026-09-06. Only primary official publications were admitted to the
source-grounded fallback. Exact verification status is recorded in
`source-verification.csv`.

- SDMX 3.1 Technical Specifications, released May 2025.
- OGC Observations, Measurements and Samples 3.0, OGC 20-082r4, published
  2023-05-26 and technically aligned with ISO 19156:2023.
- W3C SSN 2023 Edition, Recommendation 2024-12-05. Its
  `ObservationCollection` caveat is retained rather than normalized away.
- W3C RDF Data Cube, Recommendation 2014-01-16.
- W3C/OGC OWL-Time, Candidate Recommendation Draft 2022-11-15.
- W3C PROV-O, Recommendation 2013-04-30.
- W3C Data Quality Vocabulary, Working Group Note 2016-12-15.
- W3C DCAT 3, Recommendation 2024-08-22.
- W3C Model for Tabular Data and Metadata on the Web, Recommendation
  2015-12-17.
- UNECE GSIM 2.0, released December 2023; User Guide published November 2024.
- IETF RFC 3339, July 2002, as updated by RFC 9557.
- ISO 8601-1:2019, confirmed 2024, plus Amendment 1:2022. Only public ISO
  metadata was used; restricted clauses were not inspected or inferred.
- DataCite Metadata Schema 4.7, released 2026-03-03.
- CF Metadata Conventions 1.13, released December 2025.
- HL7 FHIR R5 Observation 5.0.0, generated 2023-03-26.

The sources support distinct series, collection and observation identities;
dimension, measure and unit semantics; observation values and states; multiple
time axes and vintages; sampling and coverage; derivation and forecasts;
provenance and quality; release, access, retention and loss-aware projections.
They do not delegate authority for ingestion, imputation, recalculation,
revision, suppression, publication, certification, unit changes, access widening
or physical records disposition.
