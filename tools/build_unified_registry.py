#!/usr/bin/env python3
"""Build and audit the unified Vercy world-model + interoperability registry."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

REPO = Path(__file__).resolve().parents[1]
PROJECT_CURRENT = Path(__file__).resolve().parents[3]
PLANNING = REPO / "planning"
DESIRED = PLANNING / "VERCY-DESIRED-MODELS-MEGA-REGISTRY.csv"
LEGACY = REPO / "world-models.csv"
EXTERNAL = PROJECT_CURRENT / "ver.cy" / "spec" / "docs" / "06-ecosystem" / "external-models.csv"
OUTPUT = PLANNING / "VERCY-UNIFIED-MEGA-REGISTRY.csv"
AUDIT_JSON = PLANNING / "VERCY-UNIFIED-MEGA-REGISTRY-AUDIT.json"
SIMILAR = PLANNING / "VERCY-WORLD-MODEL-SIMILARITY-REVIEW.csv"
RELATIONS = PLANNING / "VERCY-MODEL-RELATIONS.csv"

# id | English canonical name | kind | navigation path | wave | parent | rationale
ADDITIONS_TSV = r"""
WM-LIV-011	Genome / Genomic Assembly	standalone-mm	NAV.PHY.LIV.MOL	2	WM-LIV-002	Versioned genome-level biological reference
WM-LIV-012	Genomic Sequence / Variant	standalone-mm	NAV.PHY.LIV.MOL	1	WM-LIV-011	Independent identity, provenance and clinical/research lifecycle
WM-LIV-013	Gene / Genomic Feature	standalone-mm	NAV.PHY.LIV.MOL	2	WM-LIV-011	Reusable feature reference across organisms and sequences
WM-LIV-014	Protein / Biomolecule	standalone-mm	NAV.PHY.LIV.MOL	2	WM-LIV-002	Independent scientific identifiers and master repositories
WM-LIV-015	Phenotype / Trait	standalone-mm	NAV.PHY.LIV.PHN	2	WM-LIV-002	Observed trait links organisms, health and breeding
WM-LIV-016	Biological Pathway / Process	standalone-mm	NAV.PHY.LIV.MOL	3	WM-LIV-002	Reusable molecular and cellular process context
WM-LIV-017	Pedigree / Biological Lineage	pattern	NAV.PHY.LIV.LIN	2	WM-LIV-002	Cross-species lineage and inheritance pattern
WM-LIV-018	Crop Variety / Cultivar	standalone-mm	NAV.PHY.LIV.CUL	2	WM-LIV-009	Governed variety identity and agricultural lifecycle
WM-LIV-019	Livestock Breed	standalone-mm	NAV.PHY.LIV.CUL	2	WM-LIV-009	Governed breed identity and pedigree conventions
WM-LIV-020	Microbiome / Biological Community	standalone-mm	NAV.PHY.LIV.MIC	3	WM-LIV-003	Community composition has its own sampling lifecycle
WM-LIV-021	Disease / Biological Condition	standalone-mm	NAV.PHY.LIV.HLT	1	WM-LIV-002	Condition is not the same object as a care encounter
WM-LIV-022	Conservation Status Assessment	standalone-mm	NAV.PHY.LIV.CNS	3	WM-LIV-001	Versioned assessment with authority and evidence
WM-LIV-023	Clinical / Biological Specimen	standalone-mm	NAV.PHY.LIV.SPM	1	WM-LIV-002	Patient/subject-linked custody and diagnostic lifecycle distinct from generic lab sample
WM-LIV-024	Biobank / Sample Repository	standalone-mm	NAV.PHY.LIV.REP	2	WM-LIV-023	Institutional collection with consent, access and retention governance
WM-MAT-007	Laboratory Test / Analysis	standalone-mm	NAV.PHY.MAT.LAB	2	WM-MAT-005	Method, specimen, run and result lifecycle
WM-MAT-008	Observation / Measurement Record	standalone-mm	NAV.PHY.MAT.OBS	0		Generic observation linking feature, procedure, value and unit
WM-OBJ-017	Product Configuration / Variant	standalone-mm	NAV.PHY.OBJ.TYPE	1	WM-OBJ-002	Sellable/configurable variant between type and instance
WM-OBJ-018	Engineering Design / Product Definition	standalone-mm	NAV.PHY.OBJ.DES	1	WM-OBJ-002	Versioned design, requirements and approvals
WM-OBJ-019	Component Type / Engineering BOM	standalone-mm	NAV.PHY.OBJ.ASM	1	WM-OBJ-002	Reusable type-level composition distinct from as-built assembly
WM-OBJ-020	Inventory Stock Position	standalone-mm	NAV.PHY.OBJ.INV	1	WM-OBJ-001	Quantity by owner, location, status and time
WM-OBJ-021	Handling Unit / Logistics Container	standalone-mm	NAV.PHY.OBJ.PKG	2	WM-OBJ-009	Nested logistics identity and custody lifecycle
WM-OBJ-022	Asset Lifecycle Record	view-candidate	NAV.PHY.OBJ.AST	2	WM-OBJ-001	Lifecycle projection over item, events, work and ownership
WM-OBJ-023	Meter / Measuring Instrument	standalone-mm	NAV.PHY.OBJ.DEV	2	WM-OBJ-008	Calibration, channel and reading semantics
WM-OBJ-024	Robot / Autonomous Machine	standalone-mm	NAV.PHY.OBJ.ROB	3	WM-OBJ-006	Physical autonomous equipment; robotics penalty applies
WM-BLT-008	Site / Campus	standalone-mm	NAV.PHY.BLT.SITE	1	WM-PLC-002	Managed physical container for facilities and infrastructure
WM-BLT-009	Linear Infrastructure Asset	standalone-mm	NAV.PHY.BLT.NET	2	WM-BLT-003	Segmented roads, rails, pipelines and cables
WM-BLT-010	Utility Network Topology	standalone-mm	NAV.PHY.BLT.NET	2	WM-BLT-003	Nodes, edges, connectivity and operational state
WM-EAR-010	Ocean / Marine State	standalone-mm	NAV.PHY.EAR.OCN	3	WM-PLC-003	Oceanographic state and observation lifecycle
WM-EAR-011	Land Cover / Land Use	standalone-mm	NAV.PHY.EAR.LND	2	WM-PLC-002	Observed cover versus governed use classification
WM-EAR-012	Environmental Monitoring Station	standalone-mm	NAV.PHY.EAR.MON	2	WM-OBJ-023	Stable observing facility, instruments and programs
WM-SPC-003	Astronomical Observation	standalone-mm	NAV.PHY.SPC.OBS	3	WM-SPC-002	Observation products and provenance distinct from bodies
WM-SPC-004	Satellite Mission / Programme	standalone-mm	NAV.PHY.SPC.MSN	3	WM-SPC-001	Programme container for spacecraft, payloads, observations and operations
WM-FLW-009	Journey / Trip	standalone-mm	NAV.PHY.FLW.MOB	1	WM-FLW-007	Planned and actual movement of a person or vehicle
WM-FLW-010	Route / Itinerary	standalone-mm	NAV.PHY.FLW.MOB	1	WM-FLW-009	Ordered path, stops and constraints
WM-FLW-011	Shipment / Consignment	standalone-mm	NAV.PHY.FLW.LOG	1	WM-FLW-004	Commercial/logistics object with custody and delivery lifecycle
WM-FLW-012	Inventory Movement	standalone-mm	NAV.PHY.FLW.LOG	1	WM-OBJ-020	Transfer changes stock position and custody
WM-FLW-013	Supply-chain Trace / Chain of Custody	pattern	NAV.PHY.FLW.LOG	1	WM-FLW-004	Cross-organizational event/provenance pattern
WM-FLW-014	Network Flow / Telemetry Stream	standalone-mm	NAV.PHY.FLW.NET	2	WM-BLT-003	Time-varying flow through logical or physical network
WM-FLW-015	Resource Consumption	standalone-mm	NAV.PHY.FLW.RES	1	WM-FLW-008	Consumption by actor, asset, activity and interval
WM-PER-010	Contact Point / Party Profile	mixin	NAV.SOC.PER.CON	0	WM-PER-001	Reusable contact and communication preferences
WM-PER-011	Interpersonal Relationship	standalone-mm	NAV.SOC.PER.REL	1	WM-PER-001	Independent relationship roles, validity and privacy
WM-PER-013	Professional License / Credential	standalone-mm	NAV.SOC.PER.CRD	1	WM-XCT-017	Governed grant, scope, issuer and validity
WM-PER-014	Preference / Personal Profile	mixin	NAV.SOC.PER.PRF	2	WM-PER-001	User-controlled preference context
WM-PER-015	Reputation / Trust Assessment	standalone-mm	NAV.SOC.PER.TRU	2	WM-PER-001	Evidence-based assessment with issuer and appeal lifecycle
WM-ORG-010	Legal Entity Registration	standalone-mm	NAV.SOC.ORG.REG	0	WM-ORG-001	Legal identity, jurisdiction, registers and lifecycle
WM-ORG-011	Business Establishment / Branch	standalone-mm	NAV.SOC.ORG.EST	1	WM-ORG-001	Operational location distinct from legal entity and unit
WM-ORG-012	Inter-organizational Relationship	standalone-mm	NAV.SOC.ORG.REL	1	WM-ORG-001	Partnership, control, affiliation and supply relationships
WM-ORG-013	Stakeholder / Interest	standalone-mm	NAV.SOC.ORG.STK	1	WM-ORG-001	Interest, influence and impact relationship
WM-ORG-014	Customer / Account Relationship	standalone-mm	NAV.SOC.ORG.CRM	1	WM-ORG-012	Lifecycle mastered by CRM, not party identity
WM-ORG-015	Supplier / Partner Relationship	standalone-mm	NAV.SOC.ORG.SUP	1	WM-ORG-012	Qualification, risk and commercial status
WM-ORG-016	Work Assignment	standalone-mm	NAV.SOC.ORG.ASN	1	WM-ORG-005	Person/agent assigned to role, scope and time
WM-ORG-017	Performance Objective / Review	standalone-mm	NAV.SOC.ORG.PERF	2	WM-ORG-016	Objective, evidence, assessment and outcome lifecycle
WM-ORG-018	Governance Body / Committee	standalone-mm	NAV.SOC.ORG.GOV	1	WM-ORG-003	Mandate, membership and decision authority
WM-ORG-019	Organization Policy	standalone-mm	NAV.SOC.ORG.POL	1	WM-ORG-007	Approved normative rule with scope and lifecycle
WM-POL-015	Jurisdiction	standalone-mm	NAV.SOC.POL.JUR	0	WM-PLC-004	Authority scope over territory, persons or subject matter
WM-POL-016	Public Authority / Institution	standalone-mm	NAV.SOC.POL.AUT	1	WM-ORG-001	Government institution and legal competence
WM-POL-017	Administrative Procedure / Case	standalone-mm	NAV.SOC.POL.ADM	1	WM-ACT-021	Public-law case distinct from court litigation
WM-POL-018	Public Service / Government Service	standalone-mm	NAV.SOC.POL.SRV	1	WM-ACT-004	Entitlement, application and delivery lifecycle
WM-POL-019	Legal Filing / Pleading	standalone-mm	NAV.SOC.POL.FIL	1	WM-POL-009	Procedural record with party, deadline and service
WM-POL-020	Evidence Item / Exhibit	standalone-mm	NAV.SOC.POL.EVD	1	WM-POL-009	Chain of custody, admissibility and provenance
WM-POL-021	Judgment / Legal Decision	standalone-mm	NAV.SOC.POL.JDG	1	WM-POL-009	Authoritative outcome, reasoning and remedies
WM-POL-022	Sanction / Sentence	standalone-mm	NAV.SOC.POL.SAN	2	WM-POL-021	Imposed consequence with execution lifecycle
WM-POL-023	Enforcement Action	standalone-mm	NAV.SOC.POL.ENF	2	WM-POL-021	Execution by competent authority
WM-POL-024	Detention / Custody	standalone-mm	NAV.SOC.POL.CUS	2	WM-POL-023	High-sensitivity custody lifecycle and safeguards
WM-POL-025	Immigration / Visa Case	standalone-mm	NAV.SOC.POL.MIG	2	WM-POL-017	Specialized cross-border administrative lifecycle
WM-POL-026	Customs Declaration / Clearance	standalone-mm	NAV.SOC.POL.CUS2	1	WM-POL-006	Goods declaration, assessment and release lifecycle
WM-POL-027	Property Right / Tenure	standalone-mm	NAV.SOC.POL.PRP	1	WM-PLC-002	Legal interest distinct from physical asset
WM-POL-028	Border Crossing Event	standalone-mm	NAV.SOC.POL.BRD	2	WM-POL-006	Observed crossing with persons, goods, vehicle, checks and outcome
WM-POL-029	Migration / Residency Status	standalone-mm	NAV.SOC.POL.MIG	1	WM-POL-015	Governed legal status distinct from an immigration case
WM-ECO-015	Financial Account	standalone-mm	NAV.SOC.ECO.ACC	0	WM-XCT-014	Account identity, parties, currency, state and rules
WM-ECO-016	Financial Transaction / Journal Entry	standalone-mm	NAV.SOC.ECO.TXN	0	WM-ECO-015	Atomic posting/transfer with audit and balancing
WM-ECO-017	Financial Position / Balance	standalone-mm	NAV.SOC.ECO.POS	1	WM-ECO-015	Time-bound asset, liability, equity or exposure position
WM-ECO-018	Financial Statement	standalone-mm	NAV.SOC.ECO.STA	1	WM-REC-002	Governed report over accounts and reporting period
WM-ECO-019	Purchase Order	standalone-mm	NAV.SOC.ECO.ORD	0	WM-ECO-006	Buyer commitment and fulfilment lifecycle
WM-ECO-020	Sales Order	standalone-mm	NAV.SOC.ECO.ORD	0	WM-ECO-006	Seller-side order and fulfilment lifecycle
WM-ECO-021	Offer / Quote	standalone-mm	NAV.SOC.ECO.OFR	1	WM-OBJ-003	Commercial terms before order/contract
WM-ECO-022	Subscription	standalone-mm	NAV.SOC.ECO.SUB	1	WM-ECO-006	Recurring entitlement, billing and renewal lifecycle
WM-ECO-023	Reservation / Booking	standalone-mm	NAV.SOC.ECO.RSV	1	WM-ECO-006	Capacity hold and confirmation lifecycle
WM-ECO-024	Fulfilment / Delivery	standalone-mm	NAV.SOC.ECO.FUL	1	WM-ECO-019	Obligation fulfilment linked to goods/services
WM-ECO-025	Return / Refund	standalone-mm	NAV.SOC.ECO.RET	1	WM-ECO-024	Reverse fulfilment and financial adjustment
WM-ECO-026	Sales Lead / Opportunity	standalone-mm	NAV.SOC.ECO.CRM	1	WM-ORG-014	Prospect, stage, probability and outcome lifecycle
WM-ECO-027	Marketing Campaign	standalone-mm	NAV.SOC.ECO.MKTG	1	WM-ACT-028	Audience, objective, channel, content and measurement
WM-ECO-028	Advertisement / Promotion	standalone-mm	NAV.SOC.ECO.ADS	1	WM-MED-001	Paid/promotional content, placement and disclosure
WM-ECO-029	Loyalty / Reward	standalone-mm	NAV.SOC.ECO.LOY	2	WM-ORG-014	Program membership, points and benefit lifecycle
WM-ECO-030	Grant / Donation	standalone-mm	NAV.SOC.ECO.GNT	1	WM-POL-012	Award, restrictions, disbursement and reporting
WM-ECO-031	Payroll / Compensation	standalone-mm	NAV.SOC.ECO.PAYR	1	WM-ORG-005	Earnings, deductions and pay-period lifecycle
WM-ECO-032	Tax Return / Filing	standalone-mm	NAV.SOC.ECO.TAX	1	WM-POL-011	Taxpayer declaration distinct from authority assessment
WM-ECO-033	Regulatory Filing / Disclosure	standalone-mm	NAV.SOC.ECO.REG	1	WM-REC-002	Submission to authority with validation and amendment
WM-ECO-034	ESG / Sustainability Disclosure	standalone-mm	NAV.SOC.ECO.ESG	1	WM-ECO-033	Organization-level disclosure distinct from product claim
WM-ECO-035	Audit / Assurance Engagement	standalone-mm	NAV.SOC.ECO.AUD	1	WM-ACT-036	Independent scope, evidence, opinion and remediation
WM-ECO-036	Insurance Claim	standalone-mm	NAV.SOC.ECO.INS	1	WM-ECO-003	Loss notification, assessment, coverage and settlement
WM-ECO-037	Debt Instrument	standalone-mm	NAV.SOC.ECO.DEBT	1	WM-ECO-005	Debt identity, issuer, terms, cashflows, rating and lifecycle
WM-ECO-038	Equity / Security Holding	standalone-mm	NAV.SOC.ECO.SEC	1	WM-ECO-005	Ownership position and corporate-action lifecycle distinct from debt
WM-REC-007	Form / Submission	standalone-mm	NAV.INF.REC.FRM	0	WM-REC-001	Structured response package with validation lifecycle
WM-REC-008	Certificate / Credential Record	standalone-mm	NAV.INF.REC.CRT	1	WM-XCT-017	Issued documentary representation of an attestation
WM-REC-009	Application / Request Record	standalone-mm	NAV.INF.REC.APP	0	WM-REC-007	Request entering a case or service lifecycle
WM-REC-010	Decision / Approval Record	standalone-mm	NAV.INF.REC.DEC	0	WM-REC-001	Authoritative decision, rationale, approver and validity
WM-REC-011	Evidence / Supporting Record	standalone-mm	NAV.INF.REC.EVD	1	WM-REC-001	Evidence role, provenance and admissibility context
WM-REC-012	Minutes / Transcript	standalone-mm	NAV.INF.REC.MIN	1	WM-ACT-025	Durable record of a meeting or interaction
WM-REC-013	Operational Log / Trace	standalone-mm	NAV.INF.REC.LOG	1	WM-REC-001	Append-oriented technical or business event evidence
WM-REC-014	Configuration Record	standalone-mm	NAV.INF.REC.CFG	1	WM-REC-001	Versioned declared configuration distinct from runtime state
WM-REC-015	Archival Fonds / Collection	standalone-mm	NAV.INF.REC.FND	2	WM-REC-001	Archival aggregation with accession, arrangement, description and access lifecycle
WM-DAT-004	Data Schema / Data Contract	standalone-mm	NAV.INF.DAT.SCH	0	WM-DAT-001	Semantics, constraints and producer-consumer agreement
WM-DAT-005	Data Pipeline	standalone-mm	NAV.INF.DAT.PIP	1	WM-ACT-003	Executable transformation graph and operations lifecycle
WM-DAT-006	Data Lineage	pattern	NAV.INF.DAT.LIN	0	WM-XCT-012	Dataset/field derivation and processing provenance
WM-DAT-007	Data Quality Assessment	standalone-mm	NAV.INF.DAT.QLT	1	WM-DAT-001	Metrics, rules, observations and remediation lifecycle
WM-DAT-008	Data Catalog Entry / Data Product	standalone-mm	NAV.INF.DAT.CAT	1	WM-DAT-001	Discoverable governed offering distinct from dataset bytes
WM-DAT-009	Survey / Questionnaire	standalone-mm	NAV.INF.DAT.SRV	1	WM-REC-007	Questions, instrument versions and response structure
WM-DAT-010	Time Series / Observation Collection	standalone-mm	NAV.INF.DAT.TS	1	WM-MAT-008	Ordered observations with sampling semantics
WM-DAT-011	Knowledge Graph	standalone-mm	NAV.INF.DAT.KG	2	WM-KNW-001	Graph dataset with ontology, assertions and provenance
WM-DAT-012	Synthetic Data Product	standalone-mm	NAV.INF.DAT.SYN	2	WM-DAT-008	Generated dataset with privacy and fidelity evidence
WM-KNW-006	Concept / Term	standalone-mm	NAV.INF.KNW.CON	0	WM-KNW-002	Stable semantic concept independent of a label
WM-KNW-007	Claim / Proposition	standalone-mm	NAV.INF.KNW.CLM	0	WM-KNW-001	Truth-apt assertion with scope, evidence and provenance
WM-KNW-008	Evidence / Citation	standalone-mm	NAV.INF.KNW.EVD	0	WM-KNW-007	Support/challenge relation and source locator
WM-KNW-009	Hypothesis	standalone-mm	NAV.INF.KNW.HYP	1	WM-KNW-007	Testable provisional claim and evaluation lifecycle
WM-KNW-010	Decision / Rationale	standalone-mm	NAV.INF.KNW.DEC	0	WM-KNW-007	Choice, alternatives, criteria and reasoning
WM-KNW-011	Goal / Objective	standalone-mm	NAV.INF.KNW.GOL	0	WM-ACT-008	Desired outcome with measure and horizon
WM-KNW-012	Policy / Rule	standalone-mm	NAV.INF.KNW.POL	0	WM-POL-001	Executable or interpretable normative statement
WM-KNW-013	Constraint / Requirement Rule	standalone-mm	NAV.INF.KNW.CNS	1	WM-REC-006	Formal constraint independent of prose artifact
WM-KNW-014	Issue / Problem	standalone-mm	NAV.INF.KNW.ISS	0	WM-ACT-021	Recognized discrepancy requiring resolution
WM-KNW-015	Risk / Opportunity	standalone-mm	NAV.INF.KNW.RSK	0	WM-ACT-017	Uncertain event/effect with likelihood and impact
WM-KNW-016	Assumption	standalone-mm	NAV.INF.KNW.ASM	1	WM-KNW-007	Accepted premise with owner and validation state
WM-KNW-018	Taxonomy / Classification Scheme	standalone-mm	NAV.INF.KNW.TAX	1	WM-XCT-020	Governed concepts, hierarchy and mappings
WM-KNW-019	Mathematical / Computational Model	standalone-mm	NAV.INF.KNW.MATH	2	WM-KNW-001	Equations, parameters, assumptions and validation
WM-MED-002	Media Asset / Rendition	standalone-mm	NAV.INF.MED.AST	1	WM-MED-001	Technical asset and renditions distinct from creative work
WM-MED-003	Publication / Edition	standalone-mm	NAV.INF.MED.PUB	1	WM-MED-001	Publication lifecycle and edition identity
WM-MED-004	Audio / Video Recording	standalone-mm	NAV.INF.MED.AV	2	WM-MED-002	Time-based media identity and tracks
WM-MED-005	Image / Graphic	standalone-mm	NAV.INF.MED.IMG	2	WM-MED-002	Still visual asset and technical/provenance metadata
WM-MED-006	3D Asset / Scene	standalone-mm	NAV.INF.MED.3D	2	WM-MED-002	Geometry, materials, scene graph and rights
WM-MED-007	Broadcast / Stream	standalone-mm	NAV.INF.MED.STR	2	WM-MED-002	Scheduled/live distribution and measurement lifecycle
WM-MED-008	Content Provenance Credential	standalone-mm	NAV.INF.MED.PRV	1	WM-XCT-012	Signed media edit/origin chain with issuer and verification lifecycle
WM-SFT-007	Software Component / Package	standalone-mm	NAV.INF.SFT.PKG	0	WM-SFT-001	Versioned distributable dependency identity
WM-SFT-008	Build / Release	standalone-mm	NAV.INF.SFT.REL	0	WM-SFT-007	Reproducible build provenance and release lifecycle
WM-SFT-009	Deployment	standalone-mm	NAV.INF.SFT.DEP	0	WM-SFT-002	Release installed to environment with state/history
WM-SFT-010	Runtime / Compute Environment	standalone-mm	NAV.INF.SFT.RUN	1	WM-SFT-002	Execution context, resources and configuration
WM-SFT-011	Software Configuration	standalone-mm	NAV.INF.SFT.CFG	1	WM-SFT-002	Desired settings, references and version scope
WM-SFT-012	SBOM / Supply-chain Manifest	standalone-mm	NAV.INF.SFT.SBOM	0	WM-SFT-007	Signed/versioned component inventory and relationships
WM-SFT-013	Software Change / Pull Request	standalone-mm	NAV.INF.SFT.CHG	1	WM-SFT-005	Proposed diff, review and merge lifecycle
WM-SFT-014	Defect / Bug	standalone-mm	NAV.INF.SFT.BUG	0	WM-ACT-021	Software problem and resolution lifecycle
WM-SFT-015	Test Case / Test Result	standalone-mm	NAV.INF.SFT.TST	0	WM-ACT-038	Repeatable test definition, execution and evidence
WM-SFT-016	Service Level / SLO	standalone-mm	NAV.INF.SFT.SLO	1	WM-ECO-006	Measurable service commitment and compliance
WM-SFT-017	Telemetry / Operational Signal	standalone-mm	NAV.INF.SFT.TEL	1	WM-MAT-008	Metrics, logs and traces tied to runtime
WM-SFT-018	Network / Endpoint	standalone-mm	NAV.INF.SFT.NET	1	WM-SFT-002	Logical connectivity, address and exposure
WM-AI-001	AI System	standalone-mm	NAV.INF.AI.SYS	0	WM-SFT-002	Governed AI-enabled system beyond a model artifact
WM-AI-002	AI Agent	standalone-mm	NAV.INF.AI.AGT	0	WM-PER-003	Autonomous actor with tools, memory, policy and authority
WM-AI-003	AI Model Evaluation	standalone-mm	NAV.INF.AI.EVL	0	WM-SFT-004	Dataset, metric, run, finding and approval lifecycle
WM-AI-004	AI Inference / Agent Run	standalone-mm	NAV.INF.AI.RUN	0	WM-AI-001	Auditable execution with inputs, outputs, tools and cost
WM-AI-005	Prompt / Agent Configuration	standalone-mm	NAV.INF.AI.PRM	0	WM-KNW-005	Versioned operational instruction and tool configuration
WM-AI-006	Model Training / Fine-tuning Run	standalone-mm	NAV.INF.AI.TRN	1	WM-SFT-004	Data, code, parameters, compute and resulting artifact
WM-AI-007	AI Model Registry Entry	standalone-mm	NAV.INF.AI.REG	1	WM-SFT-004	Deployment status, approvals, lineage and discoverability
WM-AI-008	AI Safety / Governance Assessment	standalone-mm	NAV.INF.AI.GOV	0	WM-ACT-037	Risk, control, evidence and decision for an AI system
WM-AI-009	Evaluation Dataset / Benchmark	extension	NAV.INF.AI.DAT	1	WM-DAT-001	AI-specific governed extension of Dataset
WM-AI-010	AI Incident Report	standalone-mm	NAV.INF.AI.INC	1	WM-AI-001	Regulatory AI incident classification, reporting deadline and remediation lifecycle
WM-VRT-007	3D Scene / Environment	standalone-mm	NAV.INF.VRT.3D	2	WM-VRT-002	Spatial scene and interactive object graph
WM-VRT-008	Virtual Persona / Avatar	standalone-mm	NAV.INF.VRT.AVT	2	WM-PER-003	Representation and control distinct from natural person
WM-VRT-009	Virtual Economy	standalone-mm	NAV.INF.VRT.ECO	2	WM-VRT-002	Rules, assets and transactions inside a virtual world
WM-VRT-010	Distributed Ledger Network	standalone-mm	NAV.INF.VRT.DLT	2	WM-SFT-002	Network/governance context for tokens and smart contracts
WM-VRT-011	Smart Contract	standalone-mm	NAV.INF.VRT.SC	2	WM-SFT-007	Executable agreement deployed on a ledger
WM-VRT-012	Simulation Scenario	standalone-mm	NAV.INF.VRT.SCN	3	WM-VRT-003	Inputs, actors, environment, objectives and expected outcomes
WM-VRT-013	Digital Thread	pattern	NAV.INF.VRT.THR	2	WM-VRT-001	Lifecycle federation across design, item, operations and twin
WM-ACT-024	Decision / Approval Activity	standalone-mm	NAV.ACT.DEC	0	WM-ACT-002	Authority, inputs, choice and outcome
WM-ACT-025	Meeting / Session	standalone-mm	NAV.ACT.MTG	0	WM-ACT-018	Participants, agenda, decisions and record
WM-ACT-026	Appointment / Reservation Event	standalone-mm	NAV.ACT.APT	1	WM-ACT-018	Scheduled allocation between parties/resources
WM-ACT-027	Communication Interaction	standalone-mm	NAV.ACT.COM	0	WM-ACT-018	Conversation/contact lifecycle across channels
WM-ACT-028	Campaign	standalone-mm	NAV.ACT.CAM	1	WM-ACT-005	Coordinated activities toward audience/outcome
WM-ACT-029	Program / Portfolio	standalone-mm	NAV.ACT.PGM	1	WM-ACT-005	Governed collection of projects and benefits
WM-ACT-030	Initiative	standalone-mm	NAV.ACT.INI	1	WM-ACT-005	Change intent before or across formal projects
WM-ACT-031	Milestone / Deliverable	standalone-mm	NAV.ACT.MIL	0	WM-ACT-005	Planned achievement and accepted output
WM-ACT-032	Change Request	standalone-mm	NAV.ACT.CHG	0	WM-ACT-021	Proposed controlled change and disposition
WM-ACT-033	Review / Inspection / Audit	standalone-mm	NAV.ACT.REV	0	WM-ACT-009	Evidence gathering, criteria, findings and decision
WM-ACT-034	Assessment / Evaluation	standalone-mm	NAV.ACT.ASM	0	WM-ACT-009	Subject, criteria, evidence, score and conclusion
WM-ACT-035	Test Execution	standalone-mm	NAV.ACT.TST	1	WM-ACT-034	Repeatable procedure run producing evidence
WM-ACT-036	Research Study	standalone-mm	NAV.ACT.RES	1	WM-ACT-022	Protocol, cohort/material, observations and findings
WM-ACT-037	Survey Administration	standalone-mm	NAV.ACT.SRVY	2	WM-DAT-009	Sample, collection wave, responses and quality
WM-ACT-038	Learning Activity / Course Delivery	standalone-mm	NAV.ACT.EDU	1	WM-PER-008	Instruction, participation and assessment lifecycle
WM-ACT-039	Recruitment / Hiring Process	standalone-mm	NAV.ACT.HR	1	WM-ORG-008	Candidate, stages, decisions and employment outcome
WM-ACT-040	Onboarding / Offboarding	standalone-mm	NAV.ACT.HR	1	WM-ORG-005	Access, assets, training and obligations lifecycle
WM-ACT-041	Public Consultation	standalone-mm	NAV.ACT.CIV	2	WM-ACT-028	Proposal, participants, submissions and response
WM-ACT-042	Incident Response	standalone-mm	NAV.ACT.INC	0	WM-ACT-019	Detection through containment, recovery and lessons
WM-ACT-043	Business Continuity / Recovery	standalone-mm	NAV.ACT.RESIL	1	WM-ACT-008	Critical service, scenario, plan, exercise and recovery
WM-ACT-044	Content Publication	standalone-mm	NAV.ACT.PUB	1	WM-MED-003	Editorial approval, release, distribution and correction
WM-ACT-045	Insurance Claim Handling	standalone-mm	NAV.ACT.INS	1	WM-ECO-036	Investigation, coverage decision and settlement process
WM-ACT-046	Clinical Observation / Diagnosis	standalone-mm	NAV.ACT.HCR	1	WM-LIV-021	Clinical assertion backed by observations and practitioner
WM-ACT-047	Medical Procedure	standalone-mm	NAV.ACT.HCR	1	WM-ACT-014	Procedure order, performance, outcome and complications
WM-ACT-048	Medication Order / Administration	standalone-mm	NAV.ACT.HCR	1	WM-OBJ-005	Prescription, dispense and administration lifecycle
WM-ACT-049	Care Plan / Episode	standalone-mm	NAV.ACT.HCR	1	WM-ACT-014	Goals, problems, interventions and responsible team
WM-ACT-050	Environmental Impact Assessment	standalone-mm	NAV.ACT.ENV	2	WM-ACT-034	Project impacts, alternatives, mitigation and decision
WM-ACT-051	Regulatory Compliance Process	standalone-mm	NAV.ACT.REG	1	WM-ACT-003	Obligations, controls, evidence, findings and remediation
WM-ACT-052	Tax Filing / Assessment Process	standalone-mm	NAV.ACT.TAX	1	WM-POL-011	Return, validation, assessment, payment and dispute
WM-ACT-053	Data Processing Job / Pipeline Run	standalone-mm	NAV.ACT.DATA	1	WM-DAT-005	Auditable execution of a data pipeline or transformation
WM-ACT-054	Research Subject / Participant	standalone-mm	NAV.ACT.RES	1	WM-ACT-036	Consent, enrolment, assignment, participation and de-identification lifecycle
WM-XCT-021	Lifecycle / Status	mixin	NAV.XCT	0		Common state machine and effective validity
WM-XCT-022	Version / Change History	mixin	NAV.XCT	0		Revision identity, predecessor and migration
WM-XCT-023	Party Role	mixin	NAV.XCT	0		Actor role scoped to an object or activity
WM-XCT-024	Contact Point	mixin	NAV.XCT	0	WM-PER-010	Addressable channel with purpose and preference
WM-XCT-025	Observable Result Fields	mixin	NAV.XCT	0	WM-MAT-008	Reusable observation value, unit, method and uncertainty
WM-XCT-026	Quality / Confidence	mixin	NAV.XCT	0		Quality dimensions, score, method and confidence
WM-XCT-027	Risk / Control	mixin	NAV.XCT	0	WM-KNW-015	Risk-control linkage and residual assessment
WM-XCT-028	Evidence / Rationale	mixin	NAV.XCT	0	WM-KNW-008	Traceable support for a claim or decision
WM-XCT-029	Obligation / Commitment	mixin	NAV.XCT	0		Party, action, due date, condition and fulfilment
WM-XCT-030	Notification / Subscription	mixin	NAV.XCT	1		Event-interest and delivery preference
WM-XCT-031	Localization / Language	mixin	NAV.XCT	0		Locale, translation and terminology binding
WM-XCT-032	Currency / Monetary Value	mixin	NAV.XCT	0	WM-ECO-004	Amount, currency, valuation date and precision
WM-XCT-033	Geometry / Coordinate Reference	mixin	NAV.XCT	0	WM-XCT-010	Geometry and coordinate reference system
WM-XCT-034	Digital Signature / Proof	mixin	NAV.XCT	0	WM-XCT-006	Signature, signer, method and verification evidence
WM-XCT-035	Retention / Disposition	mixin	NAV.XCT	1		Retention trigger, hold, disposition and evidence
WM-XCT-036	Alias / Same-as Mapping	mixin	NAV.XCT	0	WM-XCT-011	Federated identity equivalence with authority/confidence
WM-XCT-037	Dependency / Impact	mixin	NAV.XCT	0		Typed dependency and downstream impact
WM-XCT-038	Policy Evaluation	pattern	NAV.XCT	1	WM-KNW-012	Policy input, decision, obligations and explanation
"""

GROUP_DOMAINS = {
    "Healthcare & Life Sciences": "PHY.LIV;SOC.PER;ACT.HCR",
    "Data, API & Serialization": "INF.DAT;INF.SFT",
    "Semantic Web & Linked Data": "INF.KNW;INF.DAT",
    "Library, Metadata & Cultural Heritage": "INF.REC;INF.MED;SOC.CIV",
    "Geospatial & Temporal": "PHY.PLC;XCT.TIME;XCT.LOC",
    "Identity, Security, Privacy & Governance": "XCT;SOC.PER;ACT.CYB",
    "Enterprise Architecture & Modeling": "SOC.ORG;ACT.CAP;INF.KNW",
    "Media, Broadcast & Content Provenance": "INF.MED;INF.REC",
    "Software, DevOps & Security Artifacts": "INF.SFT;INF.AI;ACT.CYB",
    "Commerce, Product & Supply Chain": "PHY.OBJ;SOC.ECO;PHY.FLW",
    "Manufacturing, Engineering & BIM": "PHY.OBJ;PHY.BLT;ACT.PRD",
    "3D, Gaming, XR & Robotics": "INF.VRT;INF.MED;PHY.OBJ",
    "AI, ML & Data Governance": "INF.AI;INF.DAT;XCT",
    "Research Data, Scholarly & Identifiers": "ACT.RES;INF.REC;INF.DAT",
    "IoT, Devices & Digital Twins": "PHY.OBJ;INF.VRT;INF.DAT",
    "Weather & Earth Observation": "PHY.EAR;INF.DAT",
    "Blockchain, Web3 & Tokens": "INF.VRT;SOC.ECO",
    "Finance & Insurance": "SOC.ECO",
    "Bioinformatics & Genomics Formats": "PHY.LIV;INF.DAT",
    "Calendaring, Contacts & Social": "SOC.PER;ACT.EVT;XCT.TIME",
    "Energy & Utilities": "PHY.FLW;PHY.BLT;SOC.ECO",
    "Agriculture, Food & Environment": "PHY.LIV;PHY.EAR;ACT.AGR",
    "Music, Audio & Timeline Media": "INF.MED",
    "HR, Skills & Education": "SOC.ORG;SOC.PER;ACT.EDU",
    "Aviation & Air Traffic": "PHY.OBJ;PHY.PLC;PHY.FLW",
    "Telecom & Networking": "INF.SFT;PHY.BLT;ACT.SRV",
    "Mobility & Transportation": "PHY.OBJ;PHY.FLW;ACT.SRV",
    "ESG, Sustainability & Climate Reporting": "SOC.ECO;PHY.EAR;PHY.FLW",
    "Government, Legal & Civic": "SOC.POL;ACT.CSE;INF.REC",
    "Chemistry, Materials & Laboratory": "PHY.MAT;ACT.EXP",
    "Defense, Intelligence & Emergency": "SOC.POL;ACT.INC;INF.KNW",
    "Advertising & Marketing": "SOC.ECO;INF.MED;ACT.CAM",
    "Tax, e-Invoicing & Audit": "SOC.ECO;SOC.POL;ACT.REG",
    "Survey, Statistics & Official Data": "INF.DAT;ACT.RES",
    "Telecom Billing, Roaming & Numbering": "ACT.SRV;SOC.ECO;XCT.ID",
    "Maritime & Hydrographic": "PHY.PLC;PHY.FLW;PHY.EAR",
    "Retail, Point-of-Sale & Hospitality": "SOC.ECO;ACT.SRV",
}

GROUP_MODEL_LINKS = {
    "Healthcare & Life Sciences": "WM-LIV-002;WM-LIV-021;WM-ACT-014;WM-ACT-018;WM-ACT-046;WM-ACT-049;WM-OBJ-005",
    "Software, DevOps & Security Artifacts": "WM-SFT-001;WM-SFT-007;WM-SFT-012;WM-SFT-014;WM-ACT-020;WM-ACT-042",
    "AI, ML & Data Governance": "WM-AI-001;WM-SFT-004;WM-AI-003;WM-AI-004;WM-AI-008;WM-DAT-001",
    "Commerce, Product & Supply Chain": "WM-OBJ-002;WM-OBJ-001;WM-ECO-019;WM-ECO-020;WM-FLW-011;WM-FLW-013",
    "Finance & Insurance": "WM-ECO-015;WM-ECO-016;WM-ECO-017;WM-ECO-018;WM-ECO-003;WM-ECO-036",
    "Government, Legal & Civic": "WM-POL-001;WM-POL-009;WM-POL-017;WM-POL-019;WM-POL-021;WM-POL-023",
    "Bioinformatics & Genomics Formats": "WM-LIV-011;WM-LIV-012;WM-LIV-013;WM-LIV-014;WM-LIV-015",
    "Tax, e-Invoicing & Audit": "WM-POL-011;WM-ECO-008;WM-ECO-032;WM-ECO-035;WM-ACT-052",
    "Advertising & Marketing": "WM-ECO-027;WM-ECO-028;WM-ACT-028;WM-MED-001",
    "Research Data, Scholarly & Identifiers": "WM-ACT-036;WM-REC-004;WM-DAT-001;WM-MAT-005;WM-KNW-008",
}

FIELDS = [
    "registry_id", "record_plane", "model_id", "name", "alternate_names", "entry_kind",
    "origin", "status", "review_state", "nav_path", "domain_tags", "legacy_alias", "existing_spec_ref",
    "parent_ids", "contains_ids", "aligned_model_ids", "purpose", "owner_or_maintainer",
    "source_url", "namespace_uri", "source_version_or_year", "source_group", "source_category",
    "source_format", "composition_role", "default_link_type", "priority_wave", "priority_score",
    "priority_method", "priority_confidence", "priority_rationale", "factor_demand", "factor_data", "factor_reuse", "factor_interop",
    "factor_feasibility", "factor_robotics", "factor_overlap", "possible_duplicate_of", "shared_source_with", "relations_ref", "validation_flags",
    "provenance",
]

XCT_NAV = {
    1: "OWN", 2: "ACC", 3: "DSC", 4: "AUD", 5: "PRV", 6: "PRF", 7: "ENF",
    8: "QTY", 9: "TME", 10: "LOC", 11: "IDS", 12: "PROV", 13: "REG",
    14: "LED", 15: "EVREG", 16: "IDREG", 17: "CRED", 18: "FED", 19: "SEC",
    20: "CLS", 21: "LIF", 22: "VER", 23: "ROLE", 24: "CONTACT", 25: "OBS",
    26: "QLT", 27: "RSK", 28: "EVD", 29: "OBL", 30: "NTF", 31: "LNG",
    32: "MNY", 33: "GEO", 34: "SIG", 35: "RET", 36: "ALS", 37: "DEP", 38: "POL",
}

ENTRY_KIND_OVERRIDES = {
    "WM-ACT-016": "pattern",
    "WM-REC-006": "view-candidate",
    "WM-OBJ-014": "subtype-profile",
    "WM-ECO-005": "category-split-required",
    "WM-POL-006": "category-split-required",
}

PURPOSE_OVERRIDES = {
    "WM-ECO-004": "Currency, monetary unit or transferable monetary instrument used to denominate and store value.",
    "WM-ECO-009": "A transfer that discharges or changes a monetary obligation, with payer, payee, amount, method and settlement state.",
    "WM-REC-002": "A governed factual or analytical statement issued for an audience and reporting period.",
    "WM-REC-004": "A scholarly work with authorship, venue, review, citation and publication lifecycle.",
    "WM-MED-001": "An intellectual or artistic work distinct from its files, renditions and publication events.",
    "WM-SFT-003": "A versioned machine or human interface contract with independent provider-consumer lifecycle.",
    "WM-VRT-005": "An account within a service or virtual environment; distinct from the person's federated digital identity.",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def slug(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")[:64] or "entry"


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()).strip()


def normalize_url(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    try:
        parts = urlsplit(value if "://" in value else "https://" + value)
        path = re.sub(r"/+", "/", parts.path).rstrip("/")
        return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))
    except ValueError:
        return value.lower().rstrip("/")


def factor_profile(wave: int) -> dict[str, float]:
    profiles = {
        0: dict(demand=.92, data=.84, reuse=.88, interop=.82, feasibility=.88, robotics=.00, overlap=.06),
        1: dict(demand=.82, data=.72, reuse=.64, interop=.74, feasibility=.79, robotics=.02, overlap=.08),
        2: dict(demand=.62, data=.62, reuse=.52, interop=.66, feasibility=.68, robotics=.06, overlap=.10),
        3: dict(demand=.36, data=.47, reuse=.34, interop=.56, feasibility=.52, robotics=.20, overlap=.10),
    }
    return profiles[wave]


def score(f: dict[str, float]) -> int:
    positive = .30*f["demand"] + .20*f["data"] + .15*f["reuse"] + .15*f["interop"] + .20*f["feasibility"]
    return round(100 * positive * (1-.55*f["robotics"]) * (1-.25*f["overlap"]))


def robotics_factor(name: str) -> float:
    n = name.lower()
    if any(term in n for term in ("robot", "kinematic", "actuator", "fleet coordination")):
        return .60
    if any(term in n for term in ("simulation scenario", "autonomous machine")):
        return .25
    if any(term in n for term in ("digital twin", "simulation")):
        return .08
    return .00


def owner_for_nav(nav: str) -> str:
    prefix = ".".join(nav.removeprefix("NAV.").split(".")[:2])
    return {
        "PHY.LIV": "scientific authority, biobank, healthcare or environmental steward",
        "PHY.MAT": "laboratory, manufacturer or material authority",
        "PHY.OBJ": "manufacturer, asset owner or inventory steward",
        "PHY.BLT": "site, facility or infrastructure owner/operator",
        "PHY.EAR": "environmental or Earth-observation authority",
        "PHY.SPC": "mission operator or astronomical authority",
        "PHY.FLW": "supply, logistics, utility or network operator",
        "SOC.PER": "the person or an explicitly authorized identity steward",
        "SOC.ORG": "the organization or authoritative register",
        "SOC.POL": "competent public or legal authority",
        "SOC.ECO": "contracting party, financial institution or regulator",
        "INF.REC": "record owner or records-management authority",
        "INF.DAT": "data product owner or data steward",
        "INF.KNW": "knowledge owner, standards body or decision authority",
        "INF.MED": "creator, publisher or rights holder",
        "INF.SFT": "software product/service owner",
        "INF.AI": "AI system owner and accountable deployer",
        "INF.VRT": "virtual environment or platform operator",
        "XCT.LIF": "governance steward designated by the adopting Dimension",
        "ACT.HCR": "healthcare provider or patient-authorized steward",
        "ACT.RES": "research sponsor or principal investigator",
    }.get(prefix, "owner designated by the adopting Dimension")


def desired_rows() -> list[dict[str, str]]:
    legacy = {row["ID"]: row for row in read_csv(LEGACY)}
    legacy_files = {}
    for path in REPO.glob("models/**/*.md"):
        match = re.match(r"([A-Z]\d+)-", path.name)
        if match:
            legacy_files[match.group(1)] = path.relative_to(REPO).as_posix()
    result = []
    for src in read_csv(DESIRED):
        aliases = list(dict.fromkeys(a for a in re.findall(r"\b[A-Z]\d+\b", src["legacy_alias"]) if a in legacy))
        old_rows = [legacy[a] for a in aliases]
        old = old_rows[0] if len(old_rows) == 1 else {}
        row = {field: "" for field in FIELDS}
        nav = {"WM-COM-001": "NAV.INF.COM.SVC", "WM-ACT-023": "NAV.ACT.HCR.PUB", "WM-ACT-016": "NAV.ACT.EVT.OBS"}.get(src["model_id"], src["nav_path"])
        if src["model_id"].startswith("WM-XCT-"):
            nav = f"NAV.XCT.{XCT_NAV[int(src['model_id'][-3:])]}"
        purpose = PURPOSE_OVERRIDES.get(src["model_id"], old.get("Purpose", "")) or f"Candidate governed context model for {src['name']}; boundary questions remain required."
        owners = "; ".join(dict.fromkeys(r["OwnerArchetype"] for r in old_rows if r["OwnerArchetype"]))
        spec_refs = ";".join(legacy_files[a] for a in aliases if a in legacy_files)
        raw_notes = src["review_notes"]
        if src["model_id"] == "WM-VRT-005":
            raw_notes = "KEEP-BOTH: service/platform account is distinct from federated digital identity"
        elif src["model_id"] == "WM-SFT-003":
            raw_notes = "KEEP-STANDALONE: API contract has independent version, owner and consumers"
        elif src["model_id"] in ENTRY_KIND_OVERRIDES:
            raw_notes = (raw_notes + " | " if raw_notes else "") + f"resolved-kind={ENTRY_KIND_OVERRIDES[src['model_id']]}"
        factors = {key: float(src[f"factor_{key}"]) for key in ("demand", "data", "reuse", "interop", "feasibility", "robotics", "overlap")}
        factors["robotics"] = robotics_factor(src["name"])
        row.update({
            "registry_id": src["registry_id"], "record_plane": "world-model", "model_id": src["model_id"],
            "name": src["name"], "entry_kind": ENTRY_KIND_OVERRIDES.get(src["model_id"], src["entry_kind"]), "origin": "grok-union-current",
            "status": "described-previous-version" if aliases else "candidate",
            "review_state": "migration-boundary-review" if aliases else "first-pass-reviewed", "nav_path": nav,
            "domain_tags": nav.removeprefix("NAV."), "legacy_alias": ";".join(aliases), "existing_spec_ref": spec_refs,
            "parent_ids": src["parent_mm"], "contains_ids": src["contains_mm"],
            "purpose": purpose, "owner_or_maintainer": owners or owner_for_nav(nav),
            "source_version_or_year": "2026-08-22", "priority_wave": src["priority_wave"],
            "priority_score": str(score(factors)), "priority_method": "cohort-proxy with model-specific robotics check; use TOP-50 sequence",
            "priority_confidence": "low", "priority_rationale": src["priority_rationale"],
            **{f"factor_{key}": f"{value:.2f}" for key, value in factors.items()},
            "validation_flags": raw_notes,
            "provenance": "current-112 + Grok review + Claude adversarial audit",
        })
        result.append(row)
    return result


def addition_rows() -> list[dict[str, str]]:
    result = []
    for line in ADDITIONS_TSV.strip().splitlines():
        mid, name, kind, nav, wave_s, parent, rationale = line.split("\t")
        if mid.startswith("WM-XCT-"):
            nav = f"NAV.XCT.{XCT_NAV[int(mid[-3:])]}"
        wave = int(wave_s)
        factors = factor_profile(wave)
        factors["robotics"] = robotics_factor(name)
        row = {field: "" for field in FIELDS}
        row.update({
            "registry_id": f"vr.{mid.lower()}", "record_plane": "world-model", "model_id": mid,
            "name": name, "entry_kind": kind, "origin": "claude-plus-gap-audit",
            "status": "candidate", "review_state": "boundary-review-required", "nav_path": nav,
            "domain_tags": nav.removeprefix("NAV."), "parent_ids": parent, "purpose": rationale,
            "owner_or_maintainer": owner_for_nav(nav),
            "source_version_or_year": "2026-08-22", "priority_wave": str(wave),
            "priority_score": str(score(factors)), "priority_method": "cohort-proxy with model-specific robotics check; use TOP-50 sequence",
            "priority_confidence": "low", "priority_rationale": rationale,
            **{f"factor_{key}": f"{value:.2f}" for key, value in factors.items()},
            "provenance": "Claude independent review + systematic gap audit + Claude adversarial audit",
        })
        result.append(row)
    return result


def external_kind(category: str) -> str:
    c = category.lower()
    if "metamodel" in c or "modeling language" in c:
        return "external-metamodel"
    if "information model" in c or "ontology" in c or "knowledge graph" in c or "geometry/product model" in c or "geometry/scene model" in c:
        return "external-semantic-model"
    if any(x in c for x in ("controlled vocabulary", "vocabulary", "code list", "classification", "terminology")):
        return "vocabulary-classification"
    if "identifier" in c:
        return "identifier-scheme"
    if any(x in c for x in ("protocol", "messaging", "api", "service api", "interface definition")):
        return "protocol-interface"
    if any(x in c for x in ("format", "encoding", "schema language", "serialization", "structured authoring")):
        return "format-schema"
    if "application profile" in c:
        return "application-profile"
    if "framework" in c or "methodology" in c:
        return "framework-method"
    return "external-standard"


def normalized_status(value: str) -> str:
    v = value.lower()
    if any(x in v for x in ("deprecated", "withdrawn", "obsolete", "superseded", "legacy")):
        return "legacy-or-superseded"
    if any(x in v for x in ("draft", "candidate", "proposed", "working")):
        return "draft-or-proposed"
    if any(x in v for x in ("active", "published", "standard", "recommendation", "stable", "current", "operational", "final", "ratified", "living", "formal", "in force", "open")):
        return "active-or-published"
    return "status-unverified"


def external_rows() -> list[dict[str, str]]:
    source = read_csv(EXTERNAL)
    result = []
    seen_identities: dict[str, str] = {}
    seen_urls: dict[str, str] = {}
    used_ids: set[str] = set()
    for src in source:
        normalized_source = normalize_url(src["SpecificationSourceURL"])
        identity = normalize(src["Name"]) + "|" + normalize(src["Maintainer"])
        fingerprint = normalized_source + "|" + identity
        digest = hashlib.sha1(fingerprint.encode("utf-8")).hexdigest()[:8]
        rid = f"ext.{slug(src['Acronym'] or src['Name'])}.{digest}"
        if rid in used_ids:
            rid += "." + hashlib.sha1((src["Name"] + src["Group"]).encode()).hexdigest()[:4]
        used_ids.add(rid)
        duplicate = seen_identities.get(identity, "")
        shared_source = seen_urls.get(normalized_source, "") if normalized_source else ""
        seen_identities.setdefault(identity, rid)
        if normalized_source:
            seen_urls.setdefault(normalized_source, rid)
        kind = external_kind(src["Category"])
        state = normalized_status(src["Status"])
        base = {"external-metamodel": 76, "external-semantic-model": 74, "vocabulary-classification": 68,
                "identifier-scheme": 66, "application-profile": 62, "framework-method": 58,
                "protocol-interface": 54, "format-schema": 48, "external-standard": 55}[kind]
        if state == "legacy-or-superseded":
            base -= 25
        elif state == "draft-or-proposed":
            base -= 8
        row = {field: "" for field in FIELDS}
        row.update({
            "registry_id": rid, "record_plane": "interoperability", "name": src["Name"],
            "alternate_names": src["Acronym"], "entry_kind": kind, "origin": "vercy-external-catalogue",
            "status": state, "review_state": "source-normalized", "nav_path": "EXT." + slug(src["Group"]).upper().replace("-", "."),
            "domain_tags": GROUP_DOMAINS.get(src["Group"], "UNMAPPED"),
            "aligned_model_ids": GROUP_MODEL_LINKS.get(src["Group"], ""), "purpose": src["Notes"],
            "owner_or_maintainer": src["Maintainer"], "source_url": src["SpecificationSourceURL"],
            "namespace_uri": src["NamespaceURI"], "source_version_or_year": src["Year"],
            "source_group": src["Group"], "source_category": src["Category"], "source_format": src["Format"],
            "composition_role": src["CompositionalRole"], "default_link_type": src["DefaultLinkType"],
            "priority_wave": "1" if base >= 65 else "2" if base >= 50 else "3", "priority_score": str(max(base, 0)),
            "priority_method": "entry-kind-and-source-status proxy", "priority_confidence": "low",
            "priority_rationale": "Interoperability priority by semantic role and lifecycle status",
            "possible_duplicate_of": duplicate, "shared_source_with": shared_source,
            "validation_flags": "exact-name-maintainer-duplicate" if duplicate else ("shared-source-url-review" if shared_source else ""),
            "provenance": "external-models.csv",
        })
        result.append(row)
    return result


def similarity_review(world: list[dict[str, str]]) -> list[dict[str, str]]:
    result = []
    for i, left in enumerate(world):
        ln = normalize(left["name"])
        for right in world[i+1:]:
            rn = normalize(right["name"])
            ratio = SequenceMatcher(None, ln, rn).ratio()
            tokens_l, tokens_r = set(ln.split()), set(rn.split())
            jaccard = len(tokens_l & tokens_r) / max(1, len(tokens_l | tokens_r))
            if ratio >= .76 or jaccard >= .60:
                result.append({
                    "left_id": left["model_id"], "left_name": left["name"],
                    "right_id": right["model_id"], "right_name": right["name"],
                    "name_similarity": f"{ratio:.3f}", "token_jaccard": f"{jaccard:.3f}",
                    "review": "boundary-or-synonym-review",
                })
    return sorted(result, key=lambda r: (-float(r["name_similarity"]), -float(r["token_jaccard"])))


def apply_relations(world: list[dict[str, str]]) -> None:
    if not RELATIONS.exists():
        return
    by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    for relation in read_csv(RELATIONS):
        by_source[relation["source_model_id"]].append(relation)
    for row in world:
        outgoing = by_source.get(row["model_id"], [])
        contains = [r["target_model_id"] for r in outgoing if r["relation_type"] == "CONTAINS"]
        existing = [x for x in row["contains_ids"].split(";") if x]
        row["contains_ids"] = ";".join(dict.fromkeys(existing + contains))
        row["composition_role"] = ";".join(dict.fromkeys(r["relation_type"] for r in outgoing))
        row["default_link_type"] = "TYPED-EDGES" if outgoing else ""
        row["relations_ref"] = "planning/VERCY-MODEL-RELATIONS.csv" if outgoing else ""


def audit(rows: list[dict[str, str]]) -> dict:
    world = [r for r in rows if r["record_plane"] == "world-model"]
    ext = [r for r in rows if r["record_plane"] == "interoperability"]
    ids = Counter(r["registry_id"] for r in rows)
    mids = Counter(r["model_id"] for r in world)
    parent_missing = sorted({p for r in world for p in r["parent_ids"].split(";") if p and p not in mids})
    return {
        "generated": "2026-08-22",
        "total_entries": len(rows), "world_model_entries": len(world), "interoperability_entries": len(ext),
        "world_by_kind": dict(sorted(Counter(r["entry_kind"] for r in world).items())),
        "world_by_wave": dict(sorted(Counter(r["priority_wave"] for r in world).items())),
        "external_by_kind": dict(sorted(Counter(r["entry_kind"] for r in ext).items())),
        "external_by_status": dict(sorted(Counter(r["status"] for r in ext).items())),
        "external_groups": dict(sorted(Counter(r["source_group"] for r in ext).items())),
        "duplicate_registry_ids": [k for k, v in ids.items() if v > 1],
        "duplicate_model_ids": [k for k, v in mids.items() if v > 1],
        "external_possible_duplicates": sum(bool(r["possible_duplicate_of"]) for r in ext),
        "external_shared_source_urls": sum(bool(r["shared_source_with"]) for r in ext),
        "missing_parent_model_ids": parent_missing,
        "world_missing_name": sum(not r["name"] for r in world),
        "world_missing_nav": sum(not r["nav_path"] for r in world),
        "world_with_contains": sum(bool(r["contains_ids"]) for r in world),
        "world_with_typed_relations": sum(bool(r["composition_role"]) for r in world),
        "world_described_previous_version": sum(r["status"] == "described-previous-version" for r in world),
        "world_low_confidence_priority": sum(r["priority_confidence"] == "low" for r in world),
        "external_missing_source_url": sum(not r["source_url"] for r in ext),
        "external_unmapped_domain": sum(r["domain_tags"] == "UNMAPPED" for r in ext),
    }


def main() -> None:
    world = desired_rows() + addition_rows()
    apply_relations(world)
    external = external_rows()
    rows = sorted(world, key=lambda r: (int(r["priority_wave"]), -int(r["priority_score"]), r["nav_path"], r["model_id"]))
    rows += sorted(external, key=lambda r: (-int(r["priority_score"]), r["source_group"], r["name"]))
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, FIELDS)
        writer.writeheader(); writer.writerows(rows)
    similarities = similarity_review(world)
    with SIMILAR.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, similarities[0].keys())
        writer.writeheader(); writer.writerows(similarities)
    AUDIT_JSON.write_text(json.dumps(audit(rows), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit(rows), ensure_ascii=False, indent=2))
    print(f"similarity pairs: {len(similarities)}")


if __name__ == "__main__":
    main()
