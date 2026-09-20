#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-MED-002."""

import importlib.util
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
BASE_PATH = RUN.parent / "wm-knw-009" / "build_codex_result.py"
SPEC = importlib.util.spec_from_file_location("wm_knw_009_builder", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
AT = "2026-09-07T10:30:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "Ontology for Media Resources 1.0", "World Wide Web Consortium", "https://www.w3.org/TR/mediaont-10/", "W3C Recommendation, 9 February 2012", "ontology", "Defines a core media-resource vocabulary and mappings across metadata formats, including locator, fragment, format, compression, duration, dimensions, tracks, language and rights."),
    src(2, "DCMI Metadata Terms", "Dublin Core Metadata Initiative", "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/", "DCMI Recommendation, 20 January 2020; living latest URL", "standard", "Defines interoperable resource description, format, extent, relation, provenance, rights, language and lifecycle terms."),
    src(3, "Media Types Registry", "Internet Assigned Numbers Authority", "https://www.iana.org/assignments/media-types/media-types.xhtml", "Living registry, accessed 7 September 2026", "registry", "Provides authoritative registered media types and structured syntax suffixes for technical representations."),
    src(4, "Digest Fields", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc9530.html", "RFC 9530, February 2024", "standard", "Distinguishes digest of HTTP message content from digest of the selected representation and defines registered digest algorithms."),
    src(5, "HTTP Semantics", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc9110.html", "RFC 9110, June 2022", "standard", "Defines resources, representations, content negotiation, validators, ranges, metadata and HTTP method semantics."),
    src(6, "The BagIt File Packaging Format", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc8493.html", "RFC 8493, October 2018", "standard", "Defines manifests, payload fixity and portable packaging for storage and transfer of arbitrary digital content."),
    src(7, "PREMIS Data Dictionary for Preservation Metadata", "Library of Congress", "https://www.loc.gov/standards/premis/v3/", "PREMIS 3.0, November 2015; official page updated 2023", "standard", "Defines preservation Objects, Events, Rights and Agents, including files, bitstreams, fixity, relationships and event outcomes."),
    src(8, "Metadata Encoding and Transmission Standard", "Library of Congress", "https://www.loc.gov/standards/mets/", "METS 2 schema and official maintenance site, accessed 7 September 2026", "schema", "Defines structural maps, files, descriptive and administrative metadata sections and links between compound digital-object parts."),
    src(9, "Metadata for Images in XML", "Library of Congress and NISO", "https://www.loc.gov/standards/mix/", "MIX 2.0 current schema", "schema", "Defines technical metadata for digital still images, including basic parameters, creation, performance assessment and change history."),
    src(10, "AudioMD and VideoMD", "Library of Congress", "https://www.loc.gov/standards/amdvmd/", "AudioMD and VideoMD 2.0 current schemas", "schema", "Defines technical metadata for audio- and video-based digital objects and use within METS or PREMIS extensions."),
    src(11, "PBCore XML Schema", "PBCore Metadata Standard", "https://pbcore.org/xsd", "PBCore 2.1 current release", "schema", "Defines audiovisual descriptions and separately identifiable instantiations with identifiers, dates, dimensions, digital formats, tracks, locations and rights."),
    src(12, "EBUCore Metadata Set", "European Broadcasting Union", "https://tech.ebu.ch/publications/tech3293", "EBU Tech 3293 version 1.10, 16 April 2020", "standard", "Defines an adaptable media information and asset-management model with descriptive, technical, dynamic, part and rights metadata."),
    src(13, "IPTC Photo Metadata Standard", "International Press Telecommunications Council", "https://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-2025.1.html", "IPTC Photo Metadata 2025.1 revision 1", "standard", "Defines IPTC Core and Extension photo metadata, administrative, descriptive, rights, accessibility and AI-related properties."),
    src(14, "IPTC Video Metadata Hub", "International Press Telecommunications Council", "https://iptc.org/standards/video-metadata-hub/recommendation/", "Recommendation 1.7, October 2025", "standard", "Defines format-independent video descriptive, rights, administrative and technical properties with XMP, EBUCore and JSON expressions."),
    src(15, "IIIF Image API", "IIIF Consortium", "https://iiif.io/api/image/3.0/", "Version 3.0.0, 3 June 2020; current stable", "standard", "Defines identifiers, information responses and image renditions selected by region, size, rotation, quality, format and compliance profile."),
    src(16, "IIIF Presentation API", "IIIF Consortium", "https://iiif.io/api/presentation/3.0/", "Version 3.0.0, 3 June 2020; current stable", "standard", "Defines manifests, canvases, content resources, annotations, choices, ranges, thumbnails, rendering and service links for compound media."),
    src(17, "Web Annotation Data Model", "World Wide Web Consortium", "https://www.w3.org/TR/annotation-model/", "W3C Recommendation, 23 February 2017", "standard", "Defines body-target annotations, selectors, states, motivations, provenance and lifecycle for media descriptions and segments."),
    src(18, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entities, activities, agents, generation, use, derivation, attribution, revision and invalidation."),
    src(19, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Defines permissions, prohibitions, duties, constraints, parties, assets and policy inheritance for governed use."),
    src(20, "C2PA Content Credentials Technical Specification", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html", "C2PA 2.4, April 2026", "standard", "Defines assets, derived assets, manifests, assertions, hard and soft bindings, signatures, validation and trust signals."),
    src(21, "WebVTT: The Web Video Text Tracks Format", "World Wide Web Consortium", "https://www.w3.org/TR/webvtt1/", "Living W3C specification, accessed 7 September 2026", "standard", "Defines timed text tracks, cues and rendering semantics for captions, subtitles, descriptions, chapters and metadata."),
    src(22, "Web Content Accessibility Guidelines 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/WCAG22/", "W3C Recommendation, 5 October 2023", "standard", "Defines accessibility requirements including alternatives, captions, audio description, presentation and operability."),
    src(23, "Date and Time on the Internet", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines interoperable timestamps with seconds and an explicit numeric offset or Z."),
    src(24, "JSON Canonicalization Scheme", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc8785.html", "RFC 8785, June 2020", "standard", "Defines deterministic JSON canonicalization for repeatable hashing and signing of JSON projections."),
]


ROWS = [
    ("asset-identity-boundary-and-rendition-graph", "Asset identity, boundary and rendition graph", "Separate the governed aggregate, each technical representation and every neighboring intellectual or delivery identity.", [
        ("asset-aggregate-identity-and-mastership", "Asset aggregate identity and mastership", ["SRC-001", "SRC-002", "SRC-007", "SRC-011", "SRC-012", "SRC-018", "SRC-023"], [
            ("asset-record-identifier-namespace-version-owner-and-master-system", "Asset record identifier, namespace, version, owner and master system", "identity"),
            ("creative-work-edition-asset-rendition-file-bitstream-and-locator-boundary", "Creative work, edition, asset, rendition, file, bitstream and locator boundary", "classification")]),
        ("rendition-identity-role-and-relationship", "Rendition identity, role and relationship", ["SRC-001", "SRC-005", "SRC-007", "SRC-008", "SRC-011", "SRC-015", "SRC-016", "SRC-020"], [
            ("rendition-identifier-role-master-mezzanine-access-proxy-thumbnail-and-alternate", "Rendition identifier, role, master, mezzanine, access, proxy, thumbnail and alternate", "relationship"),
            ("original-source-capture-best-copy-equivalence-supersession-and-choice-claims", "Original, source capture, best copy, equivalence, supersession and choice claims", "evidence")])]),
    ("technical-representation-and-component-description", "Technical representation and component description", "Make bytes, formats, encodings, measurable characteristics and internal components machine-checkable.", [
        ("bytes-format-fixity-and-conformance", "Bytes, format, fixity and conformance", ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-024"], [
            ("byte-length-digest-algorithm-content-representation-and-package-fixity", "Byte length, digest algorithm, content, representation and package fixity", "validation"),
            ("media-type-container-codec-profile-version-format-signature-and-conformance", "Media type, container, codec, profile, version, format signature and conformance", "classification")]),
        ("technical-characteristics-tracks-parts-and-fragments", "Technical characteristics, tracks, parts and fragments", ["SRC-001", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-014", "SRC-015", "SRC-016", "SRC-021"], [
            ("dimensions-duration-rate-resolution-colour-audio-video-and-image-characteristics", "Dimensions, duration, rate, resolution, colour, audio, video and image characteristics", "measurement"),
            ("track-channel-page-frame-segment-tile-fragment-dependency-and-compound-part", "Track, channel, page, frame, segment, tile, fragment, dependency and compound part", "composition")])]),
    ("metadata-semantics-accessibility-and-localization", "Metadata, semantics, accessibility and localization", "Preserve descriptive meaning, metadata precedence and accessible or localized alternatives without rewriting technical identity.", [
        ("embedded-sidecar-descriptive-and-semantic-metadata", "Embedded, sidecar, descriptive and semantic metadata", ["SRC-001", "SRC-002", "SRC-008", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-016", "SRC-017"], [
            ("embedded-block-sidecar-namespace-schema-source-precedence-and-conflict", "Embedded block, sidecar, namespace, schema, source, precedence and conflict", "provenance"),
            ("title-description-subject-genre-person-place-event-segment-and-annotation", "Title, description, subject, genre, person, place, event, segment and annotation", "definition")]),
        ("language-accessibility-and-alternate-representations", "Language, accessibility and alternate representations", ["SRC-001", "SRC-002", "SRC-013", "SRC-014", "SRC-016", "SRC-017", "SRC-021", "SRC-022"], [
            ("language-script-locale-caption-subtitle-transcript-translation-and-signing", "Language, script, locale, caption, subtitle, transcript, translation and signing", "interoperability"),
            ("alternative-text-audio-description-easy-read-accessibility-role-and-conformance", "Alternative text, audio description, easy read, accessibility role and conformance", "requirement")])]),
    ("provenance-derivation-rights-and-authenticity", "Provenance, derivation, rights and authenticity", "Keep transformations attributable and distinguish legal authority from cryptographic or descriptive trust evidence.", [
        ("creation-capture-derivation-and-processing-lineage", "Creation, capture, derivation and processing lineage", ["SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-018", "SRC-020", "SRC-023"], [
            ("creation-capture-import-transcode-edit-render-export-parent-ingredient-and-action", "Creation, capture, import, transcode, edit, render, export, parent, ingredient and action", "process"),
            ("actor-tool-device-software-version-setting-prompt-method-time-and-source", "Actor, tool, device, software version, setting, prompt, method, time and source", "provenance")]),
        ("rights-policy-credential-and-trust", "Rights, policy, credential and trust", ["SRC-002", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-016", "SRC-018", "SRC-019", "SRC-020"], [
            ("copyright-ownership-license-permission-prohibition-duty-territory-window-and-party", "Copyright, ownership, license, permission, prohibition, duty, territory, window and party", "access"),
            ("content-credential-hard-binding-soft-binding-signature-validation-trust-and-privacy", "Content credential, hard binding, soft binding, signature, validation, trust and privacy", "security")])]),
    ("storage-preservation-quality-and-fitness", "Storage, preservation, quality and fitness", "Maintain retrievability and evidential continuity while keeping measurements and purpose-qualified assessments distinct.", [
        ("storage-copy-custody-preservation-and-retention", "Storage, copy, custody, preservation and retention", ["SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-018", "SRC-023"], [
            ("storage-copy-location-provider-tier-custodian-availability-replication-and-encryption", "Storage copy, location, provider, tier, custodian, availability, replication and encryption", "state"),
            ("preservation-event-format-risk-migration-normalization-refresh-retention-and-hold", "Preservation event, format risk, migration, normalization, refresh, retention and hold", "retention")]),
        ("technical-quality-perceptual-quality-and-fitness", "Technical quality, perceptual quality and fitness", ["SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-021", "SRC-022"], [
            ("validation-decode-error-corruption-completeness-black-silence-clipping-and-qc", "Validation, decode error, corruption, completeness, black, silence, clipping and quality control", "quality"),
            ("perceptual-quality-intended-use-threshold-method-uncertainty-review-and-acceptance", "Perceptual quality, intended use, threshold, method, uncertainty, review and acceptance", "decision")])]),
    ("delivery-lifecycle-governance-and-interoperability", "Delivery, lifecycle, governance and interoperability", "Expose controlled representations, immutable change history and explicit semantic loss across interfaces.", [
        ("delivery-selection-publication-and-distribution", "Delivery, selection, publication and distribution", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-011", "SRC-012", "SRC-014", "SRC-015", "SRC-016", "SRC-019", "SRC-021"], [
            ("endpoint-service-protocol-cdn-locator-availability-window-embargo-and-region", "Endpoint, service, protocol, CDN, locator, availability window, embargo and region", "access"),
            ("representation-selection-negotiation-transform-parameter-cache-validator-and-range", "Representation selection, negotiation, transform parameter, cache validator and range", "process")]),
        ("lifecycle-audit-crosswalk-and-semantic-loss", "Lifecycle, audit, crosswalk and semantic loss", [f"SRC-{i:03d}" for i in range(1, 25)], [
            ("draft-active-published-restricted-withdrawn-superseded-deleted-and-tombstoned-state", "Draft, active, published, restricted, withdrawn, superseded, deleted and tombstoned state", "lifecycle"),
            ("profile-version-crosswalk-conformance-round-trip-loss-correction-and-audit", "Profile, version, crosswalk, conformance, round trip, loss, correction and audit", "interoperability")])]),
]


KIND_CYCLE = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 7) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 14) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 21) % len(KIND_CYCLE)]]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {lower} as a source-qualified Media Asset / Rendition assertion while creative works, editions, specialist media objects, rights instruments, credentials and storage systems retain external mastership.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which asset and rendition identities, boundaries, roles, values and references establish {lower}?", "kind": kinds[0], "answer_data": ["asset identifier, rendition identifier, namespace, revision, role and master system", "work, edition, parent, ingredient, component, file, bitstream, service and locator references", "typed values, units, vocabulary or format profile, source and explicit unknowns"]},
            {"id": f"{fid}-q02", "text": f"Who creates, owns, controls, validates, preserves, publishes or corrects {lower}, and under which authority?", "kind": kinds[1], "answer_data": ["creator, producer, asset steward, technical operator, rights authority, custodian and reviewer roles", "creation, transformation, rights, preservation, publication, access and correction authority", "source system, policy, license, credential, approval and accountable decision references"]},
            {"id": f"{fid}-q03", "text": f"Which events, clocks, states, lineage, evidence and competing assertions qualify {lower}?", "kind": kinds[2], "answer_data": ["capture, ingest, transform, validate, publish, preserve, restrict, withdraw, correct and delete clocks", "parent and ingredient lineage, actor, tool, method, settings, event outcome and immutable predecessor", "current state, conflicting metadata, confidence, credential validation and review evidence"]},
            {"id": f"{fid}-q04", "text": f"Which validation, security, accessibility, retention and interoperability limits apply to {lower}?", "kind": kinds[3], "answer_data": ["identity, digest, decode, format, profile, structural, accessibility and quality checks", "classification, privacy, rights, encryption, access, embargo, retention, legal hold and deletion constraints", "source and target versions, crosswalk, transformation, round-trip result and semantic-loss declaration"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed asset- and rendition-scoped values and references required to answer the governed questions for {lower}.", "value_kind": "object", "cardinality": "1", "required": True, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": f"{name} evidence manifest", "description": f"Digest-addressed manifest of asset and rendition identity, technical values, events, lineage, rights, quality, access and corrections supporting {lower}.", "media_or_form": ["application/json", "application/ld+json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative asset or rendition master-system identifier first, otherwise governed IRI, then Dimension UUID or ULID; bind the immutable revision and byte or projection digest separately.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


ENGINE = BASE.BASE
ENGINE.SOURCES = SOURCES
ENGINE.ROWS = ROWS
ENGINE.KIND_CYCLE = KIND_CYCLE
ENGINE.make_finding = make_finding


FUNCTION_ROWS = [
    ("register-media-asset", "Register media asset", "Create one stable management-aggregate identity without claiming that the record is the work, edition or bytes.", ["asset proposal", "creative-work reference", "master authority"], ["asset identifier", "initial revision"], ["active Dimension", "aggregate boundary explicit"], ["identity, scope and unknowns are appended"], ["SRC-001", "SRC-002", "SRC-007", "SRC-011", "SRC-012"]),
    ("register-rendition", "Register rendition", "Create a separately addressable technical representation and type its role within the asset graph.", ["asset revision", "rendition proposal", "role"], ["rendition identifier", "qualified relationship"], ["asset identity resolvable", "rendition bytes or service explicit"], ["siblings and source representations remain distinct"], ["SRC-001", "SRC-007", "SRC-011", "SRC-015", "SRC-016"]),
    ("identify-format", "Identify format and encoding", "Record media type, container, codec, profile, version and conformance evidence without conflation.", ["rendition", "identification observations"], ["format assertion", "conformance state"], ["byte or service target resolvable"], ["source, method and uncertainty are preserved"], ["SRC-003", "SRC-007", "SRC-009", "SRC-010", "SRC-011"]),
    ("calculate-verify-fixity", "Calculate and verify fixity", "Calculate source-qualified digests and compare expected content, representation or package fixity.", ["rendition bytes or package", "algorithm", "expected digest"], ["fixity assertion", "validation outcome"], ["algorithm allowed", "digest scope explicit"], ["identity is not replaced by checksum equality"], ["SRC-004", "SRC-006", "SRC-007"]),
    ("extract-reconcile-metadata", "Extract and reconcile metadata", "Read embedded and sidecar metadata and preserve sources, precedence, conflicts and corrections.", ["rendition", "metadata blocks", "mapping profile"], ["qualified metadata assertions", "conflict report"], ["schemas and namespaces pinned"], ["last-write-wins is rejected"], ["SRC-001", "SRC-008", "SRC-011", "SRC-012", "SRC-013", "SRC-014"]),
    ("record-derivation", "Record derivation", "Append capture, import, transcode, edit, render or export lineage with all inputs and settings.", ["input renditions", "activity", "output rendition"], ["derivation assertion", "activity evidence"], ["all inputs resolvable", "actor or tool attributable"], ["output receives new rendition identity"], ["SRC-007", "SRC-009", "SRC-010", "SRC-018", "SRC-020"]),
    ("bind-rights-policy", "Bind rights and policy", "Bind external rights, licenses and policies to asset or rendition scope without inferring authority from possession.", ["asset or rendition", "rights instrument", "scope"], ["qualified policy binding"], ["issuer and jurisdiction resolvable"], ["permissions, prohibitions, duties and windows remain explicit"], ["SRC-002", "SRC-011", "SRC-013", "SRC-014", "SRC-019"]),
    ("verify-authenticity-evidence", "Verify authenticity evidence", "Validate a bound content credential and record trust evidence without declaring semantic truth.", ["rendition", "credential", "trust policy"], ["validation report", "qualified trust state"], ["binding and trust inputs available"], ["cryptographic validity remains distinct from factual accuracy and rights"], ["SRC-018", "SRC-020"]),
    ("assess-quality-accessibility", "Assess quality and accessibility", "Record method-, profile- and purpose-qualified technical, perceptual and accessibility assessments.", ["rendition", "measurements", "intended use"], ["quality assertions", "accessibility assertion"], ["method and threshold pinned"], ["assessment does not rewrite technical facts"], ["SRC-009", "SRC-010", "SRC-013", "SRC-014", "SRC-021", "SRC-022"]),
    ("preserve-migrate", "Preserve or migrate rendition", "Create preservation copies or successor renditions while retaining fixity, events, relationships and semantic-loss evidence.", ["rendition", "preservation plan", "target profile"], ["successor rendition", "preservation event"], ["retention and hold checked"], ["source remains resolvable and outcome is verified"], ["SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-018"]),
    ("publish-authorized-representation", "Publish authorized representation", "Expose a purpose-qualified representation, service or transform under access and delivery policy.", ["asset revision", "recipient purpose", "delivery profile"], ["authorized endpoint or projection", "selection trace"], ["rights and access granted", "target profile pinned"], ["delivery is auditable and canonical identity is preserved"], ["SRC-005", "SRC-011", "SRC-015", "SRC-016", "SRC-019", "SRC-021"]),
    ("supersede-withdraw-delete", "Supersede, withdraw or delete", "Append lifecycle change and execute eligible storage actions without erasing identity, provenance or legal-hold evidence.", ["asset or rendition revision", "requested action", "authority"], ["successor or tombstone", "action evidence"], ["retention, rights and hold evaluated"], ["external masters and sibling renditions are not cascaded"], ["SRC-002", "SRC-007", "SRC-018", "SRC-019", "SRC-023"]),
]
ENGINE.FUNCTION_ROWS = FUNCTION_ROWS


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Declare the Dimension owner, media-asset master, rendition registrar, metadata steward, preservation custodian, rights authority, accessibility reviewer and auditor.",
                "Register asset-role, rendition-role, format, codec, profile, technical-property, language, accessibility, quality, lifecycle, rights, retention and projection vocabularies.",
                "Register creative work, publication, recording, image, scene, broadcast, party, storage, rights, policy, credential, event and decision masters separately.",
                "Pin media-sector, preservation, accessibility, authenticity, jurisdictional, licensing and delivery profiles."
            ],
            "namespace_guidance": "Mint only Dimension-owned asset, rendition, relationship, technical assertion, metadata assertion, lifecycle and projection identifiers locally; preserve creative-work, edition, rights, party, storage, service, credential and event identifiers as typed external references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local media asset, rendition, format, rights, preservation, access, retention and provenance registries"]
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by registry ID, model version, authoritative asset and rendition identifiers, immutable revision, representation role and master profile; never by filename, URL, storage key, timestamp or checksum alone.",
                "Keep creative work, expression or edition, asset record, rendition, file, bitstream, fragment, service, locator, storage copy and credential distinct."
            ],
            "patch_rules": [
                "Additive extensions declare target node, media profile, authority, source, method, units, standards versions, access scope and interoperability impact.",
                "Breaking identity, role, lineage, digest-scope, rights, lifecycle or time changes require a new immutable revision, migration and crosswalk maps, compatibility declaration and continued resolution of prior identifiers."
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when asset and rendition identity, boundary, role, bytes or service, lineage, rights, state, provenance and access meaning remain intact.",
                "W3C, DCMI, IANA, PREMIS, METS, MIX, AudioMD, VideoMD, PBCore, EBUCore, IPTC, IIIF and C2PA mappings pin releases and declare transformed, inferred, omitted or non-round-trippable values."
            ]
        },
        "artifact_rules": {
            "identity_priority": [
                "Authoritative master-system identifier for the media asset or separately addressable rendition.",
                "Governed globally resolvable IRI or persistent identifier bound to the correct abstraction level.",
                "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."
            ],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit numeric offset or Z; keep creation, capture, ingest, metadata, transformation, validation, preservation, publication, restriction, withdrawal, correction, deletion and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {asset-id}--{rendition-id-or-aggregate}--{artifact-kind}--{revision-or-event-id}; never use title, filename, URL, date, checksum or storage key alone as identity.",
            "integrity_rule": "Store digest and digest scope, algorithm, media type, byte length, issuer, asset and rendition identifiers, role, source and profile versions, clocks, provenance, validation, rights, accessibility, retention, access marking and semantic-loss declaration."
        },
        "policies": [
            "The adopting Dimension declares who may register assets and renditions, classify roles, extract metadata, transform, validate, preserve, publish, restrict, correct, withdraw and tombstone records.",
            "Every usable rendition requires stable identity, asset relationship, role, media type or explicit unknown, byte or service boundary, technical profile, lineage, lifecycle and applicable rights and access context.",
            "Agents never infer creative-work identity, originality, ownership, copyright, authenticity, factual truth, accessibility or fitness from a filename, URL, checksum, metadata block, storage copy or credential alone.",
            "Creative works, editions, medium-specific works, parties, agreements, rights instruments, policies, credentials, storage systems, services and accountable decisions remain external masters.",
            "Agents may perform reversible extraction, fixity, validation, low-risk transformation and projection under delegation; publication, rights grants, protected disclosure, destructive deletion and identity merge require accountable authority."
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, asset and rendition identity, requested revision, representation role, delivery and preservation state, rights, accessibility, sensitivity, retention and access policy; return the minimum necessary representation and metadata projection."],
            "create": ["Create stable asset identity and separately identified renditions with master authority, boundary, role, technical profile, lineage, state, rights context and explicit unknowns before publication or transformation."],
            "update": ["Append an immutable metadata, relationship, transformation, validation, rights, preservation, delivery, lifecycle or correction assertion with actor, authority, source, reason, method, RFC 3339 effective time and predecessor."],
            "delete": ["Apply copyright, contract, privacy, preservation, audit, retention and legal-hold policy; tombstone eligible records or erase authorized storage copies while preserving identity, material provenance and non-cascading external masters."]
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Media asset steward", "responsibilities": ["Own asset aggregate identity, rendition graph, roles, lifecycle and correction policy."]},
            {"name": "Rendition or technical metadata registrar", "responsibilities": ["Own representation identity, bytes, formats, characteristics, components, fixity and validation evidence."]},
            {"name": "Creator, producer or processing operator", "responsibilities": ["Own attributable capture, ingest, edit, transcode, render and export activities and settings."]},
            {"name": "Rights and publication authority", "responsibilities": ["Own rights bindings, license interpretation, embargo, territory, channel and accountable publication decisions."]},
            {"name": "Preservation custodian", "responsibilities": ["Own copies, storage, fixity schedules, migrations, retention, holds and recoverability evidence."]},
            {"name": "Accessibility and quality reviewer", "responsibilities": ["Own profile-qualified accessibility, technical, perceptual and fitness assessments."]},
            {"name": "Security, privacy or authenticity reviewer", "responsibilities": ["Review sensitive metadata, credentials, bindings, trust policy, encryption and protected disclosure."]},
            {"name": "Auditor", "responsibilities": ["Review identity, lineage, rights, lifecycle, corrections and destructive actions without rewriting originals."]}
        ],
        "access": {
            "default_rule": "Deny protected metadata, embargoed or licensed content and mutation unless active Dimension, role, purpose, rights instrument, territory, window, sensitivity, retention and field policy grant the action; expose the minimum necessary representation.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency preservation, security response or legally compelled access must be grounded, time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable provenance, rights, credential or legal-hold evidence."],
            "audit_requirements": ["Log actor, role, purpose, asset and rendition identity, action, decision, policy and standards versions, RFC 3339 timestamp with offset, affected bytes or fields, recipient, source evidence and outcome for privileged mutation, publication, disclosure, withdrawal or deletion."]
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": [
                "Read the nearest Dimension-owner AGENTS.md, media, rights, preservation, privacy, accessibility, delivery, retention and jurisdiction policies.",
                "Read this model AGENTS.md, pinned spec.yaml and required creative-work, publication, medium-specific, storage, rights, credential, evidence and decision instructions before mutation."
            ]
        }
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Media Asset / Rendition aggregate identity, technical representations, components, metadata, accessibility, derivation, rights, authenticity, preservation, quality, delivery, lifecycle and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Asset aggregate, rendition, file, bitstream, fragment, service, locator, storage copy and credential identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Rendition roles, media types, containers, codecs, profiles and conformance states are separately typed."},
            {"dimension": "direct properties", "status": "covered", "notes": "Byte length, digests, dimensions, duration, rates, resolution, colour, tracks, channels, parts and encoding properties are source-qualified."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Format identification, digest verification, decoding, metadata extraction, technical measurements and credential validation retain method and source."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Register, identify, verify, extract, transform, preserve, assess, publish, restrict, supersede, withdraw and delete functions expose authority and effects."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Draft, active, published, restricted, withdrawn, superseded, deleted and tombstoned states preserve immutable history."},
            {"dimension": "relationships", "status": "covered", "notes": "Work, edition, parent, ingredient, component, alternate, accessibility, storage, rights and credential links are typed."},
            {"dimension": "temporal", "status": "covered", "notes": "Creation, capture, ingest, transform, validation, preservation, publication, restriction, correction and deletion clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Content locations, described places, storage regions, territories and delivery regions are distinguished and time-qualified."},
            {"dimension": "provenance", "status": "covered", "notes": "Actors, tools, devices, software, versions, settings, prompts, methods, inputs, outputs, events and corrections are linked."},
            {"dimension": "ownership", "status": "covered", "notes": "Authorship, asset stewardship, copyright, licensed control, possession, custody, hosting and publication authority are not conflated."},
            {"dimension": "validation", "status": "covered", "notes": "Identity, digest scope, format, decode, profile, structure, metadata, accessibility, credential, quality and crosswalk validation are explicit."},
            {"dimension": "security and privacy", "status": "covered", "notes": "Sensitive metadata, encryption, credentials, trust inputs, redaction, leakage and minimum disclosure are represented."},
            {"dimension": "access", "status": "covered", "notes": "Permission, prohibition, duty, role, purpose, territory, window, embargo, accessibility and audited projection are represented."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Preservation, retention, legal hold, withdrawal, tombstone, storage-copy deletion and verified erasure are distinguished."},
            {"dimension": "interoperability", "status": "covered", "notes": "W3C, DCMI, IANA, PREMIS, METS, MIX, AudioMD, VideoMD, PBCore, EBUCore, IPTC, IIIF and C2PA projections pin versions and disclose loss."}
        ],
        "known_omissions": [
            "Image, audio, video, document, 3D, immersive, broadcast, streaming, archive and sector-specific technical profiles require specialist review.",
            "Creative works, publications, recordings, images, scenes, broadcasts, parties, storage services, agreements, rights instruments, credentials and decisions remain neighboring masters.",
            "Patent- or license-restricted codec conformance, broadcaster delivery specifications, platform moderation rules and jurisdiction-specific rights require separately pinned profiles.",
            "Automated rights grants, public release, authenticity conclusions, irreversible deletion and identity merge remain outside unreviewed agent authority."
        ],
        "conflicts": [
            "Media-resource standards differ on whether abstract works, manifestations and concrete encodings share one resource concept; this model requires explicit abstraction-level identities.",
            "Original, source, master, preservation master, mezzanine, access copy and best copy are role claims with provenance, not universal intrinsic states.",
            "Media type, file format, container, codec, profile, extension and format signature overlap operationally but are not interchangeable.",
            "Embedded, sidecar, catalogue and signed metadata can disagree; source-qualified assertions replace last-write-wins."
        ],
        "regional_assumptions": [
            "Copyright, moral rights, privacy, publicity rights, accessibility duties, retention, legal hold and deletion depend on jurisdiction, agreement, audience and purpose.",
            "EBUCore and PBCore reflect broadcast communities; IPTC reflects news and publishing; PREMIS, METS and IIIF reflect preservation and cultural-heritage practice.",
            "C2PA cryptographic validation provides provenance and trust signals but does not itself prove factual truth, copyright ownership or permission to use content."
        ],
        "adversarial_checks": [
            "Reject an asset or rendition without stable identity, abstraction boundary, master authority, revision and role.",
            "Reject filename, mutable URL, storage key, timestamp, title, checksum or credential identifier as universal asset identity.",
            "Reject a derivative that overwrites its source, loses parent or ingredient links, reuses rendition identity for changed bytes or hides transformation settings.",
            "Reject media type, container, codec, profile, extension and conformance collapsed into one field.",
            "Reject metadata conflict resolved by silent precedence or signed metadata treated as automatically true.",
            "Reject quality, accessibility or fitness claims without method, profile, target, time, threshold, uncertainty and reviewer.",
            "Reject possession, custody, storage or credential validity as proof of ownership, copyright or licensed use.",
            "Reject publication, disclosure, withdrawal or deletion outside rights, access, retention and legal-hold authority."
        ]
    }


def build():
    model = {
        "registry_id": "vr.wm-med-002",
        "model_id": "WM-MED-002",
        "name": "Media Asset / Rendition",
        "entry_kind": "aggregate",
        "purpose": "Represent one governed media-asset aggregate and its separately identified technical renditions, including bytes or services, characteristics, metadata, lineage, rights, preservation, quality, delivery and lifecycle.",
        "scope_statement": "Owns media-asset aggregate identity and revision; separately addressable rendition identities and roles; work and edition references; rendition graph and equivalence claims; byte or service boundaries; fixity; media type, container, codec, profile and conformance; technical characteristics and components; embedded and sidecar metadata with precedence and conflicts; semantic annotations; language, accessibility and alternate representations; creation, capture, derivation and processing lineage; rights and policy bindings; authenticity evidence; storage copies, preservation, quality and fitness assessments; delivery, publication, lifecycle, correction, access, retention and loss-aware projections. Creative works, publications, medium-specific content semantics, parties, agreements, rights instruments, policies, credentials, storage systems, services and accountable decisions remain external.",
        "in_scope": [
            "Media-asset aggregate identity, rendition identity, roles, relationships, byte or service boundary, fixity and technical description",
            "Metadata, accessibility, localization, derivation, rights, authenticity, storage, preservation, quality and delivery assertions",
            "Lifecycle, correction, access, retention, audit and version-pinned loss-aware interoperability"
        ],
        "out_of_scope": [
            "Owning creative-work, publication or edition, recording, image, scene, broadcast, party, agreement, rights instrument, credential, storage system, service or decision lifecycles",
            "Treating filename, URL, storage key, checksum, metadata block, credential, best-copy label or publication endpoint as universal media identity",
            "Inferring originality, factual truth, ownership, copyright, permitted use, accessibility or fitness without source-qualified evidence",
            "Publishing, granting rights, disclosing protected content, mutating external systems or irreversibly deleting bytes without accountable authority"
        ],
        "boundary_notes": [
            {"neighbor": "WM-MED-001 Creative Work / Content", "distinction": "The registered parent owns abstract intellectual content and authorship. This model owns the operational aggregate and concrete technical representations without making the work and its encodings one identity.", "source_refs": ["SRC-001", "SRC-002", "SRC-011", "SRC-012", "SRC-016"]},
            {"neighbor": "WM-MED-003 Publication / Edition", "distinction": "A publication or edition owns release and edition identity, audience and publication context. It may select media renditions but does not replace their byte, format, lineage or preservation identities.", "source_refs": ["SRC-002", "SRC-011", "SRC-012", "SRC-016"]},
            {"neighbor": "WM-MED-004, WM-MED-005, WM-MED-006 and WM-MED-007 specialist models", "distinction": "Audio/video, image/graphic, 3D/scene and broadcast/stream models extend medium-specific semantics. The present aggregate keeps only shared format-independent representation controls.", "source_refs": ["SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-021"]},
            {"neighbor": "WM-MED-008 Content Authenticity Credential", "distinction": "A credential binds signed provenance assertions to an asset or rendition. It has its own issuer, manifest, signature and validation lifecycle and cannot become asset identity or prove semantic truth.", "source_refs": ["SRC-018", "SRC-020"]},
            {"neighbor": "File, bitstream, fragment, service, locator and storage copy", "distinction": "These are technical representations, parts, access mechanisms or holdings. Mutable locators and storage placement never replace stable asset and rendition identity.", "source_refs": ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-015", "SRC-016"]},
            {"neighbor": "Rights instrument, ownership, custody and permitted use", "distinction": "Copyright, ownership, license, policy, possession, custody and publication authority are distinct external assertions. Technical control over bytes does not establish legal authority.", "source_refs": ["SRC-002", "SRC-007", "SRC-011", "SRC-013", "SRC-014", "SRC-019"]}
        ]
    }
    composition = [
        {"target": "WM-MED-001 Creative Work / Content", "relation": "REFERENCE", "purpose": "Resolve the abstract work or content while retaining separate operational asset and rendition identities.", "required": True, "source_refs": ["SRC-001", "SRC-002", "SRC-011", "SRC-012", "SRC-016"]},
        {"target": "WM-MED-003 Publication / Edition", "relation": "REFERENCE", "purpose": "Resolve release and edition context without importing publication lifecycle into the technical asset.", "required": False, "source_refs": ["SRC-002", "SRC-011", "SRC-016"]},
        {"target": "WM-MED-004 Audio / Video Recording, WM-MED-005 Image / Graphic, WM-MED-006 3D Asset / Scene and WM-MED-007 Broadcast / Stream", "relation": "EXTEND", "purpose": "Apply medium-specific technical, structural and lifecycle profiles over the common rendition controls.", "required": False, "source_refs": ["SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-021"]},
        {"target": "WM-MED-008 Content Authenticity Credential", "relation": "MIX-IN", "purpose": "Bind external signed provenance and validation evidence to a concrete asset or rendition.", "required": False, "source_refs": ["SRC-018", "SRC-020"]},
        {"target": "Rights, party, agreement, policy, storage, service, event, evidence and decision masters", "relation": "REFERENCE", "purpose": "Resolve legal, organizational, operational and evidential context without importing those lifecycles.", "required": False, "source_refs": ["SRC-002", "SRC-005", "SRC-007", "SRC-018", "SRC-019", "SRC-020"]},
        {"target": "W3C Media Ontology, DCMI Terms, IANA media types and HTTP", "relation": "ALIGN", "purpose": "Project common media description, vocabulary, representation and retrieval semantics.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005"]},
        {"target": "PREMIS, METS, MIX, AudioMD, VideoMD, PBCore and EBUCore", "relation": "ALIGN", "purpose": "Project preservation, packaging, technical image and audiovisual metadata with pinned profiles.", "required": False, "source_refs": ["SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012"]},
        {"target": "IPTC Photo Metadata and Video Metadata Hub", "relation": "ALIGN", "purpose": "Project news and publishing descriptive, administrative, rights and technical metadata.", "required": False, "source_refs": ["SRC-013", "SRC-014"]},
        {"target": "IIIF Image and Presentation APIs, Web Annotation, WebVTT and WCAG", "relation": "ALIGN", "purpose": "Project delivery, compound-object, annotation, timed-text and accessibility semantics.", "required": False, "source_refs": ["SRC-015", "SRC-016", "SRC-017", "SRC-021", "SRC-022"]},
        {"target": "PROV-O, ODRL and C2PA", "relation": "ALIGN", "purpose": "Project derivation, policy and cryptographically bound authenticity evidence without collapsing their trust domains.", "required": False, "source_refs": ["SRC-018", "SRC-019", "SRC-020"]},
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
