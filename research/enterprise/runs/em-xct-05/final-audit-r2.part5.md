TEXT TRANSPORT PART 5/5. All parts supplied now. Join PART CONTENT sections in order and perform the independent audit requested in part 1. State any missing/truncated file.
PART CONTENT
rsion migration deferred.","questions":[{"id":"DR-Q24","text":"Can the register migrate without losing meaning?","kind":"governed-context","answer_data":["Complete same-version records, exact pins, source version and explicit loss analysis","If unavailable: insufficient-context with named missing evidence; lack of read authority remains denied."]}],"artifacts":[{"id":"DR-A24","name":"Complete same-version records, exact pins, source version and explicit loss analysis","description":"Evidence to collect; not a claim that the companion creates, resolves or validates every external artifact."}],"actions":[{"id":"DR-ACT24","description":"Roundtrip same version; refuse unsupported version conversion. Proposed operation only; requires the named host/domain authority."}],"implementationScope":"local roundtrip; cross-version migration deferred"}]}]}]},"statistics":{"bundles":4,"layers":8,"findings":24,"questions":24,"artifacts":24,"actions":24},"catalogue":{"alternateNames":["EM-XCT-05","Context Package Proposal","Joint Disclosure Review","Disclosure classification and custody"],"domain":["Enterprise","Disclosure review","Information governance"],"tags":["disclosure","classification","projection","review","custody"],"adoption":"Start with one exact metadata proposal and one attributed review. Pin source/schema/shape/classification and audience/purpose/environment/prior-release/custody context. Preserve immutable revisions and inspect them against independently resolved current governance state. Three synthetic new-Dimension examples exercise the explicit native binding.","limits":"No result grants access, serves source values, proves privacy or executes disposal. Current authority, pin resolution, snapshot completeness and custody remain host responsibilities."},"invariants":"## Sixteen semantic invariants\n\n1. Each embedded member names exactly one source object; package membership can span objects but a projection cannot silently do so.\n2. Qualified ID, record revision, source/schema revision, lifecycle/applicability and digest remain distinct.\n3. All local reference occurrences of an ID agree on revision/digest; the reference cannot carry two purported current versions of that ID in one record.\n4. No undeclared source value or nested/wildcard field is accepted by the metadata-only grammar.\n5. A missing classification binding or evidence set cannot become an empty/public/clear default.\n6. A review pins exactly the proposal identity/revision/digest; membership, shape, audience or any bound context change invalidates that match.\n7. A current snapshot pins the proposal itself and independently declares all current member/context values.\n8. The complete supplied review set equals the active pin set; duplicate or competing active revisions are invalid.\n9. Active and withdrawn sets are disjoint; an active successor cannot leave its superseded target active.\n10. Review assessment does not predate proposal capture; applicability uses `[validFrom, validTo)` and future capture is stale.\n11. Current author/reviewer catalogs and authority pin are applied; segregation is explicit and actor-alias identity remains a host duty.\n12. Conflicting eligible verdicts cannot silently select a winner. Excluded verdicts retain their pin, result and reason in restricted diagnostics.\n13. Every returned report identifies its proposal, snapshot digest, evaluation time and counted/ignored records, and explicitly conveys no serving authorization.\n14. Within a supplied register, the same identity/revision cannot be repointed; repeat import is idempotent and a failed merge leaves the caller's store unchanged.\n15. Local review/proposal and supersession links resolve by exact pin/type, preserve proposal identity and nondecreasing assessment time, and do not cycle.\n16. Pin equality, a human clearance and any custody-context reference establish no source truth, inference guarantee, current grant, legal conclusion, completed delivery or destruction.\n\nInvariants 1–15 combine local checks with clearly named host attestations; invariant 16 is a semantic boundary and is not a proof produced by unit tests. The final 24 question routes are in spec.json; each names local checks versus host/deferred responsibility.\n\n"}
</file>
END FILE spec.json

## FILE test-results.json
ORIGINAL SHA256 0e1ddd002f1014e85bb4c0cfe145bcb25ee8ad3219f92b2c1d19ad2a3694a745
<file>
{"status":"passed","passed":true,"testsRun":108,"failures":0,"errors":0,"scope":"Codex reference behavior checks; native integration has a separate report; no privacy/security conformance","codeSha256":"c2371aac6c1adfbdd694e7280b2140cae6cd6649aabe3c738e6bd3f925979b17","inputHashes":{"disclosure.py":"c2371aac6c1adfbdd694e7280b2140cae6cd6649aabe3c738e6bd3f925979b17","disclosure.schema.json":"45b2f2c82b9d9af72b2b462d3e502098fbd5b166bf8bd705947ba12e1e5cc834","test_disclosure.py":"dd35bec97e0965c739dbb6449069be5dfadfc8e71083ec679bb1cc9ab1dbdf22","README.md":"92bb4ebd0138a871cb088e311799fca704b875dc236a4a5932ec62d712733299"},"exampleHashes":{"ai.json":"1100097d1526b8c53e5ad51ca75d8d5d0ccb4a59a6afe5a565a532996e799014","matrix.json":"63199a204156969003e900daea112eba5ff8545f7b21a6ce64e6e2944c04b0a0","startup.json":"44968621c7d9fbd0256270ff0a95e5a4665b83094a7c574e0ebee89bdf83023d"},"python":"3.12.14 (main, Aug 25 2026, 14:01:42) [MSC v.1944 64 bit (AMD64)]","jsonschema":"4.26.0"}
</file>
END FILE test-results.json

## FILE test_disclosure.py
ORIGINAL SHA256 dd35bec97e0965c739dbb6449069be5dfadfc8e71083ec679bb1cc9ab1dbdf22
<file>
import copy,hashlib,json,unittest,sys,importlib.metadata
from pathlib import Path
import disclosure as d

def p(name,rev='1'):
    return {'id':'urn:synthetic:'+name,'revision':rev,'digest':'sha256:'+hashlib.sha256((name+rev).encode()).hexdigest()}

def fixture(profile='startup'):
    member={'key':'project-name','source':p('project'),'schema':p('project-schema'),'shape':p('name-only-shape'),
            'fields':[{'name':'name','kind':'string','classificationBindings':[p('name-classification')]}]}
    members=[member]
    if profile=='matrix':
        member['key']='group-summary';member['source']=p('group-aggregate');member['fields'][0]['name']='headcount';member['fields'][0]['kind']='integer'
        member['schema']=p('headcount-schema');member['shape']=p('headcount-summary-shape');member['fields'][0]['classificationBindings']=[p('headcount-classification')]
        other=copy.deepcopy(member);other['key']='unit-summary';other['source']=p('unit-aggregate');members.append(other)
    if profile=='ai':
        member['key']='release-notes';member['source']=p('model-release');member['fields'][0]['name']='releaseNotes'
        member['schema']=p('release-notes-schema');member['shape']=p('release-notes-shape');member['fields'][0]['classificationBindings']=[p('release-notes-classification')]
    proposal=d.seal({'format':'vercy-disclosure-research','version':d.VERSION,'type':'proposal','dimension':'urn:synthetic:dimension:'+profile,'id':'urn:synthetic:proposal:'+profile,'revision':'1',
       'body':{'author':'urn:synthetic:founder','capturedAt':'2026-09-21T10:00:00Z','audience':p('partner'),'purpose':p('release-briefing'),'environment':p('partner-portal'),'priorReleases':p('known-prior-release-context'),'custodyContext':p('custody-instructions'),'members':members}})
    review=d.seal({'format':'vercy-disclosure-research','version':d.VERSION,'type':'review','dimension':proposal['dimension'],'id':'urn:synthetic:review:'+profile,'revision':'1',
       'body':{'proposal':d.pin(proposal),'reviewer':'urn:synthetic:reviewer','authority':p('review-authority'),'method':p('bounded-manual-review'),'evidence':[p('synthetic-assessment')],'reviewedAt':'2026-09-21T10:01:00Z','validFrom':'2026-09-21T10:01:00Z','validTo':'2026-09-22T10:01:00Z','verdict':'cleared','residualRisk':'Synthetic scenario only. No claim of inference prevention.','supersedes':None}})
    if profile=='matrix':
        review['body']['verdict']='rejected';review['body']['residualRisk']='Synthetic reviewer identifies a subtraction path between group and unit headcounts exposing an individual indicator. This package is rejected. The validator does not calculate that risk.';review=d.seal(review)
    snapshot={'format':'vercy-disclosure-host-snapshot','version':d.VERSION,'dimension':proposal['dimension'],'asOf':'2026-09-21T12:00:00Z','proposal':d.pin(proposal),'context':{k:copy.deepcopy(proposal['body'][k]) for k in ('audience','purpose','environment','priorReleases','custodyContext')},'members':copy.deepcopy(members),'proposalAuthors':['urn:synthetic:founder'],'reviewers':['urn:synthetic:reviewer','urn:synthetic:founder'],'authority':p('review-authority'),'activeReviews':[d.pin(review)],'withdrawnReviews':[],'separateReviewer':profile!='startup'}
    cap={'dimension':proposal['dimension'],'inspect':True,'record':True}
    return proposal,review,snapshot,cap

class ResearchPrototype(unittest.TestCase):
    def setUp(self):self.p,self.r,self.s,self.c=fixture();self.now='2026-09-21T12:00:00Z'
    def answer(self,**kw):
        s=kw.get('snapshot',self.s)
        if 'now' in kw and 'snapshot' not in kw:
            s=copy.deepcopy(s);s['asOf']=kw['now']
        return d.inspect(kw.get('proposal',self.p),kw.get('reviews',[self.r]),s,kw.get('capability',self.c),kw.get('now',self.now))
    def reseal_review(self):self.r=d.seal(self.r);self.s['activeReviews']=[d.pin(self.r)]
    def test_three_profiles(self):
        for profile in ('startup','matrix','ai'):
            with self.subTest(profile=profile):
                a,b,s,c=fixture(profile);self.assertEqual(d.inspect(a,[b],s,c,self.now)['status'],'rejected' if profile=='matrix' else 'applicable-review')
    def test_clearance_explicitly_not_authorization(self):self.assertIs(self.answer()['notServingAuthorization'],True)
    def test_startup_explicit_self_review(self):
        self.r['body']['reviewer']=self.p['body']['author'];self.reseal_review();self.assertEqual(self.answer()['status'],'applicable-review')
    def test_segregated_profile_refuses_self_review(self):
        self.s['separateReviewer']=True;self.r['body']['reviewer']=self.p['body']['author'];self.reseal_review();self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_revoked_reviewer(self):self.s['reviewers']=[];self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_revoked_author(self):self.s['proposalAuthors']=[];self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_changed_authority(self):self.s['authority']=p('review-authority','2');self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_withdrawn_clearance(self):self.s['withdrawnReviews']=[d.pin(self.r)];self.s['activeReviews']=[];self.assertEqual(self.answer(reviews=[])['status'],'insufficient-context')
    def test_future_review(self):self.assertEqual(self.answer(now='2026-09-21T10:00:30Z')['status'],'insufficient-context')
    def test_expiry_is_exclusive(self):self.assertEqual(self.answer(now=self.r['body']['validTo'])['status'],'insufficient-context')
    def test_start_is_inclusive(self):self.assertEqual(self.answer(now=self.r['body']['validFrom'])['status'],'applicable-review')
    def test_future_capture(self):self.assertEqual(self.answer(now='2026-09-20T10:00:00Z')['status'],'stale')
    def test_context_drift(self):
        for k in self.s['context']:
            with self.subTest(key=k):
                s=copy.deepcopy(self.s);s['context'][k]=p(k,'changed');self.assertEqual(self.answer(snapshot=s)['status'],'stale')
    def test_source_schema_shape_classification_drift(self):
        for k in ('source','schema','shape'):
            with self.subTest(key=k):
                s=copy.deepcopy(self.s);s['members'][0][k]=p(k,'2');self.assertEqual(self.answer(snapshot=s)['status'],'stale')
        self.s['members'][0]['fields'][0]['classificationBindings']=[p('binding','2')];self.assertEqual(self.answer()['status'],'stale')
    def test_added_member_needs_new_review(self):
        m=copy.deepcopy(self.p['body']['members'][0]);m['key']='another';self.p['body']['members'].append(m);self.p=d.seal(self.p);self.s['members']=self.p['body']['members']
        self.s['proposal']=d.pin(self.p)
        with self.assertRaisesRegex(d.Invalid,'review points to another proposal'):self.answer()
    def test_added_field_needs_new_review(self):
        f={'name':'budget','kind':'number','classificationBindings':[p('budget-binding')]};self.p['body']['members'][0]['fields'].append(f);self.p=d.seal(self.p);self.s['members']=self.p['body']['members']
        self.s['proposal']=d.pin(self.p)
        with self.assertRaisesRegex(d.Invalid,'review points to another proposal'):self.answer()
    def test_reordered_members_changes_pin(self):
        a,b,s,c=fixture('matrix');a['body']['members'].reverse();a=d.seal(a);s['members']=a['body']['members']
        s['proposal']=d.pin(a)
        with self.assertRaisesRegex(d.Invalid,'review points to another proposal'):d.inspect(a,[b],s,c,self.now)
    def test_current_unknown_member(self):
        self.s['members']=[]
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()
    def test_hidden_review_not_ignored(self):self.s['activeReviews'].append(p('hidden-review'));self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_empty_review_set_is_not_clearance(self):self.s['activeReviews']=[];self.assertEqual(self.answer(reviews=[])['status'],'insufficient-context')
    def test_conflicting_active_reviews(self):
        other=copy.deepcopy(self.r);other['id']='urn:synthetic:other-review';other['body']['verdict']='rejected';other=d.seal(other);self.s['activeReviews'].append(d.pin(other));self.assertEqual(self.answer(reviews=[self.r,other])['status'],'conflict')
    def test_inconclusive_is_not_clearance(self):self.r['body']['verdict']='inconclusive';self.reseal_review();self.assertEqual(self.answer()['status'],'inconclusive')
    def test_rejection_is_not_clearance(self):self.r['body']['verdict']='rejected';self.reseal_review();self.assertEqual(self.answer()['status'],'rejected')
    def test_missing_capability_before_record_diagnostics(self):
        with self.assertRaisesRegex(d.Unauthorized,'^unavailable$'):self.answer(proposal={'bad':True},capability={})
    def test_cross_dimension_capability(self):
        self.c['dimension']='urn:synthetic:other'
        with self.assertRaises(d.Unauthorized):self.answer()
    def test_cross_dimension_review(self):
        self.r['dimension']='urn:synthetic:other';self.reseal_review()
        with self.assertRaises(d.Invalid):self.answer()
    def test_pre_capture_review(self):
        self.r['body']['reviewedAt']='2026-09-21T09:59:59Z';self.reseal_review()
        with self.assertRaises(d.Invalid):self.answer()
    def test_zero_validity_interval(self):
        self.r['body']['validTo']=self.r['body']['validFrom']
        with self.assertRaises(d.Invalid):d.seal(self.r)
    def test_invalid_calendar_date(self):
        self.p['body']['capturedAt']='2026-02-30T00:00:00Z'
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_missing_offset(self):
        with self.assertRaises(d.Invalid):self.answer(now='2026-09-21T12:00:00')
    def test_tampered_digest(self):
        self.p['body']['author']='urn:synthetic:someone'
        with self.assertRaisesRegex(d.Invalid,'digest'):d.validate(self.p)
    def test_no_payload_field(self):
        self.p['body']['members'][0]['values']={'budget':100}
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_no_nested_or_wildcard_fields(self):
        for name in ('owner.email','*','/notes/title','notes[0]'):
            with self.subTest(name=name):
                x=copy.deepcopy(self.p);x['body']['members'][0]['fields'][0]['name']=name
                with self.assertRaises(d.Invalid):d.seal(x)
    def test_no_object_or_array_kind(self):
        for kind in ('object','array'):
            with self.subTest(kind=kind):
                x=copy.deepcopy(self.p);x['body']['members'][0]['fields'][0]['kind']=kind
                with self.assertRaises(d.Invalid):d.seal(x)
    def test_missing_classification_not_public(self):
        self.p['body']['members'][0]['fields'][0]['classificationBindings']=[]
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_two_classification_schemes_representable(self):
        self.p['body']['members'][0]['fields'][0]['classificationBindings'].append(p('second-scheme-binding'));d.seal(self.p)
    def test_duplicate_field_rejected(self):
        f=copy.deepcopy(self.p['body']['members'][0]['fields'][0]);f['kind']='integer';self.p['body']['members'][0]['fields'].append(f)
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_duplicate_member_key(self):
        m=copy.deepcopy(self.p['body']['members'][0]);m['source']=p('different');self.p['body']['members'].append(m)
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_same_binding_revision_conflict(self):
        f=self.p['body']['members'][0]['fields'][0];other=copy.deepcopy(f['classificationBindings'][0]);other['digest']='sha256:'+'0'*64;f['classificationBindings'].append(other)
        with self.assertRaisesRegex(d.Invalid,'incoherent reference pin'):d.seal(self.p)
    def test_duplicate_json_keys(self):
        with self.assertRaises(d.Invalid):d.load(b'{"a":1,"a":2}')
    def test_float_and_nonfinite_json(self):
        for raw in (b'{"a":1.0}',b'{"a":NaN}',b'{"a":Infinity}'):
            with self.assertRaises(d.Invalid):d.load(raw)
    def test_roundtrip(self):self.assertEqual(d.load(d.canonical(self.p)),self.p)
    def test_unsupported_version(self):
        self.p['version']='0.0.0-prototype.1'
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_idempotent_import(self):
        existing=d.import_records([],[self.p,self.r],self.p['dimension'],self.c);again=d.import_records(existing,[self.p,self.r],self.p['dimension'],self.c);self.assertEqual(existing,again)
    def test_immutable_revision_conflict_transactional(self):
        x=copy.deepcopy(self.p);x['body']['purpose']=p('other');x=d.seal(x);existing=[self.p]
        with self.assertRaises(d.Invalid):d.import_records(existing,[x],self.p['dimension'],self.c)
        self.assertEqual(existing,[self.p])
    def test_correction_preserves_history(self):
        x=copy.deepcopy(self.p);x['revision']='2';x['body']['purpose']=p('new-purpose');x=d.seal(x);result=d.import_records([self.p],[x],self.p['dimension'],self.c);self.assertEqual(len(result),2)
    def test_import_needs_write_assertion(self):
        self.c['record']=False
        with self.assertRaises(d.Unauthorized):d.import_records([],[self.p],self.p['dimension'],self.c)
    def test_identity_cannot_change_type(self):
        self.r['id']=self.p['id'];self.r['revision']='2';self.r=d.seal(self.r)
        with self.assertRaises(d.Invalid):d.import_records([self.p],[self.r],self.p['dimension'],self.c)
    def test_actor_catalog_cannot_be_substring(self):
        self.s['reviewers']='urn:synthetic:reviewer-extra'
        with self.assertRaises(d.Invalid):self.answer()
    def test_duplicate_reviews_not_votes(self):
        with self.assertRaises(d.Invalid):self.answer(reviews=[self.r,self.r])
    def test_input_bound(self):
        with self.assertRaises(d.Invalid):d.load(b' '*262145)
    def test_missing_dimension_cannot_authorize(self):
        for snapshot in (None,{}):
            with self.assertRaisesRegex(d.Unauthorized,'^unavailable$'):self.answer(proposal={'bad':True},snapshot=snapshot,capability={'inspect':True})
    def test_newline_field_alias(self):
        f=copy.deepcopy(self.p['body']['members'][0]['fields'][0]);f['name']='name\n';self.p['body']['members'][0]['fields'].append(f)
        with self.assertRaisesRegex(d.Invalid,'exact identifier syntax'):d.seal(self.p)
    def test_hidden_identity_characters(self):
        for char in ('\n','\u200b','\u202e','\x00','\ufeff'):
            with self.subTest(char=repr(char)):
                x=copy.deepcopy(self.p);x['id']+=char
                with self.assertRaises(d.Invalid):d.seal(x)
    def test_unpinned_current_proposal_not_applicable(self):
        self.s['proposal']=p('retired-proposal');self.assertEqual(self.answer()['reason'],'current-proposal-differs')
    def test_missing_proposal_pin_rejected(self):
        del self.s['proposal']
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()
    def test_self_supersession_different_digest(self):
        self.r['body']['supersedes']={'id':self.r['id'],'revision':self.r['revision'],'digest':'sha256:'+'0'*64}
        with self.assertRaisesRegex(d.Invalid,'self supersession'):d.seal(self.r)
    def test_active_superseded_review_rejected(self):
        other=copy.deepcopy(self.r);other['id']='urn:synthetic:replacement';other['body']['supersedes']=d.pin(self.r);other=d.seal(other);self.s['activeReviews'].append(d.pin(other))
        with self.assertRaisesRegex(d.Invalid,'superseded review still active'):self.answer(reviews=[self.r,other])
    def test_active_withdrawn_overlap_rejected(self):
        self.s['withdrawnReviews']=[d.pin(self.r)]
        with self.assertRaisesRegex(d.Invalid,'active and withdrawn overlap'):self.answer()
    def test_predate_checked_even_without_authority(self):
        self.r['body']['reviewedAt']='2026-09-21T09:59:59Z';self.reseal_review();self.s['reviewers']=[]
        with self.assertRaisesRegex(d.Invalid,'review predates proposal'):self.answer()
    def test_reference_revision_coherence(self):
        m=copy.deepcopy(self.p['body']['members'][0]);m['key']='other';m['source']['revision']='2';self.p['body']['members'].append(m)
        with self.assertRaisesRegex(d.Invalid,'incoherent reference pin'):d.seal(self.p)
    def test_binding_revision_coherence(self):
        field=self.p['body']['members'][0]['fields'][0];other=copy.deepcopy(field['classificationBindings'][0]);other['revision']='2';field['classificationBindings'].append(other)
        with self.assertRaisesRegex(d.Invalid,'incoherent reference pin'):d.seal(self.p)
    def test_expired_negative_preserved_in_report(self):
        other=copy.deepcopy(self.r);other['id']='urn:synthetic:expired-negative';other['body']['verdict']='rejected';other['body']['validTo']='2026-09-21T11:00:00Z';other=d.seal(other);self.s['activeReviews'].append(d.pin(other));a=self.answer(reviews=[self.r,other]);self.assertEqual(a['status'],'applicable-review');self.assertEqual(a['ignored'],[{'pin':d.pin(other),'verdict':'rejected','reason':'expired'}]);self.assertEqual(a['counted'],[d.pin(self.r)])
    def test_answer_binds_inputs(self):
        a=self.answer();self.assertEqual(a['proposal'],d.pin(self.p));self.assertEqual(a['snapshotDigest'],'sha256:'+hashlib.sha256(d.canonical(self.s)).hexdigest());self.assertEqual(a['at'],self.now)
    def test_multiple_active_revisions_rejected(self):
        other=copy.deepcopy(self.r);other['revision']='2';other=d.seal(other);self.s['activeReviews'].append(d.pin(other))
        with self.assertRaisesRegex(d.Invalid,'multiple active revisions'):self.answer(reviews=[self.r,other])
    def test_invalid_utf8(self):
        with self.assertRaisesRegex(d.Invalid,'JSON'):d.load(b'{"x":"\xff"}')
    def test_huge_integer(self):
        with self.assertRaisesRegex(d.Invalid,'integer'):d.load(b'{"x":'+b'1'*5000+b'}')
    def test_year_before_1000_platform_independent(self):self.assertEqual(d.instant('0999-01-01T00:00:00Z').year,999)
    def test_leap_second_refused(self):
        with self.assertRaisesRegex(d.Invalid,'timestamp'):d.instant('2026-12-31T23:59:60Z')
    def test_exponent_number_refused(self):
        with self.assertRaisesRegex(d.Invalid,'non-integer number'):d.load(b'{"x":1e2}')
    def test_unpaired_surrogate_refused(self):
        with self.assertRaisesRegex(d.Invalid,'string'):d.load(b'{"x":"\\ud800"}')
    def test_unsafe_integer_refused(self):
        with self.assertRaisesRegex(d.Invalid,'integer'):d.load(b'{"x":9007199254740992}')
    def test_import_rejects_dangling_proposal(self):
        with self.assertRaisesRegex(d.Invalid,'unresolved internal pin'):d.import_records([],[self.r],self.p['dimension'],self.c)
    def test_import_valid_supersession_chain(self):
        other=copy.deepcopy(self.r);other['revision']='2';other['body']['supersedes']=d.pin(self.r);other['body']['reviewedAt']='2026-09-21T10:02:00Z';other['body']['validFrom']='2026-09-21T10:02:00Z';other=d.seal(other)
        self.assertEqual(len(d.import_records([self.p,self.r],[other],self.p['dimension'],self.c)),3)
    def test_import_rejects_wrong_supersession_type(self):
        self.r['body']['supersedes']=d.pin(self.p);self.r=d.seal(self.r)
        with self.assertRaisesRegex(d.Invalid,'unresolved internal pin'):d.import_records([],[self.p,self.r],self.p['dimension'],self.c)
    def test_import_rejects_unknown_supersession(self):
        self.r['body']['supersedes']=p('unknown-review');self.r=d.seal(self.r)
        with self.assertRaisesRegex(d.Invalid,'unresolved internal pin'):d.import_records([],[self.p,self.r],self.p['dimension'],self.c)
    def test_import_cross_dimension(self):
        self.p['dimension']='urn:synthetic:elsewhere';self.p=d.seal(self.p)
        with self.assertRaisesRegex(d.Invalid,'record scope'):d.import_records([],[self.p],self.c['dimension'],self.c)
    def test_snapshot_extra_keys(self):
        self.s['allowServe']=True
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()
    def test_self_objection_still_counts_under_segregation(self):
        self.s['separateReviewer']=True
        for verdict in ('rejected','inconclusive'):
            other=copy.deepcopy(self.r);other['id']='urn:synthetic:author-objection';other['body']['reviewer']=self.p['body']['author'];other['body']['verdict']=verdict;other=d.seal(other);self.s['activeReviews']=[d.pin(self.r),d.pin(other)]
            with self.subTest(verdict=verdict):self.assertEqual(self.answer(reviews=[self.r,other])['status'],'conflict')
    def test_withdrawn_newline_alias_rejected(self):
        other=d.pin(self.r);other['id']+='\n';self.s['withdrawnReviews']=[other]
        with self.assertRaisesRegex(d.Invalid,'exact identifier syntax'):self.answer()
    def test_malformed_snapshot_before_stale(self):
        self.s['proposal']=p('different');self.s['withdrawnReviews']='garbage'
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()
    def test_malformed_snapshot_authority(self):
        self.s['authority']={'invalid':True}
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()
    def test_snapshot_multiple_active_revisions_before_completeness(self):
        other=d.pin(self.r);other['revision']='2';self.s['activeReviews'].append(other)
        with self.assertRaisesRegex(d.Invalid,'multiple active revisions'):self.answer()
    def test_active_withdrawn_different_digest_rejected(self):
        other=d.pin(self.r);other['digest']='sha256:'+'0'*64;self.s['withdrawnReviews']=[other]
        with self.assertRaisesRegex(d.Invalid,'active and withdrawn overlap'):self.answer()
    def test_snapshot_time_must_equal_evaluation_time(self):
        with self.assertRaisesRegex(d.Invalid,'snapshot time mismatch'):d.inspect(self.p,[self.r],self.s,self.c,'2026-09-21T11:00:00Z')
    def test_golden_encoding_controls_and_separator(self):
        expected=b'{"a":"\\n\\t\\u0000\xe2\x80\xa8","z":"\\\"\\\\"}'
        self.assertEqual(d.canonical({'z':'"\\','a':'\n\t\x00\u2028'}),expected)
    def test_container_subclass_rejected(self):
        class FalseString(str):
            def __eq__(self,other):return True
        x=copy.deepcopy(self.r);x['body']['reviewer']=FalseString('urn:evil')
        with self.assertRaisesRegex(d.Invalid,'unsupported JSON value'):d.seal(x)
    def test_non_object_seal(self):
        with self.assertRaisesRegex(d.Invalid,'record object'):d.seal([])
    def test_stale_report_marks_reviews_not_evaluated(self):
        self.s['proposal']=p('other');self.assertIs(self.answer()['reviewsEvaluated'],False)
    def test_snapshot_actor_newline_rejected(self):
        self.s['reviewers'].append('urn:synthetic:reviewer\n')
        with self.assertRaisesRegex(d.Invalid,'actor catalog syntax'):self.answer()


    def test_snapshot_unknown_version(self):
        self.s['version']='unknown'
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()
    def test_snapshot_version_required(self):
        del self.s['version']
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()
    def test_every_answer_binds_evaluator_version(self):
        self.assertEqual(self.answer()['evaluatorVersion'],d.VERSION)
        self.s['proposal']=p('another')
        self.assertEqual(self.answer()['evaluatorVersion'],d.VERSION)
    def test_cross_type_identity_on_inspection(self):
        self.r['id']=self.p['id'];self.r['revision']='2';self.reseal_review()
        with self.assertRaisesRegex(d.Invalid,'identity changes type'):self.answer()
    def test_active_supersession_with_forged_digest(self):
        prior=copy.deepcopy(self.r);self.r['revision']='2';self.r['body']['supersedes']=d.pin(prior);self.r['body']['supersedes']['digest']='sha256:'+'0'*64;self.r=d.seal(self.r)
        # A distinct successor ID avoids the independent one-active-revision rule.
        self.r['id']='urn:synthetic:successor';self.r=d.seal(self.r);self.s['activeReviews']=[d.pin(prior),d.pin(self.r)]
        with self.assertRaisesRegex(d.Invalid,'incoherent supersession pin'):self.answer(reviews=[prior,self.r])
    def test_future_assessment_reason(self):
        self.assertEqual(self.answer(now='2026-09-21T10:00:30Z')['ignored'][0]['reason'],'future-assessment')
    def test_not_yet_valid_reason(self):
        self.r['body']['validFrom']='2026-09-21T13:00:00Z';self.reseal_review()
        self.assertEqual(self.answer()['ignored'][0]['reason'],'not-yet-valid')
    def test_expired_reason(self):
        self.assertEqual(self.answer(now=self.r['body']['validTo'])['ignored'][0]['reason'],'expired')
    def test_import_reversing_supersession_time(self):
        prior=copy.deepcopy(self.r);prior['body']['reviewedAt']='2026-09-21T10:02:00Z';prior['body']['validFrom']='2026-09-21T10:02:00Z';prior=d.seal(prior)
        nxt=copy.deepcopy(self.r);nxt['revision']='2';nxt['body']['supersedes']=d.pin(prior);nxt=d.seal(nxt)
        with self.assertRaisesRegex(d.Invalid,'supersession time reversal'):d.import_records([],[self.p,prior,nxt],self.p['dimension'],self.c)
    def test_import_cross_proposal_supersession(self):
        other=copy.deepcopy(self.p);other['id']='urn:synthetic:other-proposal';other=d.seal(other)
        nxt=copy.deepcopy(self.r);nxt['revision']='2';nxt['body']['proposal']=d.pin(other);nxt['body']['supersedes']=d.pin(self.r);nxt=d.seal(nxt)
        with self.assertRaisesRegex(d.Invalid,'supersession crosses proposal identity'):d.import_records([],[self.p,other,self.r,nxt],self.p['dimension'],self.c)
    def test_duplicate_stored_revision(self):
        with self.assertRaisesRegex(d.Invalid,'duplicate stored revision'):d.import_records([self.p,self.p],[],self.p['dimension'],self.c)
    def test_import_review_before_capture(self):
        self.p['body']['capturedAt']='2026-09-21T10:02:00Z';self.p=d.seal(self.p);self.r['body']['proposal']=d.pin(self.p);self.r=d.seal(self.r)
        with self.assertRaisesRegex(d.Invalid,'review predates proposal'):d.import_records([],[self.p,self.r],self.p['dimension'],self.c)
    def test_partial_disposal_breaks_internal_links(self):
        with self.assertRaisesRegex(d.Invalid,'unresolved internal pin'):d.import_records([self.r],[],self.p['dimension'],self.c)
    def test_string_bound(self):
        with self.assertRaisesRegex(d.Invalid,'string'):d.canonical('a'*4097)
    def test_depth_bound(self):
        x=0
        for _ in range(22):x=[x]
        with self.assertRaisesRegex(d.Invalid,'depth'):d.canonical(x)
    def test_container_bounds(self):
        for x in ([None]*129,{str(i):None for i in range(129)}):
            with self.subTest(container=type(x).__name__),self.assertRaises(d.Invalid):d.canonical(x)
    def test_actor_list_substring_does_not_authorize(self):
        self.s['reviewers']=['urn:synthetic:reviewer-longer']
        self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_optimized_module_still_rejects_schema_version_mismatch(self):
        import tempfile,subprocess
        with tempfile.TemporaryDirectory(prefix='disclosure-version-test-') as tmp:
            root=Path(tmp);(root/'disclosure.py').write_bytes(Path(d.__file__).read_bytes())
            schema=copy.deepcopy(d.SCHEMA);schema['$defs']['proposal']['properties']['version']['const']='wrong'
            (root/'disclosure.schema.json').write_text(json.dumps(schema),encoding='utf-8')
            run=subprocess.run([sys.executable,'-O','-c','import disclosure'],cwd=root,capture_output=True,text=True)
            self.assertNotEqual(run.returncode,0);self.assertIn('schema/version mismatch',run.stderr)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ResearchPrototype);result=unittest.TextTestRunner(verbosity=2).run(suite)
    examples=Path(__file__).with_name('examples');examples.mkdir(exist_ok=True)
    for profile in ('startup','matrix','ai'):
        a,b,s,c=fixture(profile);(examples/(profile+'.json')).write_text(json.dumps({'fixtureKind':'synthetic-host-internal-only; never accept hostSnapshot or capabilities from a request','proposal':a,'reviews':[b],'hostSnapshot':s},indent=2)+'\n',encoding='utf-8',newline='\n')
    report={'status':'passed' if result.wasSuccessful() else 'failed','passed':result.wasSuccessful(),'testsRun':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'scope':'Codex reference behavior checks; native integration has a separate report; no privacy/security conformance','codeSha256':hashlib.sha256(Path(d.__file__).read_bytes()).hexdigest(),'inputHashes':{n:hashlib.sha256(Path(__file__).with_name(n).read_bytes()).hexdigest() for n in ('disclosure.py','disclosure.schema.json','test_disclosure.py','README.md')},'exampleHashes':{x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in examples.glob('*.json')},'python':sys.version,'jsonschema':importlib.metadata.version('jsonschema')}
    Path(__file__).with_name('test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    raise SystemExit(not result.wasSuccessful())

</file>
END FILE test_disclosure.py

## FILE tool-pins.json
ORIGINAL SHA256 14d54b08bdbe854a00eda39b8643c73473445312bf2ea4902954eaf716bd9ae7
<file>
{"composerVersion":"0.1.1","composerFiles":{"composition.py":"78aa1c6c29f14c7adedefd7dd8b3683c845118c49bb48d04c5e92ae4989ce06e","bootstrap_dimension.py":"5eb5491ecedcfa56ffe63d07383e9a650eed42a5d73f667c2feb2f34ea5180f5","composition-plan.schema.json":"cc33e9ee4522cd586a2e1fb07307e6aa5361bf7cf3ca99a419c0f434d0e8a079","policy.schema.json":"92e0386696c974b1e8a312b60ca08d981c223e9925c8f70dabdfa135b9041543"},"skillFiles":{"SKILL.md":"bbd714f5a0de9fad7b26df12be7fb31ce5935f3f54f3cd1037688121383cf963","agents/openai.yaml":"f7234977b2cb542bc0fb1e7665a8a27684e0fa1400696dd6e086b4fef3829cb0","mcp/server.py":"ef3b937e4ebcaa5d737f03f11e6ce5e0be80885e184c88a555e7a0d7b4c0e133","references/autonomous-runtime.md":"ae9d728a214cb296dd97b9d172b60651270e77afcbab632fce04e84dd0a3453a","references/compatibility.md":"b7c0b0ee6d16084f1422b9cb813d23c3f03cc45d047d17a43568067ebde34460","references/concept-map.md":"c216fc5ffd94a55a254f2b61e1ef5630eb8ec09a5ae70db1617318662c43c3a1","references/dimension-bootstrap.md":"7ab614fd1eba0326861d7d2d36cd690b99f26dd0f3333190401bf0782d8a6ed7","references/federation-routing.md":"fb025d2cc62db14c553e0b364c70a47e6385d519d419dec706fb6cf483658159","references/mcp-server.md":"7d1233ea34b34e927acf352c12bc367f58fda5bde249fb3e5e99aa05cff724ad","references/memory-autostart.md":"d3b831e39f2dd5f32abc97d9748ef426e72c3f31e7dbcfff65296b4bf7de5e2e","references/model-lifecycle.md":"9689f560884e12092ffa1fe0068e28f603095b6ffe8c719493f8f595fb3a06ee","references/model-resolution-api.md":"f008dc97daa193b827b9eab76dbc574f104f8d464909cd5d0e71cb8a97749261","references/presets.md":"71503847c1d67f1a227600cce96e5941ea4f3ac1cda1575fe849f18815962cb2","references/public-entry.md":"15155eec00a259dfdf6a0469ccaceba444fcba635f1a42080b36063d924d22a6","references/runtime-records.md":"71c495b38db59f048fe1ec27cd54e608adfeee5160e4d96141b18e43d6b1e809","references/storage-selection.md":"2dd3b10bab2235d04fd3b7cf5411249bf54774efc734b9d08f93483c546bcc5a","references/validation.md":"8c35e27e4fc6103b489ad8b34bd7b79eeb86a8e557752726e8f351ab4edfc9d0","references/whole-object.md":"17d9a1275015c0152267f5a4a39659244ed16c25e81e748256a9324dc5bb7b66","schemas/compatibility.schema.json":"bb32246583b04cedaff9d5e2aae75cca6e9afa014d73a6d4fcc9306054dec78a","schemas/conflict-policy.schema.json":"dece868961a56fe0f50b93564986fb5862b5cbca6ecba138db894f9ea8f6a6c5","schemas/dimension.schema.json":"b6645174e73f551d7bf27642c1887538a8e6d695d586d5101995e69dfa42ce57","schemas/event.schema.json":"e0fbf7551d3b409bf8c04aad6cb6e2caa1dcbf3e703cee9ffe6ab23664f38db6","schemas/fact.schema.json":"f15f9f652c44547384ed8ca7c0c5454a73ea7385de3ec18d8fed09502994ad0a","schemas/object.schema.json":"ff7cab00542db5388946d0704b9aa3c33a49fc8057ec1df6ace7be00e1e43a0a","schemas/relation.schema.json":"2b3b97267fbc400492948886af21010fd6592752c547269f723e7b989279135a","schemas/runtime-model.schema.json":"2ce263747b220d16980bea70f1bca9c3bba59eeec90233d6c9b880759a902c42","scripts/build_index.py":"807539c6d4522d0cbf8782e3a1466a471fa36895cb304b21ee704cb513112319","scripts/create_dimension.py":"4cc00b03be88e9a2348eb681137d0b813b10aa0b76edc881f3e9ecf8345d5b8f","scripts/migrate_dimension.py":"daae4db10760e9d44380c0606d016557ac3e52401f3a711ee11b5ad8c053f02a","scripts/poll_model_requests.py":"91c4aede63bb2eee48e5d49fcdf59d75b0e23eb12511d012c419eb141167fea9","scripts/query_dimension.py":"0c6e35345a91bdd85b7b129fedbb35f4359f6d786b39b927cc92870b65209c0c","scripts/reconcile_models.py":"4fcf76ebaa08ebdbefd2f9ac6824337f8f7d0e9d0c05329f4b3b1669f6260236","scripts/register_memory.py":"9479de2b71669042a73a2393280cc99c096795bf79f0a7eb3294025d2e82e406","scripts/resolve_model_need.py":"25fb98bd2549c0bb7b743cebb62e666a14acd1bd7fa1a2de8548ae9f1d901d5d","scripts/select_storage.py":"c08cdc15374cc496711cb2a6d3403808c008415abccfa3f3cf12f3015df400d3","scripts/self_test.py":"fe9b493b5e7c33a58f97c4fe8c1b01b3457e5eca6e5e2732fbd3497bae402158","scripts/validate_dimension.py":"815a938361420373b18448dda4caa5604d314230cf53fc6a07a9dcb96dd57df4","scripts/vercy.py":"80e31ef4d4e02bab94859163f7975cbe9678e0b31db7d51ae7acd8506b65e20d","scripts/vercy_runtime.py":"e538c64b9c824b503768b63dba5dc66a81c19ac7626eb9116579ba2925528664","scripts/write_record.py":"c60274820fd3e5a55ec790f7e64fb0e0a7e218b7fe107f02d0fcb125091da4e5","assets/dimension/AGENTS.md.template":"b435e4bc805e2aa084c648167350fd050993dab0aaa1d194697558de5586f69d","assets/dimension/compatibility.yaml":"41244d13b2e8763f2f23c44f1ffefc7dde4801b4a54f5faa852d977e0f648a4f","assets/dimension/context-routing.yaml":"52f3a4f8951e2faf3be8d6bd23af51fdfc477a347cc79db55bbcd3d717cd3f67","assets/dimension/dimension.yaml":"e92c299d857962293f2a1c13d70717beff0ec955b3ab84ea1e2763d2cff3b1d7","assets/dimension/federation.yaml":"358bf49507eb3f5c1e9fb86e45d9cc0ee9d14a8dc371f3af95af56dab0e6327b","assets/dimension/memory.yaml":"50d47c53ee2be80d293a051c7c909cb2afdf8204f9a76eadfe5673eb6cd589b4","assets/dimension/vercy.lock":"f360ae2f60e1d3f02bda506c3aed9587d6435a7d0200bef542888df32b469c99","assets/icons/vercy-logo-1024.png":"8043b9a7080d1b64fea402ba0db8d42efb366862214fc1d68d8a99086401a705","assets/icons/vercy-logo-512.png":"3832e0a25cec92cf22392a27c44b37524213844598c61a12d5032e3fea5fd690","assets/presets/ai-subject.yaml":"ed547e7628d8c4509ed1873312b45f0521036b5235a3b795a2f2a0e4a147c3b7","assets/presets/index.yaml":"69e79eb66cec03ab07badb301b0b4ebfb15b74b34daffeae78e7f11529140892","assets/presets/kernel.yaml":"b699f89fc1d040e05584bb21e00a419a7704230caba42adc37cb70631defb43d","assets/presets/organizational.yaml":"e70c6d196f1b5626f2e7646252dad4f2be961b7908ae198e9bc1d405cffad2a3","assets/presets/personal.yaml":"c201473267e64958b9844e3557f8efc95b8be790581135c42c8c38566c841483","assets/presets/reality.yaml":"2779668f8eeca66b74ff31527c323d3461f821089769ef5d7951c13afbfcad66","assets/dimension/bindings/storage.yaml":"044db01cf746678283a98c96be0d1fb8a94997393b9161a5a32e59dfc813ba5c","assets/dimension/data/index.md":"f10a3c8283ddc1ae608c6848cd561ac9b9d80a05ca684420ac185fa920b8b351","assets/dimension/migrations/index.yaml":"9a20ae6fef67ca51d4c07a27558deb20af2a7b3dafe76893783ac01e86c0dce6","assets/dimension/policies/access.yaml":"3b58ce30f6de01923dbbab069df0721552c3b9ab8ba405c30ac353ffb392779f","assets/dimension/policies/autonomy.yaml":"6629691e60540e42eabeb63f746bcb99f79f383d7c85a57217e551d4ecc6ea27","assets/dimension/policies/conflict-resolution.yaml":"241e97baa79198e4b02885f24ad1143b7ebfc3dbf52dc07e4bccb01ef31c72b2","assets/dimension/policies/lifecycle.md":"91755112dd7854a7cb06598fcb53233c68b626bb015ca7f5a3a9307258eab232","assets/dimension/policies/model-deployment.yaml":"637fc3ac655b7f5c2f36c814113b03803bce4366e62cb24bbeb4f36dba525771","assets/dimension/registries/events.yaml":"8babba185339394a775d953024c857f6bcd4f6c1037bff9019af5c8512435fef","assets/dimension/registries/meta-models.yaml":"4efb434d716f2c10a1c01deb79e44873ced31599446edab8b213e3fd7201206b","assets/dimension/registries/meta-objects.yaml":"c1b417a3019d93c594dae9854951d57c3fcd73d73a88f258b3a13c8cb5e7e3d3","assets/dimension/registries/model-links.yaml":"ecbac80f14627245ecdc5af12bb30331b88f688e8ebeaa34fba44ddc16e0c898","assets/dimension/registries/model-requests.yaml":"7f01232fd4b812d942eed0e88f154f751e7f9fb1707402a5b6b4aaa16bdba319","assets/dimension/data/events/README.md":"fa20d1960e40eee352679debcab28df245f9bef695ca72a27d28b69ab8e18737","assets/dimension/data/facts/README.md":"80433bcda7964cb8819692bd442628f56b35aa6fca96bfde0d527b2d3ed38138","assets/dimension/data/objects/README.md":"264ebb5440729741322828fd5e3c8a747c77a1662b0e64ab5ff9ce1a978ff4b8","assets/dimension/data/relations/README.md":"d7a7d3e09a3c8d0c2e0304ffe89e5fa01ad9bde730497185a7a9da7d5bf51a22","assets/presets/organizational/commercial-company.yaml":"ce8ee74e8fa61eec9583471f6b4982e920d172af3299bbfc2ed08163a6cbde2b","assets/presets/organizational/community.yaml":"31cabe5a146e2b38d173f2cb08f7e5d0df60bbcf7f273082ba97b0dd7560f001","assets/presets/organizational/family.yaml":"094438b226ed56859c72327d354e55e6ed2cd6c2658a1423ad345c326ac1a9c9","assets/presets/organizational/state.yaml":"a2aaac7f20feaffe2494406ddc5b71629027fed6c04e94f65950dac991f6ff13"}}
</file>
END FILE tool-pins.json

## FILE whole-object-coverage.yaml
ORIGINAL SHA256 66f81e0647897b1c8ee77a6798bec3a26fe756fdc38c0b8eaf0c9e53a21eba77
<file>
{"canonicalFacets":["identity-class","direct-properties","recognition-observation","capabilities-behaviour-actions","context-evidence"],"types":{"ContextPackageProposal":{"identity-class":{"status":"required","coverage":"Format/version, Dimension, qualified proposal ID, opaque revision, content digest; one collection, independent from its members' object identities."},"direct-properties":{"status":"required","coverage":"Finite exact member/field set and all audience/purpose/environment/context pins; schema supplies type, cardinality and nullability."},"recognition-observation":{"status":"required","coverage":"Author and capture time state who recorded which exact source revision/context. Host identity resolution and truth remain external, with no unpinned delegated-type claim."},"capabilities-behaviour-actions":{"status":"required","coverage":"Seal, validate, import immutable revisions, inspect applicability against a trusted snapshot; these operations do not grant access or deliver values."},"context-evidence":{"status":"required","coverage":"Exact source/schema/shape/classification/prior-release/custody pins. The host resolves them independently."}},"JointDisclosureReview":{"identity-class":{"status":"required","coverage":"Independent review ID/revision/digest and exact proposal reference; reviewer and assessed object are distinct roles."},"direct-properties":{"status":"required","coverage":"Verdict, risk statement, assessment/validity times and optional supersession pin."},"recognition-observation":{"status":"required","coverage":"Method/evidence pins and assessed proposal establish the declared observation context; no calibrated confidence or inference-prevention proof."},"capabilities-behaviour-actions":{"status":"required","coverage":"Record a verdict, correct through another immutable revision, validate internal references, count or exclude it under current host state; no authorizing or deleting action."},"context-evidence":{"status":"required","coverage":"Reviewer/authority/method/evidence pins, relation to proposal and previous review, current authority and completeness supplied by host snapshot."}}},"embeddedValues":"Members, fields and pins have no independent exported lifecycle; diagnostics are ephemeral. Physical dimensions do not apply to these information records."}
</file>
END FILE whole-object-coverage.yaml

END COMPLETE FROZEN CANDIDATE. Return verdict and actual read scope.
