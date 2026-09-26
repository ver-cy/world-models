import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-org-07"
IDS = {"WM-ORG-013", "WM-ORG-001", "WM-PER-001", "WM-ACT-034", "WM-ACT-008", "WM-KNW-007", "WM-KNW-010"}

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
 "WM-ORG-013":"publications/wm-org-013-stakeholder-interest/spec.yaml",
 "WM-ORG-001":"publications/wm-org-001-organization/spec.yaml",
 "WM-PER-001":"publications/wm-per-001-person/spec.yaml",
 "WM-ACT-034":"publications/wm-act-034-assessment-evaluation/spec.yaml",
 "WM-ACT-008":"publications/wm-act-008-plan-schedule/spec.yaml",
 "WM-KNW-007":"publications/wm-knw-007-claim-proposition/spec.yaml",
 "WM-KNW-010":"publications/wm-knw-010-decision-rationale/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-ORG-07"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-ORG-07"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "EM-ORG-01":td(W/"research/enterprise/runs/em-org-01/local-evidence.md"),
   "EM-DAT-07":td(W/"research/enterprise/runs/em-dat-07/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-ORG-07 Stakeholder and Engagement using WM-ORG-013 Stakeholder / Interest, with person, organization, assessment, plan, claim and decision boundaries. Place StakeholderInterest, EngagementPlan, Expectation and StakeholderAssessment. Decide reuse/profile/new by independent identity and lifecycle; do not allocate identifiers. Keep the person/organization subject separate from context-specific stakeholder participation. Bind every role, interest, influence, impact, expectation and engagement approach to a defined subject matter, decision/project perimeter, viewpoint, period and evidence. Treat influence/impact as dated assessments with method and uncertainty, not permanent traits. Allow conflicting interests and expectations. Define privacy, contestability, recusal/conflict-of-interest boundaries and update triggers when decision or perimeter changes. Test the same counterparty in two projects with different stakeholder maps and a reassessment that preserves basis/history. Reject global inheritance of a 'low influence' label. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Stakeholder context; Interest and expectation; Assessment; Engagement plan; Conflict and contestability; Privacy; Time/version/scenario; Acceptance scenario; Invariants; Minimal model set; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))





