# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Rename column, show two rows
print(dataframe.rename(columns={'Survived': '存活'}).head(2))

# Rename columns, show two rows
print(dataframe.rename(columns={'Survived': '存活', 'PassengerId': '编号'}).head(2))

# Load library
import collections
# Create dictionary
column_names = collections.defaultdict(str)
# Create keys
for name in dataframe.columns:
    column_names[name]
# Show dictionary
print(column_names)