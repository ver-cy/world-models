import json
from pathlib import Path
import yaml
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT=REPO/"research/enterprise/runs/em-lnd-05/provider-dossier.json"
MODELS={
 'program_portfolio':('wm-act-029-program-portfolio',{'program-or-portfolio-definition-profile-and-neighbor-boundary','aggregate-identifier-name-alias-version-source-and-lineage','strategy-policy-need-objective-alignment-thesis-and-priority','scope-inclusion-exclusion-assumption-constraint-context-and-success','component-identity-type-membership-basis-status-and-accountability','dependency-interface-shared-change-sequencing-conflict-and-external-relation','input-activity-output-capability-outcome-benefit-disbenefit-impact-and-causal-link','benefit-owner-baseline-target-indicator-realization-plan-and-attribution-limit','funding-budget-investment-cost-forecast-actual-commitment-and-value-reference','resource-capability-capacity-demand-allocation-utilization-gap-and-conflict','programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation','component-admission-removal-priority-change-successor-and-history','metric-definition-formula-unit-dimension-baseline-target-forecast-actual-and-aggregation','performance-observation-evaluation-health-variance-benefit-review-and-lesson'}),
 'project':('wm-act-005-project',{'f-project-identity','f-project-classification','f-charter-and-authorization','f-business-case-and-funding','f-objectives-and-success-criteria','f-scope-boundary-and-exclusions','f-component-links-and-dependencies','f-project-organization-and-roles','f-resource-allocation-commitment','f-budget-and-cost-baseline','f-baseline-set-and-versioning','f-change-control','f-progress-and-earned-value','f-status-reporting-and-forecast','f-closure-and-lessons'})}
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
 dossier={'contour':next(x for x in reg['units'] if x['id']=='EM-LND-05'),'registry_policy':{'reserved_candidates':['WM-ACT-029','WM-ACT-005'],'rule':'No new ID without independent identity/lifecycle and registry allocation.'},'models':{}}
 for label,(folder,ids) in MODELS.items():
  d=yaml.safe_load((REPO/'publications'/folder/'spec.yaml').read_text(encoding='utf-8'))
  dossier['models'][label]={'publication':d['publication'],'model':d['model'],'selected_findings':pick(d,ids),'functions':d.get('functions'),'composition':d.get('composition'),'researchAdjudication':d['researchAdjudication']}
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(OUT); print(OUT.stat().st_size)
if __name__=='__main__': main()
