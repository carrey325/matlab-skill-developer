# Verified gotchas

## Split panel data by group ID without requiring row uniqueness

When a selected neural-network request uses an ID-level panel split, the identifier can repeat across time rows. Validate that every ID is assigned to exactly one partition, not that IDs are unique per observation row.

```matlab
% WRONG: panel IDs repeat by design.
assert(numel(unique(tbl.ID)) == height(tbl))

% CORRECT: partition unique IDs, then map every row by membership.
ids = unique(tbl.ID,'stable');
trainRows = ismember(tbl.ID,trainIDs);
```

Evidence: MATLAB R2026a execution of `F001-id-level-panel-split/reproduce.m` on 2026-08-21.

## Build the supplied feature contract from source categories and validate its width

A pretrained `dlnetwork` need not expose predictor names in `UserData`, and shared time or administrative columns are not automatically inputs. Treat table category labels as source values rather than encoded column names, preserve their selected order, and normalize derived feature-name lists to a row. Build exactly the requested numeric feature contract, then validate its width using scalar `InputSize` from the selected input layer—not a nonexistent `InputSizes` object property.

```matlab
% WRONG: optional metadata is not the feature contract.
featureNames = net.UserData.FeatureNames;
predictorNames = setdiff(string(tbl.Properties.VariableNames),"ID");

% CORRECT: validate source labels, encode in order, then validate width.
sourceLevels = string(categories(tbl.ScoreGroup)).';
assert(all(ismember(string(tbl.ScoreGroup),sourceLevels)))
X = [double(tbl.YOB), double(string(tbl.ScoreGroup) == sourceLevels)];
featureNames = ["YOB","ScoreGroup_" + sourceLevels];
assert(size(X,2) == net.Layers(1).InputSize)
```

Evidence: MATLAB R2026a executions of `F001-network-feature-metadata/reproduce.m`, `F002-category-labels-vs-encoded-columns/reproduce.m`, `F003-selected-feature-contract/reproduce.m`, `F004-dlnetwork-input-layer-size/reproduce.m`, and `05-deep-pd-interpret-and-stress/failures/F006-feature-name-orientation/reproduce.m` on 2026-08-21.

## Do not use reserved table dimension names as variable names

MATLAB tables reserve their dimension names, including `Row` and `Variables`. Use a nonreserved reporting name such as `Observation` for an exported row index.

```matlab
% WRONG: Row conflicts with the table row-dimension name.
T = table((1:n).',pd,VariableNames=["Row","PD"]);

% CORRECT: use a nonreserved variable name.
T = table((1:n).',pd,VariableNames=["Observation","PD"]);
```

Minimal reproduction: construct the corrected table and verify its height and variable names.

Evidence: MATLAB R2026a execution of `05-deep-pd-interpret-and-stress/failures/F008-table-reserved-row-name/reproduce.m` on 2026-08-21.

## Preserve row-observation orientation for a tabular `dlnetwork`

For the supplied feature-input `dlnetwork`, a plain numeric prediction matrix uses observations in rows and the input-width features in columns. After validating `size(X,2)` against the input layer, pass `X` directly; transposing makes the observation count appear as the channel width.

```matlab
% WRONG: turns n observations into an invalid n-channel input.
y = predict(net,X.');

% CORRECT: n-by-inputWidth tabular feature matrix.
assert(size(X,2)==net.Layers(1).InputSize)
y = predict(net,X);
```

Evidence: MATLAB R2026a execution of `05-deep-pd-interpret-and-stress/failures/F010-dlnetwork-row-observations/reproduce.m` on 2026-08-21.

## Format numeric summary text with `compose`

The `string` constructor does not accept a printf-style numeric format as a second argument. Use `compose` (and convert to string when needed) for deterministic decimal formatting.

```matlab
% WRONG: unsupported string constructor signature.
line = "Mean PD: " + string(meanPD,"%.6f");

% CORRECT: printf-style numeric formatting.
line = "Mean PD: " + string(compose("%.6f",meanPD));
```

Evidence: MATLAB R2026a execution of `05-deep-pd-interpret-and-stress/failures/F012-numeric-summary-format/reproduce.m` on 2026-08-21.
