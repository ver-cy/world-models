import csv, hashlib, json, subprocess
from pathlib import Path
import yaml
W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");R=W/"research/enterprise/runs/em-tec-10"
IDS={"WM-ACT-032","WM-ACT-008","WM-ORG-016","WM-SFT-008","WM-SFT-009","WM-KNW-012","WM-KNW-010","WM-ACT-024","WM-REC-010","WM-ACT-006"}
def j(p):return json.loads(p.read_text(encoding="utf-8-sig"))
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
    c={k:v for k,v in d.items() if k not in {"sources","structure"}};c["sources"]=[{k:x.get(k) for k in ("id","title","organization","version_or_date","source_type","primary_source","authority_tier")} for x in d.get("sources",[])];c["structure"]={k:v for k,v in s.items() if k!="bundles"}|{"bundles":bs};return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"document":c}
def td(p):
    raw=p.read_bytes();return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}
reg=j(W/"research/enterprise/registry.json");q=j(W/"research/enterprise/queue.json");u=rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv");rel=rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
specs={"WM-ACT-032":"publications/wm-act-032-change-request/spec.yaml","WM-ACT-008":"publications/wm-act-008-plan-schedule/spec.yaml","WM-ORG-016":"publications/wm-org-016-work-assignment/spec.yaml","WM-SFT-008":"publications/wm-sft-008-build-release/spec.yaml","WM-SFT-009":"publications/wm-sft-009-deployment/spec.yaml","WM-KNW-012":"publications/wm-knw-012-policy-rule/spec.yaml","WM-KNW-010":"publications/wm-knw-010-decision-rationale/spec.yaml","WM-ACT-024":"publications/wm-act-024-decision-approval-activity/spec.yaml","WM-REC-010":"publications/wm-rec-010-decision-approval-record/spec.yaml","WM-ACT-006":"publications/wm-act-006-task/spec.yaml"}
d={"contour":next(x for x in reg["units"] if x["id"]=="EM-TEC-10"),"queue":next(x for x in q["units"] if x["id"]=="EM-TEC-10"),"reservations":[x for x in u if x.get("model_id") in IDS],"relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],"specs":{k:compact(W/v) for k,v in specs.items()},"prior_research":{"EM-WRK-02":td(W/"research/enterprise/runs/em-wrk-02/local-evidence.md"),"EM-PEO-07":td(W/"research/enterprise/runs/em-peo-07/local-evidence.md"),"EM-ORG-06":td(W/"research/enterprise/runs/em-org-06/local-evidence.md"),"EM-TEC-04":td(W/"research/enterprise/runs/em-tec-04/local-evidence.md"),"EM-TEC-05":td(W/"research/enterprise/runs/em-tec-05/local-evidence.md")}}
R.mkdir(parents=True,exist_ok=True);p=R/"provider-dossier.json";p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-TEC-10 Operational Change and On-call Duty. Candidate types are OperationalChange, ChangeWindow, ChangeExecution, RollbackPlan, DutyRoster and EscalationRule. Complete adjacent drafts cover Change Request, Plan/Schedule, Work Assignment, Build/Release, Deployment, Policy/Rule, the decision triad and Task. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate request/proposal from approval and execution; release from deployment/change; approved revision from execution occurrence; change window from authorization; rollback intent/plan from rollback execution and verified state; duty roster from work assignment, person, role and IAM grant; escalation rule from alert/event and authority. Define time zones/DST, overlapping windows, freeze periods, emergency change, handover, substitute/override, acknowledgment, audit evidence, rollback trigger, partial/failed rollout and post-change verification. Test one change with two windows, failed rollout, evidenced rollback and on-call handover. Reject automatic administrative rights from roster membership. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Request/decision/change; Window/schedule; Execution/deployment/rollback; Duty roster/assignment; Escalation/IAM; Time/version/handover; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps/contradictions. Do not claim canonical completeness, installability or publication readiness.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode:raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8");print(p.stat().st_size,len(r.stdout))
