import pandas as pd

# Define the path to the CSV file
csv_file_path = 'toProcess/AllGamingRevenuebyStatebyQuartersince2020Q3-Untidy.csv'
saved_path = 'processed/AllGamingRevenuebyStatebyQuarter/'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Convert all columns except 'State' to numeric
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Multiply all numeric data by 1 million and round to avoid floating-point precision issues
df.iloc[:, 1:] = (df.iloc[:, 1:] * 1_000_000).round(2)

# Remove " ($M)" from column titles
df.columns = df.columns.str.replace(r' \(\$M\)', '', regex=True)

# Pivot the data to have 'Quarter' and 'Year' columns
df = df.melt(id_vars=['State'], var_name='Quarter_Year', value_name='Revenue')

# Split 'Quarter_Year' into 'Quarter' and 'Year', considering 'CY' as well
df[['Quarter', 'Year']] = df['Quarter_Year'].str.extract(r'((?:Q\d|CY)) (\d{4})')

# Drop the 'Quarter_Year' column
df = df.drop(columns=['Quarter_Year'])

# Reorder the columns
df = df[['State', 'Year', 'Quarter', 'Revenue']]

# Sort the DataFrame by 'State', 'Year', and 'Quarter'
df = df.sort_values(by=['State', 'Year', 'Quarter'], ascending=[True, True, True])

# Set 'Revenue' to NaN where 'Revenue' is 0
df.loc[df['Revenue'] == 0, 'Revenue'] = pd.NA

# Convert 'Year' to integer
df['Year'] = df['Year'].astype(int)

# Using info() method
print(df.info())

# Create the 'processed' directory if it doesn't exist
import os
os.makedirs('processed', exist_ok=True)

# Save the processed data to a new CSV file
df.to_csv(saved_path + 'AllGamingRevenuebyStatebyQuarter-tidy-all.csv', index=False)

# Filter the DataFrame to get all data points where Quarter is 'CY'
df_cy = df[df['Quarter'] == 'CY']

# Save the filtered data to a new CSV file
df_cy.to_csv(saved_path + 'AllGamingRevenuebyStatebyQuarter-tidy-yearly.csv', index=False)

# Filter the DataFrame to get all data points where Quarter is not 'CY'
df_not_cy = df[df['Quarter'] != 'CY']

# Save the filtered data to a new CSV file
df_not_cy.to_csv(saved_path + 'AllGamingRevenuebyStatebyQuarter-tidy-quarterly.csv', index=False)