# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Determine EAD purpose and exposure convention

Use observable evidence to determine ead purpose and exposure convention without preselecting the result.

### Inputs

- declared ead use (required): Signed-off purpose, horizon, default linkage, and required exposure definition.

### Rules

#### Prudential Ead

- Conditions: declared ead use equals prudential capital.
- Rationale: Prudential EAD must follow the applicable exposure and conversion-factor framework rather than an accounting-period balance proxy.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for signed-off purpose, horizon, default linkage, and required exposure definition.; do not infer prudential-ead from provider availability.

#### Forecast Exposure Profile

- Conditions: declared ead use equals lifetime loss parameter support.
- Rationale: Accounting-support EAD requires exposure profiles aligned to the ECL horizon and contractual behaviour.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for signed-off purpose, horizon, default linkage, and required exposure definition.; do not infer forecast-exposure-profile from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine ead purpose and exposure convention.

## Define drawn and undrawn exposure components

Use observable evidence to define drawn and undrawn exposure components without preselecting the result.

### Inputs

- facility ledger completeness (required): Reconciled balances, limits, undrawn commitments, accrued amounts, and default dates.

### Rules

#### Freeze Exposure Ledger

- Conditions: facility ledger completeness equals drawn and undrawn histories reconcile.
- Rationale: The target must reconcile exposure components and default timing before conversion behaviour is estimated.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for reconciled balances, limits, undrawn commitments, accrued amounts, and default dates.; do not infer freeze-exposure-ledger from provider availability.

#### Repair Facility History

- Conditions: facility ledger completeness equals material limit or balance history missing.
- Rationale: Missing facility histories make both EAD and CCF targets unreliable and require remediation.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for reconciled balances, limits, undrawn commitments, accrued amounts, and default dates.; do not infer repair-facility-history from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define drawn and undrawn exposure components.

## Choose product-specific EAD route

Use observable evidence to choose product-specific ead route without preselecting the result.

### Inputs

- contractual drawdown option (required): Whether the product permits additional drawings, cancellations, amortisation, or limit changes before default.

### Rules

#### Conversion Factor Route

- Conditions: contractual drawdown option equals revolving or cancellable commitment with undrawn amount.
- Rationale: Revolving commitments require modelling the conversion of undrawn availability into default exposure.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for whether the product permits additional drawings, cancellations, amortisation, or limit changes before default.; do not infer conversion-factor-route from provider availability.

#### Balance Projection Route

- Conditions: contractual drawdown option equals term exposure with scheduled amortisation.
- Rationale: Amortising term facilities require balance-path projection rather than an undrawn-limit conversion model.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for whether the product permits additional drawings, cancellations, amortisation, or limit changes before default.; do not infer balance-projection-route from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to choose product-specific ead route.

## Determine whether CCF is a stable target

Use observable evidence to determine whether ccf is a stable target without preselecting the result.

### Inputs

- ccf denominator behaviour (required): Availability and stability of undrawn amounts and realised pre-default drawings.

### Rules

#### Model Ccf

- Conditions: ccf denominator behaviour equals positive stable undrawn denominator.
- Rationale: CCF is meaningful when the undrawn denominator is positive, reliable, and aligned to the observation window.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for availability and stability of undrawn amounts and realised pre-default drawings.; do not infer model-ccf from provider availability.

#### Direct Ead Or Segmented Route

- Conditions: ccf denominator behaviour equals zero small or volatile undrawn denominator.
- Rationale: Unstable denominators can produce extreme CCFs; direct EAD or a separate segment is required.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for availability and stability of undrawn amounts and realised pre-default drawings.; do not infer direct-ead-or-segmented-route from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine whether ccf is a stable target.

## Select the pre-default observation horizon

Use observable evidence to select the pre-default observation horizon without preselecting the result.

### Inputs

- decision horizon and drawdown timing (required): Required forecast horizon and observed timing of material drawings before default.

### Rules

#### One Year Reference Window

- Conditions: decision horizon and drawdown timing equals fixed one-year prudential horizon.
- Rationale: A one-year prudential horizon requires reference dates and default linkage consistent with that horizon.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for required forecast horizon and observed timing of material drawings before default.; do not infer one-year-reference-window from provider availability.

#### Period By Period Exposure Profile

- Conditions: decision horizon and drawdown timing equals multi-period lifetime exposure path.
- Rationale: Lifetime use requires conditional exposure projections by period rather than one terminal EAD copied across horizons.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for required forecast horizon and observed timing of material drawings before default.; do not infer period-by-period-exposure-profile from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select the pre-default observation horizon.

## Treat limit changes and additional drawings

Use observable evidence to treat limit changes and additional drawings without preselecting the result.

### Inputs

- limit management evidence (required): Evidence on authorised increases, temporary limits, cancellations, freezes, and borrower-initiated drawings.

### Rules

#### Model Limit And Drawdown Dynamics

- Conditions: limit management evidence equals limit changes endogenous and material.
- Rationale: Material endogenous limit changes must be represented or controlled because they alter both denominator and future exposure.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for evidence on authorised increases, temporary limits, cancellations, freezes, and borrower-initiated drawings.; do not infer model-limit-and-drawdown-dynamics from provider availability.

#### Fixed Limit Assumption

- Conditions: limit management evidence equals limits contractually fixed over horizon.
- Rationale: A fixed-limit assumption is acceptable only when supported by product terms and empirical history.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for evidence on authorised increases, temporary limits, cancellations, freezes, and borrower-initiated drawings.; do not infer fixed-limit-assumption from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to treat limit changes and additional drawings.

## Select EAD model family

Use observable evidence to select ead model family without preselecting the result.

### Inputs

- exposure target structure (required): Target type, repeated observations, boundary mass, sample size, and interpretability.

### Rules

#### Regression Candidates

- Conditions: exposure target structure equals continuous EAD or CCF with explanatory drivers.
- Rationale: Regression candidates are appropriate when conditional mean behaviour and bounds can be validated.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for target type, repeated observations, boundary mass, sample size, and interpretability.; do not infer regression-candidates from provider availability.

#### Segmented Or State Based Candidates

- Conditions: exposure target structure equals distinct utilisation regimes or product states.
- Rationale: Distinct behavioural regimes should be modelled separately when pooling would conceal different drawdown mechanisms.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for target type, repeated observations, boundary mass, sample size, and interpretability.; do not infer segmented-or-state-based-candidates from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select ead model family.

## Control EAD and CCF boundary behaviour

Use observable evidence to control ead and ccf boundary behaviour without preselecting the result.

### Inputs

- predicted exposure checks (required): Frequency and materiality of predictions below drawn balance or beyond supportable commitment assumptions.

### Rules

#### Controlled Predictions

- Conditions: predicted exposure checks equals boundary exceptions immaterial and explainable.
- Rationale: Predictions may proceed when economic bounds and any transformations are documented and empirically supported.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for frequency and materiality of predictions below drawn balance or beyond supportable commitment assumptions.; do not infer controlled-predictions from provider availability.

#### Respecify Or Cap With Policy

- Conditions: predicted exposure checks equals material negative or implausibly high predictions.
- Rationale: Material boundary violations require respecification or an explicit evidence-backed policy, not silent clipping.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for frequency and materiality of predictions below drawn balance or beyond supportable commitment assumptions.; do not infer respecify-or-cap-with-policy from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to control ead and ccf boundary behaviour.

## Determine EAD model disposition

Use observable evidence to determine ead model disposition without preselecting the result.

### Inputs

- validation evidence pattern (required): Calibration by product and utilisation, stability, sensitivity, bounds, assumptions, and limitations.

### Rules

#### Package For Validation

- Conditions: validation evidence pattern equals calibration and boundary behaviour acceptable.
- Rationale: A complete developer package can proceed when product-level calibration and assumptions support the use.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for calibration by product and utilisation, stability, sensitivity, bounds, assumptions, and limitations.; do not infer package-for-validation from provider availability.

#### Recalibrate Or Redevelop

- Conditions: validation evidence pattern equals material product bias or unstable drawdown behaviour.
- Rationale: Material product bias or unstable conversion behaviour requires remediation rather than pooled acceptance.
- Applies to: Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose..
- Excludes: PD and LGD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for calibration by product and utilisation, stability, sensitivity, bounds, assumptions, and limitations.; do not infer recalibrate-or-redevelop from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine ead model disposition.
