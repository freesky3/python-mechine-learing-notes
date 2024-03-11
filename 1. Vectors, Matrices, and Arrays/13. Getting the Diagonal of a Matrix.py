# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 2, 3],
[2, 4, 6],
[3, 8, 9]])
# Return diagonal elements
print(matrix.diagonal())

# Return diagonal one above the main diagonal
print(matrix.diagonal(offset=1))
# Return diagonal one below the main diagonal
print(matrix.diagonal(offset=-1))