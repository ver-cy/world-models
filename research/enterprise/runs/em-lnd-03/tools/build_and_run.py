import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-03"
IDS = {"WM-ORG-005", "WM-ORG-016", "WM-PER-001", "WM-ORG-002", "WM-ORG-003", "WM-ORG-004", "WM-XCT-016", "WM-XCT-023", "WM-MAT-008", "WM-XCT-002", "WM-XCT-003"}


def read_json(path): return json.loads(path.read_text(encoding="utf-8-sig"))
def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def full_spec(path):
    raw = path.read_bytes(); doc = yaml.safe_load(raw.decode("utf-8-sig"))
    structure = doc.get("structure", {})
    compact_bundles = []
    for bundle in structure.get("bundles", []):
        compact_layers = []
        for layer in bundle.get("layers", []):
            compact_findings = []
            for finding in layer.get("findings", []):
                compact_findings.append({k: v for k, v in finding.items() if k not in {"questions", "data_elements", "artifacts", "source_refs"}})
            compact_layers.append({k: v for k, v in layer.items() if k not in {"findings", "source_refs"}} | {"findings": compact_findings})
        compact_bundles.append({k: v for k, v in bundle.items() if k not in {"layers", "source_refs"}} | {"layers": compact_layers})
    compact = {k: v for k, v in doc.items() if k not in {"sources", "structure"}}
    compact["sources"] = [{k: s.get(k) for k in ("id", "title", "organization", "version_or_date", "source_type", "primary_source", "authority_tier")} for s in doc.get("sources", [])]
    compact["structure"] = {k: v for k, v in structure.items() if k != "bundles"} | {"bundles": compact_bundles}
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": compact}
def text_doc(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LND-03"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LND-03"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ORG-005": full_spec(W / "publications/wm-org-005-employment/spec.yaml"),
        "WM-ORG-016": full_spec(W / "publications/wm-org-016-work-assignment/spec.yaml"),
        "WM-PER-001_adjacent": full_spec(W / "publications/wm-per-001-person/spec.yaml"),
        "WM-ORG-002_adjacent": full_spec(W / "publications/wm-org-002-organizational-unit/spec.yaml"),
        "WM-ORG-003_adjacent": full_spec(W / "publications/wm-org-003-team/spec.yaml"),
        "WM-ORG-004_adjacent": full_spec(W / "publications/wm-org-004-position/spec.yaml"),
        "WM-XCT-016_adjacent": full_spec(W / "publications/wm-xct-016-identity-register/spec.yaml"),
        "WM-XCT-023_adjacent": full_spec(W / "publications/wm-xct-023-party-role/spec.yaml"),
        "WM-MAT-008_adjacent": full_spec(W / "publications/wm-mat-008-observation-measurement-record/spec.yaml"),
        "WM-XCT-002_adjacent": full_spec(W / "publications/wm-xct-002-access-contract-consent/spec.yaml"),
        "WM-XCT-003_adjacent": full_spec(W / "publications/wm-xct-003-projection-disclosure-policy/spec.yaml"),
    },
    "prior_research": {
        "EM-ORG-05": text_doc(W / "research/enterprise/runs/em-org-05/local-evidence.md"),
        "EM-ORG-06": text_doc(W / "research/enterprise/runs/em-org-06/local-evidence.md"),
        "EM-PEO-01": text_doc(W / "research/enterprise/runs/em-peo-01/local-evidence.md"),
        "EM-PEO-02": text_doc(W / "research/enterprise/runs/em-peo-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LND-03 Workforce Landscape using WM-ORG-005 Employment and WM-ORG-016 Work Assignment. Place WorkforceLandscape and WorkforceScope. Determine whether either needs independent identity or both are profile/projection constructs. Separate unique persons, legal headcount, active relationships, assignments, positions, FTE and capacity; define denominators, time basis and double-counting rules. Cover employees, contractors, agency workers, dual affiliation, concurrent contracts and one person with two employers. Preserve Person identity without exposing it in aggregates. Explain which workforce aggregates disclose individual information and how WM-XCT-002/003 and cohort/privacy controls limit them. Test one person with two employers yielding one unique person and methodologically justified headcount/FTE. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Population boundary; Counting semantics; Contractors and dual affiliation; Time and scenarios; Privacy and disclosure; Scenario; Invariants; Minimal profile shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit((result.stderr or result.stdout or f"claude exit {result.returncode}").strip())
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
