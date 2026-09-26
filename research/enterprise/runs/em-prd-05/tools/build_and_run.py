import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-prd-05"
IDS = {"WM-KNW-003", "WM-MED-001", "WM-ECO-006", "WM-XCT-029", "WM-REC-001", "WM-ORG-001", "WM-PER-001"}

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
 "WM-ECO-006":"publications/wm-eco-006-commercial-contract/spec.yaml",
 "WM-XCT-029":"publications/wm-xct-029-obligation-commitment/spec.yaml",
 "WM-REC-001":"publications/wm-rec-001-document-record/spec.yaml",
 "WM-ORG-001":"publications/wm-org-001-organization/spec.yaml",
 "WM-PER-001":"publications/wm-per-001-person/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-PRD-05"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-PRD-05"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "WM-KNW-003 legacy complete document":td(W/"models/knowledge-information/N12-intellectual-property.md"),
   "WM-MED-001 legacy complete document":td(W/"models/knowledge-information/N5-media-and-creative-work.md"),
   "EM-LEG-01":td(W/"research/enterprise/runs/em-leg-01/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-PRD-05 Intellectual Property and Usage Rights using legacy WM-KNW-003 Intellectual Property Right, with creative work, contract, obligation, record, organization and person boundaries. Place IPAsset, IPRegistration, RightsClaim and UsageGrant. Decide reuse/profile/new by independent identity and lifecycle; do not allocate identifiers. Separate protected subject/work from right, application, territorial registration, ownership/right-holder assertion, creator attribution, evidence, assignment and licensed use. Model jurisdiction/territory, right kind, filing/priority/grant/renewal/expiry/revocation, scope and status. Treat brand/business association separately from trademark registration. Define exclusive/non-exclusive, sublicensing, field-of-use, channel, territory, term, permitted/prohibited acts and surviving obligations. Test one brand with two territorial registrations and a license expiring before one registration. Reject inferring worldwide exclusive rights from a company logo. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; IP asset/right; Application and registration; Rights claim/ownership; Usage grant/license; Territory/time/status; Brand versus trademark; Transfer/sublicense/obligation; Acceptance scenario; Invariants; Minimal model set; Holds. Do not claim legal advice, canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))








