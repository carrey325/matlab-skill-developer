# MATLAB R2026a explainability reference

Use these APIs only with the selected trained scoring function, compatible predictor data, selected query point, and chosen categorical-variable declarations. Evidence was inspected on 2026-08-21 from official MATLAB R2026a documentation; example sections are excluded.

## Partial dependence and ICE

- `plotPartialDependence(modelOrFunction,features,data)` visualizes selected predictor dependence for a supported model or function handle.
- For ICE use `Conditional="absolute"` for uncentered curves or `"centered"` when selected; `"individual"` is unsupported. Avoid creating a second classifier solely for plotting.
- Evidence: [official page](https://ww2.mathworks.cn/help/stats/plotpartialdependence.html), R2026a.

## `lime`

- Constructor syntax is `lime(blackbox,X,QueryPoint=queryPoint,NumImportantPredictors=n,Type="regression",...)`; alternatively call `fit(results,queryPoint,n)`. Both the query and important-predictor count are required to compute a fitted local model.
- LIME generates synthetic neighborhoods, so seed random behavior only when reproducibility is specified.
- For mixed predictor tables, declare exact categorical variable names with `CategoricalPredictors`; LIME rejects ordinal categorical inputs, so use a nonordinal explainer copy with identical labels/order and leave the scored source data unchanged.
- For a linear surrogate, export `SimpleModel.ExpandedPredictorNames` aligned with `SimpleModel.Beta`; `RegressionLinear` has no `Coefficients` table.
- Evidence: [official page](https://ww2.mathworks.cn/help/stats/lime.html), R2026a.

## `shapley`

- Pass a query with `QueryPoints=queryPoints`: `shapley(blackbox,X,QueryPoints=queryPoints,...)`. When the constructor includes query points it computes values; otherwise call `fit` with query points before reading or plotting contributions.
- Keep predictor names and columns aligned with the scored model.
- Computed contribution values are in the explainer's `Shapley` table, not a `ShapleyValues` property.
- Evidence: [official page](https://ww2.mathworks.cn/help/stats/shapley.html), R2026a.
