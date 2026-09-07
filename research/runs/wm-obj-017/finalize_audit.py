"""Serialize the explicit Codex audit disposition, preserving external output."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

RUN = Path(__file__).resolve().parent
def read(name):
    return json.loads((RUN / name).read_text(encoding="utf-8"))
def digest(name):
    return hashlib.sha256((RUN / name).read_bytes()).hexdigest()
def write(name, value):
    (RUN / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    assert not (RUN / "claude-audit.plan.json").exists(), "finalized audit must not be rerun"
    manifest = read("adjudication-run.manifest.json")
    assert manifest["provider"] == "claude" and manifest["status"] == "complete"
    assert manifest["output_sha256"] == digest("synthesis-plan.json")
    plan = read("synthesis-plan.json")
    assert not plan["critical_conflicts"]
    (RUN / "claude-audit.plan.json").write_bytes((RUN / "synthesis-plan.json").read_bytes())
    (RUN / "claude-audit.manifest.json").write_bytes((RUN / "adjudication-run.manifest.json").read_bytes())
    decisions = [
        ("Aggregate boundary", "accepted", "One reusable configuration revision owns selected assertions and evaluation bindings; family, design, BOM, item, session and offer keep their own masters. Packaging standalone-mm is a separate axis."),
        ("Frozen CLASSIFIES relation", "accepted", "REFERENCE explicitly carries CLASSIFIES semantics toward WM-OBJ-001 because the research relation enum has no CLASSIFIES value. No item identity or state is imported."),
        ("Provider evidence attribution", "corrected", "This model has one 120-second timeout per research provider. Historical policy attempts are not model attempts. Haiku's separate no-tools audit succeeded but no external research result was admitted."),
        ("Source inspection and conformance", "corrected", "Sources support proposed design choices at declared inspection depth. ISO public abstracts do not establish licensed-clause conformance; neither do vocabulary references establish tested implementation conformance."),
        ("Physical and functional description", "accepted", "The proposed property and capability contracts require evidence, units and conditions. Nominal properties do not describe an instance's observed position, condition or safety."),
        ("Engineering composition mastership", "accepted", "Four boundary notes retain external design and BOM authority. Selected composition references may qualify occurrences and quantities without taking ownership of the BOM."),
        ("Evaluation and release", "accepted", "Completeness, feasibility, availability and authority are distinct results. Unknown or timed-out evaluation cannot authorize release. Imported expressions require an authorized bounded adapter."),
        ("New solver or standards prescriptions", "rejected", "The no-tools audit cannot introduce new source claims or mandate named commercial solvers. Keep a vendor-neutral evaluator profile and defer uninspected domain standards."),
        ("Interchange and retention", "accepted", "No universal lossless mapping is claimed. Required unsupported semantics cause rejection or explicit sidecar handling; retirement retains dependent-item interpretation under access and minimization policy."),
    ]
    plan["boundary_decision"]["rationale"] = decisions[0][2]
    plan["decisions"] = [{"concept": c,"disposition": d,"rationale": r} for c,d,r in decisions]
    plan["publication_holds"] = [
        "Independent Claude and Grok research is absent under owner authorization dated 2026-09-06. Each research attempt timed out once at 120 seconds. A separate Claude Haiku no-tools audit completed; its factual overstatements were corrected transparently by Codex. This remains reviewable-draft, not canonical.",
        "Source/version and claim-level verification remains qualified: Schema.org is a development vocabulary snapshot; ISO 10007 and AP242 were inspected only through public abstracts, not licensed clauses. No normative standards conformance is claimed.",
        "No real-product fixture, executable instance schema, deployed constraint evaluator or tested crosswalk is included. Adoption requires validated target-specific adapters and explicit loss reports.",
        "Physical properties, recognition and capability limits require sector-specific evidence, measurement conditions and uncertainty. The draft provides no certification or safe-actuation authority.",
        "Actual variant creation and release require an owning Dimension with declared roles, access policy, engineering authority and retention rules; the specification does not instantiate that governance.",
    ]
    plan["deferred_research"] = [
        "Real manufacturer configuration fixtures with incomplete, contradictory, timeout, revised-default and released-baseline cases.",
        "Vendor-neutral solver adapter and executable instance-validation schema with typed quantities, absence states and reproducible receipts.",
        "Target-version mapping and round-trip fixtures, including explicit rule/effectivity sidecars or rejection of unsupported required semantics.",
        "Sector metrology, recognition uncertainty, capability qualification and jurisdiction-specific evidence requirements.",
        "Licensed engineering standards and dictionary inspection before any normative alignment or conformance assertion.",
    ]
    # Corpus typography normalization is mechanical, not a semantic modification.
    plan = json.loads(json.dumps(plan).replace("\\u2014", "-").replace("\\u2013", "-"))
    write("synthesis-plan.json", plan)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write("adjudication-run.manifest.json", {"contract_version":"1.0.0", "model_id":"WM-OBJ-017", "provider":"codex", "provider_model":"current-session-no-tools-disposition", "status":"complete", "completed_at":stamp, "tools_enabled":[], "input_sha256": digest("codex.result.json"), "external_audit_sha256":digest("claude-audit.plan.json"), "external_audit_manifest_sha256":digest("claude-audit.manifest.json"), "disposition_sha256":digest("audit-disposition.md"), "output":"synthesis-plan.json", "output_sha256":digest("synthesis-plan.json"), "note":"Frozen semantic audit and explicit disposition; this script only serializes decisions, not independent research."})
