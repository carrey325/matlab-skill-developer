# Lifetime ECL Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No calculation was executed.

### `portfolioECL`

- Syntax: `[totalECL,ECLByID,ECLByPeriod] = portfolioECL(MarginalPD,LGD,EAD)`; `[totalECL,ECLByID,ECLByPeriod] = portfolioECL(___,Name=Value)`.
- Contract: marginal PD, LGD, and EAD inputs must have compatible IDs and ID order. The calculation returns total portfolio ECL plus ECL by ID and by period; total ECL reflects scenario weighting and discounting supplied through the selected contract.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/portfolioecl.html), introduced R2022a.
