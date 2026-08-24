---
name: stress-test-credit-portfolio-workflow
description: Stress-test a credit portfolio by selecting purpose and scenarios, translating macro paths into credit parameters, applying exposure assumptions, measuring concentration and sensitivities, and escalating material limitations or outcomes. Use when a risk owner has approved baseline and adverse scenarios and needs their portfolio loss and risk impacts assessed. Not for base parameter development, scenario authority approval, or regulatory capital determination.
---

# Purpose

Stress-test a credit portfolio by selecting purpose and scenarios, translating macro paths into credit parameters, applying exposure assumptions, measuring concentration and sensitivities, and escalating material limitations or outcomes.

# Scope and Applicability

Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models.

A risk owner has approved baseline and adverse scenarios and needs their portfolio loss and risk impacts assessed.

Do not use to invent supervisory scenarios, develop base PD/LGD/EAD models, determine regulatory capital, or execute management actions.

## Exclusions

- base parameter development
- scenario authority approval
- regulatory capital determination
- management action execution
- climate scenario design

# Required Inputs

- Approved stress-testing purpose and scenario paths.
- Portfolio positions and governed parameter models.
- Balance-sheet, management-action, concentration, and capital assumptions.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Approved stress-testing purpose and scenario paths, portfolio positions and governed parameter models, balance-sheet, management-action, concentration, and capital assumptions.
- Outputs: Scenario and translation contract, stressed PD, LGD, EAD, and portfolio losses, concentration and sensitivity results, limitations, escalation, and reporting package.

## Determine stress-test purpose and authority

- Inputs: Internal risk, capital planning, supervisory, reverse-stress, or exploratory purpose and accountable owner.
- Outputs: Decision record for determine stress-test purpose and authority.

## Select and validate scenario set

- Inputs: Risk narrative, macro paths, severity, plausibility, internal consistency, baseline, horizon, and coverage.
- Outputs: Decision record for select and validate scenario set.

## Select macro-to-credit translation

- Inputs: Model rating philosophy, macro links, lags, nonlinearities, segment coverage, and extrapolation range.
- Outputs: Decision record for select macro-to-credit translation.

## Stress PD, LGD, and EAD consistently

- Inputs: Conditionality, scenario horizon, downturn/recovery effects, utilisation, dependencies, and double counting.
- Outputs: Decision record for stress PD, LGD, and EAD consistently.

## Set balance-sheet and exposure evolution

- Inputs: Static/dynamic rule, amortisation, new business, defaults, cures, limits, and management actions.
- Outputs: Decision record for set balance-sheet and exposure evolution.

## Assess stressed concentration and dependence

- Inputs: Single names, sectors, regions, collateral, correlated parameter shifts, and migration clustering.
- Outputs: Decision record for assess stressed concentration and dependence.

## Design severity and assumption sensitivities

- Inputs: Key scenario, translation, correlation, recovery, exposure, and management-action uncertainties.
- Outputs: Decision record for design severity and assumption sensitivities.

## Determine stress-result disposition

- Inputs: Loss severity, concentration, capital effects, uncertainty, control findings, and risk-appetite policy.
- Outputs: Decision record for determine stress-result disposition.

## Execute the approved stress-test computation

- Work: Run the approved computational specification without changing professional choices.

## Assess stress-test technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the stress-test professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Determine stress-test purpose and authority.** Consider internal risk, capital planning, supervisory, reverse-stress, or exploratory purpose and accountable owner. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine stress-test purpose and authority.
- **Select and validate scenario set.** Consider risk narrative, macro paths, severity, plausibility, internal consistency, baseline, horizon, and coverage. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select and validate scenario set.
- **Select macro-to-credit translation.** Consider model rating philosophy, macro links, lags, nonlinearities, segment coverage, and extrapolation range. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select macro-to-credit translation.
- **Stress PD, LGD, and EAD consistently.** Consider conditionality, scenario horizon, downturn/recovery effects, utilisation, dependencies, and double counting. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to stress PD, LGD, and EAD consistently.
- **Set balance-sheet and exposure evolution.** Consider static/dynamic rule, amortisation, new business, defaults, cures, limits, and management actions. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set balance-sheet and exposure evolution.
- **Assess stressed concentration and dependence.** Consider single names, sectors, regions, collateral, correlated parameter shifts, and migration clustering. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess stressed concentration and dependence.
- **Design severity and assumption sensitivities.** Consider key scenario, translation, correlation, recovery, exposure, and management-action uncertainties. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to design severity and assumption sensitivities.
- **Determine stress-result disposition.** Consider loss severity, concentration, capital effects, uncertainty, control findings, and risk-appetite policy. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine stress-result disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **stress-test technical fitness.** Assess: select and validate scenario set, select macro-to-credit translation, stress PD, LGD, and EAD consistently, set balance-sheet and exposure evolution. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **stress-test use and release boundary.** Assess: determine stress-test purpose and authority, determine stress-result disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Scenario and translation contract.
- Stressed PD, LGD, EAD, and portfolio losses.
- Concentration and sensitivity results.
- Limitations, escalation, and reporting package.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide purpose — Determine stress-test purpose and authority
- Decide scenario — Select and validate scenario set
- Decide translation — Select macro-to-credit translation
- Decide parameters — Stress PD, LGD, and EAD consistently
- Decide balance — Set balance-sheet and exposure evolution
- Decide concentration — Assess stressed concentration and dependence
- Decide sensitivity — Design severity and assumption sensitivities
- Decide escalation — Determine stress-result disposition
- Package stress evidence — Package the stress-test professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute stress analysis
- Compute stress validation evidence

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
