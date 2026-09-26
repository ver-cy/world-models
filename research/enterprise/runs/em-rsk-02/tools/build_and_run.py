import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-rsk-02"
IDS = {"WM-ACT-033", "WM-ECO-035", "WM-KNW-014", "WM-ACT-034", "WM-KNW-007", "WM-ACT-006", "WM-KNW-012", "WM-XCT-027"}

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
 "WM-ACT-033":"publications/wm-act-033-review-inspection-audit/spec.yaml",
 "WM-ECO-035":"publications/wm-eco-035-audit-assurance-engagement/spec.yaml",
 "WM-KNW-014":"publications/wm-knw-014-issue-problem/spec.yaml",
 "WM-ACT-034":"publications/wm-act-034-assessment-evaluation/spec.yaml",
 "WM-KNW-007":"publications/wm-knw-007-claim-proposition/spec.yaml",
 "WM-ACT-006":"publications/wm-act-006-task/spec.yaml",
 "WM-KNW-012":"publications/wm-knw-012-policy-rule/spec.yaml",
 "WM-XCT-027":"publications/wm-xct-027-risk-control/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-RSK-02"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-RSK-02"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "EM-RSK-01":td(W/"research/enterprise/runs/em-rsk-01/local-evidence.md"),
   "EM-LND-15":td(W/"research/enterprise/runs/em-lnd-15/local-evidence.md"),
   "EM-WRK-01":td(W/"research/enterprise/runs/em-wrk-01/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-RSK-02 Audit, Review and Finding using WM-ACT-033 Review / Inspection / Audit, WM-ECO-035 Audit / Assurance Engagement and WM-KNW-014 Issue / Problem, with assessment, claim, task, rule and risk/control boundaries. Place Audit, AuditProcedure, AuditFinding, AssuranceOpinion and CorrectiveAction. Decide reuse/profile/new by independent identity and lifecycle; do not allocate identifiers. Separate engagement/mandate from execution, procedure from performed test, observation/evidence from finding, finding from risk/issue/task, management response from corrective action, task completion from finding closure, and assurance opinion from general compliance. Define pinned criteria, population/sampling frame/method/sample/limitations, independence/competence, scope/exclusions, materiality/severity, root-cause claim, remediation, re-test and independent closure verification. Test two processes with one excluded site and a finding retested after corrective action. Reject extrapolating one-system evidence to group-wide conformity. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Engagement/audit/procedure; Sampling and evidence; Finding/issue/risk; Opinion and scope; Corrective action and closure; Independence; Time/version/scenario; Acceptance scenario; Invariants; Minimal model set; Holds. Do not claim legal advice, canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))
