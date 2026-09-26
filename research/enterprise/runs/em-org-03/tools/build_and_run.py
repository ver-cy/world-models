import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-org-03"
IDS = {"WM-ORG-018", "WM-ORG-012", "WM-ECO-038", "WM-ORG-001", "WM-ORG-006", "WM-ACT-025", "WM-KNW-010", "WM-REC-010", "WM-ORG-007"}

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
 "WM-ORG-018":"publications/wm-org-018-governance-body-committee/spec.yaml",
 "WM-ORG-012":"publications/wm-org-012-inter-organizational-relationship/spec.yaml",
 "WM-ECO-038":"publications/wm-eco-038-equity-security-holding/spec.yaml",
 "WM-ORG-001":"publications/wm-org-001-organization/spec.yaml",
 "WM-ORG-006":"publications/wm-org-006-membership/spec.yaml",
 "WM-ACT-025":"publications/wm-act-025-meeting-session/spec.yaml",
 "WM-KNW-010":"publications/wm-knw-010-decision-rationale/spec.yaml",
 "WM-REC-010":"publications/wm-rec-010-decision-approval-record/spec.yaml",
}
d={
 "contour":next(x for x in reg["units"] if x["id"]=="EM-ORG-03"),
 "queue":next(x for x in q["units"] if x["id"]=="EM-ORG-03"),
 "reservations":[x for x in u if x.get("model_id") in IDS],
 "relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
 "specs":{k:compact(W/v) for k,v in spec_paths.items()},
 "prior_research":{
   "WM-ORG-007 legacy complete document":td(W/"models/organizations/O4-organizational-mandate-and-charter.md"),
   "EM-ORG-01":td(W/"research/enterprise/runs/em-org-01/local-evidence.md"),
   "EM-ORG-02":td(W/"research/enterprise/runs/em-org-02/local-evidence.md"),
   "EM-KNW-02":td(W/"research/enterprise/runs/em-knw-02/local-evidence.md"),
 }
}
R.mkdir(parents=True,exist_ok=True); p=R/"provider-dossier.json"
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-ORG-03 Ownership, Control and Corporate Governance using WM-ORG-018 Governance Body, WM-ORG-012 Inter-organizational Relationship and WM-ECO-038 Equity / Security Holding, with organization, membership, meeting, decision and authentic-record boundaries. Place OwnershipInterest, ShareClass, ControlRelation, GovernanceBody, Mandate and Resolution. Decide reuse/profile/new by independent identity and lifecycle; do not allocate identifiers. Separate economic interest, capital rights, voting rights, contractual control, de facto control and accounting consolidation. Define direct and indirect ownership/control calculations with multiple share classes, cross-holdings, treasury holdings, denominator/time/scenario, and no automatic inference from economic share to voting or signing authority. Define mandate, appointments, membership terms, quorum, recusals, voting rules, meeting evidence, decision and fixed resolution. Test two share classes, cross-ownership, a board membership change and a resolution adopted without quorum. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Ownership and share class; Control and consolidation; Indirect calculations; Governance body and membership; Mandate/quorum/voting; Resolution and authority; Time/version/scenario; Acceptance scenario; Invariants; Minimal model set; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8")
print(p.stat().st_size,len(r.stdout))




