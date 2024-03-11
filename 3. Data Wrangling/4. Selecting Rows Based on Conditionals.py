# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Show top two rows where column 'sex' is 'female'条件判断
print(dataframe[dataframe['Sex'] == 'female'].head(2))

# Filter rows
print(dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 62)])