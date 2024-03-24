# 找出NaN的位置
# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
## Select missing values, show two rows
print(dataframe[dataframe['Age'].isnull()].head(2))

# 替换NaN
# Load library
import numpy as np
# Attempt to replace values with NaN
dataframe['Sex'] = dataframe['Sex'].replace('male', np.nan)
print(dataframe['Sex'].head(2))

# 指定缺失值
# Load data, set missing values
dataframe = pd.read_csv(url, na_values=[np.nan, 'NONE', -999, 1])
print(dataframe['PassengerId'].head(2))