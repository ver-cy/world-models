import json
from pathlib import Path
p=Path(__file__).parent
files=['compensation-band.json','compensation-assignment.json','benefit-plan.json','benefit-enrollment.json']
roots=[json.loads((p/n).read_text()) for n in files]
profile=json.loads((p/'enterprise-compensation-benefits-profile.json').read_text())
fx=json.loads((p/'fixtures.json').read_text())
ids={r['id'] for x in roots for r in x['invariantRules']}|{r['id'] for r in profile['constraintRules']}
refs={r for c in fx['cases'] for r in c['rules']}
assert refs<=ids, sorted(refs-ids)
assert ids<=refs, sorted(ids-refs)
assert len(ids)==len(set(ids)) and len({c['id'] for c in fx['cases']})==len(fx['cases'])
assert all(x['modelId'] is None and x['registryId'] is None and not x['canonicalPublishable'] and x['candidateRevision']==3 for x in roots)
assert profile['newRuntimeId'] is False and profile['canonicalPublishable'] is False and profile['candidateRevision']==3
assert fx['candidateRevision']==3 and fx['canonicalPublishable'] is False
print(json.dumps({'ok':True,'roots':len(roots),'rules':len(ids),'fixtures':len(fx['cases'])},indent=2))
