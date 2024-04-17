# Load library
import pandas as pd
# Create datetime
print(pd.Timestamp('2017-05-01 06:00:00', tz='Europe/London'))


# Create datetime
date = pd.Timestamp('2017-05-01 06:00:00')
# Set time zone
date_in_london = date.tz_localize('Europe/London')
# Show datetime
print(date_in_london)


# Change time zone
print(date_in_london.tz_convert('Africa/Abidjan'))


# Create three dates
dates = pd.Series(pd.date_range('2/2/2002', periods=3, freq='M'))
# Set time zone
print(dates.dt.tz_localize('Africa/Abidjan'))


# Load library
from pytz import all_timezones
# Show two time zones
print(all_timezones[:5])