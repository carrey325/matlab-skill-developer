---
name: build-credit-curves-workflow
description: Build and validate a market-implied default or hazard curve by selecting instruments, conventions, recovery and discount inputs, calibration, interpolation, extrapolation, consistency checks, and use limitations. Use when a valuation or risk owner requires a calibrated credit curve from bonds, CDS, or other approved market instruments. Not for physical PD development, trading or hedging, or full CDS valuation.
---

# Purpose

Build and validate a market-implied default or hazard curve by selecting instruments, conventions, recovery and discount inputs, calibration, interpolation, extrapolation, consistency checks, and use limitations.

# Scope and Applicability

Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.

A valuation or risk owner requires a calibrated credit curve from bonds, CDS, or other approved market instruments.

Do not use for physical PD development, trading decisions, CDS contract valuation beyond the curve handoff, or rating-transition estimation.

## Exclusions

- physical PD development
- trading or hedging
- full CDS valuation
- rating transition estimation
- market data acquisition automation

# Required Inputs

- Curve purpose and valuation date.
- Approved instruments, quotes, cash flows, and conventions.
- Discount curve, recovery assumption, and extrapolation policy.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Curve purpose and valuation date, approved instruments, quotes, cash flows, and conventions, discount curve, recovery assumption, and extrapolation policy.
- Outputs: Instrument and convention set, calibrated hazard/default/survival curve, fit and consistency diagnostics, interpolation, extrapolation, and use limitations.

## Determine curve purpose and probability interpretation

- Inputs: Valuation, relative value, stress, accounting, or internal risk use and risk-neutral versus physical interpretation.
- Outputs: Decision record for determine curve purpose and probability interpretation.

## Select calibration instruments and quotes

- Inputs: Liquidity, seniority, currency, restructuring clause, maturity, collateral, accrued interest, and quote quality.
- Outputs: Decision record for select calibration instruments and quotes.

## Freeze contract and market conventions

- Inputs: Day count, payment frequency, accrual on default, settlement, currency, restructuring, and business-day rules.
- Outputs: Decision record for freeze contract and market conventions.

## Set recovery assumption or recovery calibration

- Inputs: Instrument seniority, recovery convention, observed recoveries, identifiability, and sensitivity.
- Outputs: Decision record for set recovery assumption or recovery calibration.

## Select discount curve and currency treatment

- Inputs: Collateral or funding convention, currency, valuation date, interpolation, and instrument cash flows.
- Outputs: Decision record for select discount curve and currency treatment.

## Choose calibration objective and constraints

- Inputs: Quote measure, weighting, positivity, monotonic survival, parameterization, and solver stability.
- Outputs: Decision record for choose calibration objective and constraints.

## Select interpolation and extrapolation policy

- Inputs: Observed maturities, curve smoothness, intended valuation tenors, tail support, and policy limits.
- Outputs: Decision record for select interpolation and extrapolation policy.

## Validate repricing and curve consistency

- Inputs: Instrument repricing errors, survival monotonicity, hazard signs, spread ordering, sensitivity, and stale quotes.
- Outputs: Decision record for validate repricing and curve consistency.

## Determine credit-curve disposition

- Inputs: Quote quality, conventions, assumptions, fit, shape, sensitivity, extrapolation, and intended use.
- Outputs: Decision record for determine credit-curve disposition.

## Execute the approved CURVES computation

- Work: Run the approved computational specification without changing professional choices.

## Assess CURVES technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the CURVES professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Determine curve purpose and probability interpretation.** Consider valuation, relative value, stress, accounting, or internal risk use and risk-neutral versus physical interpretation. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine curve purpose and probability interpretation.
- **Select calibration instruments and quotes.** Consider liquidity, seniority, currency, restructuring clause, maturity, collateral, accrued interest, and quote quality. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select calibration instruments and quotes.
- **Freeze contract and market conventions.** Consider day count, payment frequency, accrual on default, settlement, currency, restructuring, and business-day rules. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to freeze contract and market conventions.
- **Set recovery assumption or recovery calibration.** Consider instrument seniority, recovery convention, observed recoveries, identifiability, and sensitivity. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set recovery assumption or recovery calibration.
- **Select discount curve and currency treatment.** Consider collateral or funding convention, currency, valuation date, interpolation, and instrument cash flows. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select discount curve and currency treatment.
- **Choose calibration objective and constraints.** Consider quote measure, weighting, positivity, monotonic survival, parameterization, and solver stability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to choose calibration objective and constraints.
- **Select interpolation and extrapolation policy.** Consider observed maturities, curve smoothness, intended valuation tenors, tail support, and policy limits. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select interpolation and extrapolation policy.
- **Validate repricing and curve consistency.** Consider instrument repricing errors, survival monotonicity, hazard signs, spread ordering, sensitivity, and stale quotes. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to validate repricing and curve consistency.
- **Determine credit-curve disposition.** Consider quote quality, conventions, assumptions, fit, shape, sensitivity, extrapolation, and intended use. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine credit-curve disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **CURVES technical fitness.** Assess: select calibration instruments and quotes, freeze contract and market conventions, set recovery assumption or recovery calibration, select discount curve and currency treatment. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **CURVES use and release boundary.** Assess: determine curve purpose and probability interpretation, determine credit-curve disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Instrument and convention set.
- Calibrated hazard/default/survival curve.
- Fit and consistency diagnostics.
- Interpolation, extrapolation, and use limitations.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide purpose — Determine curve purpose and probability interpretation
- Decide instrument — Select calibration instruments and quotes
- Decide convention — Freeze contract and market conventions
- Decide recovery — Set recovery assumption or recovery calibration
- Decide discount — Select discount curve and currency treatment
- Decide calibrate — Choose calibration objective and constraints
- Decide interpolate — Select interpolation and extrapolation policy
- Decide consistency — Validate repricing and curve consistency
- Decide disposition — Determine credit-curve disposition
- Package curves evidence — Package the CURVES professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute curves analysis
- Compute curves validation evidence

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
