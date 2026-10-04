import subprocess
from pathlib import Path
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
D=REPO/"research/enterprise/runs/em-leg-03/provider-dossier.json"; O=REPO/"research/enterprise/runs/em-leg-03/claude-study.raw.md"
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent IDs. Decide REUSE ONLY, PROFILE or NEW MODEL for EM-LEG-03 Internal policies and exceptions. Resolve the apparent overlap between WM-ORG-019 Organization Policy and WM-KNW-012 Policy/Rule: preserve both only if each has a non-duplicated identity/lifecycle, otherwise identify duplicate/retirement or profile direction. Test PolicyVersion, PolicyAdoption, PolicyException and Acknowledgement identities. Distinguish reading/acknowledgement from compliance/control evidence. Model global group policy, local tightening and time-bounded exception so one applicable rule is computable at a date without silently overriding stronger law or local rules. Walk the negative and acceptance cases. Return at most 1100 words with headings Verdict; Boundary and duplicate analysis; Adoption/inheritance/exception rules; Required profile; Invariants; Scenario walkthrough; Gaps and publication holds. A profile gets no new ID.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode: raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8'); print(O); print(O.stat().st_size)
