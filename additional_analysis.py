# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clean_data import data_clean

# Convert 'DATE OCC' to datetime
data_clean['DATE OCC'] = pd.to_datetime(data_clean['DATE OCC'])

# Create a 'month' column for time series analysis
data_clean['month'] = data_clean['DATE OCC'].dt.to_period('M')

# 1. Crime Trends Over Time
crime_trends = data_clean.groupby('month').size().reset_index(name='total_crimes')
crime_trends['total_crimes'] = pd.to_numeric(crime_trends['total_crimes'], errors='coerce')
crime_trends['month'] = crime_trends['month'].dt.to_timestamp()

plt.figure(figsize=(12, 6))
sns.lineplot(data=crime_trends, x='month', y='total_crimes', marker='o')
plt.title('Crime Trends Over Time (Monthly)')
plt.xlabel('Month')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 2. Crime Distribution by Type
crime_distribution = data_clean['Crm Cd Desc'].value_counts().head(10).reset_index()
crime_distribution.columns = ['Crime Type', 'Count']

plt.figure(figsize=(10, 6))
sns.barplot(data=crime_distribution, x='Count', y='Crime Type', hue='Crime Type', palette='viridis', legend=False)
plt.title('Top 10 Crime Types')
plt.xlabel('Count')
plt.ylabel('Crime Type')
plt.show()

# 3. Age Distribution of Victims
plt.figure(figsize=(12, 6))
sns.histplot(data_clean['Vict Age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution of Victims')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid()
plt.show()

# 4. Crime Count by Day of the Week
data_clean['day_of_week'] = data_clean['DATE OCC'].dt.day_name()
crime_by_day = data_clean['day_of_week'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

plt.figure(figsize=(10, 6))
sns.barplot(x=crime_by_day.index, y=crime_by_day.values, hue=crime_by_day.index, palette='coolwarm', legend=False)
plt.title('Total Crimes by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Crimes')
plt.show()

# 5. Crime Rate by Ethnicity
ethnicity_targeted = data_clean['Vict Descent'].value_counts().reset_index()
ethnicity_targeted.columns = ['Ethnicity', 'Total Incidents']

plt.figure(figsize=(10, 6))
sns.barplot(data=ethnicity_targeted, x='Total Incidents', y='Ethnicity', hue='Ethnicity', palette='viridis', legend=False)
plt.title('Total Incidents by Ethnicity')
plt.xlabel('Total Incidents')
plt.ylabel('Ethnicity')
plt.show()

# 6. Monthly Crime Rate Change
monthly_crime_change = crime_trends['total_crimes'].pct_change() * 100
crime_trends['monthly_change'] = monthly_crime_change

plt.figure(figsize=(12, 6))
sns.lineplot(data=crime_trends, x='month', y='monthly_change', marker='o')
plt.title('Monthly Crime Rate Change (%)')
plt.xlabel('Month')
plt.ylabel('Percentage Change in Crimes')
plt.xticks(rotation=45)
plt.grid()
plt.show()

