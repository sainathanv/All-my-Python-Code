import numpy as np

# Create two arrays
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Basic operations
print("Array a:", a)
print("Array b:", b)

print("a + b =", a + b)
print("a * b =", a * b)

# matrix_1 operations
matrix_1 = np.array([[1, 2],
                   [3, 4]])
matrix_2 = np.array([[5,6],
                    [9, 0]])

print("\nmatrix_1:")
print(matrix_1)

print("Transpose:")
print(matrix_1.T)

print("matrix_1 * matrix_2:")
print(matrix_1 @ matrix_2)

# Statistical operations
print("\nMean of a:", np.mean(a))
print("Standard deviation of a:", np.std(a))

# Check NumPy version
print("\nNumPy version:", np.__version__)
