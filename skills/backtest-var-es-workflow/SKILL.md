---
name: backtest-var-es-workflow
description: Independently backtest VaR and ES forecasts by reconciling P&L and forecast timing, selecting exception and statistical tests, assessing sample and serial dependence, applying applicable traffic-light policy, testing ES severity, diagnosing failures, and routing remediation. Use when a controlled sequence of VaR/ES forecasts and realised P&L must be tested for reliability and governance action. Not for VaR or ES estimation, forecast alteration, or trading recommendations.
---

# Purpose

Independently backtest VaR and ES forecasts by reconciling P&L and forecast timing, selecting exception and statistical tests, assessing sample and serial dependence, applying applicable traffic-light policy, testing ES severity, diagnosing failures, and routing remediation.

# Scope and Applicability

Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.

A controlled sequence of VaR/ES forecasts and realised P&L must be tested for reliability and governance action.

Do not use to estimate VaR/ES, alter forecasts, select trades, or claim regulatory approval from one test.

## Exclusions

- VaR or ES estimation
- forecast alteration
- trading recommendations
- automatic model approval
- unapproved universal thresholds

# Required Inputs

- Frozen VaR/ES forecast series and risk-measure contract.
- Controlled actual and hypothetical P&L.
- Test policy, sample window, and escalation criteria.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Frozen VaR/ES forecast series and risk-measure contract, controlled actual and hypothetical P&L, test policy, sample window, and escalation criteria.
- Outputs: Forecast-to-P&L reconciliation, VaR exception and independence tests, ES severity tests, diagnosis, limitations, and remediation disposition.

## Reconcile forecasts with realised P&L

- Inputs: Portfolio ID, date, horizon, confidence, sign, currency, position basis, missing values, and actual/hypothetical P&L.
- Outputs: Decision record for reconcile forecasts with realised P&L.

## Define VaR exceptions

- Inputs: Loss sign, VaR sign, equality treatment, missing observations, confidence, and P&L variant.
- Outputs: Decision record for define VaR exceptions.

## Select VaR test family

- Inputs: Frequency, independence, conditional coverage, time-between-failures, sample size, and policy requirement.
- Outputs: Decision record for select VaR test family.

## Assess sample size and test power

- Inputs: Usable observations, confidence level, expected exceptions, structural breaks, and missing periods.
- Outputs: Decision record for assess sample size and test power.

## Apply traffic-light or institutional policy

- Inputs: Jurisdiction, model use, confidence level, sample window, and approved escalation thresholds.
- Outputs: Decision record for apply traffic-light or institutional policy.

## Select expected-shortfall backtest

- Inputs: VaR/ES forecasts, tail observations, assumed distribution or simulation capability, and test objective.
- Outputs: Decision record for select expected-shortfall backtest.

## Diagnose backtest failure

- Inputs: Exception count, clustering, tail severity, volatility regime, P&L unexplained components, risk-factor gaps, and model changes.
- Outputs: Decision record for diagnose backtest failure.

## Determine backtesting disposition

- Inputs: P&L integrity, test results, power, policy zones, ES evidence, root cause, materiality, and prior failures.
- Outputs: Decision record for determine backtesting disposition.

## Execute the approved VARBACK computation

- Work: Run the approved computational specification without changing professional choices.

## Assess VARBACK technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the VARBACK professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Reconcile forecasts with realised P&L.** Consider portfolio ID, date, horizon, confidence, sign, currency, position basis, missing values, and actual/hypothetical P&L. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to reconcile forecasts with realised P&L.
- **Define VaR exceptions.** Consider loss sign, VaR sign, equality treatment, missing observations, confidence, and P&L variant. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define VaR exceptions.
- **Select VaR test family.** Consider frequency, independence, conditional coverage, time-between-failures, sample size, and policy requirement. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select VaR test family.
- **Assess sample size and test power.** Consider usable observations, confidence level, expected exceptions, structural breaks, and missing periods. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess sample size and test power.
- **Apply traffic-light or institutional policy.** Consider jurisdiction, model use, confidence level, sample window, and approved escalation thresholds. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to apply traffic-light or institutional policy.
- **Select expected-shortfall backtest.** Consider VaR/ES forecasts, tail observations, assumed distribution or simulation capability, and test objective. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select expected-shortfall backtest.
- **Diagnose backtest failure.** Consider exception count, clustering, tail severity, volatility regime, P&L unexplained components, risk-factor gaps, and model changes. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to diagnose backtest failure.
- **Determine backtesting disposition.** Consider P&L integrity, test results, power, policy zones, ES evidence, root cause, materiality, and prior failures. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine backtesting disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **VARBACK technical fitness.** Assess: define VaR exceptions, select VaR test family, assess sample size and test power, apply traffic-light or institutional policy. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **VARBACK use and release boundary.** Assess: reconcile forecasts with realised P&L, determine backtesting disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Forecast-to-P&L reconciliation.
- VaR exception and independence tests.
- ES severity tests.
- Diagnosis, limitations, and remediation disposition.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide align — Reconcile forecasts with realised P&L
- Decide exceptions — Define VaR exceptions
- Decide tests — Select VaR test family
- Decide sample — Assess sample size and test power
- Decide traffic — Apply traffic-light or institutional policy
- Decide ES — Select expected-shortfall backtest
- Decide diagnose — Diagnose backtest failure
- Decide disposition — Determine backtesting disposition
- Package varback evidence — Package the VARBACK professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute varback analysis
- Compute varback validation evidence

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
