---
name: monitor-credit-risk-model-workflow
description: Monitor an approved credit-risk model using controlled baselines, policy thresholds, drift diagnosis, performance evidence, overrides, change assessment, and explicit continue, limit, recalibrate, redevelop, or escalate decisions. Use when a scheduled monitoring cycle, threshold breach, data change, implementation change, or external event requires a documented model-use decision. Not for initial model development, independent validation, or automatic model change.
---

# Purpose

Monitor an approved credit-risk model using controlled baselines, policy thresholds, drift diagnosis, performance evidence, overrides, change assessment, and explicit continue, limit, recalibrate, redevelop, or escalate decisions.

# Scope and Applicability

Ongoing monitoring after approval for credit-risk models and their implemented data and use environment.

A scheduled monitoring cycle, threshold breach, data change, implementation change, or external event requires a documented model-use decision.

Do not use for initial development, independent periodic validation, automatic recalibration, or model approval.

## Exclusions

- initial model development
- independent validation
- automatic model change
- production deployment
- approval authority

# Required Inputs

- Approved model and validation conditions.
- Monitoring population, predictions, outcomes, and implementation records.
- Institution-approved thresholds and escalation policy.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Approved model and validation conditions, monitoring population, predictions, outcomes, and implementation records, institution-approved thresholds and escalation policy.
- Outputs: Monitoring-period data and baseline reconciliation, drift and performance diagnosis, threshold and limitation assessment, continue, limit, recalibrate, redevelop, or escalate recommendation.

## Select monitoring population and baseline

- Inputs: Approved population, current use, reference period, outcome maturity, and data-definition continuity.
- Outputs: Decision record for select monitoring population and baseline.

## Apply institution-approved threshold policy

- Inputs: Metric definitions, amber/red criteria, observation requirements, aggregation rules, and authority.
- Outputs: Decision record for apply institution-approved threshold policy.

## Diagnose input and population drift

- Inputs: Changes in population mix, predictors, missingness, data lineage, policy, and economic environment.
- Outputs: Decision record for diagnose input and population drift.

## Diagnose calibration and discrimination change

- Inputs: Observed outcomes, expected outcomes, ranking metrics, segments, confidence, and time stability.
- Outputs: Decision record for diagnose calibration and discrimination change.

## Assess overrides and use divergence

- Inputs: Override rates, reasons, concentrations, approval patterns, downstream transformations, and unapproved uses.
- Outputs: Decision record for assess overrides and use divergence.

## Classify remediation as recalibration or redevelopment

- Inputs: Whether weakness is level-only, relationship-level, data-definition, structural, or use-related.
- Outputs: Decision record for classify remediation as recalibration or redevelopment.

## Determine interim model-use status

- Inputs: Impact, uncertainty, affected decisions, compensating controls, and remediation duration.
- Outputs: Decision record for determine interim model-use status.

## Select final monitoring action

- Inputs: Threshold results, root cause, materiality, control strength, prior breaches, and governance policy.
- Outputs: Decision record for select final monitoring action.

## Execute the approved monitoring computation

- Work: Run the approved computational specification without changing professional choices.

## Assess monitoring technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the monitoring professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Select monitoring population and baseline.** Consider approved population, current use, reference period, outcome maturity, and data-definition continuity. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select monitoring population and baseline.
- **Apply institution-approved threshold policy.** Consider metric definitions, amber/red criteria, observation requirements, aggregation rules, and authority. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to apply institution-approved threshold policy.
- **Diagnose input and population drift.** Consider changes in population mix, predictors, missingness, data lineage, policy, and economic environment. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to diagnose input and population drift.
- **Diagnose calibration and discrimination change.** Consider observed outcomes, expected outcomes, ranking metrics, segments, confidence, and time stability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to diagnose calibration and discrimination change.
- **Assess overrides and use divergence.** Consider override rates, reasons, concentrations, approval patterns, downstream transformations, and unapproved uses. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess overrides and use divergence.
- **Classify remediation as recalibration or redevelopment.** Consider whether weakness is level-only, relationship-level, data-definition, structural, or use-related. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to classify remediation as recalibration or redevelopment.
- **Determine interim model-use status.** Consider impact, uncertainty, affected decisions, compensating controls, and remediation duration. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine interim model-use status.
- **Select final monitoring action.** Consider threshold results, root cause, materiality, control strength, prior breaches, and governance policy. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select final monitoring action.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **monitoring technical fitness.** Assess: apply institution-approved threshold policy, diagnose input and population drift, diagnose calibration and discrimination change, assess overrides and use divergence. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **monitoring use and release boundary.** Assess: select monitoring population and baseline, select final monitoring action, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Monitoring-period data and baseline reconciliation.
- Drift and performance diagnosis.
- Threshold and limitation assessment.
- Continue, limit, recalibrate, redevelop, or escalate recommendation.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide baseline — Select monitoring population and baseline
- Decide threshold — Apply institution-approved threshold policy
- Decide drift — Diagnose input and population drift
- Decide performance — Diagnose calibration and discrimination change
- Decide override — Assess overrides and use divergence
- Decide change — Classify remediation as recalibration or redevelopment
- Decide use — Determine interim model-use status
- Decide escalation — Select final monitoring action
- Package monitor evidence — Package the monitoring professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute monitor analysis
- Compute monitor validation evidence

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
