import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-wrk-03"
IDS = {"WM-ACT-029", "WM-ACT-005", "WM-ACT-008", "WM-ACT-030", "WM-KNW-011", "WM-ACT-034", "WM-ORG-016"}

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
    "WM-ACT-008": "publications/wm-act-008-plan-schedule/spec.yaml",
    "WM-ACT-030": "publications/wm-act-030-initiative/spec.yaml",
    "WM-KNW-011": "publications/wm-knw-011-goal-objective/spec.yaml",
    "WM-ACT-034": "publications/wm-act-034-assessment-evaluation/spec.yaml",
    "WM-ORG-016": "publications/wm-org-016-work-assignment/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-WRK-03"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-WRK-03"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-STR-02": text_document(W / "research/enterprise/runs/em-str-02/local-evidence.md"),
        "EM-WRK-02": text_document(W / "research/enterprise/runs/em-wrk-02/local-evidence.md"),
        "EM-LND-05": text_document(W / "research/enterprise/runs/em-lnd-05/local-evidence.md"),
        "EM-STR-04": text_document(W / "research/enterprise/runs/em-str-04/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-WRK-03 Program and Benefits Management using complete WM-ACT-029 and adjacent Project, Plan/Schedule, Initiative, Goal/Objective, Assessment and Work Assignment drafts. Candidate types are Program, ProgramComponent, Tranche, BenefitDependency and TransitionPlan. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate Program from Portfolio, Project, Initiative and an arbitrary container; component membership from component mastership; project closure from outcome and benefit realization; outputs from outcomes and benefits; causal hypothesis/dependency/attribution; tranche from project phase; transition plan from operation and acceptance; program governance from project facts. Test a program with two projects plus operational transition where one project closes before the joint benefit is achieved. Reject an arbitrary folder of unrelated projects. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Program vs Portfolio; Components/membership; Tranches/transition; Benefits/dependencies/attribution; Governance/decision rights; Time/version/closure; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
