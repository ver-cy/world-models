import subprocess
from pathlib import Path
WORLD=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");D=WORLD/'research/enterprise/runs/em-org-04/provider-dossier.json';O=WORLD/'research/enterprise/runs/em-org-04/claude-study.raw.md'
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent identifiers. Review EM-ORG-04 Organizational Unit and Mandate against current reserved WM-ORG-002. Decide REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, or NEW MODEL CANDIDATE WITH IDENTIFIER UNASSIGNED only if independent identity/lifecycle is proven.

Test OrganizationalUnit identity separately from its name, mandate and placements. Decide whether UnitMandate is intrinsic, a temporal assignment, or an independent aggregate. Model StructuralPlacement as a time-, axis- and scenario-qualified edge: administrative, functional, legal, cost and reporting axes must coexist without overwriting one another. Distinguish asserted current structure, historical as-of replay, approved future structure and hypothetical scenario. A cross-functional product team or community must not be forced into one administrative parent or mistaken for a unit. Management placement must never determine employer/legal entity. Reorganization must preserve unit identity across rename/reparent and create explicit lineage for merge/split/disband. Test acyclicity per axis, scenario and validity interval.

Walk the negative case where a cross-department product team is assigned one administrative parent. Walk the acceptance case where an as-is/to-be reorganization preserves old assignments and introduces no cycle in one selected axis. Decide whether the existing WM-ORG-002 already owns all required semantics or needs a narrow Enterprise profile, and identify any unsupported scenario semantics. Return at most 1100 words with headings Verdict; Evidence state; Identity and aggregate boundary; Placement/axis/scenario contract; Mandate and authority; Temporal/reorganization rules; Invariants; Scenario walkthrough; Profile shape; Gaps and publication holds. Do not claim canonical status, approved relations or installability.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode:raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8');print(O);print(O.stat().st_size)
