#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-MED-008."""

import importlib.util
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
BASE_PATH = RUN.parent / "wm-knw-009" / "build_codex_result.py"
SPEC = importlib.util.spec_from_file_location("wm_knw_009_builder", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
AT = "2026-09-07T11:45:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "Content Credentials: C2PA Technical Specification", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html", "C2PA 2.4, April 2026", "standard", "Defines assertions, claims, manifests, content bindings, signatures, trust, validation, actions, ingredients, redaction and supported embedding profiles."),
    src(2, "Content Credentials JSON File Format", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.4/crJSON/crjson-format.html", "C2PA 2.4, April 2026", "standard", "Defines a JSON-LD derived view for evaluation and reporting while explicitly keeping the signed binary form authoritative."),
    src(3, "Attestation in the C2PA Framework", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/1.4/attestations/attestation.html", "Current official attestation document linked from C2PA 2.4", "standard", "Defines externally issued attestations, attestation manifests, credential holders and references to protected assertions."),
    src(4, "C2PA Soft Binding API", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.4/softbinding/Decoupled.html", "C2PA 2.4, April 2026", "standard", "Defines fingerprint and watermark lookup, manifest repositories, recovery responses, confidence and durable credential discovery."),
    src(5, "C2PA Implementation Guidance", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.2/guidance/Guidance.html", "Current official guidance linked from C2PA 2.4", "first-party-doc", "Explains signer, trust-list, private credential, validation, capture and workflow implementation choices."),
    src(6, "C2PA User Experience Guidance", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.2/ux/UX_Recommendations.html", "Current official UX guidance linked from C2PA 2.4", "first-party-doc", "Defines progressive disclosure, provenance indicators, validation communication, accessibility and user interpretation concerns."),
    src(7, "C2PA Security Considerations", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.4/security/Security_Considerations.html", "C2PA 2.4, April 2026", "first-party-doc", "Defines threat surfaces, signature and binding validation, ingredient verification, revocation, time and trust concerns."),
    src(8, "C2PA Harms Modelling", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.4/security/Harms_Modelling.html", "C2PA 2.4, April 2026", "first-party-doc", "Covers privacy, surveillance, coercion, exclusion, false confidence, removal and harms to vulnerable creators and subjects."),
    src(9, "Guidance for Artificial Intelligence and Machine Learning", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.3/ai-ml/ai_ml.html", "Current official AI/ML guidance linked from C2PA 2.4", "first-party-doc", "Defines AI disclosure, digital source types, training data and model-related provenance considerations."),
    src(10, "Human and Organizational Identity Recommendation", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/specifications/specifications/2.4/identity/identity.html", "C2PA 2.4, April 2026", "first-party-doc", "Separates signer credential identity from optional human or organizational identity assertions and identity providers."),
    src(11, "C2PA Conformance Explorer", "Coalition for Content Provenance and Authenticity", "https://spec.c2pa.org/conformance-explorer/", "Live conformance, signer trust and TSA trust registries, accessed 7 September 2026", "registry", "Publishes product conformance and current C2PA and TSA trust-list views used by validators."),
    src(12, "Verifiable Credentials Data Model v2.0", "World Wide Web Consortium", "https://www.w3.org/TR/vc-data-model-2.0/", "W3C Recommendation, 15 May 2025", "standard", "Defines issuer, holder, verifier, credential subject, claims, validity, status, evidence, schemas, presentations and trust boundaries."),
    src(13, "Verifiable Credential Data Integrity 1.0", "World Wide Web Consortium", "https://www.w3.org/TR/vc-data-integrity/", "W3C Recommendation, 15 May 2025", "standard", "Defines data-integrity proofs, verification results, cryptographic suites, resource integrity and transformation concerns."),
    src(14, "Securing Verifiable Credentials using JOSE and COSE", "World Wide Web Consortium", "https://www.w3.org/TR/vc-jose-cose/", "W3C Recommendation, 15 May 2025", "standard", "Defines JOSE, COSE and selective-disclosure envelopes for credentials without making one proof format part of the logical model."),
    src(15, "Controlled Identifiers v1.0", "World Wide Web Consortium", "https://www.w3.org/TR/cid-1.0/", "W3C Recommendation, 15 May 2025", "standard", "Defines controller documents, verification methods and relationships between controllers and cryptographic keys."),
    src(16, "Bitstring Status List v1.0", "World Wide Web Consortium", "https://www.w3.org/TR/vc-bitstring-status-list/", "W3C Recommendation, 15 May 2025", "standard", "Defines privacy-preserving credential revocation, suspension and refresh status publication and retrieval."),
    src(17, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entities, activities, agents, generation, use, derivation, attribution, revision and invalidation."),
    src(18, "Web Annotation Data Model", "World Wide Web Consortium", "https://www.w3.org/TR/annotation-model/", "W3C Recommendation, 23 February 2017", "standard", "Defines bodies, targets, selectors, motivations and provenance for region- or segment-scoped assertions."),
    src(19, "CBOR Object Signing and Encryption Structures", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc9052.html", "RFC 9052, August 2022; updated by RFC 9338", "standard", "Defines COSE protected and unprotected headers, payloads and signature structures used by C2PA and VC profiles."),
    src(20, "Internet X.509 Public Key Infrastructure Certificate and CRL Profile", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc5280.html", "RFC 5280, May 2008", "standard", "Defines certificate paths, extensions, validity, revocation lists, policies and certification path validation."),
    src(21, "Internet X.509 Public Key Infrastructure Time-Stamp Protocol", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3161.html", "RFC 3161, August 2001; updated by RFC 5816", "standard", "Defines trusted timestamp requests, tokens, message imprints, serial numbers and TSA evidence."),
    src(22, "Digest Fields", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc9530.html", "RFC 9530, February 2024", "standard", "Defines representation and content digests and algorithm identifiers for HTTP resources."),
    src(23, "JSON Canonicalization Scheme", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc8785.html", "RFC 8785, June 2020", "standard", "Defines deterministic JSON canonicalization for repeatable digest and signature inputs where the selected profile uses JSON."),
    src(24, "Date and Time on the Internet", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines interoperable timestamps with seconds and an explicit numeric offset or Z."),
    src(25, "IPTC Photo Metadata User Guide", "International Press Telecommunications Council", "https://www.iptc.org/std/photometadata/documentation/userguide/", "Current guide, accessed 7 September 2026", "standard", "Defines digital source type, creator, rights and image metadata guidance, including AI-generated and algorithmically altered sources."),
    src(26, "Artificial Intelligence Risk Management Framework: Generative AI Profile", "National Institute of Standards and Technology", "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf", "NIST AI 600-1, July 2024", "public-authority", "Treats provenance, watermarking, metadata, content authentication and transparency as complementary risk controls rather than truth guarantees."),
]


ROWS = [
    ("credential-identity-scope-and-asset-binding", "Credential identity, scope and asset binding", "Establish the credential subject and exact protected relationship without turning a representation or locator into identity.", [
        ("credential-manifest-claim-and-assertion-boundary", "Credential, manifest, claim and assertion boundary", ["SRC-001", "SRC-002", "SRC-003", "SRC-012", "SRC-013", "SRC-014"], [
            ("credential-identifier-namespace-version-issuer-holder-owner-and-master", "Credential identifier, namespace, version, issuer, holder, owner and master system", "identity"),
            ("manifest-store-active-manifest-claim-assertion-signature-and-presentation-boundary", "Manifest store, active manifest, claim, assertion, signature and presentation boundary", "composition")]),
        ("asset-subject-region-and-content-binding", "Asset subject, region and content binding", ["SRC-001", "SRC-004", "SRC-017", "SRC-018", "SRC-022"], [
            ("asset-rendition-segment-region-resource-and-credential-subject-binding", "Asset, rendition, segment, region, resource and credential-subject binding", "relationship"),
            ("hard-hash-soft-fingerprint-watermark-binding-algorithm-scope-and-recovery", "Hard hash, soft fingerprint, watermark binding, algorithm, scope and recovery", "evidence")])]),
    ("assertions-actions-ingredients-and-lineage", "Assertions, actions, ingredients and lineage", "Represent what was asserted and how content changed while keeping source events, parties, tools and assets as external masters.", [
        ("assertion-identity-payload-and-source", "Assertion identity, payload and source", ["SRC-001", "SRC-002", "SRC-003", "SRC-009", "SRC-012", "SRC-017", "SRC-025"], [
            ("assertion-label-version-instance-schema-format-source-and-claim-reference", "Assertion label, version, instance, schema, format, source and claim reference", "definition"),
            ("asserted-gathered-attested-metadata-digital-source-type-confidence-and-evidence", "Asserted, gathered or attested metadata, digital source type, confidence and evidence", "provenance")]),
        ("actions-ingredients-and-derivation-chain", "Actions, ingredients and derivation chain", ["SRC-001", "SRC-007", "SRC-009", "SRC-017", "SRC-018", "SRC-025", "SRC-026"], [
            ("capture-create-edit-generate-transform-publish-action-actor-tool-time-and-parameters", "Capture, create, edit, generate, transform or publish action, actor, tool, time and parameters", "event"),
            ("ingredient-parent-derived-composed-rendition-relationship-redaction-and-chain", "Ingredient, parent, derived, composed, rendition relationship, redaction and chain", "lifecycle")])]),
    ("signer-cryptography-time-and-credential-status", "Signer, cryptography, time and credential status", "Preserve who controlled the signing key, what bytes were protected and when validation evidence applied.", [
        ("signer-controller-key-and-signature", "Signer, controller, key and signature", ["SRC-001", "SRC-003", "SRC-005", "SRC-010", "SRC-013", "SRC-014", "SRC-015", "SRC-019", "SRC-020"], [
            ("signer-claim-generator-identity-provider-certificate-chain-policy-and-eku", "Signer, claim generator, identity provider, certificate chain, policy and extended key usage", "authority"),
            ("signature-suite-algorithm-key-id-protected-payload-canonicalization-and-digest", "Signature suite, algorithm, key ID, protected payload, canonicalization and digest", "security")]),
        ("trusted-time-status-and-algorithm-lifecycle", "Trusted time, status and algorithm lifecycle", ["SRC-001", "SRC-007", "SRC-011", "SRC-016", "SRC-020", "SRC-021", "SRC-024"], [
            ("claimed-signing-time-trusted-timestamp-validation-ingestion-and-observation-clocks", "Claimed signing time, trusted timestamp, validation, ingestion and observation clocks", "temporal"),
            ("certificate-validity-revocation-suspension-refresh-trust-at-signing-and-algorithm-agility", "Certificate validity, revocation, suspension, refresh, trust at signing and algorithm agility", "lifecycle")])]),
    ("storage-discovery-versioning-and-preservation", "Storage, discovery, versioning and preservation", "Keep embedded, external and recovered credentials resolvable across edits, metadata loss and cryptographic change.", [
        ("manifest-store-location-and-durable-discovery", "Manifest store location and durable discovery", ["SRC-001", "SRC-002", "SRC-004", "SRC-011", "SRC-022"], [
            ("embedded-external-cloud-repository-location-active-selection-and-receipt", "Embedded, external, cloud or repository location, active selection and receipt", "access"),
            ("soft-binding-query-repository-response-candidate-confidence-collision-and-recovery", "Soft-binding query, repository response, candidate confidence, collision and recovery", "process")]),
        ("manifest-lifecycle-preservation-and-failure", "Manifest lifecycle, preservation and failure", ["SRC-001", "SRC-004", "SRC-007", "SRC-016", "SRC-017", "SRC-020", "SRC-021", "SRC-022"], [
            ("standard-update-attestation-manifest-predecessor-successor-active-orphan-and-duplicate", "Standard, update or attestation manifest, predecessor, successor, active, orphan and duplicate", "lifecycle"),
            ("removed-corrupt-unbound-redacted-revoked-expired-archived-tombstoned-and-revalidation-state", "Removed, corrupt, unbound, redacted, revoked, expired, archived, tombstoned and revalidation state", "state")])]),
    ("validation-trust-decision-and-human-interpretation", "Validation, trust decision and human interpretation", "Return reproducible component evidence and communicate limits without converting technical validity into truth.", [
        ("validation-result-and-trust-policy", "Validation result and trust policy", ["SRC-001", "SRC-005", "SRC-007", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-016", "SRC-019", "SRC-020", "SRC-021"], [
            ("well-formed-valid-component-status-code-failure-evidence-validator-and-profile", "Well-formed or valid component, status code, failure evidence, validator and profile", "validation"),
            ("trust-list-anchor-private-store-policy-purpose-context-decision-and-review", "Trust list, anchor, private store, policy, purpose, context, decision and review", "decision")]),
        ("meaning-disclosure-and-accessible-explanation", "Meaning, disclosure and accessible explanation", ["SRC-001", "SRC-006", "SRC-008", "SRC-010", "SRC-012", "SRC-026"], [
            ("integrity-provenance-authenticity-identity-authorship-copyright-truth-and-endorsement-distinction", "Integrity, provenance, authenticity, identity, authorship, copyright, truth and endorsement distinction", "classification"),
            ("indicator-disclosure-level-summary-detail-accessibility-localization-warning-and-appeal", "Indicator, disclosure level, summary, detail, accessibility, localization, warning and appeal", "quality")])]),
    ("privacy-governance-and-interoperability", "Privacy, governance and interoperability", "Control disclosure and extension while preserving verifiable meaning across standards and jurisdictions.", [
        ("privacy-safety-harms-and-access-control", "Privacy, safety, harms and access control", ["SRC-001", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-012", "SRC-016", "SRC-026"], [
            ("consent-data-minimization-selective-disclosure-redaction-sensitive-identity-location-and-device-data", "Consent, data minimization, selective disclosure, redaction, sensitive identity, location and device data", "privacy"),
            ("surveillance-coercion-exclusion-spoofing-removal-reidentification-harm-review-and-remedy", "Surveillance, coercion, exclusion, spoofing, removal, re-identification, harm review and remedy", "exception")]),
        ("profiles-crosswalk-conformance-and-semantic-loss", "Profiles, crosswalk, conformance and semantic loss", [f"SRC-{i:03d}" for i in range(1, 27)], [
            ("c2pa-vc-data-integrity-jose-cose-x509-prov-annotation-iptc-crosswalk", "C2PA, VC, Data Integrity, JOSE, COSE, X.509, PROV, Annotation and IPTC crosswalk", "interoperability"),
            ("profile-version-license-conformance-transformation-round-trip-and-semantic-loss", "Profile, version, license, conformance, transformation, round trip and semantic loss", "requirement")])]),
]


KIND_CYCLE = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 7) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 14) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 21) % len(KIND_CYCLE)]]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {lower} as a source-qualified Content Provenance Credential assertion while media assets, creative works, parties, keys, tools, events, repositories, rights and trust decisions retain external mastership.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which credential, manifest, claim, assertion, asset or region identity, version, values and bindings establish {lower}?", "kind": kinds[0], "answer_data": ["credential, manifest, claim, assertion, asset, rendition and region identifiers", "version, profile, schema, binding method, algorithm, scope and explicit unknowns", "subject, issuer, signer, holder, validator, source system and external-master references"]},
            {"id": f"{fid}-q02", "text": f"Who creates, asserts, gathers, signs, timestamps, stores, validates, trusts, discloses or reviews {lower}, and under which authority?", "kind": kinds[1], "answer_data": ["issuer, signer, claim generator, identity provider, TSA, repository, validator, verifier and reviewer roles", "key control, certificate, trust anchor, policy, consent, purpose, access and review authority", "source, profile, jurisdiction, audience, recipient and accountable decision references"]},
            {"id": f"{fid}-q03", "text": f"Which actions, ingredients, clocks, lineage, status, evidence, failures and competing assertions qualify {lower}?", "kind": kinds[2], "answer_data": ["capture, create, edit, generate, transform, publish, redact, revoke and recover events", "ingredient, predecessor, successor, derivation, active manifest, signature, timestamp and status evidence", "validation codes, conflicts, uncertainty, limitations, harms, corrections and revalidation triggers"]},
            {"id": f"{fid}-q04", "text": f"Which security, privacy, retention, disclosure and interoperability checks apply to {lower}?", "kind": kinds[3], "answer_data": ["signature, digest, content binding, certificate path, revocation, timestamp and component validation", "minimization, consent, selective disclosure, redaction, access, retention, appeal and audit controls", "source and target versions, crosswalk, conformance, transformation, round-trip and semantic-loss report"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed credential-scoped values and references required to answer the governed questions for {lower}.", "value_kind": "object", "cardinality": "1", "required": True, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": f"{name} evidence manifest", "description": f"Digest-addressed manifest of credential identity, bindings, assertions, actors, clocks, cryptographic evidence, validation, policy, lifecycle and projection outcomes supporting {lower}.", "media_or_form": ["application/c2pa", "application/json", "application/ld+json", "application/cbor", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative credential or manifest identifier first, then issuer-qualified globally resolvable IRI, otherwise Dimension UUID or ULID; bind the target asset or region, immutable revision, proof profile and artifact digest separately.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


ENGINE = BASE.BASE
ENGINE.SOURCES = SOURCES
ENGINE.ROWS = ROWS
ENGINE.KIND_CYCLE = KIND_CYCLE
ENGINE.make_finding = make_finding


FUNCTION_ROWS = [
    ("register-provenance-credential", "Register provenance credential", "Create one stable credential identity, subject scope and master authority without claiming media identity or truth.", ["credential proposal", "asset or subject reference", "issuer authority"], ["credential identifier", "initial revision"], ["active Dimension", "identity boundary explicit"], ["identity, profile and unknowns are appended"], ["SRC-001", "SRC-003", "SRC-012"]),
    ("compose-credential-assertions", "Compose credential assertions", "Add typed assertions and claim references with explicit source, schema, instance, scope and evidence.", ["credential revision", "assertion payloads", "source metadata"], ["versioned assertion set"], ["issuer and schema resolvable"], ["prior assertions remain immutable"], ["SRC-001", "SRC-002", "SRC-003", "SRC-012"]),
    ("bind-credential-to-content", "Bind credential to content", "Create hard or soft bindings to an exact asset, rendition, segment or region.", ["credential", "target asset", "binding profile"], ["qualified content binding"], ["target and algorithm explicit"], ["binding never replaces asset identity"], ["SRC-001", "SRC-004", "SRC-018", "SRC-022"]),
    ("record-action-and-ingredient-lineage", "Record action and ingredient lineage", "Append capture, edit, generation, transformation and ingredient relationships without importing their external lifecycles.", ["credential", "actions", "ingredient references"], ["qualified provenance chain"], ["actors, tools, times and inputs source-qualified"], ["derivation graph and redactions remain auditable"], ["SRC-001", "SRC-007", "SRC-009", "SRC-017"]),
    ("issue-and-sign-credential", "Issue and sign credential", "Protect a canonical claim with an authorized signing key and an explicitly pinned proof profile.", ["claim", "signing authority", "proof profile"], ["signed credential", "signature evidence"], ["key control, certificate policy and algorithm acceptable"], ["unsigned claim and signature remain distinguishable"], ["SRC-001", "SRC-013", "SRC-014", "SRC-015", "SRC-019", "SRC-020"]),
    ("timestamp-and-publish-status", "Timestamp and publish status", "Attach trusted-time evidence and publish applicable revocation, suspension or refresh information.", ["signed credential", "TSA or status authority", "policy"], ["timestamp token", "status reference"], ["trust path and clocks explicit"], ["claimed time, trusted time and observation time stay distinct"], ["SRC-001", "SRC-011", "SRC-016", "SRC-021", "SRC-024"]),
    ("store-embed-or-externalize", "Store, embed or externalize credential", "Place a manifest store in or outside an asset while preserving resolvability, receipts and integrity.", ["credential", "asset", "storage profile"], ["embedded or external binding", "repository receipt"], ["location and retrieval policy valid"], ["storage location never becomes credential identity"], ["SRC-001", "SRC-002", "SRC-004"]),
    ("recover-durable-credential", "Recover durable credential", "Use fingerprint or watermark evidence to query repositories and return ranked credential candidates.", ["asset observation", "soft binding", "repository endpoint"], ["candidate set", "recovery evidence"], ["privacy and collision policy applied"], ["recovered candidate requires normal validation"], ["SRC-004", "SRC-007", "SRC-008"]),
    ("validate-credential", "Validate credential", "Validate structure, claim, signature, time, status, assertions, ingredients and asset binding as separate components.", ["credential", "asset", "validation profile"], ["component results", "validation report"], ["profile, algorithms and trust configuration pinned"], ["all failures and informational statuses remain attributable"], ["SRC-001", "SRC-007", "SRC-011", "SRC-013", "SRC-019", "SRC-020"]),
    ("evaluate-trust-and-disclose", "Evaluate trust and disclose", "Apply verifier purpose and trust policy, then present accessible provenance without implying factual truth.", ["validation report", "trust policy", "audience context"], ["trust decision", "disclosure view"], ["decision scope and limitations explicit"], ["technical validity and human judgment remain separate"], ["SRC-001", "SRC-005", "SRC-006", "SRC-008", "SRC-012"]),
    ("revise-redact-revoke-or-tombstone", "Revise, redact, revoke or tombstone", "Append an authorized lifecycle change while preserving prior credential and validation history.", ["credential revision", "change or status event", "authority"], ["successor or status assertion", "notice"], ["retention and legal hold checked"], ["last-write-wins and silent deletion are rejected"], ["SRC-001", "SRC-007", "SRC-008", "SRC-016", "SRC-017"]),
    ("validate-and-project-crosswalk", "Validate and project crosswalk", "Produce version-pinned C2PA, VC, PROV, IPTC or generic projections with explicit semantic loss.", ["credential revision", "target profile", "mapping"], ["target projection", "validation and loss report"], ["source and target releases pinned"], ["canonical credential remains unchanged"], [f"SRC-{i:03d}" for i in range(1, 27)]),
]
ENGINE.FUNCTION_ROWS = FUNCTION_ROWS


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Declare the Dimension owner, credential master, issuer authority, signer and key custodian, identity provider, TSA, repository operator, validator, trust-policy owner, privacy steward and independent reviewer.",
                "Register credential, manifest, assertion, action, ingredient, binding, signature, certificate, timestamp, status, validation and lifecycle vocabularies.",
                "Register media assets, creative works, parties, devices, software, keys, certificates, events, repositories, rights instruments, evidence and trust decisions separately.",
                "Pin C2PA, VC, cryptographic, identity, status, provenance, media-metadata, privacy, retention and jurisdictional profiles."
            ],
            "namespace_guidance": "Mint only Dimension-owned credential, manifest, assertion, binding, validation, disclosure and lifecycle identifiers locally; preserve asset, work, party, device, tool, key, certificate, event, repository, rights, evidence and decision identifiers as typed external references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local credential, asset, assertion, identity, key, trust, status, validation, access, retention and provenance registries"]
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by registry ID, model version, authoritative credential identifier, immutable revision, issuer, subject scope and proof profile; never by filename, URL, title, signature bytes, hash or timestamp alone.",
                "Keep asset, rendition, credential, manifest store, manifest, claim, assertion, attestation, signature, certificate, trust policy, validation result, trust decision and display label distinct."
            ],
            "patch_rules": [
                "Additive extensions declare target node, namespace, issuer authority, source, schema and standards versions, access scope, validation behavior and interoperability impact.",
                "Breaking credential identity, subject, issuer, binding, claim, proof, trust, status or lifecycle changes require an immutable successor, migration and crosswalk map, compatibility declaration and continued resolution of prior versions."
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when credential identity, subject binding, issuer, claim, proof, validation, status, provenance, privacy and access meaning remain intact.",
                "C2PA, VC, Data Integrity, JOSE, COSE, X.509, PROV, Annotation and IPTC mappings pin releases and declare transformed, inferred, omitted, unverifiable or non-round-trippable values."
            ]
        },
        "artifact_rules": {
            "identity_priority": [
                "Authoritative credential or manifest identifier issued by the declared credential master.",
                "Issuer-qualified globally resolvable IRI whose subject and revision semantics match the credential.",
                "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."
            ],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit numeric offset or Z; keep asset creation, claim generation, claimed signing, trusted timestamp, publication, validation, observation, revocation, recovery and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {credential-id}--{artifact-kind}--{revision-or-event-id}; never use a filename, asset title, URL, hash, signer name or date alone as identity.",
            "integrity_rule": "Store credential and target identifiers, immutable revision, media type, byte length, digest and scope, proof and canonicalization profiles, issuer, signer, clocks, certificate and status evidence, validation outcome, privacy and access marking, retention and semantic-loss declaration."
        },
        "policies": [
            "The adopting Dimension declares who may issue, assert, gather, sign, timestamp, store, recover, validate, trust, disclose, redact, revoke and tombstone credentials.",
            "Every usable credential requires stable identity, subject scope, issuer, claim or assertion set, content binding when applicable, proof profile, lifecycle, provenance and applicable privacy and access context.",
            "Agents never infer factual truth, authorship, copyright, ownership, editorial endorsement, safety or universal trust from a valid signature, trusted signer, watermark, label or provenance chain alone.",
            "Media assets, works, parties, devices, software, keys, certificates, events, repositories, rights instruments, evidence and accountable trust decisions remain external masters.",
            "Agents may perform reversible discovery, extraction, validation and projection under delegation; signing, identity attestation, trust-list mutation, protected disclosure, revocation and destructive deletion require accountable authority."
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, credential identity and revision, target asset and region, validation horizon, trust policy, freshness, sensitivity, retention and access policy; return the minimum necessary credential and disclosure projection."],
            "create": ["Create stable credential identity with master authority, subject scope, issuer, assertion sources, binding profile, proof policy, lifecycle, privacy context and explicit unknowns before signing or publication."],
            "update": ["Append an immutable assertion, action, ingredient, binding, signature, timestamp, status, validation, trust or redaction revision with actor, authority, source, reason, RFC 3339 effective time and predecessor."],
            "delete": ["Apply privacy, rights, dispute, audit, preservation, retention and legal-hold policy; tombstone eligible credential-owned records or remove authorized projections while preserving material identity, revocation, validation, provenance and non-cascading external references."]
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Credential steward", "responsibilities": ["Own credential identity, scope, schema, lifecycle, revision and interoperability policy."]},
            {"name": "Issuer or assertion authority", "responsibilities": ["Own the meaning, source and authority of credential claims and assertions."]},
            {"name": "Signer and key custodian", "responsibilities": ["Control approved signing credentials, proof profiles, rotation and compromise response."]},
            {"name": "Identity or attestation provider", "responsibilities": ["Own separately scoped signer, human or organizational identity evidence."]},
            {"name": "Timestamp or status authority", "responsibilities": ["Own trusted-time, revocation, suspension and refresh evidence."]},
            {"name": "Repository and preservation custodian", "responsibilities": ["Own durable storage, recovery, receipts, retention and revalidation triggers."]},
            {"name": "Validator or verifier", "responsibilities": ["Run pinned validation and trust policy, preserving component evidence and limitations."]},
            {"name": "Privacy and harm reviewer", "responsibilities": ["Own minimization, consent, redaction, disclosure, misuse and remedy controls."]},
            {"name": "Independent auditor", "responsibilities": ["Review identity, binding, proof, trust, validation, lifecycle and access without rewriting originals."]}
        ],
        "access": {
            "default_rule": "Deny sensitive provenance disclosure and mutation unless active Dimension, role, purpose, consent or lawful basis, recipient, policy, time, retention and field controls grant the action; expose the minimum necessary projection.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency safety, incident response or legally compelled access must be grounded, time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable credential identity, revocation, validation or legal-hold evidence."],
            "audit_requirements": ["Log actor, role, purpose, credential and target identity, action, decision, policy, trust and standards versions, RFC 3339 timestamp with offset, affected assertions or projections, recipient, source evidence and outcome for privileged signing, trust, disclosure, revocation or deletion."]
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": [
                "Read the nearest Dimension-owner AGENTS.md and credential, identity, key, trust, privacy, access, retention, incident and jurisdiction policies.",
                "Read this model AGENTS.md, pinned spec.yaml and required asset, work, party, device, software, key, certificate, event, repository, rights, evidence and decision instructions before mutation."
            ]
        }
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Content Provenance Credential identity, subject binding, assertions, actions, ingredients, derivation, signer and key evidence, trusted time, status, storage, recovery, validation, trust, disclosure, privacy, harms, lifecycle and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Credential, manifest store, manifest, claim, assertion, attestation, signature, asset and validation identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Standard, update, attestation and durable credentials plus assertion, binding and digital-source types are explicit."},
            {"dimension": "direct properties", "status": "covered", "notes": "Issuer, subject, schema, version, assertions, profile, binding, signature, time, status and lifecycle are covered."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Hard hashes, fingerprints, watermarks, repository discovery and validator observations retain method and confidence."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Register, assert, bind, record lineage, sign, timestamp, store, recover, validate, disclose, revise and project functions declare authority and effects."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Draft, issued, active, superseded, redacted, revoked, expired, unbound, corrupt, archived and tombstoned states preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Assets, renditions, regions, ingredients, actors, tools, signers, certificates, repositories, validators and decisions use typed references."},
            {"dimension": "temporal", "status": "covered", "notes": "Creation, action, claim, signing, trusted timestamp, publication, validation, observation, revocation, recovery and ingestion clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Asset regions, capture locations, processing locations, repository regions and applicable jurisdictions are separately scoped."},
            {"dimension": "provenance", "status": "covered", "notes": "Assertions, actions, ingredients, sources, actors, tools, derivations, redactions, validators and revisions form attributable lineage."},
            {"dimension": "ownership", "status": "covered", "notes": "Issuer, signer, holder, creator, subject, copyright holder, asset owner and trust-policy owner are not conflated."},
            {"dimension": "validation", "status": "covered", "notes": "Structure, claim, signature, time, status, assertion, ingredient and binding checks produce separate evidence and codes."},
            {"dimension": "security and privacy", "status": "covered", "notes": "Algorithm agility, key compromise, spoofing, removal, correlation, surveillance, minimization, consent and redaction are represented."},
            {"dimension": "access", "status": "covered", "notes": "Purpose, recipient, disclosure level, role, consent or lawful basis, minimum projection, appeal and audit are explicit."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Repository preservation, revocation history, revalidation, archival, tombstone, projection removal and legal hold are distinguished."},
            {"dimension": "interoperability", "status": "covered", "notes": "C2PA, VC, Data Integrity, JOSE, COSE, X.509, PROV, Annotation, HTTP digest and IPTC mappings disclose loss."}
        ],
        "known_omissions": [
            "Image, video, audio, document, live-stream, model, sensor, news, legal, health and jurisdiction-specific profiles require specialist review.",
            "Media assets, creative works, parties, identities, devices, software, keys, certificates, actions, repositories, rights, evidence and trust decisions remain neighboring masters.",
            "Decentralized transparency logs, anonymous credentials, zero-knowledge proofs, post-quantum migration, biometric identity and forensic truth assessment remain future profiles."
        ],
        "conflicts": [
            "C2PA Content Credential, W3C Verifiable Credential and generic provenance record have different subject, holder, proof and lifecycle semantics; crosswalks are projections, not identity equivalence.",
            "A cryptographically valid credential can carry false, incomplete, misleading or privacy-invasive assertions; validity, signer trust, assertion truth and asset trustworthiness remain separate results.",
            "Hard binding proves exact byte or region association while soft binding supports probabilistic recovery; neither is universal asset identity or proof of authorship.",
            "Revocation and trusted timestamps can preserve historical validity decisions, but current trust lists, current certificate status and trust at signing time are not interchangeable."
        ],
        "regional_assumptions": [
            "Identity, electronic-signature, evidentiary, copyright, privacy, biometric, consumer-protection, records and disclosure duties depend on jurisdiction and purpose.",
            "C2PA trust lists and conformance results are ecosystem-specific signals and do not create universal legal or factual trust.",
            "IPTC digital-source terms are media-industry vocabulary and must not be treated as complete technical descriptions of AI generation or editing."
        ],
        "adversarial_checks": [
            "Reject a credential without stable identity, revision, issuer, subject scope, master authority, profile, provenance and lifecycle.",
            "Reject an asset, rendition, manifest store, manifest, claim, assertion, signature, certificate, validation result or display label represented as the credential itself without an explicit profile rule.",
            "Reject a content binding without exact target scope, algorithm, digest or soft-binding evidence, profile and validation status.",
            "Reject a valid signature or trusted certificate as proof of factual truth, authorship, copyright, editorial approval, safety or universal asset authenticity.",
            "Reject claimed signing time as trusted time, current certificate status as historical status or a trust-list match as a context-free trust decision.",
            "Reject a recovered soft-binding candidate that bypasses normal signature, assertion, ingredient and asset validation.",
            "Reject redaction, update, revocation, metadata removal or destructive deletion that silently erases prior public lineage, validation evidence or legal hold.",
            "Reject disclosure of identity, location, device, biometric or behavioral data without purpose, minimum necessity, authority, recipient, retention and remedy controls.",
            "Reject crosswalk output that omits source and target releases, transformation trace, cryptographic verification limits and semantic-loss declaration."
        ]
    }


def build():
    model = {
        "registry_id": "vr.wm-med-008",
        "model_id": "WM-MED-008",
        "name": "Content Provenance Credential",
        "entry_kind": "aggregate",
        "purpose": "Represent an issuer-attributable, integrity-protected and asset-bound set of provenance assertions with verifiable lineage, status, validation and disclosure context.",
        "scope_statement": "Owns content-provenance credential identity and revision; subject asset, rendition, segment and region scope; manifest, claim, assertion and attestation composition; hard and soft content bindings; action, ingredient and derivation references; signer, claim-generator, identity-provider, key, certificate, proof, timestamp and status evidence; embedded, external, repository and durable discovery bindings; validation component results and codes; trust-policy inputs and scoped decision references; human-facing disclosure; privacy, harms, lifecycle, preservation, access, retention, audit and loss-aware interoperability. Media assets, creative works, people, organizations, devices, software, keys, certificates, actions, repositories, rights instruments, evidence and trust decisions remain external masters.",
        "in_scope": [
            "Credential identity, subject and region scope, assertions, manifests, claims, bindings, signatures, times and status",
            "Actions, ingredients, derivation, storage, discovery, recovery, validation, trust inputs and disclosure",
            "Privacy, harms, lifecycle, preservation, access, retention, audit and version-pinned interoperability"
        ],
        "out_of_scope": [
            "Owning media-asset, creative-work, party, device, software, key, certificate, action, repository, rights, evidence or accountable trust-decision lifecycles",
            "Treating a hash, filename, URL, watermark, manifest, signature, certificate, trust-list entry, validation result or label as universal asset or credential identity",
            "Inferring factual truth, authorship, copyright, ownership, editorial endorsement, legality, safety or universal trust from provenance or cryptographic validity",
            "Signing, attesting identity, changing trust lists, disclosing protected provenance, revoking credentials or irreversibly deleting records without accountable authority"
        ],
        "boundary_notes": [
            {"neighbor": "WM-MED-002 Media Asset / Rendition", "distinction": "The media model owns byte-bearing assets, renditions, technical formats and fixity. This model owns credentials and qualified bindings to those assets without importing media identity.", "source_refs": ["SRC-001", "SRC-004", "SRC-022"]},
            {"neighbor": "WM-MED-001 Creative Work / Content", "distinction": "The work model owns intellectual content and authorship context. Provenance assertions may reference it but do not prove authorship, ownership or truth.", "source_refs": ["SRC-001", "SRC-012", "SRC-017"]},
            {"neighbor": "C2PA manifest, claim, assertion and manifest store", "distinction": "These are profile-specific composition parts or containers. The logical credential record retains their identities and roles without requiring one serialization.", "source_refs": ["SRC-001", "SRC-002", "SRC-003"]},
            {"neighbor": "Signer, issuer, human identity and organization", "distinction": "A signer controls a key, an issuer makes claims, and an optional identity provider attests a person or organization. None is inferred from an asset creator field alone.", "source_refs": ["SRC-001", "SRC-003", "SRC-010", "SRC-012", "SRC-015"]},
            {"neighbor": "Validation result and trust decision", "distinction": "Validation establishes component outcomes under pinned rules. A verifier separately decides trust for a purpose and context; neither result proves assertion truth.", "source_refs": ["SRC-001", "SRC-005", "SRC-007", "SRC-012", "SRC-013"]},
            {"neighbor": "Copyright, rights and editorial policy", "distinction": "Credentials can carry or reference rights and editorial assertions, but legal ownership, permission and accountable publication decisions remain external.", "source_refs": ["SRC-001", "SRC-006", "SRC-008", "SRC-025"]},
            {"neighbor": "W3C Verifiable Credential", "distinction": "VC 2.0 supplies a broader issuer-holder-verifier claim model. C2PA and VC representations may be mapped only with explicit subject, proof, status and lifecycle semantics.", "source_refs": ["SRC-012", "SRC-013", "SRC-014", "SRC-016"]}
        ]
    }
    composition = [
        {"target": "WM-MED-002 Media Asset / Rendition", "relation": "MIX-IN", "purpose": "Bind credentials to exact media assets, renditions, segments or regions while the media model retains identity and technical mastership.", "required": True, "source_refs": ["SRC-001", "SRC-004", "SRC-022"]},
        {"target": "WM-MED-001 Creative Work / Content", "relation": "REFERENCE", "purpose": "Resolve intellectual work context without using provenance as proof of authorship, ownership or truth.", "required": False, "source_refs": ["SRC-001", "SRC-012", "SRC-017"]},
        {"target": "Party, identity, device, software, key, certificate, action, repository, rights, evidence and decision masters", "relation": "REFERENCE", "purpose": "Resolve actors, mechanisms, events, custody, legal context and accountable decisions without importing their lifecycles.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-007", "SRC-010", "SRC-015", "SRC-017", "SRC-020"]},
        {"target": "C2PA 2.4 Content Credentials, crJSON, Attestations and Soft Binding API", "relation": "ALIGN", "purpose": "Project the principal content-provenance ecosystem while preserving format independence and exposing version-specific semantics.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004"]},
        {"target": "C2PA implementation, UX, security, harms, AI/ML, identity and conformance guidance", "relation": "ALIGN", "purpose": "Project implementation and governance controls separately from normative credential structure.", "required": False, "source_refs": ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011"]},
        {"target": "W3C Verifiable Credentials 2.0, Data Integrity, VC JOSE/COSE, Controlled Identifiers and Bitstring Status", "relation": "ALIGN", "purpose": "Project generic credential, proof, controller and status semantics with explicit non-equivalence to C2PA roles.", "required": False, "source_refs": ["SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"]},
        {"target": "PROV-O and Web Annotation", "relation": "ALIGN", "purpose": "Project derivation, activity, agent and region-scoped assertion graphs.", "required": False, "source_refs": ["SRC-017", "SRC-018"]},
        {"target": "COSE, X.509 PKIX and Time-Stamp Protocol", "relation": "ALIGN", "purpose": "Project protected envelopes, certificate paths, revocation and trusted-time evidence without making one proof suite canonical.", "required": False, "source_refs": ["SRC-019", "SRC-020", "SRC-021"]},
        {"target": "HTTP Digest Fields, JSON Canonicalization and RFC 3339", "relation": "ALIGN", "purpose": "Project digest, deterministic representation and unambiguous clock rules where adopted profiles require them.", "required": False, "source_refs": ["SRC-022", "SRC-023", "SRC-024"]},
        {"target": "IPTC Photo Metadata and NIST Generative AI Profile", "relation": "ALIGN", "purpose": "Project digital-source vocabulary and complementary AI transparency and risk-control context.", "required": False, "source_refs": ["SRC-025", "SRC-026"]}
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": ENGINE.structure(), "functions": ENGINE.functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
