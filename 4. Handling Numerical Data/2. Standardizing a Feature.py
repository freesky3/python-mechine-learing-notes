# Load libraries
import numpy as np
from sklearn import preprocessing
# Create feature
x = np.array([[-1000.1],
[-200.2],
[500.5],
[600.6],
[9000.9]])
# Create scaler
# StandardScaler() is used to standardize the feature
# 这会将数据标准化到平均值为0，方差为1的分布
# 主成分分析（PCA）算法依赖于数据标准化
# 而神经网络模型则不依赖于数据标准化（用最大最小值缩放）
scaler = preprocessing.StandardScaler()
# Transform the feature
standardized = scaler.fit_transform(x)
print(standardized)

print("{:=^50s}".format("Split Line"))

# Print mean and standard deviation
print("Mean:", round(standardized.mean()))
print("Standard deviation:", standardized.std())

print("{:=^50s}".format("Split Line"))

# Create scaler
# RobustScaler() is used to scale the feature based on the interquartile range
# 它会将数据缩放到四分位范围（IQR）的范围内
# 四分位距（interquartile range, IQR），又称四分差.
# 它是描述统计学中的一种方法，以确定第三四分位数和第一四分位数的区别。
# 四分位距是指四分之一的距与方差、标准差一样，表示统计资料中各变量分散情形
# 但四分差更多为一种稳健统计（robust statistic）。
robust_scaler = preprocessing.RobustScaler()
# Transform feature
print(robust_scaler.fit_transform(x))