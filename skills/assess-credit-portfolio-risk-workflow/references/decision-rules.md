# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Select default-mode or migration-mode loss

Use observable evidence to select default-mode or migration-mode loss without preselecting the result.

### Inputs

- portfolio loss question (required): Whether only default loss or all credit-quality changes and mark-to-market effects are decision-relevant.

### Rules

#### Default Mode

- Conditions: portfolio loss question equals hold-to-horizon default loss.
- Rationale: Default-mode analysis is appropriate when loss is driven by default occurrence and recovery over the horizon.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for whether only default loss or all credit-quality changes and mark-to-market effects are decision-relevant.; do not infer default-mode from provider availability.

#### Migration Mode

- Conditions: portfolio loss question equals rating migration and valuation change.
- Rationale: Migration-mode analysis is required when non-default rating changes materially affect value.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for whether only default loss or all credit-quality changes and mark-to-market effects are decision-relevant.; do not infer migration-mode from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select default-mode or migration-mode loss.

## Set horizon and tail probability

Use observable evidence to set horizon and tail probability without preselecting the result.

### Inputs

- risk policy and use (required): Decision use, liquidity, capital planning period, holding horizon, and institution-approved confidence level.

### Rules

#### Annual Loss Distribution

- Conditions: risk policy and use equals one-year internal capital assessment.
- Rationale: A one-year horizon may align with internal capital assessment when exposures and parameters are consistently defined.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for decision use, liquidity, capital planning period, holding horizon, and institution-approved confidence level.; do not infer annual-loss-distribution from provider availability.

#### Short Horizon Risk View

- Conditions: risk policy and use equals shorter risk-management horizon.
- Rationale: A shorter horizon requires transition, exposure, and liquidity assumptions consistent with that decision use.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for decision use, liquidity, capital planning period, holding horizon, and institution-approved confidence level.; do not infer short-horizon-risk-view from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set horizon and tail probability.

## Assess portfolio parameter compatibility

Use observable evidence to assess portfolio parameter compatibility without preselecting the result.

### Inputs

- parameter interface evidence (required): PD horizon, LGD basis, EAD timing, transition states, valuation basis, and exposure snapshot.

### Rules

#### Freeze Portfolio Inputs

- Conditions: parameter interface evidence equals parameters share horizon semantics and population.
- Rationale: Portfolio aggregation requires compatible parameter semantics and exposure timing.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for pd horizon, lgd basis, ead timing, transition states, valuation basis, and exposure snapshot.; do not infer freeze-portfolio-inputs from provider availability.

#### Return To Input Owner

- Conditions: parameter interface evidence equals material semantic or snapshot mismatch.
- Rationale: Mismatched PD, LGD, EAD, transition, or exposure snapshots must be repaired before simulation.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for pd horizon, lgd basis, ead timing, transition states, valuation basis, and exposure snapshot.; do not infer return-to-input-owner from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess portfolio parameter compatibility.

## Select dependence structure

Use observable evidence to select dependence structure without preselecting the result.

### Inputs

- dependence evidence (required): Systematic factors, sector and geography links, tail dependence, contagion, calibration sample, and parsimony.

### Rules

#### Factor Copula Or Asrf

- Conditions: dependence evidence equals broad diversified portfolio with supported common factors.
- Rationale: A factor or ASRF structure is supportable when common drivers and granularity assumptions are evidenced.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for systematic factors, sector and geography links, tail dependence, contagion, calibration sample, and parsimony.; do not infer factor-copula-or-asrf from provider availability.

#### Multi Factor Or Concentration Adjustment

- Conditions: dependence evidence equals material residual sector or name dependence.
- Rationale: Residual dependence and concentration require richer factors, adjustment, or explicit limitation.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for systematic factors, sector and geography links, tail dependence, contagion, calibration sample, and parsimony.; do not infer multi-factor-or-concentration-adjustment from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select dependence structure.

## Assess name and sector concentration

Use observable evidence to assess name and sector concentration without preselecting the result.

### Inputs

- exposure concentration profile (required): Large obligors, connected counterparties, sectors, regions, factor loadings, and diversification assumptions.

### Rules

#### Name Concentration Analysis

- Conditions: exposure concentration profile equals material single-name or connected-group exposure.
- Rationale: Single-name and connected-group concentrations require explicit measurement and cannot be diversified away by model size.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for large obligors, connected counterparties, sectors, regions, factor loadings, and diversification assumptions.; do not infer name-concentration-analysis from provider availability.

#### Sector Concentration Analysis

- Conditions: exposure concentration profile equals material common sector or geographic drivers.
- Rationale: Sector and geographic concentration require systematic-factor and contribution analysis.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for large obligors, connected counterparties, sectors, regions, factor loadings, and diversification assumptions.; do not infer sector-concentration-analysis from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess name and sector concentration.

## Judge simulation precision and tail stability

Use observable evidence to judge simulation precision and tail stability without preselecting the result.

### Inputs

- simulation diagnostics (required): Scenario count, seed control, tail standard error, confidence bands, rare defaults, and repeatability.

### Rules

#### Simulation Accepted

- Conditions: simulation diagnostics equals tail estimates stable across seeds and scenario expansion.
- Rationale: Tail results require reproducible convergence evidence, not a single large simulation run.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for scenario count, seed control, tail standard error, confidence bands, rare defaults, and repeatability.; do not infer simulation-accepted from provider availability.

#### Increase Or Redesign Simulation

- Conditions: simulation diagnostics equals tail estimate materially changes with additional runs.
- Rationale: Unstable tail estimates require more scenarios, variance reduction, or model redesign before reporting.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for scenario count, seed control, tail standard error, confidence bands, rare defaults, and repeatability.; do not infer increase-or-redesign-simulation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to judge simulation precision and tail stability.

## Determine EL UL and economic-capital output

Use observable evidence to determine el ul and economic-capital output without preselecting the result.

### Inputs

- capital measurement policy (required): Loss distribution, expected loss treatment, confidence measure, diversification, capital definition, and policy owner.

### Rules

#### Economic Capital Output

- Conditions: capital measurement policy equals approved internal economic-capital policy.
- Rationale: Economic capital is a policy-governed tail-loss measure, commonly derived from unexpected loss, and must not be labelled regulatory capital.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for loss distribution, expected loss treatment, confidence measure, diversification, capital definition, and policy owner.; do not infer economic-capital-output from provider availability.

#### Risk Distribution Without Capital Label

- Conditions: capital measurement policy equals no approved capital definition.
- Rationale: Report the loss distribution and tail measures without inventing an economic-capital number.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for loss distribution, expected loss treatment, confidence measure, diversification, capital definition, and policy owner.; do not infer risk-distribution-without-capital-label from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine el ul and economic-capital output.

## Select risk contribution and diversification attribution

Use observable evidence to select risk contribution and diversification attribution without preselecting the result.

### Inputs

- allocation purpose and measure (required): Portfolio measure, marginal or component allocation, additivity, concentration, and decision use.

### Rules

#### Component Risk Contributions

- Conditions: allocation purpose and measure equals additive portfolio risk measure with stable simulation.
- Rationale: Component contributions support portfolio attribution when they reconcile to the chosen risk measure.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for portfolio measure, marginal or component allocation, additivity, concentration, and decision use.; do not infer component-risk-contributions from provider availability.

#### Sensitivity Only Attribution

- Conditions: allocation purpose and measure equals non-additive or unstable tail measure.
- Rationale: When allocation is unstable or non-additive, report sensitivities and limitations rather than false precision.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for portfolio measure, marginal or component allocation, additivity, concentration, and decision use.; do not infer sensitivity-only-attribution from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select risk contribution and diversification attribution.

## Determine portfolio-risk reportability

Use observable evidence to determine portfolio-risk reportability without preselecting the result.

### Inputs

- combined portfolio evidence (required): Input suitability, dependence validation, concentration, convergence, sensitivity, attribution, and policy alignment.

### Rules

#### Report Portfolio Risk

- Conditions: combined portfolio evidence equals tail and concentration results stable and policy-aligned.
- Rationale: Reportable results require sensitivity and limitation disclosure alongside point estimates.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for input suitability, dependence validation, concentration, convergence, sensitivity, attribution, and policy alignment.; do not infer report-portfolio-risk from provider availability.

#### Limit Remediate Or Reject

- Conditions: combined portfolio evidence equals material dependence or convergence uncertainty.
- Rationale: Material dependence or convergence uncertainty requires limitation, remediation, or rejection of the affected output.
- Applies to: Internal credit portfolio risk assessment using default-mode, migration-mode, ASRF, or simulation approaches for a declared risk-management or economic-capital purpose..
- Excludes: parameter model development, macro stress testing.
- If information is missing: Stop this decision and obtain evidence for input suitability, dependence validation, concentration, convergence, sensitivity, attribution, and policy alignment.; do not infer limit-remediate-or-reject from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine portfolio-risk reportability.
