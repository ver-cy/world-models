import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-ops-05"
IDS = {'WM-ECO-024', 'WM-OBJ-001', 'WM-OBJ-020', 'WM-FLW-004', 'WM-FLW-011', 'WM-FLW-012', 'WM-FLW-013', 'WM-ACT-007', 'WM-ECO-019', 'WM-ECO-020'}

def j(p):
    return json.loads(p.read_text(encoding="utf-8-sig"))

def rows(p):
    with p.open(encoding="utf-8-sig", newline="") as h:
        return list(csv.DictReader(h))

def compact(p):
    raw = p.read_bytes()
    d = yaml.safe_load(raw.decode("utf-8-sig"))
    s = d.get("structure", {})
    bundles = []
    for b in s.get("bundles", []):
        layers = []
        for layer in b.get("layers", []):
            findings = [
                {k: v for k, v in finding.items() if k not in {"questions", "data_elements", "artifacts", "source_refs"}}
                for finding in layer.get("findings", [])
            ]
            layers.append({k: v for k, v in layer.items() if k not in {"findings", "source_refs"}} | {"findings": findings})
        bundles.append({k: v for k, v in b.items() if k not in {"layers", "source_refs"}} | {"layers": layers})
    c = {k: v for k, v in d.items() if k not in {"sources", "structure"}}
    c["sources"] = [
        {k: x.get(k) for k in ("id", "title", "organization", "version_or_date", "source_type", "primary_source", "authority_tier")}
        for x in d.get("sources", [])
    ]
    c["structure"] = {k: v for k, v in s.items() if k != "bundles"} | {"bundles": bundles}
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": c}

def text_document(p):
    raw = p.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}

registry = j(W / "research/enterprise/registry.json")
queue = j(W / "research/enterprise/queue.json")
unified = rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
specs = {
    "WM-ECO-024": "publications/wm-eco-024-fulfilment-delivery/spec.yaml",
    "WM-OBJ-001": "publications/wm-obj-001-physical-item-instance/spec.yaml",
    "WM-OBJ-020": "publications/wm-obj-020-inventory-stock-position/spec.yaml",
    "WM-FLW-004": "publications/wm-flw-004-goods-movement-logistics/spec.yaml",
    "WM-FLW-011": "publications/wm-flw-011-shipment-consignment/spec.yaml",
    "WM-FLW-012": "publications/wm-flw-012-inventory-movement/spec.yaml",
    "WM-FLW-013": "publications/wm-flw-013-supply-chain-trace-chain-of-custody/spec.yaml",
    "WM-ACT-007": "publications/wm-act-007-work-order/spec.yaml",
    "WM-ECO-019": "publications/wm-eco-019-purchase-order/spec.yaml",
    "WM-ECO-020": "publications/wm-eco-020-sales-order/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-OPS-05"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-OPS-05"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-LND-11": text_document(W / "research/enterprise/runs/em-lnd-11/local-evidence.md"),
        "EM-OPS-04": text_document(W / "research/enterprise/runs/em-ops-04/local-evidence.md"),
        "EM-COM-03": text_document(W / "research/enterprise/runs/em-com-03/local-evidence.md"),
        "EM-OPS-02": text_document(W / "research/enterprise/runs/em-ops-02/local-evidence.md"),
        "EM-OPS-03": text_document(W / "research/enterprise/runs/em-ops-03/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-OPS-05 Inventory, Production and Logistics using complete WM-ECO-024 Fulfilment/Delivery, Physical Item, Inventory Position, Goods Movement/Logistics, Shipment/Consignment, Inventory Movement, Supply Trace, Work Order, Purchase Order and Sales Order drafts plus prior operations work. Candidate types are Lot, StockPosition, TransformationEvent, Shipment and LogisticsEvent. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Determine reuse for StockPosition, Shipment and LogisticsEvent; whether Lot and TransformationEvent require independent roots; keep serial item, lot/batch, stock position, handling unit, work/production order, planned shipment, actual movement, custody transfer, delivery receipt, inspection and acceptance distinct. Balance derives from event-ledger inputs and explicit corrections; missing row is not zero. Transformation must preserve input/output genealogy with quantities, units, yield/scrap, time, place, agent and evidence. Shipped does not mean delivered or accepted. Test one raw-material lot through transformation into serialized assemblies, partial shipment and targeted recall; recall only proven and potential affected units, not the entire SKU. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Lot/items/stock; Transformation/genealogy; Shipment/logistics/movement; Fulfilment/receipt/acceptance; Balance/corrections; Recall/impact; Time/quantity/provenance; Governance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide all five candidates and identify missing roots or contradictions. Do not claim canonical completeness, installability or publication readiness.

DOSSIER
""" + dossier_path.read_text(encoding="utf-8")
result = subprocess.run(
    ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
    input=prompt,
    text=True,
    encoding="utf-8",
    errors="replace",
    capture_output=True,
    timeout=900,
)
if result.returncode:
    raise SystemExit((result.stderr or result.stdout or f"claude exit {result.returncode}").strip())
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(dossier_path.stat().st_size, len(result.stdout))
