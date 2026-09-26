import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-REC-006' and c['registryId']=='vr.wm-rec-006'
assert {'Requirement','RequirementRevision','AcceptanceCriterion','RequirementBaseline','TraceLink','RequirementConflict'} <= set(c['objects'])
assert len(c['invariants'])>=12 and len(c['relations'])>=5
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='done-tasks-failed-test' for x in f['cases']) and any(x['id']=='baseline-membership-edit' for x in f['cases'])
print(f"candidate-ok: WM-REC-006, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
