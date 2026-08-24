---
name: estimate-lifetime-ecl-workflow
description: Estimate expected credit loss by selecting the governing regime, loss horizon, staging or scope treatment, governed PD/LGD/EAD inputs, scenarios, discounting, overlays, aggregation, reconciliation, and disposition. Use when an accountable reporting or risk owner requires an expected-credit-loss estimate from approved exposure and credit-parameter inputs. Not for PD, LGD, or EAD development, accounting policy approval, or credit approval.
---

# Purpose

Estimate expected credit loss by selecting the governing regime, loss horizon, staging or scope treatment, governed PD/LGD/EAD inputs, scenarios, discounting, overlays, aggregation, reconciliation, and disposition.

# Scope and Applicability

IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches.

An accountable reporting or risk owner requires an expected-credit-loss estimate from approved exposure and credit-parameter inputs.

Do not use to develop PD, LGD, or EAD models, approve accounting policy, perform credit approval, or claim independent validation.

## Exclusions

- PD, LGD, or EAD development
- accounting policy approval
- credit approval
- production ledger posting
- independent validation

# Required Inputs

- Governing accounting or internal-loss purpose.
- Exposure population and contractual cash flows.
- Approved PD, LGD, EAD, scenarios, discount rates, and policy inputs.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Governing accounting or internal-loss purpose, exposure population and contractual cash flows, approved PD, LGD, EAD, scenarios, discount rates, and policy inputs.
- Outputs: Regime and scope record, period loss projections and scenario-weighted ECL, overlay and reconciliation evidence, limitations, reporting package, and validation handoff.

## Select governing loss regime

- Inputs: Applicable accounting framework, reporting entity, portfolio, and internal-use mandate.
- Outputs: Decision record for select governing loss regime.

## Determine instrument scope and loss horizon

- Inputs: Measurement category, maturity, revolving features, off-balance-sheet commitment, cancellation rights, and internal risk horizon.
- Outputs: Decision record for determine instrument scope and loss horizon.

## Determine IFRS 9 staging and SICR route

- Inputs: Governing regime, origination risk, reporting-date risk, delinquency, qualitative indicators, default status, and policy rebuttals.
- Outputs: Decision record for determine IFRS 9 staging and SICR route.

## Assess PD, LGD, and EAD input suitability

- Inputs: Purpose, horizon, conditionality, scenario sensitivity, calibration date, portfolio match, and validation status.
- Outputs: Decision record for assess PD, LGD, and EAD input suitability.

## Select forward-looking scenarios and weights

- Inputs: Reasonable and supportable forecasts, scenario distinctness, horizon, probability basis, nonlinearity, and approval.
- Outputs: Decision record for select forward-looking scenarios and weights.

## Select cash-shortfall and discounting basis

- Inputs: Expected contractual cash flows, timing, effective interest rate, recoveries, and modifications.
- Outputs: Decision record for select cash-shortfall and discounting basis.

## Determine qualitative adjustment or overlay

- Inputs: Known model limitations, post-model events, data gaps, double-counting assessment, governance, and reversibility.
- Outputs: Decision record for determine qualitative adjustment or overlay.

## Aggregate and reconcile ECL

- Inputs: Exposure-level components, stage/scope totals, scenario contributions, ledger population, prior period, and movement attribution.
- Outputs: Decision record for aggregate and reconcile ECL.

## Determine ECL estimate disposition

- Inputs: Regime compliance, parameter fitness, scenario governance, overlays, reconciliation, uncertainty, and control findings.
- Outputs: Decision record for determine ECL estimate disposition.

## Execute the approved ECL computation

- Work: Run the approved computational specification without changing professional choices.

## Assess ECL technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the ECL professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Select governing loss regime.** Consider applicable accounting framework, reporting entity, portfolio, and internal-use mandate. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select governing loss regime.
- **Determine instrument scope and loss horizon.** Consider measurement category, maturity, revolving features, off-balance-sheet commitment, cancellation rights, and internal risk horizon. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine instrument scope and loss horizon.
- **Determine IFRS 9 staging and SICR route.** Consider governing regime, origination risk, reporting-date risk, delinquency, qualitative indicators, default status, and policy rebuttals. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine IFRS 9 staging and SICR route.
- **Assess PD, LGD, and EAD input suitability.** Consider purpose, horizon, conditionality, scenario sensitivity, calibration date, portfolio match, and validation status. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess PD, LGD, and EAD input suitability.
- **Select forward-looking scenarios and weights.** Consider reasonable and supportable forecasts, scenario distinctness, horizon, probability basis, nonlinearity, and approval. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select forward-looking scenarios and weights.
- **Select cash-shortfall and discounting basis.** Consider expected contractual cash flows, timing, effective interest rate, recoveries, and modifications. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select cash-shortfall and discounting basis.
- **Determine qualitative adjustment or overlay.** Consider known model limitations, post-model events, data gaps, double-counting assessment, governance, and reversibility. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine qualitative adjustment or overlay.
- **Aggregate and reconcile ECL.** Consider exposure-level components, stage/scope totals, scenario contributions, ledger population, prior period, and movement attribution. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to aggregate and reconcile ECL.
- **Determine ECL estimate disposition.** Consider regime compliance, parameter fitness, scenario governance, overlays, reconciliation, uncertainty, and control findings. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine ECL estimate disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **ECL technical fitness.** Assess: determine instrument scope and loss horizon, determine IFRS 9 staging and SICR route, assess PD, LGD, and EAD input suitability, select forward-looking scenarios and weights. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **ECL use and release boundary.** Assess: select governing loss regime, determine ECL estimate disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Regime and scope record.
- Period loss projections and scenario-weighted ECL.
- Overlay and reconciliation evidence.
- Limitations, reporting package, and validation handoff.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide regime — Select governing loss regime
- Decide scope — Determine instrument scope and loss horizon
- Decide stage — Determine IFRS 9 staging and SICR route
- Decide parameters — Assess PD, LGD, and EAD input suitability
- Decide scenario — Select forward-looking scenarios and weights
- Decide discount — Select cash-shortfall and discounting basis
- Decide overlay — Determine qualitative adjustment or overlay
- Decide aggregate — Aggregate and reconcile ECL
- Decide disposition — Determine ECL estimate disposition
- Package ECL evidence — Package the ECL professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute ECL analysis
- Compute ECL validation evidence

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
