import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-tec-05"
IDS = {"WM-ACT-019", "WM-ACT-020", "WM-KNW-014", "WM-SFT-014", "WM-ACT-006"}


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
legacy = W / "models/events-phenomena/X3-incident-and-emergency.md"
legacy_raw = legacy.read_bytes()

dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-TEC-05"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-TEC-05"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ACT-019_legacy": {"bytes": len(legacy_raw), "sha256": hashlib.sha256(legacy_raw).hexdigest(), "content": legacy_raw.decode("utf-8-sig")},
        "WM-ACT-020": full_spec(W / "publications/wm-act-020-cyber-incident/spec.yaml"),
    },
    "missing_specs": {
        "WM-KNW-014": "Reserved Issue / Problem candidate has no current specification file.",
        "WM-SFT-014": "Reserved Defect / Bug candidate has no current specification file.",
        "WM-ACT-006": "Reserved Task candidate has no current specification file.",
    },
}

R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-TEC-05 Incident, Problem and Root Cause across WM-ACT-019 Incident / Emergency and WM-ACT-020 Cyber Incident, with reserved WM-KNW-014 Issue / Problem, WM-SFT-014 Defect / Bug and WM-ACT-006 Task boundaries. Separate observation/event, operational incident, cyber incident, persistent problem, defect, response/remediation task, impact assessment and evidence-qualified root-cause claim. Determine reuse/profile/new disposition and whether RootCauseClaim or ImpactAssessment needs independent identity. Test three incidents linked to one problem, temporary restoration, one disputed cause and unfinished permanent remediation. Preserve severity versus priority and restoration versus problem closure. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Event/incident/cyber boundary; Problem/defect/task; Impact and root cause; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")

result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode:
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
