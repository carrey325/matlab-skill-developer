---
name: develop-credit-default-model-workflow
description: Develop a non-lifetime binary or multi-state credit default model with explicit target taxonomy, horizon, data structure, model-family, imbalance, interpretability, benchmarking, and disposition decisions. Use when a model owner needs a binary, ordinal, nominal, or nonlinear credit-risk model for a declared prediction and decision-support use. Not for lifetime PD term structures, points-based scorecard delivery, or transition-matrix estimation.
---

# Purpose

Develop a non-lifetime binary or multi-state credit default model with explicit target taxonomy, horizon, data structure, model-family, imbalance, interpretability, benchmarking, and disposition decisions.

# Scope and Applicability

Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.

A model owner needs a binary, ordinal, nominal, or nonlinear credit-risk model for a declared prediction and decision-support use.

Do not use for lifetime PD term structures, points-based scorecards, rating-transition matrices, production deployment, or independent validation.

## Exclusions

- lifetime PD term structures
- points-based scorecard delivery
- transition-matrix estimation
- production deployment
- independent approval

# Required Inputs

- Declared prediction use and target taxonomy.
- Borrower, account, performance, and timing data.
- Interpretability, operational, and validation constraints.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Declared prediction use and target taxonomy, borrower, account, performance, and timing data, interpretability, operational, and validation constraints.
- Outputs: Target and horizon contract, candidate-family and benchmark design, selected model and developer tests, limitations and monitoring design.

## Define the modeled credit event

- Inputs: Default or deterioration event, state labels, observation timing, cure/re-entry, and intended interpretation.
- Outputs: Decision record for define the modeled credit event.

## Select prediction horizon and output semantics

- Inputs: Decision timing, performance window, repeated forecasts, and whether cumulative risk is required.
- Outputs: Decision record for select prediction horizon and output semantics.

## Choose binary, ordinal, or nominal structure

- Inputs: Whether state labels have a defensible ordering and whether category distinctions are decision-relevant.
- Outputs: Decision record for choose binary, ordinal, or nominal structure.

## Determine panel, snapshot, or event-history data design

- Inputs: Repeated borrower observations, state dependence, censoring, sampling, and leakage risk.
- Outputs: Decision record for determine panel, snapshot, or event-history data design.

## Select statistical or nonlinear candidate family

- Inputs: Nonlinearity evidence, sample size, benchmark strength, interpretability, and operational constraints.
- Outputs: Decision record for select statistical or nonlinear candidate family.

## Treat class imbalance and rare states

- Inputs: Event counts, state frequencies, sampling design, cost asymmetry, and calibration target.
- Outputs: Decision record for treat class imbalance and rare states.

## Set interpretability and benchmark requirements

- Inputs: Decision materiality, adverse-action or explanation needs, challenger expectations, and governance burden.
- Outputs: Decision record for set interpretability and benchmark requirements.

## Determine default-model disposition

- Inputs: Out-of-sample discrimination, calibration, class-level performance, stability, benchmark comparison, and limitations.
- Outputs: Decision record for determine default-model disposition.

## Execute the approved default-model computation

- Work: Run the approved computational specification without changing professional choices.

## Assess default-model technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the default-model professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Define the modeled credit event.** Consider default or deterioration event, state labels, observation timing, cure/re-entry, and intended interpretation. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define the modeled credit event.
- **Select prediction horizon and output semantics.** Consider decision timing, performance window, repeated forecasts, and whether cumulative risk is required. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select prediction horizon and output semantics.
- **Choose binary, ordinal, or nominal structure.** Consider whether state labels have a defensible ordering and whether category distinctions are decision-relevant. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to choose binary, ordinal, or nominal structure.
- **Determine panel, snapshot, or event-history data design.** Consider repeated borrower observations, state dependence, censoring, sampling, and leakage risk. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine panel, snapshot, or event-history data design.
- **Select statistical or nonlinear candidate family.** Consider nonlinearity evidence, sample size, benchmark strength, interpretability, and operational constraints. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select statistical or nonlinear candidate family.
- **Treat class imbalance and rare states.** Consider event counts, state frequencies, sampling design, cost asymmetry, and calibration target. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to treat class imbalance and rare states.
- **Set interpretability and benchmark requirements.** Consider decision materiality, adverse-action or explanation needs, challenger expectations, and governance burden. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set interpretability and benchmark requirements.
- **Determine default-model disposition.** Consider out-of-sample discrimination, calibration, class-level performance, stability, benchmark comparison, and limitations. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine default-model disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **default-model technical fitness.** Assess: select prediction horizon and output semantics, choose binary, ordinal, or nominal structure, determine panel, snapshot, or event-history data design, select statistical or nonlinear candidate family. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **default-model use and release boundary.** Assess: define the modeled credit event, determine default-model disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Target and horizon contract.
- Candidate-family and benchmark design.
- Selected model and developer tests.
- Limitations and monitoring design.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide target — Define the modeled credit event
- Decide horizon — Select prediction horizon and output semantics
- Decide structure — Choose binary, ordinal, or nominal structure
- Decide data — Determine panel, snapshot, or event-history data design
- Decide family — Select statistical or nonlinear candidate family
- Decide imbalance — Treat class imbalance and rare states
- Decide interpret — Set interpretability and benchmark requirements
- Decide disposition — Determine default-model disposition
- Package default evidence — Package the default-model professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute default analysis
- Compute default validation evidence

# Reference Loading

- Read [regulatory evidence](references/regulatory-evidence.md) when checking the authority, locator, applicability, or interpretation of a material claim.
- Read [decision rules](references/decision-rules.md) when making a professional decision or applying its fallback.
- Read [validation guidance](references/validation-guidance.md) when planning or evaluating validation, acceptance, and recovery.

# Final Quality Checks

- Confirm purpose, definitions, applicability, material assumptions, and acceptance policy are explicit.
- Confirm every material selection records the applied rule and evidence-based rationale.
- Confirm validation distinguishes relevant performance, calibration or reconciliation, stability, sensitivity, assumptions, and limitations.
- Confirm developer testing is not represented as organizationally independent validation or regulatory approval.
- Escalate rather than inventing missing material information.
