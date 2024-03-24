# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\train.csv"
# Load data
dataframe = pd.read_csv(url)
# Create function
def uppercase(x):
    return x.upper()
# Apply function, show two rows
print(dataframe['Name'].apply(uppercase)[0:2])