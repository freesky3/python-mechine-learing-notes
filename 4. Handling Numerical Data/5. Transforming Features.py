# Load libraries
import numpy as np
from sklearn.preprocessing import FunctionTransformer
# Create feature matrix
features = np.array([[2, 3],
[2, 3],
[2, 3]])
# Define a simple function
def add_ten(x):
    return x + 10
# Create transformer
ten_transformer = FunctionTransformer(add_ten)
# Transform feature matrix
print(ten_transformer.transform(features))

print("{:=^50s}".format("Split Line"))

# Load library
import pandas as pd
# Create DataFrame
df = pd.DataFrame(features, columns=["feature_1", "feature_2"])
# Apply function
print(df.apply(add_ten))