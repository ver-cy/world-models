import json
from pathlib import Path
p=Path(__file__).parent;c=json.loads((p/'candidate.json').read_text(encoding='utf-8'));f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-DAT-008' and c['version']=='0.3.1-candidate.3' and not c['canonicalPublishable']
assert set(c['rootObjects'])=={'DataProduct','ProductCatalogRecord','ConsumerEntitlementBinding'}
assert c['identities']['consumerEntitlementBinding']==['productId','entitlementBindingId']
assert len(c['invariants'])>=28 and len({x['id'] for x in c['invariants']})==len(c['invariants'])
assert len(f['cases'])>=27 and all(isinstance(x['expectRule'],list) for x in f['cases'])
rule_ids={x['id'] for x in c['invariants']};assert all(set(x['expectRule'])<=rule_ids for x in f['cases'])
needed={'series-head-promise-breach','catalog-boundary-collision','internal-use-binding','active-unpublished-binding','catalog-tombstone'}
assert needed<={x['id'] for x in f['cases']}
print(f"candidate-ok: WM-DAT-008 {c['version']}, {len(c['invariants'])} invariants, {len(f['cases'])} fixtures")
