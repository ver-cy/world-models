import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-leg-02"
IDS = {"WM-POL-001", "WM-KNW-012", "WM-ACT-034", "WM-XCT-029", "WM-XCT-009", "WM-XCT-010"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LEG-02"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LEG-02"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-POL-001": full_spec(W / "publications/wm-pol-001-legal-instrument-norm/spec.yaml"),
        "WM-KNW-012_adjacent": full_spec(W / "publications/wm-knw-012-policy-rule/spec.yaml"),
        "WM-ACT-034_adjacent": full_spec(W / "publications/wm-act-034-assessment-evaluation/spec.yaml"),
        "WM-XCT-029_adjacent": full_spec(W / "publications/wm-xct-029-obligation-commitment/spec.yaml"),
        "WM-XCT-009_adjacent": full_spec(W / "publications/wm-xct-009-time-calendar/spec.yaml"),
        "WM-XCT-010_adjacent": full_spec(W / "publications/wm-xct-010-location-referencing-address/spec.yaml"),
    },
    "prior_research": {
        "EM-LEG-01": text_doc(W / "research/enterprise/runs/em-leg-01/local-evidence.md"),
        "EM-LEG-03": text_doc(W / "research/enterprise/runs/em-leg-03/local-evidence.md"),
        "EM-RSK-01": text_doc(W / "research/enterprise/runs/em-rsk-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LEG-02 External norms and applicability around reserved WM-POL-001 Legal Instrument / Norm. Place ExternalRequirement, NormVersion, ApplicabilityAssessment and Jurisdiction relative to WM-KNW-012 Policy / Rule, WM-ACT-034 Assessment / Evaluation and WM-XCT-029 Obligation / Commitment. Distinguish legal work, expression/version, manifestation/source, provision and normalized norm identity. Separate publication/promulgation, entry into force, efficacy/applicability, compliance/transitional deadlines, repeal/supersession and record/knowledge time. Define how exceptions, derogations, exemptions and transitional periods are represented without flattening source authority. Decide whether applicability assessment needs a new aggregate or is a profile of WM-ACT-034; require pinned norm version/provision, subject/activity/product/market, jurisdiction, facts-as-of, assessor/authority, reasoning/evidence, conclusion, confidence/limitations, review/expiry and status. Explain how conflicting assessments coexist without silent overwrite and why citation or applicability does not prove compliance. Test a future-effective amendment and two reasoned market-specific interpretations. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Legal source and versions; Temporal semantics; Exceptions and transitions; Applicability assessment; Conflicting interpretations; Jurisdiction; Obligations and compliance; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
