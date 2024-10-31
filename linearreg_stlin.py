class LinearRegression:
    def __init__(self):
        # Initialize empty lists for x and y data points
        self.x = []
        self.y = []
        # Dictionary to store computed statistics after regression
        self.stats = {}

    def read(self, filename):
        """Read data from a file where x and y values are stored alternatively."""
        # Open the file and read all values into a list
        with open(filename, "r") as f:
            data = f.read().split()
            # Convert alternating values to float and store in x and y lists
            self.x = list(map(float, data[::2]))  # even-indexed items go to x
            self.y = list(map(float, data[1::2]))  # odd-indexed items go to y
        print(f"Data successfully read from {filename}. Total points: {len(self.x)}")

    def add(self, x_val, y_val):
        """Add a single data point to x and y lists."""
        self.x.append(x_val)
        self.y.append(y_val)

    def stat(self):
        """Calculate statistics and perform linear regression."""
        # Check if data is valid: non-empty and equal length
        if not self.x or not self.y or len(self.x) != len(self.y):
            raise ValueError("Data lists x and y must be non-empty and of the same length.")

        # Number of data points
        npt = len(self.x)
        # Sum of x and y values
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        # Averages of x and y
        avg_x = sum_x / npt
        avg_y = sum_y / npt

        # Calculate Sxx, Syy, and Sxy for regression
        Sxx = sum(x ** 2 for x in self.x) - npt * avg_x ** 2
        Syy = sum(y ** 2 for y in self.y) - npt * avg_y ** 2
        Sxy = sum(x * y for x, y in zip(self.x, self.y)) - npt * avg_x * avg_y

        # Calculate slope (b) and intercept (a) of the regression line
        b = Sxy / Sxx
        a = avg_y - (b * avg_x)

        # Calculate R-squared value for correlation
        R2 = (Sxy ** 2) / (Sxx * Syy)

        # Standard error calculations
        s = ((Syy - b * Sxy) / (npt - 2)) ** 0.5
        SEa = s * ((1.0 / npt) + (avg_x ** 2 / Sxx)) ** 0.5  # SE of a
        SEb = s / (Sxx ** 0.5)  # SE of b

        # Standard deviations of x and y
        std_x = (Sxx / (npt - 1)) ** 0.5
        std_y = (Syy / (npt - 1)) ** 0.5

        # Store all computed statistics in the stats dictionary for easy access
        self.stats = {
            "npt": npt,
            "avg_x": avg_x,
            "avg_y": avg_y,
            "std_x": std_x,
            "std_y": std_y,
            "a": a,
            "b": b,
            "R2": R2,
            "SEa": SEa,
            "SEb": SEb
        }

    def output(self):
        """Print the calculated statistics."""
        # Check if stat() has been run and stats are available
        if not self.stats:
            print("No statistics available. Run stat() first.")
            return

        # Output results of regression analysis
        print(f"Total number of data read: {self.stats['npt']}")
        print(f"Average and standard deviation of data x: {self.stats['avg_x']:.6f}, {self.stats['std_x']:.6f}")
        print(f"Average and standard deviation of data y: {self.stats['avg_y']:.6f}, {self.stats['std_y']:.6f}")
        print(f"Coefficients a and b of the best fit line y = a + b * x: a = {self.stats['a']:.6f}, b = {self.stats['b']:.6f}")
        print(f"Standard errors in a and b (SE(a) and SE(b)): SE(a) = {self.stats['SEa']:.6f}, SE(b) = {self.stats['SEb']:.6f}")
        print(f"Correlation coefficient R2: {self.stats['R2']:.6f}")

if __name__ == "__main__":
    # Example usage
    data = LinearRegression()

    # Read data from a file (replace 'data.txt' with your file name)
    # data.read('dta.txt')

    # Alternatively, add data points manually
    data.add(1.0, 2.1)
    data.add(2.0, 4.1)
    data.add(3.0, 6.0)

    # Perform linear regression calculation
    data.stat()

    # Output the results
    data.output()
