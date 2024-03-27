# Load library
import pandas as pd
# Create DataFrame
data_a = {'id': ['1', '2', '3'],
'first': ['Alex', 'Amy', 'Allen'],
'last': ['Anderson', 'Ackerman', 'Ali']}
dataframe_a = pd.DataFrame(data_a, columns = ['id', 'first', 'last'])
# Create DataFrame
data_b = {'id': ['4', '5', '6'],
'first': ['Billy', 'Brian', 'Bran'],
'last': ['Bonder', 'Black', 'Balwner']}
dataframe_b = pd.DataFrame(data_b, columns = ['id', 'first', 'last'])
# Concatenate DataFrames by rows
# axis=0 means concatenate by rows; axis=1 means concatenate by columns
print(pd.concat([dataframe_a, dataframe_b], axis=0))
# Create row
row = pd.Series([10, 'Chris', 'Chillon'], index=['id', 'first', 'last'])
# Append row
print(pd.concat([dataframe_a, dataframe_b, row],ignore_index=True)) 