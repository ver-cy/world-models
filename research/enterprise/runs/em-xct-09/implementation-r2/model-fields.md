# Field catalog

All fields are required in the closed dialect unless their schema explicitly admits null; arrays may be empty subject to semantic rules. Original source meaning remains external; capture/packet/result ownership follows mastership-and-rights.yaml. No physical units apply. Scores are uninterpreted text, not calibrated numbers. Exact syntax is in classification.schema.json.

| Type | Required fields |
|---|---|
| packet | format, version, id, revision, previousDigest, owner, dimensionId, purpose, jurisdiction, knowledgeAt, effectiveAt, targetAt, mode, inference, baseProfile, profile, assignments, crosswalks, snapshots |
| host | format, dimensionId, owner, actor, purpose, packetDigest, validFrom, validUntil, approvals |
| assessment | format, version, assessmentId, packetId, packetDigest, buildId, owner, dimensionId, purpose, knowledgeAt, effectiveAt, targetAt, outcome, checks, assignments, migrationDisposition, candidate, alternatives, approvalBasis, effects, claims |

Snapshot envelope: id, source, sourceRevision, sourceDigest, capture{id,actor,at,method}, payload, digest.

Scheme payload: kind, scheme, version, complete, concepts[{code,definition,status,selectable,validFrom,validUntil}].

Profile payload: kind, id, version, parent(null or snapshot pin), subjectClass, unit, slot, meaning, strength, releasePins, allowed qualified codes, min, max.

Assignment payload: kind, id, revision, subjectId, subjectClass, unit, slot, profile pin, values, origin, method(nullable id/version), score(nullable text), assertedAt, validFrom, validUntil, state, corrects(nullable pin).

Crosswalk payload: kind, id, version, context{unit,purpose,jurisdiction}, complete, entries. Each entry has id, sources, targets, predicate, state, approver(nullable), evidence, validFrom, validUntil, origin, method(nullable), score(nullable), lossNote.

Pins are {id,digest}; CodeReference is {scheme,version,code}. Assessment findings retain rule/outcome/question/evidence; assignment results retain source/selected conformance; alternatives retain full qualified source/target sets, applicability, eligibility, claimed score/method and host acknowledgment.

Refer to model-spec.md for interval guards, cardinalities, snapshot versus semantic identity, origin requirements, permission precedence and explicit unsupported cases. Schema requiredness alone is not semantic acceptance.
