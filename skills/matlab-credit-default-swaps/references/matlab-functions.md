# Credit Default Swap Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No valuation was executed. R2022b documentation advises against serial date numbers; prefer the documented modern date representation when compatible with the selected curve object.

### `cdsprice`

- Syntax: `[Price,AccPrem,PaymentDates,PaymentTimes,PaymentCF] = cdsprice(ZeroData,ProbData,Settle,Maturity,ContractSpread)`; `[Price,AccPrem,PaymentDates,PaymentTimes,PaymentCF] = cdsprice(___,Name,Value)`.
- Contract: `ZeroData` is a zero-rate matrix or `IRDataCurve`; align default-probability data, settlement, maturity, and contract spread. Returns clean prices, accrued premiums, and payment schedules/cash flows.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/cdsprice.html), introduced R2010b.

### `cdsspread`

- Syntax: use `cdsspread(ZeroData,ProbData,Settle,Maturity,...)` with optional name-value arguments exactly as documented for the selected contract.
- Contract: `ZeroData` is a zero-rate matrix or `IRDataCurve`; returns spreads in basis points and payment-date/time output.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/cdsspread.html), introduced R2010b.
