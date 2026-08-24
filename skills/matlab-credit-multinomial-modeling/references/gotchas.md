# Verified gotchas

## Use `PredictorNames`, not `PredictorVars`, with table-form `fitmnr`

`fitmnr` accepts `PredictorNames` to select table predictors. `PredictorVars` belongs to other MATLAB fitting APIs and is rejected by `fitmnr`.

```matlab
% WRONG: fitmnr does not define PredictorVars.
mdl = fitmnr(trainData,"Rating",ModelType="ordinal",PredictorVars=predictorNames);

% CORRECT: use the documented table-form option.
mdl = fitmnr(trainData,"Rating",ModelType="ordinal",PredictorNames=predictorNames);
```

Evidence: MATLAB R2026a execution of `F001-fitmnr-predictornames/reproduce.m` on 2026-08-21.

## Validate requested categorical classes by membership, not incidental storage order

A categorical response can contain the selected nominal classes in a different internal/display order. When the request fixes the class set but not categorical storage order, compare sets; preserve labels when fitting and report probabilities using `model.ClassNames`.

```matlab
% WRONG: rejects an equivalent class set ordered differently.
assert(isequal(categories(data.Outcome), {"Active","Payoff","Default"}))

% CORRECT: validate exact membership without recoding class storage order.
expected = ["Active","Payoff","Default"];
assert(isempty(setxor(string(categories(data.Outcome)), expected)))
```

Evidence: MATLAB R2026a execution of `F001-category-membership-not-order/reproduce.m` on 2026-08-21.

## Give `confusionchart` an ordered matrix and class labels

`confusionchart(trueLabels,predictedLabels)` does not accept an `Order` name-value argument. When an exact reporting order is required, calculate the matrix with `confusionmat(...,Order=...)`, then pass the matrix and class-label vector to `confusionchart`.

```matlab
% WRONG: Order is not a confusionchart name-value argument.
confusionchart(actual,predicted,Order=cellstr(classOrder));

% CORRECT: impose order while calculating the matrix, then label the chart.
C = confusionmat(actual,predicted,Order=cellstr(classOrder));
confusionchart(C,cellstr(classOrder));
```

Minimal reproduction: construct a two-class confusion matrix with `confusionmat`, render it with explicit matrix labels, and confirm the chart is created without a property error.

Evidence: MATLAB R2026a execution of `10-ordinal-credit-rating/failures/F004-confusion-chart-order/reproduce.m` on 2026-08-21.

## Normalize table-name lists before selection or reporting

Use one homogeneous, row-oriented string array (or one cell array of character vectors) for schema lists, table selectors, and `VariableNames`. Do not mix a column `cellstr` with cells containing string scalars, and do not vertically concatenate scalar names around a row list.

```matlab
% WRONG: mixed element types/orientations.
selected = [cellstr(predictorNames),{"Response"}];
required = ["ID"; predictorNames; "Response"];

% CORRECT: normalize once and reuse a row-oriented string array.
predictorNames = string(predictorNames(:).');
selected = [predictorNames,"Response"];
subset = data(rows,selected);
T = table(actual,predicted,VariableNames=["ActualRating","PredictedRating"]);
```

Evidence: MATLAB R2026a executions of `10-ordinal-credit-rating/failures/F005-table-variable-names/reproduce.m`, `F006-name-list-orientation/reproduce.m`, and `F007-table-selector-container/reproduce.m` on 2026-08-21.

## Do not brace-extract heterogeneous predictors as one matrix

Brace extraction horizontally concatenates selected table variables. It fails when numeric and categorical predictors cannot be concatenated. Validate each type separately while retaining the table for fitting.

```matlab
% WRONG: numeric and categorical variables must concatenate before isfinite runs.
assert(all(isfinite(data{:,predictorNames}),"all"))

% CORRECT: identify numeric variables, then validate compatible subsets.
P = data(:,predictorNames);
isNum = varfun(@isnumeric,P,OutputFormat="uniform");
assert(all(isfinite(P{:,isNum}),"all"))
assert(all(~ismissing(P(:,~isNum)),"all"))
```

Evidence: MATLAB R2026a execution of `11-payoff-default-multinomial/failures/F002-mixed-table-brace-extraction/reproduce.m` on 2026-08-21.
