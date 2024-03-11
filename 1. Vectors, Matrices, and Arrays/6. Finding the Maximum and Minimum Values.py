# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
# Return maximum element
print(np.max(matrix))
# Return minimum element
print(np.min(matrix))

# Find maximum element in each column
# axis=0 表示沿列逐行进行操作
print(np.max(matrix, axis=0))
# Find maximum element in each row
# axis=1 表示沿行逐列进行操作
print(np.max(matrix, axis=1))