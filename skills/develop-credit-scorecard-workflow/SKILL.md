---
name: develop-credit-scorecard-workflow
description: Develop an interpretable credit scorecard with explicit target-population, reject-inference, binning, monotonicity, selection, scaling, cutoff-boundary, validation, and use decisions. Use when a model owner needs an interpretable points-based credit-risk ranking model for a defined population and decision-support use. Not for lifetime PD term structures, credit approval execution, or production decision engines.
---

# Purpose

Develop an interpretable credit scorecard with explicit target-population, reject-inference, binning, monotonicity, selection, scaling, cutoff-boundary, validation, and use decisions.

# Scope and Applicability

Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.

A model owner needs an interpretable points-based credit-risk ranking model for a defined population and decision-support use.

Do not use for lifetime PD term structures, unrestricted nonlinear default models, credit approval execution, or independent approval.

## Exclusions

- lifetime PD term structures
- credit approval execution
- production decision engines
- independent model approval

# Required Inputs

- Scorecard purpose and accountable population.
- Application or behavioural performance data.
- Accept/reject process and interpretability constraints.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Scorecard purpose and accountable population, application or behavioural performance data, accept/reject process and interpretability constraints.
- Outputs: Population and target contract, binning and variable-selection record, scaled scorecard specification, developer validation and cutoff-governance handoff.

## Determine scorecard purpose and responsibility boundary

- Inputs: Application, behavioural, collection, or other use plus accountable decision owner.
- Outputs: Decision record for determine scorecard purpose and responsibility boundary.

## Define target and development population

- Inputs: Default/bad definition, observation window, performance window, exclusions, and sampling frame.
- Outputs: Decision record for define target and development population.

## Determine reject-inference treatment

- Inputs: Coverage of declined applicants, historical policy, selection drivers, and unverifiable outcomes.
- Outputs: Decision record for determine reject-inference treatment.

## Select supervised binning treatment

- Inputs: Missingness, sparsity, ordering, business meaning, and bad-rate pattern for each predictor.
- Outputs: Decision record for select supervised binning treatment.

## Determine monotonicity constraints

- Inputs: Economic rationale, observed bad rates, sampling uncertainty, and temporal stability.
- Outputs: Decision record for determine monotonicity constraints.

## Select scorecard variables

- Inputs: Predictive contribution, multicollinearity, stability, missingness, availability, interpretability, and governance restrictions.
- Outputs: Decision record for select scorecard variables.

## Set points scaling and reason-code interpretation

- Inputs: Base score, odds convention, points-to-double-odds, score direction, rounding, and explanation needs.
- Outputs: Decision record for set points scaling and reason-code interpretation.

## Define cutoff and decision-policy handoff

- Inputs: Whether an accountable policy owner has supplied costs, risk appetite, legal constraints, and override rules.
- Outputs: Decision record for define cutoff and decision-policy handoff.

## Determine scorecard disposition

- Inputs: Discrimination, calibration, bin stability, population stability, implementation verification, and limitations.
- Outputs: Decision record for determine scorecard disposition.

## Execute the approved scorecard computation

- Work: Run the approved computational specification without changing professional choices.

## Assess scorecard technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the scorecard professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Determine scorecard purpose and responsibility boundary.** Consider application, behavioural, collection, or other use plus accountable decision owner. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine scorecard purpose and responsibility boundary.
- **Define target and development population.** Consider default/bad definition, observation window, performance window, exclusions, and sampling frame. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define target and development population.
- **Determine reject-inference treatment.** Consider coverage of declined applicants, historical policy, selection drivers, and unverifiable outcomes. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine reject-inference treatment.
- **Select supervised binning treatment.** Consider missingness, sparsity, ordering, business meaning, and bad-rate pattern for each predictor. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select supervised binning treatment.
- **Determine monotonicity constraints.** Consider economic rationale, observed bad rates, sampling uncertainty, and temporal stability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine monotonicity constraints.
- **Select scorecard variables.** Consider predictive contribution, multicollinearity, stability, missingness, availability, interpretability, and governance restrictions. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select scorecard variables.
- **Set points scaling and reason-code interpretation.** Consider base score, odds convention, points-to-double-odds, score direction, rounding, and explanation needs. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set points scaling and reason-code interpretation.
- **Define cutoff and decision-policy handoff.** Consider whether an accountable policy owner has supplied costs, risk appetite, legal constraints, and override rules. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define cutoff and decision-policy handoff.
- **Determine scorecard disposition.** Consider discrimination, calibration, bin stability, population stability, implementation verification, and limitations. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine scorecard disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **scorecard technical fitness.** Assess: define target and development population, determine reject-inference treatment, select supervised binning treatment, determine monotonicity constraints. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **scorecard use and release boundary.** Assess: determine scorecard purpose and responsibility boundary, determine scorecard disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- Population and target contract.
- Binning and variable-selection record.
- Scaled scorecard specification.
- Developer validation and cutoff-governance handoff.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide purpose — Determine scorecard purpose and responsibility boundary
- Decide population — Define target and development population
- Decide reject — Determine reject-inference treatment
- Decide binning — Select supervised binning treatment
- Decide monotonicity — Determine monotonicity constraints
- Decide variables — Select scorecard variables
- Decide scaling — Set points scaling and reason-code interpretation
- Decide cutoff — Define cutoff and decision-policy handoff
- Decide disposition — Determine scorecard disposition
- Package scorecard evidence — Package the scorecard professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute scorecard analysis
- Compute scorecard validation evidence

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
