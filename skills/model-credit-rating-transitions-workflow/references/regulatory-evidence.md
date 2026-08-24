# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Define rating states and ordering

- Source: European Central Bank Banking Supervision, *Guide to internal models*
- Locator: section: Rating grades and assignment consistency
- Source ID: ECB-INTERNAL-MODELS
- Authority: T2 (current)
- Applicability: european-union; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: An ordered state space requires consistent grade meaning over the observation history.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Data changes and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Material taxonomy changes require mapping, separate regimes, or a shorter history before transition estimation.

## Select cohort or duration estimator

- Source: MathWorks, *Estimate transition probability matrix*
- Locator: section: Cohort transition probability estimation
- Source ID: MATHWORKS-TRANSITION-PROBABILITIES
- Authority: T5 (current)
- Applicability: implementation; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: A cohort estimator matches snapshot observations but must define multiple transitions and withdrawals.

- Source: Reserve Bank of Australia, *Why Do Companies Fail - Modelling Approach*
- Locator: section: Event-history and duration modelling
- Source ID: RBA-SURVIVAL-METHODS
- Authority: T4 (current)
- Applicability: methodology; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Professional selection for select cohort or duration estimator must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Reserve Bank of Australia, *Why Do Companies Fail - Modelling Approach*
- Locator: section: Event-history and duration modelling
- Source ID: RBA-SURVIVAL-METHODS
- Authority: T4 (current)
- Applicability: methodology; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Duration methods use time at risk and exact transitions when event timing is trustworthy.

## Set default and withdrawal treatment

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Default and internal rating states
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Default is represented as absorbing when the use treats post-default movements outside the migration process.

- Source: European Banking Authority, *Guidelines on PD estimation LGD estimation and treatment of defaulted assets*
- Locator: section: Defaulted assets and return to non-defaulted status
- Source ID: EBA-PD-LGD
- Authority: T2 (current)
- Applicability: european-union; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Cure and post-default behaviour require explicit states rather than breaking probability conservation.

## Convert transition horizon

- Source: MathWorks, *Estimate transition probability matrix*
- Locator: section: Transition matrix interval conversion
- Source ID: MATHWORKS-TRANSITION-PROBABILITIES
- Authority: T5 (current)
- Applicability: implementation; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Horizon conversion requires a supportable time-homogeneity or generator assumption.

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Conditional and unconditional credit models
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Professional selection for convert transition horizon must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Conditional and unconditional credit models
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Regime-varying transitions should not be produced by mechanically powering one unconditional matrix.

## Treat sparse transitions and rare states

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Sample adequacy and rating-grade validation
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Constrained smoothing may reduce sampling noise while preserving probability and rating order.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Data adequacy and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: An unsupported state requires defensible merging, limitation, or exclusion rather than synthetic transitions.

## Calibrate transition and default rates

- Source: MathWorks, *modelCalibration for Lifetime PD Models*
- Locator: section: Calibration and observed-versus-predicted comparison
- Source ID: MATHWORKS-PD-CALIBRATION
- Authority: T5 (current)
- Applicability: implementation; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Calibration requires probability conservation and reconciliation to observed or approved targets.

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Calibration validation
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Professional selection for calibrate transition and default rates must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Calibration validation
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Material marginal bias requires re-estimation or explicit calibration without distorting state ordering.

## Determine stressed transition treatment

- Source: European Banking Authority, *2025 EU-wide stress test methodological note*
- Locator: section: Credit migration and stress projections
- Source ID: EBA-STRESS-METHODOLOGY-2025
- Authority: T2 (current)
- Applicability: european-union; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Stress transitions may use validated conditional relationships that preserve row probabilities and sensible deterioration.

- Source: Basel Committee on Banking Supervision, *Stress testing principles*
- Locator: section: Stress models and expert judgment
- Source ID: BCBS-STRESS-TESTING-2018
- Authority: T2 (current)
- Applicability: international; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Use transparent sensitivity matrices and limitations rather than claiming a calibrated scenario model.

## Determine transition-model disposition

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model validation and use
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: A usable matrix must reconcile, remain stable enough for its use, and disclose sparse-state uncertainty.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Model limitations and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Cohort, duration, discrete-time, or generator-based transition estimation for internal ratings or market credit states.
- Interpretation: Taxonomy or horizon failures require respecification, not a cosmetic matrix repair.
