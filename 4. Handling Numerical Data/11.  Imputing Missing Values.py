# Load libraries
import numpy as np
from fancyimpute import KNN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
# Make a simulated feature matrix
features, _ = make_blobs(n_samples = 1000,
n_features = 2,
random_state = 1)
# Standardize the features
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)
# Replace the first feature's first value with a missing value
true_value = standardized_features[0,0]
standardized_features[0,0] = np.nan
# Predict the missing values in the feature matrix
features_knn_imputer = KNN(k=5, verbose=0)
features_knn_imputed = features_knn_imputer.fit_transform(standardized_features)
# Compare true and imputed values
print("True Value:", true_value)
print("Imputed Value:", features_knn_imputed[0,0])

print("{:=^50s}".format("Split Line"))

# Load library
from sklearn.impute import SimpleImputer
# Create imputer
mean_imputer = SimpleImputer(strategy="mean")
# Impute values
features_mean_imputed = mean_imputer.fit_transform(features)
# Compare true and imputed values
print("True Value:", true_value)
print("Imputed Value:", features_mean_imputed[0,0])

print("{:=^50s}".format("Split Line"))

from sklearn.impute import KNNImputer
knn_imputer = KNNImputer(n_neighbors=5)
knn_imputed = knn_imputer.fit_transform(features)
print("True Value:", true_value)
print("Imputed Value:", knn_imputed[0,0])