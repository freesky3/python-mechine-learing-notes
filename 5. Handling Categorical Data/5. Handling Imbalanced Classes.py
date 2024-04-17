# Load libraries
# 方法一：调整权重给予同等重视
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
# Load iris data
iris = load_iris()
# Create feature matrix
features = iris.data
# Create target vector
target = iris.target
# Remove first 40 observations
features = features[40:,:]
target = target[40:]
# Create binary target vector indicating if class 0
target = np.where((target == 0), 0, 1)
# Look at the imbalanced target vector
print(target)

print("{:=^50s}".format("Split Line"))

# Create weights
weights = {0: .9, 1: 0.1}
# Create random forest classifier with weights
print(RandomForestClassifier(class_weight=weights))

print("{:=^50s}".format("Split Line"))

# Train a random forest with balanced class weights
# 调整权重给予同等重视
print(RandomForestClassifier(class_weight="balanced"))

print("{:=^50s}".format("Split Line"))

# 方法二：调整采样方式
# Indicies of each class' observations
i_class0 = np.where(target == 0)[0]
i_class1 = np.where(target == 1)[0]
# Number of observations in each class
n_class0 = len(i_class0)
n_class1 = len(i_class1)
# For every observation of class 0, randomly sample
# from class 1 without replacement
i_class1_downsampled = np.random.choice(i_class1, size=n_class0, replace=False)
# Join together class 0's target vector with the
# downsampled class 1's target vector
print(np.hstack((target[i_class0], target[i_class1_downsampled])))

print("{:=^50s}".format("Split Line"))

# Join together class 0's feature matrix with the
# downsampled class 1's feature matrix
print(np.vstack((features[i_class0,:], features[i_class1_downsampled,:]))[0:5])

print("{:=^50s}".format("Split Line"))

# 方法三：增大少数类别的样本数
# For every observation in class 1, randomly sample from class 0 with replacement
i_class0_upsampled = np.random.choice(i_class0, size=n_class1, replace=True)
# Join together class 0's upsampled target vector with class 1's target vector
print(np.concatenate((target[i_class0_upsampled], target[i_class1])))
print(np.vstack((features[i_class0_upsampled,:], features[i_class1,:]))[0:5])