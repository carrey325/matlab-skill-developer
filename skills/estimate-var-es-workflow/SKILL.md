---
name: estimate-var-es-workflow
description: Estimate VaR and expected shortfall by defining the risk use and P&L, selecting horizon and confidence, choosing historical, parametric, or simulation methods, treating nonlinear and tail risks, aggregating exposures, diagnosing estimates, and setting use limitations. Use when a market-risk owner requires VaR and/or ES estimates for a defined portfolio, horizon, confidence level, and use. Not for credit ECL, credit parameter development, or independent backtesting.
---

# Purpose

Estimate VaR and expected shortfall by defining the risk use and P&L, selecting horizon and confidence, choosing historical, parametric, or simulation methods, treating nonlinear and tail risks, aggregating exposures, diagnosing estimates, and setting use limitations.

# Scope and Applicability

Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.

A market-risk owner requires VaR and/or ES estimates for a defined portfolio, horizon, confidence level, and use.

Do not use for credit ECL, PD/LGD development, independent backtesting, trading recommendations, or limit approval.

## Exclusions

- credit ECL
- credit parameter development
- independent backtesting
- trading recommendations
- limit approval

# Required Inputs

- Market-risk purpose, portfolio, horizon, and confidence policy.
- Positions, risk factors, valuation functions, and P&L definition.
- Method, distribution, simulation, and aggregation assumptions.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Market-risk purpose, portfolio, horizon, and confidence policy, positions, risk factors, valuation functions, and P&L definition, method, distribution, simulation, and aggregation assumptions.
- Outputs: Risk-measure and P&L contract, VaR and ES estimates, method, tail, aggregation, and sensitivity diagnostics, limitations and backtesting handoff.

## Determine VaR and ES use

- Inputs: Internal risk, limit monitoring, disclosure, or applicable capital purpose and governing policy.
- Outputs: Decision record for determine VaR and ES use.

## Define portfolio and P&L measure

- Inputs: Position snapshot, valuation basis, actual/hypothetical P&L, fees, intraday changes, and risk-factor mapping.
- Outputs: Decision record for define portfolio and P&L measure.

## Set horizon and confidence level

- Inputs: Risk use, liquidity, holding period, confidence/tail probability, scaling assumptions, and data frequency.
- Outputs: Decision record for set horizon and confidence level.

## Select VaR and ES estimation method

- Inputs: History length, volatility dynamics, tails, nonlinear positions, scenario capability, and computational budget.
- Outputs: Decision record for select VaR and ES estimation method.

## Treat nonlinear positions and risk factors

- Inputs: Options, convexity, path dependence, discontinuities, basis risks, and approximation error.
- Outputs: Decision record for treat nonlinear positions and risk factors.

## Select tail and volatility treatment

- Inputs: Tail thickness, volatility clustering, procyclicality, regime shifts, and sample support.
- Outputs: Decision record for select tail and volatility treatment.

## Aggregate risk across positions and horizons

- Inputs: Joint scenarios, correlations, liquidity horizons, diversification, missing factors, and netting rules.
- Outputs: Decision record for aggregate risk across positions and horizons.

## Judge estimate stability and plausibility

- Inputs: Monte Carlo error, sample sensitivity, distribution fit, decomposition, stress comparison, and day-to-day changes.
- Outputs: Decision record for judge estimate stability and plausibility.

## Determine VaR and ES estimation disposition

- Inputs: P&L integrity, method support, nonlinear coverage, tails, aggregation, diagnostics, and intended use.
- Outputs: Decision record for determine VaR and ES estimation disposition.

## Execute the approved VaR/ES computation

- Work: Run the approved computational specification without changing professional choices.

## Assess VaR/ES technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the VaR/ES professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Determine VaR and ES use.** Consider internal risk, limit monitoring, disclosure, or applicable capital purpose and governing policy. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine VaR and ES use.
- **Define portfolio and P&L measure.** Consider position snapshot, valuation basis, actual/hypothetical P&L, fees, intraday changes, and risk-factor mapping. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define portfolio and P&L measure.
- **Set horizon and confidence level.** Consider risk use, liquidity, holding period, confidence/tail probability, scaling assumptions, and data frequency. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set horizon and confidence level.
- **Select VaR and ES estimation method.** Consider history length, volatility dynamics, tails, nonlinear positions, scenario capability, and computational budget. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select VaR and ES estimation method.
- **Treat nonlinear positions and risk factors.** Consider options, convexity, path dependence, discontinuities, basis risks, and approximation error. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to treat nonlinear positions and risk factors.
- **Select tail and volatility treatment.** Consider tail thickness, volatility clustering, procyclicality, regime shifts, and sample support. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select tail and volatility treatment.
- **Aggregate risk across positions and horizons.** Consider joint scenarios, correlations, liquidity horizons, diversification, missing factors, and netting rules. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to aggregate risk across positions and horizons.
- **Judge estimate stability and plausibility.** Consider Monte Carlo error, sample sensitivity, distribution fit, decomposition, stress comparison, and day-to-day changes. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to judge estimate stability and plausibility.
- **Determine VaR and ES estimation disposition.** Consider P&L integrity, method support, nonlinear coverage, tails, aggregation, diagnostics, and intended use. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine VaR and ES estimation disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **VaR/ES technical fitness.** Assess: define portfolio and P&L measure, set horizon and confidence level, select VaR and ES estimation method, treat nonlinear positions and risk factors. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **VaR/ES use and release boundary.** Assess: determine VaR and ES use, determine VaR and ES estimation disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Risk-measure and P&L contract.
- VaR and ES estimates.
- Method, tail, aggregation, and sensitivity diagnostics.
- Limitations and backtesting handoff.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide purpose — Determine VaR and ES use
- Decide pnl — Define portfolio and P&L measure
- Decide horizon — Set horizon and confidence level
- Decide method — Select VaR and ES estimation method
- Decide nonlinear — Treat nonlinear positions and risk factors
- Decide tail — Select tail and volatility treatment
- Decide aggregate — Aggregate risk across positions and horizons
- Decide diagnostic — Judge estimate stability and plausibility
- Decide disposition — Determine VaR and ES estimation disposition
- Package VaR/ES evidence (capability: package vares evidence) — Package the VaR/ES professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute VaR/ES analysis (capability: compute vares analysis)
- Compute VaR/ES validation evidence (capability: compute vares validation evidence)

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
