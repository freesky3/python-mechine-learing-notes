# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Calculate statistics
print('Maximum:', dataframe['Age'].max())
print('Minimum:', dataframe['Age'].min())
print('Mean:', dataframe['Age'].mean())
print('Sum:', dataframe['Age'].sum())
print('Count:', dataframe['Age'].count())

print("{:=^50s}".format("Split Line"))

# Show counts
print(dataframe.count())