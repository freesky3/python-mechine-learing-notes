# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 4],
[2, 5]])
# Calculate inverse of matrix
print(np.linalg.inv(matrix))

# Multiply matrix and its inverse
print(matrix @ np.linalg.inv(matrix))