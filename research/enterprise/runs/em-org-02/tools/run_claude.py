import subprocess
from pathlib import Path
WORLD=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
D=WORLD/'research/enterprise/runs/em-org-02/provider-dossier.json'; O=WORLD/'research/enterprise/runs/em-org-02/claude-study.raw.md'
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent identifiers. Review EM-ORG-02 Legal Identity and Registration across current WM-ORG-001 Organization, WM-ORG-010 Legal Entity Registration and WM-ORG-011 Business Establishment / Branch. Decide REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, MERGE/RETIRE DUPLICATE, or an identifier-unassigned candidate only if independent identity and lifecycle are proven.

Resolve the overlap: WM-ORG-001 currently carries identity, legal form, registration, standing, lifecycle and succession, while WM-ORG-010 claims a register-anchored legal entity with registration facts. Decide one master for organization/legal-subject identity and one for each registration record, and prevent duplicate LegalEntity. Separate subject status, registration-record status, LEI, tax/VAT identifier, national register number and evidence extract. Test identifier equality only within scheme + authority/jurisdiction + validity. Distinguish a branch with registration but no separate legal personality from an independent legal entity and from an operating establishment/premises. Decide the role of WM-ORG-011. Preserve historical parties through merger/split/conversion; succession must not rewrite old contracts.

Walk the negative case where a new extract or second register creates a duplicate company. Walk the acceptance case: one subject has three registration/identifier records, a non-person branch, and a merger; answer correctly as-of historical time. Return at most 1200 words with headings Verdict per model; Evidence state; Identity/mastership reconciliation; Registration and identifier contract; Branch/establishment boundary; Succession and temporal rules; Invariants; Scenario walkthrough; Migration/profile shape; Gaps and publication holds. Do not claim canonical status, legal effect, approved relations or installability.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode:raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8');print(O);print(O.stat().st_size)
