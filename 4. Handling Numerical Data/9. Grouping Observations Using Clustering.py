# Load libraries
# 设置环境变量线程为1的目的是为了禁止多线程
# 因为KMeans算法是并行化的，如果开启多线程，会导致内存泄漏
import os
os.environ['OMP_NUM_THREADS'] = '1'

import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
# Make simulated feature matrix
features, _ = make_blobs(n_samples = 50,
n_features = 2,
centers = 3,
random_state = 1)
# Create DataFrame
dataframe = pd.DataFrame(features, columns=["feature_1", "feature_2"])
# Make k-means clusterer
clusterer = KMeans(3, random_state=0)
# Fit clusterer
clusterer.fit(dataframe)
# Predict values
dataframe["group"] = clusterer.predict(dataframe)
# View first few observations
print(dataframe.head(10))