import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-com-03"
IDS = {"WM-ECO-020", "WM-ECO-022", "WM-ECO-021", "WM-ECO-009", "WM-ECO-008"}


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
    "contour": next(x for x in registry["units"] if x["id"] == "EM-COM-03"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-COM-03"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ECO-020": full_spec(W / "publications/wm-eco-020-sales-order/spec.yaml"),
        "WM-ECO-022": full_spec(W / "publications/wm-eco-022-subscription/spec.yaml"),
        "WM-ECO-021_adjacent": full_spec(W / "publications/wm-eco-021-offer-quote/spec.yaml"),
    },
    "prior_research": {
        "EM-COM-02": text_doc(W / "research/enterprise/runs/em-com-02/local-evidence.md"),
        "EM-FIN-03": text_doc(W / "research/enterprise/runs/em-fin-03/local-evidence.md"),
        "EM-PRD-01": text_doc(W / "research/enterprise/runs/em-prd-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-COM-03 Order, Subscription and Consumption Entitlement across WM-ECO-020 Sales Order and WM-ECO-022 Subscription, with WM-ECO-021 Offer/Quote and payment/invoice boundaries. Place Order, OrderLine, Subscription, Entitlement and Renewal. Separate order/line lifecycle, fulfilment/delivery, invoice, payment, entitlement and actual usage. Define partial fulfilment and allocation without payment implying delivery. Define mid-cycle plan/price change, suspension and renewal without rewriting history. Test partial delivery, subscription suspension and renewal at a new price while preserving prior offer/order/subscription periods. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Order/line; Subscription/entitlement/usage; Fulfilment/invoice/payment; Change/renewal/proration; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
