# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Determine EAD purpose and exposure convention

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: CRE: exposure at default and credit conversion factors
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Prudential EAD must follow the applicable exposure and conversion-factor framework rather than an accounting-period balance proxy.

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: EAD/CCF estimation scope and application
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Accounting-support EAD requires exposure profiles aligned to the ECL horizon and contractual behaviour.

## Define drawn and undrawn exposure components

- Source: European Central Bank Banking Supervision, *Guide to internal models*
- Locator: section: Credit risk data quality and EAD estimation
- Source ID: ECB-INTERNAL-MODELS
- Authority: T2 (current)
- Applicability: european-union; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: The target must reconcile exposure components and default timing before conversion behaviour is estimated.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Data quality, lineage, and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Missing facility histories make both EAD and CCF targets unreliable and require remediation.

## Choose product-specific EAD route

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Off-balance-sheet exposures and conversion factors
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Revolving commitments require modelling the conversion of undrawn availability into default exposure.

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: EAD estimation by facility type
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Amortising term facilities require balance-path projection rather than an undrawn-limit conversion model.

## Determine whether CCF is a stable target

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: CCF calculation and reference dates
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: CCF is meaningful when the undrawn denominator is positive, reliable, and aligned to the observation window.

- Source: European Central Bank Banking Supervision, *Guide to internal models*
- Locator: section: EAD estimation; margin of conservatism and data deficiencies
- Source ID: ECB-INTERNAL-MODELS
- Authority: T2 (current)
- Applicability: european-union; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Unstable denominators can produce extreme CCFs; direct EAD or a separate segment is required.

## Select the pre-default observation horizon

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: CRE: EAD reference period
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: A one-year prudential horizon requires reference dates and default linkage consistent with that horizon.

- Source: MathWorks, *Compute Expected Credit Loss for Lifetime PD Model*
- Locator: section: Lifetime ECL example; period exposure inputs
- Source ID: MATHWORKS-COX-ECL
- Authority: T5 (current)
- Applicability: implementation; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Lifetime use requires conditional exposure projections by period rather than one terminal EAD copied across horizons.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: CRE: EAD reference period
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Professional selection for select the pre-default observation horizon must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Treat limit changes and additional drawings

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: EAD risk drivers and reference data
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Material endogenous limit changes must be represented or controlled because they alter both denominator and future exposure.

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Validation of assumptions and representativeness
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: A fixed-limit assumption is acceptable only when supported by product terms and empirical history.

## Select EAD model family

- Source: MathWorks, *fitEADModel*
- Locator: section: Supported EAD model types and fitting inputs
- Source ID: MATHWORKS-FIT-EAD
- Authority: T5 (current)
- Applicability: implementation; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Regression candidates are appropriate when conditional mean behaviour and bounds can be validated.

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Exposure and credit conversion modelling practices
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Professional selection for select ead model family must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Exposure and credit conversion modelling practices
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Distinct behavioural regimes should be modelled separately when pooling would conceal different drawdown mechanisms.

## Control EAD and CCF boundary behaviour

- Source: European Central Bank Banking Supervision, *Guide to internal models*
- Locator: section: Model performance and estimation conservatism
- Source ID: ECB-INTERNAL-MODELS
- Authority: T2 (current)
- Applicability: european-union; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Predictions may proceed when economic bounds and any transformations are documented and empirically supported.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model limitations, controls, and use
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Material boundary violations require respecification or an explicit evidence-backed policy, not silent clipping.

## Determine EAD model disposition

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Outcomes analysis and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: A complete developer package can proceed when product-level calibration and assumptions support the use.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Validation findings and model redevelopment
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.
- Interpretation: Material product bias or unstable conversion behaviour requires remediation rather than pooled acceptance.
