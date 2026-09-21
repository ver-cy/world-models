#!/usr/bin/env python3
"""Expose an immutable companion in the catalogue without revising its contract.

The structured view is a source-pinned navigation projection of all 18 routes
in model-spec.md. It does not add instance types, authority or validation rules.
"""
from pathlib import Path
import hashlib
import html
import importlib.util
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT.parent.parent / "ver.cy"
SLUG = "enterprise-fact-authority"
RELEASE = "/models/wm-xct-001-ownership-stewardship/profiles/enterprise-fact-authority/0.1.0/"
SOURCE = SITE / RELEASE.lstrip("/")
TARGET = ROOT / "publications" / SLUG
PUBLIC = "/models/" + SLUG + "/"
SPEC_DIGEST = "cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582"
ZIP_DIGEST = "558d5a1b459429dadb199a3ab9ec0fcef0f2c0fb32c38e0f77c50e6809ce3574"

# The grouping follows the six rows of the released structure table. Findings
# are information needs about the model, not new domain entity definitions.
GROUPS = [
    ("FA-GOV", "Governance", "Scope, accountability and operational appointments.", [
        ("FA-GOV-SCOPE", "Scope and accountable term", "FactAuthority; definition/value separation.", [1, 2, 3, 4, 9, 12]),
        ("FA-GOV-APPOINT", "Operational appointments", "StewardshipAssignment; bounded duties and valid terms.", [5]),
    ]),
    ("FA-SOURCE", "Source policy", "Source preference and submission permission are governed separately.", [
        ("FA-SOURCE-SELECT", "Selection", "MastershipRule; explicit source priority and overlap conflict.", [7]),
        ("FA-SOURCE-SUBMIT", "Submission", "WriteGrant; current rights for an authenticated source writer.", [6]),
    ]),
    ("FA-OBS", "Observation", "Source-scoped assertions, correction history and retained evidence.", [
        ("FA-OBS-ASSERT", "Assertions and corrections", "FactObservation; immutable anchors and attributed revisions.", [11, 18]),
    ]),
    ("FA-RELY", "Reliance", "Historical evaluation, disclosure, adoption and integration.", [
        ("FA-RELY-QUERY", "Historical query and projection", "Derived Evaluation and AuthorityRegister; explicit input slices and permissions.", [8, 10, 13, 14, 15, 16, 17]),
    ]),
]

NAMES = [
    "Object boundary", "Stable identity", "Definition authority", "Accountability for values",
    "Stewardship and escalation", "Current submission rights", "Source precedence",
    "Conflicting observations", "Overlapping authorities", "Historical knowledge",
    "Correction history", "Accountability transfer", "Reader disclosure",
    "Minimum startup profile", "Missing context", "Native binding and validation",
    "Legacy migration", "Evidence and veracity",
]

# Answer shapes are concise navigation aids grounded in the corresponding
# released route and field definitions. They are not new required JSON fields.
ANSWERS = [
    ["Identify whether the record concerns meaning, values or ownership.", "For FactAuthority, governs is values; consult the separate definitionAuthorityRef for meaning."],
    ["Record ID, dimension, scope, predicate, revision and previousDigest.", "For an observation, preserve subject/source; for a part, preserve its identity, kind, owner and party/source."],
    ["The external definitionAuthorityRef and the predicate whose meaning it governs.", "State whether the external reference was verified; this companion does not validate it."],
    ["The exact fact-valid time and knowledge cut, matching authority IDs/revisions/digests and accountable party.", "No applicable authority means unknown; overlapping authority IDs mean authority-contested."],
    ["Active stewardship IDs, party references, duties, effective terms and evidence.", "Return the active resolve-conflict routes; absence is a gap. Duties confer no API write right."],
    ["Authenticated caller, source, current trusted receipt time and matching WriteGrant.", "Require one active source grant naming the caller plus current scoped authority/configuration; reject missing or ambiguous permission."],
    ["Applicable MastershipRule IDs, source URIs, priorities, valid terms and authority revision pins.", "A smaller priority wins among eligible sources; priority neither proves truth nor grants writes."],
    ["Competing observation IDs/revisions/digests, tagged lexical values and retained evidence.", "Equal-priority disagreement returns contested with no selected value; preserve all competing records."],
    ["Every matching active authority ID and exact revision digest at the requested times.", "Return authority-contested; do not choose by recency or silently merge policies."],
    ["fact-valid time, knownAt, profile version, configuration digest and full known input-slice digest.", "Filter by receipt cut, then latest revision per ID, then effective interval; reject future knowledge."],
    ["Next observation revision, immediate previousDigest, currently permitted writer and correction evidence.", "Retain earlier rows and attribution; the source/subject anchors cannot change."],
    ["Guarded closure of the old term, transfer cutoff and a new term with a new identity.", "Preserve old effective coverage; a gap remains unknown and a correction is not an automatic transfer."],
    ["Current authenticated reader, admitted purpose and full-register read configuration.", "All or deny before ledger diagnostics; never disclose a selectively filtered register as complete."],
    ["A Dimension, scoped governor, explicit accountable party, governed manual source and separate WriteGrant.", "A single-source manual register is possible; missing stewardship remains visible and no HRIS is required."],
    ["Query outcome/reason, retained evidence and unranked observation IDs in the matching slice.", "Identify the missing authority, rule or source context; do not invent a preferred value."],
    ["Own runtime identity/version/specification digest, native envelope report and companion validation report.", "Validate the nested register and extensions against the trusted previous snapshot; outer V3 validation is insufficient."],
    ["Explicit legacy-party/source/scope mappings, source evidence and staged candidates.", "Do not promote owner strings automatically; refuse migration that loses history or semantics."],
    ["Exact evidence references associated with the relevant record revisions.", "Inspect provenance externally; its presence alone establishes neither veracity nor access rights."],
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

def count_label(items, singular):
    return str(len(items)) + " " + singular + ("s" if len(items) != 1 else "")

def build():
    assert digest(SOURCE / "spec.json") == SPEC_DIGEST
    assert digest(SOURCE / "enterprise-fact-authority-0.1.0.zip") == ZIP_DIGEST
    text = (SOURCE / "model-spec.md").read_text(encoding="utf-8")
    spec = json.loads((SOURCE / "spec.json").read_text(encoding="utf-8"))
    assert spec["contract"] == text
    routes = {}
    for line in text.splitlines():
        if re.match(r"\| Q\d\d \|", line):
            route, finding_question, artifact, action = [s.strip() for s in line.strip("|").split("|")]
            finding, question = [s.strip() for s in finding_question.split("→", 1)]
            i = int(route[1:])
            routes[i] = {"id": finding, "name": NAMES[i-1],
                "description": "Information needed to answer this governance question for a Company Dimension.",
                "questions": [{"id": route, "text": question, "kind": "context-question", "answer_data": ANSWERS[i-1]}],
                "artifacts": [{"id": "A-" + route, "name": artifact, "description": "Evidence or output named by the released semantic contract."}],
                "actions": [{"id": "ACT-" + route, "description": action}],
                "source": "https://ver.cy" + RELEASE + "model-spec.md#executable-invariants-and-question-routes"}
    assert set(routes) == set(range(1, 19))
    bundles = []
    seen = []
    for bid, name, description, layers in GROUPS:
        b = {"id": bid, "name": name, "description": description, "layers": []}
        for lid, lname, ldescription, numbers in layers:
            seen.extend(numbers)
            b["layers"].append({"id": lid, "name": lname, "description": ldescription, "findings": [routes[n] for n in numbers]})
        bundles.append(b)
    assert sorted(seen) == list(range(1, 19))
    view = {"format": "vercy-model-structure-view", "viewVersion": "1.0.0", "normative": False,
        "modelId": "vr.profile.enterprise-fact-authority", "modelVersion": "0.1.0", "researchContour": "EM-XCT-02",
        "sourceSpecUrl": "https://ver.cy" + RELEASE + "spec.json", "sourceSpecDigest": "sha256:" + SPEC_DIGEST,
        "sourceDocumentUrl": "https://ver.cy" + RELEASE + "model-spec.md", "sourceDocumentDigest": "sha256:" + digest(SOURCE / "model-spec.md"),
        "interpretation": "Navigation projection of the released structure table and all Q01-Q18 routes. Answer shapes are explanatory; they add no schema fields, domain types, permissions or runtime enforcement.",
        "statistics": {"bundles": 4, "layers": 6, "findings": 18, "questions": 18, "artifacts": 18},
        "structure": {"bundles": bundles}}
    TARGET.mkdir(parents=True, exist_ok=True)
    dump(TARGET / "structure.json", view)
    entry = {"registry_id": view["modelId"], "record_plane": "world-model", "model_id": "EM-XCT-02",
        "name": "Enterprise Fact Authority", "alternate_names": ["EM-XCT-02", "Fact Authority", "Enterprise data accountability", "Stewardship and source precedence"],
        "code": SLUG, "entry_kind": "companion-contract", "status": "published", "status_raw": "published-companion",
        "spec_available": True, "version": "0.1.0", "family": "Enterprise profiles", "category": "Cross-cutting context",
        "industry": ["Cross-industry"], "domain": ["Enterprise", "Data governance"],
        "tags": ["EM-XCT-02", "authority", "stewardship", "mastership", "source-priority", "write-grants"],
        "page_url": PUBLIC, "source_url": "https://ver.cy/enterprise/research/em-xct-02/",
        "spec_url": RELEASE + "spec.json", "agents_url": RELEASE + "AGENTS.md", "yaml_url": RELEASE + "spec.json",
        "spec_digest": "sha256:" + SPEC_DIGEST, "structure_url": PUBLIC + "structure.json",
        "package_url": RELEASE + "enterprise-fact-authority-0.1.0.zip",
        "installation_requirements": "Use the pinned companion schema/validator and trusted-host binding. Native outer validation alone does not enforce nested semantics. Consult the released adoption limits.",
        "nav_path": "NAV.XCT", "legacy_alias": [], "existing_spec_ref": [], "parent_ids": [], "contains_ids": [],
        "aligned_model_ids": ["vr.wm-xct-001"],
        "purpose": "EM-XCT-02: explicit fact accountability, stewardship, source precedence, write grants and retained conflicts in a Company Dimension. Bounded original companion contract.",
        "owner": "Vercy maintainers", "review_state": "reviewable-draft", "origin": "enterprise-research",
        "namespace_uri": "urn:vercy:model:vr.profile.enterprise-fact-authority", "source_version": "0.1.0",
        "source_group": "Vercy", "source_category": "Enterprise", "source_format": "JSON-compatible specification",
        "composition_role": ["companion-contract"], "default_link_type": "aligned", "priority_wave": 1,
        "priority_score": 100, "priority_confidence": "high", "priority_rationale": "Published enterprise companion with a verified immutable package.",
        "relations_ref": "", "provenance": "Scoped Claude and Grok studies/audits; source-pinned catalogue projection by Codex."}
    dump(TARGET / "catalogue-entry.json", entry)
    module_spec = importlib.util.spec_from_file_location("enterprise_page", ROOT / "tools/build_enterprise_program.py")
    module = importlib.util.module_from_spec(module_spec); module_spec.loader.exec_module(module)
    e = html.escape
    body = '<nav><a href="/models/?q=EM-XCT-02">← Catalogue</a> · <a href="/enterprise/models/em-xct-02/">Enterprise research contour</a></nav>'
    body += '<p class="v-eyebrow">EM-XCT-02 · Enterprise profiles · Published 0.1.0</p><h1>Enterprise Fact Authority</h1>'
    body += '<p class="v-lede">Describe who is accountable for a fact, who maintains it, which source is preferred, who may submit a change, and how conflicts and history are retained in your Company Dimension.</p>'
    body += '<p><strong>4 bundles · 6 layers · 18 findings · 18 questions.</strong> Open a layer to inspect its findings, questions, expected answers, artifacts and permitted actions.</p>'
    body += '<nav class="actions"><a href="#structure">Explore structure</a><a href="structure.json">Download structure JSON</a><a href="' + RELEASE + 'enterprise-fact-authority-0.1.0.zip">Download model package</a><a href="' + RELEASE + 'model-spec.md">Read semantic contract</a><a href="' + RELEASE + 'AGENTS.md">Agent instructions</a></nav>'
    body += '<section class="box"><h2>Use in a Company Dimension</h2><p>Start with one governed fact scope, an accountable party, a manual or connected source and an explicit write grant. Add stewardship, competing sources and history as needed. The downloadable package includes the schema, reference validator and three synthetic Dimension examples.</p><p>Research assurance: <strong>reviewable-draft</strong>. EM-XCT-02 remains partially covered. The host must authenticate actors and invoke the companion validator; native envelope validation alone is insufficient. <a href="' + RELEASE + 'adoption-limits.md">Read adoption limits</a>.</p></section>'
    body += '<h2 id="structure">Bundles → Layers → Findings → Questions</h2><p>Findings are information needs about the model, not additional entity types. Expected answers describe what to collect or inspect; they are not prefilled facts about your company. Listed actions confer no permission by themselves.</p>'
    body += '<div class="actions"><button type="button" id="expand">Expand all</button><button type="button" id="collapse">Collapse all</button></div>'
    for b in bundles:
        body += '<details class="model-bundle" open><summary><span class="kind">Bundle</span> <strong>' + e(b["name"]) + '</strong> <small>' + count_label(b["layers"], "layer") + '</small></summary><p>' + e(b["description"]) + '</p>'
        for layer in b["layers"]:
            body += '<details class="model-layer"><summary><span class="kind">Layer</span> <strong>' + e(layer["name"]) + '</strong> <small>' + count_label(layer["findings"], "finding") + '</small></summary><p>' + e(layer["description"]) + '</p>'
            for f in layer["findings"]:
                q = f["questions"][0]
                body += '<article class="model-finding" id="' + e(f["id"]) + '"><span class="kind">Finding · ' + e(f["id"]) + '</span><h3>' + e(f["name"]) + '</h3><h4>Question ' + e(q["id"]) + '</h4><p class="question">' + e(q["text"]) + '</p><h4>Expected answer</h4><ul>' + ''.join('<li>' + e(a) + '</li>' for a in q["answer_data"]) + '</ul><h4>Artifact / evidence</h4><p>' + e(f["artifacts"][0]["name"]) + '</p><h4>Action and unknown handling</h4><p>' + e(f["actions"][0]["description"]) + '</p></article>'
            body += '</details>'
        body += '</details>'
    body += '<section class="box"><h2>Specification and research</h2><p>This tree is a navigation view of the published contract’s structure table and all Q01–Q18 routes. The immutable 0.1.0 specification and package are unchanged. <a href="' + RELEASE + 'spec.json">Machine specification</a> · <a href="' + RELEASE + 'checksums.json">Release checksums</a> · <a href="/enterprise/research/em-xct-02/">Claude and Grok research and audits</a>.</p><p>Catalogue identity: <code>vr.profile.enterprise-fact-authority</code>. EM-XCT-02 identifies the broader research contour. The companion is associated with <a href="/models/wm-xct-001-ownership-stewardship/">WM-XCT-001</a>; it is not its subtype. Catalogue registration and this navigation view were added after the immutable release, whose historical manifest describes its earlier discovery status.</p></section>'
    body += '<style>.model-bundle,.model-layer{border:1px solid var(--v-line);border-radius:12px;padding:18px;margin:16px 0}.model-layer{margin-left:12px}.model-finding{border-top:1px solid var(--v-line);padding:20px 8px}.model-finding h3{margin:8px 0 20px}.model-finding h4{margin:18px 0 6px}.model-finding p{margin:6px 0}.kind{font-size:12px;color:var(--v-cyan);margin-right:10px}summary{cursor:pointer}summary small{margin-left:12px;color:var(--v-muted)}.question{font-size:1.15rem}button{cursor:pointer;border:1px solid var(--v-line);border-radius:8px;padding:10px 16px;background:var(--v-panel);color:var(--v-text)}code{overflow-wrap:anywhere}@media(max-width:600px){.model-layer{margin-left:0;padding:12px}.model-bundle{padding:12px}}</style>'
    body += '<script>document.getElementById("expand").onclick=()=>document.querySelectorAll(".model-bundle,.model-layer").forEach(x=>x.open=true);document.getElementById("collapse").onclick=()=>document.querySelectorAll(".model-bundle,.model-layer").forEach(x=>x.open=false);function showAnchor(){const x=document.getElementById(location.hash.slice(1));if(x){let p=x.parentElement;while(p){if(p.tagName==="DETAILS")p.open=true;p=p.parentElement;}}}window.addEventListener("hashchange",showAnchor);showAnchor();</script>'
    page = module.page("en", "Enterprise Fact Authority · EM-XCT-02", entry["purpose"], PUBLIC, body, [("en", PUBLIC)], "2026-09-21")
    (TARGET / "index.html").write_text(page, encoding="utf-8", newline="\n")
    dump(TARGET / "view-manifest.json", {"viewVersion": "1.0.0", "modelVersion": "0.1.0", "normative": False, "sourceSpecDigest": "sha256:" + SPEC_DIGEST, "files": {p.name: digest(p) for p in TARGET.iterdir() if p.is_file() and p.name != "view-manifest.json"}})
    shutil.copytree(TARGET, SITE / "models" / SLUG, dirs_exist_ok=True)
    card_path = SITE / "models/catalog-index.json"
    cards = json.loads(card_path.read_text(encoding="utf-8"))
    cards = [card for card in cards if card["id"] != view["modelId"]]
    cards.append({"id": view["modelId"], "name": entry["name"], "version": entry["version"],
        "family": entry["family"], "category": entry["category"], "domain": entry["domain"],
        "industry": entry["industry"], "tags": entry["tags"], "url": PUBLIC,
        "status": "published", "sourceUrl": entry["source_url"]})
    dump(card_path, cards)
    print(json.dumps({"page": "https://ver.cy" + PUBLIC, **view["statistics"]}))

if __name__ == "__main__":
    build()
