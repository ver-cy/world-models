import json
from pathlib import Path
p=Path(__file__).parent
r=json.loads((p/'control.json').read_text()); q=json.loads((p/'enterprise-risk-control-profile.json').read_text()); f=json.loads((p/'fixtures.json').read_text())
ids={x['id'] for x in r['invariantRules']+q['constraintRules']}; refs={y for x in f['cases'] for y in x['rules']}
assert ids==refs and len(ids)==len(set(ids)); assert len({x['id'] for x in f['cases']})==len(f['cases'])
assert r['modelId'] is None and r['registryId'] is None and not r['canonicalPublishable']; assert q['newRuntimeId'] is False and not q['canonicalPublishable']; assert r['candidateRevision']==q['candidateRevision']==f['candidateRevision']==3
print(json.dumps({'ok':True,'roots':1,'rules':len(ids),'fixtures':len(f['cases'])},indent=2))
