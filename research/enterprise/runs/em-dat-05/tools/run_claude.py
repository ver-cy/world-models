from __future__ import annotations

import subprocess
from pathlib import Path

RUN = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models\research\enterprise\runs\em-dat-05")
dossier = (RUN / "provider-dossier.json").read_text(encoding="utf-8")

prompt = f"""You are the independent architecture reviewer for Vercy's Enterprise metamodel programme.

Review the frozen dossier for EM-DAT-05, Metric, target and observation. Choose exactly one: REUSE ONLY, PROFILE, EXTEND, or NEW MODEL.

The central question is whether Vercy lacks a reusable cross-domain Metric Definition aggregate. Do not mistake these neighboring authorities for that aggregate:
- WM-XCT-025 is a reusable observation-result field group;
- WM-DAT-010 owns a time-series/observation collection;
- WM-KNW-011 owns goals and target commitments while excluding metric definitions;
- WM-DAT-007 owns quality-assessment metrics and rules in that bounded context;
- WM-DAT-002 owns official-statistics product semantics.

Test:
1. stable metric identity versus immutable definition versions;
2. formula/expression, numerator, denominator, unit, scale, direction and aggregation;
3. dimension definitions, population and inclusion/exclusion boundaries;
4. measurement method and data-source bindings;
5. zero vs unknown vs not-applicable vs missing vs suppressed;
6. compatibility and comparability when formula, method, unit, population or dimensions change;
7. separation of metric definition, target commitment, observation, series, assessment and report;
8. acceptance scenario: two methods, a missing period and recalculation, with explicit comparable/non-comparable outcomes.

Assess alignment, without claiming conformance, to SDMX information-model practice, W3C RDF Data Cube / QB observations, SOSA/SSN observation patterns, QUDT or UCUM unit binding, and PROV-O version/provenance. Use only evidence present in the dossier.

If NEW MODEL, provide a minimal bounded aggregate proposal: identity, owned child records, lifecycle, external references, 10-15 core fields, at least 10 invariants, and three functions. If EXTEND, name the exact existing owner and prove the extension fits its purpose. Be sceptical of absorbing targets or observations into the definition.

Return at most 1100 English words with exact headings:
DECISION
BOUNDARY PROOF
MINIMAL CONTRACT
ACCEPTANCE WALKTHROUGH
HOLDS AND LIMITS
PUBLICATION RECOMMENDATION

FROZEN DOSSIER
{dossier}
"""

completed = subprocess.run(
    ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
    input=prompt,
    text=True,
    encoding="utf-8",
    errors="replace",
    capture_output=True,
    check=False,
    timeout=900,
)
output = completed.stdout.strip()
if completed.stderr.strip():
    output += "\n\nCLI STDERR\n" + completed.stderr.strip()
(RUN / "claude-study.raw.md").write_text(output + "\n", encoding="utf-8", newline="\n")
print({"returncode": completed.returncode, "chars": len(output), "output": str(RUN / "claude-study.raw.md")})
raise SystemExit(completed.returncode)
