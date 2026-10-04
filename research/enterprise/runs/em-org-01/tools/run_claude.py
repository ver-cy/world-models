import subprocess
from pathlib import Path

WORLD = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
DOSSIER = WORLD / "research/enterprise/runs/em-org-01/provider-dossier.json"
OUT = WORLD / "research/enterprise/runs/em-org-01/claude-study.raw.md"

PROMPT = """You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent identifiers. Decide EM-ORG-01 Company and Enterprise Group using existing WM-ORG-001 Organization and WM-ORG-012 Inter-organizational Relationship. Allowed dispositions: REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, or NEW MODEL CANDIDATE WITH IDENTIFIER UNASSIGNED. Never allocate an ID.

Test whether Company is only a constrained Organization profile or an independent identity. Then test whether EnterpriseGroup/BusinessBoundary has independent identity and lifecycle or is a contextual, purpose-qualified relationship projection. Separate legal entity, business organization, brand, franchise network, management perimeter, accounting consolidation perimeter, ownership/control graph and statistical enterprise group. A group membership must state basis, purpose, effective interval, evidence and authority. A brand association or common name must never prove control, legal identity or consolidation. Rebranding should preserve organization identity; merger, split, sale and succession require explicit continuity rules. Reconcile WM-ORG-001's organization-side control/group endpoints with WM-ORG-012's relationship mastership without duplicate ownership facts.

Walk the negative case: three organizations sharing one brand are collapsed into one legal entity. Walk the acceptance case: a franchise network and a holding/consolidation group yield different graphs; rebranding does not create a new organization. Decide whether a reusable group boundary/profile can be expressed over WM-ORG-012 without a new model and state the split trigger if not. Return at most 1200 words with headings Verdict; Evidence state; Identity and boundary; Group membership and perimeter contract; Brand/rebranding/succession; Mastership reconciliation; Invariants; Scenario walkthrough; Profile or candidate shape; Gaps and publication holds. Do not claim legal effect, canonical status, approved relations or installability.

FROZEN DOSSIER
""" + DOSSIER.read_text(encoding="utf-8")

result = subprocess.run(
    ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
    input=PROMPT,
    text=True,
    encoding="utf-8",
    errors="replace",
    capture_output=True,
    timeout=900,
)
if result.returncode:
    raise SystemExit(result.stderr)
OUT.write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(OUT)
print(OUT.stat().st_size)
