# Regulatory Evidence

This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.

## Determine scorecard purpose and responsibility boundary

- Source: Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk*
- Locator: section: Credit-granting process and risk assessment
- Source ID: BCBS-CREDIT-RISK-PRINCIPLES-2025
- Authority: T1 (current)
- Applicability: international; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Application scorecards require an applicant population, observation outcome, and explicit separation from the final credit decision.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model purpose, use, and data representativeness
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Behavioural scorecards require performance windows and predictors available during account management.

## Define target and development population

- Source: European Central Bank Banking Supervision, *Guide to internal models*
- Locator: section: Default definition, data, and representativeness
- Source ID: ECB-INTERNAL-MODELS
- Authority: T2 (current)
- Applicability: european-union; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: A scorecard target is supportable only when outcome timing and population exclusions match intended use.

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Data representativeness and validation samples
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Material population mismatch requires redesign before binning because later validation cannot repair a biased target.

## Determine reject-inference treatment

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Data limitations, assumptions, and sensitivity analysis
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Selection bias must be assessed and any reject-inference assumptions challenged with sensitivity and limitations.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Data quality and model use limitations
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Observed outcomes may support development when selection effects are evidenced as immaterial.

## Select supervised binning treatment

- Source: MathWorks, *Credit Scorecard Modeling Workflow*
- Locator: section: Automatic and manual binning workflow
- Source ID: MATHWORKS-SCORECARD-WORKFLOW
- Authority: T5 (current)
- Applicability: implementation; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Ordered bins should preserve a stable interpretable risk gradient without manufacturing separation.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select supervised binning treatment
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Professional selection for select supervised binning treatment must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: MathWorks, *creditscorecard*
- Locator: section: Binning and predictor treatment
- Source ID: MATHWORKS-CREDITSCORECARD
- Authority: T5 (current)
- Applicability: implementation; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Sparse categories require evidence-based merging or exclusion rather than unstable standalone points.

- Source: Basel Committee on Banking Supervision, *The Basel Framework*
- Locator: section: Methodology and limitations relevant to Select supervised binning treatment
- Source ID: BASEL-FRAMEWORK-CURRENT
- Authority: T1 (current)
- Applicability: international; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Professional selection for select supervised binning treatment must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

## Determine monotonicity constraints

- Source: MathWorks, *Credit Scorecard Modeling Workflow*
- Locator: section: Binning maps and monotonic trends
- Source ID: MATHWORKS-SCORECARD-WORKFLOW
- Authority: T5 (current)
- Applicability: implementation; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Monotonicity is justified when economic ordering and stable outcome evidence agree.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Conceptual soundness and model assumptions
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Professional selection for determine monotonicity constraints must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Conceptual soundness and model assumptions
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: A stable explainable non-monotonic relationship may be retained; monotonicity must not be imposed solely for cosmetics.

## Select scorecard variables

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Model inputs, implementation, and validation
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Variables should add stable interpretable signal and be reproducible at scoring time.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model risk, limitations, and controls
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Predictive lift does not justify an unstable, unavailable, redundant, or prohibited variable.

## Set points scaling and reason-code interpretation

- Source: MathWorks, *creditscorecard*
- Locator: section: Score scaling and points computation
- Source ID: MATHWORKS-CREDITSCORECARD
- Authority: T5 (current)
- Applicability: implementation; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Scaling translates model log odds into points only after the institution approves odds, direction, and rounding conventions.

- Source: Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk*
- Locator: section: Transparent credit process and delegated authority
- Source ID: BCBS-CREDIT-RISK-PRINCIPLES-2025
- Authority: T1 (current)
- Applicability: international; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Professional selection for set points scaling and reason-code interpretation must be justified by the declared purpose, observable data properties, assumptions, diagnostics, and limitations; provider availability is not a selection criterion.

- Source: Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk*
- Locator: section: Transparent credit process and delegated authority
- Source ID: BCBS-CREDIT-RISK-PRINCIPLES-2025
- Authority: T1 (current)
- Applicability: international; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Do not publish points or reason codes while the score convention remains ambiguous.

## Define cutoff and decision-policy handoff

- Source: Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk*
- Locator: section: Credit-granting criteria and approval authority
- Source ID: BCBS-CREDIT-RISK-PRINCIPLES-2025
- Authority: T1 (current)
- Applicability: international; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: The workflow may provide score distributions and trade-offs, but the accountable policy owner sets operational cutoffs.

- Source: Board of Governors of the Federal Reserve System, *Revised Guidance on Model Risk Management (SR 26-2)*
- Locator: section: Model use, governance, and decision authority
- Source ID: FED-SR-26-2
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: A model-development workflow must not invent approval cutoffs from model performance alone.

## Determine scorecard disposition

- Source: Basel Committee on Banking Supervision, *Studies on the validation of internal rating systems*
- Locator: section: Validation of rating and scoring systems
- Source ID: BCBS-VALIDATION-WP14
- Authority: T4 (current)
- Applicability: international; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: A developer package can proceed when binning, scaling, and implementation are reproducible and stable.

- Source: Office of the Comptroller of the Currency, *Model Risk Management Revised Guidance*
- Locator: section: Outcomes analysis and corrective action
- Source ID: OCC-MRM-2026
- Authority: T2 (current)
- Applicability: united-states; Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required.
- Interpretation: Material instability or selection bias requires remediation rather than acceptance based on a strong development Gini alone.
