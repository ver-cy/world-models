# Codex pre-provider boundary: WM-LIV-001 Taxon

Status: provisional preparation, not provider evidence or synthesis.

## Boundary

A Taxon is an explicitly circumscribed biological grouping concept asserted in
a named classification, revision or database. It owns concept identity,
according-to authority, circumscription, source-relative placement and status,
name usages, concept relations, mappings, version history and provenance.

It does not own the nomenclatural code, nomenclatural act, publication,
name-bearing specimen, organism, population, occurrence, sequence, trait,
distribution, habitat or conservation-assessment lifecycle. Those remain
referenced evidence or sibling models. A scientific name is not by itself a
taxon-concept identifier. Competing classifications remain visible.

## Candidate structure

1. Identity, authority and scope: concept identity, according-to source,
   circumscription, applicability and code domain.
2. Name usage and nomenclature: scientific usage, authorship, accepted or
   synonym status, typification references, acts and vernacular usage.
3. Classification placement: rank or rankless placement, parentage, path,
   children and incertae sedis.
4. Relations and reconciliation: within-classification relations, split, lump,
   replacement, and evidence-bearing cross-classification RCC-5-style mapping.
5. Diagnosis and evidence: diagnostic description, differential characters,
   specimen, sequence, literature and expert evidence, confidence and dispute.
6. Lifecycle and governance: versions, supersession, change rationale,
   stewardship, review, access, licence, retention and tombstone.
7. Interoperability: TCS, Darwin Core, Catalogue of Life, GBIF, NCBI and
   serializations as projections rather than semantic identity.

## Five facets

- Identity and class: required.
- Direct properties: required for native informational properties; physical
  geometry, mass and material are not applicable because the concept is not a
  physical object.
- Recognition and observation: required for diagnostic criteria, evidence,
  method, confidence and confusing alternatives.
- Capabilities and actions: optional; maintainers can register, place, revise,
  map, review, deprecate and project a concept, subject to authority.
- Context and evidence: required for origin, stewardship, classification,
  sources, time, access, uncertainty and retained history.

## Critical controls

- Prefer authoritative checklist or source concept ID, then governed IRI, then
  adopting-Dimension UUID or ULID.
- Record event timestamps with seconds and an explicit RFC 3339 offset or Z;
  keep publication date, effective time, review time and ingestion time distinct.
- Published cited versions are immutable. Revisions create successors; cited
  concepts are tombstoned rather than erased.
- Validate uniqueness, source and name references, acyclic parentage within a
  classification, code applicability, lineage and mapping semantics.
- Current approved relationship data has no outgoing WM-LIV-001 rows, so all
  sibling composition remains proposed until separately approved.

## Primary source candidates

- https://www.tdwg.org/standards/tcs/
- https://dwc.tdwg.org/terms/#taxon
- https://code.iczn.org/introduction/
- https://www.iapt-taxon.org/nomen/main.php
- https://www.catalogueoflife.org/about/checklistbank
- https://techdocs.gbif.org/en/openapi/v1/species
- https://www.ncbi.nlm.nih.gov/taxonomy
- https://www.rfc-editor.org/rfc/rfc3339
