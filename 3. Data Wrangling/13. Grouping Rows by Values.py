# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Group rows by the values of the column 'Sex',
# calculate mean of each group
print(dataframe.groupby('Sex')[['Age', 'Survived', 'Pclass']].mean())
print(dataframe.groupby('Sex')[['Age', 'Survived', 'Pclass']].count())