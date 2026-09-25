from __future__ import annotations

import csv
import json
from pathlib import Path

REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
RUN = REPO / "research" / "enterprise" / "runs" / "em-fac-01"
RUN.mkdir(parents=True, exist_ok=True)
MODELS = {
    "WM-BLT-006": "wm-blt-006-facility",
    "WM-BLT-008": "wm-blt-008-site-campus",
    "WM-BLT-001": "wm-blt-001-building-structure",
    "WM-PLC-010": "wm-plc-010-gazetteer-place",
}
KEYWORDS = ("identity", "composition", "address", "geometry", "location", "occup", "capacity", "access", "operat", "lifecycle", "contain", "space")


def load(slug: str) -> dict:
    text = (REPO / "publications" / slug / "spec.yaml").read_text(encoding="utf-8")
    return json.loads(text[text.index("{"):])


def compact(slug: str) -> dict:
    data = load(slug); findings=[]
    for bundle in data.get("structure", {}).get("bundles", []):
        for layer in bundle.get("layers", []):
            for finding in layer.get("findings", []):
                text=(finding.get("id","")+" "+finding.get("name","")).lower()
                if any(k in text for k in KEYWORDS) and len(findings)<12:
                    findings.append({"id":finding.get("id"),"name":finding.get("name"),"description":finding.get("description")})
    adjudication=data.get("researchAdjudication") or {}
    return {"publication":data.get("publication"),"metaModel":data.get("metaModel"),"model":data.get("model"),"selectedFindings":findings,"composition":data.get("composition"),"publicationHolds":adjudication.get("publicationHolds") or []}


with (REPO / "planning" / "VERCY-UNIFIED-MEGA-REGISTRY.csv").open(encoding="utf-8-sig", newline="") as handle:
    rows={r["model_id"]:r for r in csv.DictReader(handle) if r.get("model_id") in {"WM-BLT-002","WM-PLC-009"}}

dossier={
    "contour":{
        "id":"EM-FAC-01","name":"Place, office and workplace",
        "scope":"Geographic place, managed site, facility, building, premises/space and workplace designation/allocation. Lease, legal branch, asset ownership and person assignment remain external.",
        "questions":["When is office a physical place versus an organizational function?","How are remote, shared and client-site workplaces represented?","How can address change without replacing site identity?"],
        "invariants":["Address is not the sole identifier.","A place or office is not a legal branch.","Workplace designation and allocation are effective-dated.","A remote worker's home address is not automatically a company office or public fact."],
        "acceptanceScenario":"A hybrid team uses a leased office, remote workplaces and a client site without requiring the company to own any building or publishing home addresses.",
        "decision":"Choose REUSE/PROFILE/COMPLETE RESERVED MODEL/NEW MODEL/LANDSCAPE. Decide the roles of reserved WM-BLT-002 Premises / Spatial Unit and WM-PLC-009 Indoor Space, and whether workplace allocation needs its own relationship model.",
    },
    "plannedRegistryEntries":rows,
    "consumerSignals":[
        "WM-BLT-006 explicitly excludes room/space geometry and occupancy assignment to a Space model.",
        "WM-BLT-001 has a candidate CONTAINS relation to WM-BLT-002 and states independently governed premises keep their own identity and lifecycle.",
        "WM-OBJ-001 references WM-BLT-002 as the master for premises identity, geometry and address semantics.",
        "WM-ORG-005 Employment stores source-qualified workplace/remote/mobile/cross-border context but does not own workspace identity.",
        "WM-ACT-040 Onboarding/Offboarding treats Workspace and Facility as external masters.",
    ],
    "models":{mid:compact(slug) for mid,slug in MODELS.items()},
}
out=RUN/'provider-dossier.json'; out.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'output':str(out),'bytes':out.stat().st_size}))
