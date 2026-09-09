# WM-DAT-009 bounded provider focus

Research one governed Survey / Questionnaire specification used to ask questions
and capture response structure. Freeze the title ambiguity: a survey can mean a
study, program, campaign, wave or data-collection activity, while a questionnaire
is an instrument. The Vercy root may aggregate an instrument definition and its
survey-use bindings, but must keep the instrument, study, campaign, wave,
administration, interview, respondent, consent, sample, response, observation,
dataset and analysis result as independently identifiable lifecycles.

The root owns instrument identity, versions and lifecycle; purpose and intended
population; modules, sections, question items, statements and instructions;
question wording, concepts and variables; response domains, options, scales,
units, validation, missing and nonresponse codes; ordering, display and routing
logic; calculated or derived fields; language and translation variants; mode,
device and accessibility profiles; randomization and experimental forms; testing,
review and approval evidence; survey, campaign, wave, sample and consent bindings;
response and dataset schemas; publication, access, retention, provenance,
correction and interoperability projections. It does not own individual answers
or execute data collection.

Known registry context:

- registry_id: vr.wm-dat-009
- parent signal: WM-REC-007
- purpose: questions, instrument versions and response structure
- owner archetype: data product owner or data steward
- no frozen relation row exists; any parent or composition signal remains a hold

Target 6 bundles, 12 layers, 24 findings, 72 discriminating questions, at least
24 artifacts and 10 functions. Prefer current primary official sources from DDI
Alliance, UNECE, W3C, IETF, ISO public metadata, HL7 and public statistical
authorities. Pin versions, identify domain-specific profiles and declare all
projection loss.

Agents must not autonomously contact respondents, publish an instrument, approve
ethics or consent, change sampling, collect answers, infer protected traits,
link identities, widen access, create a dataset, certify results or dispose
records without delegated authority.
