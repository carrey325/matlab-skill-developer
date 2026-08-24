# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Define the modeled credit event

Use observable evidence to define the modeled credit event without preselecting the result.

### Inputs

- target event evidence (required): Default or deterioration event, state labels, observation timing, cure/re-entry, and intended interpretation.

### Rules

#### Binary Event Target

- Conditions: target event evidence equals single contractual default event.
- Rationale: A binary target is appropriate when one clearly defined default event drives the intended output.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for default or deterioration event, state labels, observation timing, cure/re-entry, and intended interpretation.; do not infer binary-event-target from provider availability.

#### Multi State Target

- Conditions: target event evidence equals multiple ordered or nominal credit states.
- Rationale: Multiple states require an explicit taxonomy; state probabilities must not be relabelled as default probabilities.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for default or deterioration event, state labels, observation timing, cure/re-entry, and intended interpretation.; do not infer multi-state-target from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define the modeled credit event.

## Select prediction horizon and output semantics

Use observable evidence to select prediction horizon and output semantics without preselecting the result.

### Inputs

- decision use horizon (required): Decision timing, performance window, repeated forecasts, and whether cumulative risk is required.

### Rules

#### Fixed Horizon Probability

- Conditions: decision use horizon equals single fixed performance window.
- Rationale: A fixed-horizon probability matches a single future performance window when observations and use align.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for decision timing, performance window, repeated forecasts, and whether cumulative risk is required.; do not infer fixed-horizon-probability from provider availability.

#### Survival Or Hazard Route

- Conditions: decision use horizon equals time-to-event with censoring.
- Rationale: Censoring and varying follow-up require survival or hazard modelling rather than fixed-window deletion.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for decision timing, performance window, repeated forecasts, and whether cumulative risk is required.; do not infer survival-or-hazard-route from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select prediction horizon and output semantics.

## Choose binary, ordinal, or nominal structure

Use observable evidence to choose binary, ordinal, or nominal structure without preselecting the result.

### Inputs

- state order evidence (required): Whether state labels have a defensible ordering and whether category distinctions are decision-relevant.

### Rules

#### Ordinal Candidate

- Conditions: state order evidence equals states have defensible worsening order.
- Rationale: An ordinal candidate uses the state ordering while requiring proportionality or alternative assumptions to be assessed.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for whether state labels have a defensible ordering and whether category distinctions are decision-relevant.; do not infer ordinal-candidate from provider availability.

#### Nominal Multinomial Candidate

- Conditions: state order evidence equals states are distinct without defensible order.
- Rationale: Nominal modelling is required when imposing order would create unsupported probability relationships.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for whether state labels have a defensible ordering and whether category distinctions are decision-relevant.; do not infer nominal-multinomial-candidate from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to choose binary, ordinal, or nominal structure.

## Determine panel, snapshot, or event-history data design

Use observable evidence to determine panel, snapshot, or event-history data design without preselecting the result.

### Inputs

- observation structure (required): Repeated borrower observations, state dependence, censoring, sampling, and leakage risk.

### Rules

#### Panel Or Event History Design

- Conditions: observation structure equals repeated observations with time-varying predictors.
- Rationale: Repeated observations require time ordering, leakage controls, and dependence-aware validation.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for repeated borrower observations, state dependence, censoring, sampling, and leakage risk.; do not infer panel-or-event-history-design from provider availability.

#### Snapshot Design

- Conditions: observation structure equals one observation per independent decision point.
- Rationale: A snapshot design is appropriate only when independence and timing assumptions are supportable.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for repeated borrower observations, state dependence, censoring, sampling, and leakage risk.; do not infer snapshot-design from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine panel, snapshot, or event-history data design.

## Select statistical or nonlinear candidate family

Use observable evidence to select statistical or nonlinear candidate family without preselecting the result.

### Inputs

- signal complexity and constraints (required): Nonlinearity evidence, sample size, benchmark strength, interpretability, and operational constraints.

### Rules

#### Statistical Benchmark And Candidates

- Conditions: signal complexity and constraints equals interpretable relationship with limited complexity.
- Rationale: Transparent statistical candidates should anchor comparison when they explain the signal adequately.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for nonlinearity evidence, sample size, benchmark strength, interpretability, and operational constraints.; do not infer statistical-benchmark-and-candidates from provider availability.

#### Nonlinear Challenger

- Conditions: signal complexity and constraints equals material nonlinear interactions with sufficient data.
- Rationale: A nonlinear challenger is justified only when out-of-sample gains, stability, and explanation burden are addressed.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for nonlinearity evidence, sample size, benchmark strength, interpretability, and operational constraints.; do not infer nonlinear-challenger from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select statistical or nonlinear candidate family.

## Treat class imbalance and rare states

Use observable evidence to treat class imbalance and rare states without preselecting the result.

### Inputs

- class support evidence (required): Event counts, state frequencies, sampling design, cost asymmetry, and calibration target.

### Rules

#### Weighted Or Resampled Study

- Conditions: class support evidence equals rare class still supports independent validation.
- Rationale: Weighting or resampling may be studied, but probability calibration must return to the target population.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for event counts, state frequencies, sampling design, cost asymmetry, and calibration target.; do not infer weighted-or-resampled-study from provider availability.

#### Combine Redesign Or Stop

- Conditions: class support evidence equals class support inadequate for reliable estimation.
- Rationale: Sparse states require defensible combination, more data, or stopping; synthetic balance cannot create information.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for event counts, state frequencies, sampling design, cost asymmetry, and calibration target.; do not infer combine-redesign-or-stop from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to treat class imbalance and rare states.

## Set interpretability and benchmark requirements

Use observable evidence to set interpretability and benchmark requirements without preselecting the result.

### Inputs

- use and challenge needs (required): Decision materiality, adverse-action or explanation needs, challenger expectations, and governance burden.

### Rules

#### Interpretable Primary Model

- Conditions: use and challenge needs equals high explanation or policy materiality.
- Rationale: High-stakes uses require an interpretable primary model or a demonstrably faithful explanation framework.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for decision materiality, adverse-action or explanation needs, challenger expectations, and governance burden.; do not infer interpretable-primary-model from provider availability.

#### Complex Model With Benchmark

- Conditions: use and challenge needs equals prediction support with controlled explanation burden.
- Rationale: A complex model still requires a transparent benchmark, sensitivity evidence, and documented limitations.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for decision materiality, adverse-action or explanation needs, challenger expectations, and governance burden.; do not infer complex-model-with-benchmark from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set interpretability and benchmark requirements.

## Determine default-model disposition

Use observable evidence to determine default-model disposition without preselecting the result.

### Inputs

- validation evidence pattern (required): Out-of-sample discrimination, calibration, class-level performance, stability, benchmark comparison, and limitations.

### Rules

#### Package For Validation

- Conditions: validation evidence pattern equals gains are stable and assumptions support intended use.
- Rationale: The selected model may proceed when gains over benchmark are stable and class-level weaknesses are controlled.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for out-of-sample discrimination, calibration, class-level performance, stability, benchmark comparison, and limitations.; do not infer package-for-validation from provider availability.

#### Simplify Recalibrate Or Redevelop

- Conditions: validation evidence pattern equals gain is unstable or unsupported by professional rationale.
- Rationale: An apparent metric winner is rejected when instability, leakage, or weak rationale outweighs development performance.
- Applies to: Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task..
- Excludes: lifetime PD term structures, points-based scorecard delivery.
- If information is missing: Stop this decision and obtain evidence for out-of-sample discrimination, calibration, class-level performance, stability, benchmark comparison, and limitations.; do not infer simplify-recalibrate-or-redevelop from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine default-model disposition.
