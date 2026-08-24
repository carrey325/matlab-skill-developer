---
name: assess-credit-portfolio-risk-workflow
description: Assess portfolio credit loss, tail risk, concentration, risk contributions, and economic capital through explicit loss-mode, horizon, dependence, input, simulation, attribution, and reporting decisions. Use when a portfolio risk owner needs loss distribution, concentration, contribution, or economic-capital evidence from governed credit inputs. Not for parameter model development, macro stress testing, or regulatory capital determination.
---

# Purpose

Assess portfolio credit loss, tail risk, concentration, risk contributions, and economic capital through explicit loss-mode, horizon, dependence, input, simulation, attribution, and reporting decisions.

# Scope and Applicability

Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.

A portfolio risk owner needs loss distribution, concentration, contribution, or economic-capital evidence from governed credit inputs.

Do not use to develop PD/LGD/EAD, run macro stress scenarios, set regulatory capital, execute trades, or approve limits.

## Exclusions

- parameter model development
- macro stress testing
- regulatory capital determination
- trading or hedging
- limit approval

# Required Inputs

- Portfolio positions and governed PD/LGD/EAD or transition inputs.
- Risk purpose, horizon, confidence, and capital policy.
- Dependence, concentration, simulation, and valuation assumptions.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Portfolio positions and governed PD/LGD/EAD or transition inputs, risk purpose, horizon, confidence, and capital policy, dependence, concentration, simulation, and valuation assumptions.
- Outputs: Portfolio loss-mode and parameter contract, loss distribution and convergence evidence, concentration and risk contributions, EL, UL, tail risk, and economic-capital report with limitations.

## Select default-mode or migration-mode loss

- Inputs: Whether only default loss or all credit-quality changes and mark-to-market effects are decision-relevant.
- Outputs: Decision record for select default-mode or migration-mode loss.

## Set horizon and tail probability

- Inputs: Decision use, liquidity, capital planning period, holding horizon, and institution-approved confidence level.
- Outputs: Decision record for set horizon and tail probability.

## Assess portfolio parameter compatibility

- Inputs: PD horizon, LGD basis, EAD timing, transition states, valuation basis, and exposure snapshot.
- Outputs: Decision record for assess portfolio parameter compatibility.

## Select dependence structure

- Inputs: Systematic factors, sector and geography links, tail dependence, contagion, calibration sample, and parsimony.
- Outputs: Decision record for select dependence structure.

## Assess name and sector concentration

- Inputs: Large obligors, connected counterparties, sectors, regions, factor loadings, and diversification assumptions.
- Outputs: Decision record for assess name and sector concentration.

## Judge simulation precision and tail stability

- Inputs: Scenario count, seed control, tail standard error, confidence bands, rare defaults, and repeatability.
- Outputs: Decision record for judge simulation precision and tail stability.

## Determine EL UL and economic-capital output

- Inputs: Loss distribution, expected loss treatment, confidence measure, diversification, capital definition, and policy owner.
- Outputs: Decision record for determine EL UL and economic-capital output.

## Select risk contribution and diversification attribution

- Inputs: Portfolio measure, marginal or component allocation, additivity, concentration, and decision use.
- Outputs: Decision record for select risk contribution and diversification attribution.

## Determine portfolio-risk reportability

- Inputs: Input suitability, dependence validation, concentration, convergence, sensitivity, attribution, and policy alignment.
- Outputs: Decision record for determine portfolio-risk reportability.

## Execute the approved portfolio-risk computation

- Work: Run the approved computational specification without changing professional choices.

## Assess portfolio-risk technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the portfolio-risk professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Select default-mode or migration-mode loss.** Consider whether only default loss or all credit-quality changes and mark-to-market effects are decision-relevant. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select default-mode or migration-mode loss.
- **Set horizon and tail probability.** Consider decision use, liquidity, capital planning period, holding horizon, and institution-approved confidence level. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set horizon and tail probability.
- **Assess portfolio parameter compatibility.** Consider PD horizon, LGD basis, EAD timing, transition states, valuation basis, and exposure snapshot. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess portfolio parameter compatibility.
- **Select dependence structure.** Consider systematic factors, sector and geography links, tail dependence, contagion, calibration sample, and parsimony. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select dependence structure.
- **Assess name and sector concentration.** Consider large obligors, connected counterparties, sectors, regions, factor loadings, and diversification assumptions. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to assess name and sector concentration.
- **Judge simulation precision and tail stability.** Consider scenario count, seed control, tail standard error, confidence bands, rare defaults, and repeatability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to judge simulation precision and tail stability.
- **Determine EL UL and economic-capital output.** Consider loss distribution, expected loss treatment, confidence measure, diversification, capital definition, and policy owner. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine el ul and economic-capital output.
- **Select risk contribution and diversification attribution.** Consider portfolio measure, marginal or component allocation, additivity, concentration, and decision use. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select risk contribution and diversification attribution.
- **Determine portfolio-risk reportability.** Consider input suitability, dependence validation, concentration, convergence, sensitivity, attribution, and policy alignment. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine portfolio-risk reportability.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **portfolio-risk technical fitness.** Assess: set horizon and tail probability, assess portfolio parameter compatibility, select dependence structure, assess name and sector concentration. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **portfolio-risk use and release boundary.** Assess: select default-mode or migration-mode loss, determine portfolio-risk reportability, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Portfolio loss-mode and parameter contract.
- Loss distribution and convergence evidence.
- Concentration and risk contributions.
- EL, UL, tail risk, and economic-capital report with limitations.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide mode — Select default-mode or migration-mode loss
- Decide horizon — Set horizon and tail probability
- Decide inputs — Assess portfolio parameter compatibility
- Decide dependence — Select dependence structure
- Decide concentration — Assess name and sector concentration
- Decide convergence — Judge simulation precision and tail stability
- Decide capital — Determine EL UL and economic-capital output
- Decide attribution — Select risk contribution and diversification attribution
- Decide disposition — Determine portfolio-risk reportability
- Package portfolio evidence — Package the portfolio-risk professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute portfolio analysis
- Compute portfolio validation evidence

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
