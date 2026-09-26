import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-prd-04"
IDS = {"WM-ACT-022", "WM-KNW-009", "WM-ACT-036", "WM-KNW-007", "WM-KNW-008", "WM-MAT-008", "WM-DAT-001"}

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
 "WM-KNW-009":"publications/wm-knw-009-hypothesis/spec.yaml",
 "WM-ACT-036":"publications/wm-act-036-research-study/spec.yaml",
 "WM-KNW-007":"publications/wm-knw-007-claim-proposition/spec.yaml",
 "WM-KNW-008":"publications/wm-knw-008-evidence-citation/spec.yaml",
 "WM-MAT-008":"publications/wm-mat-008-observation-measurement-record/spec.yaml",
 "WM-DAT-001":"publications/wm-dat-001-dataset/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-PRD-04"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-PRD-04"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "EM-KNW-02":td(W/"research/enterprise/runs/em-knw-02/local-evidence.md"),
   "EM-DAT-03":td(W/"research/enterprise/runs/em-dat-03/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-PRD-04 Research, Hypothesis and Experiment using WM-ACT-036 Research Study, WM-KNW-009 Hypothesis and reserved-but-spec-missing WM-ACT-022 Experiment / Trial, with claim, citation/evidence, observation and dataset boundaries. Place ResearchStudy, Hypothesis, ExperimentDesign, ExperimentRun and ResearchFinding. Decide reuse/profile/new by independent identity and lifecycle; do not allocate identifiers. Define preregistered versus post-hoc hypotheses, immutable protocol/design versions, run manifests with exact inputs/environment/code/configuration/randomness, observations versus missing data, analysis method and result, finding/claim with uncertainty, applicability and limitations, negative/null/inconclusive outcomes, deviations, stopping rules and reproducibility. Test two runs of one design with different inputs and contradictory results, retaining failed run and original hypothesis. Reject deleting a failed experiment or rewriting the hypothesis after results. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Study/design/run; Hypothesis lifecycle; Inputs/provenance/reproduction; Observations/missingness; Analysis/finding; Null/negative/inconclusive; Time/version/scenario; Acceptance scenario; Invariants; Minimal model set; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))







