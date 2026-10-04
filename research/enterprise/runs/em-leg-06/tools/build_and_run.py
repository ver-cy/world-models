import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-leg-06"
IDS = {"WM-XCT-002", "WM-XCT-003", "WM-DAT-001", "WM-DAT-004", "WM-PER-001", "WM-POL-001", "WM-KNW-012", "WM-ACT-021", "WM-ACT-034", "WM-XCT-029", "WM-REC-001"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LEG-06"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LEG-06"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-XCT-002": full_spec(W / "publications/wm-xct-002-access-contract-consent/spec.yaml"),
        "WM-XCT-003": full_spec(W / "publications/wm-xct-003-projection-disclosure-policy/spec.yaml"),
        "WM-DAT-001_adjacent": full_spec(W / "publications/wm-dat-001-dataset/spec.yaml"),
        "WM-DAT-004_adjacent": full_spec(W / "publications/wm-dat-004-data-schema-data-contract/spec.yaml"),
        "WM-PER-001_adjacent": full_spec(W / "publications/wm-per-001-person/spec.yaml"),
        "WM-POL-001_adjacent": full_spec(W / "publications/wm-pol-001-legal-instrument-norm/spec.yaml"),
        "WM-KNW-012_adjacent": full_spec(W / "publications/wm-knw-012-policy-rule/spec.yaml"),
        "WM-ACT-021_adjacent": full_spec(W / "publications/wm-act-021-service-case-ticket/spec.yaml"),
        "WM-ACT-034_adjacent": full_spec(W / "publications/wm-act-034-assessment-evaluation/spec.yaml"),
        "WM-XCT-029_adjacent": full_spec(W / "publications/wm-xct-029-obligation-commitment/spec.yaml"),
        "WM-REC-001_adjacent": full_spec(W / "publications/wm-rec-001-document-record/spec.yaml"),
    },
    "prior_research": {
        "EM-DAT-01": text_doc(W / "research/enterprise/runs/em-dat-01/local-evidence.md"),
        "EM-COM-04": text_doc(W / "research/enterprise/runs/em-com-04/local-evidence.md"),
        "EM-LEG-02": text_doc(W / "research/enterprise/runs/em-leg-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LEG-06 Personal-data processing and data-subject rights around WM-XCT-002 Access Contract / Consent and WM-XCT-003 Projection / Disclosure Policy. Place ProcessingActivity, Purpose, DataSubjectRequest, ProcessingBasis and RetentionRule. Determine whether an independent Processing Activity / ROPA aggregate is missing, whether DataSubjectRequest is a profile of WM-ACT-021 Service Case, and which concepts are dependent statements or policies. Separate purpose, system, operation, dataset, controller/processor role, legal basis and consent. Model purpose limitation through downstream transformations and projections without treating consent as the universal basis. Define deletion/erasure execution when accounting, legal-hold or other obligations require scoped retention; preserve proof without retaining the erased payload. Test an erasure request, lawful retention of part of the records and a minimal analytics projection. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Processing activity; Purpose and basis; Consent; Data-subject request; Retention and erasure; Projection and analytics; Roles and parties; Scenario; Invariants; Minimal completion shape; Holds. Do not claim legal advice, canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
