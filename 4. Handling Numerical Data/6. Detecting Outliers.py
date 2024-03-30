# Load libraries
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs
# Create simulated data
# features is a 2D array with 10 observations and 2 features
# _ is a dummy variable that we don't need
features, _ = make_blobs(n_samples = 10,
n_features = 2,
centers = 1,
random_state = 1)
print(features[0, 0])
print(features[0, 1])
# Replace the first observation's values with extreme values
features[0,0] = 10000
features[0,1] = 10000
# Create detector
# contamination parameter is set to 0.1, which means 10% of the data is considered as outliers
outlier_detector = EllipticEnvelope(contamination=.1)
# Fit detector
# 使用fit方法对数据进行训练，训练完成后，模型可以对新数据进行预测
outlier_detector.fit(features)
# Predict outliers
# 11表示正常数据，-1表示异常数据
print(outlier_detector.predict(features))

print("{:=^50s}".format("Split Line"))

# Create one feature
feature = features[:,0]
# Create a function to return index of outliers
def indicies_of_outliers(x):
    # q1 and q3 are the first and third quartiles of the data
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return np.where((x > upper_bound) | (x < lower_bound))
# Run function
print(indicies_of_outliers(feature))