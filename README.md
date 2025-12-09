# myPython
Containing modules/functions of Python scripts that I developed

# linearreg_stlin.py
A class for performing least squares regression

## Mathematical Background

The implementation uses the ordinary least squares (OLS) method to find the best-fit line:

**Regression Equation:**
```
y = a + b*x
```

Where:
- `b = Sxy / Sxx` (slope)
- `a = ȳ - b*x̄` (intercept)

**Key Formulas:**
- `Sxx = Σ(x²) - n*x̄²`
- `Syy = Σ(y²) - n*ȳ²`
- `Sxy = Σ(x*y) - n*x̄*ȳ`
- `R² = Sxy² / (Sxx * Syy)`
- `s = √[(Syy - b*Sxy) / (n-2)]` (residual standard error)

## Examples

### Example : Temperature Conversion

```python
# Create dataset for Celsius to Fahrenheit conversion
from linearreg_stlin import LinearRegression
data = LinearRegression()
data.add(0, 32)    # Freezing point
data.add(100, 212) # Boiling point
data.add(37, 98.6) # Body temperature

data.stat()
data.output()

# The slope should be approximately 1.8 (9/5)
# The intercept should be approximately 32
```

# matrix_stlin.py
A class for performing matrix manipulations (addition/subtraction/multiplication/inversion)
