# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Delete rows, show first two rows of output
print(dataframe[dataframe['Survived'] != 1].head(2))
print(dataframe.drop(0, axis=0).head(2))
# 这里不同的是，方括号里面并不代表范围
print(dataframe.drop([0, 2], axis=0).head(2))
# Delete row, show first two rows of output
print(dataframe[dataframe.index != 0].head(2))