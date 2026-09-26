import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R=W/"research/enterprise/runs/em-str-04"
IDS={"WM-ACT-030","WM-ACT-005","WM-ACT-029","WM-KNW-009","WM-KNW-010","WM-KNW-015","WM-KNW-016","WM-ACT-024","WM-REC-010","WM-ECO-012"}
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
    c={k:v for k,v in d.items() if k not in {"sources","structure"}}
    c["sources"]=[{k:x.get(k) for k in ("id","title","organization","version_or_date","source_type","primary_source","authority_tier")} for x in d.get("sources",[])]
    c["structure"]={k:v for k,v in s.items() if k!="bundles"}|{"bundles":bs}
    return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"document":c}
def td(p):
    raw=p.read_bytes();return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}
reg=j(W/"research/enterprise/registry.json");q=j(W/"research/enterprise/queue.json")
u=rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv");rel=rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
specs={
 "WM-ACT-030":"publications/wm-act-030-initiative/spec.yaml",
 "WM-ACT-005":"publications/wm-act-005-project/spec.yaml",
 "WM-ACT-029":"publications/wm-act-029-program-portfolio/spec.yaml",
 "WM-KNW-009":"publications/wm-knw-009-hypothesis/spec.yaml",
 "WM-KNW-010":"publications/wm-knw-010-decision-rationale/spec.yaml",
 "WM-KNW-015":"publications/wm-knw-015-risk-opportunity/spec.yaml",
 "WM-KNW-016":"publications/wm-knw-016-assumption/spec.yaml",
 "WM-ACT-024":"publications/wm-act-024-decision-approval-activity/spec.yaml",
 "WM-REC-010":"publications/wm-rec-010-decision-approval-record/spec.yaml",
 "WM-ECO-012":"publications/wm-eco-012-budget/spec.yaml",
}
d={"contour":next(x for x in reg["units"] if x["id"]=="EM-STR-04"),"queue":next(x for x in q["units"] if x["id"]=="EM-STR-04"),"reservations":[x for x in u if x.get("model_id") in IDS],"relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],"specs":{k:compact(W/v) for k,v in specs.items()},"prior_research":{"EM-STR-01":td(W/"research/enterprise/runs/em-str-01/local-evidence.md"),"EM-STR-02":td(W/"research/enterprise/runs/em-str-02/local-evidence.md"),"EM-WRK-02":td(W/"research/enterprise/runs/em-wrk-02/local-evidence.md"),"EM-FIN-01":td(W/"research/enterprise/runs/em-fin-01/local-evidence.md")}}
R.mkdir(parents=True,exist_ok=True);p=R/"provider-dossier.json";p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-STR-04 Initiative and Investment Rationale using complete WM-ACT-030 Initiative and adjacent Project, Program/Portfolio, Hypothesis, Assumption, Decision/Rationale, Decision Activity, Decision Record, Risk/Opportunity and Budget specifications. Candidate types are Initiative, BusinessCase, Alternative, Assumption and InvestmentDecision; also clarify Hypothesis and Mandate. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate initiative from idea/request/ticket/project/program/portfolio and operational work; business case release from initiative identity; alternative from decision rationale; assumption from hypothesis and forecast; decision rationale from approval occurrence, issued record and mandate; approval/funding from project creation and benefit realization. Define fair alternative comparison, baseline and do-nothing option, uncertainty and range handling, expected benefit/risk/cost references, review triggers, validity and supersession. Test two alternatives sharing one expected benefit but with different risks and a changed forecast; preserve a rejected initiative and reproduce the decision as-of date. Reject automatic project creation from a ticket or approval. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Initiative transition; Business case; Alternative/assumption/hypothesis; Decision/mandate/funding; Benefits/risks/costs; Time/version/review; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates are roots, profiles, contained records or references. Do not claim canonical completeness, installability or publication readiness.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode:raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))
