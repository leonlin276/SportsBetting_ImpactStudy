
import pandas as pd

# Define the path to the file
file_path = 'toProcess/ProblemGamblingSpending.csv'
output_directory = 'processed/ProblemGamblingSpending/'

# Load the file
df = pd.read_csv(file_path)

# Rename the columns
df.rename(columns={
    'state': 'State',
    'year': 'Year',
    'problem gambling spending': 'ProblemGamblingSpending',
    'per capita': 'PerCapita'
}, inplace=True)

# Convert the Year to integer
df['Year'] = df['Year'].astype(int)

# Convert ProblemGamblingSpending and PerCapita to numeric, setting errors='coerce' to handle non-numeric values
df['ProblemGamblingSpending'] = pd.to_numeric(df['ProblemGamblingSpending'], errors='coerce')
df['PerCapita'] = pd.to_numeric(df['PerCapita'], errors='coerce')

# Replace 0 values in ProblemGamblingSpending and PerCapita with NaN
for col in ['ProblemGamblingSpending', 'PerCapita']:
    df.loc[df[col] == 0, col] = pd.NA



print(df['State'].unique())



# Sort the dataframe by Year and State
df.sort_values(by=['Year', 'State'], ascending=[True, True], inplace=True)



# Save the data to a new CSV file
# Create the directory if it doesn't exist
import os
os.makedirs(output_directory, exist_ok=True)
df.to_csv(f'{output_directory}ProblemGamblingSpending-tidy.csv', index=False)
