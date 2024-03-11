# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load dataset
dataframe = pd.read_csv(url)
# View first two rows
print(dataframe.head(2))