import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-tec-06"
IDS = {"WM-SFT-016", "WM-ECO-006", "WM-MAT-008", "WM-ACT-004"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-TEC-06"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-TEC-06"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ECO-006": full_spec(W / "publications/wm-eco-006-commercial-contract/spec.yaml"),
        "WM-MAT-008": full_spec(W / "publications/wm-mat-008-observation-measurement-record/spec.yaml"),
        "WM-ACT-004_legacy": text_doc(W / "models/activity-work/K4-service.md"),
    },
    "missing_specs": {"WM-SFT-016": "Reserved Service Level / SLO candidate has no current specification file."},
    "prior_research": {
        "EM-DAT-05_metric_definition": text_doc(W / "research/enterprise/runs/em-dat-05/local-evidence.md"),
        "EM-LEG-01_sla_contract_boundary": text_doc(W / "research/enterprise/runs/em-leg-01/local-evidence.md"),
        "EM-PRD-02_service_boundary": text_doc(W / "research/enterprise/runs/em-prd-02/local-evidence.md"),
    },
}

R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-TEC-06 Reliability, SLO and Observability against reserved WM-SFT-016 Service Level / SLO, WM-ACT-004 Service, WM-ECO-006 Commercial Contract, WM-MAT-008 Observation / Measurement and prior Metric Definition research. Separate SLI specification, SLO policy, evaluation, error-budget policy, observability binding, raw observations and contractual SLA. Decide whether these are one aggregate, profiles or independent models. Define SLO subject placement for service, user journey, system and instance; telemetry gaps; window changes; eligibility/exclusions; useful-user outcome. Test a user journey across three services with incomplete telemetry and changed evaluation window, producing unknown rather than false success. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; SLI/SLO/evaluation/error budget; Subject placement; Observability binding; Missing data and windows; SLA boundary; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")

result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode:
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
