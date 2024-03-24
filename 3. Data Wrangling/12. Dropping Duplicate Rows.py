# 删除重复行
# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Drop duplicates, show first two rows of output
print(dataframe.drop_duplicates().head(2))

# Show number of rows
print("Number Of Rows In The Original DataFrame:", len(dataframe))
print("Number Of Rows After Deduping:", len(dataframe.drop_duplicates()))
# 两次结果一样，说明没有重复行

# 默认保留先出现的行
# Drop duplicates
print(dataframe.drop_duplicates(subset=['Pclass'])['Pclass'])

# 控制保留的行
# Drop duplicates
print(dataframe.drop_duplicates(subset=['Pclass'], keep='last')['Pclass'])

# 返回布尔序列
# keep must be either "first", "last" or False
is_duplicated = dataframe.duplicated(subset=['Pclass'], keep=False)
print(dataframe['Pclass'][is_duplicated])