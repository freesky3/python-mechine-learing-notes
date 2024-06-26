# Load library
import pandas as pd
# Create data frame
dataframe = pd.DataFrame()
# Create datetimes
dataframe['date'] = pd.date_range('1/1/2001', periods=100000, freq='H')
# Select observations between two datetimes
print(dataframe[(dataframe['date'] > '2002-1-1 01:00:00') &
(dataframe['date'] <= '2002-1-1 04:00:00')])


# Set index
dataframe = dataframe.set_index(dataframe['date'])
# Select observations between two datetimes
print(dataframe.loc['2002-1-1 01:00:00':'2002-1-1 04:00:00'])