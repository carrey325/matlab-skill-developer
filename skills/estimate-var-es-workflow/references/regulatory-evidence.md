# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Determine VaR and ES use

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model purpose and use
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Internal use may choose horizon and confidence under approved policy while retaining method and limitation transparency.

- Source: Basel Committee on Banking Supervision, *Minimum capital requirements for market risk*
- Locator: section: Internal models approach and expected shortfall
- Source ID: BCBS-MARKET-RISK-2019
- Authority: T1 (current)
- Applicability: international; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Capital support must follow the applicable market-risk framework, including ES and model eligibility requirements.

## Define portfolio and P&L measure

- Source: Basel Committee on Banking Supervision, *Minimum capital requirements for market risk*
- Locator: section: Trading desk P&L and model requirements
- Source ID: BCBS-MARKET-RISK-2019
- Authority: T1 (current)
- Applicability: international; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: A fixed-position risk-theoretical P&L isolates modeled market moves and supports consistent estimation.

- Source: Basel Committee on Banking Supervision, *Supervisory framework for backtesting market risk models*
- Locator: section: Trading outcomes for model comparison
- Source ID: BCBS-VAR-BACKTEST-1996
- Authority: T2 (historical)
- Applicability: international; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Actual P&L requires reconciliation and separation of fees, intraday, reserves, and non-model effects.

## Set horizon and confidence level

- Source: Bank of England, *Filtered historical simulation VaR models and their competitors*
- Locator: section: VaR purpose, horizon, and conditional estimation
- Source ID: BOE-FILTERED-HISTORICAL-VAR-2015
- Authority: T4 (current)
- Applicability: methodology; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: A one-day measure is appropriate only when aligned to the portfolio, valuation, and approved confidence policy.

- Source: Basel Committee on Banking Supervision, *Minimum capital requirements for market risk*
- Locator: section: Expected shortfall and liquidity horizons
- Source ID: BCBS-MARKET-RISK-2019
- Authority: T1 (current)
- Applicability: international; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Applicable market-risk capital uses ES and prescribed liquidity-horizon aggregation rather than arbitrary square-root scaling.

## Select VaR and ES estimation method

- Source: Bank of England, *Filtered historical simulation VaR models and their competitors*
- Locator: section: Historical and filtered historical simulation
- Source ID: BOE-FILTERED-HISTORICAL-VAR-2015
- Authority: T4 (current)
- Applicability: methodology; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Historical simulation preserves empirical joint moves when history is representative and positions can be revalued.

- Source: MathWorks, *Compute value at risk values*
- Locator: section: Normal t and empirical VaR methods
- Source ID: MATHWORKS-VALUE-AT-RISK
- Authority: T5 (current)
- Applicability: implementation; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Parametric estimation requires validated distribution, volatility, and dependence assumptions.

- Source: Bank of England, *Filtered historical simulation VaR models and their competitors*
- Locator: section: Historical and filtered historical simulation
- Source ID: BOE-FILTERED-HISTORICAL-VAR-2015
- Authority: T4 (current)
- Applicability: methodology; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Professional selection for select var and es estimation method must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Treat nonlinear positions and risk factors

- Source: Basel Committee on Banking Supervision, *Minimum capital requirements for market risk*
- Locator: section: Risk factor and valuation model requirements
- Source ID: BCBS-MARKET-RISK-2019
- Authority: T1 (current)
- Applicability: international; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Material nonlinear exposures require full revaluation or a validated nonlinear approximation.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model simplification and validation
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: A linear approximation is supportable only when approximation error is tested under relevant moves.

## Select tail and volatility treatment

- Source: Bank of England, *Filtered historical simulation VaR models and their competitors*
- Locator: section: Filtered historical simulation and distribution properties
- Source ID: BOE-FILTERED-HISTORICAL-VAR-2015
- Authority: T4 (current)
- Applicability: methodology; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Heavy tails and volatility dynamics require conditional or heavy-tail treatment rather than a normal unconditional assumption.

- Source: Basel Committee on Banking Supervision, *Stress testing principles*
- Locator: section: Stress testing as complement to statistical measures
- Source ID: BCBS-STRESS-TESTING-2018
- Authority: T2 (current)
- Applicability: international; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Sparse tail data require stress scenarios and limitations; ES precision cannot be manufactured.

## Aggregate risk across positions and horizons

- Source: Basel Committee on Banking Supervision, *Minimum capital requirements for market risk*
- Locator: section: Portfolio aggregation and liquidity horizons
- Source ID: BCBS-MARKET-RISK-2019
- Authority: T1 (current)
- Applicability: international; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Portfolio VaR and ES should be computed from joint P&L when dependence and nonlinearities are material.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model inputs and use limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Incompatible component measures cannot be summed or diversified without an approved aggregation method.

## Judge estimate stability and plausibility

- Source: MathWorks, *Compute expected shortfall values*
- Locator: section: Expected shortfall methods and tail calculation
- Source ID: MATHWORKS-EXPECTED-SHORTFALL
- Authority: T5 (current)
- Applicability: implementation; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: A stable estimate proceeds to independent backtesting with diagnostics and assumptions intact.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Sensitivity analysis and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Professional selection for judge estimate stability and plausibility must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Sensitivity analysis and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Method-dominated results require respecification, ranges, or limitation before use.

## Determine VaR and ES estimation disposition

- Source: Basel Committee on Banking Supervision, *Minimum capital requirements for market risk*
- Locator: section: Model validation and backtesting requirements
- Source ID: BCBS-MARKET-RISK-2019
- Authority: T1 (current)
- Applicability: international; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Release includes horizon, confidence, P&L, method, diagnostics, limitations, and a backtesting handoff.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Model limitations and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Market-risk VaR and ES estimation for internal risk management or applicable market-risk capital support using controlled position, risk-factor, and P&L data.
- Interpretation: Material P&L or coverage gaps block an unqualified risk estimate.
