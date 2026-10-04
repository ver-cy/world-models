import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-wrk-02"
IDS = {"WM-ACT-005", "WM-ACT-031", "WM-ACT-008", "WM-ACT-032"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def full_spec(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": yaml.safe_load(raw.decode("utf-8-sig"))}


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")

dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-WRK-02"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-WRK-02"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ACT-005": full_spec(W / "publications/wm-act-005-project/spec.yaml"),
        "WM-ACT-031": full_spec(W / "publications/wm-act-031-milestone-deliverable/spec.yaml"),
        "WM-ACT-008": full_spec(W / "publications/wm-act-008-plan-schedule/spec.yaml"),
        "WM-ACT-032": full_spec(W / "publications/wm-act-032-change-request/spec.yaml"),
    },
    "prior_research": {
        "EM-LND-05": (W / "research/enterprise/runs/em-lnd-05/local-evidence.md").read_text(encoding="utf-8-sig"),
        "EM-WRK-01": (W / "research/enterprise/runs/em-wrk-01/local-evidence.md").read_text(encoding="utf-8-sig"),
    },
}

R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-WRK-02 Project and Project Change Management across WM-ACT-005 Project, WM-ACT-031 Milestone/Deliverable, WM-ACT-008 Plan/Schedule and WM-ACT-032 Change Request. Determine where ProjectCharter, Baseline, Milestone, Deliverable, Acceptance and ProjectChangeRequest live without identity collapse. Define a project boundary independent of methodology, many-to-many project/product/tracker-container relations, and separation of forecast, approved baseline and actual. Test two projects sharing one tracker and one product, with an approved change request creating a new baseline while preserving the original promise and acceptance basis. Reject Jira Project as automatic business-project identity and project closure as product closure. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Project/charter; Plan/forecast/baseline/actual; Milestone/deliverable/acceptance; Change request; Product/tracker relations; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")

result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode:
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
