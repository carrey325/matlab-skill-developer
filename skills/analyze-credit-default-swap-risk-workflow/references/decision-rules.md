# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Set CDS analysis purpose and prohibited actions

Use observable evidence to set cds analysis purpose and prohibited actions without preselecting the result.

### Inputs

- declared cds task (required): Valuation, par-spread, sensitivity, accounting input, or market-implied risk purpose and responsible owner.

### Rules

#### Valuation Analysis

- Conditions: declared cds task equals contract valuation or par-spread analysis.
- Rationale: Valuation computes contract-consistent price or spread without recommending a trade.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for valuation, par-spread, sensitivity, accounting input, or market-implied risk purpose and responsible owner.; do not infer valuation-analysis from provider availability.

#### Handoff To Physical Risk Model

- Conditions: declared cds task equals physical default forecast requested.
- Rationale: Market-implied credit risk is not a physical default forecast without a separate risk-premium methodology.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for valuation, par-spread, sensitivity, accounting input, or market-implied risk purpose and responsible owner.; do not infer handoff-to-physical-risk-model from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set cds analysis purpose and prohibited actions.

## Identify contract and credit-event conventions

Use observable evidence to identify contract and credit-event conventions without preselecting the result.

### Inputs

- contract documentation evidence (required): Reference entity, obligation, seniority, currency, maturity, coupon, restructuring, credit events, and settlement.

### Rules

#### Freeze Standard Contract

- Conditions: contract documentation evidence equals standard terms and confirmation identified.
- Rationale: The contract must be mapped to applicable standard terms and confirmation before cash flows are valued.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for reference entity, obligation, seniority, currency, maturity, coupon, restructuring, credit events, and settlement.; do not infer freeze-standard-contract from provider availability.

#### Stop For Contract Clarification

- Conditions: contract documentation evidence equals material term or reference obligation ambiguous.
- Rationale: Material contract ambiguity requires legal or operations clarification; analytics must not invent terms.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for reference entity, obligation, seniority, currency, maturity, coupon, restructuring, credit events, and settlement.; do not infer stop-for-contract-clarification from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to identify contract and credit-event conventions.

## Select discount and credit curves

Use observable evidence to select discount and credit curves without preselecting the result.

### Inputs

- curve provenance and fit (required): Valuation date, currency, collateral basis, instrument set, quote freshness, calibration diagnostics, and tenor support.

### Rules

#### Accept Curves

- Conditions: curve provenance and fit equals approved curves match contract date currency and tenor.
- Rationale: Discount and credit curves must share the valuation date, currency conventions, and support the contract maturity.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for valuation date, currency, collateral basis, instrument set, quote freshness, calibration diagnostics, and tenor support.; do not infer accept-curves from provider availability.

#### Return To Curve Builder

- Conditions: curve provenance and fit equals curve date tenor or convention mismatch.
- Rationale: A curve mismatch returns to the curve workflow; it is not repaired inside CDS pricing.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for valuation date, currency, collateral basis, instrument set, quote freshness, calibration diagnostics, and tenor support.; do not infer return-to-curve-builder from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select discount and credit curves.

## Set recovery and settlement assumptions

Use observable evidence to set recovery and settlement assumptions without preselecting the result.

### Inputs

- recovery and settlement evidence (required): Fixed or market recovery, auction/physical/cash settlement, seniority, and identifiability.

### Rules

#### Fixed Recovery Pricing

- Conditions: recovery and settlement evidence equals standard fixed recovery approved.
- Rationale: A fixed recovery input must be disclosed because it materially affects hazard and valuation.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for fixed or market recovery, auction/physical/cash settlement, seniority, and identifiability.; do not infer fixed-recovery-pricing from provider availability.

#### Recovery Sensitivity Range

- Conditions: recovery and settlement evidence equals recovery uncertain or contract-specific.
- Rationale: Uncertain recovery requires sensitivity or contract-specific evidence rather than silent market default.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for fixed or market recovery, auction/physical/cash settlement, seniority, and identifiability.; do not infer recovery-sensitivity-range from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set recovery and settlement assumptions.

## Determine price spread or implied-risk route

Use observable evidence to determine price spread or implied-risk route without preselecting the result.

### Inputs

- available market observation (required): Observed upfront price, running spread, standard coupon, accrued premium, and requested output.

### Rules

#### Price Or Par Spread

- Conditions: available market observation equals credit curve supplied and contract terms fixed.
- Rationale: Given curves and terms, compute value or par spread under the specified contract.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for observed upfront price, running spread, standard coupon, accrued premium, and requested output.; do not infer price-or-par-spread from provider availability.

#### Implied Credit Calibration

- Conditions: available market observation equals market spread supplied for implied curve analysis.
- Rationale: Market spreads may calibrate implied hazard only with consistent recovery and discount assumptions.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for observed upfront price, running spread, standard coupon, accrued premium, and requested output.; do not infer implied-credit-calibration from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine price spread or implied-risk route.

## Select CDS risk sensitivities

Use observable evidence to select cds risk sensitivities without preselecting the result.

### Inputs

- material risk driver assessment (required): Spread/hazard, recovery, interest rates, maturity, curve shape, and jump-to-default relevance.

### Rules

#### Curve And Recovery Sensitivities

- Conditions: material risk driver assessment equals valuation use with material curve exposure.
- Rationale: Valuation analysis should quantify material curve and recovery sensitivities without converting them into hedging advice.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for spread/hazard, recovery, interest rates, maturity, curve shape, and jump-to-default relevance.; do not infer curve-and-recovery-sensitivities from provider availability.

#### Hazard And Survival Sensitivities

- Conditions: material risk driver assessment equals market-implied risk use.
- Rationale: Implied-risk analysis should show dependence on recovery and interpolation assumptions.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for spread/hazard, recovery, interest rates, maturity, curve shape, and jump-to-default relevance.; do not infer hazard-and-survival-sensitivities from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select cds risk sensitivities.

## Reconcile valuation to market quote

Use observable evidence to reconcile valuation to market quote without preselecting the result.

### Inputs

- valuation reconciliation (required): Clean/dirty price, accrued premium, coupon, upfront amount, settlement date, curves, and tolerance policy.

### Rules

#### Valuation Reconciled

- Conditions: valuation reconciliation equals differences explained by controlled conventions.
- Rationale: A reconciled result identifies every material convention and market input difference.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for clean/dirty price, accrued premium, coupon, upfront amount, settlement date, curves, and tolerance policy.; do not infer valuation-reconciled from provider availability.

#### Investigate Or Reject Valuation

- Conditions: valuation reconciliation equals material unexplained valuation difference.
- Rationale: Unexplained differences require investigation before the result is reported.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for clean/dirty price, accrued premium, coupon, upfront amount, settlement date, curves, and tolerance policy.; do not infer investigate-or-reject-valuation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to reconcile valuation to market quote.

## Determine CDS analysis disposition

Use observable evidence to determine cds analysis disposition without preselecting the result.

### Inputs

- combined cds evidence (required): Contract certainty, curve quality, recovery sensitivity, reconciliation, model limits, and intended use.

### Rules

#### Report Cds Analysis

- Conditions: combined cds evidence equals contract and valuation reconcile with controlled sensitivities.
- Rationale: Report the valuation or implied-risk result with market date, conventions, sensitivities, and limitations.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for contract certainty, curve quality, recovery sensitivity, reconciliation, model limits, and intended use.; do not infer report-cds-analysis from provider availability.

#### Limit Or Reject Analysis

- Conditions: combined cds evidence equals material contract curve or reconciliation defect.
- Rationale: Material contract or valuation defects block an unqualified CDS conclusion.
- Applies to: Single-name or index CDS pricing, par-spread, implied-risk, and sensitivity analysis for a declared valuation or risk-reporting use..
- Excludes: trading recommendations, hedging decisions.
- If information is missing: Stop this decision and obtain evidence for contract certainty, curve quality, recovery sensitivity, reconciliation, model limits, and intended use.; do not infer limit-or-reject-analysis from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine cds analysis disposition.
