import csv,hashlib,json,subprocess
from pathlib import Path
import yaml
W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");R=W/"research/enterprise/runs/em-lnd-15";IDS={"WM-XCT-027","WM-KNW-015","WM-ACT-033","WM-ACT-034","WM-KNW-012","WM-XCT-029","WM-MAT-008","WM-POL-001"}
def j(p):return json.loads(p.read_text(encoding="utf-8-sig"))
def rows(p):
 with p.open(encoding="utf-8-sig",newline="") as h:return list(csv.DictReader(h))
def compact(p):
 raw=p.read_bytes();d=yaml.safe_load(raw.decode("utf-8-sig"));s=d.get("structure",{});bs=[]
 for b in s.get("bundles",[]):
  ls=[]
  for l in b.get("layers",[]):
   fs=[{k:v for k,v in f.items() if k not in {"questions","data_elements","artifacts","source_refs"}} for f in l.get("findings",[])];ls.append({k:v for k,v in l.items() if k not in {"findings","source_refs"}}|{"findings":fs})
  bs.append({k:v for k,v in b.items() if k not in {"layers","source_refs"}}|{"layers":ls})
 c={k:v for k,v in d.items() if k not in {"sources","structure"}};c["sources"]=[{k:x.get(k) for k in ("id","title","organization","version_or_date","source_type","primary_source","authority_tier")} for x in d.get("sources",[])];c["structure"]={k:v for k,v in s.items() if k!="bundles"}|{"bundles":bs};return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"document":c}
def td(p):
 raw=p.read_bytes();return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}
reg=j(W/"research/enterprise/registry.json");q=j(W/"research/enterprise/queue.json");u=rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv");rel=rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
d={"contour":next(x for x in reg["units"] if x["id"]=="EM-LND-15"),"queue":next(x for x in q["units"] if x["id"]=="EM-LND-15"),"reservations":[x for x in u if x.get("model_id") in IDS],"relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],"specs":{"WM-XCT-027":compact(W/"publications/wm-xct-027-risk-control/spec.yaml"),"WM-KNW-015":compact(W/"publications/wm-knw-015-risk-opportunity/spec.yaml"),"WM-ACT-033":compact(W/"publications/wm-act-033-review-inspection-audit/spec.yaml"),"WM-ACT-034":compact(W/"publications/wm-act-034-assessment-evaluation/spec.yaml"),"WM-KNW-012":compact(W/"publications/wm-knw-012-policy-rule/spec.yaml"),"WM-XCT-029":compact(W/"publications/wm-xct-029-obligation-commitment/spec.yaml"),"WM-MAT-008":compact(W/"publications/wm-mat-008-observation-measurement-record/spec.yaml"),"WM-POL-001":compact(W/"publications/wm-pol-001-legal-instrument-norm/spec.yaml")},"prior_research":{"EM-RSK-01":td(W/"research/enterprise/runs/em-rsk-01/local-evidence.md"),"EM-DAT-07":td(W/"research/enterprise/runs/em-dat-07/local-evidence.md"),"EM-LEG-02":td(W/"research/enterprise/runs/em-leg-02/local-evidence.md")}}
R.mkdir(parents=True,exist_ok=True);p=R/"provider-dossier.json";p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LND-15 Risk and Compliance Landscape using WM-XCT-027 Risk Control, WM-KNW-015 Risk / Opportunity and WM-ACT-033 Review / Inspection / Audit plus assessment, requirement, obligation and observation boundaries. Place RiskLandscape and AssuranceCoverageView and decide whether either needs independent identity or is a governed profile/projection. Account for the identifier-unassigned Control candidate from EM-RSK-01 without allocating an ID. Define requirement applicability, risk/control/assessment/audit/finding/evidence links, coverage denominator, effectiveness versus existence/design/implementation/operation, exception/waiver expiry and conclusion validity. Detect a control without execution, a requirement without applicability and an expired exception. Separate coverage, compliance, assurance and residual risk; reject 100% completed cards as proof. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Scope and requirements; Risk/control boundary; Coverage and effectiveness; Assessments/audits/findings; Exceptions and validity; Time/scenario; Scenario; Invariants; Minimal profile shape; Holds. Do not claim legal advice, canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode:raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8");print(p.stat().st_size,len(r.stdout))
