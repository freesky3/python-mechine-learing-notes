# Load libraries
import numpy as np
from sklearn.preprocessing import Binarizer
# Create feature
age = np.array([[6],
[12],
[20],
[36],
[65]])
# Create binarizer
binarizer = Binarizer(threshold=18)
# Transform feature
print(binarizer.fit_transform(age))

print("{:=^50s}".format("Split Line"))

# Bin feature
print(np.digitize(age, bins=[20,30,64]))

print("{:=^50s}".format("Split Line"))

print(np.digitize(age, bins=[20,30,64], right=True))

print("{:=^50s}".format("Split Line"))

# Bin feature
print(np.digitize(age, bins=[18]))