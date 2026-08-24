# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Set CDS analysis purpose and prohibited actions

- Source: International Swaps and Derivatives Association, *Credit derivatives overview and market infrastructure*
- Locator: section: CDS market purpose and standard model
- Source ID: ISDA-CREDIT-DERIVATIVES-OVERVIEW
- Authority: T3 (current)
- Applicability: international-market; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Valuation computes contract-consistent price or spread without recommending a trade.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model purpose and output interpretation
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Market-implied credit risk is not a physical default forecast without a separate risk-premium methodology.

## Identify contract and credit-event conventions

- Source: International Swaps and Derivatives Association, *2014 ISDA Credit Derivatives Definitions and related material*
- Locator: section: Standard terms, credit events, and settlement
- Source ID: ISDA-CDS-DEFINITIONS-2014
- Authority: T3 (current)
- Applicability: international-market; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: The contract must be mapped to applicable standard terms and confirmation before cash flows are valued.

- Source: International Swaps and Derivatives Association, *ISDA derivatives glossary*
- Locator: section: Credit derivative contract terminology
- Source ID: ISDA-DERIVATIVES-GLOSSARY
- Authority: T3 (current)
- Applicability: international-market; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Material contract ambiguity requires legal or operations clarification; analytics must not invent terms.

## Select discount and credit curves

- Source: MathWorks, *Price credit default swaps*
- Locator: section: Zero curve and default probability inputs
- Source ID: MATHWORKS-CDS-PRICE
- Authority: T5 (current)
- Applicability: implementation; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Discount and credit curves must share the valuation date, currency conventions, and support the contract maturity.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select discount and credit curves
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Professional selection for select discount and credit curves must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: MathWorks, *Bootstrap default probability curve from bond prices*
- Locator: section: Curve construction and tenor coverage
- Source ID: MATHWORKS-BOND-DEFAULT-CURVE
- Authority: T5 (current)
- Applicability: implementation; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: A curve mismatch returns to the curve workflow; it is not repaired inside CDS pricing.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select discount and credit curves
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Professional selection for select discount and credit curves must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Set recovery and settlement assumptions

- Source: International Swaps and Derivatives Association, *2014 ISDA Credit Derivatives Definitions and related material*
- Locator: section: Recovery and settlement provisions
- Source ID: ISDA-CDS-DEFINITIONS-2014
- Authority: T3 (current)
- Applicability: international-market; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: A fixed recovery input must be disclosed because it materially affects hazard and valuation.

- Source: International Swaps and Derivatives Association, *Credit derivatives overview and market infrastructure*
- Locator: section: Standard model recovery assumptions
- Source ID: ISDA-CREDIT-DERIVATIVES-OVERVIEW
- Authority: T3 (current)
- Applicability: international-market; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Uncertain recovery requires sensitivity or contract-specific evidence rather than silent market default.

## Determine price spread or implied-risk route

- Source: MathWorks, *Price credit default swaps*
- Locator: section: CDS price calculation
- Source ID: MATHWORKS-CDS-PRICE
- Authority: T5 (current)
- Applicability: implementation; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Given curves and terms, compute value or par spread under the specified contract.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Determine price spread or implied-risk route
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Professional selection for determine price spread or implied-risk route must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: MathWorks, *Compute credit default swap spread*
- Locator: section: CDS spread and curve relationship
- Source ID: MATHWORKS-CDS-SPREAD
- Authority: T5 (current)
- Applicability: implementation; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Market spreads may calibrate implied hazard only with consistent recovery and discount assumptions.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Determine price spread or implied-risk route
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Professional selection for determine price spread or implied-risk route must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Select CDS risk sensitivities

- Source: MathWorks, *Price credit default swaps*
- Locator: section: Pricing inputs and valuation changes
- Source ID: MATHWORKS-CDS-PRICE
- Authority: T5 (current)
- Applicability: implementation; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Valuation analysis should quantify material curve and recovery sensitivities without converting them into hedging advice.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select CDS risk sensitivities
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Professional selection for select cds risk sensitivities must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: MathWorks, *Compute credit default swap spread*
- Locator: section: Spread sensitivity to default probabilities
- Source ID: MATHWORKS-CDS-SPREAD
- Authority: T5 (current)
- Applicability: implementation; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Implied-risk analysis should show dependence on recovery and interpolation assumptions.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select CDS risk sensitivities
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Professional selection for select cds risk sensitivities must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Reconcile valuation to market quote

- Source: International Swaps and Derivatives Association, *2014 ISDA Credit Derivatives Definitions and related material*
- Locator: section: Premium, settlement, and standard terms
- Source ID: ISDA-CDS-DEFINITIONS-2014
- Authority: T3 (current)
- Applicability: international-market; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: A reconciled result identifies every material convention and market input difference.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Process verification and model controls
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Unexplained differences require investigation before the result is reported.

## Determine CDS analysis disposition

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Documentation and model use
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Report the valuation or implied-risk result with market date, conventions, sensitivities, and limitations.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Limitations and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use.
- Interpretation: Material contract or valuation defects block an unqualified CDS conclusion.
