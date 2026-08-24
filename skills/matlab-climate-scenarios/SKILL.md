---
name: matlab-climate-scenarios
description: Implement selected climate scenario creation, querying, grouping, transformation, shock, and visualization work in MATLAB without choosing climate-risk policy or scenario assumptions.
---

# Implement Climate Scenarios in MATLAB

## Scope

Implement, review, or repair `climateScenario` construction and its query, regional grouping, arithmetic, shock, and plotting operations after scenario data and transformation policy are selected.

Do not select climate pathways, reference scenarios, shock severity, regional aggregation policy, or risk interpretation.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A selected climate scenario data contract, including variables, regions, times, units, reference scenario, and requested operation.

## Capability Contract

### Required Inputs

- A selected `climateScenario` operation and compatible scenario object or construction data.

### Conditional Inputs

- Region groups, variable weights, denominators, shocks, plotting options, and reference scenarios only when required by the selected operation.

### Input Validation

- Validate variable availability, region/time alignment, unit compatibility, denominator domains, and reference-scenario selection.

## Critical Rules

### Intent Preservation

- Preserve supplied scenario provenance, variable units, reference data, and transformation definitions.

### Data and Unit Conventions

- Keep scenario variable units, time horizons, regions, weights, and shock directions explicit.

### Execution Boundaries

- This skill transforms and visualizes selected scenario data; it does not translate scenarios into a business climate-risk model.

## Failure Handling

- Stop on missing variables, incompatible regions/times, invalid arithmetic domains, unavailable products, or unselected scenario assumptions.

## Gotchas

- Scenario arithmetic is operation-specific: retain the supplied reference scenario and variable-unit compatibility when dividing, summing, or shocking data.

## Reference Loading

- Load [the climate scenario function reference](references/matlab-functions.md) before implementing a selected operation.
