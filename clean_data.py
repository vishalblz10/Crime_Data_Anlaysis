# Import necessary libraries
import pandas as pd

# Load the dataset
from read_data import data

# Check for missing values
na_count = data.isnull().sum()
print(na_count)

# Remove rows with missing values and create a new DataFrame
data_clean = data.dropna().copy()  # Create a copy to avoid view issues

# Convert date columns to datetime
data_clean['DATE OCC'] = pd.to_datetime(data_clean['DATE OCC'], errors='coerce')

# Create a new column 'year' using .loc to avoid warnings
data_clean['year'] = data_clean['DATE OCC'].dt.year

# Ensure categorical variables are of type 'category'
data_clean['Vict Descent'] = data_clean['Vict Descent'].astype('category')

# Display summary of cleaned data
data_clean.info()

