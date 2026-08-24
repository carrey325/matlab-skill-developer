---
name: estimate-structural-default-risk-workflow
description: Estimate structural default risk by defining the liability boundary and horizon, selecting point-in-time or time-series calibration, solving asset value and volatility, validating market inputs, and reporting sensitivities and limitations. Use when a risk analyst requires market-based distance-to-default or default-probability evidence for a corporate issuer. Not for behavioural PD development, CDS trading, or credit approval.
---

# Purpose

Estimate structural default risk by defining the liability boundary and horizon, selecting point-in-time or time-series calibration, solving asset value and volatility, validating market inputs, and reporting sensitivities and limitations.

# Scope and Applicability

Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.

A risk analyst requires market-based distance-to-default or default-probability evidence for a corporate issuer.

Do not use for ordinary behavioural PD development, CDS trading, credit approval, or unsupported firms without market and liability information.

## Exclusions

- behavioural PD development
- CDS trading
- credit approval
- private firms without supportable inputs
- independent approval

# Required Inputs

- Issuer equity and liability data.
- Equity volatility, risk-free curve, and horizon.
- Capital-structure mapping and calibration constraints.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Issuer equity and liability data, equity volatility, risk-free curve, and horizon, capital-structure mapping and calibration constraints.
- Outputs: Structural model contract, asset value and asset-volatility calibration, distance-to-default and default-risk estimates, sensitivity, validation, and limitations report.

## Define default boundary and liability mapping

- Inputs: Short- and long-term liabilities, seniority, maturity, off-balance-sheet obligations, and model boundary.
- Outputs: Decision record for define default boundary and liability mapping.

## Set structural risk horizon

- Inputs: Use horizon, liability maturity, market-data frequency, and interpretation of default probability.
- Outputs: Decision record for set structural risk horizon.

## Select equity-volatility input

- Inputs: Observation window, frequency, corporate events, option-implied data, regime change, and annualisation.
- Outputs: Decision record for select equity-volatility input.

## Calibrate asset value and asset volatility

- Inputs: Equation residuals, initial values, convergence, bounds, observation frequency, and parameter stability.
- Outputs: Decision record for calibrate asset value and asset volatility.

## Assess market and capital-structure representativeness

- Inputs: Liquidity, stale prices, structural breaks, equity dilution, debt updates, and issuer actions.
- Outputs: Decision record for assess market and capital-structure representativeness.

## Assess structural-model sensitivity

- Inputs: Debt boundary, equity volatility, risk-free rate, horizon, payout, and model-form alternatives.
- Outputs: Decision record for assess structural-model sensitivity.

## Determine structural-risk disposition

- Inputs: Input quality, calibration stability, benchmark comparison, sensitivity, and intended use.
- Outputs: Decision record for determine structural-risk disposition.

## Execute the approved structural-default computation

- Work: Run the approved computational specification without changing professional choices.

## Assess structural-default technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the structural-default professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Define default boundary and liability mapping.** Consider short- and long-term liabilities, seniority, maturity, off-balance-sheet obligations, and model boundary. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define default boundary and liability mapping.
- **Set structural risk horizon.** Consider use horizon, liability maturity, market-data frequency, and interpretation of default probability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set structural risk horizon.
- **Select equity-volatility input.** Consider observation window, frequency, corporate events, option-implied data, regime change, and annualisation. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select equity-volatility input.
- **Calibrate asset value and asset volatility.** Consider equation residuals, initial values, convergence, bounds, observation frequency, and parameter stability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to calibrate asset value and asset volatility.
- **Assess market and capital-structure representativeness.** Consider liquidity, stale prices, structural breaks, equity dilution, debt updates, and issuer actions. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess market and capital-structure representativeness.
- **Assess structural-model sensitivity.** Consider debt boundary, equity volatility, risk-free rate, horizon, payout, and model-form alternatives. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess structural-model sensitivity.
- **Determine structural-risk disposition.** Consider input quality, calibration stability, benchmark comparison, sensitivity, and intended use. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine structural-risk disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **structural-default technical fitness.** Assess: set structural risk horizon, select equity-volatility input, calibrate asset value and asset volatility, assess market and capital-structure representativeness. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **structural-default use and release boundary.** Assess: define default boundary and liability mapping, determine structural-risk disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Structural model contract.
- Asset value and asset-volatility calibration.
- Distance-to-default and default-risk estimates.
- Sensitivity, validation, and limitations report.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide boundary — Define default boundary and liability mapping
- Decide horizon — Set structural risk horizon
- Decide volatility — Select equity-volatility input
- Decide calibrate — Calibrate asset value and asset volatility
- Decide market — Assess market and capital-structure representativeness
- Decide sensitivity — Assess structural-model sensitivity
- Decide disposition — Determine structural-risk disposition
- Package structural evidence — Package the structural-default professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute structural analysis
- Compute structural validation evidence

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
