# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Determine LGD purpose and loss concept

Use observable evidence to determine lgd purpose and loss concept without preselecting the result.

### Inputs

- declared lgd use (required): Signed-off prudential, accounting-support, or internal economic-loss purpose.

### Rules

#### Prudential Economic Loss

- Conditions: declared lgd use equals prudential capital.
- Rationale: Prudential LGD requires an economic-loss concept and regime-specific conservatism rather than an accounting allowance proxy.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for signed-off prudential, accounting-support, or internal economic-loss purpose.; do not infer prudential-economic-loss from provider availability.

#### Accounting Parameter Support

- Conditions: declared lgd use equals financial reporting parameter support.
- Rationale: Accounting-support LGD must preserve the governing allowance framework and cannot silently inherit prudential downturn treatment.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for signed-off prudential, accounting-support, or internal economic-loss purpose.; do not infer accounting-parameter-support from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine lgd purpose and loss concept.

## Select workout or market LGD basis

Use observable evidence to select workout or market lgd basis without preselecting the result.

### Inputs

- recovery observation basis (required): Availability and reliability of post-default cash flows versus observable market prices.

### Rules

#### Workout Estimation

- Conditions: recovery observation basis equals complete discounted recovery cash flows.
- Rationale: Complete recoveries, costs, and timing support workout LGD built from realised economic loss.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for availability and reliability of post-default cash flows versus observable market prices.; do not infer workout-estimation from provider availability.

#### Market Estimation

- Conditions: recovery observation basis equals reliable traded-price observations near default.
- Rationale: Observable and representative market prices can support market LGD when workout histories are not the intended measurement basis.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for availability and reliability of post-default cash flows versus observable market prices.; do not infer market-estimation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select workout or market lgd basis.

## Define recoveries, costs, and discounting

Use observable evidence to define recoveries, costs, and discounting without preselecting the result.

### Inputs

- cash flow lineage assessment (required): Evidence that recoveries, direct and indirect costs, dates, and discount-rate basis are complete.

### Rules

#### Freeze Economic Loss Cashflows

- Conditions: cash flow lineage assessment equals cash flows and costs reconciled to source systems.
- Rationale: LGD should use reconciled recovery and cost cash flows with timing retained for economic-loss measurement.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for evidence that recoveries, direct and indirect costs, dates, and discount-rate basis are complete.; do not infer freeze-economic-loss-cashflows from provider availability.

#### Repair Workout Data

- Conditions: cash flow lineage assessment equals material recovery or cost fields unresolved.
- Rationale: Missing material cash flows or costs must be remediated before model fitting because the target itself is unreliable.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for evidence that recoveries, direct and indirect costs, dates, and discount-rate basis are complete.; do not infer repair-workout-data from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define recoveries, costs, and discounting.

## Determine cure and return-to-performing treatment

Use observable evidence to determine cure and return-to-performing treatment without preselecting the result.

### Inputs

- post default status evidence (required): Observed cure definition, probation, re-default behaviour, and consistency with the default framework.

### Rules

#### Model Cure Explicitly

- Conditions: post default status evidence equals cure definition and re-default window evidenced.
- Rationale: A material cured population requires explicit cure treatment so zero or low loss observations do not distort severity estimates.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for observed cure definition, probation, re-default behaviour, and consistency with the default framework.; do not infer model-cure-explicitly from provider availability.

#### Limit Or Exclude Cure Route

- Conditions: post default status evidence equals cure evidence immature or inconsistent.
- Rationale: Unreliable cure identification requires repair or a documented limited-use treatment rather than assumed zero loss.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for observed cure definition, probation, re-default behaviour, and consistency with the default framework.; do not infer limit-or-exclude-cure-route from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine cure and return-to-performing treatment.

## Treat incomplete recovery and censoring

Use observable evidence to treat incomplete recovery and censoring without preselecting the result.

### Inputs

- recovery process maturity (required): Share and characteristics of unresolved defaults at the observation cutoff.

### Rules

#### Censoring Aware Design

- Conditions: recovery process maturity equals material unresolved recovery processes.
- Rationale: Material open recovery cases require a censoring-aware or explicitly estimated incomplete-recovery treatment.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for share and characteristics of unresolved defaults at the observation cutoff.; do not infer censoring-aware-design from provider availability.

#### Resolved Case Design

- Conditions: recovery process maturity equals nearly all cases resolved within stable window.
- Rationale: A resolved-case design is supportable only when the observation window captures the recovery process without material selection bias.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for share and characteristics of unresolved defaults at the observation cutoff.; do not infer resolved-case-design from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to treat incomplete recovery and censoring.

## Determine downturn calibration requirement

Use observable evidence to determine downturn calibration requirement without preselecting the result.

### Inputs

- economic condition sensitivity (required): Governing purpose and evidence that recoveries or losses vary materially with adverse conditions.

### Rules

#### Downturn Calibration

- Conditions: economic condition sensitivity equals prudential use with material cyclical sensitivity.
- Rationale: Prudential LGD must reflect adverse economic conditions when losses and recoveries are materially cyclical.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for governing purpose and evidence that recoveries or losses vary materially with adverse conditions.; do not infer downturn-calibration from provider availability.

#### Purpose Specific Calibration

- Conditions: economic condition sensitivity equals non-prudential use or no evidenced downturn mandate.
- Rationale: Do not manufacture a downturn overlay outside its applicable purpose; retain sensitivity analysis and limitations.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for governing purpose and evidence that recoveries or losses vary materially with adverse conditions.; do not infer purpose-specific-calibration from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine downturn calibration requirement.

## Select LGD segmentation

Use observable evidence to select lgd segmentation without preselecting the result.

### Inputs

- heterogeneity evidence (required): Differences in collateral, seniority, product, recovery process, jurisdiction, and cure behaviour.

### Rules

#### Segmented Lgd

- Conditions: heterogeneity evidence equals stable material recovery-process differences.
- Rationale: Segments are warranted when economic loss drivers and recovery mechanisms differ materially and remain supportable in sample.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for differences in collateral, seniority, product, recovery process, jurisdiction, and cure behaviour.; do not infer segmented-lgd from provider availability.

#### Pooled With Controls

- Conditions: heterogeneity evidence equals differences weak or samples too sparse.
- Rationale: Pooling with covariates or limitations is preferable to unstable micro-segments that cannot be calibrated.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for differences in collateral, seniority, product, recovery process, jurisdiction, and cure behaviour.; do not infer pooled-with-controls from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select lgd segmentation.

## Select LGD model family

Use observable evidence to select lgd model family without preselecting the result.

### Inputs

- target distribution and cure pattern (required): Boundedness, mass points, censoring, cure mixture, sample size, and interpretability requirements.

### Rules

#### Bounded Or Regression Candidates

- Conditions: target distribution and cure pattern equals continuous bounded severity without dominant cure mass.
- Rationale: Bounded-response or regression candidates match continuous severity when boundary behaviour is explicitly controlled.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for boundedness, mass points, censoring, cure mixture, sample size, and interpretability requirements.; do not infer bounded-or-regression-candidates from provider availability.

#### Two Stage Cure Severity

- Conditions: target distribution and cure pattern equals material cure/no-loss mass plus positive-loss severity.
- Rationale: A two-stage design separates cure probability from conditional loss severity when the outcome distribution is a genuine mixture.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for boundedness, mass points, censoring, cure mixture, sample size, and interpretability requirements.; do not infer two-stage-cure-severity from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select lgd model family.

## Determine LGD model disposition

Use observable evidence to determine lgd model disposition without preselecting the result.

### Inputs

- validation evidence pattern (required): Calibration, ranking, stability, sensitivity, assumptions, and unresolved limitations assessed separately.

### Rules

#### Package For Validation

- Conditions: validation evidence pattern equals calibration and stability acceptable with immaterial limitations.
- Rationale: A developer package may proceed only when performance and assumptions support the intended use; this is not independent approval.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for calibration, ranking, stability, sensitivity, assumptions, and unresolved limitations assessed separately.; do not infer package-for-validation from provider availability.

#### Recalibrate Or Redevelop

- Conditions: validation evidence pattern equals material calibration or target-definition weakness.
- Rationale: Material target, calibration, or stability weakness requires remediation or redevelopment rather than acceptance by metric averaging.
- Applies to: Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements..
- Excludes: PD and EAD development, ECL aggregation.
- If information is missing: Stop this decision and obtain evidence for calibration, ranking, stability, sensitivity, assumptions, and unresolved limitations assessed separately.; do not infer recalibrate-or-redevelop from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine lgd model disposition.
