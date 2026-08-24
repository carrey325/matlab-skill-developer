---
name: analyze-credit-default-swap-risk-workflow
description: Analyze CDS valuation and market-implied credit risk by fixing task boundaries, contract conventions, discount and credit curves, recovery, calibration, sensitivities, reconciliation, and reporting limitations without making trading or hedging decisions. Use when a valuation or risk analyst needs a CDS price, spread, or market-implied credit-risk assessment from an identified contract and market snapshot. Not for trading recommendations, hedging decisions, or trade execution.
---

# Purpose

Analyze CDS valuation and market-implied credit risk by fixing task boundaries, contract conventions, discount and credit curves, recovery, calibration, sensitivities, reconciliation, and reporting limitations without making trading or hedging decisions.

# Scope and Applicability

Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.

A valuation or risk analyst needs a CDS price, spread, or market-implied credit-risk assessment from an identified contract and market snapshot.

Do not use to recommend trades or hedges, execute transactions, resolve legal disputes, or substitute for physical PD development.

## Exclusions

- trading recommendations
- hedging decisions
- trade execution
- legal interpretation
- physical PD development

# Required Inputs

- CDS contract and valuation purpose.
- Market quote, discount curve, and credit curve.
- Recovery, settlement, and sensitivity assumptions.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: CDS contract and valuation purpose, market quote, discount curve, and credit curve, recovery, settlement, and sensitivity assumptions.
- Outputs: Contract and convention record, CDS value, par spread, or implied-risk result, curve and recovery sensitivities, reconciliation and limitations report.

## Set CDS analysis purpose and prohibited actions

- Inputs: Valuation, par-spread, sensitivity, accounting input, or market-implied risk purpose and responsible owner.
- Outputs: Decision record for set CDS analysis purpose and prohibited actions.

## Identify contract and credit-event conventions

- Inputs: Reference entity, obligation, seniority, currency, maturity, coupon, restructuring, credit events, and settlement.
- Outputs: Decision record for identify contract and credit-event conventions.

## Select discount and credit curves

- Inputs: Valuation date, currency, collateral basis, instrument set, quote freshness, calibration diagnostics, and tenor support.
- Outputs: Decision record for select discount and credit curves.

## Set recovery and settlement assumptions

- Inputs: Fixed or market recovery, auction/physical/cash settlement, seniority, and identifiability.
- Outputs: Decision record for set recovery and settlement assumptions.

## Determine price spread or implied-risk route

- Inputs: Observed upfront price, running spread, standard coupon, accrued premium, and requested output.
- Outputs: Decision record for determine price spread or implied-risk route.

## Select CDS risk sensitivities

- Inputs: Spread/hazard, recovery, interest rates, maturity, curve shape, and jump-to-default relevance.
- Outputs: Decision record for select CDS risk sensitivities.

## Reconcile valuation to market quote

- Inputs: Clean/dirty price, accrued premium, coupon, upfront amount, settlement date, curves, and tolerance policy.
- Outputs: Decision record for reconcile valuation to market quote.

## Determine CDS analysis disposition

- Inputs: Contract certainty, curve quality, recovery sensitivity, reconciliation, model limits, and intended use.
- Outputs: Decision record for determine CDS analysis disposition.

## Execute the approved CDS computation

- Work: Run the approved computational specification without changing professional choices.

## Assess CDS technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the CDS professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Set CDS analysis purpose and prohibited actions.** Consider valuation, par-spread, sensitivity, accounting input, or market-implied risk purpose and responsible owner. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set CDS analysis purpose and prohibited actions.
- **Identify contract and credit-event conventions.** Consider reference entity, obligation, seniority, currency, maturity, coupon, restructuring, credit events, and settlement. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to identify contract and credit-event conventions.
- **Select discount and credit curves.** Consider valuation date, currency, collateral basis, instrument set, quote freshness, calibration diagnostics, and tenor support. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select discount and credit curves.
- **Set recovery and settlement assumptions.** Consider fixed or market recovery, auction/physical/cash settlement, seniority, and identifiability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set recovery and settlement assumptions.
- **Determine price spread or implied-risk route.** Consider observed upfront price, running spread, standard coupon, accrued premium, and requested output. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine price spread or implied-risk route.
- **Select CDS risk sensitivities.** Consider spread/hazard, recovery, interest rates, maturity, curve shape, and jump-to-default relevance. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select CDS risk sensitivities.
- **Reconcile valuation to market quote.** Consider clean/dirty price, accrued premium, coupon, upfront amount, settlement date, curves, and tolerance policy. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to reconcile valuation to market quote.
- **Determine CDS analysis disposition.** Consider contract certainty, curve quality, recovery sensitivity, reconciliation, model limits, and intended use. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine CDS analysis disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **CDS technical fitness.** Assess: identify contract and credit-event conventions, select discount and credit curves, set recovery and settlement assumptions, determine price spread or implied-risk route. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **CDS use and release boundary.** Assess: set CDS analysis purpose and prohibited actions, determine CDS analysis disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Contract and convention record.
- CDS value, par spread, or implied-risk result.
- Curve and recovery sensitivities.
- Reconciliation and limitations report.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide purpose — Set CDS analysis purpose and prohibited actions
- Decide contract — Identify contract and credit-event conventions
- Decide curves — Select discount and credit curves
- Decide recovery — Set recovery and settlement assumptions
- Decide calibrate — Determine price spread or implied-risk route
- Decide sensitivity — Select CDS risk sensitivities
- Decide reconcile — Reconcile valuation to market quote
- Decide disposition — Determine CDS analysis disposition
- Package CDS evidence — Package the CDS professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute CDS analysis
- Compute CDS validation evidence

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
