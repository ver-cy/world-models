import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-SFT-003' and c['registryId']=='vr.wm-sft-003'
assert {'InterfaceContract','ContractRevision','ConsumerPin','EndpointBinding','CompatibilityAssessment'} <= set(c['objects'])
assert len(c['invariants'])>=12 and len(c['relations'])>=4 and len(c['compatibilityRules'])>=5
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='url-change-only' for x in f['cases']) and any(x['id']=='semantic-change-same-url' for x in f['cases'])
print(f"candidate-ok: WM-SFT-003, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
