import json
from pathlib import Path
import yaml
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT=REPO/"research/enterprise/runs/em-leg-01/provider-dossier.json"
MODELS={
 "contract":("wm-eco-006-commercial-contract",{"agreement-record-identity","party-position-and-role","party-legal-identification","signing-authority-and-capacity","offer-acceptance-and-conclusion","execution-signature-and-form","effectiveness-conditions-and-validity","clause-addressability","obligation-deontic-specification","milestone-and-due-condition","performance-record-and-acceptance","breach-excuse-and-remedy","amendment-and-variation","assignment-and-novation","termination-expiry-and-survival"}),
 "obligation":("wm-xct-029-obligation-commitment",{"obligation-identity","deontic-modality","obligor-bearer","obligee-beneficiary","obligated-action","antecedent-and-detachment","performance-standard","quantification-and-progress","due-time-and-window","lifecycle-state-machine","fulfilment-and-acceptance","fulfilment-evidence","breach-determination","excuse-remedy-consequence","source-and-authority","assignment-and-novation"})}
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
 dossier={'contour':next(x for x in reg['units'] if x['id']=='EM-LEG-01'),'related_registry':{'service_level_reserved':{'registry_id':'vr.wm-sft-016','model_id':'WM-SFT-016','name':'Service Level / SLO','status':'candidate','review_state':'boundary-review-required'}},'registry_policy':{'reserved_candidates':['WM-ECO-006','WM-XCT-029'],'rule':'No new ID without independent identity/lifecycle and registry allocation.'},'models':{}}
 for label,(folder,ids) in MODELS.items():
  d=yaml.safe_load((REPO/'publications'/folder/'spec.yaml').read_text(encoding='utf-8'))
  dossier['models'][label]={'publication':d['publication'],'model':d['model'],'selected_findings':pick(d,ids),'functions':d.get('functions'),'composition':d.get('composition'),'researchAdjudication':d['researchAdjudication']}
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(OUT); print(OUT.stat().st_size)
if __name__=='__main__': main()
