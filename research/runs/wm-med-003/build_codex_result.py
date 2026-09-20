#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-MED-003."""

import importlib.util
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
BASE_PATH = RUN.parent / "wm-knw-009" / "build_codex_result.py"
SPEC = importlib.util.spec_from_file_location("wm_knw_009_builder", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
AT = "2026-09-07T11:20:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "IFLA Library Reference Model", "International Federation of Library Associations and Institutions", "https://repository.ifla.org/handle/20.500.14598/40", "2017 text with 2024 corrections; repository version 2, 5 February 2025", "standard", "Defines Res, Work, Expression, Manifestation, Item, Agent, Nomen, Place and Time-span, plus aggregates, serials and bibliographic user tasks."),
    src(2, "PRESSoo", "International Federation of Library Associations and Institutions", "https://www.ifla.org/g/cataloguing/pressoo/", "Version 1.3, current official page", "ontology", "Models serial works, publication plans, issues, continuing-resource change and publication events without forcing monograph assumptions."),
    src(3, "RDA Registry", "RDA Steering Committee", "https://www.rdaregistry.info/", "Release 5.4.13, accessed 7 September 2026", "registry", "Publishes machine-readable RDA entities, elements and controlled terminologies for works, expressions, manifestations, items, agents and nomens."),
    src(4, "Overview of the BIBFRAME 2.0 Model", "Library of Congress", "https://www.loc.gov/bibframe/docs/bibframe2-model.html", "BIBFRAME 2.0, 21 April 2016; official documentation current", "ontology", "Separates Work, Instance and Item and locates publisher, place, date, format, identifiers, contributions and holdings at explicit abstraction levels."),
    src(5, "MARC 21 Format for Bibliographic Data", "Library of Congress", "https://www.loc.gov/marc/bibliographic/", "1999 edition through Update 42, May 2026", "standard", "Defines exchange fields for identifiers, titles, edition and imprint statements, physical description, series, notes, links and holdings."),
    src(6, "Metadata Object Description Schema", "Library of Congress", "https://www.loc.gov/standards/mods/", "MODS 3.8, current version", "schema", "Defines a structured bibliographic element set for titles, names, resource types, origin, language, physical description, identifiers, relations, access and record provenance."),
    src(7, "International Standard Bibliographic Description", "International Federation of Library Associations and Institutions", "https://repository.ifla.org/rest/api/core/bitstreams/202c522c-82e9-41ae-ab7c-d7227070142c/content", "ISBD 2011 consolidated edition, 2021 update", "standard", "Defines transcribed and supplied bibliographic description areas including title, responsibility, edition, publication, manufacture, series, resource description, notes and identifiers."),
    src(8, "DCMI Metadata Terms", "Dublin Core Metadata Initiative", "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/", "DCMI Recommendation, 20 January 2020; living latest URL", "standard", "Defines interoperable title, creator, publisher, issued, modified, language, format, relation, provenance, rights and lifecycle terms."),
    src(9, "CreativeWork", "Schema.org Community Group", "https://schema.org/CreativeWork", "Living vocabulary, accessed 7 September 2026", "ontology", "Provides widely deployed web discovery properties for creative works, editions, parts, translations, accessibility, publication events, identifiers and offers."),
    src(10, "DataCite Metadata Schema", "DataCite", "https://schema.datacite.org/meta/kernel-4/", "Version 4.7, released 3 March 2026", "schema", "Defines DOI metadata for research outputs, resource types, creators, publishers, dates, versions, languages, rights, funding and typed related resources."),
    src(11, "Crossref Metadata Schema Versions", "Crossref", "https://www.crossref.org/documentation/schema-library/schema-versions/", "Crossref 5.5.0 current recommended schema, accessed 7 September 2026", "schema", "Defines registered scholarly and professional publication metadata including contributors, titles, versions, publication dates, identifiers, relations, funding, licences, citations and status."),
    src(12, "DOI Handbook", "DOI Foundation", "https://www.doi.org/the-identifier/resources/handbook/", "Version of record, September 2025; page updated December 2025", "standard", "Defines DOI names, referents, registrants, registration agencies, metadata, resolution, persistence, updates and multiple-resolution services."),
    src(13, "ISBN Users' Manual", "International ISBN Agency", "https://www.isbn-international.org/content/isbn-users-manual/29", "Seventh international edition, 2017/2018", "standard", "Explains when distinct editions, languages, formats and product forms receive distinct ISBNs and how publishers and registration agencies administer assignments."),
    src(14, "ISSN Manual and ISSN System Guidance", "ISSN International Centre", "https://www.issn.org/understanding-the-issn/", "ISO 3297 seventh edition, June 2022; current ISSN Manual", "standard", "Defines continuing-resource, medium-edition, key-title and ISSN assignment concepts and the international registration network."),
    src(15, "ONIX for Books Release 3.1 Downloads", "EDItEUR", "https://www.editeur.org/93/Release-3.1-Downloads/", "Release 3.1 revision 2, 28 October 2024", "schema", "Defines book-trade product records, edition and version detail, contributors, measures, subjects, publishing status, rights, markets, prices and collateral."),
    src(16, "Journal Article Tag Suite", "National Information Standards Organization and U.S. National Library of Medicine", "https://jats.nlm.nih.gov/1.4/", "NISO JATS 1.4, ANSI/NISO Z39.96-2024, approved 31 October 2024", "schema", "Defines journal article front matter, contributors, publication and issue metadata, multilingual content, body structure, references, corrections and related articles."),
    src(17, "EPUB 3.3", "World Wide Web Consortium", "https://www.w3.org/TR/epub-33/", "W3C Recommendation, 13 January 2026", "standard", "Defines a distribution and interchange format for digital publications, package metadata, manifest, spine, navigation, resources, rendering and conformance."),
    src(18, "EPUB Accessibility 1.1", "World Wide Web Consortium", "https://www.w3.org/TR/epub-a11y-11/", "W3C Recommendation, 17 October 2024", "standard", "Defines accessibility discoverability metadata, content conformance, certification and distribution responsibilities for EPUB publications."),
    src(19, "PREMIS Data Dictionary for Preservation Metadata", "Library of Congress", "https://www.loc.gov/standards/premis/v3/", "PREMIS 3.0, November 2015; official page current", "standard", "Defines preservation Objects, Events, Rights and Agents, including identifiers, relationships, fixity, event outcomes and preservation rights."),
    src(20, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entities, activities, agents, generation, use, derivation, attribution, revision, specialization and invalidation."),
    src(21, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Defines permissions, prohibitions, duties, constraints, parties, assets and policy inheritance for access and distribution."),
    src(22, "IIIF Presentation API", "IIIF Consortium", "https://iiif.io/api/presentation/3.0/", "Version 3.0.0, 3 June 2020; current stable", "standard", "Defines manifests, collections, canvases, ranges, annotations, structures, navigation, rendering and external services for compound digital objects."),
    src(23, "Date and Time on the Internet", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines interoperable timestamps with seconds and an explicit numeric offset or Z."),
    src(24, "JSON Canonicalization Scheme", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc8785.html", "RFC 8785, June 2020", "standard", "Defines deterministic JSON canonicalization for repeatable hashing and signing of publication metadata projections."),
]


ROWS = [
    ("publication-edition-identity-and-responsibility", "Publication-edition identity and responsibility", "Establish the governed release subject and responsible agents without collapsing bibliographic abstraction levels.", [
        ("edition-root-identity-and-abstraction-boundary", "Edition root identity and abstraction boundary", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-012", "SRC-013"], [
            ("publication-edition-identifier-namespace-revision-owner-and-master", "Publication-edition identifier, namespace, revision, owner and master system", "identity"),
            ("work-expression-edition-manifestation-item-copy-file-and-url-boundary", "Work, expression, edition, manifestation, item, copy, file and URL boundary", "classification")]),
        ("titles-edition-statements-and-agent-responsibility", "Titles, edition statements and agent responsibility", ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-015", "SRC-016"], [
            ("preferred-variant-parallel-key-short-and-series-title-with-edition-statement", "Preferred, variant, parallel, key, short and series title with edition statement", "definition"),
            ("publisher-imprint-creator-editor-translator-contributor-and-responsibility-statement", "Publisher, imprint, creator, editor, translator, contributor and responsibility statement", "relationship")])]),
    ("issuance-seriality-and-constituent-structure", "Issuance, seriality and constituent structure", "Represent release context and ordered parts across monographs, serials and collections without inventing one universal hierarchy.", [
        ("publication-statement-mode-of-issuance-and-clocks", "Publication statement, mode of issuance and clocks", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-011", "SRC-015", "SRC-016", "SRC-023"], [
            ("publication-production-distribution-manufacture-place-agent-and-statement", "Publication, production, distribution, manufacture, place, agent and statement", "authority"),
            ("publication-release-online-availability-copyright-deposit-and-record-clocks", "Publication, release, online availability, copyright, deposit and record clocks", "temporal")]),
        ("series-volume-issue-part-and-ordering", "Series, volume, issue, part and ordering", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-014", "SRC-016", "SRC-022"], [
            ("series-title-identifier-numbering-chronology-frequency-continuity-and-predecessor", "Series title, identifier, numbering, chronology, frequency, continuity and predecessor", "lifecycle"),
            ("volume-issue-part-article-chapter-membership-order-pagination-and-location", "Volume, issue, part, article, chapter, membership, order, pagination and location", "composition")])]),
    ("content-audience-language-and-accessibility", "Content, audience, language and accessibility", "Bind the edition to content and record how intended readers can discover, navigate and use it.", [
        ("work-expression-language-audience-and-subject-bindings", "Work, expression, language, audience and subject bindings", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-013", "SRC-016"], [
            ("work-expression-translation-adaptation-revision-version-and-derivation-binding", "Work, expression, translation, adaptation, revision, version and derivation binding", "relationship"),
            ("language-script-direction-audience-education-subject-genre-summary-and-keyword", "Language, script, direction, audience, education, subject, genre, summary and keyword", "classification")]),
        ("navigation-structure-and-accessibility", "Navigation, structure and accessibility", ["SRC-009", "SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-022"], [
            ("table-of-contents-spine-page-list-landmark-range-navigation-and-reading-order", "Table of contents, spine, page list, landmark, range, navigation and reading order", "composition"),
            ("accessibility-feature-hazard-summary-conformance-certifier-and-remediation", "Accessibility feature, hazard, summary, conformance, certifier and remediation", "validation")])]),
    ("identifiers-rights-markets-and-availability", "Identifiers, rights, markets and availability", "Qualify authority-assigned identifiers and access conditions without turning commerce, possession or resolution into publication identity.", [
        ("identifier-authority-target-and-resolution", "Identifier authority, target and resolution", ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015"], [
            ("isbn-issn-doi-urn-local-identifier-qualifier-status-and-cancellation", "ISBN, ISSN, DOI, URN, local identifier, qualifier, status and cancellation", "identity"),
            ("identifier-target-granularity-agency-registration-metadata-resolution-and-alias", "Identifier target granularity, agency, registration, metadata, resolution and alias", "authority")]),
        ("rights-market-channel-and-access", "Rights, market, channel and access", ["SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-017", "SRC-018", "SRC-021"], [
            ("publisher-imprint-distributor-platform-market-territory-channel-and-audience", "Publisher, imprint, distributor, platform, market, territory, channel and audience", "access"),
            ("copyright-license-permission-prohibition-duty-embargo-availability-and-legal-deposit", "Copyright, license, permission, prohibition, duty, embargo, availability and legal deposit", "requirement")])]),
    ("lifecycle-correction-provenance-and-preservation", "Lifecycle, correction, provenance and preservation", "Preserve attributable change, public status and archival continuity without silently replacing prior editions.", [
        ("revision-correction-retraction-and-supersession", "Revision, correction, retraction and supersession", ["SRC-001", "SRC-002", "SRC-003", "SRC-008", "SRC-010", "SRC-011", "SRC-012", "SRC-016", "SRC-019", "SRC-020", "SRC-023"], [
            ("edition-version-release-revision-erratum-corrigendum-successor-and-change-summary", "Edition, version, release, revision, erratum, corrigendum, successor and change summary", "lifecycle"),
            ("retraction-withdrawal-removal-takedown-silent-replacement-tombstone-and-notice", "Retraction, withdrawal, removal, takedown, silent replacement, tombstone and notice", "event")]),
        ("record-provenance-evidence-deposit-and-preservation", "Record provenance, evidence, deposit and preservation", ["SRC-005", "SRC-006", "SRC-008", "SRC-010", "SRC-011", "SRC-012", "SRC-015", "SRC-016", "SRC-017", "SRC-019", "SRC-020", "SRC-023", "SRC-024"], [
            ("metadata-source-creator-change-agent-authority-method-evidence-and-confidence", "Metadata source, creator, change agent, authority, method, evidence and confidence", "provenance"),
            ("archive-location-deposit-copy-preservation-event-fixity-retention-and-hold-binding", "Archive location, deposit copy, preservation event, fixity, retention and hold binding", "retention")])]),
    ("discovery-citation-governance-and-interoperability", "Discovery, citation, governance and interoperability", "Expose faithful bibliographic projections and quality evidence while declaring profile-specific semantic loss.", [
        ("citation-discovery-and-related-resources", "Citation, discovery and related resources", ["SRC-005", "SRC-006", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-014", "SRC-016", "SRC-022"], [
            ("citation-title-contributor-container-edition-volume-issue-page-date-and-identifier", "Citation title, contributor, container, edition, volume, issue, page, date and identifier", "interoperability"),
            ("is-part-of-has-part-version-translation-review-correction-citation-and-related-item", "Is part of, has part, version, translation, review, correction, citation and related item", "relationship")]),
        ("crosswalk-validation-quality-and-semantic-loss", "Crosswalk, validation, quality and semantic loss", [f"SRC-{i:03d}" for i in range(1, 25)], [
            ("ifla-rda-bibframe-marc-mods-isbd-dc-and-schemaorg-crosswalk", "IFLA, RDA, BIBFRAME, MARC, MODS, ISBD, Dublin Core and Schema.org crosswalk", "interoperability"),
            ("onix-jats-crossref-datacite-epub-iiif-profile-validation-round-trip-and-loss", "ONIX, JATS, Crossref, DataCite, EPUB and IIIF profile, validation, round trip and loss", "quality")])]),
]


KIND_CYCLE = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 7) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 14) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 21) % len(KIND_CYCLE)]]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {lower} as a source-qualified Publication / Edition assertion while works, expressions, files, copies, publishing workflows, parties, rights instruments, channels and identifier agencies retain external mastership.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which publication-edition identity, abstraction level, type, values and references establish {lower}?", "kind": kinds[0], "answer_data": ["edition identifier, namespace, revision, publication type and master system", "work, expression, manifestation, issue, constituent, item, asset and external-master references", "typed values, language, territory, vocabulary or profile, source and explicit unknowns"]},
            {"id": f"{fid}-q02", "text": f"Who creates, authorizes, publishes, registers, distributes, preserves or corrects {lower}, and under which responsibility?", "kind": kinds[1], "answer_data": ["creator, editor, translator, publisher, imprint, registrar, distributor, custodian and reviewer roles", "responsibility statement, contribution role, publication, identifier, rights, preservation and correction authority", "source system, agreement, policy, registration agency, approval and accountable decision references"]},
            {"id": f"{fid}-q03", "text": f"Which dates, events, states, lineage, evidence and competing assertions qualify {lower}?", "kind": kinds[2], "answer_data": ["creation, expression, publication, release, online, availability, copyright, deposit, modification, correction and withdrawal clocks", "predecessor, successor, version, translation, part, carrier and manifestation lineage with immutable revision", "current state, transcribed statement, supplied value, conflict, confidence, notice and review evidence"]},
            {"id": f"{fid}-q04", "text": f"Which identity, structural, accessibility, rights, retention and interoperability checks apply to {lower}?", "kind": kinds[3], "answer_data": ["identifier target, cardinality, title, responsibility, structure, chronology, pagination and schema validation", "copyright, licence, territory, embargo, accessibility, privacy, legal deposit, retention, hold and takedown constraints", "source and target releases, crosswalk, transformation, round-trip result and semantic-loss declaration"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed edition-scoped values and references required to answer the governed questions for {lower}.", "value_kind": "object", "cardinality": "1", "required": True, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": f"{name} evidence manifest", "description": f"Revision-addressed manifest of edition identity, statements, relationships, clocks, authority, rights, lifecycle, evidence and projection outcomes supporting {lower}.", "media_or_form": ["application/json", "application/ld+json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative publication or edition master-system identifier first, authority-qualified ISBN, ISSN, DOI or URN only for its declared target, otherwise governed IRI then Dimension UUID or ULID; bind immutable revision and artifact digest separately.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


ENGINE = BASE.BASE
ENGINE.SOURCES = SOURCES
ENGINE.ROWS = ROWS
ENGINE.KIND_CYCLE = KIND_CYCLE
ENGINE.make_finding = make_finding


FUNCTION_ROWS = [
    ("register-publication-edition", "Register publication edition", "Create one stable edition-level identity without claiming that it is the abstract work, workflow, copy, file or URL.", ["edition proposal", "work or expression reference", "publisher authority"], ["edition identifier", "initial revision"], ["active Dimension", "abstraction boundary explicit"], ["identity, scope and unknowns are appended"], ["SRC-001", "SRC-003", "SRC-004", "SRC-007"]),
    ("bind-work-expression", "Bind work and expression", "Relate the edition to source work, expression, translation, adaptation or revision without importing those lifecycles.", ["edition revision", "work and expression references", "relation type"], ["qualified content binding"], ["targets resolvable", "abstraction levels declared"], ["edition and content identities remain distinct"], ["SRC-001", "SRC-003", "SRC-004", "SRC-008", "SRC-010"]),
    ("assign-validate-identifiers", "Assign or validate identifiers", "Record ISBN, ISSN, DOI, URN and local identifiers with target, agency, status and resolution evidence.", ["edition", "identifier assertion", "authority"], ["qualified identifier binding", "validation outcome"], ["target granularity explicit", "agency resolvable"], ["identifier never replaces edition identity outside its scope"], ["SRC-003", "SRC-004", "SRC-005", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014"]),
    ("record-publication-statement", "Record publication statement", "Capture transcribed and normalized publisher, imprint, place, date, manufacture and distribution statements with source.", ["edition", "source manifestation", "statement"], ["qualified publication statement"], ["source and transcription status known"], ["transcribed text and normalized references coexist"], ["SRC-004", "SRC-005", "SRC-006", "SRC-007"]),
    ("compose-series-issue", "Compose series, volume or issue", "Link serial and collection membership, numbering, chronology, constituents and ordering without collapsing independent identities.", ["edition or issue", "container", "membership assertions"], ["qualified structure graph"], ["member and container identities resolvable"], ["order, enumeration and chronology remain explicit"], ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-011", "SRC-014", "SRC-016", "SRC-022"]),
    ("bind-manifestation-distribution", "Bind manifestation and distribution", "Associate formats, carriers, media assets, channels, markets and availability without owning files, copies or commercial systems.", ["edition", "manifestation or asset", "distribution context"], ["qualified manifestation and availability bindings"], ["targets and authority resolvable"], ["format, channel and edition identities remain distinct"], ["SRC-004", "SRC-005", "SRC-009", "SRC-015", "SRC-017", "SRC-021"]),
    ("assess-accessibility", "Assess accessibility", "Record edition- and manifestation-qualified discoverability, features, hazards, conformance and certification evidence.", ["edition or manifestation", "accessibility metadata", "assessment profile"], ["accessibility assertion", "validation report"], ["profile and target pinned"], ["claims retain assessor, date, evidence and limitations"], ["SRC-009", "SRC-017", "SRC-018"]),
    ("record-authorized-publication", "Record authorized publication", "Append the accountable outcome of a publication workflow without executing or absorbing that external workflow.", ["edition revision", "publication decision", "release context"], ["published-state assertion", "publication event reference"], ["publisher authority and rights granted"], ["release, availability and publication clocks remain distinct"], ["SRC-001", "SRC-004", "SRC-008", "SRC-011", "SRC-015", "SRC-020", "SRC-021", "SRC-023"]),
    ("revise-correct-edition", "Revise or correct edition", "Create a successor revision or edition and explicit correction notice while preserving prior public states.", ["prior edition revision", "change set", "authority"], ["successor revision or edition", "correction notice"], ["change classification and identity rules evaluated"], ["silent replacement is rejected"], ["SRC-001", "SRC-010", "SRC-011", "SRC-016", "SRC-019", "SRC-020"]),
    ("retract-withdraw-tombstone", "Retract, withdraw or tombstone", "Record scoped retraction, withdrawal, removal or takedown without erasing bibliographic identity and evidence.", ["edition revision", "notice", "authority"], ["lifecycle assertion", "public tombstone or restriction"], ["rights, retention and legal hold checked"], ["reason, scope, successor and public notice remain auditable"], ["SRC-008", "SRC-010", "SRC-011", "SRC-019", "SRC-020", "SRC-023"]),
    ("preserve-deposit-publication", "Preserve and deposit publication", "Bind archive locations, deposit copies, media assets, preservation events, retention and fixity evidence.", ["edition", "preservation plan", "deposit requirement"], ["preservation bindings", "deposit evidence"], ["repository and asset identities resolvable"], ["edition identity survives carrier migration"], ["SRC-005", "SRC-006", "SRC-017", "SRC-019", "SRC-020"]),
    ("validate-project-crosswalk", "Validate and project crosswalk", "Produce version-pinned bibliographic projections and explicit round-trip loss reports.", ["edition revision", "target profile", "mapping"], ["target projection", "validation and loss report"], ["source and target releases pinned"], ["canonical edition record remains unchanged"], [f"SRC-{i:03d}" for i in range(1, 25)]),
]
ENGINE.FUNCTION_ROWS = FUNCTION_ROWS


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Declare the Dimension owner, publication-edition master, bibliographic steward, publisher authority, identifier registrar, serials coordinator, rights authority, accessibility reviewer, preservation custodian and auditor.",
                "Register publication type, mode of issuance, title, contribution role, edition, language, seriality, identifier, lifecycle, rights, access, accessibility, retention and projection vocabularies.",
                "Register works, expressions, media assets, copies, parties, organizations, identifier agencies, publication workflows, events, rights instruments, channels, repositories and decisions separately.",
                "Pin bibliographic, book-trade, serial, scholarly, digital-publication, accessibility, preservation and jurisdictional profiles."
            ],
            "namespace_guidance": "Mint only Dimension-owned publication-edition, revision, title assertion, contribution binding, structure, lifecycle and projection identifiers locally; preserve work, expression, manifestation, item, asset, party, identifier-agency, workflow, event, rights, channel and repository identifiers as typed external references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local publication, edition, serial, identifier, rights, accessibility, preservation, access, retention and provenance registries"]
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by registry ID, model version, authoritative publication-edition identifier, immutable revision, abstraction level and master profile; never by title, ISBN, DOI, URL, filename, date or catalogue key alone.",
                "Keep work, expression, edition, manifestation, issue, release, item, copy, file, publication event and publishing workflow distinct."
            ],
            "patch_rules": [
                "Additive extensions declare target node, publication profile, authority, source, vocabulary and standards versions, access scope and interoperability impact.",
                "Breaking identity, abstraction, constituent, identifier-target, title, responsibility, chronology, rights, lifecycle or time changes require an immutable revision or successor edition, migration and crosswalk maps, compatibility declaration and continued resolution of prior identifiers."
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when edition identity, work or expression binding, publication statement, constituent ordering, identifier scope, lifecycle, provenance, rights and access meaning remain intact.",
                "IFLA, RDA, BIBFRAME, MARC, MODS, ISBD, Dublin Core, Schema.org, ONIX, JATS, Crossref, DataCite, EPUB and IIIF mappings pin releases and declare transformed, inferred, omitted or non-round-trippable values."
            ]
        },
        "artifact_rules": {
            "identity_priority": [
                "Authoritative master-system identifier for the publication or edition at the declared abstraction level.",
                "Authority-qualified ISBN, ISSN, DOI, URN or governed IRI only when its target and registration semantics match the edition.",
                "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."
            ],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit numeric offset or Z; keep creation, expression, publication, release, online, availability, copyright, deposit, metadata, modification, correction, retraction, withdrawal and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {edition-id}--{issue-or-aggregate}--{artifact-kind}--{revision-or-event-id}; never use title, ISBN, ISSN, DOI, URL, date, page range or filename alone as identity.",
            "integrity_rule": "Store artifact digest and scope, edition and revision identifiers, identifier target, publication type, source and profile versions, clocks, authority, provenance, lifecycle, rights, accessibility, retention, access marking and semantic-loss declaration."
        },
        "policies": [
            "The adopting Dimension declares who may register editions, assign identifiers, transcribe statements, bind contributors, compose issues, publish, correct, retract, preserve and tombstone records.",
            "Every usable edition requires stable identity, abstraction level, master authority, work or expression binding, title, publication type, lifecycle, provenance and applicable rights and access context.",
            "Agents never infer edition identity, authorship, publisher authority, legal publication, copyright, accessibility, availability or equivalence from a title, identifier, URL, file, copy or catalogue record alone.",
            "Works, expressions, manifestations, assets, copies, parties, agencies, workflows, events, rights instruments, channels, repositories and accountable decisions remain external masters.",
            "Agents may perform reversible metadata extraction, validation and projection under delegation; identifier assignment, public release, rights grants, protected disclosure, retraction and destructive deletion require accountable authority."
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, edition identity, abstraction level, requested revision, work and expression binding, publication and availability state, rights, accessibility, sensitivity, retention and access policy; return the minimum necessary bibliographic projection."],
            "create": ["Create stable publication-edition identity with master authority, abstraction boundary, content bindings, title, publication type, responsible agents, lifecycle, rights context and explicit unknowns before identifier assignment or release."],
            "update": ["Append an immutable statement, relationship, constituent, identifier, publication, rights, accessibility, preservation, lifecycle or correction assertion with actor, authority, source, reason, RFC 3339 effective time and predecessor."],
            "delete": ["Apply copyright, contract, privacy, deposit, preservation, audit, retention and legal-hold policy; tombstone eligible records or remove authorized projections while preserving edition identity, public notices, provenance and non-cascading external masters."]
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Publication-edition steward", "responsibilities": ["Own edition identity, abstraction boundary, lifecycle, revision and correction policy."]},
            {"name": "Bibliographic metadata registrar", "responsibilities": ["Own titles, statements, content bindings, constituent structure, language, audience and discovery metadata."]},
            {"name": "Publisher or imprint authority", "responsibilities": ["Own accountable publication, release, edition designation and public status decisions."]},
            {"name": "Identifier registrar", "responsibilities": ["Own identifier target, agency, assignment, status, alias and resolution evidence."]},
            {"name": "Serials or collection coordinator", "responsibilities": ["Own continuity, enumeration, chronology, frequency, issue and collection membership assertions."]},
            {"name": "Rights and distribution authority", "responsibilities": ["Own rights bindings, embargo, territory, market, channel and access decisions."]},
            {"name": "Accessibility reviewer", "responsibilities": ["Own target-qualified accessibility metadata, conformance, certification and remediation evidence."]},
            {"name": "Preservation custodian", "responsibilities": ["Own deposit, archive, asset bindings, preservation events, retention, holds and recoverability evidence."]},
            {"name": "Auditor", "responsibilities": ["Review identity, identifiers, publication authority, lineage, rights, corrections, withdrawals and destructive actions without rewriting originals."]}
        ],
        "access": {
            "default_rule": "Deny protected metadata, embargoed or licensed content and mutation unless active Dimension, role, purpose, rights instrument, territory, window, sensitivity, retention and field policy grant the action; expose the minimum necessary bibliographic projection.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency preservation, security response or legally compelled access must be grounded, time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable edition identity, public correction, retraction or legal-hold evidence."],
            "audit_requirements": ["Log actor, role, purpose, edition identity, action, decision, policy and standards versions, RFC 3339 timestamp with offset, affected statements or projections, recipient, source evidence and outcome for privileged identifier assignment, publication, disclosure, correction, withdrawal or deletion."]
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": [
                "Read the nearest Dimension-owner AGENTS.md and publication, bibliographic, identifier, rights, accessibility, preservation, access, retention and jurisdiction policies.",
                "Read this model AGENTS.md, pinned spec.yaml and required work, expression, media-asset, publication-workflow, party, rights, identifier, repository, evidence and decision instructions before mutation."
            ]
        }
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Publication / Edition identity, abstraction boundaries, responsibility, issuance, seriality, constituents, identifiers, content bindings, accessibility, rights, availability, lifecycle, corrections, preservation, discovery and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Publication-edition, work, expression, manifestation, issue, release, item, copy, file, URL and catalogue-record identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Publication types, modes of issuance, edition designations, seriality, formats, carriers and lifecycle states are separately typed."},
            {"dimension": "direct properties", "status": "covered", "notes": "Titles, statements, language, audience, numbering, chronology, pagination, identifiers, dates and accessibility properties are source-qualified."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Identifier resolution, metadata extraction, schema validation, availability observation and accessibility assessment retain method and source."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Register, bind, identify, compose, publish, assess, revise, correct, retract, preserve and project functions expose authority and effects."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Planned, registered, published, available, embargoed, corrected, superseded, retracted, withdrawn and tombstoned assertions preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Work, expression, translation, version, predecessor, successor, series, issue, constituent, manifestation, asset, rights and archive links are typed."},
            {"dimension": "temporal", "status": "covered", "notes": "Creation, expression, publication, release, online, availability, copyright, deposit, metadata, correction and withdrawal clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Publication places, production places, markets, territories, jurisdictions, archive regions and described places remain distinct."},
            {"dimension": "provenance", "status": "covered", "notes": "Statements retain source, transcription status, actors, agencies, methods, authority, evidence, revision and correction lineage."},
            {"dimension": "ownership", "status": "covered", "notes": "Authorship, contribution, publisher responsibility, imprint, distribution, copyright, possession and repository custody are not conflated."},
            {"dimension": "validation", "status": "covered", "notes": "Identity, identifier target, title, responsibility, structure, chronology, pagination, schema, accessibility and crosswalk validation are explicit."},
            {"dimension": "security and privacy", "status": "covered", "notes": "Embargoed content, personal contributor data, protected metadata, malicious digital publications and minimum disclosure are represented."},
            {"dimension": "access", "status": "covered", "notes": "Permission, prohibition, duty, role, purpose, territory, market, channel, embargo, availability and audited projection are represented."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Legal deposit, preservation, retention, hold, withdrawal, tombstone, projection removal and asset deletion are distinguished."},
            {"dimension": "interoperability", "status": "covered", "notes": "IFLA, RDA, BIBFRAME, MARC, MODS, ISBD, DC, Schema.org, ONIX, JATS, Crossref, DataCite, EPUB and IIIF projections pin versions and disclose loss."}
        ],
        "known_omissions": [
            "Book, serial, scholarly, news, legal, standards, software, dataset, music, audiovisual and jurisdiction-specific publication profiles require specialist review.",
            "Works, expressions, manifestations, media assets, copies, parties, agencies, workflows, events, rights instruments, commerce, channels, repositories, citations and decisions remain neighboring masters.",
            "Legal publication, legal deposit, copyright, moral rights, retraction duties, accessibility and embargo enforcement require separately pinned jurisdictional profiles.",
            "Automated identifier assignment, public release, rights grants, retraction, protected disclosure, irreversible deletion and identity merge remain outside unreviewed agent authority."
        ],
        "conflicts": [
            "IFLA LRM, RDA, BIBFRAME, ONIX, JATS, Crossref and DataCite do not use identical Work, Expression, Manifestation, Edition, Instance, Product, Version and Item boundaries; every mapping must declare its abstraction choice.",
            "ISBN can distinguish product forms while DOI policies choose registered referents and ISSN identifies continuing-resource medium editions; identifier equality never proves universal edition equality.",
            "Publication, release, issued, available, online, copyright, deposit and metadata-registration dates overlap in implementations but are not interchangeable.",
            "Corrected files, Crossmark-style updates, errata, corrigenda, new editions, retractions and withdrawals have community-specific identity rules; silent replacement is never assumed."
        ],
        "regional_assumptions": [
            "Copyright, moral rights, legal deposit, mandatory publication, accessibility, privacy, consumer information, embargo and takedown duties depend on jurisdiction, sector, audience and purpose.",
            "MARC, MODS and BIBFRAME reflect library communities; ONIX reflects book trade; JATS and Crossref reflect scholarly publishing; DataCite reflects research outputs; no one profile is universal.",
            "A DOI, ISBN, ISSN or accessibility certificate is authority-scoped evidence and does not itself prove authorship, ownership, factual accuracy, legal publication or permission to access."
        ],
        "adversarial_checks": [
            "Reject a publication-edition record without stable identity, abstraction boundary, master authority, revision, work or expression binding and publication type.",
            "Reject title, ISBN, ISSN, DOI, URL, filename, date, citation string or catalogue key as universal edition identity.",
            "Reject work, expression, edition, manifestation, issue, item, copy, media asset and publication workflow collapsed into one record.",
            "Reject serial membership without container and member identity, enumeration, chronology, order, continuity and source.",
            "Reject corrected content that overwrites public history, reuses identity contrary to the active profile or omits change and notice evidence.",
            "Reject accessibility, availability, publisher or rights claims without target, authority, territory, time, source and limitations.",
            "Reject identifier resolution, possession, distribution or public access as proof of ownership, copyright, legal publication or equivalence.",
            "Reject crosswalk output that omits source and target releases, transformation trace, validation result and semantic-loss declaration."
        ]
    }


def build():
    model = {
        "registry_id": "vr.wm-med-003",
        "model_id": "WM-MED-003",
        "name": "Publication / Edition",
        "entry_kind": "aggregate",
        "purpose": "Represent one governed publication-edition identity and its bibliographic, release, constituent, identifier, responsibility, rights, accessibility, lifecycle, preservation and interoperability context.",
        "scope_statement": "Owns publication-edition identity and revision; explicit work and expression bindings; titles and edition statements; publisher, imprint and contribution responsibility; publication statements and separate clocks; mode of issuance; series, volume, issue and constituent structure; language, audience, subject and navigation; identifier assertions and target authority; manifestation, asset and distribution bindings; rights, market, territory, embargo, availability, accessibility and legal-deposit context; correction, retraction, withdrawal, supersession, preservation, provenance, discovery, citation, validation, access, retention and loss-aware projections. Works, expressions, manifestations, assets, copies, parties, identifier agencies, workflows, events, rights instruments, commerce, channels, repositories, citations and accountable decisions remain external.",
        "in_scope": [
            "Publication-edition identity, abstraction boundary, content bindings, titles, statements, responsibility, issuance and constituent structure",
            "Identifiers, language, audience, accessibility, rights, markets, availability, lifecycle, corrections, provenance and preservation bindings",
            "Discovery, citation, access, retention, audit and version-pinned loss-aware interoperability"
        ],
        "out_of_scope": [
            "Owning creative-work, expression, file, copy, party, identifier-agency, publication-workflow, event, rights-instrument, commerce, channel, repository, citation or decision lifecycles",
            "Treating title, ISBN, ISSN, DOI, URL, filename, publication date, citation string or catalogue record as universal edition identity",
            "Inferring authorship, publisher authority, ownership, copyright, legal publication, accessibility, availability or edition equivalence without source-qualified evidence",
            "Assigning identifiers, publishing, granting rights, retracting, disclosing protected content or irreversibly deleting records without accountable authority"
        ],
        "boundary_notes": [
            {"neighbor": "WM-MED-001 Creative Work / Content", "distinction": "The registered parent owns abstract intellectual content and authorship. This model owns a publisher-authorized edition or release identity and never turns the work and its issued form into one identity.", "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-008"]},
            {"neighbor": "WM-MED-002 Media Asset / Rendition", "distinction": "A media asset owns byte-bearing renditions, formats, fixity and technical preservation. This edition selects or binds manifestations and assets but retains bibliographic and release identity.", "source_refs": ["SRC-004", "SRC-017", "SRC-019", "SRC-022"]},
            {"neighbor": "WM-ACT-044 Content Publication", "distinction": "The activity model owns editorial approval, release execution, distribution, correction and takedown workflow. This model records accountable outcomes and public lifecycle without absorbing the case process.", "source_refs": ["SRC-001", "SRC-011", "SRC-020"]},
            {"neighbor": "Manifestation, item, copy, file and access URL", "distinction": "These are embodiments, holdings, byte objects or locators. They may change or multiply while the governed edition identity and its relationship assertions remain stable.", "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-017", "SRC-019"]},
            {"neighbor": "Series, volume, issue, article, chapter and collection", "distinction": "Each independently identifiable publication retains its own record. Container membership, order, enumeration and chronology are typed relationships, not permission to erase nested identities.", "source_refs": ["SRC-001", "SRC-002", "SRC-005", "SRC-010", "SRC-011", "SRC-014", "SRC-016"]},
            {"neighbor": "Identifier, publisher, imprint, distributor, platform and rights instrument", "distinction": "Identifiers and organizations carry authority-scoped roles; resolution, distribution or possession does not establish edition identity, ownership, copyright or permission.", "source_refs": ["SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-021"]}
        ]
    }
    composition = [
        {"target": "WM-MED-001 Creative Work / Content", "relation": "REFERENCE", "purpose": "Resolve the abstract work and expression context while retaining separate edition identity.", "required": True, "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-008"]},
        {"target": "WM-MED-002 Media Asset / Rendition", "relation": "REFERENCE", "purpose": "Resolve digital or physical manifestations and technical assets without importing file and preservation identity.", "required": False, "source_refs": ["SRC-004", "SRC-017", "SRC-019", "SRC-022"]},
        {"target": "WM-ACT-044 Content Publication", "relation": "REFERENCE", "purpose": "Resolve editorial, release, distribution, correction and takedown execution while this model records edition state and outcomes.", "required": False, "source_refs": ["SRC-001", "SRC-011", "SRC-020"]},
        {"target": "Party, organization, identifier agency, rights, agreement, channel, repository, event, evidence and decision masters", "relation": "REFERENCE", "purpose": "Resolve responsible, legal, operational and evidential context without importing those lifecycles.", "required": False, "source_refs": ["SRC-008", "SRC-012", "SRC-013", "SRC-014", "SRC-019", "SRC-020", "SRC-021"]},
        {"target": "IFLA LRM, PRESSoo and RDA Registry", "relation": "ALIGN", "purpose": "Project conceptual bibliographic, serial and cataloguing relationships with explicit abstraction mappings.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003"]},
        {"target": "BIBFRAME 2.0, MARC 21, MODS and ISBD", "relation": "ALIGN", "purpose": "Project library linked-data and exchange descriptions with pinned versions and transcribed-statement handling.", "required": False, "source_refs": ["SRC-004", "SRC-005", "SRC-006", "SRC-007"]},
        {"target": "Dublin Core Terms and Schema.org", "relation": "ALIGN", "purpose": "Project common web discovery metadata without treating the shallow web vocabulary as canonical structure.", "required": False, "source_refs": ["SRC-008", "SRC-009"]},
        {"target": "DataCite, Crossref and DOI", "relation": "ALIGN", "purpose": "Project research-output, scholarly-publication and persistent-identifier metadata with authority-scoped referents.", "required": False, "source_refs": ["SRC-010", "SRC-011", "SRC-012"]},
        {"target": "ISBN, ISSN and ONIX", "relation": "ALIGN", "purpose": "Project book, continuing-resource and book-trade product metadata without universalizing their identifier or product boundaries.", "required": False, "source_refs": ["SRC-013", "SRC-014", "SRC-015"]},
        {"target": "JATS, EPUB and EPUB Accessibility", "relation": "ALIGN", "purpose": "Project journal article, digital-publication package and accessibility metadata with conformance evidence.", "required": False, "source_refs": ["SRC-016", "SRC-017", "SRC-018"]},
        {"target": "PREMIS, PROV-O, ODRL and IIIF Presentation", "relation": "ALIGN", "purpose": "Project preservation, provenance, rights and compound-object presentation without importing external masters.", "required": False, "source_refs": ["SRC-019", "SRC-020", "SRC-021", "SRC-022"]},
        {"target": "RFC 3339 and RFC 8785", "relation": "ALIGN", "purpose": "Project unambiguous clocks and deterministic JSON representations for artifacts and signatures.", "required": False, "source_refs": ["SRC-023", "SRC-024"]}
    ]
    return {
        "schema_version": "1.0.0",
        "model": model,
        "sources": SOURCES,
        "structure": ENGINE.structure(),
        "functions": ENGINE.functions(),
        "composition": composition,
        "service_layers": services(),
        "coverage": coverage(),
    }


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
