# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Determine VaR and ES use

Use observable evidence to determine var and es use without preselecting the result.

### Inputs

- declared market risk use (required): Internal risk, limit monitoring, disclosure, or applicable capital purpose and governing policy.

### Rules

#### Internal Risk Measures

- Conditions: declared market risk use equals internal market-risk measurement.
- Rationale: Internal use may choose horizon and confidence under approved policy while retaining method and limitation transparency.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for internal risk, limit monitoring, disclosure, or applicable capital purpose and governing policy.; do not infer internal-risk-measures from provider availability.

#### Market Risk Capital Branch

- Conditions: declared market risk use equals Basel internal-model capital support.
- Rationale: Capital support must follow the applicable market-risk framework, including ES and model eligibility requirements.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for internal risk, limit monitoring, disclosure, or applicable capital purpose and governing policy.; do not infer market-risk-capital-branch from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine var and es use.

## Define portfolio and P&L measure

Use observable evidence to define portfolio and p&l measure without preselecting the result.

### Inputs

- pnl and position contract (required): Position snapshot, valuation basis, actual/hypothetical P&L, fees, intraday changes, and risk-factor mapping.

### Rules

#### Risk Theoretical Pnl

- Conditions: pnl and position contract equals fixed positions with clean hypothetical P&L.
- Rationale: A fixed-position risk-theoretical P&L isolates modeled market moves and supports consistent estimation.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for position snapshot, valuation basis, actual/hypothetical p&l, fees, intraday changes, and risk-factor mapping.; do not infer risk-theoretical-pnl from provider availability.

#### Reconcile And Separate Pnl

- Conditions: pnl and position contract equals actual P&L includes non-model components.
- Rationale: Actual P&L requires reconciliation and separation of fees, intraday, reserves, and non-model effects.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for position snapshot, valuation basis, actual/hypothetical p&l, fees, intraday changes, and risk-factor mapping.; do not infer reconcile-and-separate-pnl from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define portfolio and p&l measure.

## Set horizon and confidence level

Use observable evidence to set horizon and confidence level without preselecting the result.

### Inputs

- approved risk measure policy (required): Risk use, liquidity, holding period, confidence/tail probability, scaling assumptions, and data frequency.

### Rules

#### One Day Policy Measure

- Conditions: approved risk measure policy equals daily internal risk monitoring.
- Rationale: A one-day measure is appropriate only when aligned to the portfolio, valuation, and approved confidence policy.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for risk use, liquidity, holding period, confidence/tail probability, scaling assumptions, and data frequency.; do not infer one-day-policy-measure from provider availability.

#### Liquidity Horizon Es

- Conditions: approved risk measure policy equals capital liquidity horizon requirement.
- Rationale: Applicable market-risk capital uses ES and prescribed liquidity-horizon aggregation rather than arbitrary square-root scaling.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for risk use, liquidity, holding period, confidence/tail probability, scaling assumptions, and data frequency.; do not infer liquidity-horizon-es from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set horizon and confidence level.

## Select VaR and ES estimation method

Use observable evidence to select var and es estimation method without preselecting the result.

### Inputs

- return distribution and revaluation evidence (required): History length, volatility dynamics, tails, nonlinear positions, scenario capability, and computational budget.

### Rules

#### Historical Simulation

- Conditions: return distribution and revaluation evidence equals representative history with full revaluation available.
- Rationale: Historical simulation preserves empirical joint moves when history is representative and positions can be revalued.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for history length, volatility dynamics, tails, nonlinear positions, scenario capability, and computational budget.; do not infer historical-simulation from provider availability.

#### Parametric Var Es

- Conditions: return distribution and revaluation evidence equals stable parametric structure with validated tail distribution.
- Rationale: Parametric estimation requires validated distribution, volatility, and dependence assumptions.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for history length, volatility dynamics, tails, nonlinear positions, scenario capability, and computational budget.; do not infer parametric-var-es from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select var and es estimation method.

## Treat nonlinear positions and risk factors

Use observable evidence to treat nonlinear positions and risk factors without preselecting the result.

### Inputs

- valuation nonlinearity evidence (required): Options, convexity, path dependence, discontinuities, basis risks, and approximation error.

### Rules

#### Full Revaluation Or Simulation

- Conditions: valuation nonlinearity evidence equals material nonlinear or path-dependent exposure.
- Rationale: Material nonlinear exposures require full revaluation or a validated nonlinear approximation.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for options, convexity, path dependence, discontinuities, basis risks, and approximation error.; do not infer full-revaluation-or-simulation from provider availability.

#### Linear Or Delta Approximation

- Conditions: valuation nonlinearity evidence equals portfolio locally linear with controlled approximation.
- Rationale: A linear approximation is supportable only when approximation error is tested under relevant moves.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for options, convexity, path dependence, discontinuities, basis risks, and approximation error.; do not infer linear-or-delta-approximation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to treat nonlinear positions and risk factors.

## Select tail and volatility treatment

Use observable evidence to select tail and volatility treatment without preselecting the result.

### Inputs

- tail diagnostic evidence (required): Tail thickness, volatility clustering, procyclicality, regime shifts, and sample support.

### Rules

#### Filtered Or Heavy Tail Model

- Conditions: tail diagnostic evidence equals heavy tails and conditional volatility evident.
- Rationale: Heavy tails and volatility dynamics require conditional or heavy-tail treatment rather than a normal unconditional assumption.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for tail thickness, volatility clustering, procyclicality, regime shifts, and sample support.; do not infer filtered-or-heavy-tail-model from provider availability.

#### Scenario Supplement And Limitation

- Conditions: tail diagnostic evidence equals limited tail sample or structural break.
- Rationale: Sparse tail data require stress scenarios and limitations; ES precision cannot be manufactured.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for tail thickness, volatility clustering, procyclicality, regime shifts, and sample support.; do not infer scenario-supplement-and-limitation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select tail and volatility treatment.

## Aggregate risk across positions and horizons

Use observable evidence to aggregate risk across positions and horizons without preselecting the result.

### Inputs

- dependence and aggregation evidence (required): Joint scenarios, correlations, liquidity horizons, diversification, missing factors, and netting rules.

### Rules

#### Joint Portfolio Aggregation

- Conditions: dependence and aggregation evidence equals joint scenarios preserve cross-risk dependence.
- Rationale: Portfolio VaR and ES should be computed from joint P&L when dependence and nonlinearities are material.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for joint scenarios, correlations, liquidity horizons, diversification, missing factors, and netting rules.; do not infer joint-portfolio-aggregation from provider availability.

#### Repair Before Aggregation

- Conditions: dependence and aggregation evidence equals components use incompatible scenarios or horizons.
- Rationale: Incompatible component measures cannot be summed or diversified without an approved aggregation method.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for joint scenarios, correlations, liquidity horizons, diversification, missing factors, and netting rules.; do not infer repair-before-aggregation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to aggregate risk across positions and horizons.

## Judge estimate stability and plausibility

Use observable evidence to judge estimate stability and plausibility without preselecting the result.

### Inputs

- estimation diagnostics (required): Monte Carlo error, sample sensitivity, distribution fit, decomposition, stress comparison, and day-to-day changes.

### Rules

#### Estimate Ready For Backtest

- Conditions: estimation diagnostics equals estimates stable across credible method sensitivities.
- Rationale: A stable estimate proceeds to independent backtesting with diagnostics and assumptions intact.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for monte carlo error, sample sensitivity, distribution fit, decomposition, stress comparison, and day-to-day changes.; do not infer estimate-ready-for-backtest from provider availability.

#### Limit Respecify Or Scenario Range

- Conditions: estimation diagnostics equals estimate dominated by method or sample choice.
- Rationale: Method-dominated results require respecification, ranges, or limitation before use.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for monte carlo error, sample sensitivity, distribution fit, decomposition, stress comparison, and day-to-day changes.; do not infer limit-respecify-or-scenario-range from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to judge estimate stability and plausibility.

## Determine VaR and ES estimation disposition

Use observable evidence to determine var and es estimation disposition without preselecting the result.

### Inputs

- combined estimation evidence (required): P&L integrity, method support, nonlinear coverage, tails, aggregation, diagnostics, and intended use.

### Rules

#### Release For Backtesting

- Conditions: combined estimation evidence equals measure supported for declared use.
- Rationale: Release includes horizon, confidence, P&L, method, diagnostics, limitations, and a backtesting handoff.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for p&l integrity, method support, nonlinear coverage, tails, aggregation, diagnostics, and intended use.; do not infer release-for-backtesting from provider availability.

#### Remediate Or Reject Estimate

- Conditions: combined estimation evidence equals material P&L or model-coverage gap.
- Rationale: Material P&L or coverage gaps block an unqualified risk estimate.
- Applies to: Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data..
- Excludes: credit ECL, credit parameter development.
- If information is missing: Stop this decision and obtain evidence for p&l integrity, method support, nonlinear coverage, tails, aggregation, diagnostics, and intended use.; do not infer remediate-or-reject-estimate from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine var and es estimation disposition.
