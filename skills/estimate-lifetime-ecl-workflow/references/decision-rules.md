# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Select governing loss regime

Use observable evidence to select governing loss regime without preselecting the result.

### Inputs

- declared reporting basis (required): Applicable accounting framework, reporting entity, portfolio, and internal-use mandate.

### Rules

#### Ifrs Nine Branch

- Conditions: declared reporting basis equals IFRS reporting.
- Rationale: IFRS 9 requires its own impairment, staging, forward-looking, and discounting logic.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for applicable accounting framework, reporting entity, portfolio, and internal-use mandate.; do not infer ifrs-nine-branch from provider availability.

#### Cecl Branch

- Conditions: declared reporting basis equals US GAAP CECL reporting.
- Rationale: CECL applies lifetime expected losses to in-scope amortised-cost assets under US GAAP and must remain separate from IFRS staging.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for applicable accounting framework, reporting entity, portfolio, and internal-use mandate.; do not infer cecl-branch from provider availability.

#### Internal Economic Loss Branch

- Conditions: declared reporting basis equals approved internal economic-loss mandate outside financial reporting.
- Rationale: Internal economic-loss estimation requires a signed risk definition, horizon, scenario policy, and reporting boundary and must not be labelled IFRS 9 or CECL.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for applicable accounting framework, reporting entity, portfolio, and internal-use mandate.; do not infer internal-economic-loss-branch from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select governing loss regime.

## Determine instrument scope and loss horizon

Use observable evidence to determine instrument scope and loss horizon without preselecting the result.

### Inputs

- instrument classification and commitment (required): Measurement category, maturity, revolving features, off-balance-sheet commitment, cancellation rights, and internal risk horizon.

### Rules

#### Twelve Month Ecl

- Conditions: instrument classification and commitment equals IFRS Stage 1 exposure.
- Rationale: Stage 1 uses 12-month expected credit losses while retaining lifetime cash shortfall effects from defaults possible in the next 12 months.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for measurement category, maturity, revolving features, off-balance-sheet commitment, cancellation rights, and internal risk horizon.; do not infer twelve-month-ecl from provider availability.

#### Contractual Term Lifetime Loss

- Conditions: instrument classification and commitment equals CECL amortised-cost asset.
- Rationale: CECL estimates expected losses over the contractual term subject to applicable extension and cancellation guidance.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for measurement category, maturity, revolving features, off-balance-sheet commitment, cancellation rights, and internal risk horizon.; do not infer contractual-term-lifetime-loss from provider availability.

#### Policy Horizon Economic Loss

- Conditions: instrument classification and commitment equals internal economic-loss portfolio with approved risk horizon.
- Rationale: Internal loss horizons must follow the approved decision use and remain explicitly distinct from accounting measurement horizons.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for measurement category, maturity, revolving features, off-balance-sheet commitment, cancellation rights, and internal risk horizon.; do not infer policy-horizon-economic-loss from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine instrument scope and loss horizon.

## Determine IFRS 9 staging and SICR route

Use observable evidence to determine ifrs 9 staging and sicr route without preselecting the result.

### Inputs

- credit risk change evidence (required): Governing regime, origination risk, reporting-date risk, delinquency, qualitative indicators, default status, and policy rebuttals.

### Rules

#### Stage Two Lifetime

- Conditions: credit risk change evidence equals IFRS asset with significant increase since initial recognition without impairment.
- Rationale: SICR moves an IFRS 9 asset to lifetime ECL before it becomes credit-impaired.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for governing regime, origination risk, reporting-date risk, delinquency, qualitative indicators, default status, and policy rebuttals.; do not infer stage-two-lifetime from provider availability.

#### Stage Three Credit Impaired

- Conditions: credit risk change evidence equals IFRS asset credit-impaired at reporting date.
- Rationale: Credit-impaired assets require lifetime ECL and interest treatment consistent with the standard.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for governing regime, origination risk, reporting-date risk, delinquency, qualitative indicators, default status, and policy rebuttals.; do not infer stage-three-credit-impaired from provider availability.

#### Staging Not Applicable Use Regime Scope

- Conditions: credit risk change evidence equals CECL or internal economic-loss branch.
- Rationale: IFRS 9 staging must not be imported into CECL or internal economic-loss calculations; retain the regime-specific scope and horizon decision.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for governing regime, origination risk, reporting-date risk, delinquency, qualitative indicators, default status, and policy rebuttals.; do not infer staging-not-applicable-use-regime-scope from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine ifrs 9 staging and sicr route.

## Assess PD LGD and EAD input suitability

Use observable evidence to assess pd lgd and ead input suitability without preselecting the result.

### Inputs

- parameter governance evidence (required): Purpose, horizon, conditionality, scenario sensitivity, calibration date, portfolio match, and validation status.

### Rules

#### Accept Governed Parameters

- Conditions: parameter governance evidence equals parameters aligned to regime horizon and portfolio.
- Rationale: ECL may consume approved parameters only when semantics, horizon, and scenario treatment align with the loss calculation.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for purpose, horizon, conditionality, scenario sensitivity, calibration date, portfolio match, and validation status.; do not infer accept-governed-parameters from provider availability.

#### Return To Parameter Owner

- Conditions: parameter governance evidence equals parameter semantics or portfolio mismatch.
- Rationale: ECL must not silently transform unsuitable PD, LGD, or EAD; material mismatches return to the adjacent development workflow.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for purpose, horizon, conditionality, scenario sensitivity, calibration date, portfolio match, and validation status.; do not infer return-to-parameter-owner from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess pd lgd and ead input suitability.

## Select forward-looking scenarios and weights

Use observable evidence to select forward-looking scenarios and weights without preselecting the result.

### Inputs

- scenario governance record (required): Reasonable and supportable forecasts, scenario distinctness, horizon, probability basis, nonlinearity, and approval.

### Rules

#### Probability Weighted Scenarios

- Conditions: scenario governance record equals multiple plausible outcomes with nonlinear loss response.
- Rationale: Nonlinear expected losses require probability-weighted scenarios that represent a range of plausible outcomes.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for reasonable and supportable forecasts, scenario distinctness, horizon, probability basis, nonlinearity, and approval.; do not infer probability-weighted-scenarios from provider availability.

#### Single Scenario With Nonlinearity Test

- Conditions: scenario governance record equals single central forecast demonstrably sufficient.
- Rationale: A single scenario is acceptable only when it is representative and nonlinear effects are shown immaterial for the applicable regime.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for reasonable and supportable forecasts, scenario distinctness, horizon, probability basis, nonlinearity, and approval.; do not infer single-scenario-with-nonlinearity-test from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select forward-looking scenarios and weights.

## Select cash-shortfall and discounting basis

Use observable evidence to select cash-shortfall and discounting basis without preselecting the result.

### Inputs

- cash flow and rate contract (required): Expected contractual cash flows, timing, effective interest rate, recoveries, and modifications.

### Rules

#### Effective Interest Discounting

- Conditions: cash flow and rate contract equals IFRS 9 cash-shortfall measurement.
- Rationale: IFRS 9 ECL discounts expected cash shortfalls using the applicable effective interest rate basis.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for expected contractual cash flows, timing, effective interest rate, recoveries, and modifications.; do not infer effective-interest-discounting from provider availability.

#### Method Consistent Discounting

- Conditions: cash flow and rate contract equals CECL loss-rate or discounted-cash-flow method.
- Rationale: CECL discounting and cash-flow treatment must follow the selected compliant method and instrument scope.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for expected contractual cash flows, timing, effective interest rate, recoveries, and modifications.; do not infer method-consistent-discounting from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select cash-shortfall and discounting basis.

## Determine qualitative adjustment or overlay

Use observable evidence to determine qualitative adjustment or overlay without preselecting the result.

### Inputs

- model gap and emerging risk evidence (required): Known model limitations, post-model events, data gaps, double-counting assessment, governance, and reversibility.

### Rules

#### Controlled Overlay

- Conditions: model gap and emerging risk evidence equals material risk not captured by governed models.
- Rationale: An overlay requires evidence, quantified rationale, no double counting, ownership, monitoring, and exit criteria.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for known model limitations, post-model events, data gaps, double-counting assessment, governance, and reversibility.; do not infer controlled-overlay from provider availability.

#### No Additional Overlay

- Conditions: model gap and emerging risk evidence equals effect already represented in scenarios or parameters.
- Rationale: Do not add an overlay for a risk already captured in parameters or scenario weights.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for known model limitations, post-model events, data gaps, double-counting assessment, governance, and reversibility.; do not infer no-additional-overlay from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine qualitative adjustment or overlay.

## Aggregate and reconcile ECL

Use observable evidence to aggregate and reconcile ecl without preselecting the result.

### Inputs

- reconciliation evidence (required): Exposure-level components, stage/scope totals, scenario contributions, ledger population, prior period, and movement attribution.

### Rules

#### Final Ecl Aggregation

- Conditions: reconciliation evidence equals components reconcile to controlled population and ledger.
- Rationale: Aggregation must preserve traceability from exposure components to portfolio totals and reporting balances.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for exposure-level components, stage/scope totals, scenario contributions, ledger population, prior period, and movement attribution.; do not infer final-ecl-aggregation from provider availability.

#### Repair Reconciliation

- Conditions: reconciliation evidence equals unexplained population or movement difference.
- Rationale: Unexplained reconciliation differences block reporting even when model calculations run successfully.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for exposure-level components, stage/scope totals, scenario contributions, ledger population, prior period, and movement attribution.; do not infer repair-reconciliation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to aggregate and reconcile ecl.

## Determine ECL estimate disposition

Use observable evidence to determine ecl estimate disposition without preselecting the result.

### Inputs

- combined ecl evidence (required): Regime compliance, parameter fitness, scenario governance, overlays, reconciliation, uncertainty, and control findings.

### Rules

#### Report With Limitations

- Conditions: combined ecl evidence equals all material components supported and reconciled.
- Rationale: A reportable estimate includes limitations and uncertainty; calculation completion alone is insufficient.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for regime compliance, parameter fitness, scenario governance, overlays, reconciliation, uncertainty, and control findings.; do not infer report-with-limitations from provider availability.

#### Remediate Or Stop Reporting

- Conditions: combined ecl evidence equals material unsupported policy parameter or reconciliation.
- Rationale: Material unsupported inputs or reconciliation failures require remediation or escalation before reporting.
- Applies to: IFRS 9, US CECL, or explicitly defined internal economic-loss estimation with separate applicability branches..
- Excludes: PD LGD or EAD development, accounting policy approval.
- If information is missing: Stop this decision and obtain evidence for regime compliance, parameter fitness, scenario governance, overlays, reconciliation, uncertainty, and control findings.; do not infer remediate-or-stop-reporting from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine ecl estimate disposition.
