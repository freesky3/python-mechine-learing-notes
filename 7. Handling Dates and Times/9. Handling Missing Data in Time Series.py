# Load libraries
import pandas as pd
import numpy as np
# Create date
time_index = pd.date_range("01/01/2010", periods=5, freq="M")
# Create data frame, set index
dataframe = pd.DataFrame(index=time_index)
# Create feature with a gap of missing values
dataframe["Sales"] = [1.0,2.0,np.nan,np.nan,5.0]
# Interpolate missing values
print(dataframe.interpolate())

# Forward-fill
print(dataframe.ffill())

# Back-fill
print(dataframe.bfill())

# Interpolate missing values
print(dataframe.interpolate(method="quadratic"))

# Interpolate missing values
print(dataframe.interpolate(limit=1, limit_direction="forward"))