import json
from pathlib import Path
p=Path(__file__).parent
roots=[json.loads((p/n).read_text()) for n in ['grade-scheme.json','role-profile.json','grade-assignment.json']]
fx=json.loads((p/'fixtures.json').read_text())
ids={r['id'] for x in roots for r in x['invariantRules']}
refs={r for c in fx['cases'] for r in c['rules']}
assert refs<=ids, sorted(refs-ids)
assert all(x['modelId'] is None and x['registryId'] is None and not x['canonicalPublishable'] for x in roots)
assert len(ids)==54 and len(fx['cases'])==61
print(json.dumps({'ok':True,'roots':3,'rules':len(ids),'fixtures':len(fx['cases'])},indent=2))
