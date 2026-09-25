import subprocess
from pathlib import Path
W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");D=W/'research/enterprise/runs/em-org-06/provider-dossier.json';O=W/'research/enterprise/runs/em-org-06/claude-study.raw.md'
p="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent identifiers. Review EM-ORG-06 Positions, Roles and Accountability against WM-ORG-004 Position and WM-XCT-023 Party Role. Decide REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, or an identifier-unassigned candidate only with proven independent identity/lifecycle.

Separate durable vacant Position, abstract BusinessRole, scoped PartyRole assertion, occupation/job/grade classifier, person-to-position occupancy, Accountability, DecisionRight, RACI assignment, HeadcountPlan and IAM access role. Decide what each existing model owns and what remains external. Support job sharing and role assertions without a position. A position must survive occupant change and retain authorized FTE/budget. RACI must identify subject/context, role type, party/position, validity and conflict rules. Business roles and RACI may inform authorization but never confer technical permissions. Decide whether Accountability/DecisionRight/RACI need independent identity or are profiles of PartyRole assertions; decide whether HeadcountPlan is intrinsic position capacity or a separate planning fact.

Walk the negative case where deleting an employee deletes the position and budget. Walk acceptance: occupant changes preserve position; one person plays two roles; two fractional occupancies fill one position where allowed. Return at most 1100 words with headings Verdict per type; Evidence state; Identity/mastership; Position/occupancy/capacity; Business role and PartyRole; Accountability/RACI/IAM boundary; Invariants; Scenario walkthrough; Profile shape; Gaps and publication holds. Do not claim canonical status, approved relations or installability.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=p,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode:raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8');print(O);print(O.stat().st_size)
