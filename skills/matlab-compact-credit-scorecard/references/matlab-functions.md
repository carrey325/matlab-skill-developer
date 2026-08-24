# Compact Credit Scorecard Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No operation was executed in this baseline.

## Conversion and object

### `compact`

- Syntax: `csc = compact(sc)`.
- Contract: convert a full `creditscorecard` into a `compactCreditScorecard`. The full object must already have been processed with `autobinning` and `fitmodel` or `fitConstrainedModel`; `formatpoints` is optional.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/creditscorecard.compact.html), introduced R2019a.

### `compactCreditScorecard`

- Syntax: `csc = compactCreditScorecard(sc)`.
- Contract: create a compact scorecard from a compatible full scorecard. Its properties retain description, good label, response, weights, numeric/categorical predictor sets, and model predictors.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/compactcreditscorecard.html), introduced R2019a.

## Compact-object methods

### `displaypoints`

- Syntax: `PointsInfo = displaypoints(csc)`; `[PointsInfo,MinScore,MaxScore] = displaypoints(csc)`; `[PointsInfo,MinScore,MaxScore] = displaypoints(___,Name,Value)`.
- Contract: return per-bin points and optional compact-scorecard bounds.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/compactcreditscorecard.displaypoints.html), introduced R2019a.

### `score`

- Syntax: `[Scores,Points] = score(csc,data)`.
- Contract: score a table containing all compact-object predictors; return one score per observation and per-predictor points.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/compactcreditscorecard.score.html), introduced R2019a.

### `probdefault`

- Syntax: `pd = probdefault(csc,data)`.
- Contract: return a `NumObs`-by-1 default-probability array for a compatible predictor table.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/compactcreditscorecard.probdefault.html), introduced R2019a.

### `validatemodel`

- Syntax: `Stats = validatemodel(csc,data)`; `[Stats,T] = validatemodel(___,Name,Value)`; `[Stats,T,hf] = validatemodel(___,Name,Value)`.
- Contract: return validation measures and optional detailed/figure output. The table needs all predictors and a binary response.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/compactcreditscorecard.validatemodel.html), introduced R2019b.
