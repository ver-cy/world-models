"""Bounded reference validator. Does not implement production IAM or decide employment outcomes."""
import json,copy,sys
from pathlib import Path
from datetime import datetime
from jsonschema import Draft202012Validator,FormatChecker
ROOT=Path(__file__).resolve().parent
SCHEMA=json.loads((ROOT/'instance.schema.json').read_text(encoding='utf-8'))
def parse(t):return datetime.fromisoformat(t.replace('Z','+00:00'))
def errors(d):
    out=['schema:'+e.message for e in Draft202012Validator(SCHEMA,format_checker=FormatChecker()).iter_errors(d)]
    if out:return out
    def require(ok,rule):
        if not ok:out.append(rule)
    context=d['governing_context'];require(context['kind']=={'employee':'employment','contractor':'contract','founder':'founder-mandate'}[d['profile']],'context-profile')
    require(parse(d['period']['start'])<parse(d['period']['end']),'period-order')
    groups=['objectives','evidence','assessments','calibrations','appeals','recognition','disclosures'];ids=[x['id'] for g in groups for x in d[g]];require(len(ids)==len(set(ids)),'unique-record-ids')
    ev={x['id']:x for x in d['evidence']};assess={x['id']:x for x in d['assessments']};scales={(x['id'],x['version']):x for x in d['scale_versions']}
    require(len(scales)==len(d['scale_versions']),'scale-version-uniqueness')
    for x in d['evidence']:
        require(x['context_ref']==context['reference'],'evidence-governing-context');require(x['purpose']==d['purpose'],'evidence-purpose')
        require(parse(x['observed_at'])<=parse(x['recorded_at']),'evidence-time-order')
        require(bool(x['attributions']),'attribution-required')
    issued=[x for x in d['assessments'] if x['status']=='issued'];require(len(issued)<=1,'single-current-outcome')
    if d['state'] in ['issued','corrected','closed']:require(len(issued)==1,'issued-state-outcome')
    for x in d['assessments']:
        require(parse(x['valid_at'])<=parse(x['recorded_at']),'assessment-valid-recorded-order')
        if 'redaction' in x:
            require(x['status']=='superseded','redacted-superseded-only')
            require(parse(x['redaction']['recorded_at'])>=parse(x['recorded_at']),'redaction-time-order')
            continue
        refs=x['evidence_refs'];require(all(i in ev for i in refs),'assessment-evidence-references')
        if x['status']=='issued':
            require(x['actor_kind']=='human','human-issuance');require(bool(refs),'issued-evidence')
            usable=[ev[i] for i in refs if i in ev and ev[i]['use_state']!='excluded' and ev[i]['kind'] not in ['activity-count','surveillance-proxy']]
            require(bool(usable),'no-proxy-only-rating');require(not any(ev[i]['use_state']=='excluded' for i in refs if i in ev),'excluded-evidence')
            if any(ev[i]['use_state']=='contested' for i in refs if i in ev):require(x['known_conflict'],'visible-conflict')
        if x['rating'] is not None:
            key=(x['scale_ref'],x['scale_version']);require(key in scales,'pinned-rating-scale')
            if key in scales:require(x['rating'] in scales[key]['anchors'],'scale-anchor')
        else:require(x['scale_ref'] is None and x['scale_version'] is None,'narrative-without-scale')
        if x['supersedes']:
            prior=assess.get(x['supersedes']);require(prior is not None,'correction-history')
            if prior:require(prior['status']=='superseded' and parse(prior['issued_at'])<parse(x['issued_at']),'correction-order')
    for c in d['calibrations']:
        require(c['before_assessment_ref'] in assess and c['after_assessment_ref'] in assess,'calibration-references')
        require(c['before_assessment_ref']!=c['after_assessment_ref'],'calibration-before-after')
        before=assess.get(c['before_assessment_ref']);after=assess.get(c['after_assessment_ref'])
        if before and after:
            require(after.get('supersedes')==before['id'] and before['status']=='superseded','calibration-supersession')
    for a in d['appeals']:
        require(a['assessment_ref'] in assess,'appeal-reference')
        if a['correction_ref']:require(a['correction_ref'] in assess,'appeal-correction-reference')
    for x in d['disclosures']:
        require(x['canonical_subject_ref']==d['id'],'one-object-projection');require(x['source_owner_ref']==context['owner_org_ref'],'preserve-master-owner');require(bool(x['field_paths']),'explicit-disclosure-fields');require('*' not in x['field_paths'],'no-wildcard-disclosure')
        require(x['source_revision']==d['revision'],'projection-revision-pin')
        for pointer in x['field_paths']:
            try:
                assert pointer.startswith('/')
                value=d
                for part in pointer[1:].split('/'):
                    key=part.replace('~1','/').replace('~0','~')
                    value=value[int(key)] if isinstance(value,list) else value[key]
            except (AssertionError,KeyError,IndexError,ValueError,TypeError):out.append('projection-field-reference')
        if any(p.startswith('/assessments') for p in x['field_paths']) and d['appeals']:
            require('/appeals' in x['field_paths'],'dispute-context-in-projection')
    history=d['history'];require(bool(history),'revision-history')
    if history:
        require(history[-1]['revision']==d['revision'],'current-revision');require(history[0]['previous_revision'] is None,'first-revision')
        for previous,current in zip(history,history[1:]):require(current['previous_revision']==previous['revision'] and current['revision']>previous['revision'] and parse(current['recorded_at'])>parse(previous['recorded_at']),'revision-chain')
    return out
def main():
    cases={p.name:json.loads(p.read_text(encoding='utf-8')) for p in ROOT.glob('example-*.json')};results=[]
    for name,d in cases.items():
        issue=errors(d);assert not issue,(name,issue);results.append({'case':name,'expected':'valid','passed':True})
    base=cases['example-dual-employment.json']
    mutations=[('proxy-only-rating',lambda x:x['assessments'][1].update(evidence_refs=['urn:synthetic:evidence:commits']),'no-proxy-only-rating'),('scale-drift',lambda x:x['assessments'][1].update(scale_version='unavailable'),'pinned-rating-scale'),('automated-issuance',lambda x:x['assessments'][1].update(actor_kind='agent'),'human-issuance'),('hidden-conflict',lambda x:x['assessments'][1].update(known_conflict=False),'visible-conflict'),('history-erasure',lambda x:x['assessments'].pop(0),'correction-history'),('cross-employer-master-transfer',lambda x:x['disclosures'][0].update(source_owner_ref='urn:synthetic:org:c'),'preserve-master-owner'),('multi-object-projection',lambda x:x['disclosures'][0].update(canonical_subject_ref='urn:synthetic:person:p'),'one-object-projection'),('purpose-laundering',lambda x:x['evidence'][0].update(purpose='layoff-selection'),'evidence-purpose'),('unscoped-employment',lambda x:x['evidence'][0].update(context_ref='urn:synthetic:employment:e2'),'evidence-governing-context'),('empty-attribution',lambda x:x['evidence'][0].update(attributions=[]),'attribution-required'),('invalid-period',lambda x:x['period'].update(end=x['period']['start']),'period-order'),('duplicate-case-record-id',lambda x:x['evidence'].append(copy.deepcopy(x['evidence'][0])),'unique-record-ids'),('hidden-calibration',lambda x:x['calibrations'][0].update(before_assessment_ref=x['calibrations'][0]['after_assessment_ref']),'calibration-before-after'),('wildcard-disclosure',lambda x:x['disclosures'][0].update(field_paths=['*']),'no-wildcard-disclosure'),('recognition-writes-rating',lambda x:x['recognition'][0].update(changes_rating=True),'schema:'),('automatic-employment-decision',lambda x:x['policy'].update(automatic_employment_decisions=True),'schema:'),('portable-person-score',lambda x:x['policy'].update(portable_person_score=True),'schema:'),('missing-authority',lambda x:x['governing_context'].pop('authority_ref'),'schema:')]
    mutations.extend([('projection-stale-revision',lambda x:x['disclosures'][0].update(source_revision=1),'projection-revision-pin'),('missing-projection-field',lambda x:x['disclosures'][0].update(field_paths=['/invented']),'projection-field-reference'),('one-sided-outcome-export',lambda x:x['disclosures'][0].update(field_paths=['/assessments/1/narrative']),'dispute-context-in-projection'),('contractor-fake-employment',lambda x:x.update(profile='contractor'),'context-profile'),('missing-disclosure-authority',lambda x:x['disclosures'][0].pop('authorization_ref'),'schema:')])
    mutations.extend([('calibration-without-supersession',lambda x:x['assessments'][1].update(supersedes=None),'calibration-supersession'),('forged-redaction-on-live-assertion',lambda x:x['assessments'][1].update(redaction={'reason':'Erase'}),'schema:')])
    for name,mutation,expected in mutations:
        candidate=copy.deepcopy(base);mutation(candidate);issue=errors(candidate);assert any(expected in e for e in issue),(name,issue);results.append({'case':name,'expected':'invalid','expected_rule':expected,'passed':True})
    report={'schema_version':'1.0.0','passed':len(results),'failed':0,'scope':'Reference example rules only; not production IAM, legal conformance, a live HRIS adapter or universal domain completeness.','cases':results}
    (ROOT/'fixture-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':len(results),'failed':0}))
if __name__=='__main__':main()
