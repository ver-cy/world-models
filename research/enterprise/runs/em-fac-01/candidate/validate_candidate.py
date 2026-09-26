import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-BLT-002' and c['registryId']=='vr.wm-blt-002'
assert {'SpatialUnit','ContainmentAssertion','BoundaryEvidence','AreaMeasurement','UseDesignation','SplitMergeLineage'} <= set(c['objects'])
assert len(c['invariants'])>=12 and len(c['relations'])>=4
assert set(c['lineageEventKinds'])=={'split','merge'}
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='home-work-privacy' for x in f['cases']) and any(x['id']=='unit-split' for x in f['cases'])
print(f"candidate-ok: WM-BLT-002, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
