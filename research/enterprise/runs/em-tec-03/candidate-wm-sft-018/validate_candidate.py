import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-SFT-018' and c['registryId']=='vr.wm-sft-018'
assert {'NetworkEndpoint','AddressBinding','ConnectivityRelation','ExposureAssertion','ZoneMembership'} <= set(c['objects'])
assert len(c['invariants'])>=12 and len(c['relations'])>=4
assert all(x['relation']=='REFERENCE' for x in c['relations'])
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='address-reassignment' for x in f['cases'])
assert any(x['id']=='declared-not-observed' for x in f['cases'])
print(f"candidate-ok: WM-SFT-018, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
