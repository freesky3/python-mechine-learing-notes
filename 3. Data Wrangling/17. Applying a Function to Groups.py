# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Group rows, apply function to groups
print(dataframe.groupby('Sex').apply(lambda x: x.count()))
print(dataframe.groupby('Sex')[['Age', 'Survived']].apply(lambda x: x.mean()))