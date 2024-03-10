# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python mechine learing辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Select first row
print(dataframe.iloc[0])
print(dataframe.loc[0])

print("{:=^50s}".format("Split Line"))

# Set index 设定索引的列
dataframe = dataframe.set_index(dataframe['Survived'])
# Show row 对索引所在列进行搜索
print(dataframe.loc[1].head(2))