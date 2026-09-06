#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-ORG-006."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent

SOURCES = [
    {"id":"SRC-001","title":"The Organization Ontology","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/vocab-org/","version_or_date":"W3C Recommendation, 16 January 2014","source_type":"ontology","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Defines org:Membership as a qualified n-ary relationship among an agent, organization and role, supports duration, and distinguishes membership from a post that may exist without a holder."},
    {"id":"SRC-002","title":"Time Ontology in OWL","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/owl-time/","version_or_date":"W3C Recommendation, 19 October 2017; current 15 November 2022 edition","source_type":"ontology","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Provides instants, intervals, durations and temporal relations for membership validity, role bindings, decisions and non-contiguous periods."},
    {"id":"SRC-003","title":"PROV-O: The PROV Ontology","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/prov-o/","version_or_date":"W3C Recommendation, 30 April 2013","source_type":"ontology","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Provides entities, activities, agents, attribution, delegation, revision and qualified influence for admission, lifecycle, evidence and correction provenance."},
    {"id":"SRC-004","title":"ODRL Information Model 2.2","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/odrl-model/","version_or_date":"W3C Recommendation, 15 February 2018","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Provides policy, permission, prohibition, duty, party, action and constraint concepts for referenced membership terms without making policy evaluation part of the relationship."},
    {"id":"SRC-005","title":"Verifiable Credentials Data Model v2.0","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/vc-data-model-2.0/","version_or_date":"W3C Recommendation, 15 May 2025","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Provides issuer, credential subject, validity, status, schema, terms of use and evidence for optional portable membership attestations; the credential remains evidence, not the membership."},
    {"id":"SRC-006","title":"LegalRuleML Core Specification Version 1.0","organization":"OASIS Open","url":"https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/os/legalruleml-core-spec-v1.0-os.html","version_or_date":"OASIS Standard, 30 August 2021","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Provides authority, jurisdiction, role and legal-rule metadata patterns for memberships constituted by law, charter, bylaws, resolution or other governed instruments."},
    {"id":"SRC-007","title":"SKOS Simple Knowledge Organization System Reference","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/skos-reference/","version_or_date":"W3C Recommendation, 18 August 2009","source_type":"ontology","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Provides stable concept schemes, identifiers, labels, notations, hierarchies and mappings for membership types, roles, standing and reason vocabularies."},
    {"id":"SRC-008","title":"General Data Protection Regulation","organization":"European Union","url":"https://eur-lex.europa.eu/eli/reg/2016/679/oj","version_or_date":"Regulation (EU) 2016/679, 27 April 2016","source_type":"legislation","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Provides an EU privacy profile for purpose limitation, minimization, accuracy, retention, security, access and rectification where membership data concerns a natural person."},
    {"id":"SRC-009","title":"Date and Time on the Internet: Timestamps","organization":"Internet Engineering Task Force","url":"https://www.rfc-editor.org/rfc/rfc3339","version_or_date":"RFC 3339, July 2002","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:20:00Z","relevance":"Defines interoperable timestamps with seconds and explicit UTC relation for admission, lifecycle, assertion and knowledge times."},
]

BUNDLES = [
    ("relationship-identity-parties-and-scheme", "Relationship identity, parties and scheme", "Identifies one membership and the member, organization or group and governing membership scheme.", "A direct memberOf edge is insufficient when role, validity, basis and standing must be qualified and independently governed.", ["SRC-001","SRC-003","SRC-007"], [
        ("membership-master-identity", "Membership master identity", "Stable relationship identity, source systems, aliases and successor lineage.", ["SRC-001","SRC-003"], [
            ("authoritative-membership-identifier-and-master-system", "Authoritative membership identifier and master system", "The stable relationship identifier, issuer, namespace, master system, local keys and resolution status.", "identity", ["SRC-001","SRC-003"], "identifier", True),
            ("duplicate-merge-split-reissue-and-successor-lineage", "Duplicate, merge, split, reissue and successor lineage", "Reconciliation and successor rules that preserve cited identities and prior assertions.", "lifecycle", ["SRC-003"], "object", False),
        ]),
        ("parties-type-and-governing-scheme", "Parties, type and governing scheme", "Member and organization bindings plus profile-qualified classification.", ["SRC-001","SRC-006","SRC-007"], [
            ("member-agent-and-organization-or-group-bindings", "Member agent and organization or group bindings", "Typed references to the member agent and admitting organization or governed group with identity authority and intervals.", "relationship", ["SRC-001"], "object", True),
            ("membership-type-profile-classification-and-scheme-version", "Membership type, profile, classification and scheme version", "Versioned type and profile concepts, scheme authority, applicability and class-distinguishing criteria.", "classification", ["SRC-001","SRC-006","SRC-007"], "collection", True),
        ]),
    ]),
    ("admission-eligibility-and-authority", "Admission, eligibility and authority", "Explains how membership is proposed, evaluated and admitted under a governing basis.", "Membership existence and standing require attributable authority and evidence, not directory presence, payment or self-assertion alone.", ["SRC-001","SRC-003","SRC-005","SRC-006"], [
        ("application-nomination-and-eligibility", "Application, nomination and eligibility", "External request, sponsorship and eligibility assertions linked to this relationship.", ["SRC-003","SRC-006"], [
            ("application-nomination-invitation-and-sponsor-reference", "Application, nomination, invitation and sponsor reference", "References the initiating request or act, nominator, sponsor, requested class, time and provenance.", "provenance", ["SRC-003","SRC-006"], "collection", False),
            ("eligibility-criteria-evidence-exception-and-expiry", "Eligibility criteria, evidence, exception and expiry", "Versioned criteria, evidence, evaluator, exception authority, decision scope and freshness without importing assessments.", "validation", ["SRC-006","SRC-007"], "collection", False),
        ]),
        ("decision-basis-and-effective-admission", "Decision, basis and effective admission", "The accountable admission or rejection and its relationship effect.", ["SRC-003","SRC-005","SRC-006","SRC-009"], [
            ("governing-charter-bylaw-rule-resolution-or-agreement", "Governing charter, bylaw, rule, resolution or agreement", "Typed references to the constitutive or contractual basis, authority, jurisdiction, version and precedence scope.", "authority", ["SRC-006"], "collection", True),
            ("admission-rejection-decision-conditions-and-effective-time", "Admission or rejection decision, conditions and effective time", "Decision maker, authority, reason, conditions, appeal state and distinct decision, effective and knowledge times.", "decision", ["SRC-003","SRC-005","SRC-006","SRC-009"], "object", False),
        ]),
    ]),
    ("roles-scope-and-participation-context", "Roles, scope and participation context", "Qualifies which roles are held through membership and where they apply.", "A membership can carry several role bindings, while posts, duties and activities retain independent identity and lifecycle.", ["SRC-001","SRC-002","SRC-004","SRC-007"], [
        ("role-and-post-binding", "Role and post binding", "Membership roles, scopes and optional post references with their own intervals.", ["SRC-001","SRC-002","SRC-007"], [
            ("role-concept-scope-unit-and-validity", "Role concept, scope, unit and validity", "Versioned role reference, organizational or domain scope, effective interval and profile-specific cardinality.", "relationship", ["SRC-001","SRC-002","SRC-007"], "collection", False),
            ("role-held-through-membership-versus-independent-post", "Role held through membership versus independent post", "Distinguishes a member's role binding from an independently existing post that can be vacant or held by another route.", "classification", ["SRC-001"], "object", False),
        ]),
        ("participation-affiliation-and-non-equivalence", "Participation, affiliation and non-equivalence", "References activities and adjacent relationships without conflating them with membership.", ["SRC-001","SRC-004","SRC-006"], [
            ("participation-activity-project-and-contribution-references", "Participation, activity, project and contribution references", "Time-qualified links to externally mastered activities, projects and contributions associated with membership.", "relationship", ["SRC-001","SRC-003"], "collection", False),
            ("employment-office-subscription-citizenship-licence-and-access-boundary", "Employment, office, subscription, citizenship, licence and access boundary", "Typed non-equivalence and optional relationship links that prevent inference of membership from neighboring statuses.", "interoperability", ["SRC-001","SRC-004","SRC-006"], "collection", True),
        ]),
    ]),
    ("standing-validity-and-lifecycle", "Standing, validity and lifecycle", "Represents current and historic membership condition, intervals and governed transitions.", "Standing, rights and duties may change independently, and suspension or expiry must not erase relationship identity or prior validity.", ["SRC-001","SRC-002","SRC-003","SRC-009"], [
        ("validity-state-and-observation", "Validity, state and observation", "Relationship validity intervals, asserted standing and observed freshness.", ["SRC-001","SRC-002","SRC-009"], [
            ("proposed-pending-active-suspended-ended-rejected-and-revoked-state", "Proposed, pending, active, suspended, ended, rejected and revoked state", "Profile-qualified relationship state, source, authority, valid interval, confidence and explicit unknown status.", "state", ["SRC-001","SRC-002"], "object", True),
            ("valid-decision-event-observation-and-knowledge-time", "Valid, decision, event, observation and knowledge time", "Separate time axes and intervals for relationship effect, decisions, events, observations and when assertions became known.", "temporal", ["SRC-002","SRC-003","SRC-009"], "object", True),
        ]),
        ("renewal-suspension-and-reinstatement", "Renewal, suspension and reinstatement", "Non-terminal changes and their effect on role, right and duty bindings.", ["SRC-002","SRC-003","SRC-004","SRC-006"], [
            ("renewal-extension-revalidation-and-lapse", "Renewal, extension, revalidation and lapse", "Renewal basis, decision, changed conditions, new validity, grace period and lapse effect with predecessor lineage.", "lifecycle", ["SRC-002","SRC-003","SRC-006"], "object", False),
            ("suspension-restriction-reinstatement-and-restored-standing", "Suspension, restriction, reinstatement and restored standing", "Authority, reason, due process, affected rights and duties, review date, remedy and reinstatement effect.", "process", ["SRC-003","SRC-004","SRC-006"], "object", False),
        ]),
        ("resignation-termination-and-revocation", "Resignation, termination and revocation", "Terminal or successor events, reasons, challenge and surviving history.", ["SRC-003","SRC-004","SRC-006"], [
            ("resignation-expiry-termination-removal-and-revocation-basis", "Resignation, expiry, termination, removal and revocation basis", "Initiating actor, basis, authority, notice, effective time, stated reason and distinction among voluntary, automatic and adverse endings.", "lifecycle", ["SRC-003","SRC-006"], "object", False),
            ("challenge-appeal-remedy-successor-and-tombstone", "Challenge, appeal, remedy, successor and tombstone", "Contest status, review authority, decision and remedy, reinstatement or successor identity and durable minimum tombstone.", "decision", ["SRC-003","SRC-006"], "object", False),
        ]),
    ]),
    ("terms-duties-fees-and-benefits", "Terms, duties, fees and benefits", "Links governed terms and economic or non-economic consequences without importing policy, payment or entitlement execution.", "Membership may create referenced obligations, fees and benefits, but the relationship is not itself a policy engine, subscription, account or access grant.", ["SRC-004","SRC-006"], [
        ("terms-rights-duties-and-constraints", "Terms, rights, duties and constraints", "Versioned rule and policy bindings that qualify membership.", ["SRC-004","SRC-006"], [
            ("term-version-precedence-acceptance-and-amendment", "Term version, precedence, acceptance and amendment", "Applicable term sources, version, precedence, party notice or acceptance, effective time and immutable amendment lineage.", "constraint", ["SRC-003","SRC-004","SRC-006"], "collection", True),
            ("permission-prohibition-duty-and-compliance-reference", "Permission, prohibition, duty and compliance reference", "ODRL or profile-specific policy links with assigner, assignee, target, action, constraint and external evaluation evidence.", "relationship", ["SRC-004"], "collection", False),
        ]),
        ("fee-benefit-and-entitlement-references", "Fee, benefit and entitlement references", "Economic and service consequences and their independent records.", ["SRC-004"], [
            ("fee-assessment-invoice-payment-waiver-and-arrears-reference", "Fee assessment, invoice, payment, waiver and arrears reference", "Links externally mastered fee and payment records and states why they do or do not affect membership standing.", "relationship", ["SRC-004"], "collection", False),
            ("benefit-service-resource-and-access-entitlement-reference", "Benefit, service, resource and access-entitlement reference", "Links externally mastered benefits and grants with scope, validity and governing term without treating access as membership proof.", "relationship", ["SRC-004"], "collection", False),
        ]),
    ]),
    ("evidence-privacy-dispute-and-trust", "Evidence, privacy, dispute and trust", "Maintains assertions, attestations, conflicts and privacy-safe projections.", "Membership may be private or contested; identifiers, status services and aggregate counts can leak its existence even when payload fields are hidden.", ["SRC-003","SRC-005","SRC-008"], [
        ("assertions-evidence-and-quality", "Assertions, evidence and quality", "Attributable source statements, observations and reconciliation.", ["SRC-003","SRC-005"], [
            ("member-organization-sponsor-issuer-and-authority-assertions", "Member, organization, sponsor, issuer and authority assertions", "Parallel statements with actor, role, basis, valid and knowledge time, confidence, acknowledgement and contest status.", "provenance", ["SRC-003","SRC-005"], "collection", True),
            ("evidence-attestation-freshness-quality-and-reconciliation", "Evidence, attestation, freshness, quality and reconciliation", "Source records, method, issuer, digest, status observation, freshness, conflict and explicit reconciliation result.", "quality", ["SRC-003","SRC-005"], "collection", False),
        ]),
        ("credential-directory-and-proof-projections", "Credential, directory and proof projections", "Portable and discoverable representations that remain separate from the source relationship.", ["SRC-001","SRC-005","SRC-008"], [
            ("verifiable-membership-credential-and-status-reference", "Verifiable membership credential and status reference", "Issuer, subject, schema, validity, evidence, status and terms-of-use references plus privacy and correlation profile.", "evidence", ["SRC-005","SRC-008"], "collection", False),
            ("directory-listing-badge-roster-and-minimal-verification", "Directory listing, badge, roster and minimal verification", "Purpose-specific projections, exposed fields, audience, freshness, revocation behavior and non-authoritative status.", "access", ["SRC-001","SRC-005","SRC-008"], "collection", False),
        ]),
        ("privacy-access-correction-and-retention", "Privacy, access, correction and retention", "Field-sensitive disclosure and durable lawful history.", ["SRC-003","SRC-008"], [
            ("existence-role-date-standing-and-evidence-disclosure", "Existence, role, date, standing and evidence disclosure", "Separately classifies the sensitivity, purpose, audience and masking rules for each fact and inference surface.", "privacy", ["SRC-005","SRC-008"], "object", True),
            ("access-correction-restriction-retention-legal-hold-and-deletion", "Access, correction, restriction, retention, legal hold and deletion", "Member and organization rights, steward duties, disputed fields, per-artifact retention and tombstone behavior.", "retention", ["SRC-003","SRC-008"], "object", True),
        ]),
    ]),
    ("interoperability-governance-and-agent-operations", "Interoperability, governance and agent operations", "Controls classifications, mappings, validation and safe automated action.", "Exchange must preserve qualified relation identity, roles, time, authority, disagreement and privacy rather than reducing membership to a boolean edge.", ["SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-007","SRC-009"], [
        ("classification-and-profile-projections", "Classification and profile projections", "Versioned type, role, state and reason vocabularies and mappings.", ["SRC-001","SRC-005","SRC-007"], [
            ("membership-role-standing-and-reason-concept-schemes", "Membership, role, standing and reason concept schemes", "Pinned concept identifiers, labels, scope notes, hierarchy, authority, version and mapping confidence.", "classification", ["SRC-007"], "collection", True),
            ("w3c-org-credential-policy-and-domain-profile-mappings", "W3C ORG, credential, policy and domain-profile mappings", "Source and target versions, mapping scope, transformed or omitted data, validation and non-round-trip declarations.", "interoperability", ["SRC-001","SRC-004","SRC-005"], "collection", False),
        ]),
        ("agent-control-and-safe-operation", "Agent control and safe operation", "Authorized operations, invariants, rollback and audit.", ["SRC-003","SRC-004","SRC-008","SRC-009"], [
            ("agent-operation-authority-purpose-and-confirmation-class", "Agent operation authority, purpose and confirmation class", "Classifies read, create, admit, suspend, reinstate, terminate, disclose and delete operations as autonomous, propose, confirm or forbidden.", "security", ["SRC-003","SRC-004","SRC-008"], "object", True),
            ("prewrite-postwrite-validation-conflict-and-recovery", "Pre-write and post-write validation, conflict and recovery", "Identity, party, authority, time, state-transition, policy, privacy, concurrency and rollback checks with immutable audit evidence.", "validation", ["SRC-002","SRC-003","SRC-009"], "collection", True),
        ]),
    ]),
]


def finding(row):
    fid, name, description, kind, refs, value_kind, required = row
    return {
        "id": fid,
        "name": name,
        "description": description,
        "source_refs": refs,
        "questions": [
            {"id":f"{fid}-q01", "text":f"What exact values, references, qualifiers and explicit unknowns must be recorded for {name.lower()}?", "kind":kind, "answer_data":["value or reference", "scheme and scope", "valid time", "explicit unknowns"]},
            {"id":f"{fid}-q02", "text":f"Which member, organization, authority, source and evidence establishes {name.lower()}, at what event, valid and knowledge time, and with what confidence?", "kind":"evidence", "answer_data":["asserting actor", "authority and basis", "source and evidence", "times", "confidence"]},
            {"id":f"{fid}-q03", "text":f"How may {name.lower()} be validated, challenged, corrected, superseded, retained or disclosed without erasing prior assertions or importing a neighboring model's lifecycle?", "kind":"validation", "answer_data":["validation rule", "challenge and correction route", "successor or tombstone", "access and retention effect"]},
        ],
        "data_elements":[{"id":f"{fid}-data", "name":f"{name} data", "description":f"Structured, source-qualified answer data for {name.lower()}.", "value_kind":value_kind, "cardinality":"1" if required else "0..n", "required":required, "source_refs":refs}],
        "artifacts":[{"id":f"{fid}-record", "name":f"{name} record", "description":f"Versioned evidence-bearing record for {name.lower()} with authority, event, valid and knowledge time, provenance and access marking.", "media_or_form":["logical record", "signed or attributable evidence reference"], "serial":True, "identity_strategy":f"Membership identifier plus {fid} assertion or event identifier; mutable party names, dates, directory keys and file hashes never identify the relationship.", "source_refs":refs}],
        "inline_only_rationale":None,
    }


def structure():
    return {"bundles":[{"id":bid,"name":name,"description":description,"rationale":rationale,"source_refs":refs,"layers":[{"id":lid,"name":lname,"description":ldescription,"source_refs":lrefs,"findings":[finding(item) for item in findings]} for lid,lname,ldescription,lrefs,findings in layers]} for bid,name,description,rationale,refs,layers in BUNDLES]}


FUNCTIONS = [
    ("propose-membership", "Propose membership", "Create a proposed relationship with stable identity, parties, scheme, requested type and explicit unknowns.", ["member reference","organization reference","membership profile","source"], ["proposed membership revision"], ["actor has proposal authority","duplicate check completed"], ["new relationship identity and provenance are recorded"], ["SRC-001","SRC-003"]),
    ("evaluate-eligibility", "Evaluate eligibility", "Record an attributable eligibility assessment and exceptions without importing the assessment process.", ["membership","criteria version","evidence","evaluator"], ["eligibility assertion"], ["criteria and authority are pinned"], ["result, uncertainty, expiry and evidence become queryable"], ["SRC-003","SRC-006","SRC-007"]),
    ("record-admission-decision", "Record admission decision", "Append authorized admission or rejection with conditions, effect and appeal state.", ["membership","decision reference","authority"], ["decision and lifecycle event"], ["party identities and governing basis validate"], ["relationship state changes at declared effective time without erasing proposal history"], ["SRC-003","SRC-006","SRC-009"]),
    ("bind-role", "Bind role", "Add, change or end a role binding with scope and validity while preserving membership identity.", ["membership","role reference","scope","interval"], ["role-binding revision"], ["profile permits the role and cardinality"], ["role history remains immutable and current projection is recomputed"], ["SRC-001","SRC-002","SRC-007"]),
    ("bind-terms", "Bind terms", "Attach a versioned external term or policy with precedence and applicability.", ["membership","term source","scope and precedence"], ["term binding revision"], ["term source resolves and authority is known"], ["permissions, prohibitions and duties remain externally evaluable"], ["SRC-004","SRC-006"]),
    ("renew-membership", "Renew membership", "Append renewal, extension or revalidation with changed conditions and a new interval.", ["membership","renewal basis","decision"], ["renewal event"], ["current state and renewal authority permit change"], ["predecessor validity and changed terms remain citable"], ["SRC-002","SRC-003","SRC-006"]),
    ("suspend-or-reinstate", "Suspend or reinstate", "Record temporary restriction or restored standing and its effect on roles, rights and duties.", ["membership","authority","reason","effect map"], ["suspension or reinstatement event"], ["due process and state transition validate"], ["affected bindings and review date are explicit"], ["SRC-003","SRC-004","SRC-006"]),
    ("end-membership", "End membership", "Record resignation, expiry, termination, removal or revocation with basis, notice, challenge and successor.", ["membership","ending basis","authority or member act"], ["ending event"], ["profile permits transition and actor has authority"], ["membership enters ended or contested state without cascading deletion"], ["SRC-003","SRC-006"]),
    ("reconcile-assertions", "Reconcile assertions", "Compare member, organization, issuer and authority assertions and append agreement, disagreement or unresolved state.", ["assertion set","evidence","reconciliation policy"], ["reconciliation record"], ["sources and authority scopes are known"], ["no source is silently overwritten and conflict remains queryable"], ["SRC-003","SRC-005"]),
    ("issue-membership-attestation", "Issue membership attestation", "Create or link a portable proof without treating the credential as the source relationship.", ["membership revision","issuer","credential profile"], ["digest-pinned attestation reference"], ["issuer authority, privacy and minimum disclosure validate"], ["credential status and source digest are linked and auditable"], ["SRC-005","SRC-008"]),
    ("issue-minimal-membership-view", "Issue minimal membership view", "Create a purpose-bound directory, roster or verification projection.", ["membership","requester and purpose","field policy"], ["expiring projection"], ["authority and minimum-necessary fields validate"], ["existence, role, dates, standing and evidence are disclosed independently"], ["SRC-001","SRC-005","SRC-008"]),
    ("project-membership-profile", "Project membership profile", "Transform a validated revision into W3C ORG, credential, policy or domain profile with declared loss.", ["membership revision","target profile"], ["validated exchange projection"], ["source and target versions are pinned"], ["mapping lineage, omissions and round-trip limits are recorded"], ["SRC-001","SRC-004","SRC-005","SRC-007"]),
]

def service_layers():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Dimension identity, owner, membership registrar, member-rights steward and namespace",
                "Agent, organization, role, post, activity, policy, payment, credential, access, evidence and lifecycle-event registries",
                "Master-system mappings for member, organization, membership, role binding, decision and attestation identifiers",
                "Membership-scheme, eligibility, due-process, privacy, retention, federation and autonomous-agent policies"
            ],
            "namespace_guidance": "Mint membership and assertion identifiers in the adopting Dimension namespace only when no authoritative master identifier exists; preserve agents, organizations, roles, posts, activities, payments, credentials, access grants, policies, evidence and decisions as typed references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local membership, role-binding, standing, decision, attestation, access and provenance registries"]
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by authoritative membership identifier, issuer and governing scheme, never by member-organization pair, role, directory key, badge, credential, payment, date or hash alone.",
                "Keep membership, employment, office, participation, subscription, citizenship, licence, credential, payment and access-entitlement lifecycles distinct."
            ],
            "patch_rules": [
                "Additive extensions declare target bundle, layer or finding, membership scheme and domain profile, source, authority, privacy, due-process and interoperability impact.",
                "Identity, party, role, standing or lifecycle-semantics changes require a successor version, bitemporal migration map, rollback path and continued resolution of prior records."
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when membership identity, parties, role scope, validity, authority, disagreement, access and lifecycle meaning remain intact.",
                "W3C ORG, credential, policy, directory and domain projections pin source and target versions and disclose transformed, omitted, aggregated or non-round-trippable values."
            ]
        },
        "artifact_rules": {
            "identity_priority": [
                "Authoritative membership master-system identifier qualified by issuer and membership scheme.",
                "Governed globally resolvable membership IRI with explicit member and organization references.",
                "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."
            ],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep event, decision, effective, observation, knowledge, issuance and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {membership-id}--{artifact-kind}--{assertion-or-event-id}; never use party names, a directory key, role, date, credential identifier, filename or hash alone as membership identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and profile versions, authority, valid and knowledge times, provenance, assurance, licence and access marking for every retained serial artifact."
        },
        "policies": [
            "The adopting Dimension declares who may propose, evaluate, admit, bind roles, renew, suspend, reinstate, end, attest, disclose, correct, retain and tombstone membership records.",
            "A direct memberOf edge, directory listing, badge, payment, credential or access grant is evidence or projection and never alone establishes a current qualified membership.",
            "Member and organization assertions remain separately attributable; organizational stewardship never grants unilateral authority to erase member-side evidence, lawful correction, appeal, portability or retention rights.",
            "Agents, organizations, roles, posts, activities, projects, policies, payments, subscriptions, credentials and access grants remain in their owning systems and are referenced.",
            "Automated agents may read, validate, reconcile and append low-risk observations within policy; admission, adverse restriction, revocation, wider disclosure and destructive retirement require accountable authority."
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, membership scheme, requested valid and knowledge time, evidence freshness and access scope; return the minimum permitted projection without leaking private membership existence."],
            "create": ["Create stable membership identity, member and organization references, governing scheme, source provenance and explicit unknowns before admission, role or term bindings."],
            "update": ["Append an assertion, event or successor revision with actor, authority, reason, RFC 3339 time, evidence and before-and-after validation; never overwrite a cited assertion, decision or event."],
            "delete": ["Apply charter, member-rights, legal-hold, dispute, credential-status and retention policy; prefer ended state or tombstone, preserve identity and history, and never cascade into referenced parties, roles, payments, policies or evidence."]
        },
        "roles": [
            {"name":"Dimension owner","responsibilities":["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name":"Member or member-authorized steward","responsibilities":["Attest member-side facts, exercise access and correction rights, acknowledge terms and preserve contested assertions."]},
            {"name":"Organization or group authority","responsibilities":["Own membership scheme, admission and standing authority within charter or mandate."]},
            {"name":"Membership registrar","responsibilities":["Maintain identifiers, party bindings, roles, validity, standing and lifecycle records without importing external masters."]},
            {"name":"Sponsor, nominator or approver","responsibilities":["Provide attributable proposal, sponsorship or decision evidence within delegated scope."]},
            {"name":"Appeal or review authority","responsibilities":["Review eligibility, suspension, removal, revocation and correction disputes independently where policy requires."]},
            {"name":"Privacy and access steward","responsibilities":["Apply purpose limitation, existence privacy, minimum disclosure, correction, retention and security rules."]},
            {"name":"Independent auditor","responsibilities":["Review authority, transitions, attestations, disclosures and provenance without rewriting source evidence."]}
        ],
        "access": {
            "default_rule": "Deny mutation and disclosure of membership existence, role, standing, reason or evidence unless active Dimension, membership scheme, role, purpose and field policy grant it; expose the minimum necessary projection.",
            "scopes": ["bundle","layer","finding","artifact"],
            "exceptions": ["Statutory, judicial, safeguarding or emergency access must cite authority, be purpose-bound, attributable and reviewable, and must not erase original assertions, disputes, decisions or audit evidence."],
            "audit_requirements": ["Log actor, agent, role, purpose, membership and party identities, action, policy and scheme profile, RFC 3339 timestamp with offset, affected scope, requested and effective authority, evidence and outcome."]
        },
        "agents_bootstrap": {
            "filename":"AGENTS.md",
            "required_fields":["Name","Type","Specification URL","Storage type URL","Interface URL","Processes URL"],
            "read_order":[
                "Read the nearest Dimension-owner AGENTS.md, membership mastership, scheme, member-rights, privacy, correction, retention, appeal and federation policies.",
                "Read this model AGENTS.md, pinned spec.yaml and required agent, organization, role, post, policy, payment, credential, access, evidence and decision model instructions before mutation or disclosure."
            ]
        }
    }


def coverage():
    dims = [
        ("identity", "Stable membership identity, issuer, aliases, duplicates and successor lineage are explicit."),
        ("classification and definition", "Qualified membership is separated from employment, office, participation, subscription, citizenship, licence and access."),
        ("direct relational properties", "Member, organization, scheme, type, roles, scope, validity, standing and basis are first-class; physical properties are not applicable."),
        ("recognition and observation", "Admission, authority, evidence, standing observation, confusing neighboring relations, confidence and freshness are covered."),
        ("capabilities and possible actions", "Propose, evaluate, admit, bind, renew, suspend, reinstate, end, reconcile, attest and project operations are governed."),
        ("composition", "Roles, posts, activities, policies, payments, credentials and access grants remain external typed references."),
        ("lifecycle", "Proposal, decision, admission, renewal, suspension, reinstatement, resignation, termination, revocation and tombstone preserve history."),
        ("relationships", "Member, organization, sponsor, nominator, approver, issuer, authority, role and activity relations are typed and time-qualified."),
        ("temporal", "Event, decision, valid, observation, knowledge, issuance and ingestion times remain distinct and use RFC 3339 for events."),
        ("spatial", "Geographic or logical scope is referenced when the membership scheme or role requires it; organization location remains external."),
        ("provenance", "Member, organization, sponsor, issuer and authority assertions, evidence, revision and reconciliation are attributable."),
        ("ownership and stewardship", "Bilateral provenance and power asymmetry are explicit while each referenced record retains its master system."),
        ("validation and quality", "Duplicates, scheme scope, eligibility, state transitions, stale standing, conflicting assertions and projection loss are checked."),
        ("access and privacy", "Private existence, field-level purpose, minimum disclosure, correction, restriction and audit are covered."),
        ("retention and deletion", "Per-artifact retention, legal hold, credential status, tombstone and non-cascading deletion preserve lawful evidence."),
        ("interoperability", "W3C ORG, OWL-Time, ODRL, VC, LegalRuleML and SKOS projections are versioned and loss-aware.")
    ]
    return {
        "claim":"Covers a general qualified Membership relationship from identity and admission through roles, standing, terms, lifecycle, proof, privacy and exchange, with explicit non-equivalence and neighboring-model boundaries.",
        "confidence":"medium",
        "checklist":[{"dimension":d,"status":"covered","notes":n} for d,n in dims],
        "known_omissions":[
            "Domain profiles for companies, cooperatives, associations, unions, professional bodies, standards organizations, clubs, communities, families, religious bodies, political parties and machine-agent groups require specialist review.",
            "Applications, nominations, decisions, roles, posts, activities, payments, subscriptions, credentials, access grants and policy evaluation remain in neighboring models.",
            "Certified W3C ORG, OWL-Time, ODRL, VC, LegalRuleML, directory and domain-schema crosswalks, conformance suites and privacy fixtures remain future work."
        ],
        "conflicts":[
            "A broad org:memberOf assertion may include affiliation, while this model requires a qualified scheme, parties, basis and standing and therefore cannot treat every memberOf edge as canonical Membership.",
            "A role may be held through membership or through an independently existing post or office, and those routes cannot be inferred as equivalent.",
            "Credential, payment, subscription and access status can diverge from underlying membership standing and must retain separate authority and time."
        ],
        "regional_assumptions":[
            "The GDPR provides an EU privacy profile and does not create universal global obligations.",
            "LegalRuleML supplies legal-rule metadata patterns and does not determine which charter, bylaw or authority is valid in a particular jurisdiction.",
            "W3C ORG intentionally uses broad membership semantics, so domain profiles must narrow admission, role, standing and lifecycle rules."
        ],
        "adversarial_checks":[
            "Reject employment, citizenship, office, subscription, licence, participation or access relationships represented as Membership without an explicit membership scheme and boundary decision.",
            "Reject current-standing inference from memberOf, a directory listing, payment, badge, credential or access grant alone.",
            "Reject organization-only control over member evidence, correction, appeal, portability, privacy or lawful retention.",
            "Reject private-membership leakage through predictable identifiers, directory counts, event timing, search results or credential-status endpoints.",
            "Reject mutation, attestation, disclosure or revocation beyond actor authority, scheme scope, purpose, state preconditions and confirmation class."
        ]
    }


def build():
    return {
        "schema_version":"1.0.0",
        "model": {
            "registry_id":"vr.wm-org-006",
            "model_id":"WM-ORG-006",
            "name":"Membership",
            "entry_kind":"relationship",
            "purpose":"Represent one governed, qualified relationship between a member agent and an organization or group, including admission, roles, validity, standing, terms, lifecycle, evidence and privacy without depending on storage or interface format.",
            "scope_statement":"Owns membership relationship identity, member and organization bindings, governing scheme and type, admission basis and decision effect, role bindings, validity and standing, term references, renewal, suspension, reinstatement and ending events, party assertions, proof projections, privacy and interoperability while external systems own agents, organizations, roles, posts, activities, policies, payments, subscriptions, credentials, access grants, decisions and evidence objects.",
            "in_scope":["Membership identity, member and organization or group references, membership scheme, type, classification and non-equivalence boundaries", "Application, nomination, eligibility, authority, admission, role bindings, validity, standing, renewal, suspension, reinstatement, resignation, termination and revocation", "Terms, duties, fee and benefit references, assertions, evidence, attestations, directories, privacy, retention, disputes, provenance and exchange"],
            "out_of_scope":["Employment, office-holding, citizenship, licensing, subscription, participation, affiliation and access-entitlement master lifecycles", "Member, organization, group, role, post, activity, project, policy, payment, credential, access-grant, decision and evidence master records", "Universal eligibility, admission, disciplinary, due-process, fee, privacy or retention rules, or automatic authority for an agent to admit, suspend, revoke or disclose membership"],
            "boundary_notes":[
                {"neighbor":"Employment", "distinction":"Employment is a work relationship with labour-status, term and assignment semantics; Membership is governed belonging under a membership scheme and never imports employment classification or lifecycle.", "source_refs":["SRC-001","SRC-006"]},
                {"neighbor":"Role, Post and Office", "distinction":"A role is a reusable concept, a post or office can exist independently and a membership role binding states what role a member holds through this relationship and when.", "source_refs":["SRC-001","SRC-007"]},
                {"neighbor":"Participation and Affiliation", "distinction":"Participation is involvement in an activity and affiliation can be informal or broadly asserted; canonical Membership requires a qualified scheme, parties, basis, standing and provenance.", "source_refs":["SRC-001","SRC-003"]},
                {"neighbor":"Subscription, Payment and Benefit", "distinction":"Recurring service and financial records may be conditions or consequences of membership but retain separate identity, state and execution.", "source_refs":["SRC-004"]},
                {"neighbor":"Credential and Directory Entry", "distinction":"A credential, badge, roster or listing is an issuer-controlled proof or projection whose status may diverge from the authoritative membership relationship.", "source_refs":["SRC-001","SRC-005"]},
                {"neighbor":"Access Entitlement and Policy", "distinction":"Membership may be an input to permission decisions, but policy rules, grants, evaluation and enforcement remain external and membership never guarantees access.", "source_refs":["SRC-004","SRC-008"]}
            ]
        },
        "sources":SOURCES,
        "structure":structure(),
        "functions":[{"id":r[0],"name":r[1],"description":r[2],"inputs":r[3],"outputs":r[4],"preconditions":r[5],"effects":r[6],"source_refs":r[7]} for r in FUNCTIONS],
        "composition":[
            {"target":"Agent, Organization, Group, Role, Post, Activity, Policy, Payment, Subscription, Credential, Access, Decision and Evidence models", "relation":"REFERENCE", "purpose":"Connect governed membership context while retaining external identity, authority and lifecycle.", "required":True, "source_refs":["SRC-001","SRC-003","SRC-004","SRC-005","SRC-006"]},
            {"target":"W3C Organization Ontology", "relation":"ALIGN", "purpose":"Project qualified member, organization, role and duration relationships while preserving the narrower Vercy boundary.", "required":True, "source_refs":["SRC-001"]},
            {"target":"OWL-Time and RFC 3339", "relation":"ALIGN", "purpose":"Represent intervals and relations and serialize event timestamps with seconds and explicit UTC offset.", "required":True, "source_refs":["SRC-002","SRC-009"]},
            {"target":"ODRL Information Model 2.2", "relation":"ALIGN", "purpose":"Reference membership-related permissions, prohibitions, duties and constraints without importing policy evaluation.", "required":False, "source_refs":["SRC-004"]},
            {"target":"Verifiable Credentials Data Model 2.0", "relation":"ALIGN", "purpose":"Issue portable membership attestations that remain evidence projections with separate issuer, validity and status.", "required":False, "source_refs":["SRC-005"]},
            {"target":"LegalRuleML and SKOS", "relation":"ALIGN", "purpose":"Qualify authority, jurisdiction and rule metadata and version membership, role, standing and reason concepts.", "required":False, "source_refs":["SRC-006","SRC-007"]}
        ],
        "service_layers":service_layers(),
        "coverage":coverage()
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
