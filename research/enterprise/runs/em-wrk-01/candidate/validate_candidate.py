import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-ACT-006' and c['registryId']=='vr.wm-act-006'
assert {'Task','StateTransition','Assignment','EstimateAssertion','OutcomeAssertion'} <= set(c['objects'])
assert set(c['outcomes'])=={'done','accepted','cancelled','rejected'}
assert len(c['invariants'])>=12 and len(c['relations'])>=5
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='idempotent-reimport' for x in f['cases']) and any(x['id']=='closed-fixed-no-acceptance' for x in f['cases'])
print(f"candidate-ok: WM-ACT-006, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
