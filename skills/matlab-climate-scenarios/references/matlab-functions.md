# Climate Scenario Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No operation was executed. All functions operate on selected scenario data and do not supply climate-risk interpretation.

### `climateScenario`

- Syntax: `cs = climateScenario(data)`; `cs = climateScenario(data,RegionVar=rVar,VariableVar=vVar,ScenarioVar=sVar,YearVar=yVar,ValueVar=valVar,CustomIdenfitifierVars=ciVar)`; `cs = climateScenario(data,RegionVar=rVar,VariableVar=vVar,ScenarioVar=sVar,YearVar=yVar,ValueVar=valVar,CustomIdenfitifierVars=ciVar,Name=Value)`.
- Contract: `data` is a table. Default column names are Region, Variable, Scenario, Year, and Value; make nondefault names explicit. Returns a `climateScenario` object.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/climatescenario.html), R2025a.

### Object methods

- `cs = divideVariables(cs,numerators,denominators,Name=Value)` — compute ratios of compatible selected variables. [Source](https://ww2.mathworks.cn/help/risk/climatescenario.dividevariables.html).
- `cs = groupRegions(cs,regions,Name=Value)` — create selected regional groups. [Source](https://ww2.mathworks.cn/help/risk/climatescenario.groupregions.html).
- `plot(cs,Name=Value)`; `h = plot(cs,Name=Value)` — plot selected scenario data. [Source](https://ww2.mathworks.cn/help/risk/climatescenario.plot.html).
- `result = query(cs,Name=Value)` — return a selected scenario-data subset. [Source](https://ww2.mathworks.cn/help/risk/climatescenario.query.html).
- `cs = shockVariables(cs,referenceScenario,Name=Value)` — shock variables relative to a string-scalar reference scenario. [Source](https://ww2.mathworks.cn/help/risk/climatescenario.shockvariables.html).
- `cs = sumVariables(cs,variables,Name=Value)` — compute a selected weighted variable sum. [Source](https://ww2.mathworks.cn/help/risk/climatescenario.sumvariables.html).

All object methods were introduced in R2025a.
