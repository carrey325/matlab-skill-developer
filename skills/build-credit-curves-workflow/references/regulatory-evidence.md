# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Determine curve purpose and probability interpretation

- Source: International Swaps and Derivatives Association, *Credit derivatives overview and market infrastructure*
- Locator: section: CDS market and standard model context
- Source ID: ISDA-CREDIT-DERIVATIVES-OVERVIEW
- Authority: T3 (current)
- Applicability: international-market; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Market prices imply risk-neutral default compensation and must not be presented as a physical forecast.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model purpose and output use
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: A physical forecast belongs in a PD development workflow rather than being inferred from traded spreads without adjustment.

## Select calibration instruments and quotes

- Source: MathWorks, *Bootstrap default probability curve from bond prices*
- Locator: section: Bond default probability bootstrap inputs
- Source ID: MATHWORKS-BOND-DEFAULT-CURVE
- Authority: T5 (current)
- Applicability: implementation; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Bonds may support curve bootstrapping when cash flows, seniority, optionality, and discounting are controlled.

- Source: International Swaps and Derivatives Association, *2014 ISDA Credit Derivatives Definitions and related material*
- Locator: section: Standard CDS terms and credit events
- Source ID: ISDA-CDS-DEFINITIONS-2014
- Authority: T3 (current)
- Applicability: international-market; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Professional selection for select calibration instruments and quotes must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: International Swaps and Derivatives Association, *2014 ISDA Credit Derivatives Definitions and related material*
- Locator: section: Standard CDS terms and credit events
- Source ID: ISDA-CDS-DEFINITIONS-2014
- Authority: T3 (current)
- Applicability: international-market; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Standard CDS spreads support hazard calibration when contract conventions and recovery are consistent.

## Freeze contract and market conventions

- Source: International Swaps and Derivatives Association, *2014 ISDA Credit Derivatives Definitions and related material*
- Locator: section: Standard terms, settlement, and credit events
- Source ID: ISDA-CDS-DEFINITIONS-2014
- Authority: T3 (current)
- Applicability: international-market; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Calibration requires conventions that reproduce instrument cash flows and quoted spreads.

- Source: International Swaps and Derivatives Association, *ISDA derivatives glossary*
- Locator: section: Credit derivative and market convention definitions
- Source ID: ISDA-DERIVATIVES-GLOSSARY
- Authority: T3 (current)
- Applicability: international-market; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Unknown or mixed conventions require repair or separate curves; silent defaults create false calibration accuracy.

## Set recovery assumption or recovery calibration

- Source: International Swaps and Derivatives Association, *Credit derivatives overview and market infrastructure*
- Locator: section: CDS standard model and recovery assumptions
- Source ID: ISDA-CREDIT-DERIVATIVES-OVERVIEW
- Authority: T3 (current)
- Applicability: international-market; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: A fixed recovery assumption must be disclosed because hazard and recovery are not separately identified from limited spreads.

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Recovery and default modelling
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Recovery may be calibrated only when independent data make it identifiable and stable.

## Select discount curve and currency treatment

- Source: MathWorks, *Price credit default swaps*
- Locator: section: Discount curve and CDS cash-flow inputs
- Source ID: MATHWORKS-CDS-PRICE
- Authority: T5 (current)
- Applicability: implementation; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Credit calibration must use a discount curve consistent with instrument currency and valuation conventions.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model inputs and implementation controls
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Professional selection for select discount curve and currency treatment must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model inputs and implementation controls
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: A discount mismatch biases inferred default rates and must be repaired before credit calibration.

## Choose calibration objective and constraints

- Source: MathWorks, *Bootstrap default probability curve from bond prices*
- Locator: section: Bootstrap constraints and outputs
- Source ID: MATHWORKS-BOND-DEFAULT-CURVE
- Authority: T5 (current)
- Applicability: implementation; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Calibration should preserve nonnegative hazards and non-increasing survival while explaining residual quote error.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model limitations and implementation verification
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Professional selection for choose calibration objective and constraints must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model limitations and implementation verification
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: An economically inconsistent fit requires quote cleaning, revised assumptions, or rejection—not acceptance of negative default intensity.

## Select interpolation and extrapolation policy

- Source: MathWorks, *Bootstrap default probability curve from bond prices*
- Locator: section: Default curve interpolation
- Source ID: MATHWORKS-BOND-DEFAULT-CURVE
- Authority: T5 (current)
- Applicability: implementation; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Interpolation may be used inside supported tenor ranges with shape and repricing checks.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Extrapolation and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Professional selection for select interpolation and extrapolation policy must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Extrapolation and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Extrapolation requires an approved tail rule, sensitivity, and explicit use limitation.

## Validate repricing and curve consistency

- Source: MathWorks, *Compute credit default swap spread*
- Locator: section: Spread calculation and curve inputs
- Source ID: MATHWORKS-CDS-SPREAD
- Authority: T5 (current)
- Applicability: implementation; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Curve use requires both quote fit and economically coherent probability shape.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Model validation and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Professional selection for validate repricing and curve consistency must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Model validation and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Material repricing or probability-shape failure blocks curve release.

## Determine credit-curve disposition

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Documentation and model use
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: A curve is released with valuation date, instruments, assumptions, diagnostics, and tenor limits.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Limitations and model risk management
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Default-probability, survival, hazard, or spread curve construction for valuation and market-implied credit-risk analysis.
- Interpretation: Material quote, recovery, or extrapolation weakness requires use limitation or rejection.
