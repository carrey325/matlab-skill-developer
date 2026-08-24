# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Define rating states and ordering

Use observable evidence to define rating states and ordering without preselecting the result.

### Inputs

- rating taxonomy evidence (required): Grade definitions, ordering, default, not-rated/withdrawn, cure, and mapping changes.

### Rules

#### Ordered Rating State Space

- Conditions: rating taxonomy evidence equals stable ordered internal grades plus default.
- Rationale: An ordered state space requires consistent grade meaning over the observation history.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for grade definitions, ordering, default, not-rated/withdrawn, cure, and mapping changes.; do not infer ordered-rating-state-space from provider availability.

#### Harmonise Or Split Taxonomy

- Conditions: rating taxonomy evidence equals taxonomy changed materially over time.
- Rationale: Material taxonomy changes require mapping, separate regimes, or a shorter history before transition estimation.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for grade definitions, ordering, default, not-rated/withdrawn, cure, and mapping changes.; do not infer harmonise-or-split-taxonomy from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define rating states and ordering.

## Select cohort or duration estimator

Use observable evidence to select cohort or duration estimator without preselecting the result.

### Inputs

- rating observation pattern (required): Observation frequency, exact transition dates, censoring, withdrawals, and within-period multiple moves.

### Rules

#### Cohort Estimator

- Conditions: rating observation pattern equals ratings observed only at regular snapshots.
- Rationale: A cohort estimator matches snapshot observations but must define multiple transitions and withdrawals.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for observation frequency, exact transition dates, censoring, withdrawals, and within-period multiple moves.; do not infer cohort-estimator from provider availability.

#### Duration Or Generator Estimator

- Conditions: rating observation pattern equals event dates and exposure time are reliable.
- Rationale: Duration methods use time at risk and exact transitions when event timing is trustworthy.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for observation frequency, exact transition dates, censoring, withdrawals, and within-period multiple moves.; do not infer duration-or-generator-estimator from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select cohort or duration estimator.

## Set default and withdrawal treatment

Use observable evidence to set default and withdrawal treatment without preselecting the result.

### Inputs

- terminal state evidence (required): Default absorption, cure/re-entry, withdrawn ratings, missing ratings, and competing exits.

### Rules

#### Absorbing Default State

- Conditions: terminal state evidence equals default is terminal for intended horizon.
- Rationale: Default is represented as absorbing when the use treats post-default movements outside the migration process.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for default absorption, cure/re-entry, withdrawn ratings, missing ratings, and competing exits.; do not infer absorbing-default-state from provider availability.

#### Explicit Post Default States

- Conditions: terminal state evidence equals cure or post-default migration is in scope.
- Rationale: Cure and post-default behaviour require explicit states rather than breaking probability conservation.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for default absorption, cure/re-entry, withdrawn ratings, missing ratings, and competing exits.; do not infer explicit-post-default-states from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set default and withdrawal treatment.

## Convert transition horizon

Use observable evidence to convert transition horizon without preselecting the result.

### Inputs

- target horizon and process assumption (required): Observed interval, requested horizon, homogeneity, generator embeddability, and business cycle.

### Rules

#### Matrix Power Or Generator Conversion

- Conditions: target horizon and process assumption equals time-homogeneous process is supportable.
- Rationale: Horizon conversion requires a supportable time-homogeneity or generator assumption.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for observed interval, requested horizon, homogeneity, generator embeddability, and business cycle.; do not infer matrix-power-or-generator-conversion from provider availability.

#### Regime Specific Horizon Estimation

- Conditions: target horizon and process assumption equals transition dynamics vary materially by regime.
- Rationale: Regime-varying transitions should not be produced by mechanically powering one unconditional matrix.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for observed interval, requested horizon, homogeneity, generator embeddability, and business cycle.; do not infer regime-specific-horizon-estimation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to convert transition horizon.

## Treat sparse transitions and rare states

Use observable evidence to treat sparse transitions and rare states without preselecting the result.

### Inputs

- cell support evidence (required): Exposure time, transition counts, zero cells, rare grades, and estimation uncertainty.

### Rules

#### Constrained Smoothing

- Conditions: cell support evidence equals sparse adjacent transitions with coherent ordering.
- Rationale: Constrained smoothing may reduce sampling noise while preserving probability and rating order.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for exposure time, transition counts, zero cells, rare grades, and estimation uncertainty.; do not infer constrained-smoothing from provider availability.

#### Merge Limit Or Stop State

- Conditions: cell support evidence equals state has inadequate exposure or unstable meaning.
- Rationale: An unsupported state requires defensible merging, limitation, or exclusion rather than synthetic transitions.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for exposure time, transition counts, zero cells, rare grades, and estimation uncertainty.; do not infer merge-limit-or-stop-state from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to treat sparse transitions and rare states.

## Calibrate transition and default rates

Use observable evidence to calibrate transition and default rates without preselecting the result.

### Inputs

- matrix calibration evidence (required): Row sums, observed frequencies, default marginals, long-run or PIT target, and segment stability.

### Rules

#### Calibrated Transition Matrix

- Conditions: matrix calibration evidence equals matrix probabilities and marginals reconcile.
- Rationale: Calibration requires probability conservation and reconciliation to observed or approved targets.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for row sums, observed frequencies, default marginals, long-run or pit target, and segment stability.; do not infer calibrated-transition-matrix from provider availability.

#### Reestimate Or Calibrate

- Conditions: matrix calibration evidence equals default or migration marginals materially biased.
- Rationale: Material marginal bias requires re-estimation or explicit calibration without distorting state ordering.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for row sums, observed frequencies, default marginals, long-run or pit target, and segment stability.; do not infer reestimate-or-calibrate from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to calibrate transition and default rates.

## Determine stressed transition treatment

Use observable evidence to determine stressed transition treatment without preselecting the result.

### Inputs

- scenario and regime evidence (required): Scenario use, rating philosophy, macro sensitivity, monotonicity, and probability constraints.

### Rules

#### Scenario Conditional Transitions

- Conditions: scenario and regime evidence equals validated conditional transition relationship exists.
- Rationale: Stress transitions may use validated conditional relationships that preserve row probabilities and sensible deterioration.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for scenario use, rating philosophy, macro sensitivity, monotonicity, and probability constraints.; do not infer scenario-conditional-transitions from provider availability.

#### Sensitivity Matrices With Limits

- Conditions: scenario and regime evidence equals no validated macro-transition link.
- Rationale: Use transparent sensitivity matrices and limitations rather than claiming a calibrated scenario model.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for scenario use, rating philosophy, macro sensitivity, monotonicity, and probability constraints.; do not infer sensitivity-matrices-with-limits from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine stressed transition treatment.

## Determine transition-model disposition

Use observable evidence to determine transition-model disposition without preselecting the result.

### Inputs

- validation evidence pattern (required): State stability, probability conservation, calibration, horizon conversion, sensitivity, and use limitations.

### Rules

#### Package Transition Model

- Conditions: validation evidence pattern equals matrix stable and fit for declared horizon.
- Rationale: A usable matrix must reconcile, remain stable enough for its use, and disclose sparse-state uncertainty.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for state stability, probability conservation, calibration, horizon conversion, sensitivity, and use limitations.; do not infer package-transition-model from provider availability.

#### Respecify Or Reject

- Conditions: validation evidence pattern equals material taxonomy or horizon assumption failure.
- Rationale: Taxonomy or horizon failures require respecification, not a cosmetic matrix repair.
- Applies to: Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states..
- Excludes: rating assignment, binary default model development.
- If information is missing: Stop this decision and obtain evidence for state stability, probability conservation, calibration, horizon conversion, sensitivity, and use limitations.; do not infer respecify-or-reject from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine transition-model disposition.
