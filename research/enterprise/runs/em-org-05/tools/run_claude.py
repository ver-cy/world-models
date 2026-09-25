import subprocess
from pathlib import Path
WORLD=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");D=WORLD/'research/enterprise/runs/em-org-05/provider-dossier.json';O=WORLD/'research/enterprise/runs/em-org-05/claude-study.raw.md'
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent identifiers. Review EM-ORG-05 Collectives, Teams and Membership against WM-ORG-003 Team and WM-ORG-006 Membership. Decide REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, MERGE/RETIRE DUPLICATE, or NEW MODEL CANDIDATE WITH IDENTIFIER UNASSIGNED only if independent identity/lifecycle is proven.

Resolve overlap between WM-ORG-003's nested membership-assignment and WM-ORG-006's governed membership relationship. Distinguish team staffing/participation assignment from formal membership/belonging, employment, office/post occupancy, project participation, subscription and access entitlement. Decide how Team, temporary inter-company team, Collective and CommunityOfPractice map without duplicating participants. Test whether WM-ORG-003's exactly-one containing organization prevents inter-company collectives and whether a profile can replace it with sponsor/managing organization roles while retaining a single record authority. Decide whether WorkingAgreement is a referenced knowledge artifact or an owned team charter component. TechnicalDomain may be a classifier or a governed practice/community subject; state the test.

Membership must have identity, member/group refs, scheme/type, admission basis, validity, standing, role binding and provenance. No membership or participant list grants employment, funding, product access or authority. Walk the negative case where a community member gets access to all products of other members. Walk the acceptance case with a temporary inter-company team and a permanent community, keeping membership, employment and access independent. Return at most 1200 words with headings Verdict per model/type; Evidence state; Root identities and lifecycle; Membership mastership; Inter-company and community profile; Working agreement and technical domain; Invariants; Scenario walkthrough; Migration/profile shape; Gaps and publication holds. Do not claim canonical status, approved relations or installability.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode:raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8');print(O);print(O.stat().st_size)
