# MATLAB R2026a multinomial-model reference

Use this record only after the implementation contract has selected response labels, class order, predictor treatment, model type, split, and validation requirements. Evidence was inspected on 2026-08-21 from official MATLAB R2026a documentation; example sections are excluded.

## `fitmnr`

- Syntax: `model = fitmnr(X,Y)`, `fitmnr(Tbl,ResponseVarName)`, `fitmnr(Tbl,Formula)`, and `fitmnr(___,Name=Value)`.
- `X` is an `n`-by-`p` numeric predictor matrix. `Y` can be an `n`-by-1 numeric, logical, string, categorical, or cellstr response, or an `n`-by-`k` response matrix. A table form includes predictors and response.
- `ModelType` is `"nominal"` by default and also supports `"ordinal"` and `"hierarchical"`.
- Relevant controls: `PredictorNames`, `CategoricalPredictors`, `IncludeClassInteractions`, `Link`, `Weights`, `IterationLimit`, `Tolerance`, and `EstimateDispersion`.
- `PredictorNames` (not `PredictorVars`) limits the predictors in a table-form call, for example `fitmnr(Tbl,"Rating",ModelType="ordinal",PredictorNames=predictorNames)`.
- Output is a `MultinomialRegression` object. Use its prediction interface to obtain labels and selected posterior-probability outputs without changing row or class order.
- Evidence: [official page](https://ww2.mathworks.cn/help/stats/fitmnr.html), R2026a. Introduced in R2023a.
