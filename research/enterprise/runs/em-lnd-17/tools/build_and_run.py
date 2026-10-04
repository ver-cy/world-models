import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-17"
IDS = {"WM-BLT-006", "WM-BLT-008", "WM-BLT-001", "WM-OBJ-001", "WM-PLC-010", "WM-XCT-010", "WM-ACT-007"}

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
 "WM-BLT-006":"publications/wm-blt-006-facility/spec.yaml",
 "WM-BLT-008":"publications/wm-blt-008-site-campus/spec.yaml",
 "WM-BLT-001":"publications/wm-blt-001-building-structure/spec.yaml",
 "WM-OBJ-001":"publications/wm-obj-001-physical-item-instance/spec.yaml",
 "WM-PLC-010":"publications/wm-plc-010-gazetteer-place/spec.yaml",
 "WM-XCT-010":"publications/wm-xct-010-location-referencing-address/spec.yaml",
 "WM-ACT-007":"publications/wm-act-007-work-order/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-LND-17"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-LND-17"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "EM-FAC-01":td(W/"research/enterprise/runs/em-fac-01/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LND-17 Asset and Place Landscape using WM-BLT-006 Facility and WM-BLT-008 Site / Campus, with building, physical item, gazetteer place, address and work-order boundaries. Place AssetPlaceLandscape and OccupancyView and decide whether either needs independent identity or is a governed profile/projection. Keep place, site, facility, building, interior space and movable asset identities separate. Define effective-dated placement, custody, ownership, operational responsibility, occupancy/use, availability and maintenance relations, including planned versus observed location and uncertainty. Test a leased asset moving between two sites while ownership stays external, operational responsibility changes, maintenance is due, and history remains reconstructable. Reject the negative case that a company's registered address locates all its assets. Protect personal/home and sensitive asset location through derived views. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Spatial spine; Asset placement and responsibility; Planned versus observed; Occupancy and availability; Maintenance; Privacy and projections; Time/version/scenario; Acceptance scenario; Invariants; Minimal profile shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))

