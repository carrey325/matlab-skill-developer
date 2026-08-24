# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Determine LGD purpose and loss concept

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: CRE: internal ratings-based approach; LGD requirements
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Prudential LGD requires an economic-loss concept and regime-specific conservatism rather than an accounting allowance proxy.

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: Scope and estimation requirements for LGD
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Accounting-support LGD must preserve the governing allowance framework and cannot silently inherit prudential downturn treatment.

## Select workout or market LGD basis

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: Chapter 7 LGD estimation; realised LGD
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Complete recoveries, costs, and timing support workout LGD built from realised economic loss.

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: LGD and recovery-rate modelling practices
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Observable and representative market prices can support market LGD when workout histories are not the intended measurement basis.

## Define recoveries, costs, and discounting

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: Realised LGD components and discounting
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: LGD should use reconciled recovery and cost cash flows with timing retained for economic-loss measurement.

- Source: European Central Bank Banking Supervision, *Guide to internal models*
- Locator: section: Credit risk; data quality and LGD realised values
- Source ID: ECB-INTERNAL-MODELS
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Missing material cash flows or costs must be remediated before model fitting because the target itself is unreliable.

## Determine cure and return-to-performing treatment

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: Treatment of return to non-defaulted status
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: A material cured population requires explicit cure treatment so zero or low loss observations do not distort severity estimates.

- Source: European Banking Authority, *Guidelines on the application of the definition of default*
- Locator: section: Return to non-defaulted status and probation
- Source ID: EBA-DEFINITION-OF-DEFAULT-2026
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Unreliable cure identification requires repair or a documented limited-use treatment rather than assumed zero loss.

## Treat incomplete recovery and censoring

- Source: European Central Bank Banking Supervision, *Guide to internal models*
- Locator: section: LGD estimation; incomplete recovery processes
- Source ID: ECB-INTERNAL-MODELS
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Material open recovery cases require a censoring-aware or explicitly estimated incomplete-recovery treatment.

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: Recovery process length and incomplete cases
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: A resolved-case design is supportable only when the observation window captures the recovery process without material selection bias.

## Determine downturn calibration requirement

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: CRE: downturn LGD requirements
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Prudential LGD must reflect adverse economic conditions when losses and recoveries are materially cyclical.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model purpose, assumptions, limitations, and outcomes analysis
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Do not manufacture a downturn overlay outside its applicable purpose; retain sensitivity analysis and limitations.

## Select LGD segmentation

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: Risk differentiation and LGD segmentation
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Segments are warranted when economic loss drivers and recovery mechanisms differ materially and remain supportable in sample.

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Validation of rating-system segmentation and estimates
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Pooling with covariates or limitations is preferable to unstable micro-segments that cannot be calibrated.

## Select LGD model family

- Source: MathWorks, *Overview of Loss Given Default Models*
- Locator: section: Supported LGD model types and assumptions
- Source ID: MATHWORKS-LGD-OVERVIEW
- Authority: T5 (current)
- Applicability: implementation; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Bounded-response or regression candidates match continuous severity when boundary behaviour is explicitly controlled.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select LGD model family
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Professional selection for select lgd model family must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: MathWorks, *Model Loss Given Default*
- Locator: section: Two-stage LGD example and comparison
- Source ID: MATHWORKS-LGD-COMPARISON
- Authority: T5 (current)
- Applicability: implementation; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: A two-stage design separates cure probability from conditional loss severity when the outcome distribution is a genuine mixture.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select LGD model family
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Professional selection for select lgd model family must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Determine LGD model disposition

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model validation, outcomes analysis, and governance
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: A developer package may proceed only when performance and assumptions support the intended use; this is not independent approval.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Validation findings, limitations, and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.
- Interpretation: Material target, calibration, or stability weakness requires remediation or redevelopment rather than acceptance by metric averaging.
