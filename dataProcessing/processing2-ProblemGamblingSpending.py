import pandas as pd
import os


output_directory = 'processed/ProblemGamblingSpendingV2/'


# Load the CSV file into a DataFrame
file_path = 'toProcess/ProblemGamblingSpending_RaviUpdate.csv'
df_add = pd.read_csv(file_path)

# Load the second CSV file into another DataFrame
file_path_tidy = 'processed/ProblemGamblingSpending/ProblemGamblingSpending-tidy.csv'
df_tidy = pd.read_csv(file_path_tidy)

# print(df_add)

# Remove commas from the 'ProblemGamblingSpending' column and convert to numeric, forcing errors to NaN
df_add['ProblemGamblingSpending'] = df_add['ProblemGamblingSpending'].str.replace(',', '')
df_add['ProblemGamblingSpending'] = df_add['ProblemGamblingSpending'].str.replace('$', '')
df_add['ProblemGamblingSpending'] = pd.to_numeric(df_add['ProblemGamblingSpending'], errors='coerce')
df_tidy['ProblemGamblingSpending'] = pd.to_numeric(df_tidy['ProblemGamblingSpending'], errors='coerce').astype('Int64')

# print(df_add)
print(df_add.dtypes)

# Update the 'ProblemGamblingSpending' and 'PerCapita' columns in df_tidy with values from df_add for rows where Year == 2021
for state in df_add['State']:
    df_tidy.loc[(df_tidy['State'] == state) & (df_tidy['Year'] == 2021), 'ProblemGamblingSpending'] = df_add.loc[df_add['State'] == state, 'ProblemGamblingSpending'].values[0]
    df_tidy.loc[(df_tidy['State'] == state) & (df_tidy['Year'] == 2021), 'PerCapita'] = df_add.loc[df_add['State'] == state, 'PerCapita'].values[0]


# Replace 0 values in 'ProblemGamblingSpending' and 'PerCapita' with NaN without using replace
df_tidy.loc[df_tidy['ProblemGamblingSpending'] == 0, 'ProblemGamblingSpending'] = pd.NA
df_tidy.loc[df_tidy['PerCapita'] == 0, 'PerCapita'] = pd.NA


# print(df_tidy[df_tidy['Year'] == 2021])
print(df_tidy[df_tidy['Year'] == 2021])

print(df_tidy.dtypes)

# create the directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Save the updated DataFrame to a new CSV file
output_file_path = output_directory + 'ProblemGamblingSpending-tidy-v2.csv'
df_tidy.to_csv(output_file_path, index=False)
