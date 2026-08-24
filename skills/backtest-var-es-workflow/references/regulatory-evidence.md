# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Reconcile forecasts with realised P&L

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Comparison of daily VaR with trading outcomes
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Backtesting requires each ex ante forecast to align with the subsequent controlled P&L observation.

- Source: MathWorks, *VaR backtesting workflow*
- Locator: section: Backtest data and time alignment
- Source ID: MATHWORKS-VAR-BACKTEST-WORKFLOW
- Authority: T5 (current)
- Applicability: implementation; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Misaligned forecasts and P&L invalidate exception counts and must be repaired first.

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Comparison of daily VaR with trading outcomes
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Professional selection for reconcile forecasts with realised p&l must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Define VaR exceptions

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Definition and counting of exceptions
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Exceptions must be counted consistently from the frozen risk and P&L convention.

- Source: MathWorks, *VaR backtesting workflow*
- Locator: section: VaR failures and portfolio data
- Source ID: MATHWORKS-VAR-BACKTEST-WORKFLOW
- Authority: T5 (current)
- Applicability: implementation; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Do not count exceptions until sign and P&L conventions are resolved.

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Definition and counting of exceptions
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Professional selection for define var exceptions must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Select VaR test family

- Source: MathWorks, *VaR backtesting workflow*
- Locator: section: Binomial and proportion-of-failures tests
- Source ID: MATHWORKS-VAR-BACKTEST-WORKFLOW
- Authority: T5 (current)
- Applicability: implementation; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Frequency tests assess whether exception proportion matches the forecast confidence level.

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Statistical interpretation of backtesting results
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Professional selection for select var test family must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Statistical interpretation of backtesting results
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Independence or conditional coverage tests are needed when exceptions cluster through time.

## Assess sample size and test power

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Sample and exception interpretation
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Test conclusions must reflect expected exception counts and statistical power.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Data limitations and validation uncertainty
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: A weak or mixed sample requires limitations and supplementary evidence, not an automatic pass.

## Apply traffic-light or institutional policy

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Supervisory interpretation and zones
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Traffic-light classification is used only under its applicable framework and sample convention.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model use and policy governance
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Do not transplant regulatory traffic-light thresholds to an inapplicable internal measure.

## Select expected-shortfall backtest

- Source: MathWorks, *Expected shortfall estimation and backtesting*
- Locator: section: esbacktest inputs and tests
- Source ID: MATHWORKS-ES-BACKTEST-WORKFLOW
- Authority: T5 (current)
- Applicability: implementation; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Direct ES tests can assess tail severity without requiring a full forecast distribution.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select expected-shortfall backtest
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Professional selection for select expected-shortfall backtest must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: MathWorks, *Expected shortfall estimation and backtesting*
- Locator: section: Simulation-based ES backtesting
- Source ID: MATHWORKS-ES-BACKTEST-WORKFLOW
- Authority: T5 (current)
- Applicability: implementation; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Simulation-based tests assess ES against the model's conditional tail distribution.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select expected-shortfall backtest
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Professional selection for select expected-shortfall backtest must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Diagnose backtest failure

- Source: Bank of England, *Filtered historical simulation VaR models and their competitors*
- Locator: section: VaR dynamics and testing
- Source ID: BOE-FILTERED-HISTORICAL-VAR-2015
- Authority: T4 (current)
- Applicability: methodology; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Systematic exception frequency may indicate level or volatility calibration weakness.

- Source: Basel Committee on Banking Supervision, *Minimum capital requirements for market risk*
- Locator: section: Backtesting and model eligibility
- Source ID: BCBS-MARKET-RISK-2019
- Authority: T1 (current)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Clustering or tail-severity failures suggest dynamics, tail, coverage, or regime weaknesses beyond simple scaling.

## Determine backtesting disposition

- Source: Basel Committee on Banking Supervision, *Minimum capital requirements for market risk*
- Locator: section: Backtesting requirements
- Source ID: BCBS-MARKET-RISK-2019
- Authority: T1 (current)
- Applicability: international; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: PASS requires a complete and correctly scoped test suite, not zero exceptions.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Validation findings and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Independent or second-line testing of supplied VaR and ES forecast series for a defined portfolio and approved risk-measure contract.
- Interpretation: Material failures route to recalibration, redevelopment, use limitation, or escalation based on root cause and policy.
