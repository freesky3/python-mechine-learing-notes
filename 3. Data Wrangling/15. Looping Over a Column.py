# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Print first two names uppercased
print(dataframe['Name'][0:2])
for name in dataframe['Name'][0:2]:
    print(name.upper())