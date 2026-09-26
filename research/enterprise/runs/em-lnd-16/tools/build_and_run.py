import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-16"
IDS = {"WM-KNW-006", "WM-KNW-010", "WM-REC-001", "WM-KNW-007", "WM-KNW-008", "WM-REC-010", "WM-KNW-018"}

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
 "WM-KNW-006":"publications/wm-knw-006-concept-term/spec.yaml",
 "WM-KNW-010":"publications/wm-knw-010-decision-rationale/spec.yaml",
 "WM-REC-001":"publications/wm-rec-001-document-record/spec.yaml",
 "WM-KNW-007":"publications/wm-knw-007-claim-proposition/spec.yaml",
 "WM-KNW-008":"publications/wm-knw-008-evidence-citation/spec.yaml",
 "WM-REC-010":"publications/wm-rec-010-decision-approval-record/spec.yaml",
 "WM-KNW-018":"publications/wm-knw-018-taxonomy-classification-scheme/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-LND-16"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-LND-16"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "EM-KNW-01":td(W/"research/enterprise/runs/em-knw-01/local-evidence.md"),
   "EM-KNW-02":td(W/"research/enterprise/runs/em-knw-02/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LND-16 Knowledge and Decision Landscape using WM-KNW-006 Concept / Term, WM-KNW-010 Decision / Rationale and WM-REC-001 Document / Record, with claim, citation, decision-record and concept-scheme boundaries. Place KnowledgeLandscape and DecisionDependencyView and decide whether either needs independent identity or is a governed profile/projection. Define semantic links among documents, concepts, claims, citations, evidence sources, decisions and fixed records while preserving each master. Explain impact propagation when a shared source is retracted or a claim is rebutted, incompatible meanings for equal labels, missing-source detection, rights-preserving indexing, redaction and inference non-disclosure. Test the negative case where a search summary leaks restricted correspondence. Distinguish semantic relation from identity/equality and evidence from truth. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Semantic graph; Decisions and impact; Terminology conflict; Missing source and uncertainty; Rights and projections; Time/version/scenario; Acceptance scenario; Invariants; Minimal profile shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))
