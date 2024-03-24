# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# 对照组
print(dataframe.head(2))
# Delete column
print(dataframe.drop('PassengerId', axis=1).head(2))
# Drop columns
print(dataframe.drop(['PassengerId', 'Survived'], axis=1).head(2))
# 尽量不要改动原数据，可以添加新数据接受修改后的数据