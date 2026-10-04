import json
from pathlib import Path
p=Path(__file__).parent
a=json.loads((p/'wm-act-003.candidate.json').read_text(encoding='utf-8'))
b=json.loads((p/'wm-act-009.candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert a['registryId']=='vr.wm-act-003' and b['registryId']=='vr.wm-act-009'
assert a['entryKind']==b['entryKind']=='standalone-mm'
assert a['publishableCanonical'] is b['publishableCanonical'] is False
assert a['fixturesExecuted'] is b['fixturesExecuted'] is False
assert a['legacyVersion']==b['legacyVersion']=='0.2.0-legacy'
assert len(a['invariants'])>=30 and len(b['invariants'])>=24
for x in ['WorkItemEvent','CutoverRecord','ConformanceResult','DeviationKindVocabulary']: assert x in a['objects']
for x in ['EditionManifest','CompetenceRequirement','ClaimRetractionNote']: assert x in b['objects']
assert a['objects']['ProcessInstance']['required'].count('variantKey')==1
assert 'variantKeyOrNone' not in str(a)
assert all(r['required'] is False for r in a['relations'] if r['target'] in {'vr.wm-act-009','vr.wm-act-006','vr.wm-org-016'})
assert len(f['cases'])>=75 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
required={'retroactive-instruction-update','conformance-across-cutover','digest-mismatch-on-pin','wm-act-009-legacy-preserved','tombstoned-performer-preserves-trace-digest'}
assert required <= {x['id'] for x in f['cases']}
print(f"candidate-ok: WM-ACT-003 {len(a['invariants'])} invariants; WM-ACT-009 {len(b['invariants'])} invariants; {len(f['cases'])} fixtures")
