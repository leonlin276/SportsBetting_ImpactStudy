
import pandas as pd

# Define the path to the Excel file
excel_file_path = 'toProcess/OnlineSportsBettingRevenueByState.xlsx'
output_directory = 'processed/OnlineSportsBettingRevenueByState/'
file_path_2 = 'toProcess/OnlineSportsBettingRevenueByState-tidy-monthly_Fixed.csv'


# Load the Excel file
excel_file = pd.ExcelFile(excel_file_path)

# Load the csv file
file_2 = pd.read_csv(file_path_2)


# Create an empty DataFrame to store the processed data
processed_data = pd.DataFrame(columns=['State', 'Year', 'Month', 'Revenue', 'Handle', 'Hold', 'Taxes'])

# Iterate through each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Load the sheet into a DataFrame
    df = excel_file.parse(sheet_name)
    # Extract the state from the sheet name
    state = sheet_name.replace('OnlineSportsBetting', '').replace('OnlineSportsBettin', '').strip()
    # Add the state name to each row in the DataFrame
    df['State'] = state
    # Append the data to the processed_data DataFrame
    processed_data = pd.concat([processed_data, df], ignore_index=True)


# Rename the 'Month' column to 'Date'
processed_data.rename(columns={'Month': 'Date'}, inplace=True)


# Convert the 'Revenue', 'Handle', 'Hold', and 'Taxes' columns to numeric
processed_data[['Revenue', 'Handle', 'Hold', 'Taxes']] = processed_data[['Revenue', 'Handle', 'Hold', 'Taxes']].apply(pd.to_numeric, errors='coerce')

# Set 'Revenue', 'Handle', 'Hold', and 'Taxes' to NaN where they are 0
for col in ['Revenue', 'Handle', 'Hold', 'Taxes']:
    processed_data.loc[processed_data[col] == 0, col] = pd.NA



# # Correct the state names in the processed data

# print(sorted(file_2['State'].unique()))
# print(sorted(processed_data['State'].unique()))

# Define the state name substitutions
state_substitutions = {
    'Arizona': 'Arizona',
    'Arkansas': 'Arkansas',
    'Colorado': 'Colorado',
    'Connecticut': 'Connecticut',
    'DC': 'District of Columbia',
    'Delaware': 'Delaware',
    'Illinois': 'Illinois',
    'Indiana': 'Indiana',
    'Iowa': 'Iowa',
    'Kansas': 'Kansas',
    'Kentucky': 'Kentucky',
    'LouisianaMon': 'Louisiana',
    'Maine': 'Maine',
    'Maryland': 'Maryland',
    'Massachusetts': 'Massachusetts',
    'Michigan': 'Michigan',
    'Mississippi': 'Mississippi',
    'Montana': 'Montana',
    'Nevada': 'Nevada',
    'NewHampshire': 'New Hampshire',
    'NewJersey': 'New Jersey',
    'NewYork': 'New York',
    'NorthCarolina': 'North Carolina',
    'Ohio': 'Ohio',
    'Oregon': 'Oregon',
    'Pennsylvania': 'Pennsylvania',
    'RhodeIsland': 'Rhode Island',
    'SouthDakota': 'South Dakota',
    'Tennessee': 'Tennessee',
    'Vermont': 'Vermont',
    'Virgina': 'Virginia',
    'WestVirginia': 'West Virginia',
    'Wyoming': 'Wyoming'
}

# Replace state names in processed_data
processed_data['State'] = processed_data['State'].replace(state_substitutions)



# Extract rows where 'Date' is 'Total'
state_historical_total = processed_data[processed_data['Date'] == 'Total']

# Remove rows where 'Date' is 'Total' in processed_data
processed_data_removeTotal = processed_data[processed_data['Date'] != 'Total']



# Drop the 'Date' and 'Year' columns from state_historical_total
state_historical_total.drop(columns=['Date', 'Year'], inplace=True)
# Reorder the columns to 'State', 'Revenue', 'Handle', 'Hold', 'Taxes'
state_historical_total = state_historical_total[['State', 'Revenue', 'Handle', 'Hold', 'Taxes']]

state_historical_total = state_historical_total.sort_values(by=['State'], ascending=[True])



# Convert 'Date' to datetime format
processed_data_removeTotal['Date'] = pd.to_datetime(processed_data_removeTotal['Date'], errors='coerce')

# Drop rows with NA values in 'Date' column
processed_data_removeTotal.dropna(subset=['Date'], inplace=True)

# Extract the year and month from 'Date'
processed_data_removeTotal['Year'] = processed_data_removeTotal['Date'].dt.year.astype(int)
processed_data_removeTotal['Month'] = processed_data_removeTotal['Date'].dt.month.astype(int)

# Reorder the columns to move 'Date' after 'Month'
processed_data_removeTotal = processed_data_removeTotal[['State', 'Year', 'Month', 'Date', 'Revenue', 'Handle', 'Hold', 'Taxes']]

# Sort the processed data by 'State' (A to Z) and 'Year' (ascending)
processed_data_removeTotal = processed_data_removeTotal.sort_values(by=['State', 'Year', 'Month'], ascending=[True, True, True])


print(processed_data_removeTotal.info())


# Save the data to a new CSV file
# Create the directory if it doesn't exist
import os
os.makedirs(output_directory, exist_ok=True)
state_historical_total.to_csv(f'{output_directory}OnlineSportsBettingRevenueByState-tidy-historicalTotal.csv', index=False)
processed_data_removeTotal.to_csv(f'{output_directory}OnlineSportsBettingRevenueByState-tidy-monthly.csv', index=False)

