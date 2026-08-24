# Credit Portfolio Risk Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No calculation was executed in this baseline. Select the concrete copula class before calling a shared method.

## `creditDefaultCopula`

- Construct with `cdc = creditDefaultCopula(EAD,PD,LGD,Weights)` or `cdc = creditDefaultCopula(___,Name,Value)`. `EAD`, `PD`, and `LGD` are aligned counterparty vectors; PD and LGD values are in `[0,1]`; weights represent factor and idiosyncratic weights.
- Run `cdc = simulate(cdc,NumScenarios)` or `cdc = simulate(___,Name,Value)` before extracting simulation outputs. `NumScenarios` is a nonnegative integer; simulation populates portfolio losses.
- Post-simulation methods: `cbTable = confidenceBands(cdc)` or `confidenceBands(cdc,Name,Value)`; `scenarios = getScenarios(cdc,scenarioIndices)`; `[riskMeasures,confidenceIntervals] = portfolioRisk(cdc)` or `portfolioRisk(cdc,Name,Value)`; `Contributions = riskContribution(cdc)` or `riskContribution(cdc,Name,Value)`.
- `getScenarios` returns counterparty-loss columns for requested scenario indices; portfolio-risk output includes portfolio measures; contribution output is per counterparty.
- Evidence: [constructor](https://ww2.mathworks.cn/help/risk/creditdefaultcopula.html), [simulate](https://ww2.mathworks.cn/help/risk/creditdefaultcopula.simulate.html), [confidenceBands](https://ww2.mathworks.cn/help/risk/creditdefaultcopula.creditcopula_default_confidencebands.html), [getScenarios](https://ww2.mathworks.cn/help/risk/creditdefaultcopula.creditcopula_default_getscenarios.html), [portfolioRisk](https://ww2.mathworks.cn/help/risk/creditdefaultcopula.creditcopula_default_portfoliorisk.html), [riskContribution](https://ww2.mathworks.cn/help/risk/creditdefaultcopula.creditcopula_default_riskcontribution.html). Introduced R2017a; constructor has an R2026a parallel-execution control.

## `creditMigrationCopula`

- Construct with `cmc = creditMigrationCopula(migrationValues,ratings,transitionMatrix,LGD,Weights)` or `cmc = creditMigrationCopula(___,Name,Value)`. Keep rating-state ordering consistent across migration values, ratings, and transition probabilities.
- Run `cmc = simulate(cmc,NumScenarios)` or `cmc = simulate(___,Name,Value)` before analysis. Then use `confidenceBands`, `getScenarios`, `portfolioRisk`, and `riskContribution` with `cmc` in the same syntax shapes as the default-copula methods.
- Migration scenarios return counterparty values rather than default-copula loss scenarios.
- Evidence: [constructor](https://ww2.mathworks.cn/help/risk/creditmigrationcopula.html), [simulate](https://ww2.mathworks.cn/help/risk/creditmigrationcopula.simulate.html), [confidenceBands](https://ww2.mathworks.cn/help/risk/creditmigrationcopula.creditcopula_migration_confidencebands.html), [getScenarios](https://ww2.mathworks.cn/help/risk/creditmigrationcopula.creditcopula_migration_getscenarios.html), [portfolioRisk](https://ww2.mathworks.cn/help/risk/creditmigrationcopula.creditcopula_migration_portfoliorisk.html), [riskContribution](https://ww2.mathworks.cn/help/risk/creditmigrationcopula.creditcopula_migration_riskcontribution.html). Introduced R2017a; constructor has an R2026a parallel-execution control.

## Portfolio-level calculations

### `asrf`

- Syntax: `[capital,VaR] = asrf(PD,LGD,R)`; `[capital,VaR] = asrf(___,Name,Value)`.
- Contract: aligned PD and LGD vectors have values in `[0,1]`; the output capital is per counterparty and is currency-denominated only when EAD is supplied.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/asrf.html), introduced R2017b.

### `concentrationIndices`

- Syntax: `ci = concentrationIndices(PortfolioData)`; `[ci,Lorenz] = concentrationIndices(___,Name,Value)`.
- Contract: `PortfolioData` is a nonnegative row or column portfolio-position vector. Output is a concentration-index table and optional Lorenz data.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/concentrationindices.html), introduced R2017a.
