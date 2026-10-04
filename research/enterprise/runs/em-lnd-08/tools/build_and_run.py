import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models"); R=W/"research/enterprise/runs/em-lnd-08"
IDS={"WM-ORG-014","WM-ECO-020","WM-ORG-001","WM-ORG-012","WM-ECO-021","WM-ECO-022","WM-ECO-026","WM-ECO-027","WM-MAT-008","WM-XCT-002","WM-XCT-003"}
def read_json(p): return json.loads(p.read_text(encoding="utf-8-sig"))
def rows(p):
 with p.open(encoding="utf-8-sig",newline="") as h:return list(csv.DictReader(h))
def compact(p):
 raw=p.read_bytes(); d=yaml.safe_load(raw.decode("utf-8-sig")); s=d.get("structure",{}); bs=[]
 for b in s.get("bundles",[]):
  ls=[]
  for l in b.get("layers",[]):
   fs=[{k:v for k,v in f.items() if k not in {"questions","data_elements","artifacts","source_refs"}} for f in l.get("findings",[])]
   ls.append({k:v for k,v in l.items() if k not in {"findings","source_refs"}}|{"findings":fs})
  bs.append({k:v for k,v in b.items() if k not in {"layers","source_refs"}}|{"layers":ls})
 c={k:v for k,v in d.items() if k not in {"sources","structure"}}; c["sources"]=[{k:x.get(k) for k in ("id","title","organization","version_or_date","source_type","primary_source","authority_tier")} for x in d.get("sources",[])]; c["structure"]={k:v for k,v in s.items() if k!="bundles"}|{"bundles":bs}
 return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"document":c}
def textdoc(p):
 raw=p.read_bytes(); return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}
reg=read_json(W/"research/enterprise/registry.json"); q=read_json(W/"research/enterprise/queue.json"); u=rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv"); rel=rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
d={"contour":next(x for x in reg["units"] if x["id"]=="EM-LND-08"),"queue":next(x for x in q["units"] if x["id"]=="EM-LND-08"),"reservations":[x for x in u if x.get("model_id") in IDS],"relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],"specs":{
"WM-ORG-014":compact(W/"publications/wm-org-014-customer-account-relationship/spec.yaml"),"WM-ECO-020":compact(W/"publications/wm-eco-020-sales-order/spec.yaml"),"WM-ORG-001":compact(W/"publications/wm-org-001-organization/spec.yaml"),"WM-ORG-012":compact(W/"publications/wm-org-012-inter-organizational-relationship/spec.yaml"),"WM-ECO-021":compact(W/"publications/wm-eco-021-offer-quote/spec.yaml"),"WM-ECO-022":compact(W/"publications/wm-eco-022-subscription/spec.yaml"),"WM-ECO-026":compact(W/"publications/wm-eco-026-sales-lead-opportunity/spec.yaml"),"WM-ECO-027":compact(W/"publications/wm-eco-027-marketing-campaign/spec.yaml"),"WM-MAT-008":compact(W/"publications/wm-mat-008-observation-measurement-record/spec.yaml"),"WM-XCT-002":compact(W/"publications/wm-xct-002-access-contract-consent/spec.yaml"),"WM-XCT-003":compact(W/"publications/wm-xct-003-projection-disclosure-policy/spec.yaml")},"prior_research":{"EM-COM-01":textdoc(W/"research/enterprise/runs/em-com-01/research-reconciliation.md"),"EM-COM-02":textdoc(W/"research/enterprise/runs/em-com-02/local-evidence.md"),"EM-COM-03":textdoc(W/"research/enterprise/runs/em-com-03/local-evidence.md"),"EM-LND-02":textdoc(W/"research/enterprise/runs/em-lnd-02/local-evidence.md")}}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"; p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LND-08 Commercial Landscape using WM-ORG-014 Customer Account Relationship and WM-ECO-020 Sales Order, with party/group, opportunity, quote, subscription, campaign, observation, access and projection context. Place CommercialLandscape and MarketScope and decide whether either needs independent identity or is a governed profile/projection. Define party reuse across customer/supplier/partner roles; concentration without double-counting a corporate group; typed unknown/disputed group links; seller/business perimeter; segmentation method and period. Separate forecast, pipeline, quote, order, subscription and observed revenue/delivery facts. Identify forecasts unsupported by orders without treating them as false. Test customer concentration in two business perimeters while preserving uncertain group relationships and a party that is both customer and supplier. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Market scope; Party roles and grouping; Concentration; Forecast versus fact; Time/scenario; Access and disclosure; Scenario; Invariants; Minimal profile shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8"); print(p.stat().st_size,len(r.stdout))
