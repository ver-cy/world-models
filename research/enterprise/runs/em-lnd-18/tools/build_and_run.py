import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-18"
IDS = {'WM-XCT-039', 'WM-XCT-037', 'WM-ORG-001', 'WM-ORG-012', 'WM-KNW-012'}

def j(p):
    return json.loads(p.read_text(encoding="utf-8-sig"))

def rows(p):
    with p.open(encoding="utf-8-sig", newline="") as h:
        return list(csv.DictReader(h))

def compact(p):
    raw = p.read_bytes()
    d = yaml.safe_load(raw.decode("utf-8-sig"))
    s = d.get("structure", {})
    bundles = []
    for b in s.get("bundles", []):
        layers = []
        for layer in b.get("layers", []):
            findings = [
                {k: v for k, v in finding.items() if k not in {"questions", "data_elements", "artifacts", "source_refs"}}
                for finding in layer.get("findings", [])
            ]
            layers.append({k: v for k, v in layer.items() if k not in {"findings", "source_refs"}} | {"findings": findings})
        bundles.append({k: v for k, v in b.items() if k not in {"layers", "source_refs"}} | {"layers": layers})
    c = {k: v for k, v in d.items() if k not in {"sources", "structure"}}
    c["sources"] = [
        {k: x.get(k) for k in ("id", "title", "organization", "version_or_date", "source_type", "primary_source", "authority_tier")}
        for x in d.get("sources", [])
    ]
    c["structure"] = {k: v for k, v in s.items() if k != "bundles"} | {"bundles": bundles}
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": c}

def text_document(p):
    raw = p.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}

registry = j(W / "research/enterprise/registry.json")
queue = j(W / "research/enterprise/queue.json")
unified = rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
specs = {
    "WM-XCT-039": "publications/wm-xct-039-managed-it-service-graph/spec.yaml",
    "WM-XCT-037": "publications/wm-xct-037-dependency-impact/spec.yaml",
    "WM-ORG-001": "publications/wm-org-001-organization/spec.yaml",
    "WM-ORG-012": "publications/wm-org-012-inter-organizational-relationship/spec.yaml",
    "WM-KNW-012": "publications/wm-knw-012-policy-rule/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LND-18"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LND-18"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-LND-01": text_document(W / "research/enterprise/runs/em-lnd-01/local-evidence.md"),
        "EM-LND-02": text_document(W / "research/enterprise/runs/em-lnd-02/local-evidence.md"),
        "EM-LND-03": text_document(W / "research/enterprise/runs/em-lnd-03/local-evidence.md"),
        "EM-LND-04": text_document(W / "research/enterprise/runs/em-lnd-04/local-evidence.md"),
        "EM-LND-05": text_document(W / "research/enterprise/runs/em-lnd-05/local-evidence.md"),
        "EM-LND-06": text_document(W / "research/enterprise/runs/em-lnd-06/local-evidence.md"),
        "EM-LND-07": text_document(W / "research/enterprise/runs/em-lnd-07/local-evidence.md"),
        "EM-LND-08": text_document(W / "research/enterprise/runs/em-lnd-08/local-evidence.md"),
        "EM-LND-09": text_document(W / "research/enterprise/runs/em-lnd-09/local-evidence.md"),
        "EM-LND-10": text_document(W / "research/enterprise/runs/em-lnd-10/local-evidence.md"),
        "EM-LND-11": text_document(W / "research/enterprise/runs/em-lnd-11/local-evidence.md"),
        "EM-LND-12": text_document(W / "research/enterprise/runs/em-lnd-12/local-evidence.md"),
        "EM-LND-13": text_document(W / "research/enterprise/runs/em-lnd-13/local-evidence.md"),
        "EM-LND-14": text_document(W / "research/enterprise/runs/em-lnd-14/local-evidence.md"),
        "EM-LND-15": text_document(W / "research/enterprise/runs/em-lnd-15/local-evidence.md"),
        "EM-LND-16": text_document(W / "research/enterprise/runs/em-lnd-16/local-evidence.md"),
        "EM-LND-17": text_document(W / "research/enterprise/runs/em-lnd-17/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-LND-18 Enterprise Landscape using all seventeen completed domain-landscape syntheses plus complete current graph-host, dependency, organization, inter-organizational relationship and policy/rule drafts. Candidate types are EnterpriseLandscape and EnterpriseViewScope. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Determine whether Enterprise Landscape is a governed composition declaration and reproducible projection, and whether Enterprise View Scope is a versioned contained policy/release rather than a subject root. It must select only domains justified by named management questions, retain domain mastership, rights, provenance, time and uncertainty across context transitions, and permit different profiles for a three-person service firm and a holding group without installing every domain. Define conflict handling when local terms, identifiers, clocks, completeness claims, access rules or edge semantics diverge. Never collapse meanings by shared labels. Define completeness relative to an explicit closed scope and declared unavailable/withheld domains; absence of a domain is not incompleteness when outside the question. Evaluate whether WM-XCT-039 can host this composition or remains managed-IT-specific; avoid a universal kernel or copy of enterprise data. Test two selective enterprise views, cross-domain traversal with conflicting meanings and a denied/withheld domain. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Enterprise declaration/scope; Selection/questions; Composition/transitions; Semantic conflicts; Completeness/absence; Rights/access; Time/provenance; Host/runtime boundary; Governance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide both candidates and identify host or policy gaps. Do not claim canonical completeness, installability or publication readiness.

DOSSIER
""" + dossier_path.read_text(encoding="utf-8")
result = subprocess.run(
    ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
    input=prompt,
    text=True,
    encoding="utf-8",
    errors="replace",
    capture_output=True,
    timeout=900,
)
if result.returncode:
    raise SystemExit((result.stderr or result.stdout or f"claude exit {result.returncode}").strip())
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(dossier_path.stat().st_size, len(result.stdout))
