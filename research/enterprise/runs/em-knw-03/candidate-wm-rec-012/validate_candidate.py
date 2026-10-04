import json
from pathlib import Path
p=Path(__file__).parent;c=json.loads((p/'candidate.json').read_text(encoding='utf-8'));f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-REC-012' and c['version']=='0.1.0-candidate.3' and not c['canonicalPublishable']
ids=[x['id'] for x in c['invariants']]; assert len(ids)==len(set(ids)) and all(x.startswith('INV-') for x in ids)
assert c['relations'][0]['required']=='conditional' and c['relations'][1]['required']=='conditional'
assert all(x['expectRule'] in ids for x in f['cases'])
assert len(c['invariants'])>=34 and len(f['cases'])>=38
print(f"candidate-ok: WM-REC-012 {c['version']}, {len(c['invariants'])} invariants, {len(f['cases'])} fixtures")
