# Load library
import numpy as np
# Create 4x3 matrix
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12]])
# Reshape matrix into 2x6 matrix
print(matrix.reshape(2, 6))
# 化为一行矩阵
print(matrix.reshape(1, -1))
# 化为一行向量
print(matrix.reshape(12))