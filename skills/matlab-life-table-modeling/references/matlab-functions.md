# Life Table Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No function was executed.

### `lifetablefit`

- Syntax: `[a,elx] = lifetablefit(x,lx)`; `[a,elx] = lifetablefit(___,lifemodel,objtype,interpmethod,a0)`.
- Contract: calibrate a parametric life-table model from survival data and return fitted parameters plus fitted survival values.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/lifetablefit.html), R2015a.

### `lifetablegen`

- Syntax: `[qx,lx,dx] = lifetablegen(x,a)`; `[qx,lx,dx] = lifetablegen(x,a,lifemodel)`.
- Contract: generate death probabilities, survival counts, and deaths from a calibrated mortality model.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/lifetablegen.html), R2015a.

### `lifetableconv`

- Syntax: `[qx,lx,dx] = lifetableconv(x0,lx0)`; `[qx,lx,dx] = lifetableconv(x0,y0,y0type)`.
- Contract: convert life-table series to life tables with forced termination.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/lifetableconv.html), R2015a.
