import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-ops-02"
IDS = {"WM-ECO-019", "WM-ECO-021", "WM-ECO-006", "WM-KNW-010", "WM-ACT-034", "WM-ORG-001", "WM-XCT-016"}

def j(p): return json.loads(p.read_text(encoding="utf-8-sig"))
def rows(p):
    with p.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def compact(p):
    raw = p.read_bytes(); d = yaml.safe_load(raw.decode("utf-8-sig")); s = d.get("structure", {}); bs = []
    for b in s.get("bundles", []):
        ls = []
        for l in b.get("layers", []):
            fs = [{k:v for k,v in f.items() if k not in {"questions","data_elements","artifacts","source_refs"}} for f in l.get("findings", [])]
            ls.append({k:v for k,v in l.items() if k not in {"findings","source_refs"}} | {"findings":fs})
        bs.append({k:v for k,v in b.items() if k not in {"layers","source_refs"}} | {"layers":ls})
    c = {k:v for k,v in d.items() if k not in {"sources","structure"}}
    c["sources"] = [{k:x.get(k) for k in ("id","title","organization","version_or_date","source_type","primary_source","authority_tier")} for x in d.get("sources", [])]
    c["structure"] = {k:v for k,v in s.items() if k != "bundles"} | {"bundles":bs}
    return {"bytes":len(raw), "sha256":hashlib.sha256(raw).hexdigest(), "document":c}
def td(p):
    raw=p.read_bytes(); return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}

reg=j(W/"research/enterprise/registry.json"); q=j(W/"research/enterprise/queue.json")
u=rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv"); rel=rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
spec_paths = {
 "WM-ECO-019":"publications/wm-eco-019-purchase-order/spec.yaml",
 "WM-ECO-021":"publications/wm-eco-021-offer-quote/spec.yaml",
 "WM-ECO-006":"publications/wm-eco-006-commercial-contract/spec.yaml",
 "WM-KNW-010":"publications/wm-knw-010-decision-rationale/spec.yaml",
 "WM-ACT-034":"publications/wm-act-034-assessment-evaluation/spec.yaml",
 "WM-ORG-001":"publications/wm-org-001-organization/spec.yaml",
 "WM-XCT-016":"publications/wm-xct-016-identity-register/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-OPS-02"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-OPS-02"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "EM-COM-01":td(W/"research/enterprise/runs/em-com-01/README.md") if (W/"research/enterprise/runs/em-com-01/README.md").exists() else {"note":"immutable release recorded outside run folder"},
   "EM-PRD-01":td(W/"research/enterprise/runs/em-prd-01/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-OPS-02 Procurement and Supplier Selection using WM-ECO-019 Purchase Order plus offer, contract, decision, assessment, party and identity boundaries. Place ProcurementRequest, SourcingEvent, SupplierBid, BidEvaluation and AwardDecision. Decide which are profiles/components and which require independent identity/lifecycle; do not allocate identifiers. Separate supplier qualification from bid evaluation, evaluation from decision, award from purchase order, and order from signed contract. Define versioned requirements/criteria, sealed bid submission and opening, clarifications, conflicts of interest, evaluator independence, scoring provenance, exceptions and single-source justification. Test three bids where a criterion changes, one evaluator has a conflict and the final award remains explainable without deleting history. Reject the negative case that winning automatically creates a signed contract. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Process boundary; Request and sourcing event; Bid and evaluation; Award and downstream commerce; Supplier qualification; Conflict and fairness; Single source; Time/version/scenario; Acceptance scenario; Invariants; Minimal model set; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))


