import pandas as pd
import os


def process1_crime_data(file_path):
    processed1_output_directory = 'processed/CrimeDataTidy/'

    # Read the CSV file
    crime_data = pd.read_csv(file_path)


    # Convert YEAR, POP, and MONTH columns to integers
    crime_data['STATE'] = crime_data['STATE'].astype(int)
    crime_data['DIV'] = crime_data['DIV'].astype(int)
    crime_data['YEAR'] = crime_data['YEAR'].astype(int)
    crime_data['COUNTY'] = crime_data['COUNTY'].astype(int)
    crime_data['POP'] = crime_data['POP'].astype(int)
    # Remove non-numeric values from the MONTH column
    # crime_data = crime_data[pd.to_numeric(crime_data['MONTH'], errors='coerce').notnull()]
    crime_data['MONTH'] = crime_data['MONTH'].astype(int)

    # # Remove all rows where MONTH == 98
    # crime_data = crime_data[crime_data['MONTH'] != 98]
    
    original_state_name_list.extend(crime_data['STNAME'].unique())

    # Dictionary to map state abbreviations to formal state names

    # Define a dictionary to map the provided abbreviations and informal names to formal state names
    # state_name_mapping = {}

    # # Replace state abbreviations with formal state names
    # crime_data['STNAME'] = crime_data['STNAME'].replace(state_name_mapping)

    corrected_state_name_list.extend(crime_data['STNAME'].unique())


    # Count the number of occurrences where the value of YEAR, STNAME is the same
    case_num_data = crime_data.groupby(['STATE', 'YEAR']).size().reset_index(name='StateCaseNumYearly')
    
    # print(case_num_data.columns)


    # Merge
    result_data = pd.merge(crime_data, case_num_data, on=['STATE', 'YEAR'])


    # # Add a new column 'Date' by combining YEAR and MONTH
    # result_data['Date'] = pd.to_datetime(result_data['YEAR'].astype(str) + '-' + result_data['MONTH'].astype(str))

    # Reorder columns as DIV, STNAME, YEAR, MONTH, Date, STPOP, CaseNum
    result_data = result_data[['STATE', 'DIV', 'STNAME', 'COUNTY', 'YEAR', 'MONTH', 'POP', 'StateCaseNumYearly', 'OFFENSE']]


    # # Calculate the crime rate by dividing CaseNum by STPOP
    # result_data['CrimeRate'] = result_data['CaseNum'] / result_data['STPOP']


    # Create the output directory if it doesn't exist
    os.makedirs(processed1_output_directory, exist_ok=True)

    # Define the output file path
    output_file_path = os.path.join(processed1_output_directory, os.path.basename(file_path).replace('Air.csv','-tidy.csv'))

    # Save the dataframe to the new CSV file
    result_data.to_csv(output_file_path, index=False)



# Process all CSV files in the directory
input_directory = 'toProcess/CrimeDataTsvsAir/'
# State Name List
original_state_name_list = []
corrected_state_name_list = []

for file_name in os.listdir(input_directory):
    if file_name.endswith('.csv'):
        file_path = os.path.join(input_directory, file_name)
        process1_crime_data(file_path)
        print(f'Processed {file_path}')


# Make the state names in the list unique
original_state_name_list = list(set(original_state_name_list))
corrected_state_name_list = list(set(corrected_state_name_list))

# Print the unique state names
print('Original State Name List:', original_state_name_list)
# print('Corrected State Name List:', corrected_state_name_list)