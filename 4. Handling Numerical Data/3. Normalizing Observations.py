# Load libraries
import numpy as np
from sklearn.preprocessing import Normalizer
# Create feature matrix
features = np.array([[0.5, 0.5],
[1.1, 3.4],
[1.5, 20.2],
[1.63, 34.4],
[10.9, 3.3]])
# Create normalizer
normalizer = Normalizer(norm="l2")
# Transform feature matrix
print(normalizer.transform(features))

print("{:=^50s}".format("Split Line"))

print([i[0]**2 + i[1]**2 for i in normalizer.transform(features)])

print("{:=^50s}".format("Split Line"))

# Transform feature matrix
# l1 norm指以和为一归一化
features_l1_norm = Normalizer(norm="l1").transform(features)
# Show feature matrix
print(features_l1_norm)

print("{:=^50s}".format("Split Line"))

# Print sum
print("Sum of the observation\'s values:",
[features_l1_norm[i, 0] + features_l1_norm[i, 1] for i in range(len(features_l1_norm))])