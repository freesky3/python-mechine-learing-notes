# Load libraries
import numpy as np
import pandas as pd
# Create strings
date_strings = np.array(['03-04-2005 11:35 PM',
'23-05-2010 12:01 AM',
'04-09-2009 09:09 PM'])
# Convert to datetimes
print([pd.to_datetime(date, format='%d-%m-%Y %I:%M %p') for date in date_strings])


# Convert to datetimes
print([pd.to_datetime(date, format="%d-%m-%Y %I:%M %p", errors="coerce")
for date in date_strings])

'''
Code Description Example
%Y Full year 2001
%m Month w/ zero padding 04
%d Day of the month w/ zero padding 09
%I Hour (12hr clock) w/ zero padding 02
%p AM or PM AM
%M Minute w/ zero padding 05
%S Second w/ zero padding 09
'''