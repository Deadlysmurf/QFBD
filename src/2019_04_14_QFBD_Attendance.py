#Import packages
import pandas as pd
import pybaseball

## The Data
years = range(1977, 2019)

raw_data = pd.DataFrame()

for i in years:
    data_load = pybaseball.schedule_and_record(i, 'TOR')
    data_load['Year'] = i
    raw_data = pd.concat([raw_data, data_load], axis=0, join='outer', join_axes=None, ignore_index=True)

#Data Prep
home_only = raw_data[raw_data['Home_Away'] == 'Home']

home_only = home_only.dropna(subset=['Attendance'])

home_only.sort_values('Attendance', inplace=True)

#Final Answer
print(home_only[['Date', 'Year', 'Tm', 'Opp', 'Attendance']].head())
