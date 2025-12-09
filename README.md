# myPython
Containing modules/functions of Python scripts that I developed

# 1. linearreg_stlin.py
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

# 2. matrix_stlin.py
A class for performing matrix manipulations (addition/subtraction/multiplication/inversion)

## Mathematical Background

### Matrix Operations

**Addition/Subtraction:**
```
[A + B]ᵢⱼ = Aᵢⱼ + Bᵢⱼ
```

**Multiplication:**
```
[A × B]ᵢⱼ = Σₖ Aᵢₖ × Bₖⱼ
```

**Determinant (2×2):**
```
det([[a, b], [c, d]]) = ad - bc
```

**Determinant (n×n):**
Uses cofactor expansion along the first row.

**Matrix Inversion:**
Uses Gaussian elimination with augmented matrix [A|I] → [I|A⁻¹]

**Binary Exponentiation:**
Efficiently computes A^n in O(log n) multiplications instead of O(n).

## Examples

### Example 1: Solving Linear Systems

```python
from matrix_stlin import Matrix
# Solve Ax = b by computing x = A^(-1)b
A = Matrix([[2, 1], [5, 7]])
b = Matrix([[11], [13]])

A_inv = A ** -1
x = A_inv * b

print("Solution:")
print(x)
```

### Example 2: Matrix Powers

```python
from matrix_stlin import Matrix
# Calculate transition matrix after n steps
transition = Matrix([[0.7, 0.3], [0.4, 0.6]])

# After 3 steps
result = transition ** 3
print("After 3 transitions:")
print(result)
```

### Example 3: Verifying Properties

```python
from matrix_stlin import Matrix
m = Matrix([[4, 7], [2, 6]])

# Verify: M * M^(-1) = I
identity_check = m * (m ** -1)
print("M * M^(-1):")
print(identity_check)

# Verify: (AB)^(-1) = B^(-1)A^(-1)
n = Matrix([[3, 5], [1, 2]])
lhs = (m * n) ** -1
rhs = (n ** -1) * (m ** -1)
print("(AB)^(-1) = B^(-1)A^(-1):")
print(lhs)
print(rhs)
```

### Example 4: Determinant Calculation

```python
from matrix_stlin import Matrix
m = Matrix([[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 10]])

det = m.determinant()
print(f"Determinant: {det}")

if det != 0:
    print("Matrix is invertible")
else:
    print("Matrix is singular (not invertible)")
```

## Algorithm Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Addition/Subtraction | O(n²) | O(n²) |
| Multiplication | O(n³) | O(n²) |
| Determinant | O(n!) | O(n²) |
| Inverse | O(n³) | O(n²) |
| Power (binary exp) | O(n³ log k) | O(n²) |

Where n is the matrix dimension and k is the exponent.

## Limitations

- **Only square matrices** - Non-square matrices will raise an error
- **Numerical precision** - Floating-point arithmetic may introduce small errors
- **No eigenvalue computation** - Not implemented in this version
- **No special matrices** - No optimizations for sparse, diagonal, or symmetric matrices
- **Performance** - Pure Python implementation is slower than NumPy for large matrices
- **Determinant algorithm** - Recursive method is slow for large matrices (O(n!))

## Error Handling

The class will raise `ValueError` for:
- Non-square matrix initialization
- Incompatible dimensions in operations
- Division by zero during inversion
- Attempting to invert a singular matrix (determinant = 0)
- Unsupported exponents (negative numbers other than -1)

## Common Use Cases

1. **Linear systems solving** - Computing A⁻¹b
2. **Coordinate transformations** - Rotation, scaling, translation matrices
3. **Markov chains** - Transition matrix powers
4. **Graphics programming** - 3D transformations
5. **Scientific computing** - Small matrix operations without NumPy dependency

## Tips and Best Practices

1. **Check invertibility** - Always verify determinant ≠ 0 before inverting
2. **Numerical stability** - Be aware of floating-point precision limitations
3. **Performance** - For large matrices (>100×100), consider using NumPy
4. **Identity verification** - Use small tolerance when checking M × M⁻¹ = I
5. **Chain operations** - Leverage operator overloading for readable code

## Comparison with NumPy

| Feature | This Library | NumPy |
|---------|-------------|-------|
| Dependencies | None | Requires NumPy |
| Performance | Slower | Much faster |
| Matrix types | Square only | All shapes |
| API simplicity | Simple | Comprehensive |
| Best for | Learning, small matrices | Production, large matrices |

