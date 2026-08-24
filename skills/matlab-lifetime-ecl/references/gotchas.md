# Verified ECL gotchas

## Keep calendar metadata out of `portfolioECL` value tables

For table-form inputs, `portfolioECL` treats repeated ID rows as successive periods and every non-ID column as a scenario value column. Static LGD and EAD inputs can contain one value per ID without a calendar field. Pass marginal PD as the selected ordered rows with only the ID and PD value columns; otherwise a calendar year can be interpreted as an invalid PD scenario.

```matlab
% WRONG: Year is interpreted as another PD value column.
MarginalPD = annualRows(:,["ID","Year","MarginalPD"]);

% CORRECT: retain row order but pass only ID and the selected value column.
MarginalPD = annualRows(:,["ID","MarginalPD"]);
portfolioECL(MarginalPD,LGD,EAD,IDVar="ID",Periodicity="annual");
```

Evidence: MATLAB R2026a execution of `02-cox-pd-and-ecl/failures/F004-portfolio-ecl-wide-shape/reproduce.m` on 2026-08-21.
