import json
from pathlib import Path
import yaml
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT=REPO/"research/enterprise/runs/em-lnd-01/provider-dossier.json"
MODELS={
 'unit':('wm-org-002-organizational-unit',{'unit-identifier-scheme','unit-kind-classification','parent-child-containment','concurrent-hierarchies','reporting-lines','cross-unit-affiliations','reorganization-act','unit-lineage','effective-dating-bitemporality','as-of-reconstruction'}),
 'team':('wm-org-003-team',{'team-identifier-assignment','team-boundary-and-entity-distinction','containing-and-managing-organization','team-charter-and-mandate','decision-rights-ownership-and-reporting-line','membership-assignment-record','role-and-position-binding','nesting-and-inherited-membership','team-status-lifecycle','effective-dating-and-time-semantics','formation-and-dissolution','merge-split-and-transfer-events'}),
 'position':('wm-org-004-position',{'position-identifier-and-keys','unit-and-cost-center-placement','reporting-and-supervisory-relations','vacancy-and-occupancy-state','position-lifecycle-states','effective-dated-change-and-history','delegated-authority-and-decision-rights'}),
 'assignment':('wm-org-016-work-assignment',{'assignment-record-identity','assignment-participants-and-relation-shape','role-and-position-linkage','granted-authority-and-decision-rights','supervision-reporting-and-delegation','effort-allocation-and-capacity','effective-period-concurrency-and-succession','assignment-state-model-and-transitions','amendment-and-material-change'})}
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
 dossier={'contour':next(x for x in reg['units'] if x['id']=='EM-LND-01'),'registry_policy':{'reserved_candidates':['WM-ORG-002','WM-ORG-003','WM-ORG-004','WM-ORG-016'],'rule':'No new ID without independent identity/lifecycle and registry allocation.'},'models':{}}
 for label,(folder,ids) in MODELS.items():
  d=yaml.safe_load((REPO/'publications'/folder/'spec.yaml').read_text(encoding='utf-8'))
  dossier['models'][label]={'publication':d['publication'],'model':d['model'],'selected_findings':pick(d,ids),'functions':d.get('functions'),'composition':d.get('composition'),'researchAdjudication':d['researchAdjudication']}
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(OUT); print(OUT.stat().st_size)
if __name__=='__main__': main()
