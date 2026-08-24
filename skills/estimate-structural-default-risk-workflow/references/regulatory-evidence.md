# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Define default boundary and liability mapping

- Source: MathWorks, *Merton structural default model*
- Locator: section: Liability and default point inputs
- Source ID: MATHWORKS-MERTON-MODEL
- Authority: T5 (current)
- Applicability: implementation; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: The default boundary must be documented from liabilities rather than assumed from equity value alone.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model assumptions and limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Professional selection for define default boundary and liability mapping must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model assumptions and limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Complex liabilities require boundary scenarios and explicit limitation because one debt proxy is not identifiable.

## Set structural risk horizon

- Source: MathWorks, *Merton structural default model*
- Locator: section: Model horizon and probability outputs
- Source ID: MATHWORKS-MERTON-MODEL
- Authority: T5 (current)
- Applicability: implementation; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: A point-in-time estimate is aligned to one valuation date and selected horizon.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Set structural risk horizon
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Professional selection for set structural risk horizon must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: MathWorks, *Merton model by time series*
- Locator: section: Time-series structural calibration
- Source ID: MATHWORKS-MERTON-TIME-SERIES
- Authority: T5 (current)
- Applicability: implementation; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: A time-series design is required when asset value and default risk must evolve with market observations.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Set structural risk horizon
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Professional selection for set structural risk horizon must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Select equity-volatility input

- Source: MathWorks, *Merton structural default model*
- Locator: section: Equity volatility input
- Source ID: MATHWORKS-MERTON-MODEL
- Authority: T5 (current)
- Applicability: implementation; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Historical volatility may be used when the window represents current risk and is robust to corporate events.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Sensitivity and changing conditions
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Professional selection for select equity-volatility input must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Sensitivity and changing conditions
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Regime uncertainty requires alternative windows or implied measures and sensitivity rather than one mechanical estimate.

## Calibrate asset value and asset volatility

- Source: MathWorks, *Merton structural default model*
- Locator: section: Asset value and volatility solution
- Source ID: MATHWORKS-MERTON-MODEL
- Authority: T5 (current)
- Applicability: implementation; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: A valid solution must satisfy equity-value and volatility relationships with stable, economically plausible parameters.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Implementation verification and model limitations
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Professional selection for calibrate asset value and asset volatility must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Implementation verification and model limitations
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Unstable calibration requires changed inputs, constraints, or limitation; solver completion is not validation.

## Assess market and capital-structure representativeness

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Data quality and model use
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Structural output is meaningful only for a current, internally consistent market and liability snapshot.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Data and model controls
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Stale or inconsistent market data require repair or stopping rather than false precision.

## Assess structural-model sensitivity

- Source: MathWorks, *Merton model by time series*
- Locator: section: Sensitivity of structural estimates over time
- Source ID: MATHWORKS-MERTON-TIME-SERIES
- Authority: T5 (current)
- Applicability: implementation; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Robustness across credible input ranges supports directional use while retaining structural assumptions.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model uncertainty and limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Professional selection for assess structural-model sensitivity must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model uncertainty and limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Dominant input uncertainty requires a range and use limitation rather than a single default probability.

## Determine structural-risk disposition

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Validation and documentation
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Report distance-to-default and probability with market date, boundary, horizon, assumptions, and limitations.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model limitations and use restrictions
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Merton-style structural credit-risk estimation from equity, liability, interest-rate, and market-volatility information.
- Interpretation: Material identification or data failure prevents an unqualified point estimate.
