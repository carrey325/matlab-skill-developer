# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Determine governing purpose and applicability

Separate prudential, accounting, and internal-risk purposes before defining PD semantics.

### Inputs

- purpose (required): Primary decision use and accountable owner.
- regime (required): Applicable regulatory, accounting, or internal policy regime.
- portfolio (required): Portfolio and entity scope.

### Rules

#### Prudential Irb

- Conditions: purpose equals prudential regulatory capital.
- Rationale: IRB estimates follow prudential definitions, long-run calibration, and applicable supervisory requirements.
- Applies to: prudential IRB.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Accounting Lifetime Ecl

- Conditions: purpose equals financial reporting expected credit loss.
- Rationale: Accounting lifetime PD supports impairment measurement but must remain distinct from prudential capital semantics.
- Applies to: IFRS 9 or applicable accounting policy.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Internal Risk Management

- Conditions: purpose equals internal risk management.
- Rationale: Internal-use models require an explicit policy owner and cannot silently inherit external-regime rules.
- Applies to: internal risk management.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

### Fallback

Outcome: insufficient purpose. Stop and obtain a signed-off purpose, accountable owner, portfolio, and applicability assessment.

## Define horizon and PD semantics

Choose a PD quantity whose horizon, conditioning, and aggregation are consistent with the governing purpose.

### Inputs

- applicability branch (required): Selected governing-purpose branch.
- required output (required): One-year, conditional term structure, marginal, or cumulative lifetime PD.
- event timing (required): Observed default-event timing resolution.

### Rules

#### Prudential One Year

- Conditions: applicability branch equals prudential-irb.
- Rationale: The Basel IRB quantity is a long-run average of one-year default rates, not an accounting lifetime cumulative PD.
- Applies to: prudential IRB.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Conditional One Year Sequence

- Conditions: required output equals conditional period PD term structure.
- Rationale: A sequence of conditional period PDs preserves period-by-period event conditioning and can support later cumulative calculations.
- Applies to: lifetime PD development.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Cumulative Lifetime

- Conditions: required output equals cumulative lifetime PD.
- Rationale: Cumulative lifetime PD must be derived consistently from conditional survival/default semantics and must not be labelled a one-year IRB PD.
- Applies to: accounting or internal lifetime risk.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

### Fallback

Outcome: undefined semantics. Stop until horizon, conditional versus cumulative meaning, default event, and downstream use are explicit.

## Determine data and sample route

Decide whether data support development, require remediation, or justify only a limited-use analysis.

### Inputs

- lineage complete (required): Data lineage and timing are documented.
- default consistent (required): Default is consistently implemented over history.
- representative (required): Development data represent the application population and relevant conditions.
- sample adequate (required): Events, exposures, periods, and partitions support robust estimation and testing.
- deficiencies remediable (required): Material deficiencies can be corrected or conservatively bounded.

### Rules

#### Proceed

- Conditions: lineage complete equals true; and default consistent equals true; and representative equals true; and sample adequate equals true.
- Rationale: All material data prerequisites are evidenced and a reproducible development/test design is feasible.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Repair

- Conditions: deficiencies remediable equals true; and sample adequate equals false.
- Rationale: A correctable deficiency should be remediated before fitting rather than hidden by a method choice.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Limit Use

- Conditions: representative equals false; and deficiencies remediable equals false.
- Rationale: A bounded exploratory or segment-limited analysis may proceed only with explicit limitations and no production-acceptance claim.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

### Fallback

Outcome: stop for data. Stop when default consistency, lineage, or a defensible sample cannot be established.

## Select candidate model family

Match the statistical family to the observation structure, event timing, censoring, interpretability, and intended output before fitting.

### Inputs

- event timing (required): Discrete interval or continuous/right-censored time-to-event data.
- output semantics (required): Conditional, marginal, or cumulative PD output.
- censoring material (required): Whether censoring materially affects the usable event history.
- proportional hazards tenable (optional): Whether a Cox proportional-hazards structure is defensible.
- link rationale (optional): Reason to prefer logistic or probit link.
- custom need (optional): Documented need not met by supported standard families.

### Rules

#### Discrete Time Logistic

- Conditions: event timing equals discrete intervals; and link rationale in one of log-odds interpretation, established challenger baseline.
- Rationale: Use logistic only when the data are organized as discrete risk intervals and the link choice is justified; implementation support alone is not a reason.
- Applies to: all declared branches.
- Excludes: unmodelled material censoring, continuous-time interpretation without interval conversion.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Discrete Time Probit

- Conditions: event timing equals discrete intervals; and link rationale equals latent-normal response rationale.
- Rationale: Use probit as a justified alternative link for discrete conditional PD, evaluated on common out-of-sample evidence.
- Applies to: all declared branches.
- Excludes: selection solely because the provider exposes the option.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Cox Time To Event

- Conditions: event timing equals time to event with right censoring; and censoring material equals true; and proportional hazards tenable equals true.
- Rationale: A Cox candidate is appropriate only for a time-to-event objective with censoring and a defensible proportional-hazards structure.
- Applies to: all declared branches.
- Excludes: known material violation of proportional hazards, discrete-only observation with material ties that the chosen Cox treatment cannot justify.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Custom Specified

- Conditions: custom need present.
- Rationale: Use a custom family only after standard candidates are shown inadequate and estimation, prediction, validation, and recovery contracts are fully specified.
- Applies to: all declared branches.
- Excludes: undocumented convenience wrappers.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

### Fallback

Outcome: no defensible family. Stop or research further when event timing, censoring, assumptions, or output semantics do not support a candidate family.

## Select rating philosophy

Choose desired sensitivity to current and forecast economic conditions and define expected migration and backtesting behavior.

### Inputs

- purpose (required): Governing use of the PD estimate.
- economic sensitivity (required): Desired sensitivity to current or forecast conditions.
- stability objective (required): Desired stability of grades or PD estimates through the cycle.
- macro scenarios in scope (required): Whether scenario-conditioned forecasts are required.

### Rules

#### Point In Time

- Conditions: economic sensitivity equals current or forecast conditions; and macro scenarios in scope equals true.
- Rationale: A PIT design is appropriate when the intended PD should respond to current or forecast conditions; expect greater cyclicality and validate accordingly.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Through The Cycle

- Conditions: stability objective equals stable through ordinary cyclical movement; and macro scenarios in scope equals false.
- Rationale: A TTC design emphasizes stability through ordinary cyclical movement and requires a compatible long-run calibration and backtesting interpretation.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Hybrid

- Conditions: economic sensitivity equals bounded; and stability objective equals partial stability.
- Rationale: A hybrid philosophy is acceptable only when the sensitivity mechanism and expected migration behavior are explicitly documented and tested.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

### Fallback

Outcome: undefined philosophy. Stop until the owner chooses and documents economic sensitivity, stability objective, and scenario use.

## Select calibration target

Choose a target consistent with purpose, horizon semantics, rating philosophy, segmentation, and observation period.

### Inputs

- applicability branch (required): Governing purpose branch.
- rating philosophy (required): PIT, TTC, or documented hybrid.
- output semantics (required): One-year, conditional term structure, or cumulative lifetime PD.
- target representative (required): Whether the observed target represents the application portfolio and intended conditions.

### Rules

#### Long Run Average

- Conditions: applicability branch equals prudential-irb; and rating philosophy in one of through-the-cycle, hybrid.
- Rationale: Prudential IRB calibration uses the applicable long-run average default rate at the relevant grade, pool, or segment level.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Point In Time Observed

- Conditions: rating philosophy equals point-in-time; and target representative equals true.
- Rationale: A PIT target should reflect the relevant condition and period while remaining representative of the intended application.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Conditional Horizon Curve

- Conditions: output semantics equals conditional period PD term structure; and target representative equals true.
- Rationale: Calibrate and evaluate the conditional horizon profile rather than substituting a single aggregate rate for all periods.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

### Fallback

Outcome: unsupported target. Stop or limit use when the target period, segment, or economic-condition basis is not representative and cannot be adjusted defensibly.

## Select model disposition

Integrate validation evidence, limitations, intended use, and governance boundaries into an explicit disposition.

### Inputs

- discrimination (required): Risk-based discrimination result.
- calibration (required): Target-consistent calibration result.
- stability (required): Temporal and segment stability result.
- assumptions (required): Assumption diagnostics and sensitivity results.
- limitations material (required): Whether unresolved limitations are material to use.
- independent validation status (required): Whether required independent validation has occurred.

### Rules

#### Accept For Developer Package

- Conditions: discrimination equals PASS; and calibration equals PASS; and stability equals PASS; and limitations material equals false.
- Rationale: All developer gates pass for intended use; package as a development conclusion subject to required independent validation and approval.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Accept With Limitations

- Conditions: limitations material equals false; and independent validation status equals pending.
- Rationale: Developer evidence may support a bounded recommendation while the package clearly records limitations and pending independent review.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Recalibrate

- Conditions: calibration equals REMEDIATE; and discrimination in one of PASS, PASS_WITH_LIMITATION.
- Rationale: When ranking remains adequate but the target is missed, diagnose target, segmentation, or calibration method before refitting the whole model.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

#### Redevelop

- Conditions: discrimination in one of REMEDIATE, REJECT; and assumptions not equals PASS.
- Rationale: Conceptual, assumption, or ranking failures require respecification or redevelopment rather than cosmetic recalibration.
- Applies to: all declared branches.
- Excludes: no additional cases.
- If information is missing: Request the missing material information and use the decision fallback; do not infer it from provider availability.

### Fallback

Outcome: reject or escalate. Reject the candidate or escalate when evidence is incomplete, contradictory, or outside delegated acceptance authority.
