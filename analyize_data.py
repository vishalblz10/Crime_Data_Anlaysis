# Import necessary libraries
import pandas as pd
from clean_data import data_clean

# Calculate crime rate change from 2020 to 2023
crime_rate_change = data_clean[data_clean['year'].between(2020, 2023)].groupby('year').size().reset_index(name='total_crimes')

# Calculate percentage change
crime_rate_change['percentage_change'] = crime_rate_change['total_crimes'].pct_change() * 100

# Display the crime rate change
print(crime_rate_change)

# Identify targeted ethnic groups
ethnicity_targeted = data_clean['Vict Descent'].value_counts().reset_index()
ethnicity_targeted.columns = ['ethnicity', 'total_incidents']

# Display targeted ethnic groups
print(ethnicity_targeted)
