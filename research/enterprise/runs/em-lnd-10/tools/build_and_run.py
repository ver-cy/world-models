import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-10"
IDS = {"WM-ECO-012", "WM-ECO-015", "WM-ECO-016", "WM-ECO-017", "WM-ECO-018", "WM-ECO-038", "WM-MAT-008", "WM-ORG-012"}

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
    "WM-ECO-012": "publications/wm-eco-012-budget/spec.yaml",
    "WM-ECO-015": "publications/wm-eco-015-financial-account/spec.yaml",
    "WM-ECO-016": "publications/wm-eco-016-financial-transaction-journal-entry/spec.yaml",
    "WM-ECO-017": "publications/wm-eco-017-financial-position-balance/spec.yaml",
    "WM-ECO-018": "publications/wm-eco-018-financial-statement/spec.yaml",
    "WM-ECO-038": "publications/wm-eco-038-equity-security-holding/spec.yaml",
    "WM-MAT-008": "publications/wm-mat-008-observation-measurement-record/spec.yaml",
    "WM-ORG-012": "publications/wm-org-012-inter-organizational-relationship/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LND-10"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LND-10"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-FIN-01": text_document(W / "research/enterprise/runs/em-fin-01/local-evidence.md"),
        "EM-FIN-02": text_document(W / "research/enterprise/runs/em-fin-02/local-evidence.md"),
        "EM-FIN-04": text_document(W / "research/enterprise/runs/em-fin-04/local-evidence.md"),
        "EM-FIN-05": text_document(W / "research/enterprise/runs/em-fin-05/local-evidence.md"),
        "EM-LND-08": text_document(W / "research/enterprise/runs/em-lnd-08/local-evidence.md"),
        "EM-LND-12": text_document(W / "research/enterprise/runs/em-lnd-12/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-LND-10 Financial Landscape using complete WM-ECO-012 Budget, WM-ECO-016 Financial Transaction / Journal Entry, WM-ECO-018 Financial Statement plus Account, Position/Balance, Equity Holding, Observation and Organizational Relationship drafts and prior finance/landscape work. Candidate types are FinanceLandscape and FinanceViewPolicy. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Determine whether the landscape is a governed declaration/profile and reproducible projection over existing masters, whether FinanceViewPolicy is a pinned policy/rule set rather than a new aggregate, and which missing roots from prior work are required (Responsibility Centre, Consolidation Scope/Run, Chart of Accounts/Mapping, Metric Definition, Cost Allocation). Separate plans, actual postings, balances, statement issues, responsibility ownership, consolidation perimeters, transformations, eliminations, currency translation, allocation, observation and derived view rows. Require explicit book, ledger revision, period, scenario, version, organization/responsibility scope, accounting framework, chart/mapping, consolidation scope/run, currency/rate set, transformation, elimination, allocation, knowledge cut, comparability classification and unresolved residual. Prevent arithmetic across currencies, periods, books, bases or scenarios without an authorized transformation. Preserve source facts and disclose unmatched/unallocated residuals. Test two books and three currencies with plan/actual comparison, one intercompany elimination and one unallocated cost; block an unjustified total and produce a reproducible exception-aware view. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Landscape/view policy; Plans/actuals; Books/accounts/responsibility; Consolidation/elimination; Currency/period/comparability; Allocation/residuals; Projection/time/provenance; Governance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide both candidate types and identify dependency gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
