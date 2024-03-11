# Load library
import pandas as pd
# Create URL
url = r"D:\code-learning\python-learning\python辅助\text.xlsx"
# Load data
# sheetname=0 表示工作表1
dataframe = pd.read_excel(url, header=1)
# View the first two rows
print(dataframe.head(2))