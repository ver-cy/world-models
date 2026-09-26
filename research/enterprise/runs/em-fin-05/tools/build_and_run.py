import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-fin-05"
IDS = {"WM-ECO-002", "WM-FLW-015", "WM-MAT-008", "WM-ECO-008", "WM-ECO-016", "WM-ECO-012"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-FIN-05"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-FIN-05"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ECO-002": full_spec(W / "publications/wm-eco-002-price-valuation/spec.yaml"),
        "WM-FLW-015_adjacent": full_spec(W / "publications/wm-flw-015-resource-consumption/spec.yaml"),
        "WM-MAT-008_adjacent": full_spec(W / "publications/wm-mat-008-observation-measurement-record/spec.yaml"),
        "WM-ECO-008_adjacent": full_spec(W / "publications/wm-eco-008-invoice-commercial-document/spec.yaml"),
        "WM-ECO-016_adjacent": full_spec(W / "publications/wm-eco-016-financial-transaction-journal-entry/spec.yaml"),
    },
    "prior_research": {
        "EM-FIN-01": text_doc(W / "research/enterprise/runs/em-fin-01/local-evidence.md"),
        "EM-FIN-02": text_doc(W / "research/enterprise/runs/em-fin-02/local-evidence.md"),
        "EM-PRD-01": text_doc(W / "research/enterprise/runs/em-prd-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-FIN-05 Cost, Consumption and Cost Allocation against reserved WM-ECO-002 Price/Valuation and adjacent WM-FLW-015 Resource Consumption, WM-MAT-008 Observation, WM-ECO-008 Invoice and WM-ECO-016 Journal Entry. Place CostRecord, UsageRecord, AllocationRule and UnitCostObservation. Keep quoted price, invoice amount, ledger-recognized cost, measured usage, allocated cost and valuation distinct. Decide which concepts require independent identities/lifecycles and which can reuse current masters. Define versioned allocation rules, allocation bases, shared/reserved capacity, discounts, commitments, multi-currency, residuals, confidence and reconciliation. Test allocating one shared cloud invoice, reserved capacity and a discount across project and product targets while preserving a visible unallocated remainder and preventing 100% duplication. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Price/cost/usage boundaries; Allocation rule and execution; Unit economics; Currency/time; Reconciliation/correction; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
