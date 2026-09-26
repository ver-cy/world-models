import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-wrk-01"
IDS = {"WM-ACT-006", "WM-ACT-003", "WM-ACT-005", "WM-ACT-029", "WM-REC-006"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def full_spec(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": yaml.safe_load(raw.decode("utf-8-sig"))}


def text_doc(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")

dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-WRK-01"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-WRK-01"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ACT-006": full_spec(W / "publications/wm-act-006-task/spec.yaml"),
        "WM-ACT-003_legacy": text_doc(W / "models/activity-work/K3-process-and-workflow.md"),
    },
    "prior_research": {
        "EM-PRD-03_requirement": text_doc(W / "research/enterprise/runs/em-prd-03/local-evidence.md"),
        "EM-LND-05_project_program": text_doc(W / "research/enterprise/runs/em-lnd-05/local-evidence.md"),
        "EM-TEC-05_task_boundary": text_doc(W / "research/enterprise/runs/em-tec-05/local-evidence.md"),
    },
}

R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-WRK-01 Work Items and Delivery Flow against WM-ACT-006 Task, WM-ACT-003 Process/Workflow, WM-ACT-005 Project, WM-ACT-029 Program/Portfolio and WM-REC-006 Requirement. Determine whether WorkItem, WorkItemType, WorkflowDefinition, Transition, Backlog, Iteration and Estimate belong in one Task aggregate, as profiles, or need independent identities. Separate Epic/Feature as work containers from product requirement/value intent; tracker containers from projects; workflow source status from normalized outcome; effort estimate from actual time. Define idempotent cross-tracker import and evidence-based done/accepted/cancelled/rejected outcomes. Test migration between two workflows preserving distinct outcomes and no duplicate tasks. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Work item/type; Workflow/transition/outcome; Backlog/iteration; Estimate/time; Epic/feature/requirement/project; Import and acceptance; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")

result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode:
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
