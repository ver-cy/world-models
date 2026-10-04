import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-leg-04"
IDS = {"WM-POL-004", "WM-POL-014", "WM-XCT-017", "WM-ECO-022", "WM-KNW-003", "WM-PER-013", "WM-POL-001", "WM-ACT-034"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LEG-04"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LEG-04"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "spec_availability": {mid: bool(list((W / "publications").glob(mid.lower() + "-*/spec.yaml"))) for mid in IDS},
    "specs": {
        "WM-POL-004": full_spec(W / "publications/wm-pol-004-permit-authorization/spec.yaml"),
        "WM-XCT-017_adjacent": full_spec(W / "publications/wm-xct-017-attestation-credential/spec.yaml"),
        "WM-ECO-022_adjacent": full_spec(W / "publications/wm-eco-022-subscription/spec.yaml"),
        "WM-PER-013_adjacent": full_spec(W / "publications/wm-per-013-professional-license-credential/spec.yaml"),
        "WM-POL-001_adjacent": full_spec(W / "publications/wm-pol-001-legal-instrument-norm/spec.yaml"),
        "WM-ACT-034_adjacent": full_spec(W / "publications/wm-act-034-assessment-evaluation/spec.yaml"),
    },
    "prior_research": {
        "EM-LEG-02": text_doc(W / "research/enterprise/runs/em-leg-02/local-evidence.md"),
        "EM-COM-03": text_doc(W / "research/enterprise/runs/em-com-03/local-evidence.md"),
        "EM-TEC-02": text_doc(W / "research/enterprise/runs/em-tec-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LEG-04 Permits, licences and authorized activity around reserved WM-POL-004 Permit / Authorization, which explicitly owns the application-to-decision case and excludes the permission-bearing grant. Place Permit, Licence, PermitCondition and LicenceScope. Decide whether the granted regulatory authorization should complete reserved WM-POL-014 Rights / Entitlements, use WM-XCT-017 Attestation / Credential, or remain an identifier-unassigned independent model candidate. Keep regulatory permission separate from commercial consumption entitlement/subscription and intellectual-property licence grant. Define identity, holder and non-transferability, authority and legal basis, regulated subject/activity/product/site/asset, territory, conditions, validity, renewal, variation, suspension, revocation, surrender and expiry. Explain how to represent an activity before a stable classifier exists. Prevent implicit extension to subsidiaries, locations, activities or successor entities. Test a licence for one site, temporary suspension and a new activity outside scope. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Case versus grant; Regulatory versus commercial/IP rights; Scope and activity; Conditions; Lifecycle; Parties and affiliates; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
