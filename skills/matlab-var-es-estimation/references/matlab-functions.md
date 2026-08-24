# VaR and ES Estimation Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No estimate was executed. Select the distribution representation explicitly and preserve the supplied loss/return convention.

### `valueAtRisk`

- Syntax: `VaR = valueAtRisk("normal",VaRLevels)`; `VaR = valueAtRisk("normal",VaRLevels,Name=Value)`; `VaR = valueAtRisk("t",VaRLevels,DegreesOfFreedom=dof)`; `VaR = valueAtRisk("t",VaRLevels,DegreesOfFreedom=dof,Name=Value)`; `VaR = valueAtRisk("empirical",VaRLevels,InputData=data)`; `VaR = valueAtRisk(pdobj,VaRLevels)`.
- Contract: VaR levels are numeric values in `(0,1)`; Student's t degrees of freedom are at least 3; empirical data is numeric. R2026a supports empirical distribution objects.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/valueatrisk.html), introduced R2025a.

### `expectedShortfall`

- Syntax: `ES = expectedShortfall("normal",VaRLevels)`; `ES = expectedShortfall("normal",VaRLevels,Name=Value)`; `ES = expectedShortfall("t",VaRLevels,DegreesOfFreedom=dof)`; `ES = expectedShortfall("t",VaRLevels,DegreesOfFreedom=dof,Name=Value)`; `ES = expectedShortfall("empirical",VaRLevels,InputData=data)`; `ES = expectedShortfall(pdobj,VaRLevels)`.
- Contract: use the same VaR-level, t-distribution, empirical-data, and R2026a empirical-object constraints as `valueAtRisk`.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/expectedshortfall.html), introduced R2025a.
