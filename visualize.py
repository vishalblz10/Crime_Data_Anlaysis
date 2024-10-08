# Load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the analysis results
from clean_data import data_clean

crime_rate_change = data_clean[data_clean['year'].between(2020, 2023)].groupby('year').size().reset_index(name='total_crimes')

# Calculate percentage change
crime_rate_change['percentage_change'] = crime_rate_change['total_crimes'].pct_change() * 100

# Plot crime rate change
plt.figure(figsize=(10, 5))
sns.lineplot(data=crime_rate_change, x='year', y='total_crimes', marker='o')
plt.title('Crime Rate Change (2020-2023)')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.grid()
plt.show()

# Identify targeted ethnic groups
ethnicity_targeted = data_clean['Vict Descent'].value_counts().reset_index()
ethnicity_targeted.columns = ['ethnicity', 'total_incidents']

# Plot targeted ethnic groups
plt.figure(figsize=(10, 5))
sns.barplot(data=ethnicity_targeted, x='total_incidents', y='ethnicity', hue='ethnicity', palette='viridis', legend=False)
plt.title('Total Incidents by Ethnicity')
plt.xlabel('Total Incidents')
plt.ylabel('Ethnicity')
plt.show()