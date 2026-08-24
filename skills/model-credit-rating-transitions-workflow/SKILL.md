---
name: model-credit-rating-transitions-workflow
description: Develop a rating-transition model by defining states, observation method, default treatment, horizon conversion, sparse-cell treatment, smoothing, calibration, stress response, validation, and use limitations. Use when a risk owner requires a transition matrix or transition process for migration analysis, portfolio risk, stress testing, or planning. Not for rating assignment, binary default model development, or credit curve construction.
---

# Purpose

Develop a rating-transition model by defining states, observation method, default treatment, horizon conversion, sparse-cell treatment, smoothing, calibration, stress response, validation, and use limitations.

# Scope and Applicability

Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.

A risk owner requires a transition matrix or transition process for migration analysis, portfolio risk, stress testing, or planning.

Do not use for rating assignment, ordinary binary default modelling, credit curve bootstrapping, or portfolio aggregation.

## Exclusions

- rating assignment
- binary default model development
- credit curve construction
- portfolio aggregation
- independent approval

# Required Inputs

- Rating-state taxonomy and history.
- Observation dates, withdrawals, defaults, and censoring.
- Target horizon and use constraints.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Rating-state taxonomy and history, observation dates, withdrawals, defaults, and censoring, target horizon and use constraints.
- Outputs: State and observation contract, transition estimator and horizon conversion, calibration, smoothing, and stability evidence, validated matrix package and limitations.

## Define rating states and ordering

- Inputs: Grade definitions, ordering, default, not-rated/withdrawn, cure, and mapping changes.
- Outputs: Decision record for define rating states and ordering.

## Select cohort or duration estimator

- Inputs: Observation frequency, exact transition dates, censoring, withdrawals, and within-period multiple moves.
- Outputs: Decision record for select cohort or duration estimator.

## Set default and withdrawal treatment

- Inputs: Default absorption, cure/re-entry, withdrawn ratings, missing ratings, and competing exits.
- Outputs: Decision record for set default and withdrawal treatment.

## Convert transition horizon

- Inputs: Observed interval, requested horizon, homogeneity, generator embeddability, and business cycle.
- Outputs: Decision record for convert transition horizon.

## Treat sparse transitions and rare states

- Inputs: Exposure time, transition counts, zero cells, rare grades, and estimation uncertainty.
- Outputs: Decision record for treat sparse transitions and rare states.

## Calibrate transition and default rates

- Inputs: Row sums, observed frequencies, default marginals, long-run or PIT target, and segment stability.
- Outputs: Decision record for calibrate transition and default rates.

## Determine stressed transition treatment

- Inputs: Scenario use, rating philosophy, macro sensitivity, monotonicity, and probability constraints.
- Outputs: Decision record for determine stressed transition treatment.

## Determine transition-model disposition

- Inputs: State stability, probability conservation, calibration, horizon conversion, sensitivity, and use limitations.
- Outputs: Decision record for determine transition-model disposition.

## Execute the approved TRANSITIONS computation

- Work: Run the approved computational specification without changing professional choices.

## Assess TRANSITIONS technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the TRANSITIONS professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Define rating states and ordering.** Consider grade definitions, ordering, default, not-rated/withdrawn, cure, and mapping changes. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define rating states and ordering.
- **Select cohort or duration estimator.** Consider observation frequency, exact transition dates, censoring, withdrawals, and within-period multiple moves. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select cohort or duration estimator.
- **Set default and withdrawal treatment.** Consider default absorption, cure/re-entry, withdrawn ratings, missing ratings, and competing exits. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to set default and withdrawal treatment.
- **Convert transition horizon.** Consider observed interval, requested horizon, homogeneity, generator embeddability, and business cycle. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to convert transition horizon.
- **Treat sparse transitions and rare states.** Consider exposure time, transition counts, zero cells, rare grades, and estimation uncertainty. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to treat sparse transitions and rare states.
- **Calibrate transition and default rates.** Consider row sums, observed frequencies, default marginals, long-run or PIT target, and segment stability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to calibrate transition and default rates.
- **Determine stressed transition treatment.** Consider scenario use, rating philosophy, macro sensitivity, monotonicity, and probability constraints. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine stressed transition treatment.
- **Determine transition-model disposition.** Consider state stability, probability conservation, calibration, horizon conversion, sensitivity, and use limitations. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine transition-model disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **TRANSITIONS technical fitness.** Assess: select cohort or duration estimator, set default and withdrawal treatment, convert transition horizon, treat sparse transitions and rare states. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **TRANSITIONS use and release boundary.** Assess: define rating states and ordering, determine transition-model disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- State and observation contract.
- Transition estimator and horizon conversion.
- Calibration, smoothing, and stability evidence.
- Validated matrix package and limitations.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide states — Define rating states and ordering
- Decide observation — Select cohort or duration estimator
- Decide default — Set default and withdrawal treatment
- Decide horizon — Convert transition horizon
- Decide sparse — Treat sparse transitions and rare states
- Decide calibration — Calibrate transition and default rates
- Decide stress — Determine stressed transition treatment
- Decide disposition — Determine transition-model disposition
- Package transitions evidence — Package the TRANSITIONS professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute transitions analysis
- Compute transitions validation evidence

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
