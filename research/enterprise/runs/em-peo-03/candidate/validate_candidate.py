import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-PER-009' and c['registryId']=='vr.wm-per-009'
assert {'CompetencyScheme','SkillCompetencyConcept','CompetencyComposition','ConceptMapping'} <= set(c['objects'])
assert set(c['conceptTypes'])=={'skill','competency'}
assert len(c['invariants'])>=12 and len(c['relations'])>=3
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='same-number-different-scale' for x in f['cases'])
print(f"candidate-ok: WM-PER-009, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
