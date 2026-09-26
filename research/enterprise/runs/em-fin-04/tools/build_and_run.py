import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-fin-04"
IDS = {"WM-ECO-018", "WM-ECO-015", "WM-ECO-016", "WM-ECO-017", "WM-ORG-001", "WM-ORG-012", "WM-ECO-038", "WM-KNW-012"}

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
    "WM-ECO-018": "publications/wm-eco-018-financial-statement/spec.yaml",
    "WM-ECO-015": "publications/wm-eco-015-financial-account/spec.yaml",
    "WM-ECO-016": "publications/wm-eco-016-financial-transaction-journal-entry/spec.yaml",
    "WM-ECO-017": "publications/wm-eco-017-financial-position-balance/spec.yaml",
    "WM-ORG-001": "publications/wm-org-001-organization/spec.yaml",
    "WM-ORG-012": "publications/wm-org-012-inter-organizational-relationship/spec.yaml",
    "WM-ECO-038": "publications/wm-eco-038-equity-security-holding/spec.yaml",
    "WM-KNW-012": "publications/wm-knw-012-policy-rule/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-FIN-04"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-FIN-04"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-FIN-02": text_document(W / "research/enterprise/runs/em-fin-02/local-evidence.md"),
        "EM-ORG-03": text_document(W / "research/enterprise/runs/em-org-03/local-evidence.md"),
        "EM-ORG-01": text_document(W / "research/enterprise/runs/em-org-01/local-evidence.md"),
        "EM-DAT-06": text_document(W / "research/enterprise/runs/em-dat-06/local-evidence.md"),
        "EM-FAC-02": text_document(W / "research/enterprise/runs/em-fac-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-FIN-04 Financial Reporting and Consolidation using complete WM-ECO-018 Financial Statement plus adjacent Account, Journal Entry, Position/Balance, Organization, Inter-organizational Relationship, Equity Holding and Policy/Rule drafts and prior boundary work. Candidate types are FinancialStatement, ConsolidationScope, ConsolidationRun and EliminationEntry. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate statement/report issue from consolidation scope, run, transformation, elimination and source ledgers. Distinguish legal/accounting control from common ownership, management perimeter from statutory reporting perimeter, ledger facts from consolidation adjustments, source postings from elimination results, current event time from as-of knowledge time, and original issue from restatement. Require pinned ledgers/books, periods, chart/policy/framework/taxonomy/currency/rate versions, entity scope and control basis, ownership percentages, transformation mappings, intercompany matching, pair evidence, run configuration, cutoff, late adjustments and authorization. Test two ledgers, a scope change and elimination of an intercompany sale; preserve reproducibility at prior knowledge time. Reject inclusion based only on common owners. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Statement/scope/run; Perimeter/control; Source ledgers/transformation; Elimination entry; Currency/time/knowledge; Restatement/publication; Governance/assurance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
