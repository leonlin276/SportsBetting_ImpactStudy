
import pandas as pd

# Define the path to the Excel file
excel_file_path = 'toProcess/MonthlyRevenueForEachState2012to2024.xlsx'
output_directory = 'processed/MonthlyRevenueForEachState2012to2024/'

# Load the Excel file
excel_file = pd.ExcelFile(excel_file_path)

# Create an empty DataFrame to store the processed data
processed_data = pd.DataFrame(columns=['State', 'Year', 'Month', 'Revenue'])

# Iterate through each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Load the sheet into a DataFrame
    df = excel_file.parse(sheet_name)
    
    # Extract the year from the sheet name
    year = int(sheet_name)
    
    # Melt the DataFrame to have 'State' and 'Revenue' columns
    df_melted = df.melt(id_vars=['Month'], var_name='State', value_name='Revenue')
    
    # Add the 'Year' column
    df_melted['Year'] = year
    
    # Append the processed data to the main DataFrame
    processed_data = pd.concat([processed_data, df_melted], ignore_index=True)



# Replace 'Total USA' with 'United States' in the 'State' column
processed_data['State'] = processed_data['State'].replace('Total USA', 'United States')
processed_data['State'] = processed_data['State'].replace('Total', 'United States')

print(processed_data['State'].unique())


# Replace 'Total' with 'YTD Total' in the 'Month' column
processed_data['Month'] = processed_data['Month'].replace('Total', 'YTD Total')


# Convert 'Year' to integer
processed_data['Year'] = processed_data['Year'].astype(int)

# Convert the 'Revenue' column to numeric
processed_data['Revenue'] = pd.to_numeric(processed_data['Revenue'], errors='coerce')

# Set 'Revenue' to NaN where 'Revenue' is 0
processed_data.loc[processed_data['Revenue'] == 0, 'Revenue'] = pd.NA



# Sort the processed data by 'State' (A to Z) and 'Year' (ascending)
processed_data = processed_data.sort_values(by=['State', 'Year'], ascending=[True, True])



# Create a 'Date' column from 'Year' and 'Month'
processed_data['Date'] = pd.to_datetime(processed_data['Year'].astype(str) + '-' + processed_data['Month'], format='%Y-%B', errors='coerce')



# Reorder the columns to move 'Date' after 'Month'
processed_data = processed_data[['State', 'Year', 'Month', 'Date', 'Revenue']]



print(processed_data.info())



# Create the directory if it doesn't exist
import os
os.makedirs(output_directory, exist_ok=True)

# Save the processed data to a new CSV file
processed_data.to_csv(f'{output_directory}MonthlyRevenueForEachState2012to2024-tidy-all.csv', index=False)


# Extract rows where 'Month' is 'YTD Total'
yearly_data = processed_data[processed_data['Month'] == 'YTD Total']

# Save the YTD Total data to a new CSV file
yearly_data.to_csv(f'{output_directory}MonthlyRevenueForEachState2012to2024-tidy-yearly.csv', index=False)


# Extract rows where 'Month' is not 'YTD Total'
monthly_data = processed_data[processed_data['Month'] != 'YTD Total']

# Save the monthly data to a new CSV file
monthly_data.to_csv(f'{output_directory}MonthlyRevenueForEachState2012to2024-tidy-monthly.csv', index=False)
