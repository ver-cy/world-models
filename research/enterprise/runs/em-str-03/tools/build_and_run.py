import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R=W/"research/enterprise/runs/em-str-03"
IDS={"WM-ACT-001","WM-ACT-003","WM-ACT-034","WM-ORG-002","WM-ORG-003","WM-ORG-004","WM-KNW-011","WM-MAT-008"}

def j(p): return json.loads(p.read_text(encoding="utf-8-sig"))
def rows(p):
    with p.open(encoding="utf-8-sig",newline="") as h:return list(csv.DictReader(h))
def compact(p):
    raw=p.read_bytes();d=yaml.safe_load(raw.decode("utf-8-sig"));s=d.get("structure",{});bs=[]
    for b in s.get("bundles",[]):
        ls=[]
        for l in b.get("layers",[]):
            fs=[{k:v for k,v in f.items() if k not in {"questions","data_elements","artifacts","source_refs"}} for f in l.get("findings",[])]
            ls.append({k:v for k,v in l.items() if k not in {"findings","source_refs"}}|{"findings":fs})
        bs.append({k:v for k,v in b.items() if k not in {"layers","source_refs"}}|{"layers":ls})
    c={k:v for k,v in d.items() if k not in {"sources","structure"}}
    c["sources"]=[{k:x.get(k) for k in ("id","title","organization","version_or_date","source_type","primary_source","authority_tier")} for x in d.get("sources",[])]
    c["structure"]={k:v for k,v in s.items() if k!="bundles"}|{"bundles":bs}
    return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"document":c}
def td(p):
    raw=p.read_bytes();return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}

reg=j(W/"research/enterprise/registry.json");q=j(W/"research/enterprise/queue.json")
u=rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv");rel=rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
specs={
 "WM-ACT-034":"publications/wm-act-034-assessment-evaluation/spec.yaml",
 "WM-ORG-002":"publications/wm-org-002-organizational-unit/spec.yaml",
 "WM-ORG-003":"publications/wm-org-003-team/spec.yaml",
 "WM-ORG-004":"publications/wm-org-004-position/spec.yaml",
 "WM-KNW-011":"publications/wm-knw-011-goal-objective/spec.yaml",
 "WM-MAT-008":"publications/wm-mat-008-observation-measurement-record/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-STR-03"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-STR-03"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "legacy_specs":{
   "WM-ACT-001":td(W/"models/activity-work/K1-function-and-capability.md"),
   "WM-ACT-003":td(W/"models/activity-work/K3-process-and-workflow.md"),
 },
 "current_specs":{k:compact(W/v) for k,v in specs.items()},
 "prior_research":{
   "EM-STR-01":td(W/"research/enterprise/runs/em-str-01/local-evidence.md"),
   "EM-STR-02":td(W/"research/enterprise/runs/em-str-02/local-evidence.md"),
   "EM-LND-04":td(W/"research/enterprise/runs/em-lnd-04/local-evidence.md"),
   "EM-OPS-01":td(W/"research/enterprise/runs/em-ops-01/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True);p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-STR-03 Business Capability using the complete available WM-ACT-001 legacy Function / Capability specification and reservation, WM-ACT-003 legacy Process / Workflow, current WM-ACT-034 Assessment / Evaluation, WM-ORG-002 Organizational Unit, WM-ORG-003 Team, WM-ORG-004 Position, WM-KNW-011 Goal / Objective and WM-MAT-008 Observation / Measurement Record. Candidate types are BusinessCapability, CapabilityLevel, CapabilityAssessment and CapabilityRealization. Decide whether WM-ACT-001 can be completed/narrowed as the Business Capability master, should be split because it conflates individual skill/function/capacity, or should be retired in favor of a new candidate; do not allocate identifiers. Separate capability from function, process, organizational unit, team, position, product/service, resource and capacity. Define stable identity across reorganization, decomposition without org-chart taxonomy, required/actual level, maturity versus performance, assessment method and evidence, realization bindings, coverage/completeness, scenario state and time/version semantics. Test transfer of a process to another unit while capability identity stays stable and only realization changes. Reject department names as sole capability definitions and systems as full realizers. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Capability/function/process; Taxonomy/decomposition; Level/maturity/performance; Assessment/evidence; Realization/coverage; Organization/time/scenario; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide reuse/profile/split/retire and identify which candidates need independent identity. Do not claim canonical completeness, installability or publication readiness.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode:raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))
