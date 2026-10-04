import json
from pathlib import Path
import yaml
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT=REPO/"research/enterprise/runs/em-leg-03/provider-dossier.json"
MODELS={
 "organization_policy":("wm-org-019-organization-policy",{"policy-identity-record","policy-approval-record","policy-scope-record","policy-applicability-record","policy-clauses-record","policy-precedence-record","policy-exceptions-record","policy-implementation-record","policy-release-record","policy-review-record","policy-mastership-record","policy-mapping-record"}),
 "policy_rule":("wm-knw-012-policy-rule",{"statement-identifier-and-naming","version-identity-and-point-in-time","deontic-modality-force-and-defeasibility","issuing-authority-and-mandate","subject-target-action-and-context-scope","rule-slot-inventory-and-atomicity","policy-set-containment-and-inheritance","constraint-expression-binding","combining-and-hit-policy-declaration","override-and-superiority-relations","derogation-and-waiver-declaration","declared-conflicts-and-alternatives","policy-lifecycle-state-model","amendment-supersession-and-repeal","validity-intervals-and-record-time"})}
def pick(d,ids):
 out=[]
 for b in d['structure']['bundles']:
  for l in b['layers']:
   for f in l['findings']:
    if f['id'] in ids: out.append({'bundle':{k:b.get(k) for k in ('id','name','description')},'layer':{k:l.get(k) for k in ('id','name','description')},'finding':f})
 missing=ids-{x['finding']['id'] for x in out}
 if missing: raise ValueError(sorted(missing))
 return out
def main():
 reg=json.loads((REPO/'research/enterprise/registry.json').read_text(encoding='utf-8'))
 dossier={'contour':next(x for x in reg['units'] if x['id']=='EM-LEG-03'),'registry_policy':{'reserved_candidates':['WM-ORG-019','WM-KNW-012'],'rule':'No new ID without independent identity/lifecycle and registry allocation.'},'models':{}}
 for label,(folder,ids) in MODELS.items():
  d=yaml.safe_load((REPO/'publications'/folder/'spec.yaml').read_text(encoding='utf-8'))
  dossier['models'][label]={'publication':d['publication'],'model':d['model'],'selected_findings':pick(d,ids),'functions':d.get('functions'),'composition':d.get('composition'),'researchAdjudication':d['researchAdjudication']}
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(OUT); print(OUT.stat().st_size)
if __name__=='__main__': main()
