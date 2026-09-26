import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-dat-07"
IDS = {"WM-ACT-034", "WM-KNW-007", "WM-ACT-036", "WM-KNW-010", "WM-ACT-024", "WM-REC-002"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-DAT-07"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-DAT-07"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ACT-034": full_spec(W / "publications/wm-act-034-assessment-evaluation/spec.yaml"),
        "WM-KNW-007": full_spec(W / "publications/wm-knw-007-claim-proposition/spec.yaml"),
        "WM-ACT-036_adjacent": full_spec(W / "publications/wm-act-036-research-study/spec.yaml"),
        "WM-KNW-010_adjacent": full_spec(W / "publications/wm-knw-010-decision-rationale/spec.yaml"),
        "WM-ACT-024_adjacent": full_spec(W / "publications/wm-act-024-decision-approval-activity/spec.yaml"),
    },
    "prior_research": {
        "EM-DAT-04": text_doc(W / "research/enterprise/runs/em-dat-04/local-evidence.md"),
        "EM-DAT-06": text_doc(W / "research/enterprise/runs/em-dat-06/local-evidence.md"),
        "EM-KNW-02": text_doc(W / "research/enterprise/runs/em-knw-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-DAT-07 Analytical Study and Conclusion across target WM-ACT-034 Assessment/Evaluation and WM-KNW-007 Claim/Proposition, explicitly comparing adjacent WM-ACT-036 Research Study, WM-KNW-010 Decision/Rationale and WM-ACT-024 Decision/Approval Activity. Place AnalyticalStudy, AnalysisMethod, AnalyticalFinding and Recommendation. Preserve study/question/protocol/population/sample/method/execution, observation/evidence, claim/finding, report, recommendation, decision content and decision occurrence as distinct where needed. Define how association, causation, assumptions, alternative interpretations, exclusions, bias and generalisability are recorded. Test two competing interpretations of the same ticket-growth dataset with a biased sample; reject the inference that ticket growth proves an employee productivity decline. A recommendation must not become an accepted decision. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Study/method boundary; Finding/claim boundary; Causality and alternatives; Recommendation/decision boundary; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
