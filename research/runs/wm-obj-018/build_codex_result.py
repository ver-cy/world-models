"""Serialize subject-authored engineering-definition questions and fields.

This proposes an information model. It does not implement engineering analysis,
PMI interpretation, a CAD translator or instance certification.
"""
import json
import re
from pathlib import Path

RUN = Path(__file__).resolve().parent
STAMP = "2026-09-07T13:39:00Z"

def sr(*ids):
    return [f"SRC-{i:03d}" for i in ids]

SOURCES = [
    ("Design Solution Definition", "NASA", "https://www.nasa.gov/reference/4-4-design-solution-definition/", "Systems Engineering Handbook web chapter 4.4 inspected 2026-09-07", "first-party-doc", "Design intent, alternatives, technical package and design assurance; NASA guidance is not a universal mandated workflow."),
    ("Technical Data Management", "NASA", "https://www.nasa.gov/reference/6-6-technical-data-management/", "Systems Engineering Handbook web chapter 6.6 inspected 2026-09-07", "first-party-doc", "Technical data identification, authority, access and long-term usability; proposed Vercy policies are not NASA compliance claims."),
    ("MBE PMI Validation and Conformance Testing Project", "NIST", "https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-validation", "Historical project page inspected 2026-09-07; uses historical Y14 editions", "public-authority", "Semantic versus graphical PMI, native and derivative comparison and qualified fixtures; not proof of current CAD capabilities."),
    ("Managed model-based 3D engineering", "ISO", "https://www.iso.org/standard/84300.html", "ISO 10303-242:2025 edition 4; public scope only", "standard", "Product-definition, engineering geometry, interface and lifecycle scope; no licensed clauses or conformance mapping inspected."),
    ("Requirements Interchange Format 1.2 release", "OMG", "https://www.omg.org/spec/ReqIF/1.2/About-ReqIF", "1.2, July 2016", "standard", "Pinned requirements-interchange release and normative artifacts; does not itself prove a design satisfies a requirement."),
    ("ReqIF XML schema", "OMG", "https://www.omg.org/spec/ReqIF/20110401/reqif.xsd", "20110401 schema linked by ReqIF 1.2 release", "schema", "Selected typed attribute and identifier/last-change declarations inspected; complete semantic mapping remains untested."),
    ("Configuration Management", "NASA", "https://www.nasa.gov/reference/6-5-configuration-management/", "Systems Engineering Handbook web chapter 6.5 inspected 2026-09-07", "first-party-doc", "Controlled baselines, change authority and historical status; waiver is not automatically a baseline revision."),
    ("PROV-DM", "W3C", "https://www.w3.org/TR/prov-dm/", "Recommendation 2013-04-30", "standard", "Attribution and derivation references for engineering assertions and transformations; governance is separately declared."),
    ("Date and Time on the Internet: Timestamps", "IETF", "https://www.rfc-editor.org/rfc/rfc3339", "RFC 3339, July 2002", "standard", "Seconds and explicit offset for recorded and effective times; timestamps are not unique design IDs."),
]

# Three explicit field groups answer each layer's three subject-authored
# questions. Nested object descriptions enumerate their expected semantics;
# an executable instance schema remains an explicit adoption hold.
LAYERS = [
    ("design-revision", "Controlled revision and design subject", sr(1,4,7), "Separate the informational design from physical item, commercial variant and representation file.", [
        ("identity", "object", "Issuer-qualified design ID, immutable revision, alias scope and authoritative master; never a filename alone."),
        ("design-subject", "object", "Product family WM-OBJ-002 reference, configuration scope and maturity code; physical observations remain external."),
        ("representation-authority", "object", "Authoritative representation policy, competing drawing/model assertions and designated resolver; do not silently select newest."),
    ], ["identity", "classification", "authority"]),
    ("baseline-package", "Baseline and technical data package", sr(1,2,7), "Bind a maturity-appropriate package to an immutable baseline rather than an unqualified file collection.", [
        ("package-manifest", "collection", "File or external record ID, revision, media type, exact-byte digest and role for each baseline constituent."),
        ("completeness", "object", "Maturity-specific required deliverables, presence and explicit absence reasons; no universal fixed lifecycle gate."),
        ("retrievability", "object", "Pinned dependency graph, authorized resolver, offline preservation form and retrieval checks; unresolved references visible."),
    ], ["composition", "requirement", "access"]),
    ("requirement-allocation", "Requirement allocation", sr(1,5,6), "Keep requirement content in WM-REC-006 and own only qualified realization and evidence bindings.", [
        ("allocation", "collection", "WM-REC-006 requirement identity/revision to design-element identity/revision, relation direction and allocation status."),
        ("allocation-gaps", "collection", "Unallocated requirements, ambiguous or conflicting assignments and responsible resolution role."),
        ("satisfaction-evidence", "object", "Acceptance criterion, method, evidence, scoped status and accountable reviewer; a link is not proof of satisfaction."),
    ], ["relationship", "exception", "evidence"]),
    ("design-rationale", "Alternatives and rationale", sr(1,8), "Record why this solution was selected while keeping decision authority external and identifiable.", [
        ("trade-study", "object", "Candidate alternatives, versioned criteria, weights, objective values and rejected-option rationale."),
        ("assumptions", "collection", "Assumption identity, uncertain estimate, sensitivity, evidence and conditions that could reverse preference."),
        ("selection-decision", "reference", "Decision record with responsible authority, selected revision, rationale and reconsideration trigger."),
    ], ["decision", "quality", "authority"]),
    ("architecture-interface", "Architecture and interface contract", sr(1,4), "Reference intended architecture and engineering composition without absorbing independent BOM masters.", [
        ("architecture-map", "collection", "Functional element to physical component and WM-OBJ-019 BOM occurrence/revision mappings."),
        ("interface-contract", "collection", "Endpoint IDs, protocol or connector revision, datum/reference frames, mating predicates and compatible counterpart scope."),
        ("interface-gaps", "collection", "Unresolved external endpoint, version mismatch, constraint conflict and release-blocking disposition."),
    ], ["composition", "spatial", "constraint"]),
    ("geometry-pmi", "Geometry, material and semantic PMI", sr(3,4), "Represent intended geometric meaning, not merely visual resemblance or observed dimensions.", [
        ("geometric-definition", "collection", "Stable feature IDs, geometry representation, nominal dimension/quantity, unit, datum references and tolerance expression."),
        ("pmi-status", "object", "Semantic representation versus graphical presentation, feature associations, machine interpretation capability and unsupported annotations."),
        ("material-surface", "collection", "Material specification/revision, surface condition, unit convention, test/measurement conditions and evidence; no guessed hardness or density."),
    ], ["measurement", "interoperability", "definition"]),
    ("behavior-envelope", "Functional envelope and failure assumptions", sr(1,4), "Document intended behavior and limits as qualified design assertions, not physical actuation authority.", [
        ("intended-behavior", "collection", "Functional class, supported action/mode, inputs, expected outputs and load/environment preconditions."),
        ("failure-envelope", "collection", "Failure/hazard references, prohibited use, interface limits and expected mitigation/recovery assumptions."),
        ("qualification-gap", "collection", "Unsupported capability claim, required analysis/test and explicit uncertainty; no certification from model validity."),
    ], ["definition", "constraint", "evidence"]),
    ("design-assurance", "Design verification and validation", sr(1,3,8), "Separate design requirements satisfaction from stakeholder-fit assessment and from end-product testing.", [
        ("verification", "collection", "Design-target revision, allocated requirement, method, acceptance criterion, result and evidence; not manufactured-item verification."),
        ("validation", "collection", "Stakeholder expectation, intended-use scenario, method, result, evidence and reviewer; separate from requirement verification."),
        ("assurance-scope", "object", "Exact design and analysis versions, assumptions, unresolved findings, method limitations and assurance kind."),
    ], ["validation", "quality", "provenance"]),
    ("release-effectivity", "Review, release, change and effectivity", sr(1,7,9), "Preserve controlled release and change history; scoped deviations do not silently rewrite a baseline.", [
        ("release-authority", "object", "Approver identity and delegated authority, gate criteria, open findings and release decision/time."),
        ("revision-change", "object", "Before/after identities, expected-base digest, reason, impact set and required dependent reviews."),
        ("effectivity-deviation", "object", "Explicit applicability predicate over time/context/variant/serial range, boundary semantics and separately approved deviation/waiver scope."),
    ], ["authority", "lifecycle", "temporal"]),
    ("realization-handoff", "Manufacturing and inspection handoff", sr(1,2,4,7), "Deliver intended definition and reconcile realization evidence without overwriting intent.", [
        ("handoff-content", "collection", "Build-to and inspect-to document revisions plus tooling, process and inspection-master references."),
        ("acknowledgement", "object", "Receiving organization, purpose, exact package digest, receipt time and acceptance/rejection status."),
        ("as-built-discrepancy", "collection", "Observed item/inspection reference, divergence from intended definition, approved deviation or engineering-change decision; no uncontrolled backwrite."),
    ], ["process", "event", "exception"]),
    ("technical-stewardship", "Technical stewardship, access and retention", sr(2,7,8), "Keep owner, custodian, author and consumer roles distinct across Dimensions and tool lifetimes.", [
        ("mastership", "object", "Owning Dimension, definition owner, author, custodian and controlled source references with distinct responsibilities."),
        ("disclosure", "object", "Field/artifact scope, recipient, purpose, proprietary/restricted classification and referenced authorization decision."),
        ("preservation", "object", "Retention trigger, hold, obsolete-tool migration, readable preservation form, dependency continuity and minimized tombstone."),
    ], ["ownership", "security", "retention"]),
    ("engineering-fidelity", "Transformation and engineering fidelity", sr(2,3,4,5,6), "A valid export file or matching rendering does not prove engineering-semantic equivalence.", [
        ("transformation", "object", "Native and neutral format/releases, translator version, exact source/target digest and transformation provenance."),
        ("semantic-loss", "collection", "Lost geometry, feature associations, tolerances, units, PMI or traceability with explicit severity and receiver disposition."),
        ("acceptance-fixture", "object", "Reference fixture/version, geometry and semantic comparison criteria, results, unsupported constructs and reject/sidecar policy."),
    ], ["provenance", "interoperability", "validation"]),
]

BUNDLES = [
    ("design-authority", "Design authority and baselines", "Establish exactly which intended definition and controlled package an agent is reading."),
    ("design-intent", "Intent and justification", "Explain requirement realization and the selection of this solution over alternatives."),
    ("product-definition", "Product definition and interfaces", "Describe engineering structure and machine-interpretable geometry and annotations."),
    ("behavior-assurance", "Intended behavior and assurance", "Qualify what the intended product should do and what supports that assertion."),
    ("change-realization", "Change and realization", "Control approved revisions and preserve the boundary between design intent and built reality."),
    ("technical-exchange", "Controlled technical exchange", "Preserve authority, accessibility and engineering meaning across custodians and formats."),
]

def authored_questions():
    sections = re.split(r"(?m)^### ", (RUN / "question-design.md").read_text(encoding="utf-8"))[1:]
    out = []
    for section in sections:
        title, text = section.split("\n", 1)
        text = text.split("Candidate fields:", 1)[0]
        questions = [" ".join(x.split()) for x in re.findall(r"(?ms)^- (.*?)(?=^- |\Z)", text)]
        assert len(questions) == 3 and all(q.endswith("?") for q in questions), title
        out.append((title.strip(), questions))
    assert len(out) == 12
    return out

def structure():
    authored = authored_questions()
    layers = []
    for row, (heading, questions) in zip(LAYERS, authored):
        lid, name, sources, description, fields, kinds = row
        assert heading == name
        elements = [{"id": f"{lid}-{key}", "name": key, "description": desc, "value_kind": kind, "cardinality": "0..n" if kind == "collection" else "1", "required": kind != "collection", "source_refs": sources} for key,kind,desc in fields]
        finding = {"id": lid+"-record", "name": name+" record", "description": description, "source_refs": sources,
            "questions": [{"id": f"{lid}-q{i+1:02d}", "text": text, "kind": kinds[i], "answer_data": [elements[i]["id"]]} for i,text in enumerate(questions)],
            "data_elements": elements,
            "artifacts": [{"id": lid+"-evidence", "name": name+" evidence manifest", "description": "Revision-bound supporting records for "+name.lower()+"; retain source and unresolved assertions without copying protected external masters.", "media_or_form": ["application/json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative master-system evidence ID first, then issuer-qualified UUID; bind design revision, evidence scope and digest separately. A timestamp or filename alone is not identity.", "source_refs": sources}], "inline_only_rationale": None}
        layers.append({"id":lid,"name":name,"description":description,"source_refs":sources,"findings":[finding]})
    return {"bundles": [{"id":bid,"name":name,"description":desc,"rationale":"Proposed Vercy decomposition: "+desc,"source_refs":sorted(set(s for l in layers[i*2:i*2+2] for s in l["source_refs"])),"layers":layers[i*2:i*2+2]} for i,(bid,name,desc) in enumerate(BUNDLES)]}

def services():
    return {
        "dimension": {"owner_package_requirements": ["Identify the Dimension owner and authoritative engineering-definition masters.", "Declare namespaces, model/definition registries and immutable revision bindings.", "Declare release authority, access policy, federation rules and retention obligations."], "namespace_guidance": "Use issuer-qualified design IDs and stable local feature IDs. Local extensions name their owning Dimension and pinned base; filenames are storage bindings.", "registry_links": ["Dimension model registry", "Design and baseline registry", "Requirement and interface masters", "Change and evidence registry"]},
        "canon_and_patch": {"canonicalization_rules": ["Preserve intended definition separately from observed physical-item state.", "Pin every released package member; disagreement between representations remains contested until resolved by declared authority."], "patch_rules": ["Create an authorized new revision or namespaced extension with expected-base digest; reject concurrent conflicting changes.", "Assess requirement, geometry/PMI, interface, applicability and handoff impact before release; never silently rewrite historical baselines."], "compatibility_rules": ["A new representation format does not imply a new design identity; changed engineering meaning requires explicit controlled revision.", "A scoped waiver or deviation is not automatically a baseline change; preserve exact applicability and authority."]},
        "artifact_rules": {"identity_priority": ["Authoritative master-system ID", "Governed issuer-qualified UUID", "Dimension UUID with immutable revision and digest"], "timestamp_rule": "Use RFC 3339 with seconds and UTC Z or explicit numeric offset; keep recording, approval and effectivity times distinct.", "serial_naming_rule": "Evidence type plus opaque master ID and revision; no sole date identifiers or confidential data in filenames.", "integrity_rule": "Verify exact bytes, media type and pinned dependency digests; imported CAD macros, expressions and external entities remain untrusted and are never automatically executed."},
        "policies": ["Design data validity is not manufactured-item fitness, certification, export permission or authority to actuate.", "Maintain the distinction between nominal engineering values and measured instance properties, with units and evidence.", "This information contract supplies no CAD translator, solver, PMI interpreter or executable instance conformance schema."],
        "crud": {"read": ["Read AGENTS.md and owner policy, pinned design revision and representation authority, then only authorized package and requirement references."], "create": ["Reuse the active authorized Dimension; create a partial design definition bound to family and requirement masters with explicit unknowns."], "update": ["Append a controlled revision under expected-base checks; review dependent requirements, features, interfaces and release evidence."], "delete": ["Retire first; evaluate retention/hold and dependent-item continuity before authorized deletion. Preserve minimized tombstone and required historical definition references."]},
        "roles": [{"name": n,"responsibilities":[r]} for n,r in [("Dimension owner","Defines namespace, storage, delegation and federation."),("Design authority","Owns intended definition and resolves representation conflicts."),("Design author","Creates traceable changes and records assumptions without self-granting release."),("Engineering reviewer","Checks requirement evidence, interfaces, geometry and unresolved findings."),("Release approver","Authorizes an immutable baseline within delegated scope."),("Technical data custodian","Maintains access, fixity and preservation without becoming design owner."),("Exchange maintainer","Tests translations and exposes semantic loss.")]],
        "access": {"default_rule":"Deny undeclared access; a public model specification grants no access to an organization's actual technical package.","scopes":["bundle","layer","finding","artifact"],"exceptions":["A scoped disclosure exception requires accountable authority, purpose, recipient, expiry and redaction policy; no automatic cross-Dimension copying."],"audit_requirements":["Record actor, target design revision, operation, authority decision, time and affected package digest for controlled changes and protected access."]},
        "agents_bootstrap": {"filename":"AGENTS.md","required_fields":["Name","Type","Specification URL","Storage type URL","Interface URL","Processes URL","Dimension","Design authority","Revision","Policy URL"],"read_order":["AGENTS.md and Dimension owner/access policy","Pinned specification and design revision with representation precedence","Baseline manifest and authorized requirement/interface references","Design assurance, release, change and retention process"]},
    }

def build():
    model = {"registry_id":"vr.wm-obj-018","model_id":"WM-OBJ-018","name":"Engineering Design / Product Definition","entry_kind":"aggregate","purpose":"Represent an authoritative intended product definition with controlled revisions, requirement realization, engineering meaning, assurance evidence and lifecycle context.","scope_statement":"Owns informational design identity, intended definition assertions, technical-package bindings, requirement and interface traceability, qualified nominal properties, review/release and change context. Product family, selected variant, engineering BOM, physical items, requirements and execution/test masters retain their own lifecycles.","in_scope":["Design revision, representation authority and baseline package","Requirement allocation, rationale, architecture, geometry, semantic PMI and intended behavior","Scoped design assurance, controlled change, realization handoff, stewardship and loss-aware exchange"],"out_of_scope":["Actual item location, mass, wear or present operating state; automated manufacturing or physical actuation","Owning product family, variant configuration, BOM, requirement, workflow or test execution","Claiming certified safety or standards compliance from a valid information model"],"boundary_notes":[
        {"neighbor":"WM-REC-006 Requirement","distinction":"Preserve the frozen REFERENCE realization relation. Requirement content stays mastered there; linked design satisfaction needs separate qualified evidence.","source_refs":sr(1,5,6)},
        {"neighbor":"WM-OBJ-002 Product Type / Catalog Item and WM-OBJ-017 Product Configuration / Variant","distinction":"Family and selected variant retain their identity; a variant can bind this design revision without becoming the design itself.","source_refs":sr(1,4)},
        {"neighbor":"WM-OBJ-019 Component Type / Engineering BOM","distinction":"Reference reusable composition and selected occurrences; do not replace the independent engineering BOM master.","source_refs":sr(4)},
        {"neighbor":"WM-OBJ-001 Physical Object / Item","distinction":"Design is informational intent. Nominal values and design assurance do not establish measured item condition or end-product certification.","source_refs":sr(1,3)},
        {"neighbor":"CAD file, drawing, document, analysis and inspection masters","distinction":"Files are versioned representations and evidence; independent tool, document and execution lifecycles remain referenced.","source_refs":sr(2,3,4,8)},
    ]}
    fnrows = [
        ("resolve-design-baseline","Resolve authoritative baseline","Resolve a design revision and representation authority before selecting package members.",["Qualified design ID","Authorized baseline registry"],["Pinned package or explicit ambiguity"],["Owner access policy is satisfied"],["Conflicting representations are not silently merged"],sr(2,7)),
        ("trace-requirement-realization","Trace requirement realization","Link exact requirement and design-element revisions; never infer satisfaction from link presence.",["Requirement revision","Design element","Evidence reference"],["Qualified allocation and gap report"],["Both masters are resolvable"],["Unallocated or contradictory requirements remain visible"],sr(1,5,6)),
        ("inspect-engineering-definition","Inspect intended engineering meaning","Check geometry, units, PMI associations and interface bindings through approved tooling; this contract does not implement it.",["Pinned design package","Declared engineering profile"],["Scoped inspection receipt and unsupported constructs"],["Authorized non-executing read or approved sandboxed adapter"],["Rendering equivalence is never substituted for semantic equivalence"],sr(3,4)),
        ("assess-design-assurance","Assess design assurance evidence","Distinguish requirements verification and stakeholder-fit validation of design from end-product tests.",["Design revision","Scoped analysis/review evidence"],["Qualified design assurance and open findings"],["Target revision and acceptance criteria are explicit"],["No physical certification or safety authority is inferred"],sr(1,8)),
        ("release-controlled-revision","Release controlled revision","Record approval after required completeness, review and applicability checks.",["Proposed revision","Review findings","Release authority"],["Immutable baseline and scoped release receipt"],["Expected-base digest matches; required gates pass; no blocking finding"],["Retain prior baseline and change-impact trace"],sr(1,7,9)),
        ("handoff-definition","Handoff definition and reconcile deviations","Transmit only authorized package members and record receiver acknowledgement and as-built discrepancies.",["Pinned package","Authorized recipient and purpose"],["Digest-bound receipt and discrepancy dispositions"],["Disclosure and relevant external-write authority granted"],["As-built differences never silently rewrite intended design"],sr(1,2,7)),
        ("exchange-with-loss-report","Exchange with engineering loss report","Use versioned tested mappings and reject unsupported required semantics.",["Native package","Target profile","Approved translator"],["Derivative artifact and explicit fidelity report"],["License/access permit export; reference criteria are declared"],["Keep source unchanged and preserve transformation provenance"],sr(2,3,4)),
        ("retire-and-preserve-design","Retire and preserve historical interpretation","Retain controlled history and readable dependencies under retention and hold policy.",["Retirement authority","Dependencies and retention review"],["Retired revision and preservation/tombstone record"],["No prohibited deletion or unresolved hold"],["Never reassign a retired design ID"],sr(2,7)),
    ]
    functions = [dict(zip(["id","name","description","inputs","outputs","preconditions","effects","source_refs"],r)) for r in fnrows]
    targets = [("WM-REC-006","Preserve requirement-realization traceability from frozen relation ledger.",True,sr(1,5,6)),("WM-OBJ-002","Resolve family/master classification.",True,sr(1,4)),("WM-OBJ-017","Bind configured variants to intended engineering revision.",False,sr(4)),("WM-OBJ-019","Reference engineering composition masters.",False,sr(4)),("WM-OBJ-001","Resolve as-built instance context without importing observations as design truth.",False,sr(1,4)),("Document, analysis, inspection, workflow and decision masters","Reference authoritative representations, evidence and execution rather than duplicating lifecycles.",False,sr(2,8))]
    composition = [{"target":t,"relation":"REFERENCE","purpose":p,"required":r,"source_refs":s} for t,p,r,s in targets]
    composition.append({"target":"ISO AP242 public scope and OMG ReqIF 1.2","relation":"ALIGN","purpose":"Candidate versioned engineering and requirement exchange profiles; exact mappings and normative conformance remain unverified.","required":False,"source_refs":sr(4,5,6)})
    dims=[("identity","Design ID and immutable revision distinct from representation filename"),("lifecycle","Maturity, baseline, controlled revision and retirement"),("relationships","Requirement realization and external family/variant/BOM/item masters"),("temporal","Recorded, approval and effective time separated"),("provenance","Evidence and transformation attribution"),("ownership","Design authority distinct from technical data custodian"),("validation","Design verification, stakeholder validation and product testing distinct"),("access","Scoped technical disclosure and federation"),("interoperability","Semantic PMI and versioned transformation losses"),("direct properties","Intended geometry, units, material and nominal parameters, not item observations"),("recognition","Stable features and representation associations; visual similarity insufficient"),("capabilities","Intended behavior and limits with evidence and explicit unknowns"),("retention","Readable historical baselines and dependency continuity")]
    coverage={"claim":"Source-grounded proposed Vercy engineering-definition contract, not exhaustive sector coverage, implemented runtime or certified design assurance.","confidence":"medium","checklist":[{"dimension":d,"status":"covered","notes":n} for d,n in dims]+[{"dimension":"Operational conformance","status":"gap","notes":"No executable instance schema, CAD adapter, real design fixture or normative certification is delivered."}],"known_omissions":["Claude and Grok research each timed out once at 120 seconds; no independent external research result is admitted. Visible owner-authorized provider waiver remains.","ISO AP242 support is public scope only; ASME empty catalogue description was not admitted. Licensed clauses and sector-specific PMI/metrology semantics require specialist review.","NIST fixtures are historical and selected; their old references to current standards are not 2026 version assertions or proof of present tool capability.","NASA process guidance is domain-specific. Local lifecycle, disclosure and release policy must be declared; no universal four-baseline scheme is mandated.","Nested field groups are an information contract, not a complete executable instance schema. CAD/PMI interpretation, real-product examples, target crosswalks and round-trip acceptance fixtures are deferred.","Direct intended properties and capability assertions require product-specific evidence. Actual location, measured state, manufactured-item safety and legal certification remain outside this aggregate."],"conflicts":[],"regional_assumptions":["Industry, contract and jurisdiction determine technical disclosure, retention and certification duties; this model does not grant permission or legal compliance."],"adversarial_checks":["Reject informational design treated as a physical item with actual pose or wear.","Reject requirement linkage as proof of satisfaction or design verification as end-product certification.","Reject filenames, mutable latest links or renderings as authoritative engineering identity.","Reject missing semantic PMI hidden behind a visually matching derivative.","Reject unauthorized release, silent competing-representation resolution or conflicting expected-base update.","Reject obsolete fixture editions as current standards or uninspected normative claims."]}
    sources=[{"id":f"SRC-{i:03d}","title":t,"organization":o,"url":u,"version_or_date":v,"source_type":k,"primary_source":True,"authority_tier":2 if k=="first-party-doc" else 1,"accessed_at":STAMP,"relevance":r} for i,(t,o,u,v,k,r) in enumerate(SOURCES,1)]
    return {"schema_version":"1.0.0","model":model,"sources":sources,"structure":structure(),"functions":functions,"composition":composition,"service_layers":services(),"coverage":coverage}

if __name__ == "__main__":
    (RUN/"codex.result.json").write_text(json.dumps(build(),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
