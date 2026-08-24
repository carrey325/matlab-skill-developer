# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Select default-mode or migration-mode loss

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Default-mode and mark-to-market approaches
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Default-mode analysis is appropriate when loss is driven by default occurrence and recovery over the horizon.

- Source: MathWorks, *creditMigrationCopula model*
- Locator: section: Migration portfolio model and valuation states
- Source ID: MATHWORKS-CREDIT-MIGRATION-COPULA
- Authority: T5 (current)
- Applicability: implementation; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Migration-mode analysis is required when non-default rating changes materially affect value.

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Default-mode and mark-to-market approaches
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Professional selection for select default-mode or migration-mode loss must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Set horizon and tail probability

- Source: Basel Committee on Banking Supervision, *Range of practices and issues in economic capital frameworks*
- Locator: section: Economic capital horizon and confidence practices
- Source ID: BCBS-ECONOMIC-CAPITAL-2009
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: A one-year horizon may align with internal capital assessment when exposures and parameters are consistently defined.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model purpose and use
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: A shorter horizon requires transition, exposure, and liquidity assumptions consistent with that decision use.

## Assess portfolio parameter compatibility

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Credit risk parameter definitions and aggregation
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Portfolio aggregation requires compatible parameter semantics and exposure timing.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model use and data lineage
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Mismatched PD, LGD, EAD, transition, or exposure snapshots must be repaired before simulation.

## Select dependence structure

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Dependence and aggregation approaches
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: A factor or ASRF structure is supportable when common drivers and granularity assumptions are evidenced.

- Source: Basel Committee on Banking Supervision, *Studies on credit risk concentration*
- Locator: section: Sector concentration and contagion
- Source ID: BCBS-CREDIT-CONCENTRATION-2006
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Residual dependence and concentration require richer factors, adjustment, or explicit limitation.

## Assess name and sector concentration

- Source: Basel Committee on Banking Supervision, *Supervisory framework for measuring and controlling large exposures*
- Locator: section: Connected counterparties and large exposure measurement
- Source ID: BCBS-LARGE-EXPOSURES-2014
- Authority: T1 (current)
- Applicability: international; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Single-name and connected-group concentrations require explicit measurement and cannot be diversified away by model size.

- Source: Basel Committee on Banking Supervision, *Studies on credit risk concentration*
- Locator: section: Sectoral concentration measurement
- Source ID: BCBS-CREDIT-CONCENTRATION-2006
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Sector and geographic concentration require systematic-factor and contribution analysis.

## Judge simulation precision and tail stability

- Source: Bank for International Settlements, *Modelling and calibration errors in measures of portfolio credit risk*
- Locator: section: Simulation and calibration error in tail risk
- Source ID: BIS-PORTFOLIO-CALIBRATION-2007
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Tail results require reproducible convergence evidence, not a single large simulation run.

- Source: MathWorks, *creditDefaultCopula model*
- Locator: section: Simulation and confidence-band diagnostics
- Source ID: MATHWORKS-CREDIT-DEFAULT-COPULA
- Authority: T5 (current)
- Applicability: implementation; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Unstable tail estimates require more scenarios, variance reduction, or model redesign before reporting.

- Source: Bank for International Settlements, *Modelling and calibration errors in measures of portfolio credit risk*
- Locator: section: Simulation and calibration error in tail risk
- Source ID: BIS-PORTFOLIO-CALIBRATION-2007
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Professional selection for judge simulation precision and tail stability must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Determine EL UL and economic-capital output

- Source: Basel Committee on Banking Supervision, *Range of practices and issues in economic capital frameworks*
- Locator: section: Economic capital definitions and use
- Source ID: BCBS-ECONOMIC-CAPITAL-2009
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Economic capital is a policy-governed tail-loss measure, commonly derived from unexpected loss, and must not be labelled regulatory capital.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model output use and governance
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Report the loss distribution and tail measures without inventing an economic-capital number.

## Select risk contribution and diversification attribution

- Source: MathWorks, *creditDefaultCopula model*
- Locator: section: Risk contribution output
- Source ID: MATHWORKS-CREDIT-DEFAULT-COPULA
- Authority: T5 (current)
- Applicability: implementation; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Component contributions support portfolio attribution when they reconcile to the chosen risk measure.

- Source: Bank for International Settlements, *Modelling and calibration errors in measures of portfolio credit risk*
- Locator: section: Model and calibration uncertainty
- Source ID: BIS-PORTFOLIO-CALIBRATION-2007
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Professional selection for select risk contribution and diversification attribution must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Bank for International Settlements, *Modelling and calibration errors in measures of portfolio credit risk*
- Locator: section: Model and calibration uncertainty
- Source ID: BIS-PORTFOLIO-CALIBRATION-2007
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: When allocation is unstable or non-additive, report sensitivities and limitations rather than false precision.

## Determine portfolio-risk reportability

- Source: Basel Committee on Banking Supervision, *Range of practices and issues in economic capital frameworks*
- Locator: section: Economic capital validation and use
- Source ID: BCBS-ECONOMIC-CAPITAL-2009
- Authority: T4 (current)
- Applicability: methodology; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Reportable results require sensitivity and limitation disclosure alongside point estimates.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model limitations and use restrictions
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose.
- Interpretation: Material dependence or convergence uncertainty requires limitation, remediation, or rejection of the affected output.
