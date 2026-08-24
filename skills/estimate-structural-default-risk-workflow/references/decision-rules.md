# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Define default boundary and liability mapping

Use observable evidence to define default boundary and liability mapping without preselecting the result.

### Inputs

- capital structure evidence (required): Short- and long-term liabilities, seniority, maturity, off-balance-sheet obligations, and model boundary.

### Rules

#### Mapped Default Boundary

- Conditions: capital structure evidence equals simple corporate structure with reliable liabilities.
- Rationale: The default boundary must be documented from liabilities rather than assumed from equity value alone.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for short- and long-term liabilities, seniority, maturity, off-balance-sheet obligations, and model boundary.; do not infer mapped-default-boundary from provider availability.

#### Scenario Boundaries With Limitation

- Conditions: capital structure evidence equals complex or opaque liability structure.
- Rationale: Complex liabilities require boundary scenarios and explicit limitation because one debt proxy is not identifiable.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for short- and long-term liabilities, seniority, maturity, off-balance-sheet obligations, and model boundary.; do not infer scenario-boundaries-with-limitation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define default boundary and liability mapping.

## Set structural risk horizon

Use observable evidence to set structural risk horizon without preselecting the result.

### Inputs

- decision horizon and debt maturity (required): Use horizon, liability maturity, market-data frequency, and interpretation of default probability.

### Rules

#### Point In Time Structural Estimate

- Conditions: decision horizon and debt maturity equals single reporting-date horizon.
- Rationale: A point-in-time estimate is aligned to one valuation date and selected horizon.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for use horizon, liability maturity, market-data frequency, and interpretation of default probability.; do not infer point-in-time-structural-estimate from provider availability.

#### Time Series Structural Estimate

- Conditions: decision horizon and debt maturity equals evolving issuer risk over many dates.
- Rationale: A time-series design is required when asset value and default risk must evolve with market observations.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for use horizon, liability maturity, market-data frequency, and interpretation of default probability.; do not infer time-series-structural-estimate from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set structural risk horizon.

## Select equity-volatility input

Use observable evidence to select equity-volatility input without preselecting the result.

### Inputs

- volatility evidence (required): Observation window, frequency, corporate events, option-implied data, regime change, and annualisation.

### Rules

#### Historical Equity Volatility

- Conditions: volatility evidence equals liquid stable equity return history.
- Rationale: Historical volatility may be used when the window represents current risk and is robust to corporate events.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for observation window, frequency, corporate events, option-implied data, regime change, and annualisation.; do not infer historical-equity-volatility from provider availability.

#### Multiple Volatility Scenarios

- Conditions: volatility evidence equals recent regime shift or event dominates history.
- Rationale: Regime uncertainty requires alternative windows or implied measures and sensitivity rather than one mechanical estimate.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for observation window, frequency, corporate events, option-implied data, regime change, and annualisation.; do not infer multiple-volatility-scenarios from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select equity-volatility input.

## Calibrate asset value and asset volatility

Use observable evidence to calibrate asset value and asset volatility without preselecting the result.

### Inputs

- solver and identification evidence (required): Equation residuals, initial values, convergence, bounds, observation frequency, and parameter stability.

### Rules

#### Accept Calibrated Assets

- Conditions: solver and identification evidence equals solution converges with stable residuals.
- Rationale: A valid solution must satisfy equity-value and volatility relationships with stable, economically plausible parameters.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for equation residuals, initial values, convergence, bounds, observation frequency, and parameter stability.; do not infer accept-calibrated-assets from provider availability.

#### Respecify Or Limit Calibration

- Conditions: solver and identification evidence equals multiple or unstable solutions.
- Rationale: Unstable calibration requires changed inputs, constraints, or limitation; solver completion is not validation.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for equation residuals, initial values, convergence, bounds, observation frequency, and parameter stability.; do not infer respecify-or-limit-calibration from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to calibrate asset value and asset volatility.

## Assess market and capital-structure representativeness

Use observable evidence to assess market and capital-structure representativeness without preselecting the result.

### Inputs

- market input quality (required): Liquidity, stale prices, structural breaks, equity dilution, debt updates, and issuer actions.

### Rules

#### Freeze Market Snapshot

- Conditions: market input quality equals inputs liquid current and internally consistent.
- Rationale: Structural output is meaningful only for a current, internally consistent market and liability snapshot.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for liquidity, stale prices, structural breaks, equity dilution, debt updates, and issuer actions.; do not infer freeze-market-snapshot from provider availability.

#### Repair Or Stop Estimate

- Conditions: market input quality equals stale illiquid or inconsistent inputs.
- Rationale: Stale or inconsistent market data require repair or stopping rather than false precision.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for liquidity, stale prices, structural breaks, equity dilution, debt updates, and issuer actions.; do not infer repair-or-stop-estimate from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess market and capital-structure representativeness.

## Assess structural-model sensitivity

Use observable evidence to assess structural-model sensitivity without preselecting the result.

### Inputs

- parameter sensitivity results (required): Debt boundary, equity volatility, risk-free rate, horizon, payout, and model-form alternatives.

### Rules

#### Stable Structural Risk

- Conditions: parameter sensitivity results equals default risk robust across credible ranges.
- Rationale: Robustness across credible input ranges supports directional use while retaining structural assumptions.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for debt boundary, equity volatility, risk-free rate, horizon, payout, and model-form alternatives.; do not infer stable-structural-risk from provider availability.

#### Limited Use Structural Risk

- Conditions: parameter sensitivity results equals estimate dominated by one uncertain input.
- Rationale: Dominant input uncertainty requires a range and use limitation rather than a single default probability.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for debt boundary, equity volatility, risk-free rate, horizon, payout, and model-form alternatives.; do not infer limited-use-structural-risk from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess structural-model sensitivity.

## Determine structural-risk disposition

Use observable evidence to determine structural-risk disposition without preselecting the result.

### Inputs

- combined structural evidence (required): Input quality, calibration stability, benchmark comparison, sensitivity, and intended use.

### Rules

#### Report Structural Risk

- Conditions: combined structural evidence equals calibration and sensitivity support intended use.
- Rationale: Report distance-to-default and probability with market date, boundary, horizon, assumptions, and limitations.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for input quality, calibration stability, benchmark comparison, sensitivity, and intended use.; do not infer report-structural-risk from provider availability.

#### Reject Or Report Range Only

- Conditions: combined structural evidence equals material identification or market-data failure.
- Rationale: Material identification or data failure prevents an unqualified point estimate.
- Applies to: Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information..
- Excludes: behavioural PD development, CDS trading.
- If information is missing: Stop this decision and obtain evidence for input quality, calibration stability, benchmark comparison, sensitivity, and intended use.; do not infer reject-or-report-range-only from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine structural-risk disposition.
