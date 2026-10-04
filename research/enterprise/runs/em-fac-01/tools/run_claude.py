from __future__ import annotations

import subprocess
from pathlib import Path

RUN = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models\research\enterprise\runs\em-fac-01")
dossier = (RUN / "provider-dossier.json").read_text(encoding="utf-8")
prompt = f"""You are the independent architecture reviewer for Vercy's Enterprise metamodel programme.

Review the frozen dossier for EM-FAC-01, Place, office and workplace. Choose one or a precise combination of REUSE, PROFILE, COMPLETE RESERVED MODEL, NEW MODEL, and LANDSCAPE.

Determine the smallest coherent enterprise composition across Gazetteer Place, Site/Campus, Facility, Building, the reserved WM-BLT-002 Premises / Spatial Unit and reserved WM-PLC-009 Indoor Space. Resolve any overlap between the two reserved entries rather than creating synonyms.

Test:
1. physical place/site/facility/building/space identities and containment;
2. office as a usage/designation role versus an organization/legal branch;
3. stable site identity across address change;
4. leased office and client site without ownership of the building;
5. remote/home workplace without publishing or converting a home address into a company office;
6. shared desk/coworking/hotelling and time-bounded workplace allocation;
7. distinction between premises identity, occupancy/use designation, allocation, lease, employment context and access grant;
8. whether workplace allocation needs an independent relationship/event identity or belongs as an assertion profile of an existing model.

If completing WM-BLT-002, give its minimal identity, lifecycle, core fields and invariants, and state what happens to WM-PLC-009. If proposing another model, prove independent identity and lifecycle. Do not absorb lease, legal entity, employment, person, credential or booking lifecycles.

Return at most 1100 English words with exact headings:
DECISION
BOUNDARY AND OVERLAP RESOLUTION
MINIMAL CONTRACTS
ACCEPTANCE WALKTHROUGH
PRIVACY AND AUTHORITY RULES
HOLDS AND PUBLICATION RECOMMENDATION

FROZEN DOSSIER
{dossier}
"""
result = subprocess.run(
    ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
    input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, check=False, timeout=900,
)
output = result.stdout.strip()
if result.stderr.strip():
    output += "\n\nCLI STDERR\n" + result.stderr.strip()
(RUN / "claude-study.raw.md").write_text(output + "\n", encoding="utf-8", newline="\n")
print({"returncode": result.returncode, "chars": len(output), "output": str(RUN / "claude-study.raw.md")})
raise SystemExit(result.returncode)
