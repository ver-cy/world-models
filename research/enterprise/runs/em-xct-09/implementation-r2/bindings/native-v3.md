# Native V3 reference binding

Install this exact companion and schema through the separately pinned WM-XCT-040 composer. Predecessor packages are semantic-only references. The composer installs the declared evaluator and closed schema bytes but does not execute them automatically.

After host-authorized review, native_records creates one local ClassificationAssessment object and one restricted classification.assessment.snapshot fact. Its nested value is {packet, assessment}; the supplied canonical subject IDs inside the packet remain external references. The aggregate has local owner, boundary, purpose and deterministic assessment identity. This is not a multi-subject federation Projection or a classification fact on the business subject.

Use the installed validate_native_fact after ordinary V3 validation. It closes the fact envelope, checks the fact's Assessment subject ID, owner, digest and capture time, and replays every nested outcome with the exact installed build. It does not inspect a separate native object record; ordinary V3 validation and the host remain responsible for that record. Replay establishes consistency only and does not re-authorize reads or approve mapping assertions. native_records performs no authorization. Host storage/read permissions and independently retained grant provenance remain mandatory.

review checks both its assessment and the combined packet/assessment value against the closed schema and1MiB canonical ceiling before returning. Large packets can therefore be refused even when the packet alone fits: the complete replayable value must fit. Native capture requires the same limit; no truncation or dropping alternatives is allowed.

An identical assessment has the same object/fact IDs even if captured later; keep the first stored record. The Vercy writer rejects repeated IDs. Changed input/build/approval yields a distinct assessment object; no automatic supersession or existing-Dimension migration is provided. Actual test scope is stated in acceptance-results.json; a descriptor alone is not installation evidence.
