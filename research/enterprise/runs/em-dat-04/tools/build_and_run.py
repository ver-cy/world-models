import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-dat-04"
IDS = {"WM-DAT-007", "WM-MAT-008", "WM-KNW-013", "WM-KNW-014", "WM-ACT-034", "WM-DAT-001", "WM-DAT-004"}


def read_json(path): return json.loads(path.read_text(encoding="utf-8-sig"))
def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def full_spec(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": yaml.safe_load(raw.decode("utf-8-sig"))}
def text_doc(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}

registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-DAT-04"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-DAT-04"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-DAT-007": full_spec(W / "publications/wm-dat-007-data-quality-assessment/spec.yaml"),
        "WM-MAT-008_adjacent": full_spec(W / "publications/wm-mat-008-observation-measurement-record/spec.yaml"),
        "WM-KNW-013_adjacent": full_spec(W / "publications/wm-knw-013-constraint-requirement-rule/spec.yaml"),
        "WM-KNW-014_adjacent": full_spec(W / "publications/wm-knw-014-issue-problem/spec.yaml"),
        "WM-ACT-034_adjacent": full_spec(W / "publications/wm-act-034-assessment-evaluation/spec.yaml"),
    },
    "prior_research": {
        "EM-DAT-03": text_doc(W / "research/enterprise/runs/em-dat-03/local-evidence.md"),
        "EM-DAT-05": text_doc(W / "research/enterprise/runs/em-dat-05/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-DAT-04 Data Quality and Context Coverage across reserved WM-DAT-007 Data Quality Assessment and its observation, metric-definition, constraint/rule, issue and general-assessment neighbors. Place DataQualityRule, QualityEvaluation, QualityIssue and CoverageAssessment without duplicating reusable rule/metric, observation or issue masters. Define purpose-qualified completeness, accuracy, validity, freshness and coverage; specify how unknown denominators, sampling frames, uncertainty, reference truth and time are recorded. A correction must not rewrite an earlier assessment. Test a fully populated but stale dataset and a partial high-accuracy sample, ensuring 100% field population never becomes 100% truth. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Rule/metric/observation boundaries; Dimensions and denominators; Evaluation and verdict; Issue/remediation; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
