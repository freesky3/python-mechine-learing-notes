# Load library
import pandas as pd
# Create DataFrame
employee_data = {'employee_id': ['1', '2', '3', '4'],
'name': ['Amy Jones', 'Allen Keys', 'Alice Bees',
'Tim Horton']}
dataframe_employees = pd.DataFrame(employee_data, columns = ['employee_id',
'name'])
# Create DataFrame
sales_data = {'employee_id': ['3', '4', '5', '6'],
'total_sales': [23456, 2512, 2345, 1455]}
dataframe_sales = pd.DataFrame(sales_data, columns = ['employee_id',
'total_sales'])
# Merge DataFrames
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id'))
# Merge DataFrames
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer'))
# Merge DataFrames
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='left'))
# Merge DataFrames
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='right'))
# Merge DataFrames
# If column names are different in both DataFrames, use left_on and right_on parameters to specify the column names in each DataFrame.
print(pd.merge(dataframe_employees, dataframe_sales, left_on='employee_id', right_on='employee_id'))
print(pd.merge(dataframe_employees, dataframe_sales, left_index=False, right_index=False))
print(pd.merge(dataframe_employees, dataframe_sales, left_index=True, right_index=True))