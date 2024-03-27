# Load libraries
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
# Create feature matrix
features = np.array([[2, 3],
[2, 3],
[2, 3]])
# Create PolynomialFeatures object
# degree=2 means we want to generate 2nd degree polynomial features
# include_bias=False means we don't want to include the bias term
polynomial_interaction = PolynomialFeatures(degree=2,
interaction_only=True, include_bias=False)
# Create polynomial features
print(polynomial_interaction.fit_transform(features))