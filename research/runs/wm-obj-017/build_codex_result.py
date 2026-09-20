"""Subject-authored configuration research; mechanical serialization only.

Questions and fields are explicit, not expanded from a generic question cycle.
This is a proposed Vercy information contract, not an executable configurator.
"""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
STAMP = "2026-09-07T13:24:00Z"

SOURCE_ROWS = [
    ("ProductGroup", "Schema.org", "https://schema.org/ProductGroup", "development vocabulary inspected 2026-09-07", "schema", "Variant groups and explicit variation axes; projection inheritance has exceptions."),
    ("ProductModel", "Schema.org", "https://schema.org/ProductModel", "development vocabulary inspected 2026-09-07", "schema", "Base-model relationships are not transitive inheritance; model and individual remain distinct."),
    ("Consumer Product Variant in GDSN implementation guideline", "GS1", "https://ref.gs1.org/guidelines/cpv/1.1.0/", "1.1, November 2024", "standard", "CPV distinguishes consumer-relevant changes within GTIN scope; first consult GTIN management rules."),
    ("Product configuration models overview", "Microsoft", "https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-configuration-models", "page updated 2026-05-06", "first-party-doc", "Implementation evidence for typed options, constraints, calculations and selected BOM references, not universal vendor semantics."),
    ("Universal Business Language", "OASIS", "https://docs.oasis-open.org/ubl/UBL-2.4.html", "2.4 pinned edition", "standard", "Catalogue item specification and pricing updates have different purposes; use explicit lossy projections."),
    ("PROV-DM", "W3C", "https://www.w3.org/TR/prov-dm/", "Recommendation 2013-04-30", "standard", "Entity, activity, agent, derivation and attribution vocabulary for selection and release evidence."),
    ("Date and Time on the Internet: Timestamps", "IETF", "https://www.rfc-editor.org/rfc/rfc3339", "RFC 3339, July 2002", "standard", "Timestamp syntax with seconds and offset; time does not substitute for unique identity."),
    ("Guidelines for configuration management", "ISO", "https://www.iso.org/standard/70400.html", "ISO 10007:2017 public abstract only", "standard", "Configuration management scope only; licensed clauses were not inspected and conformance is not claimed."),
    ("Managed model-based 3D engineering", "ISO", "https://www.iso.org/standard/84300.html", "ISO 10303-242:2025 public scope only", "standard", "Engineering product-data exchange boundary only; no AP242 mapping or clause compliance claim."),
]

def refs(*numbers):
    return [f"SRC-{n:03d}" for n in numbers]

def field(key, kind, description, cardinality="1"):
    return key, kind, description, cardinality

def question(kind, text, *keys):
    return kind, text, list(keys)

# Two subject layers per bundle; every layer owns a focused assertion record.
ROWS = [
    ("variant-identity", "Variant identity and family", "Separate the reusable definition from the product family and its physical instances.", [
        ("family-binding", "Family and state binding", refs(1,2,8), "Bind one definition revision to a family revision; a session is not the reusable root.", [
            field("variant-id", "identifier", "Issuer-qualified master ID; immutable across non-breaking revisions."),
            field("revision", "identifier", "Immutable revision, not a mutable latest pointer."),
            field("family", "reference", "WM-OBJ-002 identity, revision, option-space revision and master locator."),
            field("state", "code", "partial, resolved, released, superseded or retired. Resolution and release are separate gates."),
        ], [
            question("identity", "Which issuer-qualified definition ID and immutable revision are being described?", "variant-id", "revision"),
            question("relationship", "Which family and option-space revision determine the meaning of these selections?", "family"),
            question("state", "Is this a partial definition, a resolved configuration or an approved reusable variant?", "state"),
            question("classification", "Can instances reference this revision without copying their serial numbers or current location into the variant?", "variant-id", "family"),
        ], "Definition and family-binding manifest"),
        ("identifier-crosswalk", "Commercial identifier scope", refs(2,3,5), "Identifiers are scoped aliases; none is assumed equivalent to every engineering definition.", [
            field("aliases", "collection", "Scheme, issuer, value, scope, validity interval and mapped revision for SKU, GTIN or CPV.", "0..n"),
            field("identity-decision", "object", "Accountable decision, consulted allocation policy version and rationale for new ID versus alias."),
            field("offer-links", "reference", "Separate seller offers and their own price and availability masters.", "0..n"),
        ], [
            question("identity", "Who issued each SKU or trade identifier and within which catalogue is it unique?", "aliases"),
            question("constraint", "If a CPV is present, which GTIN qualifies it and why does the change not require a new GTIN under the consulted rules?", "aliases", "identity-decision"),
            question("temporal", "When did each alias become applicable and can an older alias still resolve its historical definition?", "aliases"),
            question("relationship", "Which commercial offers reference this variant without turning a price change into an engineering revision?", "offer-links"),
        ], "Identifier allocation and crosswalk decision"),
    ]),
    ("feature-selections", "Feature selections and origin", "Make values interpretable before attempting configuration evaluation.", [
        ("option-domain", "Typed feature domain", refs(1,4), "Reference the family's feature dictionary and record local restrictions without overwriting its master.", [
            field("feature", "reference", "Stable feature concept and versioned dictionary reference."),
            field("domain", "object", "Primitive type, enum or range, quantity kind, unit URI, precision and valid bounds."),
            field("multiplicity", "object", "Minimum and maximum choices, conditional mandatory predicate and option group."),
            field("extensions", "collection", "Namespaced proposed option values, approval state and family compatibility assessment.", "0..n"),
        ], [
            question("definition", "Which versioned feature concept does the option name denote?", "feature"),
            question("measurement", "Which datatype, unit, precision and allowed range make the selected value comparable?", "domain"),
            question("requirement", "How many values may be chosen and when does the option become mandatory?", "multiplicity"),
            question("authority", "Who approved a new option value and does it extend the family or remain a local proposal?", "extensions"),
        ], "Feature-domain restriction record"),
        ("selection-origin", "Explicit, inherited and computed values", refs(4,6), "Store a typed value separately from its origin and absence reason; freeze released values.", [
            field("value", "object", "Typed selected value or explicit absence tag: unknown, unresolved, not-applicable or omitted. False remains a value."),
            field("origin", "code", "explicit, inherited, defaulted or computed; never infer origin from equality alone."),
            field("derivation", "object", "Source revision, actor or activity, rule version and evidence reference; non-executing."),
            field("default-impact", "collection", "Changed defaults and affected draft revisions; released values are retained.", "0..n"),
        ], [
            question("provenance", "Was the value chosen, inherited, defaulted or calculated and which source revision produced it?", "origin", "derivation"),
            question("state", "Does no recorded value mean unknown, unresolved, not applicable or genuinely omitted rather than false?", "value"),
            question("lifecycle", "Which unfinished configurations must be reevaluated after a family default changes?", "default-impact"),
            question("evidence", "Can the released selection be reconstructed without rereading a mutable default or rerunning an unpinned formula?", "value", "derivation"),
        ], "Selection provenance snapshot"),
    ]),
    ("configuration-evaluation", "Compatibility and resolution", "Keep rules, verdicts and explanations distinct; never treat feasibility as permission.", [
        ("rule-binding", "Pinned constraints and calculations", refs(4,8), "Reference the applicable rule set; evaluation occurs only in an authorized adapter.", [
            field("rules", "collection", "Rule ID, revision, language, requires/excludes/cardinality/formula/table kind, component scope and digest.", "1..n"),
            field("table-policy", "object", "Closed or open world, meaning of absent rows and effective table snapshot."),
            field("evaluation-context", "object", "Engine/profile version, supported datatypes, bounded execution settings and input digest."),
        ], [
            question("constraint", "Which requires, excludes or group-cardinality rule applies to this component and its selected features?", "rules"),
            question("exception", "Does an absent compatibility-table combination mean forbidden or merely unknown?", "table-policy"),
            question("process", "Which declared engine understands this rule language and how are cycles, unsupported types or evaluation limits reported?", "evaluation-context"),
            question("security", "Are imported expressions treated as data until an authorized bounded adapter evaluates the pinned version?", "rules", "evaluation-context"),
        ], "Constraint-set binding and evaluation profile"),
        ("resolution-report", "Completeness and satisfiability evidence", refs(4,6), "Report independent dimensions of evaluation rather than a single overloaded valid flag.", [
            field("completeness", "object", "Complete or incomplete, missing mandatory features and rule-set scope."),
            field("feasibility", "code", "satisfiable, unsatisfiable, unknown, untested or error; timeout is unknown, never success."),
            field("explanation", "object", "Conflicting inputs and rule references, alternatives and explanation completeness; no minimal-core claim without proof."),
            field("decision-context", "object", "Input/rule/engine digest, evaluation time, assumptions and separate availability and authorization decisions."),
        ], [
            question("validation", "Is the selection complete independently of whether a feasible completion exists?", "completeness", "feasibility"),
            question("exception", "Which selected values and constraints explain a contradiction, and is the explanation complete or only partial?", "explanation"),
            question("evidence", "Can another approved evaluator reproduce the verdict from the same inputs, rules and engine profile?", "decision-context"),
            question("decision", "Is an alternative merely technically feasible, actually available, or also authorized for this context?", "decision-context", "explanation"),
        ], "Configuration evaluation receipt"),
    ]),
    ("resolved-properties", "Physical definition and usable capabilities", "Describe nominal reality without inventing measurements or assuring safe operation.", [
        ("physical-signature", "Nominal physical and recognition signature", refs(1,2,9), "Proposed Vercy extension: qualified direct properties supplement product classification and context.", [
            field("physical-class", "reference", "Physical-object class and material dictionary revision; unknown if unverified."),
            field("nominal-properties", "collection", "Dimension, mass, density, hardness or material property: value, unit, tolerance, method, conditions and evidence; distinguish bulk from component values.", "0..n"),
            field("recognition", "collection", "Colour, finish, markings, geometry or distinguishing feature; sibling contrasts, ambiguity and evidence.", "0..n"),
            field("instance-required", "collection", "Location, damage, actual mass or other properties requiring a specific item observation.", "0..n"),
        ], [
            question("classification", "Which physical class and material definition apply to the configured product?", "physical-class"),
            question("measurement", "What nominal dimensions, mass, density or hardness are actually supported, in which units and under which conditions?", "nominal-properties"),
            question("quality", "Which visible features distinguish this variant from siblings and where would recognition remain ambiguous?", "recognition"),
            question("spatial", "Which location, orientation or condition claims must come from an observed instance rather than this reusable definition?", "instance-required"),
        ], "Nominal property and recognition evidence"),
        ("capability-envelope", "Functions, interfaces and use envelope", refs(2,9), "Proposed capability contract stores evidence and operating limits, not automatic actuation authority.", [
            field("capabilities", "collection", "Functional class, supported action, input/output and manufacturer-declared preconditions.", "0..n"),
            field("interfaces", "collection", "Mechanical, electrical or protocol connector and revision with mating compatibility evidence.", "0..n"),
            field("limits", "collection", "Rated load, temperature, power, fragility, handling or prohibited-use limit with conditions and source.", "0..n"),
            field("qualification", "object", "Applicable test or declaration references and unknowns; rating is not legal approval or present operability."),
        ], [
            question("definition", "What actions can this variant support and which inputs, outputs and preconditions describe them?", "capabilities"),
            question("interoperability", "Which interface revision and evidence justify a claimed compatible connection?", "interfaces"),
            question("constraint", "Within which load, temperature, power and handling limits are the declared functions supported?", "limits"),
            question("evidence", "Which qualification evidence supports those limits and which claims still require inspection of the built item?", "qualification"),
        ], "Capability and limit declaration"),
    ]),
    ("baseline-lifecycle", "Design baseline and lifecycle", "Connect definition to engineering and manufacturing masters without replacing them.", [
        ("design-effectivity", "Design, selected composition and effectivity", refs(4,8,9), "Bind exact engineering baselines and qualify where they apply.", [
            field("design", "reference", "WM-OBJ-018 design identity, revision and source master.", "0..1"),
            field("selected-bom", "reference", "WM-OBJ-019 BOM revision and selected occurrence/quantity bindings; unresolved alternatives explicit.", "0..1"),
            field("effectivity", "object", "Predicate over date, production context, market or serial range with timezone, boundary inclusion and unresolved context."),
            field("context-links", "collection", "External manufacturing, installation and sale context references; no personal-order data copied.", "0..n"),
        ], [
            question("composition", "Which engineering design and selected BOM revision define this configuration?", "design", "selected-bom"),
            question("exception", "Which component alternatives or quantities are unresolved and therefore prevent baseline release?", "selected-bom"),
            question("temporal", "Which effective dates, production contexts or serial ranges include this baseline and how are boundary instants interpreted?", "effectivity"),
            question("relationship", "Where are the manufacturing, installation and sale conditions mastered rather than duplicated?", "context-links"),
        ], "Engineering baseline and applicability binding"),
        ("release-change", "Approval, revision and replacement", refs(3,6,8), "Released revisions stay reproducible when defaults, designs or commercial mappings change.", [
            field("approval", "object", "Approver, authority, requirement and evaluation receipts, approval time and allowed release context."),
            field("change", "object", "Before/after revision, reason, impact and identity decision; optimistic expected-base digest."),
            field("replacement", "collection", "Predecessor/successor, substitution direction, fit/function evidence and restrictions; no automatic equivalence.", "0..n"),
            field("retirement", "object", "Retirement state/time/reason, remaining service obligations and durable historical resolution.", "0..1"),
        ], [
            question("authority", "Who approved this baseline and which requirements and evaluation receipts support the release?", "approval"),
            question("lifecycle", "Does the change require a new variant identity or a revision under the declared allocation policy?", "change"),
            question("constraint", "In which direction is a successor a permitted substitute and which fit or function differences prevent interchangeability?", "replacement"),
            question("retention", "After retirement, which historical revision and service obligations must remain resolvable for existing items?", "retirement"),
        ], "Release and change-control receipt"),
    ]),
    ("governed-exchange", "Governance and loss-aware exchange", "Preserve authority and meaning across Dimensions and representations.", [
        ("mastership-disclosure", "Definition mastership and confidential selections", refs(6,8), "Vercy policy: local adaptation cannot silently replace organization-owned product definition.", [
            field("mastership", "object", "Dimension, accountable owner, source location, write authority and field-level stewardship."),
            field("disclosure", "object", "Audience, purpose, confidentiality scopes and redaction policy; personal selections stay in their owning Dimension."),
            field("retention-policy", "object", "Retention period/event, hold, tombstone requirements and minimized provenance."),
        ], [
            question("ownership", "Which organization or Dimension controls the definition and who may propose versus release extensions?", "mastership"),
            question("access", "Which options expose confidential design or customer requirements and who may read each scope?", "disclosure"),
            question("privacy", "Can an agent reference organizational context without copying a private customer selection into a public variant?", "disclosure", "mastership"),
            question("retention", "What minimal tombstone preserves dependent-item interpretation after authorized deletion without retaining unnecessary personal data?", "retention-policy"),
        ], "Variant stewardship and disclosure contract"),
        ("projection-loss", "Versioned projections and semantic loss", refs(1,2,3,5,9), "Mappings require tests; a common name does not prove identity or equivalent constraint semantics.", [
            field("mapping", "object", "Source and target schema releases, field mappings, transformation version and dictionary license."),
            field("inheritance-policy", "object", "Explicit handling of ProductGroup exceptions and non-transitive ProductModel inheritance."),
            field("loss-report", "collection", "Dropped rules, units, provenance, effectivity or cardinality and reject/sidecar/manual-review disposition.", "0..n"),
            field("conformance", "object", "Fixture, validator version, round-trip result, known unsupported constructs and raw-source digest."),
        ], [
            question("interoperability", "Which source and target releases and dictionary permissions govern this projection?", "mapping"),
            question("constraint", "Does the Schema.org projection preserve grouping exceptions instead of assuming transitive feature inheritance?", "inheritance-policy"),
            question("quality", "Which rules, effectivity expressions or provenance facts cannot survive the target format and how is that loss exposed?", "loss-report"),
            question("validation", "Which round-trip fixtures demonstrate preserved variant identity and which constructs remain unverified?", "conformance"),
        ], "Projection and round-trip loss report"),
    ]),
]

def structure():
    bundles = []
    for bid, bname, bdesc, layer_rows in ROWS:
        layers = []
        for lid, name, source_refs, description, fields, questions, artifact in layer_rows:
            fid = lid + "-record"
            elements = [{"id": f"{lid}-{key}", "name": key, "description": desc, "value_kind": kind, "cardinality": card, "required": card.startswith("1"), "source_refs": source_refs} for key, kind, desc, card in fields]
            known = {x[0] for x in fields}
            assert all(set(q[2]) <= known for q in questions)
            finding = {"id": fid, "name": name + " record", "description": description, "source_refs": source_refs,
                "questions": [{"id": f"{lid}-q{n:02d}", "text": text, "kind": kind, "answer_data": [f"{lid}-{key}" for key in keys]} for n, (kind,text,keys) in enumerate(questions,1)],
                "data_elements": elements,
                "artifacts": [{"id": lid+"-evidence", "name": artifact, "description": "Versioned evidence for " + name.lower() + "; preserves source references and unresolved assertions, without copying external master data.", "media_or_form": ["application/json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative master-system record ID first; otherwise issuer-qualified UUID. Bind immutable variant revision, evidence scope and digest separately; timestamps are not sole IDs.", "source_refs": source_refs}], "inline_only_rationale": None}
            layers.append({"id": lid, "name": name, "description": description, "source_refs": source_refs, "findings": [finding]})
        bundles.append({"id": bid, "name": bname, "description": bdesc, "rationale": "Proposed Vercy decomposition: " + bdesc, "source_refs": sorted(set(r for l in layers for r in l["source_refs"])), "layers": layers})
    return {"bundles": bundles}

def services():
    return {
        "dimension": {"owner_package_requirements": ["Declare the accountable Dimension owner and authorized product-definition masters.", "Register installed specification and immutable variant revisions with namespace and digest.", "Declare federation and disclosure policy before following organizational or personal links."], "namespace_guidance": "Use owner-qualified variant IDs with stable local feature keys; a local patch keeps an explicit base revision and never impersonates the organization master.", "registry_links": ["Dimension model registry", "Variant and family registry", "Engineering baseline registry", "Change and access event registry"]},
        "canon_and_patch": {"canonicalization_rules": ["Freeze family/rule/value revisions; keep type, unit, absence and selection origin distinct.", "A released configuration requires completeness, successful feasibility evaluation and accountable release authority; none implies safety certification."], "patch_rules": ["Apply extension only to the authorized owning Dimension using an expected-base digest and namespaced IDs; reject conflicts rather than last-writer-wins.", "Validate option references, types, multiplicities, constraints, effectivity and mapping losses before release; append change evidence."], "compatibility_rules": ["Changed defaults never retroactively rewrite released values.", "Evaluate revision versus new identity under owner and adopted external identifier policy; preserve predecessor and substitution direction."]},
        "artifact_rules": {"identity_priority": ["Authoritative master-system ID", "Issuer-qualified UUID", "Dimension UUID with immutable revision and digest"], "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit UTC Z or numeric offset; preserve effective time separately from recording time.", "serial_naming_rule": "Use evidence-type plus opaque record ID and revision; never use a bare date as identity or customer data in filenames.", "integrity_rule": "Record exact-byte digest and media type; verify pinned references, refuse unsafe paths or automatic execution of imported expressions."},
        "policies": ["This specification describes data and proposed operations, not an implemented constraint solver or safety approval system.", "No public disclosure of confidential selections, design files or customer-specific configuration without authority.", "Physical properties and operating limits remain unknown until evidence is supplied; never infer hardness, density or safety from a class name."],
        "crud": {"read": ["Read AGENTS.md, owner policy, pinned specification and variant revision, then only authorized family/rule/design references."], "create": ["Reuse the active Dimension, resolve an existing family and allocate a source-qualified partial definition; record unknown values explicitly."], "update": ["Write a new revision under expected-base concurrency check; reevaluate affected constraints and retain evidence and historical baselines."], "delete": ["Retire by default. Check retention and legal holds and dependent instances before authorized deletion; preserve a minimized tombstone and historical resolution where required."]},
        "roles": [{"name": n, "responsibilities": [d]} for n,d in [
            ("Dimension owner", "Sets storage, namespace and federated access policy."), ("Product definition steward", "Owns family binding, identifier allocation and proposed changes."), ("Configuration author", "Records selections and provenance without releasing an unapproved variant."), ("Engineering reviewer", "Checks rule verdict, nominal-property evidence, composition and effectivity."), ("Release authority", "Approves immutable baseline within delegated scope."), ("Projection maintainer", "Tests mappings and reports semantic loss without changing source meaning.")]],
        "access": {"default_rule": "Deny undeclared access; public metadata does not grant access to confidential features or linked masters.", "scopes": ["bundle", "layer", "finding", "artifact"], "exceptions": ["Time-limited approved disclosure must identify audience, purpose and redacted fields; retain provenance without revealing protected values."], "audit_requirements": ["Record actor, Dimension, target revision, operation, authority decision and RFC 3339 time for changes and protected reads."]},
        "agents_bootstrap": {"filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL", "Dimension", "Variant master", "Revision", "Policy URL"], "read_order": ["AGENTS.md and current Dimension owner/access policy", "Pinned model specification and variant revision", "Family, option/rule references and evaluation receipt", "Design/effectivity, release and permitted extension process"]},
    }

def build():
    source_data = [{"id": f"SRC-{i:03d}", "title": t, "organization": o, "url": u, "version_or_date": v, "source_type": k, "primary_source": True, "authority_tier": 2 if k in ("schema","first-party-doc") else 1, "accessed_at": STAMP, "relevance": r} for i,(t,o,u,v,k,r) in enumerate(SOURCE_ROWS,1)]
    model = {"registry_id": "vr.wm-obj-017", "model_id": "WM-OBJ-017", "name": "Product Configuration / Variant", "entry_kind": "aggregate", "purpose": "Describe a reusable configured product definition between product family and physical instance, including selections, qualified direct properties, capabilities and contextual evidence.", "scope_statement": "The aggregate owns a versioned partial, resolved or released configuration definition and its selected-feature assertions, rule/evaluation bindings, nominal properties, lifecycle and mappings. The whole family option space, design, BOM, item, session, offer and order remain external masters.", "in_scope": ["Definition identity, scoped aliases, selections, rules and reproducible evaluation evidence", "Nominal physical properties, recognition features, capabilities and explicit use limits", "Design/BOM links, effectivity, release, stewardship and loss-aware interchange"], "out_of_scope": ["Owning the full product family, solver implementation, engineering design, BOM, item instance, inventory, offer, order or session lifecycle", "Automatic physical operation, certification, undisclosed customer data transfer or execution of imported rule code"], "boundary_notes": [
        {"neighbor": "WM-OBJ-002 Product Type / Catalog Item", "distinction": "Family and option-space masters are referenced by revision; this root owns one reusable selection definition.", "source_refs": refs(1,2,4)},
        {"neighbor": "WM-OBJ-001 Physical Object / Item", "distinction": "Frozen registry relation CLASSIFIES is represented by a REFERENCE with explicit classifies meaning because the research schema lacks CLASSIFIES. Nominal properties are not observed instance state.", "source_refs": refs(2,9)},
        {"neighbor": "WM-OBJ-018 Engineering Design / Product Definition and WM-OBJ-019 Component Type / Engineering BOM", "distinction": "Engineering masters retain designs and composition. This definition binds selected revisions and applicability, not their independent lifecycles.", "source_refs": refs(4,9)},
        {"neighbor": "Offer, order, inventory and configuration session", "distinction": "Pricing, availability, customer intent and temporal selections remain separately mastered context; a session may yield a reusable definition but is not that definition.", "source_refs": refs(4,5)},
    ]}
    fnrows = [
        ("resolve-family", "Resolve family and aliases", "Resolve issuer scope and family revision before accepting a candidate definition.", ["Master ID or qualified alias", "Authorized family registry"], ["Unique family and revision or explicit ambiguity"], ["Read access is granted"], ["No identifier is silently merged"], refs(1,2,3)),
        ("materialize-selection", "Materialize selected values", "Resolve inherited and computed inputs while preserving value origin and explicit unknowns.", ["Pinned family", "Typed choices and derivation evidence"], ["Revision-bound selection snapshot"], ["Options and types resolve; calculations run only in an authorized adapter"], ["Existing released values remain unchanged"], refs(4,6)),
        ("evaluate-configuration", "Evaluate feasibility and completeness", "Invoke a separately approved bounded evaluator and retain its verdict; this contract does not implement a solver.", ["Pinned rules, input digest and evaluator profile"], ["Completeness, feasibility and explanation receipt"], ["Supported language, authorized evaluator and execution limits"], ["Timeout remains unknown; feasibility grants no release permission"], refs(4)),
        ("qualify-properties", "Qualify nominal properties and capabilities", "Attach evidence-backed direct properties and limits, leaving absent measurements unknown.", ["Selection revision", "Authorized design and qualification evidence"], ["Qualified physical signature and capability envelope"], ["Units, conditions and nominal versus observed scope are explicit"], ["No inferred present operability or safety certification"], refs(2,9)),
        ("release-baseline", "Release a reusable baseline", "Record accountable approval only after completeness, feasibility, design applicability and policy checks.", ["Evaluation receipt", "Design/BOM bindings", "Approval authority"], ["Immutable released revision and change receipt"], ["No required unresolved selection; positive feasibility; release authority; expected-base match"], ["Historic revisions remain resolvable; conflicting updates are rejected"], refs(6,8)),
        ("project-variant", "Project a variant with loss report", "Translate only supported assertions into a versioned target profile.", ["Authorized variant revision", "Tested mapping and target version"], ["Projection, digest and explicit loss report"], ["License and disclosure permit export; unsupported mandatory semantics cause rejection"], ["Source remains unchanged; round-trip differences are visible"], refs(1,2,3,5,9)),
        ("retire-variant", "Retire with dependent-item continuity", "Preserve historical interpretation while honoring authorized retention and minimization rules.", ["Retirement authority", "Dependency and hold review"], ["Retired revision, successor links and minimized tombstone"], ["No prohibited deletion or unresolved hold"], ["Retired identity is never reassigned"], refs(6,8)),
    ]
    functions = [dict(zip(["id","name","description","inputs","outputs","preconditions","effects","source_refs"], r)) for r in fnrows]
    composition = [
        {"target": t, "relation": "REFERENCE", "purpose": p, "required": req, "source_refs": sr} for t,p,req,sr in [
            ("WM-OBJ-002", "Resolve the versioned family and option-space master.", True, refs(1,2,4)),
            ("WM-OBJ-001", "CLASSIFIES configured physical instances without owning their identity or state; explicit projection of frozen registry relation.", False, refs(2,9)),
            ("WM-OBJ-018", "Bind the selected engineering design revision.", False, refs(9)),
            ("WM-OBJ-019", "Bind selected BOM occurrences, quantities and alternatives.", False, refs(4,9)),
            ("Offer, order, inventory and configuration-session masters", "Resolve commercial and customer context without copying private or volatile records.", False, refs(4,5)),
        ]
    ]
    composition += [{"target": "Schema.org ProductGroup and ProductModel; GS1 CPV 1.1; OASIS UBL 2.4", "relation": "ALIGN", "purpose": "Candidate projections only; preserve identity scope and publish unsupported semantics and inheritance differences.", "required": False, "source_refs": refs(1,2,3,5)}]
    checks = [("identity", "Issuer-qualified stable ID, revision and scoped aliases"), ("lifecycle", "Partial/resolved/released/superseded/retired states and explicit release gate"), ("relationships", "Family, classifies-instance, design, BOM and commercial masters stay distinct"), ("temporal", "Effectivity separate from recorded time and alias validity"), ("provenance", "Selection origin and pinned derivation evidence"), ("ownership", "Dimension and definition mastership with delegated release authority"), ("validation", "Completeness, feasibility, source qualification and projection checks are separate"), ("access", "Confidential design and customer selection policies at all scopes"), ("interoperability", "Versioned mappings, non-transitive inheritance and loss reports"), ("physical properties", "Nominal qualified properties and recognition, no fabricated observations"), ("functions", "Capability and use limits distinct from actuation permission"), ("retention", "Retired identities, dependent items and minimized tombstones")]
    coverage = {"claim": "Source-grounded Vercy reviewable draft with twelve focused finding records; proposed design choices are not universal standard requirements, exhaustive product coverage or implemented runtime behavior.", "confidence": "medium", "checklist": [{"dimension": d, "status": "covered", "notes": n} for d,n in checks] + [{"dimension": "Operational and domain conformance", "status": "gap", "notes": "No real manufacturer fixture, solver adapter, executable instance schema or certified projection implementation is supplied."}], "known_omissions": ["Claude and Grok research both timed out after one bounded attempt. No external research result was admitted; provider waiver remains visible even if separate no-tools review succeeds.", "ISO 10007 and AP242 were inspected only through public abstracts/scopes, not licensed clauses. Dictionary, domain and normative mapping verification remains on hold.", "Sector-specific automotive, medical, food, aerospace, building-product and regulated-market profiles require specialist evidence and fixtures.", "The typed data elements are an information contract, not a complete executable instance-validation schema or constraint solver. No implementation conformance is claimed.", "Broad physical properties and capability envelopes are proposed Vercy extensions. Every real property requires its own evidence, unit, conditions and uncertainty; no universal hardness, fragility or safety ontology is supplied."], "conflicts": [], "regional_assumptions": ["Market, identifier allocation, safety and retention obligations must be resolved under applicable owner policy and jurisdiction; this draft grants no legal approval."], "adversarial_checks": ["Reject a GTIN/CPV/SKU or URL treated as universal engineering identity.", "Reject false collapsed with unknown or a changed default silently rewriting a released variant.", "Reject solver timeout as success, feasibility as release authority or technical compatibility as commercial availability.", "Reject nominal mass, hardness or capability as an observed instance property or permission to actuate.", "Reject transitive Schema.org inheritance, hidden projection loss or an unlicensed normative-conformance claim.", "Reject private customer selections copied into a public variant or a conflicting unguarded update."]}
    return {"schema_version": "1.0.0", "model": model, "sources": source_data, "structure": structure(), "functions": functions, "composition": composition, "service_layers": services(), "coverage": coverage}

if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
