# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Select unique values
print(dataframe['Sex'].unique())

# Show counts
print(dataframe['Pclass'].value_counts())

# Show number of unique values
print(dataframe['Pclass'].nunique())