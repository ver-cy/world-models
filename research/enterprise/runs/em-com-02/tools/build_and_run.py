import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-com-02"
IDS = {"WM-ECO-026", "WM-ECO-021", "WM-ECO-027"}


def read_json(path): return json.loads(path.read_text(encoding="utf-8-sig"))
def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def full_spec(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": yaml.safe_load(raw.decode("utf-8-sig"))}

registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-COM-02"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-COM-02"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ECO-026": full_spec(W / "publications/wm-eco-026-sales-lead-opportunity/spec.yaml"),
        "WM-ECO-021": full_spec(W / "publications/wm-eco-021-offer-quote/spec.yaml"),
        "WM-ECO-027": full_spec(W / "publications/wm-eco-027-marketing-campaign/spec.yaml"),
    },
    "prior_research": {"EM-COM-01": (W / "research/enterprise/runs/em-com-01/research-reconciliation.md").read_text(encoding="utf-8-sig")},
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-COM-02 Sales and Marketing Interactions across WM-ECO-026 Sales Lead/Opportunity, WM-ECO-021 Offer/Quote, WM-ECO-027 Marketing Campaign and the counterparty boundary. Place Lead, Opportunity, Quote, Campaign and AttributionClaim with clear identity/lifecycle. Define when a lead may reference a Party without merging identities; evidence for opportunity probability and attribution; the boundary where a quote becomes an offer, order or binding contract. Preserve forecasts versus recognized revenue and avoid double recognition across two quotes. Test two campaigns, one lead and two independent quotes with method/window-qualified attribution. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Lead/party; Opportunity/forecast; Quote/offer/contract; Campaign/attribution; Conversion and deduplication; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
