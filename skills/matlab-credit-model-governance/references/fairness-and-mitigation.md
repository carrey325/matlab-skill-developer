# MATLAB R2026a fairness and mitigation reference

Use these records after the implementation contract has selected the label convention, protected attributes, policy values, and data partition. Evidence was inspected on 2026-08-21 from official MATLAB R2026a documentation; example sections are excluded.

## `fairnessMetrics`

- Syntax: `metrics = fairnessMetrics(Tbl,ResponseName)` and `fairnessMetrics(___,SensitiveAttributeNames=...,Predictions=...,Name=Value)`.
- Input labels are binary. `Predictions` supplies aligned predicted labels; `PositiveClass`, `ReferenceGroup`, `ModelNames`, and `Weights` are optional controls.
- `report(metrics)` generates the metrics table and `plot(metrics,metric)` visualizes a selected fairness metric.
- Evidence: [official page](https://ww2.mathworks.cn/help/stats/fairnessmetrics.html), R2026a.

## `fairnessWeights`

- Syntax: `weights = fairnessWeights(Tbl,AttributeName,ResponseVarName)`; output is a nonnegative column vector.
- Use an explicitly selected sensitive attribute and binary response. Optional initial weights are supplied using `Weights`.
- Evidence: [official page](https://ww2.mathworks.cn/help/stats/fairnessweights.html), R2026a.

## `disparateImpactRemover`

- Syntax: `remover = disparateImpactRemover(Tbl,AttributeName)` or `[remover,transformedData] = disparateImpactRemover(___,Name=Value)`.
- `PredictorNames` selects transformed numeric predictors; `RepairFraction` is in `[0,1]` and defaults to 1.
- Use `transform(remover,newData)` to apply the fitted transformer to compatible held-out data.
- Evidence: [official page](https://ww2.mathworks.cn/help/stats/disparateimpactremover.html) and [transform](https://ww2.mathworks.cn/help/stats/disparateimpactremover.transform.html), R2026a.
