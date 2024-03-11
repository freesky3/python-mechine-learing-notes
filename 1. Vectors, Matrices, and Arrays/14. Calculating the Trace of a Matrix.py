# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 2, 3],
[2, 4, 6],
[3, 8, 9]])
# Return trace
print(matrix.trace())

# Return diagonal and sum elements
print(sum(matrix.diagonal(offset=1)))