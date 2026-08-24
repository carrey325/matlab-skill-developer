---
name: validate-credit-risk-model-workflow
description: Independently validate a credit-risk model through scope, independence, conceptual soundness, data and implementation verification, benchmarking, outcomes analysis, limitations, and disposition decisions. Use when a new model, material change, periodic review, or serious monitoring finding requires an independent validation opinion. Not for model development, developer self-testing, or production monitoring.
---

# Purpose

Independently validate a credit-risk model through scope, independence, conceptual soundness, data and implementation verification, benchmarking, outcomes analysis, limitations, and disposition decisions.

# Scope and Applicability

Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence.

A new model, material change, periodic review, or serious monitoring finding requires an independent validation opinion.

Do not use for model development self-testing, model approval by the owner, production monitoring, or regulatory approval claims.

## Exclusions

- model development
- developer self-testing
- production monitoring
- regulatory approval
- remediation implementation

# Required Inputs

- Model inventory record and intended use.
- Development package, code, data, and limitations.
- Validation mandate, materiality, and independence record.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Model inventory record and intended use, development package, code, data, and limitations, validation mandate, materiality, and independence record.
- Outputs: Independent validation scope, conceptual, implementation, and outcomes findings, limitations and remediation requirements, validation disposition and escalation record.

## Set risk-based validation scope

- Inputs: Model use, exposure, complexity, change magnitude, prior findings, and potential harm.
- Outputs: Decision record for set risk-based validation scope.

## Determine validator independence

- Inputs: Reporting line, development involvement, incentives, authority, competence, and access to evidence.
- Outputs: Decision record for determine validator independence.

## Assess conceptual soundness

- Inputs: Purpose alignment, theory, assumptions, variable logic, segmentation, horizon, and alternatives.
- Outputs: Decision record for assess conceptual soundness.

## Verify data and implementation

- Inputs: Independent data lineage checks, code reproduction, transformations, parameter version, and output reconciliation.
- Outputs: Decision record for verify data and implementation.

## Select benchmark and challenger evidence

- Inputs: Materiality, available data, model complexity, accepted practice, and prior benchmarks.
- Outputs: Decision record for select benchmark and challenger evidence.

## Judge outcomes and stability

- Inputs: Calibration, discrimination, segment results, time stability, overrides, use tests, and backtesting as applicable.
- Outputs: Decision record for judge outcomes and stability.

## Classify limitations and compensating controls

- Inputs: Impact, likelihood, detectability, affected use, available controls, and remediation time.
- Outputs: Decision record for classify limitations and compensating controls.

## Issue independent validation disposition

- Inputs: Severity and interaction of conceptual, implementation, outcomes, governance, and limitation findings.
- Outputs: Decision record for issue independent validation disposition.

## Execute the approved validation computation

- Work: Run the approved computational specification without changing professional choices.

## Assess validation technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the validation professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Set risk-based validation scope.** Consider model use, exposure, complexity, change magnitude, prior findings, and potential harm. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set risk-based validation scope.
- **Determine validator independence.** Consider reporting line, development involvement, incentives, authority, competence, and access to evidence. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine validator independence.
- **Assess conceptual soundness.** Consider purpose alignment, theory, assumptions, variable logic, segmentation, horizon, and alternatives. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess conceptual soundness.
- **Verify data and implementation.** Consider independent data lineage checks, code reproduction, transformations, parameter version, and output reconciliation. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to verify data and implementation.
- **Select benchmark and challenger evidence.** Consider materiality, available data, model complexity, accepted practice, and prior benchmarks. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select benchmark and challenger evidence.
- **Judge outcomes and stability.** Consider calibration, discrimination, segment results, time stability, overrides, use tests, and backtesting as applicable. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to judge outcomes and stability.
- **Classify limitations and compensating controls.** Consider impact, likelihood, detectability, affected use, available controls, and remediation time. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to classify limitations and compensating controls.
- **Issue independent validation disposition.** Consider severity and interaction of conceptual, implementation, outcomes, governance, and limitation findings. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to issue independent validation disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **validation technical fitness.** Assess: determine validator independence, assess conceptual soundness, verify data and implementation, select benchmark and challenger evidence. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **validation use and release boundary.** Assess: set risk-based validation scope, issue independent validation disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Independent validation scope.
- Conceptual, implementation, and outcomes findings.
- Limitations and remediation requirements.
- Validation disposition and escalation record.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide scope — Set risk-based validation scope
- Decide independence — Determine validator independence
- Decide concept — Assess conceptual soundness
- Decide implementation — Verify data and implementation
- Decide benchmark — Select benchmark and challenger evidence
- Decide outcomes — Judge outcomes and stability
- Decide limitations — Classify limitations and compensating controls
- Decide disposition — Issue independent validation disposition
- Package validate evidence — Package the validation professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute validate analysis
- Compute validate validation evidence

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
