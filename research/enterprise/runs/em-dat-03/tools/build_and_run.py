import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-dat-03"
IDS = {"WM-DAT-005", "WM-DAT-006", "WM-ACT-053", "WM-DAT-001", "WM-DAT-004", "WM-XCT-012"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-DAT-03"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-DAT-03"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-DAT-005": full_spec(W / "publications/wm-dat-005-data-pipeline/spec.yaml"),
        "WM-DAT-006": full_spec(W / "publications/wm-dat-006-data-lineage/spec.yaml"),
        "WM-ACT-053_adjacent": full_spec(W / "publications/wm-act-053-data-processing-job-pipeline-run/spec.yaml"),
        "WM-DAT-001_adjacent": full_spec(W / "publications/wm-dat-001-dataset/spec.yaml"),
        "WM-DAT-004_adjacent": full_spec(W / "publications/wm-dat-004-data-schema-data-contract/spec.yaml"),
        "WM-XCT-012_adjacent": full_spec(W / "publications/wm-xct-012-provenance/spec.yaml"),
    },
    "prior_research": {
        "EM-DAT-01": text_doc(W / "research/enterprise/runs/em-dat-01/local-evidence.md"),
        "EM-DAT-02": text_doc(W / "research/enterprise/runs/em-dat-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-DAT-03 Pipeline, Run and Data Lineage across reserved WM-DAT-005 Data Pipeline, WM-DAT-006 Data Lineage and WM-ACT-053 Data Processing Job / Pipeline Run. Place DataPipeline, PipelineRun, Transformation and LineageAssertion without duplicating definition, execution, dataset/schema or provenance masters. Define identity, versioning and mastership for pipeline definitions, steps, transformations, runs, attempts, input/output bindings and lineage assertions. Explain how lineage can be partially observed without asserting false causality, how manual corrections and opaque external inputs are represented, and what evidence is sufficient to reproduce a concrete output. Test two runs, a manual correction and an unknown external input producing a partially evidenced chain. Distinguish intended topology from observed lineage, derivation from correlation, missing evidence from absence of dependency, and run success from data quality. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Definition versus execution; Lineage assertion; Manual correction and opaque input; Reproducibility; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
