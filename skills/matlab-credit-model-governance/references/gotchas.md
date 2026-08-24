# Verified gotchas

## Preserve response schema and match external prediction labels

MATLAB table variable names are case-sensitive. For a separate aligned prediction vector, preserve the exact response name, validate row count, and match the response label type. For example, threshold decisions for a numeric `0/1` response must also be numeric rather than logical.

```matlab
% WRONG: changes the supplied table schema.
fairnessMetrics(data,"Status",Predictions="Predictions")

% CORRECT: preserve `status` and pass the aligned vector.
predictions = double(pd >= threshold);
assert(numel(predictions) == height(data))
fairnessMetrics(data,"status",Predictions=predictions)
```

Evidence: MATLAB R2026a executions of `F001-table-variable-case/reproduce.m` and `07-credit-reweighting/failures/F001-fairness-prediction-type/reproduce.m` on 2026-08-21.

## Pass the requested fairness metric positionally to `plot`

For a `fairnessMetrics` object, the selected metric is a positional plot input rather than the `Metric=...` name-value argument. Use the canonical metric name as the second argument.

```matlab
% WRONG: Metric is not a supported plot name-value argument.
plot(metrics, Metric="StatisticalParityDifference")

% CORRECT: metric is the positional second input.
plot(metrics, "StatisticalParityDifference")
```

Evidence: MATLAB R2026a execution of `F002-fairness-plot-metric-positional/reproduce.m` on 2026-08-21.

## Preserve the supplied source-variable name when deriving a sensitive attribute

MATLAB tables are schema-bound and a selected age field might be named `CustAge`, not a guessed generic `Age`. Validate and use the supplied source variable exactly before deriving the requested protected-group column.

```matlab
% WRONG: assumes an alias that is absent from the supplied table.
assert(ismember("Age", string(data.Properties.VariableNames)))

% CORRECT: validate and use the selected source field.
assert(ismember("CustAge", string(data.Properties.VariableNames)))
age = data.CustAge;
```

Evidence: MATLAB R2026a execution of `F001-preserve-age-source-name/reproduce.m` on 2026-08-21.

## Use the documented ICE conditional value

For `plotPartialDependence`, individual conditional expectation curves use `Conditional="absolute"` (or `"centered"` when specifically selected). `"individual"` is not an accepted value.

```matlab
% WRONG: unsupported Conditional value.
plotPartialDependence(scoreFcn,feature,X,Conditional="individual");

% CORRECT: uncentered ICE curves.
plotPartialDependence(scoreFcn,feature,X,Conditional="absolute");
```

Evidence: MATLAB R2026a execution of `09-scorecard-explainability/failures/F004-explainer-query-signatures/reproduce.m` on 2026-08-21.

## Name LIME/Shapley query arguments and supply LIME predictor count

The third positional argument to `lime` is not a model-type string, and `fit(limeObject,queryPoint)` is incomplete because `numImportantPredictors` is required. Create a fitted LIME result with named `QueryPoint`, `NumImportantPredictors`, and `Type`, or pass both required positional inputs to `fit`. For `shapley`, pass query data with the `QueryPoints` name-value argument.

```matlab
% WRONG: positional model type, incomplete fit, and positional Shapley query.
L = lime(scoreFcn,X,"regression");
L = fit(L,queryPoint);
S = shapley(scoreFcn,X,queryPoint);

% CORRECT: explicit query/model contract; constructor computes the explanation.
L = lime(scoreFcn,X,QueryPoint=queryPoint, ...
    NumImportantPredictors=width(X),Type="regression");
S = shapley(scoreFcn,X,QueryPoints=queryPoint);
```

Evidence: MATLAB R2026a execution of `05-deep-pd-interpret-and-stress/failures/F009-explainer-query-signatures/reproduce.m` on 2026-08-21.

## Read contributions from the actual explainer properties

A LIME linear surrogate is a `RegressionLinear` object, which exposes coefficients through `Beta` and expanded term names through `ExpandedPredictorNames`; it has no `Coefficients` table. A Shapley explainer exposes computed values in its `Shapley` table, not `ShapleyValues`.

```matlab
% WRONG: properties do not exist on these R2026a objects.
limeTerms = L.SimpleModel.Coefficients;
shapleyTerms = S.ShapleyValues;

% CORRECT: preserve expanded-term alignment and the computed Shapley table.
limeTerms = table(string(L.SimpleModel.ExpandedPredictorNames(:)), ...
    L.SimpleModel.Beta(:),VariableNames=["Term","Coefficient"]);
shapleyTerms = S.Shapley;
```

Evidence: MATLAB R2026a execution of `09-scorecard-explainability/failures/F005-explainer-result-properties/reproduce.m` on 2026-08-21.

## Convert ordinal categories to nonordinal explainer inputs and declare them

LIME does not support ordinal categorical predictors. For explanation only, create a nonordinal categorical copy that preserves the same labels and category order, keep the scoring function's label-based encoding unchanged, and pass the exact variable name in `CategoricalPredictors`. Do not alter the original scoring tables or network feature order.

```matlab
% WRONG: ScoreGroup is ordinal in the source table.
L = lime(scoreFcn,X,QueryPoint=q,NumImportantPredictors=width(X),Type="regression");

% CORRECT: nonordinal explainer copy with identical labels/order.
levels = string(categories(X.ScoreGroup));
X.ScoreGroup = categorical(string(X.ScoreGroup),levels,Ordinal=false);
q = X(queryIndex,:);
L = lime(scoreFcn,X,QueryPoint=q,NumImportantPredictors=width(X), ...
    Type="regression",CategoricalPredictors="ScoreGroup");
S = shapley(scoreFcn,X,QueryPoints=q,CategoricalPredictors="ScoreGroup");
```

Evidence: MATLAB R2026a execution of `05-deep-pd-interpret-and-stress/failures/F011-categorical-explainer-input/reproduce.m` on 2026-08-21.
