import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-REC-006' and c['registryId']=='vr.wm-rec-006'
assert {'Requirement','RequirementRevision','AcceptanceCriterion','RequirementRevisionSetView','TraceLink'} <= set(c['objects'])
assert 'RequirementBaseline' not in c['objects'] and 'RequirementConflict' not in c['objects']
assert len(c['invariants'])>=35 and len(c['relations'])>=5
assert c['objects']['RequirementRevisionSetView']['objectKind']=='derived-non-authoritative-view'
assert c['objects']['TraceLink']['objectKind']=='contained-outbound-association'
assert len(f['cases'])>=33 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='authoritative-baseline-hidden-root' for x in f['cases'])
assert any(x['id']=='mirrored-trace-forbidden' for x in f['cases'])
assert any(x['id']=='redacted-view-incomplete' for x in f['cases'])
print(f"candidate-ok: WM-REC-006, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
