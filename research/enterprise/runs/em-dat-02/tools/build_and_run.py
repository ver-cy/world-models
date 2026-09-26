import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-dat-02"
IDS = {"WM-DAT-008", "WM-DAT-001", "WM-DAT-004", "WM-DAT-007", "WM-MAT-008", "WM-SFT-003", "WM-ACT-053"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-DAT-02"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-DAT-02"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-DAT-008": full_spec(W / "publications/wm-dat-008-data-catalog-entry-data-product/spec.yaml"),
        "WM-DAT-001_adjacent": full_spec(W / "publications/wm-dat-001-dataset/spec.yaml"),
        "WM-DAT-004_adjacent": full_spec(W / "publications/wm-dat-004-data-schema-data-contract/spec.yaml"),
        "WM-DAT-007_adjacent": full_spec(W / "publications/wm-dat-007-data-quality-assessment/spec.yaml"),
        "WM-MAT-008_adjacent": full_spec(W / "publications/wm-mat-008-observation-measurement-record/spec.yaml"),
    },
    "prior_research": {
        "EM-DAT-01": text_doc(W / "research/enterprise/runs/em-dat-01/local-evidence.md"),
        "EM-DAT-05": text_doc(W / "research/enterprise/runs/em-dat-05/local-evidence.md"),
        "EM-TEC-03": text_doc(W / "research/enterprise/runs/em-tec-03/local-evidence.md"),
        "EM-PRD-01": text_doc(W / "research/enterprise/runs/em-prd-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-DAT-02 Data Product across reserved WM-DAT-008 Data Catalog Entry / Data Product and its dataset, contract, quality, metric, interface and pipeline neighbors. Decide whether DataProduct is an independently governed offering described by CatalogRecord, and whether DataProductOffering or DataConsumerAgreement needs a separate identity, can be a contained versioned component, or must reuse an existing external master. Preserve independent Dataset and DatasetVersion identities, distributions, interface contracts, pipeline executions, access authorization, quality assessments, observations and commercial/legal agreements. Define the minimum promotion gate from an ordinary dataset/table to a Data Product: purpose, accountable owner, consumer scope, value/use cases, composition, access route, versioned contract, measurable quality/SLO promise and lifecycle. Test one product supplying two independently versioned datasets plus one API under different consumer terms without collapsing versions, authorization, availability, delivery or fitness. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Catalog record versus product; Dataset/distribution/interface/pipeline boundaries; Offering/agreement placement; Promise and evidence; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
