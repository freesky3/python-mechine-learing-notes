# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python mechine learing辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Show two rows
print(dataframe.head(2))

# Show dimensions
print(dataframe.shape)

# Show statistics
print(dataframe.describe())