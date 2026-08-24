# Verified LGD MATLAB Gotchas

Each correction below is backed by an isolated MATLAB R2026a failure reproduction. Apply it only when the matching operation is present.

## `groupsummary` grouping-variable lists

For table grouping, do not pass a cell array whose elements are MATLAB string scalars. Use a string array or a cell array of character vectors.

```matlab
% WRONG — 1-by-N cell array of string scalars; groupsummary rejects it.
grouped = groupsummary(data,{"LTVBand","AgeBand","Type"},"mean","LGD");

% CORRECT — cell array of character vectors.
grouped = groupsummary(data,{'LTVBand','AgeBand','Type'},'mean','LGD');

% ALSO CORRECT — string array, not a cell array.
grouped = groupsummary(data,["LTVBand","AgeBand","Type"],"mean","LGD");
```

Verified failure identifier: `MATLAB:groupsummary:GroupVariablesTableSubscript`.

## Tobit censoring-limit option names

`fitLGDModel` takes the model family as its second positional argument. For a two-sided Tobit model, use `CensoringSide`, `LeftLimit`, and `RightLimit`; `LowerLimit` and `UpperLimit` are not supported names.

```matlab
% WRONG — invented option names.
mdl = fitLGDModel(data, 'Tobit', ...
    'LowerLimit', 0, 'UpperLimit', 1);

% CORRECT — explicit two-sided censoring and limits.
mdl = fitLGDModel(data, 'Tobit', ...
    'CensoringSide', 'both', 'LeftLimit', 0, 'RightLimit', 1);
```

Verified failure identifier: `MATLAB:InputParser:UnmatchedParameter`.
