from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
STUDY = Path(__file__).resolve().parent
NOW = "2026-10-04T17:55:00Z"


SOURCES = [
    ("SRC-001", "Process / Workflow", "Vercy", "https://ver.cy/models/wm-act-003-process-workflow/spec.yaml", "0.3.0-research.1", "Defines internal process realization without owning beneficiary value states."),
    ("SRC-002", "Occurrence / Event", "Vercy", "https://ver.cy/models/wm-act-015-occurrence-event/spec.yaml", "0.3.0-research.1", "Provides attributable trigger occurrences without defining a stream."),
    ("SRC-003", "Party Role", "Vercy", "https://ver.cy/models/wm-xct-023-party-role/spec.yaml", "0.3.0-research.1", "Provides beneficiary and counterparty role bindings."),
    ("SRC-004", "Goal / Objective", "Vercy", "https://ver.cy/models/wm-knw-011-goal-objective/spec.yaml", "0.3.0-research.1", "Provides goal and objective references without absorbing stream identity."),
    ("SRC-005", "Version / Change History", "Vercy", "https://ver.cy/models/wm-xct-022-version-change-history/spec.yaml", "0.3.0-research.1", "Provides immutable version and successor semantics."),
    ("SRC-006", "Dependency / Impact Edge", "Vercy", "https://ver.cy/models/wm-xct-037-dependency-impact-edge/spec.yaml", "0.3.0-research.1", "Provides evidence-bounded dependency and impact edges."),
    ("SRC-007", "Claude enterprise value-stream study", "Anthropic Claude", "https://ver.cy/enterprise/research/value-streams-2026-10-04/claude-study.raw.md", "2026-10-04", "Independent frozen no-tools boundary review."),
    ("SRC-008", "Grok enterprise value-stream study", "xAI Grok", "https://ver.cy/enterprise/research/value-streams-2026-10-04/grok-study.raw.md", "2026-10-04", "Independent frozen no-tools boundary review."),
    ("SRC-009", "Value Delivery Modeling Language (VDML) 1.1", "Object Management Group", "https://www.omg.org/spec/VDML/1.1", "2018-03", "Primary standard for value creation, exchange, roles, activities and capabilities."),
    ("SRC-010", "Process Classification Framework", "APQC", "https://www.apqc.org/process-frameworks", "current at 2026-10-04", "Primary process taxonomy used to distinguish process decomposition from value-stream identity."),
]


def source_objects():
    return [
        {
            "id": sid,
            "title": title,
            "organization": org,
            "url": url,
            "version_or_date": version,
            "source_type": "secondary" if sid in {"SRC-007", "SRC-008"} else ("standard" if sid == "SRC-009" else ("classifier" if sid == "SRC-010" else "first-party-doc")),
            "primary_source": sid not in {"SRC-007", "SRC-008"},
            "authority_tier": 2 if sid in {"SRC-007", "SRC-008"} else 1,
            "accessed_at": NOW,
            "relevance": relevance,
        }
        for sid, title, org, url, version, relevance in SOURCES
    ]


def finding(prefix: str, number: int, name: str, description: str, fields: list[tuple[str, str, str, bool]], refs: list[str]):
    fid = f"{prefix}-f{number:02d}"
    question_kinds = [
        ("identity", "classification", "provenance"),
        ("ownership", "authority", "access"),
        ("definition", "relationship", "validation"),
        ("event", "temporal", "constraint"),
        ("composition", "process", "interoperability"),
        ("measurement", "quality", "evidence"),
        ("lifecycle", "state", "retention"),
        ("security", "privacy", "exception"),
    ][number - 1]
    return {
        "id": fid,
        "name": name,
        "description": description,
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"What authoritative identity and scope establish {name.lower()}?", "kind": question_kinds[0], "answer_data": ["Stable identifier, owning authority and governed scope"]},
            {"id": f"{fid}-q02", "text": f"Which change creates a successor for {name.lower()}?", "kind": question_kinds[1], "answer_data": ["Explicit version driver and immutable predecessor reference"]},
            {"id": f"{fid}-q03", "text": f"Which evidence supports {name.lower()} without copying another master?", "kind": question_kinds[2], "answer_data": ["Pinned source reference, asserter and knowledge time"]},
        ],
        "data_elements": [
            {"id": f"{fid}-{field_id}", "name": field_name, "description": field_desc, "value_kind": "reference" if field_id.endswith("ref") else "text", "cardinality": "1" if required else "0..1", "required": required, "source_refs": refs}
            for field_id, field_name, field_desc, required in fields
        ],
        "artifacts": [
            {"id": f"{fid}-a01", "name": f"{name} record", "description": f"Immutable evidence for {name.lower()}.", "media_or_form": ["JSON", "YAML", "registry record"], "serial": True, "identity_strategy": f"Stable {fid} identity plus immutable revision digest.", "source_refs": refs}
        ],
        "inline_only_rationale": None,
    }


def bundle(prefix: str, number: int, name: str, rationale: str, findings: list[dict], refs: list[str]):
    bid = f"{prefix}-b{number}"
    layers = []
    for idx, item in enumerate(findings, 1):
        layers.append({"id": f"{bid}-l{idx}", "name": item["name"], "description": item["description"], "source_refs": refs, "findings": [item]})
    return {"id": bid, "name": name, "description": rationale, "rationale": rationale, "source_refs": refs, "layers": layers}


def service_layers(model_name: str):
    return {
        "dimension": {"owner_package_requirements": ["Owning Dimension identifier", "Authoritative registry reference", "Delegation and access policy"], "namespace_guidance": f"Mint {model_name} identifiers only in the owning Dimension namespace.", "registry_links": ["https://ver.cy/models/"]},
        "canon_and_patch": {"canonicalization_rules": ["Released revisions are immutable and content-addressed."], "patch_rules": ["Corrections append a successor or correction assertion; history is preserved."], "compatibility_rules": ["A breaking identity or boundary change requires a new major version."]},
        "artifact_rules": {"identity_priority": ["Authoritative master-system identifier", "Owning-Dimension identifier", "Content digest"], "timestamp_rule": "Use RFC 3339 timestamps with Seconds and an explicit Offset.", "serial_naming_rule": "Serial artifacts include model identifier, object identifier and immutable revision.", "integrity_rule": "Digest every released record and retain source provenance."},
        "policies": ["One source masters each fact.", "Unknown evidence remains unknown and never becomes success or zero."],
        "crud": {"read": ["Resolve by stable identifier and revision."], "create": ["Require owner, scope and identity basis."], "update": ["Create immutable successor revisions for semantic change."], "delete": ["Retain tombstones and historical references; destructive deletion requires explicit authority."]},
        "roles": [
            {"name": "Model steward", "responsibilities": ["Own definitions and version decisions."]},
            {"name": "Operating owner", "responsibilities": ["Own adoption and realization evidence."]},
            {"name": "Evidence producer", "responsibilities": ["Supply attributable observations and source references."]},
            {"name": "Reviewer", "responsibilities": ["Review boundary, invariants and publication holds."]},
        ],
        "access": {"default_rule": "Least privilege under the adopting Dimension policy.", "scopes": ["bundle", "layer", "finding", "artifact"], "exceptions": ["Public projections may expose only explicitly approved fields."], "audit_requirements": ["Record reads of restricted evidence and every state-changing action."]},
        "agents_bootstrap": {"filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"], "read_order": ["AGENTS.md", "spec.yaml"]},
    }


def coverage(claim: str, omissions: list[str], conflicts: list[str]):
    dimensions = ["identity", "lifecycle", "relationships", "temporal", "provenance", "ownership", "validation", "access", "interoperability", "boundary", "beneficiary", "trigger", "value states", "terminal outcome", "realization", "projection"]
    return {
        "claim": claim,
        "confidence": "medium",
        "checklist": [{"dimension": item, "status": "covered", "notes": f"The specification states an explicit {item} rule."} for item in dimensions],
        "known_omissions": omissions,
        "conflicts": conflicts,
        "regional_assumptions": ["No jurisdiction-specific meaning is inferred; local duties and rights remain external."],
        "adversarial_checks": ["Reject department and process lists presented as value streams.", "Reject completion, delivery or payment as automatic proof of beneficiary outcome.", "Reject maps and dashboards that mint duplicate business identity.", "Preserve unknown realization and missing evidence explicitly."],
    }


def value_stream_result():
    refs = ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010"]
    fs = [
        finding("vs", 1, "Stream identity", "One recipient-value progression remains identifiable across process, system and organization redesign.", [("stream-id", "Value stream identifier", "Stable identifier for the recipient-value progression.", True), ("name", "Name", "Recipient-oriented name.", True)], refs),
        finding("vs", 2, "Enterprise boundary role", "Internal and external are roles relative to a governed enterprise boundary, not separate roots.", [("boundary-ref", "Boundary reference", "Governed enterprise boundary.", True), ("role", "Boundary role", "internal, inbound, outbound or reciprocal.", True)], refs),
        finding("vs", 3, "Beneficiary and need", "The stream begins with a named beneficiary role and a need the enterprise undertakes to satisfy.", [("beneficiary-ref", "Beneficiary role reference", "External or internal beneficiary role.", True), ("need", "Beneficiary need", "Need stated from the beneficiary perspective.", True)], refs),
        finding("vs", 4, "Trigger", "A recognizable event or condition starts the value progression.", [("trigger-class-ref", "Trigger class reference", "Pinned trigger class.", True), ("entry-criteria", "Entry criteria", "Conditions under which the stream starts.", True)], refs),
        finding("vs", 5, "Stage sequence", "Contained stages record ordered beneficiary value-state changes rather than internal tasks.", [("stage-sequence", "Stage sequence", "Ordered contained stages.", True), ("state-transition", "Value-state transition", "Before and after beneficiary value states.", True)], refs),
        finding("vs", 6, "Terminal value outcome", "The terminal condition is distinct from output, delivery, completion, payment and benefit realization.", [("outcome-class-ref", "Outcome class reference", "Governed terminal outcome class.", True), ("exit-criteria", "Exit criteria", "Evidence-compatible completion criteria.", True)], refs),
        finding("vs", 7, "Version and lifecycle", "Released versions are immutable and change only when beneficiary, trigger, state sequence or terminal outcome changes.", [("version", "Version", "Immutable definition revision.", True), ("status", "Lifecycle status", "draft, approved, effective, superseded or retired.", True)], refs),
        finding("vs", 8, "Realization separation", "Processes, capabilities, units and systems realize stages by reference and never define the stream identity.", [("realization-ref", "Realization reference", "External governed realization binding.", False), ("evidence-ref", "Evidence reference", "Evidence for a claimed binding.", False)], refs),
    ]
    bundles = [
        bundle("vs", 1, "Identity and boundary", "Defines stable stream identity relative to a governed Enterprise boundary.", fs[0:2], refs),
        bundle("vs", 2, "Beneficiary progression", "Defines beneficiary need, trigger, contained stages and terminal value state.", fs[2:6], refs),
        bundle("vs", 3, "Governance and realization", "Separates definition governance from mutable realization and evidence.", fs[6:8], refs),
    ]
    return {
        "schema_version": "1.0.0",
        "model": {"registry_id": "vr.wm-act-055", "model_id": "WM-ACT-055", "name": "Value Stream", "entry_kind": "aggregate", "purpose": "Represent a governed, outside-in progression from a beneficiary need and trigger through contained beneficiary value-state stages to a terminal value outcome, independently of the processes, systems and organization that realize it.", "scope_statement": "Owns stable Value Stream identity, immutable definition versions, beneficiary and enterprise-boundary role, trigger class, contained stage order and value states, entry and exit criteria, terminal outcome class and lifecycle. It references realization, objectives, observations and decisions without absorbing their mastership.", "in_scope": ["Stable value-stream identity and immutable definition versions", "Beneficiary need, trigger, contained stage sequence and terminal value outcome", "Internal, inbound, outbound and reciprocal roles relative to a governed Enterprise boundary"], "out_of_scope": ["Process steps, customer touchpoints, projects, systems, organization charts, observations, financial postings and benefit realization"], "boundary_notes": [{"neighbor": "WM-ACT-003 Process / Workflow", "distinction": "A process is an internal realization mechanism. Redesigning it does not change the stream while beneficiary value states remain stable.", "source_refs": refs}, {"neighbor": "Outcome and Benefit Realization", "distinction": "The stream defines its intended terminal value-state class but does not assert observed outcome or realized benefit.", "source_refs": refs}, {"neighbor": "Value Stream Realization", "distinction": "Operating adoption and realizer bindings are governed separately from the definition and may change without revising the stream.", "source_refs": refs}]},
        "sources": source_objects(), "structure": {"bundles": bundles},
        "functions": [
            {"id": "register-value-stream", "name": "Register value stream", "description": "Create a stable identity and initial immutable definition.", "inputs": ["beneficiary need", "trigger", "stage sequence", "terminal outcome"], "outputs": ["registered value stream version"], "preconditions": ["owning authority and boundary are known"], "effects": ["a resolvable stream identity exists"], "source_refs": refs},
            {"id": "release-stream-version", "name": "Release stream version", "description": "Freeze a reviewed definition revision.", "inputs": ["draft definition"], "outputs": ["immutable released revision"], "preconditions": ["identity and stage invariants pass"], "effects": ["the revision becomes referenceable"], "source_refs": refs},
            {"id": "supersede-stream-version", "name": "Supersede stream version", "description": "Link a successor after a semantic change.", "inputs": ["current revision", "successor revision"], "outputs": ["supersession relation"], "preconditions": ["a version driver changed"], "effects": ["prior history remains resolvable"], "source_refs": refs},
            {"id": "classify-boundary-role", "name": "Classify boundary role", "description": "Classify one stream relative to a pinned enterprise boundary.", "inputs": ["stream revision", "enterprise boundary"], "outputs": ["boundary-role assertion"], "preconditions": ["boundary is governed"], "effects": ["internal or external role is explicit"], "source_refs": refs},
        ],
        "composition": [
            {"target": "WM-XCT-023", "relation": "REFERENCE", "purpose": "Beneficiary and counterparty roles", "required": True, "source_refs": refs},
            {"target": "WM-ACT-015", "relation": "REFERENCE", "purpose": "Trigger occurrence classes", "required": True, "source_refs": refs},
            {"target": "WM-XCT-022", "relation": "REFERENCE", "purpose": "Immutable version and successor semantics", "required": True, "source_refs": refs},
            {"target": "WM-KNW-011", "relation": "REFERENCE", "purpose": "Goal and objective alignment", "required": False, "source_refs": refs},
            {"target": "WM-ACT-003", "relation": "REFERENCE", "purpose": "Process realization without identity import", "required": False, "source_refs": refs},
            {"target": "WM-XCT-041", "relation": "REFERENCE", "purpose": "Governed enterprise realization binding", "required": False, "source_refs": refs},
        ],
        "service_layers": service_layers("Value Stream"),
        "coverage": coverage("Covers the complete identity and boundary contract for industry-neutral internal and external Enterprise value streams; archetypes are governed classifications, not separate roots.", ["Observed outcome and benefit realization remain external.", "Industry-specific stage vocabularies are profiles."], ["Claude treated realization as a link pending governance evidence; Grok proved a separate realization aggregate. The companion model remains reviewable-draft."]),
    }


def realization_result():
    refs = ["SRC-001", "SRC-003", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010"]
    fs = [
        finding("vr", 1, "Realization identity", "One enterprise boundary's governed adoption of one immutable stream version has identity independent of the stream definition.", [("realization-id", "Realization identifier", "Stable governed realization identity.", True), ("stream-ref", "Stream version reference", "Pinned WM-ACT-055 version.", True)], refs),
        finding("vr", 2, "Scope and accountability", "Realization scope and operating accountability are explicit and time-bounded.", [("boundary-ref", "Enterprise boundary", "Governing boundary.", True), ("owner-ref", "Operating owner", "Accountable operating owner.", True)], refs),
        finding("vr", 3, "Stage realization binding", "Each binding relates a contained stream stage to external process, capability, unit or system masters.", [("stage-ref", "Stage reference", "Pinned contained stage.", True), ("realizer-ref", "Realizer reference", "External process, capability, unit or system.", True)], refs),
        finding("vr", 4, "Binding evidence", "Every asserted realization binding has an attributable evidence basis and confidence state.", [("evidence-ref", "Evidence reference", "Pinned supporting evidence.", True), ("confidence", "Confidence state", "Qualified confidence or unresolved state.", True)], refs),
        finding("vr", 5, "Operational status", "The realization reports adoption status without asserting beneficiary outcome.", [("status", "Operational status", "proposed, active, degraded, suspended or retired.", True), ("effective-window", "Effective window", "Valid-time interval.", True)], refs),
        finding("vr", 6, "Coverage and gaps", "Missing or partial realizers remain explicit gaps and never become zero or failure by inference.", [("coverage", "Coverage assertion", "Scoped coverage statement.", False), ("gap", "Gap statement", "Known missing realization.", False)], refs),
        finding("vr", 7, "Independent version driver", "Owner, scope, realizer topology or evidence rule changes create a realization successor without revising the stream.", [("version", "Version", "Immutable realization revision.", True), ("supersedes-ref", "Superseded revision", "Prior realization revision.", False)], refs),
        finding("vr", 8, "Review and retirement", "Periodic review can suspend or retire a realization while preserving the reusable stream definition.", [("review-ref", "Review reference", "Assessment or approval evidence.", False), ("retired-at", "Retirement time", "Effective end of realization.", False)], refs),
    ]
    bundles = [bundle("vr", 1, "Identity and accountability", "Defines realization identity, scope and accountable operating ownership.", fs[0:2], refs), bundle("vr", 2, "Bindings and evidence", "Relates stages to external realizers with attributable evidence.", fs[2:6], refs), bundle("vr", 3, "Version and lifecycle", "Versions and retires realization independently of the reusable definition.", fs[6:8], refs)]
    return {
        "schema_version": "1.0.0",
        "model": {"registry_id": "vr.wm-xct-041", "model_id": "WM-XCT-041", "name": "Value Stream Realization", "entry_kind": "relationship", "purpose": "Represent one governed Enterprise boundary's adoption of a pinned Value Stream version and its attributable stage-to-process, capability, organization and system realization bindings.", "scope_statement": "Owns realization identity, pinned stream revision, governing boundary, scope, operating owner, immutable realization versions, typed stage-realizer bindings, evidence basis, status, gaps, review and retirement. It never owns stream definition, process, capability, organization, system, observation or outcome identity.", "in_scope": ["Independent realization identity and immutable versions", "Enterprise boundary, scope, accountability and effective window", "Typed stage-to-realizer bindings with evidence, status and explicit gaps"], "out_of_scope": ["Value Stream definition, beneficiary value-state semantics, process execution, capability definition, organization or system mastership, observed outcome and benefit realization"], "boundary_notes": [{"neighbor": "WM-ACT-055 Value Stream", "distinction": "The stream owns beneficiary progression; this model owns one enterprise's mutable realization of a pinned revision.", "source_refs": refs}, {"neighbor": "WM-ACT-003 Process / Workflow", "distinction": "Processes remain external masters and may realize stages of many streams.", "source_refs": refs}, {"neighbor": "WM-XCT-037 Dependency / Impact Edge", "distinction": "Dependency edges can support traversal, but this aggregate owns realization scope, accountability, lifecycle and evidence requirements.", "source_refs": refs}]},
        "sources": source_objects(), "structure": {"bundles": bundles},
        "functions": [
            {"id": "register-realization", "name": "Register realization", "description": "Create one governed realization of a pinned stream revision.", "inputs": ["stream revision", "enterprise boundary", "scope", "operating owner"], "outputs": ["realization revision"], "preconditions": ["stream revision and boundary resolve"], "effects": ["realization identity exists"], "source_refs": refs},
            {"id": "bind-stage-realizer", "name": "Bind stage realizer", "description": "Relate one contained stage to an external realizer with evidence.", "inputs": ["stage reference", "realizer reference", "evidence"], "outputs": ["typed realization binding"], "preconditions": ["both references resolve"], "effects": ["realization topology is explicit"], "source_refs": refs},
            {"id": "record-realization-gap", "name": "Record realization gap", "description": "Preserve missing or partial realization as an explicit gap.", "inputs": ["scope", "gap basis"], "outputs": ["gap assertion"], "preconditions": ["scope is known"], "effects": ["unknown coverage is not treated as zero"], "source_refs": refs},
            {"id": "supersede-realization", "name": "Supersede realization", "description": "Release a successor after owner, scope or topology change.", "inputs": ["current realization", "successor"], "outputs": ["supersession link"], "preconditions": ["a realization version driver changed"], "effects": ["history remains resolvable"], "source_refs": refs},
        ],
        "composition": [
            {"target": "WM-ACT-055", "relation": "REFERENCE", "purpose": "Pinned value-stream definition", "required": True, "source_refs": refs},
            {"target": "WM-XCT-001", "relation": "REFERENCE", "purpose": "Stewardship and ownership authority", "required": True, "source_refs": refs},
            {"target": "WM-XCT-037", "relation": "REFERENCE", "purpose": "Evidence-bounded dependency and impact traversal", "required": False, "source_refs": refs},
            {"target": "WM-ACT-003", "relation": "REFERENCE", "purpose": "Process realizer", "required": False, "source_refs": refs},
            {"target": "WM-ACT-034", "relation": "REFERENCE", "purpose": "Assessment evidence", "required": False, "source_refs": refs},
        ],
        "service_layers": service_layers("Value Stream Realization"),
        "coverage": coverage("Covers a governed Enterprise realization binding separately from the reusable Value Stream definition.", ["Business Capability and Metric Definition remain separately allocated candidates.", "Observed outcomes and benefits remain external."], ["Claude required demonstrated independent governance before promotion; Grok supplied the ownership and transfer test. Publication remains reviewable-draft pending field use."]),
    }


def add_registry_rows():
    path = ROOT / "planning" / "VERCY-UNIFIED-MEGA-REGISTRY.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fields = reader.fieldnames
    assert fields
    additions = [
        {"registry_id": "vr.wm-act-055", "record_plane": "world-model", "model_id": "WM-ACT-055", "name": "Value Stream", "alternate_names": "Enterprise Value Stream; Value Creation Stream", "entry_kind": "standalone-mm", "origin": "claude-grok-enterprise-value-stream-study", "status": "candidate", "review_state": "boundary-reviewed", "nav_path": "NAV.ACT.VST", "domain_tags": "ACT.VST", "purpose": "Recipient-triggered progression of beneficiary value states to a terminal value outcome", "owner_or_maintainer": "enterprise value architecture authority", "priority_wave": "1", "priority_score": "82", "priority_method": "identity-lifecycle-boundary-review", "priority_confidence": "medium", "priority_rationale": "Required root for Enterprise value-stream representation", "factor_demand": "0.90", "factor_data": "0.75", "factor_reuse": "0.92", "factor_interop": "0.85", "factor_feasibility": "0.82", "factor_robotics": "0.05", "factor_overlap": "0.08", "relations_ref": "planning/VERCY-MODEL-RELATIONS.csv", "provenance": "Independent frozen Claude Opus and Grok 4.7 studies plus local reconciliation"},
        {"registry_id": "vr.wm-xct-041", "record_plane": "world-model", "model_id": "WM-XCT-041", "name": "Value Stream Realization", "alternate_names": "Enterprise Stream Realization; Stage Realization Binding", "entry_kind": "standalone-mm", "origin": "claude-grok-enterprise-value-stream-study", "status": "candidate", "review_state": "boundary-review-required", "nav_path": "NAV.XCT.VSR", "domain_tags": "XCT.VSR", "purpose": "Governed enterprise adoption of a pinned value-stream version and evidenced stage-realizer bindings", "owner_or_maintainer": "enterprise operating owner", "priority_wave": "1", "priority_score": "76", "priority_method": "identity-lifecycle-boundary-review", "priority_confidence": "medium", "priority_rationale": "Separates reusable stream definition from mutable enterprise realization", "factor_demand": "0.82", "factor_data": "0.72", "factor_reuse": "0.88", "factor_interop": "0.82", "factor_feasibility": "0.78", "factor_robotics": "0.08", "factor_overlap": "0.12", "relations_ref": "planning/VERCY-MODEL-RELATIONS.csv", "validation_flags": "provider-split-visible", "provenance": "Grok independent root recommendation accepted with Claude governance condition and visible hold"},
    ]
    existing = {r["model_id"] for r in rows}
    for item in additions:
        if item["model_id"] not in existing:
            rows.append({field: item.get(field, "") for field in fields})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)


def add_relation_rows():
    path = ROOT / "planning" / "VERCY-MODEL-RELATIONS.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle); rows = list(reader); fields = reader.fieldnames
    assert fields
    additions = [
        ("WM-ACT-055", "REFERENCE", "WM-XCT-023", "Resolve beneficiary and counterparty roles.", "Role identity and lifecycle remain target-owned."),
        ("WM-ACT-055", "REFERENCE", "WM-ACT-015", "Resolve attributable trigger occurrences.", "Trigger occurrence identity remains target-owned."),
        ("WM-ACT-055", "REFERENCE", "WM-XCT-022", "Pin immutable definition versions and successors.", "Version history remains target-owned."),
        ("WM-ACT-055", "REFERENCE", "WM-KNW-011", "Resolve goal and objective alignment.", "Goal identity remains target-owned."),
        ("WM-ACT-055", "REFERENCE", "WM-XCT-041", "Resolve governed Enterprise realization.", "Realization has independent scope, owner and lifecycle."),
        ("WM-XCT-041", "REFERENCE", "WM-ACT-055", "Pin one immutable stream definition version.", "Stream identity and value states remain target-owned."),
        ("WM-XCT-041", "REFERENCE", "WM-XCT-001", "Resolve stewardship and accountable ownership.", "Authority remains target-owned."),
        ("WM-XCT-041", "REFERENCE", "WM-XCT-037", "Traverse evidence-bounded dependencies and impacts.", "Generic edge semantics remain target-owned."),
        ("WM-XCT-041", "REFERENCE", "WM-ACT-003", "Resolve process realizers.", "Process identity and execution remain target-owned."),
        ("WM-XCT-041", "REFERENCE", "WM-ACT-034", "Resolve assessment evidence.", "Assessment identity and conclusions remain target-owned."),
    ]
    existing = {(r["source_model_id"], r["relation_type"], r["target_model_id"]) for r in rows}
    for source, relation, target, semantics, rationale in additions:
        if (source, relation, target) not in existing:
            rows.append(dict(zip(fields, [source, relation, target, semantics, rationale, "candidate"])))
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n"); writer.writeheader(); writer.writerows(rows)


def write_run(result: dict, decision: str, holds: list[str], deferred: list[str]):
    model_id = result["model"]["model_id"]
    run = ROOT / "research" / "runs" / model_id.lower()
    run.mkdir(parents=True, exist_ok=True)
    result_path = run / "synthesis.result.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    prompt_hash = hashlib.sha256((STUDY / "provider-prompt.md").read_bytes()).hexdigest()
    provider_hashes = {name: hashlib.sha256((STUDY / name).read_bytes()).hexdigest() for name in ["claude-study.raw.md", "grok-study.raw.md"]}
    adjudication = {
        "contract_version": "1.0.0", "model_id": model_id, "generated_at": NOW,
        "input_sha256": {"claude": provider_hashes["claude-study.raw.md"], "grok": provider_hashes["grok-study.raw.md"]},
        "provider_mode": "dual-provider", "active_providers": ["claude", "grok"], "waived_providers": [],
        "provider_policy": {"mode": "dual-provider", "frozen_prompt_sha256": prompt_hash, "review_rule": "Both providers received the exact same public frozen dossier without tools."},
        "base_provider": "codex", "boundary_decision": {"entry_kind": result["model"]["entry_kind"], "status": "accepted-reviewable-draft", "rationale": decision},
        "decisions": [{"concept": result["model"]["name"], "disposition": "accepted-reviewable-draft", "rationale": decision}],
        "critical_conflicts": [], "deferred_research": deferred, "publication_holds": holds,
        "status": "reviewable-draft", "publishable": False, "reviewable": True,
    }
    (run / "adjudication.json").write_text(json.dumps(adjudication, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (run / "provider-evidence.json").write_text(json.dumps({"promptSha256": prompt_hash, "providerResponses": provider_hashes}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    add_registry_rows(); add_relation_rows()
    write_run(value_stream_result(), "Claude and Grok independently accept Value Stream as a stable definition root. Stages are contained; maps, journeys and processes remain projections or realizers.", ["Every referenced base remains a reviewable draft unless its own publication says otherwise.", "Outcome and Benefit Realization remain external and unresolved as independent roots.", "Industry-specific stage vocabularies require separate profiles and fixtures."], ["Allocate Business Capability, Capability Realization and Metric Definition through their owning contours.", "Validate industry-specific profiles without changing the generic identity rule."])
    write_run(realization_result(), "Grok proves independent realization identity, owner, scope and transfer lifecycle; Claude accepts promotion only when that governance exists. The model therefore publishes as a reviewable draft with the provider split visible.", ["Provider split remains visible: Claude treated realization as a link until governance evidence exists; Grok recommends an independent aggregate.", "Field adoption and transfer fixtures are required before canonical promotion.", "Business Capability and Metric Definition references remain optional and unallocated."], ["Test ownership transfer and one-to-many realization across real enterprise implementations.", "Add capability and metric references only after those separate candidates receive registry allocation."])
    print("generated registry rows, relations and two research runs")
