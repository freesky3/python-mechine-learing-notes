# Load library
import pandas as pd
# Create DataFrame
dataframe = pd.DataFrame()
# Add columns
dataframe['Name'] = ['Jacky Jackson', 'Steven Stevenson']
dataframe['Age'] = [38, 25]
dataframe['Driver'] = [True, False]
# Show DataFrame
print(dataframe)

# Create row
new_person = pd.Series(['Molly Mooney', 40, True], index=['Name','Age','Driver'])
# Append row
dataframe.loc[2] = new_person
dataframe.loc[3] = ["zikai fang", 19, False]
print(dataframe)