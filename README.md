# myPython

A collection of pure Python implementations of common mathematical and scientific computing algorithms, designed for educational purposes and lightweight applications without external dependencies.

## 📚 Overview

This repository contains custom Python modules for:
- **Linear Regression Analysis** - Statistical modeling and prediction
- **Matrix Operations** - Linear algebra computations

All implementations are written in pure Python with no external dependencies, making them ideal for learning, teaching, and lightweight applications.

## 📁 Repository Structure

```
myPython/
├── LICENSE                # GPL-3.0 license
├── README.md              # This file
├── linearreg_stlin.py     # Linear regression module
└── matrix_stlin.py        # Matrix operations module
```

## 🚀 Quick Start

### Installation

Simply clone the repository:

```bash
git clone https://github.com/shiangtai/myPython.git
cd myPython
```

No additional dependencies required!

### Basic Usage

```python
# Linear Regression
from linearreg_stlin import LinearRegression

data = LinearRegression()
data.add(1.0, 2.1)
data.add(2.0, 4.1)
data.add(3.0, 6.0)
data.stat()
data.output()

# Matrix Operations
from matrix_stlin import Matrix

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
result = m1 * m2
print(result)
```

## 📦 Modules

### 1. linearreg_stlin.py

A class for performing ordinary least squares (OLS) regression analysis.

#### Features
- Read data from files or add points programmatically
- Calculate regression coefficients (slope and intercept)
- Compute R² (coefficient of determination)
- Calculate standard errors for coefficients
- No external dependencies

#### Quick Example

```python
from linearreg_stlin import LinearRegression

# Temperature conversion example
data = LinearRegression()
data.add(0, 32)      # Freezing point
data.add(100, 212)   # Boiling point
data.add(37, 98.6)   # Body temperature

data.stat()
data.output()

# Output:
# Total number of data read: 3
# Coefficients a and b: a = 32.000000, b = 1.800000
# Correlation coefficient R2: 1.000000
```

#### API Methods

| Method | Description |
|--------|-------------|
| `read(filename)` | Read x,y data from file (alternating values) |
| `add(x, y)` | Add a single data point |
| `stat()` | Perform regression analysis |
| `output()` | Display results |

#### Mathematical Background

**Regression Equation:**
```
y = a + b*x
```

**Key Formulas:**
- Slope: `b = Sxy / Sxx`
- Intercept: `a = ȳ - b*x̄`
- R²: `Sxy² / (Sxx * Syy)`
- Standard Error: `s = √[(Syy - b*Sxy) / (n-2)]`

Where:
- `Sxx = Σ(x²) - n*x̄²`
- `Syy = Σ(y²) - n*ȳ²`
- `Sxy = Σ(x*y) - n*x̄*ȳ`

[📖 Full documentation for linearreg_stlin.py →](#detailed-linearreg-documentation)

---

### 2. matrix_stlin.py

A class for performing matrix operations on square matrices.

#### Features
- Matrix addition, subtraction, multiplication
- Matrix inversion (Gaussian elimination)
- Matrix exponentiation (efficient binary method)
- Determinant calculation
- Operator overloading for intuitive syntax
- No external dependencies

#### Quick Example

```python
from matrix_stlin import Matrix

# Create matrices
m = Matrix([[4, 7], [2, 6]])

# Matrix operations
m_squared = m ** 2
m_inverse = m ** -1
identity = m * m_inverse

print("M²:")
print(m_squared)
print("\nM⁻¹:")
print(m_inverse)
print("\nM × M⁻¹ (should be identity):")
print(identity)
```

#### Supported Operations

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Addition | `m1 + m2` | Element-wise addition |
| Subtraction | `m1 - m2` | Element-wise subtraction |
| Multiplication | `m1 * m2` | Matrix multiplication |
| Power | `m ** n` | Matrix to power n |
| Inverse | `m ** -1` | Matrix inverse |
| Identity | `Matrix.identity(n)` | Create n×n identity matrix |
| Determinant | `m.determinant()` | Calculate determinant |

#### Mathematical Background

**Matrix Multiplication:**
```
[A × B]ᵢⱼ = Σₖ Aᵢₖ × Bₖⱼ
```

**Determinant (2×2):**
```
det([[a, b], [c, d]]) = ad - bc
```

**Matrix Inversion:**  
Uses Gaussian elimination: `[A|I] → [I|A⁻¹]`

**Binary Exponentiation:**  
Computes A^n in O(log n) multiplications

[📖 Full documentation for matrix_stlin.py →](#detailed-matrix-documentation)

---

## 📊 Detailed Documentation

### Detailed linearreg Documentation

#### Class: `LinearRegression`

**Constructor:**
```python
data = LinearRegression()
```

**Methods:**

1. **`read(filename)`**
   - Read data from file with alternating x,y values
   - File format: `x1 y1 x2 y2 x3 y3 ...`
   - Example:
     ```python
     data.read('measurements.txt')
     ```

2. **`add(x_val, y_val)`**
   - Add a single data point
   - Example:
     ```python
     data.add(1.5, 3.2)
     ```

3. **`stat()`**
   - Perform regression analysis
   - Calculates: slope, intercept, R², standard errors
   - Must be called before `output()`
   - Example:
     ```python
     data.stat()
     ```

4. **`output()`**
   - Display regression results
   - Shows: data statistics, coefficients, R², standard errors
   - Example:
     ```python
     data.output()
     ```

**Statistics Dictionary:**

After calling `stat()`, access computed values via `data.stats`:

```python
data.stats['npt']    # Number of points
data.stats['avg_x']  # Mean of x
data.stats['avg_y']  # Mean of y
data.stats['std_x']  # Standard deviation of x
data.stats['std_y']  # Standard deviation of y
data.stats['a']      # Intercept
data.stats['b']      # Slope
data.stats['R2']     # R-squared
data.stats['SEa']    # Standard error of intercept
data.stats['SEb']    # Standard error of slope
```

#### Use Cases

1. **Scientific Measurements** - Calibration curves
2. **Economics** - Trend analysis
3. **Engineering** - Performance modeling
4. **Education** - Teaching regression concepts
5. **Quick Analysis** - When NumPy isn't available

---

### Detailed Matrix Documentation

#### Class: `Matrix`

**Constructor:**
```python
m = Matrix([[1, 2], [3, 4]])  # 2x2 matrix
```

**Properties:**
- `data` - The underlying 2D list
- `rows` - Number of rows
- `cols` - Number of columns

**Methods:**

1. **`is_square()`**
   - Returns `True` if matrix is square
   - Example:
     ```python
     if m.is_square():
         print("Can compute determinant")
     ```

2. **`determinant()`**
   - Calculate determinant (square matrices only)
   - Example:
     ```python
     det = m.determinant()
     ```

3. **`inverse()`**
   - Calculate matrix inverse using Gaussian elimination
   - Raises `ValueError` if matrix is singular
   - Example:
     ```python
     m_inv = m.inverse()
     # or: m_inv = m ** -1
     ```

4. **`Matrix.identity(size)` (static)**
   - Create identity matrix
   - Example:
     ```python
     I = Matrix.identity(3)
     ```

#### Practical Examples

**Example 1: Solving Linear Systems**

```python
from matrix_stlin import Matrix

# Solve: 2x + y = 11, 5x + 7y = 13
A = Matrix([[2, 1], [5, 7]])
b = Matrix([[11], [13]])

x = (A ** -1) * b
print("Solution:", x)
```

**Example 2: Markov Chain Transitions**

```python
from matrix_stlin import Matrix

# Transition matrix
P = Matrix([[0.7, 0.3], [0.4, 0.6]])

# State after 5 steps
P5 = P ** 5
print("After 5 transitions:", P5)
```

**Example 3: Verifying Matrix Properties**

```python
from matrix_stlin import Matrix

m = Matrix([[4, 7], [2, 6]])
n = Matrix([[3, 5], [1, 2]])

# Verify: (AB)⁻¹ = B⁻¹A⁻¹
lhs = (m * n) ** -1
rhs = (n ** -1) * (m ** -1)
print("LHS:", lhs)
print("RHS:", rhs)
```

**Example 4: Graphics Transformations**

```python
from matrix_stlin import Matrix

# 2D rotation matrix (45 degrees)
import math
theta = math.pi / 4
rotation = Matrix([
    [math.cos(theta), -math.sin(theta)],
    [math.sin(theta), math.cos(theta)]
])

# Point to rotate
point = Matrix([[1], [0]])
rotated = rotation * point
print("Rotated point:", rotated)
```

#### Algorithm Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Addition/Subtraction | O(n²) | O(n²) |
| Multiplication | O(n³) | O(n²) |
| Determinant | O(n!) | O(n²) |
| Inverse | O(n³) | O(n²) |
| Power | O(n³ log k) | O(n²) |

#### Use Cases

1. **Linear System Solving** - Ax = b
2. **Computer Graphics** - Transformations
3. **Probability Theory** - Markov chains
4. **Physics Simulations** - State transitions
5. **Education** - Teaching linear algebra

---

## ⚠️ Limitations

### linearreg_stlin.py
- **Simple linear regression only** (one predictor variable)
- **No outlier detection**
- **No confidence intervals**
- **No diagnostic plots**

### matrix_stlin.py
- **Square matrices only** (non-square not supported)
- **Numerical precision** (floating-point errors)
- **Performance** (slower than NumPy for large matrices)
- **Determinant algorithm** (O(n!) - slow for large n)

## 🎯 When to Use This Library

**✅ Use when:**
- Learning Python or linear algebra concepts
- Working in environments without NumPy/SciPy
- Need lightweight, dependency-free solutions
- Teaching or demonstrating algorithms
- Working with small datasets/matrices (<100×100)

## 📚 Comparison with Popular Libraries

| Feature | myPython | NumPy | SciPy | scikit-learn |
|---------|----------|-------|-------|--------------|
| Dependencies | None | NumPy | NumPy | NumPy, SciPy |
| Performance | Moderate | Fast | Fast | Fast |
| Ease of Use | Simple | Moderate | Moderate | Simple |
| Linear Regression | ✓ | - | ✓ | ✓ |
| Matrix Ops | ✓ (square) | ✓ (all) | ✓ (all) | - |
| Best For | Learning | Production | Scientific | ML |

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🧪 Add unit tests
- ⚡ Optimize algorithms

Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shiang-Tai Lin**
- GitHub: [@shiangtai](https://github.com/shiangtai)
- Institution: National Taiwan University

## 🙏 Acknowledgments

- Inspired by the need for dependency-free mathematical tools
- Designed for educational purposes and lightweight applications
- Thanks to the open-source community

## 📖 Additional Resources

### For Learning More:
- [Linear Regression Theory](https://en.wikipedia.org/wiki/Linear_regression)
- [Matrix Operations](https://en.wikipedia.org/wiki/Matrix_(mathematics))
- [Gaussian Elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)

### Alternative Libraries:
- **NumPy**: [numpy.org](https://numpy.org/)
- **SciPy**: [scipy.org](https://scipy.org/)
- **scikit-learn**: [scikit-learn.org](https://scikit-learn.org/)

## 📮 Contact

For questions, suggestions, or collaboration:
- Open an issue on [GitHub](https://github.com/shiangtai/myPython/issues)
- Email: stlin@ntu.edu.tw

---

**Note**: This library is primarily designed for educational purposes. For production applications requiring high performance or advanced features, consider using NumPy, SciPy, or scikit-learn.
