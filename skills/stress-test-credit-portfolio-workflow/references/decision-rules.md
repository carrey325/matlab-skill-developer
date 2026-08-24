# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Determine stress-test purpose and authority

Use observable evidence to determine stress-test purpose and authority without preselecting the result.

### Inputs

- approved stress mandate (required): Internal risk, capital planning, supervisory, reverse-stress, or exploratory purpose and accountable owner.

### Rules

#### Internal Stress Program

- Conditions: approved stress mandate equals institution internal severe-but-plausible assessment.
- Rationale: Internal stress tests require governance, severity rationale, coverage, and decision linkage.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for internal risk, capital planning, supervisory, reverse-stress, or exploratory purpose and accountable owner.; do not infer internal-stress-program from provider availability.

#### Supervisory Methodology Branch

- Conditions: approved stress mandate equals specified supervisory exercise.
- Rationale: A supervisory exercise must follow its published horizon, static-balance-sheet, risk, and reporting assumptions.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for internal risk, capital planning, supervisory, reverse-stress, or exploratory purpose and accountable owner.; do not infer supervisory-methodology-branch from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine stress-test purpose and authority.

## Select and validate scenario set

Use observable evidence to select and validate scenario set without preselecting the result.

### Inputs

- scenario design evidence (required): Risk narrative, macro paths, severity, plausibility, internal consistency, baseline, horizon, and coverage.

### Rules

#### Freeze Scenario Set

- Conditions: scenario design evidence equals approved coherent baseline and adverse paths.
- Rationale: Scenarios must be internally coherent and severe enough for the purpose while remaining traceable to an approved narrative.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for risk narrative, macro paths, severity, plausibility, internal consistency, baseline, horizon, and coverage.; do not infer freeze-scenario-set from provider availability.

#### Repair Scenario Set

- Conditions: scenario design evidence equals material risk driver absent or internally inconsistent.
- Rationale: A materially incomplete or inconsistent scenario cannot be repaired by model sensitivity after execution.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for risk narrative, macro paths, severity, plausibility, internal consistency, baseline, horizon, and coverage.; do not infer repair-scenario-set from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select and validate scenario set.

## Select macro-to-credit translation

Use observable evidence to select macro-to-credit translation without preselecting the result.

### Inputs

- parameter model sensitivity evidence (required): Model rating philosophy, macro links, lags, nonlinearities, segment coverage, and extrapolation range.

### Rules

#### Model Based Translation

- Conditions: parameter model sensitivity evidence equals validated PIT or satellite relationships exist.
- Rationale: Validated point-in-time or satellite relationships may translate scenario paths when their range and lags are controlled.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for model rating philosophy, macro links, lags, nonlinearities, segment coverage, and extrapolation range.; do not infer model-based-translation from provider availability.

#### Expert Adjustment With Limits

- Conditions: parameter model sensitivity evidence equals relationship unavailable or extrapolation dominates.
- Rationale: Expert adjustments require transparent rationale, sensitivity ranges, governance, and cannot masquerade as model output.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for model rating philosophy, macro links, lags, nonlinearities, segment coverage, and extrapolation range.; do not infer expert-adjustment-with-limits from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select macro-to-credit translation.

## Stress PD LGD and EAD consistently

Use observable evidence to stress pd lgd and ead consistently without preselecting the result.

### Inputs

- parameter stress contract (required): Conditionality, scenario horizon, downturn/recovery effects, utilisation, dependencies, and double counting.

### Rules

#### Joint Parameter Projection

- Conditions: parameter stress contract equals parameter models share scenario semantics.
- Rationale: PD, LGD, and EAD must respond consistently to the same scenario and timing assumptions.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for conditionality, scenario horizon, downturn/recovery effects, utilisation, dependencies, and double counting.; do not infer joint-parameter-projection from provider availability.

#### Sensitivity Range Or Gap

- Conditions: parameter stress contract equals one or more parameter links unsupported.
- Rationale: Unsupported parameter translation must be represented as a range or GAP, not a zero response.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for conditionality, scenario horizon, downturn/recovery effects, utilisation, dependencies, and double counting.; do not infer sensitivity-range-or-gap from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to stress pd lgd and ead consistently.

## Set balance-sheet and exposure evolution

Use observable evidence to set balance-sheet and exposure evolution without preselecting the result.

### Inputs

- balance sheet policy (required): Static/dynamic rule, amortisation, new business, defaults, cures, limits, and management actions.

### Rules

#### Static Balance Projection

- Conditions: balance sheet policy equals supervisory static-balance requirement.
- Rationale: Apply the published static-balance rules consistently and disclose their effect.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for static/dynamic rule, amortisation, new business, defaults, cures, limits, and management actions.; do not infer static-balance-projection from provider availability.

#### Dynamic Balance Projection

- Conditions: balance sheet policy equals approved internal dynamic plan.
- Rationale: Dynamic projections require independently approved business and management-action assumptions.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for static/dynamic rule, amortisation, new business, defaults, cures, limits, and management actions.; do not infer dynamic-balance-projection from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set balance-sheet and exposure evolution.

## Assess stressed concentration and dependence

Use observable evidence to assess stressed concentration and dependence without preselecting the result.

### Inputs

- stressed exposure profile (required): Single names, sectors, regions, collateral, correlated parameter shifts, and migration clustering.

### Rules

#### Stressed Sector Concentration

- Conditions: stressed exposure profile equals scenario concentrates losses in common drivers.
- Rationale: Stress testing must surface concentrations that ordinary diversification assumptions can conceal.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for single names, sectors, regions, collateral, correlated parameter shifts, and migration clustering.; do not infer stressed-sector-concentration from provider availability.

#### Single Name Stress

- Conditions: stressed exposure profile equals largest-obligor losses dominate tail.
- Rationale: Large-name sensitivity and connected-counterparty effects require separate reporting.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for single names, sectors, regions, collateral, correlated parameter shifts, and migration clustering.; do not infer single-name-stress from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess stressed concentration and dependence.

## Design severity and assumption sensitivities

Use observable evidence to design severity and assumption sensitivities without preselecting the result.

### Inputs

- uncertainty register (required): Key scenario, translation, correlation, recovery, exposure, and management-action uncertainties.

### Rules

#### Targeted Sensitivity Suite

- Conditions: uncertainty register equals few dominant uncertain assumptions.
- Rationale: Targeted sensitivities should show how dominant assumptions change losses and capital-relevant outputs.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for key scenario, translation, correlation, recovery, exposure, and management-action uncertainties.; do not infer targeted-sensitivity-suite from provider availability.

#### Wide Range And Use Limitation

- Conditions: uncertainty register equals model outside empirical support.
- Rationale: Out-of-range extrapolation requires wider ranges and explicit use limitations.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for key scenario, translation, correlation, recovery, exposure, and management-action uncertainties.; do not infer wide-range-and-use-limitation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to design severity and assumption sensitivities.

## Determine stress-result disposition

Use observable evidence to determine stress-result disposition without preselecting the result.

### Inputs

- stress result and limitations (required): Loss severity, concentration, capital effects, uncertainty, control findings, and risk-appetite policy.

### Rules

#### Report And Monitor

- Conditions: stress result and limitations equals results supported and within approved escalation policy.
- Rationale: Supported results are reported with scenario and model limitations and linked to the approved governance process.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for loss severity, concentration, capital effects, uncertainty, control findings, and risk-appetite policy.; do not infer report-and-monitor from provider availability.

#### Escalate Or Reject Output

- Conditions: stress result and limitations equals material vulnerability or unsupported result.
- Rationale: Material vulnerability, control failure, or unsupported extrapolation requires escalation or rejection of the affected conclusion.
- Applies to: Credit portfolio stress testing for internal risk, capital planning support, supervisory exercises, or defined scenario analysis using governed parameter and portfolio models..
- Excludes: base parameter development, scenario authority approval.
- If information is missing: Stop this decision and obtain evidence for loss severity, concentration, capital effects, uncertainty, control findings, and risk-appetite policy.; do not infer escalate-or-reject-output from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine stress-result disposition.
