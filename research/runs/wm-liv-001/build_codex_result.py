#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-LIV-001."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ACCESSED_AT = "2026-09-06T00:31:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": i, "title": title, "organization": org, "url": url,
        "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": ACCESSED_AT, "relevance": relevance,
    }


SOURCES = [
    src("SRC-001", "Taxon Concept Standard", "Biodiversity Information Standards (TDWG)", "https://tcs.tdwg.org/", "Current vocabulary standard accessed 2026-09-06", "standard", "Defines Taxon Concept, Taxon Name, Taxon Concept Mapping and Nomenclatural Type classes for format-independent exchange."),
    src("SRC-002", "Taxon Concept Standard examples", "Biodiversity Information Standards (TDWG)", "https://tcs.tdwg.org/examples/", "Current examples accessed 2026-09-06", "first-party-doc", "Demonstrates according-to, synonym, vernacular name, parent and child, congruence, inclusion, overlap, disjointness and typification semantics."),
    src("SRC-003", "Darwin Core Quick Reference Guide", "Biodiversity Information Standards (TDWG)", "https://dwc.tdwg.org/terms/", "Current recommended terms accessed 2026-09-06", "standard", "Defines the Taxon class and identifiers, name usage, parentage, rank, status, provenance, access and record-level terms used by biodiversity systems."),
    src("SRC-004", "International Code of Zoological Nomenclature", "International Commission on Zoological Nomenclature", "https://code.iczn.org/introduction/", "Online Code accessed 2026-09-06", "standard", "Establishes zoological nomenclatural scope and distinguishes taxonomic judgment from governed names and name-bearing types."),
    src("SRC-005", "International Code of Nomenclature for algae, fungi, and plants", "International Association for Plant Taxonomy", "https://www.iapt-taxon.org/nomen/main.php", "Madrid Code notice and prior electronic Code accessed 2026-09-06", "standard", "Establishes code-governed botanical, fungal and algal naming and shows that applicable code editions must be versioned."),
    src("SRC-006", "ChecklistBank", "Catalogue of Life", "https://www.catalogueoflife.org/about/checklistbank", "Service documentation accessed 2026-09-06", "registry", "Provides governed checklist, dataset, release, source, identifier and reconciliation context for taxonomic concepts."),
    src("SRC-007", "Species API", "Global Biodiversity Information Facility", "https://techdocs.gbif.org/en/openapi/v1/species", "Current API reference accessed 2026-09-06", "first-party-doc", "Provides operational lookup, matching, hierarchy, name usage and backbone-taxonomy projections with GBIF identifiers."),
    src("SRC-008", "NCBI Taxonomy", "National Center for Biotechnology Information", "https://www.ncbi.nlm.nih.gov/taxonomy", "Current database page accessed 2026-09-06", "registry", "Defines a curated classification and nomenclature for organisms represented in public sequence databases."),
    src("SRC-009", "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entity, activity, agent, attribution, source, derivation, revision and invalidation provenance for concept assertions and mappings."),
    src("SRC-010", "RFC 3339: Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339", "RFC 3339, July 2002", "standard", "Defines interoperable event timestamps with seconds and an explicit UTC offset for revision, review, ingestion and publication events."),
]


# bundle: id, name, description, rationale, refs, layers
# layer: id, name, description, refs, findings
# finding: id, name, description, question kind, refs, value kind, required, artifact
STRUCTURE = [
    ("concept-identity-authority-and-scope", "Concept identity, authority and scope", "Establishes which taxon concept is asserted, by whom, in which classification and with which circumscription.", "A name string cannot uniquely identify a taxon concept because the same name may denote different circumscriptions and competing classifications.", ["SRC-001", "SRC-002", "SRC-003", "SRC-009"], [
        ("concept-identity-and-source", "Concept identity and source", "Stable identity and according-to authority for a concept assertion.", ["SRC-001", "SRC-002", "SRC-003", "SRC-006"], [
            ("taxon-concept-master-identity", "Taxon concept master identity", "Records the authoritative concept identifier, governed namespace, alternate identifiers, source release and collision history independently of names.", "identity", ["SRC-001", "SRC-003", "SRC-006", "SRC-007", "SRC-008"], "object", True, "Concept identity record"),
            ("according-to-source-and-circumscription", "According-to source and circumscription", "Binds the concept to the classification, checklist, revision, publication or database that asserts its included and excluded biological scope.", "definition", ["SRC-001", "SRC-002", "SRC-003", "SRC-006"], "collection", True, "Circumscription assertion"),
        ]),
        ("scope-applicability-and-boundary", "Scope, applicability and boundary", "Domain applicability and separation from neighboring biological records.", ["SRC-001", "SRC-003", "SRC-004", "SRC-005"], [
            ("taxonomic-scope-and-code-applicability", "Taxonomic scope and code applicability", "Records kingdom or organismal domain, extant or fossil scope, hybrid or operational treatment, applicable nomenclatural code and explicit exceptions.", "classification", ["SRC-001", "SRC-004", "SRC-005", "SRC-008"], "collection", True, "Applicability profile"),
            ("concept-name-organism-and-specimen-boundary", "Concept, name, organism and specimen boundary", "States why the concept is distinct from its name usages, organisms, populations, specimens, occurrences and observations, with typed references only.", "relationship", ["SRC-001", "SRC-003", "SRC-004"], "collection", True, "Boundary decision record"),
        ]),
    ]),
    ("name-usage-and-nomenclature", "Name usage and nomenclature", "Represents scientific and vernacular name usages attached to a taxon concept without collapsing names into concepts.", "Taxonomic acceptance is source-relative, while nomenclatural availability, validity or legitimacy follows an applicable code and edition.", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005"], [
        ("scientific-name-usage", "Scientific name usage", "Scientific name forms and source-relative usage status.", ["SRC-001", "SRC-002", "SRC-003"], [
            ("scientific-name-and-canonical-form", "Scientific name and canonical form", "Records the full scientific name, canonical form, rank context, spelling, identifier, language or script and exact source usage.", "definition", ["SRC-001", "SRC-003", "SRC-004", "SRC-005"], "collection", True, "Scientific name usage record"),
            ("accepted-synonym-and-misapplied-usage", "Accepted, synonym and misapplied usage", "Classifies a name usage as accepted, synonym, misapplied, doubtful, unavailable, invalid or another governed source-relative status.", "state", ["SRC-001", "SRC-002", "SRC-003"], "collection", True, "Name usage status assertion"),
        ]),
        ("authorship-publication-and-type", "Authorship, publication and type", "Nomenclatural evidence referenced from authoritative masters.", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005"], [
            ("authorship-and-original-publication", "Authorship and original publication", "Records parsed and verbatim authorship, basionym or original combination references, publication citation and source-specific interpretation.", "provenance", ["SRC-001", "SRC-003", "SRC-004", "SRC-005"], "collection", True, "Authorship and publication reference"),
            ("type-and-nomenclatural-act-reference", "Type and nomenclatural act reference", "References name-bearing type material, typification, proposal, conservation, rejection, ruling or other act without importing specimen or act lifecycle.", "evidence", ["SRC-001", "SRC-002", "SRC-004", "SRC-005"], "collection", False, "Typification and act evidence"),
        ]),
        ("vernacular-usage", "Vernacular usage", "Human-language names with geographic and community context.", ["SRC-001", "SRC-002", "SRC-003"], [
            ("vernacular-name-language-and-script", "Vernacular name, language and script", "Records a vernacular label, normalized and verbatim forms, language, script, grammatical notes and source citation.", "definition", ["SRC-001", "SRC-002", "SRC-003"], "collection", False, "Vernacular name record"),
            ("regional-preference-community-and-source", "Regional preference, community and source", "Qualifies geographic scope, community, preferred or deprecated use, season or context, evidence and responsible steward.", "spatial", ["SRC-001", "SRC-002", "SRC-003"], "collection", False, "Vernacular usage assertion"),
        ]),
    ]),
    ("classification-placement-and-membership", "Classification placement and membership", "Represents rank or rankless placement, parentage, paths and direct members inside a named classification version.", "Placement is an assertion owned by a classification, not an intrinsic universal property of a taxon concept.", ["SRC-001", "SRC-002", "SRC-003", "SRC-006", "SRC-007", "SRC-008"], [
        ("rank-parentage-and-root", "Rank, parentage and root", "Immediate governed placement within one classification.", ["SRC-001", "SRC-002", "SRC-003"], [
            ("rank-or-rankless-placement", "Rank or rankless placement", "Records the exact rank term, vocabulary and source, or an explicit rankless treatment without forcing a Linnaean rank.", "classification", ["SRC-001", "SRC-003", "SRC-006", "SRC-008"], "object", False, "Rank placement assertion"),
            ("parent-concept-and-classification-root", "Parent concept and classification root", "Links the immediate parent and root in the same classification release, with placement authority and effective interval.", "relationship", ["SRC-001", "SRC-002", "SRC-003", "SRC-006"], "collection", True, "Parentage assertion"),
        ]),
        ("path-membership-and-uncertain-placement", "Path, membership and uncertain placement", "Ancestor path, direct children and unresolved position.", ["SRC-001", "SRC-002", "SRC-003", "SRC-006", "SRC-007"], [
            ("classification-path-and-child-membership", "Classification path and child membership", "Records ordered ancestor references, directly included child concepts, membership role, source release and consistency evidence.", "composition", ["SRC-001", "SRC-002", "SRC-006", "SRC-007"], "collection", True, "Classification path projection"),
            ("uncertain-placement-and-incertae-sedis", "Uncertain placement and incertae sedis", "Records unresolved, provisional or competing placements, candidate parents, reason, method, evidence, confidence and review status.", "quality", ["SRC-001", "SRC-003", "SRC-006"], "collection", False, "Uncertain placement assessment"),
        ]),
    ]),
    ("concept-relations-and-reconciliation", "Concept relations and reconciliation", "Preserves taxonomic change and maps concepts across classifications using explicit evidence-bearing semantics.", "Similarity of names or identifiers is insufficient for concept equivalence; mappings need direction, scope, provenance and uncertainty.", ["SRC-001", "SRC-002", "SRC-003", "SRC-006", "SRC-009"], [
        ("within-classification-relations", "Within-classification relations", "Name relationships and concept succession inside an authority context.", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005"], [
            ("synonymy-basionym-and-combination", "Synonymy, basionym and combination", "Records typed name and usage relationships, direction, applicable code, source assertion and exceptions without treating every synonym as concept identity.", "relationship", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005"], "collection", True, "Nomenclatural relationship assertion"),
            ("split-lump-replacement-and-successor", "Split, lump, replacement and successor", "Records taxonomic revision events that create successor concepts, retained portions, split or merged scopes and change rationale.", "lifecycle", ["SRC-001", "SRC-002", "SRC-006", "SRC-009"], "collection", True, "Concept succession map"),
        ]),
        ("cross-classification-mapping", "Cross-classification mapping", "Set-theoretic concept relationships across authorities and releases.", ["SRC-001", "SRC-002", "SRC-006", "SRC-009"], [
            ("congruence-inclusion-and-direction", "Congruence, inclusion and direction", "Records congruent, includes or is-included-in relationships between source-qualified concepts, including direction and compared circumscriptions.", "relationship", ["SRC-001", "SRC-002", "SRC-009"], "collection", True, "Concept inclusion mapping"),
            ("overlap-disjointness-and-mapping-provenance", "Overlap, disjointness and mapping provenance", "Records partial overlap, disjointness or unresolved relation with mapper, method, evidence, confidence, date and supersession.", "evidence", ["SRC-001", "SRC-002", "SRC-006", "SRC-009"], "collection", True, "Concept reconciliation record"),
        ]),
    ]),
    ("diagnosis-evidence-and-uncertainty", "Diagnosis, evidence and uncertainty", "Captures how the concept is recognized and what supports or disputes its circumscription without absorbing evidence-object masters.", "Agents need diagnostic and confidence context to distinguish a taxon concept from neighboring concepts and to avoid presenting unresolved judgment as fact.", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-008", "SRC-009"], [
        ("diagnosis-and-recognition", "Diagnosis and recognition", "Defining description and differential characters.", ["SRC-001", "SRC-003", "SRC-004", "SRC-005"], [
            ("diagnostic-description-and-source", "Diagnostic description and source", "Records the concept diagnosis, character statement, covered life stage or sex, method, source, language and applicability limits.", "definition", ["SRC-001", "SRC-003", "SRC-004", "SRC-005"], "collection", True, "Diagnostic description"),
            ("differential-characters-and-confusing-concepts", "Differential characters and confusing concepts", "Records features that distinguish the concept from named alternatives, observation method, conditions, thresholds, uncertainty and failure modes.", "validation", ["SRC-001", "SRC-003"], "collection", False, "Differential diagnosis matrix"),
        ]),
        ("specimen-sequence-literature-and-expert-evidence", "Specimen, sequence, literature and expert evidence", "External evidence references and their role in concept support.", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-008", "SRC-009"], [
            ("specimen-and-sequence-evidence-reference", "Specimen and sequence evidence reference", "Links type, voucher, collection, material sample or sequence identifiers with evidence role, custody source, quality and access marking.", "evidence", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-008"], "collection", False, "Material and sequence evidence index"),
            ("literature-and-expert-assertion", "Literature and expert assertion", "Links supporting or rejecting publications, datasets and expert judgments with claim, author, method, review status and provenance.", "provenance", ["SRC-001", "SRC-003", "SRC-009"], "collection", True, "Evidence and assertion bundle"),
        ]),
        ("confidence-dispute-and-revision-need", "Confidence, dispute and revision need", "Assessment quality and visible unresolved taxonomic judgment.", ["SRC-001", "SRC-003", "SRC-006", "SRC-009"], [
            ("confidence-method-and-review-status", "Confidence, method and review status", "Records confidence scale, assessment method, reviewer, evidence cut-off, result, limitations and next review trigger.", "measurement", ["SRC-001", "SRC-006", "SRC-009"], "object", True, "Concept confidence assessment"),
            ("dispute-species-complex-and-pending-revision", "Dispute, species complex and pending revision", "Preserves competing circumscriptions, unresolved identification, cryptic complex, disputed placement and planned revision without forcing consensus.", "exception", ["SRC-001", "SRC-003", "SRC-006", "SRC-009"], "collection", False, "Taxonomic dispute record"),
        ]),
    ]),
    ("lifecycle-stewardship-and-governance", "Lifecycle, stewardship and governance", "Controls immutable versions, review authority, access, licence, retention and non-destructive retirement.", "Taxonomic concepts are cited and reused over long periods, so revision must preserve resolvability, provenance and historical meaning.", ["SRC-001", "SRC-003", "SRC-006", "SRC-009", "SRC-010"], [
        ("version-lifecycle-and-change", "Version lifecycle and change", "Release identity, effective time and succession.", ["SRC-001", "SRC-006", "SRC-009", "SRC-010"], [
            ("concept-version-effective-and-record-time", "Concept version, effective and record time", "Records immutable concept version, release, effective interval, publication date, review time, ingestion time and assertion status as distinct values.", "temporal", ["SRC-001", "SRC-006", "SRC-009", "SRC-010"], "collection", True, "Version and time record"),
            ("supersession-deprecation-and-change-rationale", "Supersession, deprecation and change rationale", "Links predecessor and successor concepts, changed boundary, name or placement, reason, authority, migration impact and continued resolution policy.", "lifecycle", ["SRC-001", "SRC-002", "SRC-006", "SRC-009"], "collection", True, "Concept change set"),
        ]),
        ("stewardship-access-and-retention", "Stewardship, access and retention", "Responsibility, review, rights and preservation.", ["SRC-003", "SRC-006", "SRC-009"], [
            ("taxonomic-authority-review-and-provenance", "Taxonomic authority, review and provenance", "Records asserting authority, steward, editor, reviewer, delegated role, method, source chain, decision and accountable timestamps.", "ownership", ["SRC-001", "SRC-006", "SRC-009", "SRC-010"], "collection", True, "Review and provenance record"),
            ("licence-access-retention-and-tombstone", "Licence, access, retention and tombstone", "Records license, attribution, sensitive evidence, withholding or generalization, retention, legal hold, deletion authority and tombstone behavior.", "retention", ["SRC-003", "SRC-006", "SRC-009"], "collection", True, "Access and retention policy record"),
        ]),
    ]),
    ("interoperability-and-projections", "Interoperability and projections", "Maps the semantic model to biodiversity standards, registries, APIs and serializations without coupling identity to a format.", "Each external system has a source-relative classification and may lose semantics, so projections require pinned versions, mappings and round-trip limits.", ["SRC-001", "SRC-002", "SRC-003", "SRC-006", "SRC-007", "SRC-008"], [
        ("standard-and-registry-bindings", "Standard and registry bindings", "Pinned mappings to principal taxonomic exchange systems.", ["SRC-001", "SRC-003", "SRC-006", "SRC-007", "SRC-008"], [
            ("tcs-and-darwin-core-binding", "TCS and Darwin Core binding", "Maps concept, name, according-to, parent, child, accepted usage, synonym and mapping fields to pinned TCS and Darwin Core terms with loss disclosure.", "interoperability", ["SRC-001", "SRC-002", "SRC-003"], "collection", True, "TCS and Darwin Core crosswalk"),
            ("catalogue-of-life-gbif-and-ncbi-binding", "Catalogue of Life, GBIF and NCBI binding", "Maps source dataset, release, taxon identifiers, name usage, hierarchy and reconciliation status to each registry without claiming universal equivalence.", "interoperability", ["SRC-006", "SRC-007", "SRC-008"], "collection", False, "Registry identifier crosswalk"),
        ]),
        ("canonical-and-serialized-projections", "Canonical and serialized projections", "Resolvable citation, integrity and representation variants.", ["SRC-001", "SRC-003", "SRC-006", "SRC-009"], [
            ("canonical-uri-citation-and-digest", "Canonical URI, citation and digest", "Records stable resolution URI, human citation, source snapshot, media type, byte length and digest for a concept version and mapping set.", "provenance", ["SRC-001", "SRC-003", "SRC-006", "SRC-009"], "collection", True, "Canonical concept citation"),
            ("machine-human-and-round-trip-projections", "Machine, human and round-trip projections", "Defines JSON, RDF, CSV, Darwin Core Archive, API and human-card projections with schema, ordering, omitted values and round-trip tests.", "interoperability", ["SRC-001", "SRC-002", "SRC-003", "SRC-006", "SRC-007"], "collection", False, "Projection conformance pack"),
        ]),
    ]),
]


def finding(row):
    fid, name, description, kind, refs, value_kind, required, artifact_name = row
    questions = [
        {"id": f"{fid}-q01", "text": f"What exact values and source-qualified meaning must be recorded for {name.lower()}?", "kind": kind, "answer_data": [name, "Authoritative identifier or controlled value", "Source classification and version", "Explicit unknown or not-applicable reason"]},
        {"id": f"{fid}-q02", "text": f"Which authority, source, method and evidence establish {name.lower()}, with what confidence, effective time and limitations?", "kind": "evidence", "answer_data": ["Authority or steward reference", "Source and method reference", "Evidence and confidence", "Effective and recorded timestamps"]},
        {"id": f"{fid}-q03", "text": f"How must {name.lower()} be related, validated and preserved when classifications disagree or change?", "kind": "validation", "answer_data": ["Typed related concept or external reference", "Validation and conflict result", "Predecessor or successor link", "Provenance and retention decision"]},
    ]
    return {
        "id": fid, "name": name, "description": description,
        "source_refs": refs, "questions": questions,
        "data_elements": [{
            "id": f"{fid}-record", "name": f"{name} record",
            "description": f"Structured source-qualified values for {name.lower()}, including authority, version, provenance, uncertainty and applicable time.",
            "value_kind": value_kind, "cardinality": "1" if required else "0..n",
            "required": required, "source_refs": refs,
        }],
        "artifacts": [{
            "id": f"{fid}-artifact", "name": artifact_name,
            "description": f"Versioned evidence or exchange artifact supporting {name.lower()} without replacing the authoritative master record.",
            "media_or_form": ["JSON", "YAML", "RDF or CSV when mapped", "Human-readable record"],
            "serial": True,
            "identity_strategy": "Use the authoritative taxon-concept ID plus immutable assertion or event ID; never use a scientific name, date, filename or hash alone as semantic identity.",
            "source_refs": refs,
        }],
        "inline_only_rationale": None,
    }


def structure():
    bundles = []
    for bid, bname, bdesc, rationale, brefs, layers in STRUCTURE:
        built_layers = []
        for lid, lname, ldesc, lrefs, findings in layers:
            built_layers.append({"id": lid, "name": lname, "description": ldesc, "source_refs": lrefs, "findings": [finding(x) for x in findings]})
        bundles.append({"id": bid, "name": bname, "description": bdesc, "rationale": rationale, "source_refs": brefs, "layers": built_layers})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-taxon-concept", "Register taxon concept", "Create a stable source-qualified concept identity and initial circumscription.", ["According-to source", "Concept identifier", "Circumscription", "Authority"], ["Immutable concept version", "Validation result"], ["Source and identity authority are resolved"], ["Registers concept without treating a name as its identity"], ["SRC-001", "SRC-003", "SRC-006"]),
    ("bind-name-usage", "Bind name usage", "Attach a scientific or vernacular name usage with source-relative status.", ["Concept version", "Name reference", "Usage status", "Code profile"], ["Name usage assertion"], ["Concept and name identities are resolved"], ["Adds typed usage without merging concept and name lifecycles"], ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005"]),
    ("place-in-classification", "Place in classification", "Assert rank or rankless parentage in one classification release.", ["Concept version", "Classification release", "Parent", "Rank or rankless marker"], ["Placement assertion", "Cycle check"], ["Parent and release are resolved"], ["Creates source-specific placement and path evidence"], ["SRC-001", "SRC-003", "SRC-006"]),
    ("revise-circumscription", "Revise circumscription", "Create a successor concept for a boundary, split, lump or placement change.", ["Predecessor", "New circumscription", "Change reason", "Authority"], ["Successor version", "Change set"], ["Published predecessor is immutable"], ["Preserves lineage and leaves predecessor resolvable"], ["SRC-001", "SRC-002", "SRC-006", "SRC-009"]),
    ("map-taxon-concepts", "Map taxon concepts", "Record congruence, inclusion, overlap, disjointness or unresolved relation across classifications.", ["Source concept", "Target concept", "Mapping relation", "Evidence"], ["Qualified mapping assertion"], ["Both concepts and classification versions are resolved"], ["Adds directional evidence-bearing reconciliation without rewriting either source"], ["SRC-001", "SRC-002", "SRC-009"]),
    ("attach-diagnostic-evidence", "Attach diagnostic evidence", "Reference diagnosis, distinguishing characters, specimens, sequences, literature or expert assertions.", ["Concept version", "Evidence reference", "Evidence role", "Access marking"], ["Evidence binding"], ["External evidence identity and provenance are available"], ["Supports or challenges the concept without importing evidence lifecycle"], ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-008", "SRC-009"]),
    ("review-taxonomic-assertion", "Review taxonomic assertion", "Record an accountable assessment of identity, placement, mapping or evidence.", ["Assertion", "Reviewer", "Method", "Evidence cut-off"], ["Review decision", "Confidence assessment"], ["Reviewer authority and conflicts are declared"], ["Adds review provenance and next-review trigger"], ["SRC-006", "SRC-009", "SRC-010"]),
    ("validate-classification", "Validate classification", "Check identifiers, parentage, source bindings, code applicability, mappings and version lineage.", ["Classification release", "Validation profile"], ["Validation report"], ["Pinned rules and references are available"], ["Reports cycles, broken links, ambiguity and semantic conflicts without silent repair"], ["SRC-001", "SRC-003", "SRC-006"]),
    ("deprecate-taxon-concept", "Deprecate taxon concept", "Retire a concept version while preserving citation and successor navigation.", ["Concept version", "Authority", "Reason", "Successor references"], ["Deprecation event", "Tombstone projection"], ["Retention and dependent citations are checked"], ["Stops new use while preserving historical identity and provenance"], ["SRC-006", "SRC-009", "SRC-010"]),
    ("publish-checklist-projection", "Publish checklist projection", "Render a governed classification or checklist without changing source concepts.", ["Concept versions", "Projection profile", "Release metadata"], ["Checklist artifact", "Digest", "Conformance report"], ["All required concepts and mappings validate"], ["Creates immutable machine and human projections"], ["SRC-001", "SRC-003", "SRC-006", "SRC-007"]),
    ("reconcile-registry-identifiers", "Reconcile registry identifiers", "Link Catalogue of Life, GBIF, NCBI and other source identifiers with explicit match semantics.", ["Concept version", "Registry records", "Matching method"], ["Identifier crosswalk", "Unresolved candidates"], ["Registry versions and evidence are pinned"], ["Adds mappings without claiming name equality as concept equivalence"], ["SRC-006", "SRC-007", "SRC-008"]),
    ("export-taxon-concept", "Export taxon concept", "Produce a selected format or API representation with declared omissions and round-trip limits.", ["Concept version", "Target profile", "Access scope"], ["Serialized projection", "Loss report"], ["Access policy and profile version permit export"], ["Provides portable output while semantic identity remains format-independent"], ["SRC-001", "SRC-003", "SRC-006", "SRC-007"]),
]


def service_layers():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension identity, owner, accountable taxonomic steward and namespace", "Taxon, name, classification, evidence, publication, organization, person, access and provenance registries", "Master-system and federation mappings for external taxonomy services", "Authority, review, access, retention, licensing and publication policies"],
            "namespace_guidance": "Mint taxon concept, concept version, placement, mapping, review and local assertion identifiers in the adopting Dimension namespace only when no authoritative source identifier exists; keep names, organisms, specimens, occurrences, sequences, publications and external registry identities as typed references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local taxon concept, classification, mapping, evidence and provenance registries"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize by authoritative source, source release and taxon-concept identifier, never by scientific name text alone.", "Keep concept, name usage, placement assertion, mapping, evidence object and conservation assessment distinct; preserve competing classifications and source-relative accepted status."],
            "patch_rules": ["Additive extensions declare target bundle, layer or finding, namespace, source, authority, code profile, compatibility and interoperability effect.", "A circumscription, identity or relation-semantics change creates a successor version with migration and rollback mappings rather than mutating a cited release."],
            "compatibility_rules": ["Consumers may ignore unknown additive fields only when concept identity, according-to source, circumscription, classification placement, name-usage status, provenance and lifecycle meaning remain intact.", "TCS, Darwin Core, Catalogue of Life, GBIF, NCBI and code projections pin source and target versions and disclose transformed, omitted or non-round-trippable semantics."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative checklist, taxonomic publication or taxonomy master-system concept identifier plus source release.", "Governed globally resolvable taxon-concept IRI qualified by according-to authority.", "Adopting-Dimension UUID or ULID when no authoritative external concept identifier exists."],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep nomenclatural publication date, concept effective time, review time, ingestion time, mapping time and retirement time distinct.",
            "serial_naming_rule": "Name serial artifacts as {taxon-concept-id}--{artifact-kind}--{assertion-or-event-id}; never use a scientific name, date, filename or hash alone as taxon concept identity.",
            "integrity_rule": "Store digest, media type, byte length, source release, creator, licence, access marking, effective time, provenance and assurance for every retained serial artifact and projection.",
        },
        "policies": ["The adopting Dimension declares who may register, revise, map, review, publish, deprecate, disclose and remove taxon concept records.", "Accepted, synonym and placement status are always qualified by classification, source release and effective time; disagreement remains visible.", "Agents never infer concept equivalence from matching names, ranks or registry labels alone and never fabricate physical properties for a taxon concept.", "Nomenclatural codes, publications, names, specimens, organisms, occurrences, sequences, distributions, habitats and conservation assessments remain in their owning systems and are referenced.", "Automated agents may resolve, validate and project published low-risk concept data within policy, while new circumscription, destructive consolidation, restricted-evidence disclosure and irreversible retirement require accountable authority."],
        "crud": {
            "read": ["Resolve active Dimension, authoritative concept ID, source classification and release, applicable code, version, access scope and requested projection; return the minimum permitted evidence-bearing view."],
            "create": ["Create stable source-qualified concept identity, circumscription, authority, placement, name usage, provenance and explicit unknowns before publication."],
            "update": ["Create an immutable successor with actor, authority, reason, semantic change class, RFC 3339 effective time, predecessor links and before-and-after validation; never overwrite a cited concept version."],
            "delete": ["Apply citation, dependency, retention, licence and legal-hold policy; prefer deprecation and tombstone, preserve identity and lineage, and never cascade into referenced names, specimens, organisms, occurrences, sequences or evidence."],
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, autonomy, access, retention and federation rules."]},
            {"name": "Taxonomic authority or concept author", "responsibilities": ["Own circumscription, placement, revision rationale and scientific judgment."]},
            {"name": "Nomenclatural steward", "responsibilities": ["Interpret applicable code, name usage, authorship, typification and acts."]},
            {"name": "Checklist or registry publisher", "responsibilities": ["Own releases, identifiers, resolution, availability, licence and distribution metadata."]},
            {"name": "Data curator", "responsibilities": ["Maintain mappings, references, quality flags, provenance and issue queues."]},
            {"name": "Reviewer or mapping expert", "responsibilities": ["Assess evidence, competing concepts, mappings, confidence and conformance."]},
            {"name": "Evidence custodian", "responsibilities": ["Own specimen, sequence, publication or dataset records and their access controls."]},
            {"name": "Access and compliance authority", "responsibilities": ["Govern restricted evidence, licensing, disclosure, retention and audit."]},
        ],
        "access": {
            "default_rule": "Deny mutation and restricted-evidence disclosure unless the active Dimension, role, purpose, source licence and field policy grant the action; preserve public concept identifiers and citations when policy permits.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency correction of harmful misidentification must be time-limited, attributable and independently reviewed, and must not erase the prior cited concept, evidence or audit trail."],
            "audit_requirements": ["Log actor, agent, role, purpose, concept and version, source release, action, policy and code profile, RFC 3339 timestamp with offset, affected scope, evidence, validation result and successor or rollback reference."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read the nearest Dimension-owner AGENTS.md, taxonomy-source, authority, access, licensing, retention and federation policies.", "Read this model AGENTS.md, pinned spec.yaml and required name, organism, specimen, occurrence, sequence, publication, classification, evidence and provenance model instructions before mutation."],
        },
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering taxon concept identity, source authority, circumscription, name usage, nomenclature, classification placement, reconciliation, diagnosis, evidence, uncertainty, lifecycle, governance and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Authoritative source, release and concept identifier are distinct from name strings and local aliases."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Circumscription, according-to authority, taxonomic domain, code applicability, rank or rankless status and placement are explicit."},
            {"dimension": "direct properties", "status": "covered", "notes": "Native informational properties include identity, source, circumscription, placement, status and diagnosis; physical geometry, mass and material do not apply to a concept."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Diagnosis, differential characters, confusing concepts, method, conditions, evidence, confidence and failure modes support recognition."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Registration, name binding, placement, revision, mapping, evidence attachment, review, validation, retirement, projection, reconciliation and export are controlled functions."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Immutable versions, effective times, split, lump, succession, deprecation and tombstones preserve cited history."},
            {"dimension": "relationships", "status": "covered", "notes": "Names, parents, children, concepts, classifications, evidence, authorities, mappings and successors use typed source-qualified relations."},
            {"dimension": "temporal", "status": "covered", "notes": "Publication, effective, review, ingestion, mapping and retirement times remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Geography qualifies vernacular usage and source scope; organism distribution remains external."},
            {"dimension": "provenance", "status": "covered", "notes": "Sources, authors, stewards, reviews, evidence, mappings, revisions and projections retain attribution and derivation."},
            {"dimension": "ownership", "status": "covered", "notes": "Dimension owner, taxonomic authority, nomenclatural steward, publisher, curator, reviewer, evidence custodian and access authority are separated."},
            {"dimension": "validation and quality", "status": "covered", "notes": "Uniqueness, source resolution, code applicability, parent cycles, lineage, mapping semantics, confidence and round trips are checked."},
            {"dimension": "access", "status": "covered", "notes": "Licensing, restricted evidence, withholding, generalization, role and purpose govern projections."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Cited versions are retained or tombstoned and deletion never cascades into external biological or evidence masters."},
            {"dimension": "interoperability", "status": "covered", "notes": "TCS, Darwin Core, Catalogue of Life, GBIF and NCBI mappings pin versions and disclose loss."},
        ],
        "known_omissions": ["Code-specific botanical, zoological, prokaryotic and viral nomenclature require separate expert profiles.", "Organism, population, specimen, occurrence, sequence, trait, distribution, habitat and conservation-assessment lifecycles remain in neighboring models.", "Certified registry crosswalks, full TCS conformance fixtures, phylogenetic rankless profiles and mapping benchmarks remain future work."],
        "conflicts": ["TCS now distinguishes Taxon Concept and Taxon Name explicitly, while many Darwin Core and registry records use a broader Taxon or name-usage record; projections must disclose the chosen interpretation.", "Accepted status and parentage vary by source and release, so no single classification is treated as universal truth.", "Nomenclatural codes govern names and types but do not determine taxonomic circumscription or scientific acceptance."],
        "regional_assumptions": ["Applicable nomenclatural code depends on organismal domain and edition, not geography alone.", "Catalogue of Life, GBIF and NCBI are authoritative for their own releases and scopes, not universal arbiters of all taxonomy.", "Vernacular names and preferences are language, community and region specific."],
        "adversarial_checks": ["Reject identity based only on scientific-name text, rank or a local display label.", "Reject a parent, accepted name or synonym assertion that lacks a source classification and release.", "Reject inferred congruence from matching names when circumscriptions or evidence have not been compared.", "Reject mutation of a cited concept version or deletion that breaks historical references.", "Reject physical organism, specimen, occurrence, distribution or conservation facts copied into the taxon concept as intrinsic properties."],
    }


def build():
    return {
        "schema_version": "1.0.0",
        "model": {
            "registry_id": "vr.wm-liv-001", "model_id": "WM-LIV-001", "name": "Taxon", "entry_kind": "entity",
            "purpose": "Represent a governed, source-qualified taxon concept so agents can identify, compare, cite, revise and exchange biological classifications without confusing concepts with names or organisms.",
            "scope_statement": "Owns taxon-concept identity, according-to authority, circumscription, source-relative name usages, placement, concept relations, mappings, diagnosis, evidence references, uncertainty, version history, stewardship and projections while external systems own nomenclatural codes and acts, publications, names, specimens, organisms, occurrences, sequences, habitats, distributions and conservation assessments.",
            "in_scope": ["Taxon concept identity, source, release, circumscription, scope, code applicability, name usages, rank or rankless placement and hierarchy", "Concept succession and cross-classification relations, diagnosis, evidence references, confidence, disputes, stewardship, access, retention and provenance", "TCS, Darwin Core, Catalogue of Life, GBIF, NCBI and machine or human projections with version and loss controls"],
            "out_of_scope": ["Organism, population, specimen, material sample, occurrence, observation, sequence, trait, distribution, habitat or conservation-assessment master lifecycle", "Nomenclatural code, act, publication, scientific-name master, type-specimen custody or registry-service implementation", "Universal acceptance, placement or equivalence inferred from a name string, rank, matching label or one preferred backbone"],
            "boundary_notes": [
                {"neighbor": "Taxon Name and Nomenclatural Act", "distinction": "A taxon concept is a circumscribed grouping according to a source; names, typification and code-governed acts have separate identity and lifecycle and are attached as usages or evidence.", "source_refs": ["SRC-001", "SRC-002", "SRC-004", "SRC-005"]},
                {"neighbor": "Organism, Population, Specimen and Occurrence", "distinction": "Physical or observed biological entities may support or instantiate identification, but their properties, location, custody and event history do not become properties of the concept.", "source_refs": ["SRC-003", "SRC-004"]},
                {"neighbor": "Classification Scheme", "distinction": "A classification owns the ordered system and release; this model owns one source-qualified concept and its placement assertions within that system.", "source_refs": ["SRC-001", "SRC-006"]},
                {"neighbor": "Distribution, Habitat, Trait and Conservation Assessment", "distinction": "These are time- and evidence-dependent assertions about members or populations and remain external references rather than defining taxon-concept identity by default.", "source_refs": ["SRC-003", "SRC-006"]},
                {"neighbor": "Checklist and Taxonomy Registry", "distinction": "Catalogue of Life, GBIF and NCBI own service releases and local identifiers; Vercy preserves mappings and scope instead of declaring their records universally equivalent.", "source_refs": ["SRC-006", "SRC-007", "SRC-008"]},
            ],
        },
        "sources": SOURCES,
        "structure": structure(),
        "functions": [{"id": r[0], "name": r[1], "description": r[2], "inputs": r[3], "outputs": r[4], "preconditions": r[5], "effects": r[6], "source_refs": r[7]} for r in FUNCTIONS],
        "composition": [
            {"target": "Scientific Name, Nomenclatural Act, Publication and Type Specimen models", "relation": "REFERENCE", "purpose": "Bind code-governed name and evidence identities without importing their lifecycle.", "required": True, "source_refs": ["SRC-001", "SRC-002", "SRC-004", "SRC-005"]},
            {"target": "Organism, Population, Specimen, Occurrence, Sequence, Trait, Distribution, Habitat and Conservation models", "relation": "REFERENCE", "purpose": "Connect observations and domain evidence while retaining their direct properties and mastership externally.", "required": False, "source_refs": ["SRC-003", "SRC-006", "SRC-008"]},
            {"target": "Classification, Evidence, Provenance, Person, Organization, Language and Geography models", "relation": "REFERENCE", "purpose": "Resolve source authority, mappings, review, vernacular context and provenance by typed identities.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-009"]},
            {"target": "Taxon Concept Standard", "relation": "ALIGN", "purpose": "Supports format-independent Taxon Concept, Taxon Name, Mapping and Nomenclatural Type semantics.", "required": False, "source_refs": ["SRC-001", "SRC-002"]},
            {"target": "Darwin Core", "relation": "ALIGN", "purpose": "Supports broad biodiversity exchange while requiring explicit concept-versus-name-usage interpretation.", "required": False, "source_refs": ["SRC-003"]},
            {"target": "Catalogue of Life, GBIF and NCBI taxonomy services", "relation": "ALIGN", "purpose": "Supports operational identifier, checklist, hierarchy and reconciliation projections with source-relative scope.", "required": False, "source_refs": ["SRC-006", "SRC-007", "SRC-008"]},
        ],
        "service_layers": service_layers(),
        "coverage": coverage(),
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
