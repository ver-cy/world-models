import json
from pathlib import Path
p=Path(__file__).parent;c=json.loads((p/'candidate.json').read_text(encoding='utf-8'));f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-ACT-022' and c['registryId']=='vr.wm-act-022' and c['canonicalPublishable'] is False
assert {'ExperimentRun','DesignPin','RunManifest','ExperimentAttempt','RunDeviation','ResultAccessEvent','RunCoverage','RunErratum','RunSupersessionLink'}<=set(c['objects'])
assert len(c['invariants'])>=20 and len(c['relations'])>=7 and len(f['cases'])>=10
assert {'positive','negative'}<={x['kind'] for x in f['cases']}
assert all(x.get('expectedCode') for x in f['cases'] if x['kind']=='negative')
print(f"candidate-ok: WM-ACT-022, {len(c['invariants'])} invariants, {len(c['relations'])} boundaries, {len(f['cases'])} fixtures")
