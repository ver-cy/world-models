import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-rsk-04"
IDS = {"WM-ACT-043"}

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
spec=W/"publications/wm-act-043-business-continuity-recovery/spec.yaml"
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-RSK-04"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-RSK-04"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "publication":j(W/"publications/wm-act-043-business-continuity-recovery/publication.json"),
 "spec":{"WM-ACT-043":compact(spec)},
 "prior_research":{
   "EM-TEC-06":td(W/"research/enterprise/runs/em-tec-06/local-evidence.md"),
   "EM-LND-12":td(W/"research/enterprise/runs/em-lnd-12/local-evidence.md"),
   "EM-LND-17":td(W/"research/enterprise/runs/em-lnd-17/local-evidence.md"),
   "EM-RSK-02":td(W/"research/enterprise/runs/em-rsk-02/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-RSK-04 Business Continuity, Backup and Recovery using the complete WM-ACT-043 Business Continuity / Recovery specification and its reservation. Place BusinessImpactAnalysis, ContinuityPlan, BackupPolicy, RestoreTest and RecoveryEvidence by independent identity and lifecycle; do not allocate identifiers. Test whether the five candidates are aggregate-owned records/profiles or independent models. Separate business impact tolerance from RTO/RPO targets, dependency order from inventory, backup execution from restore proof, exercise from real activation, recovery from reconstitution, and readiness assertions from observed outcomes. Define authoritative targets, scope and version pins, recovery dependency graph, test design, synthetic data, evidence integrity, partial failure, time semantics, access protection and closure rules. Test restoration of a synthetic service chain where one dependency is unavailable; reject the claim that a green backup job proves RTO, RPO or recoverability. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; BIA and objectives; Plans and policies; Backup versus restore; Exercises and real events; Dependencies and ordering; Evidence and time; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide if any candidate needs a new model identity and identify specification gaps or contradictions. Do not claim standards conformance, canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))
