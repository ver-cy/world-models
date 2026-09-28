import json
from pathlib import Path
p=Path(__file__).parent;c=json.loads((p/'candidate.json').read_text(encoding='utf-8'));f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-ACT-019' and c['version']=='0.2.1-candidate.1' and not c['canonicalPublishable']
assert c['disposition']['kind']=='replace-legacy-model-semantics' and not c['disposition']['newModelId']
assert {'Incident','ImpactAssessment','IncidentCorrespondence','IncidentMerge','QualificationReference'}<=set(c['objects'])
assert len(c['allowedTransitions'])>=10 and len(c['invariants'])>=33 and len(c['holds'])>=14
assert c['referenceType']['representationRoles']==['originating','master','mirror']
assert c['neighborExpectations']['WM-KNW-014']['rootCauseClaim']['statuses'][-2:]==['endorsed','superseded']
assert len(f['cases'])>=32 and all('expectRule' in x for x in f['cases'])
needed={'valid-declaration','cyber-first','valid-merge','versionless-defect-ref','cascade-delete','clock-inversion','free-text-root-cause'}
assert needed<={x['id'] for x in f['cases']}
print(f"candidate-ok: WM-ACT-019 {c['version']}, {len(c['invariants'])} invariants, {len(f['cases'])} fixtures")
