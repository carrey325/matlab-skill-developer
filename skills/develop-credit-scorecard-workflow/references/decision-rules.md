# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Determine scorecard purpose and responsibility boundary

Use observable evidence to determine scorecard purpose and responsibility boundary without preselecting the result.

### Inputs

- declared scorecard use (required): Application, behavioural, collection, or other use plus accountable decision owner.

### Rules

#### Application Scorecard

- Conditions: declared scorecard use equals origination risk ranking support.
- Rationale: Application scorecards require an applicant population, observation outcome, and explicit separation from the final credit decision.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for application, behavioural, collection, or other use plus accountable decision owner.; do not infer application-scorecard from provider availability.

#### Behavioural Scorecard

- Conditions: declared scorecard use equals existing-customer behavioural ranking.
- Rationale: Behavioural scorecards require performance windows and predictors available during account management.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for application, behavioural, collection, or other use plus accountable decision owner.; do not infer behavioural-scorecard from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine scorecard purpose and responsibility boundary.

## Define target and development population

Use observable evidence to define target and development population without preselecting the result.

### Inputs

- outcome and sampling design (required): Default/bad definition, observation window, performance window, exclusions, and sampling frame.

### Rules

#### Freeze Target Population

- Conditions: outcome and sampling design equals outcome and windows align with intended population.
- Rationale: A scorecard target is supportable only when outcome timing and population exclusions match intended use.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for default/bad definition, observation window, performance window, exclusions, and sampling frame.; do not infer freeze-target-population from provider availability.

#### Repair Population Design

- Conditions: outcome and sampling design equals selection or window mismatch is material.
- Rationale: Material population mismatch requires redesign before binning because later validation cannot repair a biased target.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for default/bad definition, observation window, performance window, exclusions, and sampling frame.; do not infer repair-population-design from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define target and development population.

## Determine reject-inference treatment

Use observable evidence to determine reject-inference treatment without preselecting the result.

### Inputs

- selection mechanism evidence (required): Coverage of declined applicants, historical policy, selection drivers, and unverifiable outcomes.

### Rules

#### Explicit Reject Inference Study

- Conditions: selection mechanism evidence equals accepted-only sample with material policy selection.
- Rationale: Selection bias must be assessed and any reject-inference assumptions challenged with sensitivity and limitations.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for coverage of declined applicants, historical policy, selection drivers, and unverifiable outcomes.; do not infer explicit-reject-inference-study from provider availability.

#### Observed Outcome Development

- Conditions: selection mechanism evidence equals representative outcome coverage or no material rejection selection.
- Rationale: Observed outcomes may support development when selection effects are evidenced as immaterial.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for coverage of declined applicants, historical policy, selection drivers, and unverifiable outcomes.; do not infer observed-outcome-development from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine reject-inference treatment.

## Select supervised binning treatment

Use observable evidence to select supervised binning treatment without preselecting the result.

### Inputs

- predictor distribution and risk shape (required): Missingness, sparsity, ordering, business meaning, and bad-rate pattern for each predictor.

### Rules

#### Ordered Monotone Bins

- Conditions: predictor distribution and risk shape equals ordered predictor with stable risk gradient.
- Rationale: Ordered bins should preserve a stable interpretable risk gradient without manufacturing separation.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for missingness, sparsity, ordering, business meaning, and bad-rate pattern for each predictor.; do not infer ordered-monotone-bins from provider availability.

#### Merge Or Exclude Levels

- Conditions: predictor distribution and risk shape equals categorical levels with sparse or unstable outcomes.
- Rationale: Sparse categories require evidence-based merging or exclusion rather than unstable standalone points.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for missingness, sparsity, ordering, business meaning, and bad-rate pattern for each predictor.; do not infer merge-or-exclude-levels from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select supervised binning treatment.

## Determine monotonicity constraints

Use observable evidence to determine monotonicity constraints without preselecting the result.

### Inputs

- risk relationship evidence (required): Economic rationale, observed bad rates, sampling uncertainty, and temporal stability.

### Rules

#### Enforce Monotone Relationship

- Conditions: risk relationship evidence equals economic order and stable empirical trend agree.
- Rationale: Monotonicity is justified when economic ordering and stable outcome evidence agree.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for economic rationale, observed bad rates, sampling uncertainty, and temporal stability.; do not infer enforce-monotone-relationship from provider availability.

#### Retain Documented Nonlinearity

- Conditions: risk relationship evidence equals non-monotonic pattern is stable and explainable.
- Rationale: A stable explainable non-monotonic relationship may be retained; monotonicity must not be imposed solely for cosmetics.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for economic rationale, observed bad rates, sampling uncertainty, and temporal stability.; do not infer retain-documented-nonlinearity from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine monotonicity constraints.

## Select scorecard variables

Use observable evidence to select scorecard variables without preselecting the result.

### Inputs

- candidate variable evidence (required): Predictive contribution, multicollinearity, stability, missingness, availability, interpretability, and governance restrictions.

### Rules

#### Retain Variable

- Conditions: candidate variable evidence equals incremental stable and operationally available signal.
- Rationale: Variables should add stable interpretable signal and be reproducible at scoring time.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for predictive contribution, multicollinearity, stability, missingness, availability, interpretability, and governance restrictions.; do not infer retain-variable from provider availability.

#### Exclude Variable

- Conditions: candidate variable evidence equals unstable redundant unavailable or prohibited signal.
- Rationale: Predictive lift does not justify an unstable, unavailable, redundant, or prohibited variable.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for predictive contribution, multicollinearity, stability, missingness, availability, interpretability, and governance restrictions.; do not infer exclude-variable from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select scorecard variables.

## Set points scaling and reason-code interpretation

Use observable evidence to set points scaling and reason-code interpretation without preselecting the result.

### Inputs

- score delivery requirements (required): Base score, odds convention, points-to-double-odds, score direction, rounding, and explanation needs.

### Rules

#### Freeze Points Scale

- Conditions: score delivery requirements equals odds convention and score direction approved.
- Rationale: Scaling translates model log odds into points only after the institution approves odds, direction, and rounding conventions.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for base score, odds convention, points-to-double-odds, score direction, rounding, and explanation needs.; do not infer freeze-points-scale from provider availability.

#### Stop Before Score Delivery

- Conditions: score delivery requirements equals delivery convention unresolved.
- Rationale: Do not publish points or reason codes while the score convention remains ambiguous.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for base score, odds convention, points-to-double-odds, score direction, rounding, and explanation needs.; do not infer stop-before-score-delivery from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set points scaling and reason-code interpretation.

## Define cutoff and decision-policy handoff

Use observable evidence to define cutoff and decision-policy handoff without preselecting the result.

### Inputs

- decision policy authority (required): Whether an accountable policy owner has supplied costs, risk appetite, legal constraints, and override rules.

### Rules

#### Handoff Score Distribution

- Conditions: decision policy authority equals policy owner supplies approved decision criteria.
- Rationale: The workflow may provide score distributions and trade-offs, but the accountable policy owner sets operational cutoffs.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for whether an accountable policy owner has supplied costs, risk appetite, legal constraints, and override rules.; do not infer handoff-score-distribution from provider availability.

#### Stop At Model Output

- Conditions: decision policy authority equals cutoff requested without policy authority.
- Rationale: A model-development workflow must not invent approval cutoffs from model performance alone.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for whether an accountable policy owner has supplied costs, risk appetite, legal constraints, and override rules.; do not infer stop-at-model-output from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to define cutoff and decision-policy handoff.

## Determine scorecard disposition

Use observable evidence to determine scorecard disposition without preselecting the result.

### Inputs

- validation evidence pattern (required): Discrimination, calibration, bin stability, population stability, implementation verification, and limitations.

### Rules

#### Package For Validation

- Conditions: validation evidence pattern equals performance and stability acceptable with controlled limitations.
- Rationale: A developer package can proceed when binning, scaling, and implementation are reproducible and stable.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for discrimination, calibration, bin stability, population stability, implementation verification, and limitations.; do not infer package-for-validation from provider availability.

#### Rebin Reestimate Or Redevelop

- Conditions: validation evidence pattern equals material instability selection bias or implementation mismatch.
- Rationale: Material instability or selection bias requires remediation rather than acceptance based on a strong development Gini alone.
- Applies to: Professional application or behavioural scorecard development where points, reason codes, and stable interpretable relationships are required..
- Excludes: lifetime PD term structures, credit approval execution.
- If information is missing: Stop this decision and obtain evidence for discrimination, calibration, bin stability, population stability, implementation verification, and limitations.; do not infer rebin-reestimate-or-redevelop from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine scorecard disposition.
