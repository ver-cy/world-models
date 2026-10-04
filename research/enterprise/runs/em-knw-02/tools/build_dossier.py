import json
from pathlib import Path
import yaml

REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT = REPO / "research/enterprise/runs/em-knw-02/provider-dossier.json"
MODELS = {
 "decision": ("wm-knw-010-decision-rationale", {"dr-core-identity","dr-core-question","dr-core-alternative-set","dr-core-evaluation-results","dr-core-selection","dr-rsn-finding-rationale-statement","dr-rsn-finding-argument-structure","dr-rsn-finding-claim-binding","dr-rsn-finding-evidence-citation","dr-rsn-finding-counterargument-dissent","dr-gov-fnd-approval-binding","dr-gov-fnd-status-validity","dr-gov-fnd-review-appeal-reopening"}),
 "decision_record": ("wm-rec-010-decision-approval-record", {"f01-decision-identifier","f02-version-and-expression-identity","f05-matter-under-decision","f06-outcome-and-disposition","f08-statement-of-reasons","f09-options-considered","f10-evidence-and-findings","f11-authority-and-legal-basis","f15-attestation-and-integrity-evidence","f18-status-model-and-finality","f19-supersession-and-revocation","f20-challenge-and-annulment"}),
 "claim": ("wm-knw-007-claim-proposition", {"canonical-statement","claim-identifier","subject-and-population-scope","conditions-assumptions-and-defeaters","claimant-and-assertion-act","conflict-and-contradiction","preference-and-supersession","evidence-link-binding","argument-structure-role-reference","status-and-state-transitions","retraction-correction-and-status-notices"}),
 "citation": ("wm-knw-008-evidence-citation", {"citation-record-identity","citing-context-binding","stance-and-intent","evidence-type-and-method","anchor-selectors","resource-state-binding","certainty-and-limitations","contested-and-counter-evidence","cited-source-status-observation","verification-record","lifecycle-states","supersession-and-versioning"}),
}

def pick(d, ids):
 out=[]
 for b in d["structure"]["bundles"]:
  for l in b["layers"]:
   for f in l["findings"]:
    if f["id"] in ids: out.append({"bundle":{k:b.get(k) for k in ("id","name","description")},"layer":{k:l.get(k) for k in ("id","name","description")},"finding":f})
 missing=ids-{x["finding"]["id"] for x in out}
 if missing: raise ValueError(sorted(missing))
 return out

def main():
 reg=json.loads((REPO/"research/enterprise/registry.json").read_text(encoding="utf-8"))
 dossier={"contour":next(x for x in reg["units"] if x["id"]=="EM-KNW-02"),"registry_policy":{"reserved_candidates":["WM-KNW-010","WM-REC-010","WM-KNW-007","WM-KNW-008"],"rule":"No new ID without independent identity/lifecycle and registry allocation."},"models":{}}
 for label,(folder,ids) in MODELS.items():
  d=yaml.safe_load((REPO/"publications"/folder/"spec.yaml").read_text(encoding="utf-8"))
  dossier["models"][label]={"publication":d["publication"],"model":d["model"],"selected_findings":pick(d,ids),"functions":d.get("functions"),"composition":d.get("composition"),"researchAdjudication":d["researchAdjudication"]}
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(OUT); print(OUT.stat().st_size)

if __name__=="__main__": main()
