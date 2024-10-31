class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
        if not self.is_square():
            raise ValueError("Only square matrices are supported for this operation.")

    def is_square(self):
        return self.rows == self.cols

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Incompatible dimensions for matrix addition")

        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Incompatible dimensions for matrix subtraction")

        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for matrix multiplication")

        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def __pow__(self, exponent):
        if exponent == -1:
            return self.inverse()
        elif exponent == 0:
            return Matrix.identity(self.rows)
        elif exponent > 0:
            result = Matrix.identity(self.rows)
            base = self
            while exponent > 0:
                if exponent % 2 == 1:
                    result = result * base
                base = base * base
                exponent //= 2
            return result
        else:
            raise ValueError("Only positive integers and -1 (for inverse) are supported for powers.")

    def inverse(self):
        # Check if matrix is invertible
        if not self.is_square() or self.determinant() == 0:
            raise ValueError("Matrix is not invertible")

        size = self.rows
        identity = Matrix.identity(size)
        augmented = [self.data[i] + identity.data[i] for i in range(size)]
        
        # Applying Gaussian elimination
        for i in range(size):
            # Make the diagonal contain all 1's
            if augmented[i][i] == 0:
                for j in range(i + 1, size):
                    if augmented[j][i] != 0:
                        augmented[i], augmented[j] = augmented[j], augmented[i]
                        break
            divisor = augmented[i][i]
            if divisor == 0:
                raise ValueError("Matrix is not invertible")
            for j in range(2 * size):
                augmented[i][j] /= divisor

            # Make the other columns contain 0's
            for k in range(size):
                if k == i:
                    continue
                factor = augmented[k][i]
                for j in range(2 * size):
                    augmented[k][j] -= factor * augmented[i][j]

        # Extract the inverse matrix
        inverse_data = [row[size:] for row in augmented]
        return Matrix(inverse_data)

    def determinant(self):
        if not self.is_square():
            raise ValueError("Determinant is only defined for square matrices.")
        
        # Simple determinant calculation for 2x2 matrices
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        # Recursive determinant calculation for larger matrices
        det = 0
        for c in range(self.cols):
            submatrix = [
                [self.data[r][col] for col in range(self.cols) if col != c]
                for r in range(1, self.rows)
            ]
            det += ((-1) ** c) * self.data[0][c] * Matrix(submatrix).determinant()
        return det

    @staticmethod
    def identity(size):
        return Matrix([[1 if i == j else 0 for j in range(size)] for i in range(size)])

    def __repr__(self):
        return "\n".join([" ".join(f"{x:0.2f}" for x in row) for row in self.data])

if __name__ == "__main__":
    # Example usage
    m1 = Matrix([[8, 2, 3], [-3, 5, 6], [7, 8, 9]])
    m2 = Matrix([[9, 8, 7], [6, 9, 4], [3, 2, 1]])  

    
    m = m1*m2
    print("Original matrix m:")
    print(m)

    print(m+m)
    print(m-m)
    print(m*m)
    print(m**2)
    print(m*m*m)
    print(m**3)
    print(m*m*m*m)
    print(m**4)
    print(m*(m**-1))
    n=m**-1
    print(m*n)
    print(n)
