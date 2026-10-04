import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-11"
IDS = {'WM-OBJ-001', 'WM-OBJ-002', 'WM-OBJ-017', 'WM-OBJ-018', 'WM-OBJ-019', 'WM-OBJ-020', 'WM-FLW-004', 'WM-FLW-011', 'WM-FLW-012', 'WM-FLW-013', 'WM-ACT-007', 'WM-ECO-019', 'WM-ECO-020', 'WM-ECO-024'}

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
    "WM-OBJ-001": "publications/wm-obj-001-physical-item-instance/spec.yaml",
    "WM-OBJ-002": "publications/wm-obj-002-product-type-catalog-item/spec.yaml",
    "WM-OBJ-017": "publications/wm-obj-017-product-configuration-variant/spec.yaml",
    "WM-OBJ-018": "publications/wm-obj-018-engineering-design-product-definition/spec.yaml",
    "WM-OBJ-019": "publications/wm-obj-019-component-type-engineering-bom/spec.yaml",
    "WM-OBJ-020": "publications/wm-obj-020-inventory-stock-position/spec.yaml",
    "WM-FLW-004": "publications/wm-flw-004-goods-movement-logistics/spec.yaml",
    "WM-FLW-011": "publications/wm-flw-011-shipment-consignment/spec.yaml",
    "WM-FLW-012": "publications/wm-flw-012-inventory-movement/spec.yaml",
    "WM-FLW-013": "publications/wm-flw-013-supply-chain-trace-chain-of-custody/spec.yaml",
    "WM-ACT-007": "publications/wm-act-007-work-order/spec.yaml",
    "WM-ECO-019": "publications/wm-eco-019-purchase-order/spec.yaml",
    "WM-ECO-020": "publications/wm-eco-020-sales-order/spec.yaml",
    "WM-ECO-024": "publications/wm-eco-024-fulfilment-delivery/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LND-11"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LND-11"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-OPS-03": text_document(W / "research/enterprise/runs/em-ops-03/local-evidence.md"),
        "EM-PRD-01": text_document(W / "research/enterprise/runs/em-prd-01/local-evidence.md"),
        "EM-PRD-02": text_document(W / "research/enterprise/runs/em-prd-02/local-evidence.md"),
        "EM-LND-12": text_document(W / "research/enterprise/runs/em-lnd-12/local-evidence.md"),
        "EM-LND-13": text_document(W / "research/enterprise/runs/em-lnd-13/local-evidence.md"),
        "EM-LND-17": text_document(W / "research/enterprise/runs/em-lnd-17/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-LND-11 Operations Landscape and Supply Network using complete current Physical Item, Product Type, Product Variant, Engineering Definition, Engineering BOM, Inventory Position, Goods Movement, Shipment, Inventory Movement, Supply Trace/Chain of Custody, Work Order, Purchase Order, Sales Order and Fulfilment/Delivery drafts plus prior boundary work. Candidate types are OperationsLandscape and SupplyNetwork. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Determine whether OperationsLandscape is a governed declaration and reproducible projection; whether SupplyNetwork is a stable subject root, a scoped network declaration or a graph projection over parties, facilities and supply relations. Separate engineering BOM/intended composition, manufacturing or transformation plan, work order, actual consumption/production event, serialized item, lot/batch, inventory position, movement, custody transfer, shipment, order, delivery, supplier identity and trace assertion. Require every genealogy edge to cite actual events/evidence, quantity/unit/time/location/capacity, source and confidence. Mark unknown origin and incomplete trace explicitly. Never infer actual lot composition from BOM alone. Test a recalled component lot: classify proven affected, potentially affected and not evidenced items without overreach, and expose an unknown supplier break. Also align process definitions with actual movements without treating plan as movement. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Landscape/network; Product/design/BOM; Work/transform events; Lots/items/inventory; Movements/shipment/delivery; Traceability/evidence; Recall/impact; Time/quantity/provenance; Governance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide both candidates and identify missing aggregate roots or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
