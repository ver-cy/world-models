import csv, hashlib, json, subprocess
from pathlib import Path
import yaml
W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");R=W/"research/enterprise/runs/em-tec-07"
IDS={"WM-SFT-006","WM-SFT-007","WM-SFT-008","WM-SFT-009","WM-SFT-012","WM-ACT-006","WM-ACT-034","WM-KNW-007","WM-ACT-020"}
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
    c={k:v for k,v in d.items() if k not in {"sources","structure"}};c["sources"]=[{k:x.get(k) for k in ("id","title","organization","version_or_date","source_type","primary_source","authority_tier")} for x in d.get("sources",[])];c["structure"]={k:v for k,v in s.items() if k!="bundles"}|{"bundles":bs}
    return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"document":c}
def td(p):
    raw=p.read_bytes();return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"content":raw.decode("utf-8-sig")}
reg=j(W/"research/enterprise/registry.json");q=j(W/"research/enterprise/queue.json");u=rows(W/"planning/VERCY-UNIFIED-MEGA-REGISTRY.csv");rel=rows(W/"planning/VERCY-MODEL-RELATIONS.csv")
specs={"WM-SFT-006":"publications/wm-sft-006-vulnerability-record/spec.yaml","WM-SFT-007":"publications/wm-sft-007-software-component-package/spec.yaml","WM-SFT-008":"publications/wm-sft-008-build-release/spec.yaml","WM-SFT-009":"publications/wm-sft-009-deployment/spec.yaml","WM-SFT-012":"publications/wm-sft-012-sbom-supply-chain-manifest/spec.yaml","WM-ACT-006":"publications/wm-act-006-task/spec.yaml","WM-ACT-034":"publications/wm-act-034-assessment-evaluation/spec.yaml","WM-KNW-007":"publications/wm-knw-007-claim-proposition/spec.yaml","WM-ACT-020":"publications/wm-act-020-cyber-incident/spec.yaml"}
d={"contour":next(x for x in reg["units"] if x["id"]=="EM-TEC-07"),"queue":next(x for x in q["units"] if x["id"]=="EM-TEC-07"),"reservations":[x for x in u if x.get("model_id") in IDS],"relations":[x for x in rel if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],"publication":j(W/"publications/wm-sft-006-vulnerability-record/publication.json"),"specs":{k:compact(W/v) for k,v in specs.items()},"prior_research":{"EM-TEC-01":td(W/"research/enterprise/runs/em-tec-01/local-evidence.md"),"EM-TEC-02":td(W/"research/enterprise/runs/em-tec-02/local-evidence.md"),"EM-TEC-04":td(W/"research/enterprise/runs/em-tec-04/local-evidence.md"),"EM-TEC-05":td(W/"research/enterprise/runs/em-tec-05/local-evidence.md"),"EM-RSK-01":td(W/"research/enterprise/runs/em-rsk-01/local-evidence.md")}}
R.mkdir(parents=True,exist_ok=True);p=R/"provider-dossier.json";p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
prompt="""Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-TEC-07 Vulnerability, Affectedness and Remediation using complete WM-SFT-006 plus current component/package, build/release, deployment, SBOM, task, assessment, claim and cyber-incident drafts. Candidate types are Vulnerability, AffectednessAssessment, Remediation and ExploitEvidence. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate source-qualified vulnerability identity from weakness and advisory; product/package version affectedness from deployed-instance exposure; generic severity from environmental risk and priority; public exploit signal from exploit artifact/evidence and from an incident; fix availability/build inclusion/deployment/instance verification; remediation work from closure evidence. Define version/configuration conditions, VEX-like statuses, transitive dependency reachability, SBOM and runtime evidence, time/knowledge semantics, supersession and privacy. Test a conditionally affected component, a fixed build and one still-unupdated instance. Reject claims that a CVE in a transitive dependency proves exploitability or incident, and that a closed ticket proves remediation. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Vulnerability/advisory/weakness; Affectedness/exposure; Severity/risk/priority; Exploit evidence/incident; Fix/remediation/verification; Time/version/scenario; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates are roots, profiles, contained records or references, and identify specification contradictions/gaps. Do not claim canonical completeness, installability or publication readiness.\n\nDOSSIER\n"""+p.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode:raise SystemExit((r.stderr or r.stdout or f"claude exit {r.returncode}").strip())
(R/"claude-study.raw.md").write_text(r.stdout.rstrip()+"\n",encoding="utf-8");print(p.stat().st_size,len(r.stdout))
