import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['runtimeId']=='vr.vercy.plmm' and c['modelId']=='PLMM'
assert c['legacyRelease']['immutable'] and c['legacyRelease']['version']=='0.1.0-legacy'
assert len(c['bundles'])==11 and len({x['id'] for x in c['bundles']})==11
assert len(c['invariants'])>=12 and len(c['operations'])>=6
assert c['sourcePin']['commit']=='a8e388c21901540b71cc8479d4d6ef119c2ea276'
assert c['sourcePin']['contentDigest'].startswith('sha256:')
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any('unpinned' in x['id'] for x in f['cases']) and any('empty' in x['id'] for x in f['cases'])
print(f"candidate-ok: PLMM, {len(c['bundles'])} bundles, {len(c['invariants'])} invariants, {len(f['cases'])} fixtures")
