import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-wrk-04"
IDS = {"WM-ACT-029", "WM-ACT-005", "WM-ACT-030", "WM-ECO-012", "WM-KNW-011", "WM-KNW-010", "WM-ACT-024", "WM-REC-010"}

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
    "WM-ACT-029": "publications/wm-act-029-program-portfolio/spec.yaml",
    "WM-ACT-005": "publications/wm-act-005-project/spec.yaml",
    "WM-ACT-030": "publications/wm-act-030-initiative/spec.yaml",
    "WM-ECO-012": "publications/wm-eco-012-budget/spec.yaml",
    "WM-KNW-011": "publications/wm-knw-011-goal-objective/spec.yaml",
    "WM-KNW-010": "publications/wm-knw-010-decision-rationale/spec.yaml",
    "WM-ACT-024": "publications/wm-act-024-decision-approval-activity/spec.yaml",
    "WM-REC-010": "publications/wm-rec-010-decision-approval-record/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-WRK-04"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-WRK-04"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-WRK-03": text_document(W / "research/enterprise/runs/em-wrk-03/local-evidence.md"),
        "EM-STR-04": text_document(W / "research/enterprise/runs/em-str-04/local-evidence.md"),
        "EM-STR-01": text_document(W / "research/enterprise/runs/em-str-01/local-evidence.md"),
        "EM-FIN-01": text_document(W / "research/enterprise/runs/em-fin-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-WRK-04 Portfolio and Investment Selection using complete WM-ACT-029 and adjacent Project, Initiative, Budget, Goal/Objective and decision-triad drafts. Candidate types are Portfolio, PortfolioComponent, SelectionCriterion, Prioritization, InvestmentAllocation and PortfolioScenario. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate Portfolio from Program, catalogue, project and initiative; component membership from component mastership; selection criteria from observed scores; ranking from intrinsic work properties; portfolio allocation from budget authority, commitment, accounting actual and component funding; scenario from approved baseline; strategic alignment from causal benefit claims. Test two portfolios referencing one initiative with different funding shares while the selected scenario preserves criteria and decision evidence. Permit unrelated components and reject automatic program semantics. Define alternative comparison, constrained capacity, double-funding prevention, product-vs-project comparison, review cadence, rebalance, effective intervals and supersession. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Portfolio boundaries; Components/membership; Criteria/scoring/prioritization; Allocation/funding; Scenarios/decisions; Governance; Time/version/rebalance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
