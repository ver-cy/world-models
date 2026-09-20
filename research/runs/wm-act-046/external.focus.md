# WM-ACT-046 bounded external review focus

Research one format-neutral meta-model for a clinical assertion that may be an observation result or a diagnosis, with an explicit profile discriminator. Preserve the boundary between the act or record of asserting clinical information and the external patient, practitioner, encounter, specimen, device, procedure, diagnostic report, disease or biological-condition masters.

Stress-test these distinctions:

- observable or test definition versus an observation result;
- measured, coded, ordinal, narrative, multimedia and absent or unknown result values;
- observation result versus interpretation, clinical impression and diagnosis;
- finding or symptom versus persistent condition or disease;
- provisional, differential, confirmed, refuted and entered-in-error verification states;
- observation status versus clinical status versus verification status;
- subject, focus, performer, author, recorder, interpreter and responsible asserter;
- effective or specimen time versus issued, recorded, ingested and known time;
- source record versus normalized terminology mapping and analytic projection;
- correction, amendment, refutation and replacement without deleting clinical history.

Use current primary specifications where possible: HL7 FHIR R5 Observation, Condition, DiagnosticReport and ClinicalImpression; openEHR Reference Model OBSERVATION and EVALUATION; SNOMED CT clinical-finding concept model and context rules; LOINC observation semantics; WHO ICD-11; OMOP CDM 5.4; DICOM Structured Reporting; UCUM; PROV-O; applicable privacy and timestamp standards.

Target 6 bundles, 12 layers, 24 findings, 72 or more discriminating questions, 24 artifacts and 10 governed functions. Treat external terminology and exchange standards as version-pinned projections, not universal semantics. Include an explicit independent-review hold if no valid external result is admitted.
