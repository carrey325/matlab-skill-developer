# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Define the modeled credit event

- Source: European Banking Authority, *Guidelines on the application of the definition of default*
- Locator: section: Definition and application of default
- Source ID: EBA-DEFINITION-OF-DEFAULT-2026
- Authority: T2 (current)
- Applicability: european-union; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: A binary target is appropriate when one clearly defined default event drives the intended output.

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Rating states and model outputs
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Multiple states require an explicit taxonomy; state probabilities must not be relabelled as default probabilities.

## Select prediction horizon and output semantics

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model purpose and output interpretation
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: A fixed-horizon probability matches a single future performance window when observations and use align.

- Source: Irving Fisher Committee on Central Bank Statistics, *Bank failure prediction - a two-step survival time approach*
- Locator: section: Two-step survival-time methodology
- Source ID: IFC-DISCRETE-SURVIVAL
- Authority: T4 (current)
- Applicability: methodology; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Censoring and varying follow-up require survival or hazard modelling rather than fixed-window deletion.

## Choose binary, ordinal, or nominal structure

- Source: Basel Committee on Banking Supervision, *Credit risk modelling current practices and applications*
- Locator: section: Internal rating grades and risk differentiation
- Source ID: BCBS-CREDIT-RISK-MODELLING-1999
- Authority: T4 (current)
- Applicability: methodology; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: An ordinal candidate uses the state ordering while requiring proportionality or alternative assumptions to be assessed.

- Source: European Central Bank Banking Supervision, *Guide to internal models*
- Locator: section: Rating systems, grades, and risk differentiation
- Source ID: ECB-INTERNAL-MODELS
- Authority: T2 (current)
- Applicability: european-union; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Nominal modelling is required when imposing order would create unsupported probability relationships.

## Determine panel, snapshot, or event-history data design

- Source: Reserve Bank of Australia, *Why Do Companies Fail - Modelling Approach*
- Locator: section: Panel and survival modelling design
- Source ID: RBA-SURVIVAL-METHODS
- Authority: T4 (current)
- Applicability: methodology; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Repeated observations require time ordering, leakage controls, and dependence-aware validation.

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Data and sample validation
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: A snapshot design is appropriate only when independence and timing assumptions are supportable.

## Select statistical or nonlinear candidate family

- Source: MathWorks, *creditscorecard*
- Locator: section: Interpretable logistic credit modelling
- Source ID: MATHWORKS-CREDITSCORECARD
- Authority: T5 (current)
- Applicability: implementation; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Transparent statistical candidates should anchor comparison when they explain the signal adequately.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model complexity, benchmarking, and validation
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Professional selection for select statistical or nonlinear candidate family must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model complexity, benchmarking, and validation
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: A nonlinear challenger is justified only when out-of-sample gains, stability, and explanation burden are addressed.

## Treat class imbalance and rare states

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Data representativeness and model outcomes
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Weighting or resampling may be studied, but probability calibration must return to the target population.

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Sample adequacy and validation limitations
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Sparse states require defensible combination, more data, or stopping; synthetic balance cannot create information.

## Set interpretability and benchmark requirements

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model use, governance, and effective challenge
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: High-stakes uses require an interpretable primary model or a demonstrably faithful explanation framework.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Benchmarking and model complexity
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: A complex model still requires a transparent benchmark, sensitivity evidence, and documented limitations.

## Determine default-model disposition

- Source: MathWorks, *Compare Logistic Lifetime PD Model to Champion Model*
- Locator: section: Champion-challenger comparison
- Source ID: MATHWORKS-CHAMPION-CHALLENGER
- Authority: T5 (current)
- Applicability: implementation; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: The selected model may proceed when gains over benchmark are stable and class-level weaknesses are controlled.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Outcomes analysis and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: Professional selection for determine default-model disposition must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Outcomes analysis and model limitations
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional default or credit-state model development when neither an interpretable scorecard delivery nor a lifetime-PD term structure is the primary task.
- Interpretation: An apparent metric winner is rejected when instability, leakage, or weak rationale outweighs development performance.
