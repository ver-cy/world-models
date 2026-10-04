import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-02"
IDS = {"WM-ORG-001", "WM-ORG-012", "WM-ORG-010", "WM-ORG-011", "WM-XCT-001", "WM-XCT-002", "WM-XCT-003", "WM-XCT-040"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LND-02"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LND-02"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ORG-001": full_spec(W / "publications/wm-org-001-organization/spec.yaml"),
        "WM-ORG-012": full_spec(W / "publications/wm-org-012-inter-organizational-relationship/spec.yaml"),
        "WM-ORG-010_adjacent": full_spec(W / "publications/wm-org-010-legal-entity-registration/spec.yaml"),
        "WM-ORG-011_adjacent": full_spec(W / "publications/wm-org-011-business-establishment-branch/spec.yaml"),
        "WM-XCT-001_adjacent": full_spec(W / "publications/wm-xct-001-ownership-stewardship/spec.yaml"),
        "WM-XCT-002_adjacent": full_spec(W / "publications/wm-xct-002-access-contract-consent/spec.yaml"),
        "WM-XCT-003_adjacent": full_spec(W / "publications/wm-xct-003-projection-disclosure-policy/spec.yaml"),
        "WM-XCT-040_adjacent": full_spec(W / "publications/wm-xct-040-model-composition-resolution/spec.yaml"),
    },
    "prior_research": {
        "EM-ORG-01": text_doc(W / "research/enterprise/runs/em-org-01/local-evidence.md"),
        "EM-ORG-02": text_doc(W / "research/enterprise/runs/em-org-02/local-evidence.md"),
        "EM-LND-01": text_doc(W / "research/enterprise/runs/em-lnd-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LND-02 Group company landscape using WM-ORG-001 Organization and WM-ORG-012 Inter-organizational Relationship. Place GroupLandscape and GroupScopeView. Determine whether either needs independent identity or both are governed profiles/projections. Separate legal ownership/control, accounting consolidation, management boundary, operational service perimeter, brand/trade-name affiliation, franchise/network participation, security trust and data-sharing authorization. Preserve unknown, disputed and unverified owners/relationships. Explain federated fact mastership, as-of and scenario semantics, and how subsidiary access stays bounded through WM-XCT-002/003 rather than inferred from group membership. Test a holding and a franchise network with different perimeters and limited cross-organization projections. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Boundary types; Membership and uncertainty; Time and scenarios; Federation; Access and projection; Holding/franchise scenario; Invariants; Minimal profile shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
