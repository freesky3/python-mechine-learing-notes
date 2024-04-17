# Load library
import pandas as pd
# Create dates
dates = pd.Series(pd.date_range("2/2/2002", periods=3, freq="M"))
# Show days of the week
print(dates.dt.day_name())

# Show days of the week
print(dates.dt.weekday)