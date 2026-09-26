import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-str-01"
IDS = {"WM-KNW-011","WM-ACT-030","WM-KNW-010","WM-ACT-024","WM-REC-010","WM-ACT-001","WM-ACT-003"}

def j(p): return json.loads(p.read_text(encoding="utf-8-sig"))
def rows(p):
    with p.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def compact(p):
    raw=p.read_bytes(); d=yaml.safe_load(raw.decode("utf-8-sig")); s=d.get("structure",{}); bs=[]
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
    raw=p.read_bytes(); return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}

reg=j(W/"research/enterprise/registry.json"); q=j(W/"research/enterprise/queue.json")
u=rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv"); rel=rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
specs={
 "WM-KNW-011":"publications/wm-knw-011-goal-objective/spec.yaml",
 "WM-ACT-030":"publications/wm-act-030-initiative/spec.yaml",
 "WM-KNW-010":"publications/wm-knw-010-decision-rationale/spec.yaml",
 "WM-ACT-024":"publications/wm-act-024-decision-approval-activity/spec.yaml",
 "WM-REC-010":"publications/wm-rec-010-decision-approval-record/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-STR-01"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-STR-01"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "current_specs":{k:compact(W/v) for k,v in specs.items()},
 "legacy_boundaries":{
   "WM-ACT-001":td(W/"models/activity-work/K1-function-and-capability.md"),
   "WM-ACT-003":td(W/"models/activity-work/K3-process-and-workflow.md"),
 },
 "prior_research":{
   "EM-STR-02":td(W/"research/enterprise/runs/em-str-02/local-evidence.md"),
   "EM-LND-04":td(W/"research/enterprise/runs/em-lnd-04/local-evidence.md"),
   "EM-LND-05":td(W/"research/enterprise/runs/em-lnd-05/local-evidence.md"),
   "EM-KNW-02":td(W/"research/enterprise/runs/em-knw-02/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-STR-01 Strategy, Business Model and Value Streams. Candidate types are Strategy, BusinessModel, StrategicTheme, ValueProposition, ValueStream and StrategicScenario. Current complete adjacent specifications cover WM-KNW-011 Goal/Objective, WM-ACT-030 Initiative, WM-KNW-010 Decision/Rationale, WM-ACT-024 Decision/Approval Activity and WM-REC-010 Decision/Approval Record; WM-ACT-001 Capability and WM-ACT-003 Process/Workflow are legacy-only. Outcome and Benefit Realization is already an identifier-unassigned candidate from EM-STR-02. Determine reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate mission and policy from strategic choice, strategy from plan/initiative/portfolio, value proposition from offer, value stream from process, business model from organization, hypothesis from fact, forecast from outcome, and authoritative actuals from strategic scenarios. Define recipients, markets, choices, assumptions, causal hypotheses, value mechanism, stages, capabilities, measures, review triggers, horizon, versioning, scenario isolation and decision authority. Test a startup and a multi-industry group after a channel or segment change. Reject a project list labelled strategy. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Strategy and themes; Business model and value proposition; Value stream versus process; Scenario and hypothesis; Objectives/capabilities/initiatives/decisions; Time/version/review; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates require independent model identity, which are profiles/contained records, and which stay blocked by missing specifications or registry allocation. Do not claim canonical completeness, installability or publication readiness.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))
