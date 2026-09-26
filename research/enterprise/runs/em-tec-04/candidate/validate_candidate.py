import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-SFT-010' and c['registryId']=='vr.wm-sft-010'
assert {'RuntimeEnvironment','InfrastructureResource','DeployedInstance','HostingRelation','ConfigurationItemDesignation','StateAssertion'} <= set(c['objects'])
assert len(c['invariants'])>=12 and len(c['relations'])>=4
assert set(c['hostingRelationKinds'])=={'runs-on','member-of','backed-by','served-by'}
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='node-replacement-as-of' for x in f['cases']) and any(x['id']=='ip-reassignment' for x in f['cases'])
print(f"candidate-ok: WM-SFT-010, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
