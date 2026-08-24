# MATLAB Brinson Gotchas by Function

## `brinsonAttribution`

- Pass exactly one AssetTable.
- Preserve the six-column positional order; swapping portfolio and benchmark weights can silently change results.
- Build exactly one row per asset-period key.
- Number periods from one using the supplied equal-interval contract.
- Do not accept automatic weight normalization as successful input validation.

## AssetTable Construction

- Keep names, returns, categories, portfolio weights, and benchmark weights in the same asset-period order.
- Flatten an asset-by-period matrix with `(:)` only when every other column uses the same column-major order.
- Use strings or categorical arrays, not unequal-length char matrices.
- Do not transpose a table; orient vectors before construction.

## `tick2ret`

- Call it on time-by-asset prices, not on a one-row asset history.
- Extract numeric contents before using a table with a numeric-only call.
- Account for the missing first return period.

## Object Functions

- Use documented functions such as `totalAttribution` and `categoryAttribution` rather than invented plural variants.
- A helper defined inside an official example is not a toolbox function unless its source is available in scope.

The old four-asset expected values are official-example fixtures and were not rerun in this restructuring.
