import subprocess
from pathlib import Path
WORLD=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
D=WORLD/"research/enterprise/runs/em-lnd-06/provider-dossier.json"; O=WORLD/"research/enterprise/runs/em-lnd-06/claude-study.raw.md"
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent IDs. Decide among REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, or RETIRE for EM-LND-06 Software Product Landscape. PLMM already has reserved id vr.vercy.plmm but runtime 0.1.0-legacy is non-installable with an empty bundle projection; a richer pinned PLMM repository draft exists. AISMM runtime and pinned repository both currently say 3.1.0; explicitly determine whether the historical 3.2 mismatch still exists in this dossier. WM-XCT-039 is a narrower Managed IT Service Graph. Decide what PLMM may master independently (landscape membership/dependencies/completeness/impact routing) without copying product internals or creating a second SoftwareProduct. Test LandscapeMembership and LandscapeDependency identity/lifecycle, version-pinned dependency edges, incomplete graph/unknown impact, tenant/service graph specialization, and exact migration from legacy bytes. Walk the negative case (legacy install called canonical) and acceptance case (three products/shared platform impact graph with visible gaps). Return at most 1200 words with headings Verdict; Evidence state/version reconciliation; Boundary; Membership/dependency/completeness contract; Migration path; Invariants; Scenario walkthrough; Gaps and publication holds. Do not claim installability or compatibility without evidence.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode: raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8'); print(O); print(O.stat().st_size)
