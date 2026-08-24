# Credit Scorecard Function Evidence

## Evidence scope

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No function was executed in this baseline. Use the linked page for every optional name-value argument before writing code; this file records the supported entry points and the constraints that change implementation decisions.

## Predictor screening and full scorecard object

### `screenpredictors`

- Syntax: `metric_table = screenpredictors(data)`; `metric_table = screenpredictors(___,Name,Value)`.
- Contract: `data` is a table, tall table, or tall timetable with supported predictor types. It returns one metric row per predictor, including information value, accuracy ratio, AUROC, entropy, Gini, chi-square p-value, and missing percentage.
- Preserve explicit `IDVar`, `ResponseVar`, `PredictorVars`, `WeightsVar`, `NumBins`, and `FrequencyShift`; the response must be binary. Introduced in R2019a.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/screenpredictors.html).

### `creditscorecard`

- Syntax: `sc = creditscorecard(data)`; `sc = creditscorecard(___,Name,Value)`.
- Contract: create a `creditscorecard` from a MATLAB table that contains a binary response. The object preserves the selected good label, response, weights, predictor types, missing-data behavior, ID, predictor variables, and source data.
- Make `GoodLabel`, `ResponseVar`, `WeightsVar`, and `BinMissingData` explicit whenever defaults are not part of the implementation brief. Introduced in R2014b.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.html).

## Binning and predictor inspection

### `autobinning`

- Syntax: `sc = autobinning(sc)`; `sc = autobinning(sc,PredictorNames)`; `sc = autobinning(___,Name,Value)`.
- Top-level name-value arguments are `Algorithm`, `AlgorithmOptions`, and `Display`. Algorithm-specific controls belong in the `AlgorithmOptions` cell array. For `Algorithm="Split"`, use `MaxNumBins` for the bin cap and `MinCount` for the minimum observations per bin.
- Contract: update a full scorecard with automatic binning rules for selected predictors. Predictor names are case-sensitive; rebinned predictors replace earlier manual bin changes.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.autobinning.html), introduced R2014b.

### `bindata`

- Syntax: `bdata = bindata(sc)`; `bdata = bindata(sc,data)`; `bdata = bindata(sc,Name,Value)`.
- Contract: apply the scorecard bin rules to its raw table or a compatible table. The supplied table must contain the scorecard predictors.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.bindata.html), introduced R2014b.

### `bininfo`

- Syntax: `bi = bininfo(sc,PredictorName)`; `bi = bininfo(___,Name,Value)`; `[bi,bm] = bininfo(sc,PredictorName,Name,Value)`; `[bi,bm,mv] = bininfo(sc,PredictorName,Name,Value)`.
- Contract: return bin information and optional maps/statistics for one case-sensitive predictor. Avoid zero-frequency bins because their statistics can be undefined.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.bininfo.html), introduced R2014b.

### `fillmissing`

- Syntax: `sc = fillmissing(sc,PredictorNames,Statistics)`; `sc = fillmissing(___,ConstantValue)`.
- Contract: update a scorecard's predictor missing values using the requested statistic or constant. This function is not MATLAB's generic `fillmissing` call; dispatch from the scorecard object.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.fillmissing.html), introduced R2020a.

### `modifybins`

- Syntax: `sc = modifybins(sc,PredictorName,Name,Value)`.
- Contract: update bins for one case-sensitive predictor of a full scorecard.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.modifybins.html), introduced R2014b.

### `modifypredictor`

- Syntax: `sc = modifypredictor(sc,PredictorName)`; `sc = modifypredictor(___,Name,Value)`.
- Contract: update supported properties of one or more case-sensitive full-scorecard predictors.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.modifypredictor.html), introduced R2015b.

### `plotbins`

- Syntax: `plotbins(sc,PredictorName)`; `hFigure = plotbins(sc,PredictorName)`; `hFigure = plotbins(___,Name,Value)`.
- Contract: create one or more predictor-bin histogram figures from a full scorecard.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.plotbins.html), introduced R2014b.

### `predictorinfo`

- Syntax: `[T,Stats] = predictorinfo(sc,PredictorName)`.
- Contract: return summary information and statistics for one case-sensitive predictor in a full scorecard.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.predictorinfo.html), introduced R2015b.

## Fit, points, score, PD, and validation

### `fitmodel`

- Syntax: `sc = fitmodel(sc)`; `[sc,mdl] = fitmodel(sc)`; `[sc,mdl] = fitmodel(___,Name,Value)`.
- Contract: fit logistic regression to the scorecard's WOE data and return an updated scorecard plus optional `GeneralizedLinearModel`.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.fitmodel.html), introduced R2014b.

### `fitConstrainedModel`

- Syntax: `[sc,mdl] = fitConstrainedModel(sc)`; `[sc,mdl] = fitConstrainedModel(___,Name,Value)`.
- Contract: fit a constrained logistic model to WOE data and return an updated scorecard plus `GeneralizedLinearModel`.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.fitconstrainedmodel.html), introduced R2019a.

### `setmodel`

- Syntax: `sc = setmodel(sc,ModelPredictors,ModelCoefficients)`.
- Contract: set the full scorecard's model predictors and coefficients. Predictor names must match scorecard predictor variables; do not include the intercept in `ModelPredictors`.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.setmodel.html), introduced R2014b.

### `formatpoints`

- Syntax: `sc = formatpoints(sc,Name,Value)`.
- For odds-based scaling use `PointsOddsAndPDO=[Points,Odds,PDO]`. `BasePoints` is a logical indicator for separating base points, not the numeric target score.
- Contract: update full-scorecard points and scaling using selected options.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.formatpoints.html), introduced R2014b.

### `displaypoints`

- Syntax: `PointsInfo = displaypoints(sc)`; `[PointsInfo,MinScore,MaxScore] = displaypoints(sc)`; `[PointsInfo,MinScore,MaxScore] = displaypoints(___,Name,Value)`.
- Contract: return points per predictor/bin and optional score bounds for a full scorecard.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.displaypoints.html), introduced R2014b.

### `score`

- Syntax: `Scores = score(sc)`; `Scores = score(sc,data)`; `[Scores,Points] = score(sc)`; `[Scores,Points] = score(sc,data)`.
- Contract: return one score per observation and optional per-predictor points. External data must contain all model predictors.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.score.html), introduced R2014b.

### `probdefault`

- Syntax: `pd = probdefault(sc)`; `pd = probdefault(sc,data)`.
- Contract: return a `NumObs`-by-1 numeric default-probability array. External data must contain the model predictors.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.probdefault.html), introduced R2015a.

### `validatemodel`

- Syntax: `Stats = validatemodel(sc)`; `Stats = validatemodel(sc,data)`; `[Stats,T] = validatemodel(sc,Name,Value)`; `[Stats,T,hf] = validatemodel(sc,Name,Value)`.
- Contract: return scorecard validation measures, optional detailed statistics, and optional figure output. Validation data must contain a binary response and all model predictors.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.validatemodel.html), introduced R2015a.
- `VariableSelection` defaults to `"Stepwise"`. Use `VariableSelection="FullModel"` when the implementation contract requires every selected predictor.
- `score` returns numeric scores and a per-predictor points table; concatenate that table directly with identifiers rather than wrapping it in `array2table`.
