import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-07"
IDS = {"WM-SFT-001", "WM-ECO-021", "WM-ACT-004", "WM-ECO-020", "WM-ECO-022", "WM-ACT-029", "WM-ECO-006", "WM-XCT-029", "WM-MAT-008", "WM-ORG-014"}


def read_json(path): return json.loads(path.read_text(encoding="utf-8-sig"))
def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def compact_spec(path):
    raw = path.read_bytes(); doc = yaml.safe_load(raw.decode("utf-8-sig")); structure = doc.get("structure", {})
    bundles=[]
    for b in structure.get("bundles", []):
        layers=[]
        for l in b.get("layers", []):
            findings=[{k:v for k,v in f.items() if k not in {"questions","data_elements","artifacts","source_refs"}} for f in l.get("findings", [])]
            layers.append({k:v for k,v in l.items() if k not in {"findings","source_refs"}}|{"findings":findings})
        bundles.append({k:v for k,v in b.items() if k not in {"layers","source_refs"}}|{"layers":layers})
    compact={k:v for k,v in doc.items() if k not in {"sources","structure"}}
    compact["sources"]=[{k:s.get(k) for k in ("id","title","organization","version_or_date","source_type","primary_source","authority_tier")} for s in doc.get("sources",[])]
    compact["structure"]={k:v for k,v in structure.items() if k!="bundles"}|{"bundles":bundles}
    return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"document":compact}
def text_doc(path):
    raw=path.read_bytes(); return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}


registry=read_json(W/"research/enterprise/registry.json"); queue=read_json(W/"research/enterprise/queue.json")
unified=read_rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv"); relations=read_rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
dossier={
 "contour":next(x for x in registry["units"] if x["id"]=="EM-LND-07"),
 "queue":next(x for x in queue["units"] if x["id"]=="EM-LND-07"),
 "related_registry_contours":[x for x in registry["units"] if x["id"] in {"EM-PRD-01","EM-PRD-02","EM-COM-02","EM-COM-03"}],
 "reservations":[x for x in unified if x.get("model_id") in IDS],
 "relations":[x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "spec_availability":{mid:bool(list((W/"publications").glob(mid.lower()+"-*/spec.yaml"))) for mid in IDS},
 "specs":{
  "WM-SFT-001":compact_spec(W/"publications/wm-sft-001-software-product/spec.yaml"),
  "WM-ECO-021":compact_spec(W/"publications/wm-eco-021-offer-quote/spec.yaml"),
  "WM-ECO-020":compact_spec(W/"publications/wm-eco-020-sales-order/spec.yaml"),
  "WM-ECO-022":compact_spec(W/"publications/wm-eco-022-subscription/spec.yaml"),
  "WM-ACT-029":compact_spec(W/"publications/wm-act-029-program-portfolio/spec.yaml"),
  "WM-ECO-006":compact_spec(W/"publications/wm-eco-006-commercial-contract/spec.yaml"),
  "WM-XCT-029":compact_spec(W/"publications/wm-xct-029-obligation-commitment/spec.yaml"),
  "WM-MAT-008":compact_spec(W/"publications/wm-mat-008-observation-measurement-record/spec.yaml"),
  "WM-ORG-014":compact_spec(W/"publications/wm-org-014-customer-account-relationship/spec.yaml"),
 },
 "prior_research":{
  "EM-PRD-01":text_doc(W/"research/enterprise/runs/em-prd-01/local-evidence.md"),
  "EM-PRD-02":text_doc(W/"research/enterprise/runs/em-prd-02/local-evidence.md"),
  "EM-COM-03":text_doc(W/"research/enterprise/runs/em-com-03/local-evidence.md"),
 },
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"; p.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LND-07 Product and Service Offering Portfolio, whose registry has no target IDs. Place OfferingLandscape and OfferingPortfolioScope across product, service definition, Product Catalogue/Offering Catalogue candidates, offer/quote, order, subscription/entitlement, contract/obligation, consumers and economics. Decide whether either landscape candidate needs independent identity or is a governed profile/projection. Keep Product, Service, Offering, Quote and Entitlement distinct. Define an explicit comparison method for commercial products versus internal services without treating zero revenue as zero value. Detect offerings that duplicate an intended outcome using evidence and uncertainty, not name similarity. Explain how retirement/closure handles active offers, subscriptions, contracts, obligations, support/retention and successor/migration. Test two commercial products and one internal service under different justified criteria. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Portfolio boundary; Product/service/offering; Comparison method; Duplicate outcomes; Economics and value; Retirement and obligations; Time/scenario; Scenario; Invariants; Minimal profile shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
result=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if result.returncode: raise SystemExit((result.stderr or result.stdout or f"claude exit {result.returncode}").strip())
(R/"claude-study.raw.md").write_text(result.stdout.rstrip()+"\n",encoding="utf-8"); print(p.stat().st_size,len(result.stdout))
