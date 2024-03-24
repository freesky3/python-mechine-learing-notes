# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Replace values, show two rows
print(dataframe['Sex'].replace("female", "Woman").head(2))
print(dataframe['Sex'].replace(["male", "female"], ["男", "女"]).head(5))
print(dataframe.replace(1, "One").head(2))
# 参数 regex=True 表示 replace 方法将使用正则表达式进行匹配
print(dataframe.replace(r"1st", "First", regex=True).head(2))