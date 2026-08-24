# Verified gotchas

## Validate staged macro inputs against their selected schemas

When macro predictors arrive in a separate keyed table, validate each source, construct the selected join, and validate predictors on the resulting model-input panel. Historical macro rows and named scenario shocks can have different contracts; do not require a scenario-only shock table to carry the historical time key.

```matlab
% WRONG: GDP and Market are supplied by dataMacro, not the loan panel.
assert(ismember("GDP", data.Properties.VariableNames))

% CORRECT: validate the joined model-input table.
modelData = join(data,dataMacro);
assert(all(ismember(["GDP","Market"],modelData.Properties.VariableNames)))

% A scenario row needs only the fields selected by its own contract.
assert(all(ismember(["GDP","Market"],dataMacroStress.Properties.VariableNames)))
```

Evidence: MATLAB R2026a executions of `F001-panel-macro-validation/reproduce.m` and `F002-scenario-macro-schema/reproduce.m` on 2026-08-21.

## Preserve heterogeneous table schemas and use supported name selectors

Selected PD predictors can mix numeric and categorical variables. Do not brace-concatenate them merely to check missingness. Keep variable-name lists as a string array or a cell array of character vectors—not a cell array of string scalars—and validate each selected variable without changing the schema.

```matlab
% WRONG: braces concatenate mixed numeric and categorical variables.
any(ismissing(modelData{:,requiredVariables}),"all")

% CORRECT: validate missingness per selected variable.
hasMissing = false(numel(requiredVariables),1);
for k = 1:numel(requiredVariables)
    hasMissing(k) = any(ismissing(modelData.(requiredVariables{k})),"all");
end
assert(~any(hasMissing))

% Supported selector container.
macroSubset = dataMacro(:,["Year","GDP","Market"]);
```

Evidence: MATLAB R2026a executions of `F003-heterogeneous-table-missingness/reproduce.m` and `F004-table-variable-index-type/reproduce.m` on 2026-08-21.

## Use lifetime-PD role argument names

`fitLifetimePDModel` does not use generic `PredictorVars`, `ResponseVariable`, or `IDVariable` controls. Supply the selected role names using `IDVar`, `AgeVar`, `LoanVars`, `MacroVars`, and `ResponseVar`. A Cox model requires `AgeVar`.

```matlab
% WRONG
fitLifetimePDModel(trainData,"Cox",PredictorVars=["ScoreGroup","GDP"])

% CORRECT
fitLifetimePDModel(trainData,"Cox", ...
    IDVar="ID",AgeVar="YOB",LoanVars="ScoreGroup", ...
    MacroVars={"GDP","Market"},ResponseVar="Default")
```

Evidence: MATLAB R2026a execution of `02-cox-pd-and-ecl/failures/F001-lifetime-pd-role-names/reproduce.m` on 2026-08-21.

## Keep each ID contiguous in lifetime-PD panel data

Before fitting or predicting a selected lifetime-PD model, ensure all rows for a given `IDVar` are together. Joins and concatenations can change panel ordering, so restore the selected ID/time ordering explicitly.

```matlab
% WRONG: assume a join preserved panel row grouping.
modelData = join(data,dataMacro);

% CORRECT: restore ID-contiguous chronological panel order.
modelData = sortrows(join(data,dataMacro),["ID","YOB","Year"]);
```

Evidence: MATLAB R2026a execution of `F005-id-contiguity/reproduce.m` on 2026-08-21.

## Test key uniqueness with supported MATLAB operations

There is no general MATLAB table helper named `duplicated`. Validate uniqueness by comparing the number of keys with the number of unique keys.

```matlab
% WRONG: undefined helper.
assert(~any(duplicated(dataMacro.Year)))

% CORRECT: supported uniqueness check.
assert(numel(unique(dataMacro.Year)) == height(dataMacro))
```

Evidence: MATLAB R2026a execution of `03-ttc-pit-pd/failures/F001-undefined-duplicated/reproduce.m` on 2026-08-21.
