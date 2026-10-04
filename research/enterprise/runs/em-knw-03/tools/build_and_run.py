import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-knw-03"
IDS = {"WM-ACT-025", "WM-REC-012", "WM-ACT-027", "WM-REC-010", "WM-KNW-010", "WM-ACT-024", "WM-ACT-006"}


def read_json(path): return json.loads(path.read_text(encoding="utf-8-sig"))
def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def full_spec(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": yaml.safe_load(raw.decode("utf-8-sig"))}
def text_doc(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}

registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
rec12 = W / "publications/wm-rec-012-minutes-transcript/spec.yaml"
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-KNW-03"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-KNW-03"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "target_spec_availability": {"WM-REC-012": {"path": str(rec12.relative_to(W)), "exists": rec12.exists()}},
    "specs": {
        "WM-ACT-025": full_spec(W / "publications/wm-act-025-meeting-session/spec.yaml"),
        "WM-ACT-027_adjacent": full_spec(W / "publications/wm-act-027-communication-interaction/spec.yaml"),
        "WM-REC-010_adjacent": full_spec(W / "publications/wm-rec-010-decision-approval-record/spec.yaml"),
        "WM-KNW-010_adjacent": full_spec(W / "publications/wm-knw-010-decision-rationale/spec.yaml"),
        "WM-ACT-024_adjacent": full_spec(W / "publications/wm-act-024-decision-approval-activity/spec.yaml"),
        "WM-ACT-006_adjacent": full_spec(W / "publications/wm-act-006-task/spec.yaml"),
    },
    "prior_research": {"EM-KNW-02": text_doc(W / "research/enterprise/runs/em-knw-02/local-evidence.md")},
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-KNW-03 Communication and Collaborative Meeting across reserved WM-ACT-025 Meeting/Session and reserved-but-missing-spec WM-REC-012 Minutes/Transcript, comparing WM-ACT-027 Communication Interaction and decision/task authorities. Place Meeting, MeetingParticipation, CommunicationChannel, DiscussionThread and MessageReference. Define the missing WM-REC-012 boundary sufficiently for later completion: durable record identity, draft/approval/correction, transcript versus minutes, agenda/time anchors, attribution, quotation, access/redaction and retention. Distinguish invitation, attendance, presence, participation, vote, assent and approval. Explain what can move from chat/discussion into an official fact, task, proposal or decision, and which authority/evidence is required. Test a discussion that creates a task and proposed decision while only a later authorized decision occurrence changes official status. Preserve access restrictions when quoting source communication. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Meeting/participation; Channel/thread/message; Minutes/transcript; Promotion to official objects; Access and quotation; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
