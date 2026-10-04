import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-peo-07"
IDS = {"WM-ACT-008", "WM-XCT-009", "WM-PER-001", "WM-ORG-005", "WM-ORG-016", "WM-ACT-006", "WM-MAT-008"}

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
 "WM-ACT-008":"publications/wm-act-008-plan-schedule/spec.yaml",
 "WM-XCT-009":"publications/wm-xct-009-time-calendar/spec.yaml",
 "WM-PER-001":"publications/wm-per-001-person/spec.yaml",
 "WM-ORG-005":"publications/wm-org-005-employment/spec.yaml",
 "WM-ORG-016":"publications/wm-org-016-work-assignment/spec.yaml",
 "WM-ACT-006":"publications/wm-act-006-task/spec.yaml",
 "WM-MAT-008":"publications/wm-mat-008-observation-measurement-record/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-PEO-07"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-PEO-07"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "EM-PEO-02":td(W/"research/enterprise/runs/em-peo-02/local-evidence.md"),
   "EM-WRK-01":td(W/"research/enterprise/runs/em-wrk-01/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-PEO-07 Availability and Time Accounting using WM-ACT-008 Plan / Schedule, with time/calendar, person, employment, work-assignment, task and observation boundaries. Place WorkCalendar, Absence, Availability, Worklog, Timesheet and TimeApproval. Decide reuse/profile/new by independent identity and lifecycle; do not allocate identifiers. Separate contractual work pattern, calendar rules, absence, planned availability, assignment/allocation, actual work record and approved timesheet. Define time-zone/DST handling, partial FTE/day, overlapping entries, corrections, units/precision, approval and privacy. Keep medical reason outside ordinary availability. Treat missing record as unknown, not zero. Test a DST transition, half-time engagement, two projects and corrected timesheet without negative or double capacity. Reject worklog as proof of presence, productivity or quality. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Calendar and work pattern; Absence and privacy; Availability/capacity/allocation; Worklog; Timesheet and approval; Time-zone/DST/overlap; Correction and audit; Acceptance scenario; Invariants; Minimal model set; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))






