# Verified gotchas

## Set the intended good response label explicitly

For a binary response, creditscorecard uses the response value with the highest count as the default GoodLabel. When the business label must identify a particular response value, pass GoodLabel explicitly and verify the resulting object property before binning, fitting, or scoring.

Official corroboration: [creditscorecard](https://ww2.mathworks.cn/help/finance/creditscorecard.html), GoodLabel name-value argument. A relevant [MathWorks Answers question](https://ww2.mathworks.cn/matlabcentral/answers/509451-autobinning-response-highest-count-gets-to-be-good) was reviewed on 2026-08-21; it is used only because the official page confirms the behavior.

## Nest algorithm-specific `autobinning` controls in `AlgorithmOptions`

`autobinning` accepts only `Algorithm`, `AlgorithmOptions`, and `Display` as top-level name-value arguments. For the Split algorithm, maximum bins and minimum observations per bin are `MaxNumBins` and `MinCount` inside the `AlgorithmOptions` cell array; `MinBinSize` is not a Split option.

```matlab
% WRONG: these are not top-level autobinning arguments, and MinBinSize is unsupported.
sc = autobinning(sc,predictors,MaxNumBins=5,MinBinSize=50);

% CORRECT: select Split and pass its exact option names in AlgorithmOptions.
sc = autobinning(sc,predictors,Algorithm="Split", ...
    AlgorithmOptions={"MaxNumBins",5,"MinCount",50});
```

Minimal reproduction: construct a `creditscorecard`, invoke the corrected call for numeric and categorical predictors, and confirm it returns a fitted binning definition without an option-parser error.

Evidence: MATLAB R2026a execution of `09-scorecard-explainability/failures/F001-autobinning-split-options/reproduce.m` on 2026-08-21.

## Use `PointsOddsAndPDO` for odds-based score scaling

`formatpoints` does not define separate `PointsToDoubleOdds`, `OddsBase`, or numeric `BasePoints` arguments. Supply the selected points, odds, and points-to-double-odds values as the three-element `PointsOddsAndPDO` vector. `BasePoints` is only a logical control for separating base points.

```matlab
% WRONG: these names do not form the formatpoints scaling interface.
sc = formatpoints(sc,PointsToDoubleOdds=20,OddsBase=50,BasePoints=600);

% CORRECT: [target points, target odds, points to double odds].
sc = formatpoints(sc,PointsOddsAndPDO=[600 50 20]);
```

Minimal reproduction: fit a scorecard, apply the corrected scaling vector, and confirm `formatpoints` returns a scorecard without an option-parser error.

Evidence: MATLAB R2026a execution of `09-scorecard-explainability/failures/F002-formatpoints-scaling/reproduce.m` on 2026-08-21.

## Request `FullModel` explicitly when all predictors must be retained

`fitmodel(sc)` defaults to stepwise variable selection. When the selected implementation requires a full scorecard model, set `VariableSelection="FullModel"`; otherwise successful execution can silently omit predictors.

```matlab
% WRONG for a full-model requirement: defaults to Stepwise.
sc = fitmodel(sc);

% CORRECT: retain all selected predictors.
sc = fitmodel(sc,VariableSelection="FullModel",Display="Off");
```

Minimal reproduction: fit a scorecard with the corrected option and verify the returned generalized linear model contains every selected predictor.

Evidence: MATLAB R2026a execution of `07-credit-reweighting/failures/F003-full-model-selection/reproduce.m` on 2026-08-21.

## Do not transfer evaluated binning parameters into another request

`evaluation-findings.md` records scenario evidence, not suite-wide defaults. A Split `MaxNumBins=5` / `MinCount=50` contract belongs only to a request that selects those controls. When another request asks only for automatic binning, preserve that contract instead of importing parameters from a different scenario.

```matlab
% Use this when the current contract selects automatic binning only.
sc = autobinning(sc,predictors);
```

Evidence: MATLAB R2026a independent-refit mismatch in `07-credit-reweighting/failures/F004-cross-scenario-binning` and `08-credit-disparate-impact-removal/failures/F005-cross-scenario-binning` on 2026-08-21.

## Concatenate the `score` points table directly

The second output of `score(sc,data)` is already a table. Passing it to `array2table` creates a nested table variable that `writetable` cannot export. Concatenate identifier columns with the points table directly.

```matlab
% WRONG: points is already a table, so this nests it.
[scores,points] = score(sc,data);
out = [idTable,array2table(points)];

% CORRECT: preserve the returned point columns.
[scores,points] = score(sc,data);
out = [idTable,points];
```

Evidence: MATLAB R2026a execution of `09-scorecard-explainability/failures/F006-score-points-table/reproduce.m` on 2026-08-21.
