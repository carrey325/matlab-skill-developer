# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Determine curve purpose and probability interpretation

Use observable evidence to determine curve purpose and probability interpretation without preselecting the result.

### Inputs

- declared curve use (required): Valuation, relative value, stress, accounting, or internal risk use and risk-neutral versus physical interpretation.

### Rules

#### Risk Neutral Default Curve

- Conditions: declared curve use equals market-consistent valuation.
- Rationale: Market prices imply risk-neutral default compensation and must not be presented as a physical forecast.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for valuation, relative value, stress, accounting, or internal risk use and risk-neutral versus physical interpretation.; do not infer risk-neutral-default-curve from provider availability.

#### Handoff To Pd Workflow

- Conditions: declared curve use equals internal physical risk forecast.
- Rationale: A physical forecast belongs in a PD development workflow rather than being inferred from traded spreads without adjustment.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for valuation, relative value, stress, accounting, or internal risk use and risk-neutral versus physical interpretation.; do not infer handoff-to-pd-workflow from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine curve purpose and probability interpretation.

## Select calibration instruments and quotes

Use observable evidence to select calibration instruments and quotes without preselecting the result.

### Inputs

- market instrument evidence (required): Liquidity, seniority, currency, restructuring clause, maturity, collateral, accrued interest, and quote quality.

### Rules

#### Bond Price Bootstrap

- Conditions: market instrument evidence equals liquid consistent bond set.
- Rationale: Bonds may support curve bootstrapping when cash flows, seniority, optionality, and discounting are controlled.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for liquidity, seniority, currency, restructuring clause, maturity, collateral, accrued interest, and quote quality.; do not infer bond-price-bootstrap from provider availability.

#### Cds Spread Calibration

- Conditions: market instrument evidence equals liquid standard CDS tenors.
- Rationale: Standard CDS spreads support hazard calibration when contract conventions and recovery are consistent.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for liquidity, seniority, currency, restructuring clause, maturity, collateral, accrued interest, and quote quality.; do not infer cds-spread-calibration from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select calibration instruments and quotes.

## Freeze contract and market conventions

Use observable evidence to freeze contract and market conventions without preselecting the result.

### Inputs

- convention record (required): Day count, payment frequency, accrual on default, settlement, currency, restructuring, and business-day rules.

### Rules

#### Freeze Curve Conventions

- Conditions: convention record equals complete convention set matches quotes.
- Rationale: Calibration requires conventions that reproduce instrument cash flows and quoted spreads.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for day count, payment frequency, accrual on default, settlement, currency, restructuring, and business-day rules.; do not infer freeze-curve-conventions from provider availability.

#### Repair Or Segment Instruments

- Conditions: convention record equals material convention unknown or mixed.
- Rationale: Unknown or mixed conventions require repair or separate curves; silent defaults create false calibration accuracy.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for day count, payment frequency, accrual on default, settlement, currency, restructuring, and business-day rules.; do not infer repair-or-segment-instruments from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to freeze contract and market conventions.

## Set recovery assumption or recovery calibration

Use observable evidence to set recovery assumption or recovery calibration without preselecting the result.

### Inputs

- recovery market evidence (required): Instrument seniority, recovery convention, observed recoveries, identifiability, and sensitivity.

### Rules

#### Fixed Recovery Assumption

- Conditions: recovery market evidence equals recovery fixed by approved market convention.
- Rationale: A fixed recovery assumption must be disclosed because hazard and recovery are not separately identified from limited spreads.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for instrument seniority, recovery convention, observed recoveries, identifiability, and sensitivity.; do not infer fixed-recovery-assumption from provider availability.

#### Joint Or Separate Recovery Study

- Conditions: recovery market evidence equals recovery instruments provide independent information.
- Rationale: Recovery may be calibrated only when independent data make it identifiable and stable.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for instrument seniority, recovery convention, observed recoveries, identifiability, and sensitivity.; do not infer joint-or-separate-recovery-study from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set recovery assumption or recovery calibration.

## Select discount curve and currency treatment

Use observable evidence to select discount curve and currency treatment without preselecting the result.

### Inputs

- discounting contract (required): Collateral or funding convention, currency, valuation date, interpolation, and instrument cash flows.

### Rules

#### Freeze Discount Curve

- Conditions: discounting contract equals approved currency-consistent discount curve.
- Rationale: Credit calibration must use a discount curve consistent with instrument currency and valuation conventions.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for collateral or funding convention, currency, valuation date, interpolation, and instrument cash flows.; do not infer freeze-discount-curve from provider availability.

#### Repair Discounting

- Conditions: discounting contract equals discount basis inconsistent with instruments.
- Rationale: A discount mismatch biases inferred default rates and must be repaired before credit calibration.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for collateral or funding convention, currency, valuation date, interpolation, and instrument cash flows.; do not infer repair-discounting from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select discount curve and currency treatment.

## Choose calibration objective and constraints

Use observable evidence to choose calibration objective and constraints without preselecting the result.

### Inputs

- quote error and shape evidence (required): Quote measure, weighting, positivity, monotonic survival, parameterization, and solver stability.

### Rules

#### Constrained Hazard Calibration

- Conditions: quote error and shape evidence equals quotes can be matched with nonnegative hazards.
- Rationale: Calibration should preserve nonnegative hazards and non-increasing survival while explaining residual quote error.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for quote measure, weighting, positivity, monotonic survival, parameterization, and solver stability.; do not infer constrained-hazard-calibration from provider availability.

#### Reject Or Clean Inputs

- Conditions: quote error and shape evidence equals fit requires negative hazard or unstable parameters.
- Rationale: An economically inconsistent fit requires quote cleaning, revised assumptions, or rejection—not acceptance of negative default intensity.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for quote measure, weighting, positivity, monotonic survival, parameterization, and solver stability.; do not infer reject-or-clean-inputs from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to choose calibration objective and constraints.

## Select interpolation and extrapolation policy

Use observable evidence to select interpolation and extrapolation policy without preselecting the result.

### Inputs

- tenor coverage and use (required): Observed maturities, curve smoothness, intended valuation tenors, tail support, and policy limits.

### Rules

#### Controlled Interpolation

- Conditions: tenor coverage and use equals requested tenors lie within liquid observations.
- Rationale: Interpolation may be used inside supported tenor ranges with shape and repricing checks.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for observed maturities, curve smoothness, intended valuation tenors, tail support, and policy limits.; do not infer controlled-interpolation from provider availability.

#### Limited Extrapolation

- Conditions: tenor coverage and use equals requested tenor extends beyond reliable quotes.
- Rationale: Extrapolation requires an approved tail rule, sensitivity, and explicit use limitation.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for observed maturities, curve smoothness, intended valuation tenors, tail support, and policy limits.; do not infer limited-extrapolation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select interpolation and extrapolation policy.

## Validate repricing and curve consistency

Use observable evidence to validate repricing and curve consistency without preselecting the result.

### Inputs

- curve diagnostics (required): Instrument repricing errors, survival monotonicity, hazard signs, spread ordering, sensitivity, and stale quotes.

### Rules

#### Curve Validated For Use

- Conditions: curve diagnostics equals repricing and economic shape checks pass.
- Rationale: Curve use requires both quote fit and economically coherent probability shape.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for instrument repricing errors, survival monotonicity, hazard signs, spread ordering, sensitivity, and stale quotes.; do not infer curve-validated-for-use from provider availability.

#### Recalibrate Or Reject Curve

- Conditions: curve diagnostics equals material repricing or shape failure.
- Rationale: Material repricing or probability-shape failure blocks curve release.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for instrument repricing errors, survival monotonicity, hazard signs, spread ordering, sensitivity, and stale quotes.; do not infer recalibrate-or-reject-curve from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to validate repricing and curve consistency.

## Determine credit-curve disposition

Use observable evidence to determine credit-curve disposition without preselecting the result.

### Inputs

- combined curve evidence (required): Quote quality, conventions, assumptions, fit, shape, sensitivity, extrapolation, and intended use.

### Rules

#### Publish Curve With Assumptions

- Conditions: combined curve evidence equals fit stable and use lies within supported range.
- Rationale: A curve is released with valuation date, instruments, assumptions, diagnostics, and tenor limits.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for quote quality, conventions, assumptions, fit, shape, sensitivity, extrapolation, and intended use.; do not infer publish-curve-with-assumptions from provider availability.

#### Limit Or Reject Curve

- Conditions: combined curve evidence equals material data or identifiability weakness.
- Rationale: Material quote, recovery, or extrapolation weakness requires use limitation or rejection.
- Applies to: Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis..
- Excludes: physical PD development, trading or hedging.
- If information is missing: Stop this decision and obtain evidence for quote quality, conventions, assumptions, fit, shape, sensitivity, extrapolation, and intended use.; do not infer limit-or-reject-curve from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine credit-curve disposition.
