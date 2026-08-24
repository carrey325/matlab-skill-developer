# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Reconcile forecasts with realised P&L

Use observable evidence to reconcile forecasts with realised p&l without preselecting the result.

### Inputs

- forecast pnl alignment (required): Portfolio ID, date, horizon, confidence, sign, currency, position basis, missing values, and actual/hypothetical P&L.

### Rules

#### Freeze Backtest Sample

- Conditions: forecast pnl alignment equals one-to-one controlled alignment.
- Rationale: Backtesting requires each ex ante forecast to align with the subsequent controlled P&L observation.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for portfolio id, date, horizon, confidence, sign, currency, position basis, missing values, and actual/hypothetical p&l.; do not infer freeze-backtest-sample from provider availability.

#### Repair Before Testing

- Conditions: forecast pnl alignment equals timing portfolio or P&L mismatch.
- Rationale: Misaligned forecasts and P&L invalidate exception counts and must be repaired first.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for portfolio id, date, horizon, confidence, sign, currency, position basis, missing values, and actual/hypothetical p&l.; do not infer repair-before-testing from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to reconcile forecasts with realised p&l.

## Define VaR exceptions

Use observable evidence to define var exceptions without preselecting the result.

### Inputs

- approved exception convention (required): Loss sign, VaR sign, equality treatment, missing observations, confidence, and P&L variant.

### Rules

#### Record Var Exception

- Conditions: approved exception convention equals loss exceeds matched VaR under approved convention.
- Rationale: Exceptions must be counted consistently from the frozen risk and P&L convention.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for loss sign, var sign, equality treatment, missing observations, confidence, and p&l variant.; do not infer record-var-exception from provider availability.

#### Stop For Convention

- Conditions: approved exception convention equals exception depends on unresolved sign or P&L choice.
- Rationale: Do not count exceptions until sign and P&L conventions are resolved.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for loss sign, var sign, equality treatment, missing observations, confidence, and p&l variant.; do not infer stop-for-convention from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define var exceptions.

## Select VaR test family

Use observable evidence to select var test family without preselecting the result.

### Inputs

- backtest question and sample (required): Frequency, independence, conditional coverage, time-between-failures, sample size, and policy requirement.

### Rules

#### Coverage Frequency Tests

- Conditions: backtest question and sample equals question is unconditional exception frequency.
- Rationale: Frequency tests assess whether exception proportion matches the forecast confidence level.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for frequency, independence, conditional coverage, time-between-failures, sample size, and policy requirement.; do not infer coverage-frequency-tests from provider availability.

#### Independence And Conditional Tests

- Conditions: backtest question and sample equals exception clustering is material.
- Rationale: Independence or conditional coverage tests are needed when exceptions cluster through time.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for frequency, independence, conditional coverage, time-between-failures, sample size, and policy requirement.; do not infer independence-and-conditional-tests from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select var test family.

## Assess sample size and test power

Use observable evidence to assess sample size and test power without preselecting the result.

### Inputs

- observation and exception count (required): Usable observations, confidence level, expected exceptions, structural breaks, and missing periods.

### Rules

#### Interpret Test Results

- Conditions: observation and exception count equals sample supports selected test interpretation.
- Rationale: Test conclusions must reflect expected exception counts and statistical power.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for usable observations, confidence level, expected exceptions, structural breaks, and missing periods.; do not infer interpret-test-results from provider availability.

#### Limited Statistical Conclusion

- Conditions: observation and exception count equals sample too short or structurally mixed.
- Rationale: A weak or mixed sample requires limitations and supplementary evidence, not an automatic pass.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for usable observations, confidence level, expected exceptions, structural breaks, and missing periods.; do not infer limited-statistical-conclusion from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess sample size and test power.

## Apply traffic-light or institutional policy

Use observable evidence to apply traffic-light or institutional policy without preselecting the result.

### Inputs

- applicable backtest policy (required): Jurisdiction, model use, confidence level, sample window, and approved escalation thresholds.

### Rules

#### Apply Traffic Light Policy

- Conditions: applicable backtest policy equals policy explicitly applies to this VaR model.
- Rationale: Traffic-light classification is used only under its applicable framework and sample convention.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for jurisdiction, model use, confidence level, sample window, and approved escalation thresholds.; do not infer apply-traffic-light-policy from provider availability.

#### Use Institution Specific Policy

- Conditions: applicable backtest policy equals different use horizon or confidence.
- Rationale: Do not transplant regulatory traffic-light thresholds to an inapplicable internal measure.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for jurisdiction, model use, confidence level, sample window, and approved escalation thresholds.; do not infer use-institution-specific-policy from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to apply traffic-light or institutional policy.

## Select expected-shortfall backtest

Use observable evidence to select expected-shortfall backtest without preselecting the result.

### Inputs

- es forecast information (required): VaR/ES forecasts, tail observations, assumed distribution or simulation capability, and test objective.

### Rules

#### Direct Es Tests

- Conditions: es forecast information equals only VaR and ES sequences available.
- Rationale: Direct ES tests can assess tail severity without requiring a full forecast distribution.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for var/es forecasts, tail observations, assumed distribution or simulation capability, and test objective.; do not infer direct-es-tests from provider availability.

#### Simulation Based Es Tests

- Conditions: es forecast information equals full conditional distribution can be simulated.
- Rationale: Simulation-based tests assess ES against the model's conditional tail distribution.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for var/es forecasts, tail observations, assumed distribution or simulation capability, and test objective.; do not infer simulation-based-es-tests from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select expected-shortfall backtest.

## Diagnose backtest failure

Use observable evidence to diagnose backtest failure without preselecting the result.

### Inputs

- failure pattern evidence (required): Exception count, clustering, tail severity, volatility regime, P&L unexplained components, risk-factor gaps, and model changes.

### Rules

#### Calibration Or Level Diagnosis

- Conditions: failure pattern evidence equals frequency bias without clustering.
- Rationale: Systematic exception frequency may indicate level or volatility calibration weakness.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for exception count, clustering, tail severity, volatility regime, p&l unexplained components, risk-factor gaps, and model changes.; do not infer calibration-or-level-diagnosis from provider availability.

#### Structural Or Regime Diagnosis

- Conditions: failure pattern evidence equals clustered exceptions or severe ES misses.
- Rationale: Clustering or tail-severity failures suggest dynamics, tail, coverage, or regime weaknesses beyond simple scaling.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for exception count, clustering, tail severity, volatility regime, p&l unexplained components, risk-factor gaps, and model changes.; do not infer structural-or-regime-diagnosis from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to diagnose backtest failure.

## Determine backtesting disposition

Use observable evidence to determine backtesting disposition without preselecting the result.

### Inputs

- combined backtest evidence (required): P&L integrity, test results, power, policy zones, ES evidence, root cause, materiality, and prior failures.

### Rules

#### Pass Backtest

- Conditions: combined backtest evidence equals tests support model with no material control defect.
- Rationale: PASS requires a complete and correctly scoped test suite, not zero exceptions.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for p&l integrity, test results, power, policy zones, es evidence, root cause, materiality, and prior failures.; do not infer pass-backtest from provider availability.

#### Remediate Limit Or Redevelop

- Conditions: combined backtest evidence equals material failure with diagnosable remedy.
- Rationale: Material failures route to recalibration, redevelopment, use limitation, or escalation based on root cause and policy.
- Applies to: Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract..
- Excludes: VaR or ES estimation, forecast alteration.
- If information is missing: Stop this decision and obtain evidence for p&l integrity, test results, power, policy zones, es evidence, root cause, materiality, and prior failures.; do not infer remediate-limit-or-redevelop from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine backtesting disposition.
