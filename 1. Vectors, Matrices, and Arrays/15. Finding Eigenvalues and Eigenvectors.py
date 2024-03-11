# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, -1, 3],
[1, 1, 6],
[3, 8, 9]])
# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
# View eigenvalues
print(eigenvalues)
# View eigenvectors
print(eigenvectors)