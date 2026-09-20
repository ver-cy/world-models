# WM-ACT-047 bounded external review focus

Research one format-neutral meta-model for a medical procedure occurrence: an action performed, attempted, stopped or not performed on or for a subject. Treat order, plan, appointment, encounter, consent, observation, report, complication, adverse event, device, specimen and follow-up instruction as external masters linked to the procedure occurrence.

Stress-test these distinctions:

- procedure definition or code versus a particular occurrence;
- ServiceRequest or plan versus performed action;
- scheduling or workflow Task versus clinical procedure event;
- preparation, in-progress, on-hold, stopped, completed, not-done and entered-in-error;
- intended procedure versus procedure actually performed, including deviations;
- method, technique, approach, access, body site, morphology, focus and intent;
- performer, assistant, device and organization roles versus recorder or reporter;
- used device or substance versus implanted, removed or manipulated focal device;
- immediate outcome versus observation, diagnostic report, complication, adverse event and long-term condition;
- routine component procedure versus separately identified procedure occurrence;
- consent or authorization reference versus proof that the procedure was clinically or legally appropriate;
- occurrence time versus recorded, reported, ingested and knowledge time.

Use current primary specifications where possible: HL7 FHIR R5 Procedure, ServiceRequest, CarePlan, Observation and AdverseEvent; openEHR RM INSTRUCTION and ACTION; SNOMED CT procedure concept model; WHO ICHI and Surgical Safety Checklist; OMOP CDM 5.4; FDA UDI; PROV-O; privacy and timestamp standards.

Target 6 bundles, 12 layers, 24 findings, 72 or more discriminating questions, 24 artifacts and 10 governed functions. Treat code systems and exchange standards as version-pinned projections, not universal clinical semantics. Include an explicit independent-review hold if no valid external result is admitted.
