import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-ops-03"
IDS = {"WM-ECO-011", "WM-ACT-007", "WM-OBJ-001", "WM-OBJ-022", "WM-OBJ-023", "WM-ACT-013", "WM-ACT-034", "WM-MAT-008"}

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
 "WM-ACT-007":"publications/wm-act-007-work-order/spec.yaml",
 "WM-OBJ-001":"publications/wm-obj-001-physical-item-instance/spec.yaml",
 "WM-ACT-034":"publications/wm-act-034-assessment-evaluation/spec.yaml",
 "WM-MAT-008":"publications/wm-mat-008-observation-measurement-record/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-OPS-03"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-OPS-03"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "WM-ECO-011 legacy complete document":td(W/"models/society/B11-personal-property-and-assets.md"),
   "EM-LND-17":td(W/"research/enterprise/runs/em-lnd-17/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-OPS-03 Asset, Maintenance and Calibration using the legacy WM-ECO-011 Economic Asset view and WM-ACT-007 Work Order, with WM-OBJ-001 Physical Item, asset-lifecycle, measuring-instrument, maintenance, assessment and observation boundaries. Place AssetInstance, Custody, MaintenancePlan, MaintenanceEvent and CalibrationEvent. Decide which reuse/profile existing masters and which require independent identity/lifecycle; do not allocate identifiers. Separate physical identity, ownership/title, custody, operator/responsibility and location. Define component replacement and identity-continuity rules, planned maintenance versus authorization versus performed work, condition evidence, calibration method/reference/traceability/range/uncertainty/result/certificate/validity and fitness-for-use. Test a leased instrument, component replacement and expired calibration while preserving responsibility and suitability history. Reject the negative case that one instrument's successful calibration applies to every instrument of its model. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Asset and economic view; Custody and responsibility; Component replacement; Maintenance plan/order/event; Calibration event and certificate; Validity and fitness; Time/version/scenario; Acceptance scenario; Invariants; Minimal model set; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))



