# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
# Flatten matrix
print(matrix.flatten('C'))
print(matrix.flatten('F'))