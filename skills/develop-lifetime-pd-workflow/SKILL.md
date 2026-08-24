---
name: develop-lifetime-pd-workflow
description: Develop and developer-test lifetime probability-of-default models with explicit purpose, horizon, model-family, rating-philosophy, calibration, validation, recovery, and monitoring decisions. Use for professional model-development work; not for expected-credit-loss aggregation, deployment, credit approval, or independent approval.
---

# Purpose

Develop, developer-test, select, and package a lifetime probability-of-default model with explicit monitoring-design and governance boundaries.

# Scope and Applicability

Applies to professional lifetime-PD development for prudential, accounting-support, or internal-risk purposes when applicability branches and PD semantics are kept distinct.

Use this workflow when a practitioner must define, fit, developer-test, compare, and package a lifetime-PD model for a stated portfolio and decision use. Do not use it when the request is only to run already-specified code, calculate ECL, deploy a model, approve credit, or claim independent validation.

## Exclusions

- Expected-credit-loss aggregation or allowance calculation.
- LGD or EAD modeling.
- Production deployment or production monitoring automation.
- Credit approval or loan decision execution.
- Organizationally independent validation, regulatory approval, or model-risk approval.

# Required Inputs

- modeling-objective: Intended use, owner, portfolio, regime, horizon, rating philosophy needs, materiality, and acceptance authority.
- credit-data-lineage: Longitudinal exposure and default data with definitions, timestamps, provenance, transformations, and limitations.
- validation-context: Use-specific risk appetite, benchmarks, required tests, organizational validation boundary, and monitoring expectations.

# Professional Workflow

## Define purpose and applicability

Establish intended use, owner, portfolio, governing regime, exclusions, and adjacent handoffs.

- Assess or perform: Define purpose, applicability, default, horizon, PD semantics, and ownership before modeling.
- Required inputs: modeling-objective.
- Produce: bounded-objective, applicability-branch.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.
- Apply these professional decisions: Determine governing purpose and applicability.

## Define default, horizon, and PD semantics

Make default event, horizon, conditioning, cumulative logic, and observation timing explicit.

- Assess or perform: Define purpose, applicability, default, horizon, PD semantics, and ownership before modeling.
- Required inputs: bounded-objective, credit-data-lineage.
- Produce: default-and-horizon-contract.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.
- Apply these professional decisions: Define horizon and PD semantics.

## Assess data suitability

Assess lineage, consistency, missingness, representativeness, event coverage, and remediability.

- Assess or perform: Assess lineage, quality, representativeness, sample adequacy, limitations, and remediation.
- Required inputs: credit-data-lineage, default-and-horizon-contract.
- Produce: data-suitability-assessment.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.
- Apply these professional decisions: Determine data and sample route.

## Construct modeling and validation samples

Define reproducible inclusion, exclusions, intervals, feature timing, temporal or obligor partitions, and leakage controls.

- Assess or perform: Create a reproducible population, temporal split, data contract, and leakage controls.
- Required inputs: data-suitability-assessment.
- Produce: modeling-population, data-contract, sample-design.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.

## Specify candidate model designs

Select model family, predictor rationale, rating philosophy, calibration target, assumptions, and challenger set.

- Assess or perform: Apply explicit decision rules for model family, philosophy, calibration target, and disposition.
- Required inputs: modeling-population, data-contract, bounded-objective.
- Produce: candidate-specifications, selection-rationale.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.
- Apply these professional decisions: Select candidate model family, Select rating philosophy, Select calibration target.

## Fit approved candidate specifications

Estimate approved candidates reproducibly while preserving event, horizon, and predictor-timing conventions.

- Assess or perform: Fit only approved candidate specifications without changing their professional semantics.
- Required inputs: candidate-specifications, modeling-population, data-contract.
- Produce: fitted-candidates, fit-evidence.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.

## Assess discrimination

Evaluate ranking performance on held-out and relevant segment evidence, with uncertainty and benchmark context.

- Assess or perform: Assess discrimination, calibration, stability, assumptions, sensitivity, and limitations on appropriate evidence.
- Required inputs: fitted-candidates, validation-context.
- Produce: discrimination-evidence.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.

## Assess calibration

Evaluate target-consistent calibration by horizon, segment, and relevant period separately from ranking performance.

- Assess or perform: Assess discrimination, calibration, stability, assumptions, sensitivity, and limitations on appropriate evidence.
- Required inputs: fitted-candidates, validation-context.
- Produce: calibration-evidence.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.

## Assess stability, assumptions, and sensitivity

Test temporal and segment stability, model assumptions, economic sensitivity, overrides, and plausible perturbations.

- Assess or perform: Assess discrimination, calibration, stability, assumptions, sensitivity, and limitations on appropriate evidence.
- Required inputs: fitted-candidates, validation-context.
- Produce: stability-and-sensitivity-evidence.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.

## Select, limit, remediate, or reject

Integrate all gate outcomes and limitations into a traceable developer disposition without claiming independent approval.

- Assess or perform: Apply explicit decision rules for model family, philosophy, calibration target, and disposition.
- Required inputs: discrimination-evidence, calibration-evidence, stability-and-sensitivity-evidence.
- Produce: selection-decision.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.
- Apply these professional decisions: Select model disposition.

## Produce the development package

Document purpose, data, design, applied rules, evidence, assumptions, limitations, implementation contract, and approval boundary.

- Assess or perform: Package decisions, evidence, limitations, monitoring design, and independent-validation boundary.
- Required inputs: selection-decision, fitted-candidates.
- Produce: validated-pd-model-package, developer-validation-report.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.

## Define monitoring and escalation requirements

Define metrics, segments, frequencies, thresholds, drift diagnostics, owners, and actions; do not implement production monitoring.

- Assess or perform: Package decisions, evidence, limitations, monitoring design, and independent-validation boundary.
- Required inputs: validated-pd-model-package, developer-validation-report.
- Produce: monitoring-requirements.
- Complete only when: All named outputs are documented and internally consistent; Material assumptions, limitations, evidence, and escalation needs are explicit.

# Decision Policy

Use the concise policies below and load [decision rules](references/decision-rules.md) for conditions, rationale, applicability, exclusions, and missing-information behavior.

- Determine governing purpose and applicability: Separate prudential, accounting, and internal-risk purposes before defining PD semantics. Fallback: Stop and obtain a signed-off purpose, accountable owner, portfolio, and applicability assessment.
- Define horizon and PD semantics: Choose a PD quantity whose horizon, conditioning, and aggregation are consistent with the governing purpose. Fallback: Stop until horizon, conditional versus cumulative meaning, default event, and downstream use are explicit.
- Determine data and sample route: Decide whether data support development, require remediation, or justify only a limited-use analysis. Fallback: Stop when default consistency, lineage, or a defensible sample cannot be established.
- Select candidate model family: Match the statistical family to the observation structure, event timing, censoring, interpretability, and intended output before fitting. Fallback: Stop or research further when event timing, censoring, assumptions, or output semantics do not support a candidate family.
- Select rating philosophy: Choose desired sensitivity to current and forecast economic conditions and define expected migration and backtesting behavior. Fallback: Stop until the owner chooses and documents economic sensitivity, stability objective, and scenario use.
- Select calibration target: Choose a target consistent with purpose, horizon semantics, rating philosophy, segmentation, and observation period. Fallback: Stop or limit use when the target period, segment, or economic-condition basis is not representative and cannot be adjusted defensibly.
- Select model disposition: Integrate validation evidence, limitations, intended use, and governance boundaries into an explicit disposition. Fallback: Reject the candidate or escalate when evidence is incomplete, contradictory, or outside delegated acceptance authority.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- Discrimination and ranking gate: assess out-of-sample ranking, segment consistency, temporal variation, benchmark improvement, material bias. Use predeclared, use-specific thresholds; do not treat a statistically nonzero score or in-sample fit as acceptance.
- Calibration and horizon gate: assess target alignment, level bias, PD bounds, conditional-to-cumulative consistency, nondecreasing cumulative default probability where mathematically applicable, horizon shape, segment concentration, uncertainty and event scarcity. Apply thresholds and remediation actions defined before seeing final results; diagnose target, semantics, or segmentation mismatch before recalibration.
- Stability, assumptions, and sensitivity gate: assess performance stability, population and feature drift, assumption validity, economic sensitivity, override behavior, limitation materiality. Require diagnostics proportional to risk; a limitation may pass only when bounded, governed, and monitored, otherwise remediate or reject.

# Failure and Recovery

- Return to data assessment, correct lineage, definition, representativeness, partitioning, or event-coverage defects, and rerun the data decision.
- Diagnose whether the cause is specification, target, segmentation, implementation, or data; change only the implicated component and rerun all affected gates.

# Stop / Escalation Conditions

- Stop and escalate with a precise missing-information and impact statement; do not invent a model-development basis.
- Stop that representation, label the work developer testing, and hand off to the required independent validation or approval function.

# Deliverables

- validated-pd-model-package: Developer-selected specification, applied decision rules, data and implementation contract, evidence, assumptions, limitations, and handoffs.
- developer-validation-report: Risk-based discrimination, calibration, stability, sensitivity, assumption, limitation, and remediation evidence without an independent-approval claim.
- monitoring-requirements: Metrics, segments, frequencies, thresholds, diagnostics, owners, actions, and escalation triggers for later implementation.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- define professional purpose and applicability
- define default horizon and pd semantics
- assess credit data suitability
- design modeling and validation samples
- specify lifetime pd model design
- decide model disposition
- package model development evidence
- design model monitoring and escalation

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- fit lifetime pd models
- compute credit model discrimination
- compute credit model calibration
- compute credit model stability and sensitivity (implementation coverage gap must be resolved)

# Reference Loading

- Read [regulatory evidence](references/regulatory-evidence.md) when checking the authority, locator, applicability, or interpretation of a material claim.
- Read [decision rules](references/decision-rules.md) when choosing purpose, data route, model family, rating philosophy, calibration target, or acceptance route.
- Read [validation guidance](references/validation-guidance.md) when planning or evaluating developer validation and recovery.

# Final Quality Checks

- Confirm purpose, horizon, PD semantics, default definition, applicability, rating philosophy, and calibration target are explicit.
- Confirm every material selection records the applied rule and evidence-based rationale.
- Confirm validation distinguishes discrimination, calibration, stability, sensitivity, assumptions, and limitations.
- Confirm developer testing is not represented as organizationally independent validation or regulatory approval.
- Escalate rather than inventing missing material information.
