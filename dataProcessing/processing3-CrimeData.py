import pandas as pd
import os

input_directory = 'processed/CrimeDataTidy/'
processed_output_directory = 'processed/CrimeDataYearly/'

def import_and_combine_csv_files(input_directory):
    combined_data = []
    for file_name in os.listdir(input_directory):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_directory, file_name)
            df = pd.read_csv(file_path)
            combined_data.append(df)
            print(f'Imported {file_path}')
    combined_df = pd.concat(combined_data, ignore_index=True)
    return combined_df

crime_data_full = import_and_combine_csv_files(input_directory)


crime_data_subset1 = crime_data_full[['STATE', 'DIV', 'YEAR', 'StateCaseNumYearly']]


# Group by STATE, DIV, YEAR, and StateCaseNumYearly without aggregation
grouped_data = crime_data_subset1.groupby(['STATE', 'DIV', 'YEAR', 'StateCaseNumYearly']).first().reset_index()



state_dict = {
    1: "Alabama",
    2: "Arizona",
    3: "Arkansas",
    4: "California",
    5: "Colorado",
    6: "Connecticut",
    7: "Delaware",
    8: "District of Columbia",
    9: "Florida",
    10: "Georgia",
    11: "Idaho",
    12: "Illinois",
    13: "Indiana",
    14: "Iowa",
    15: "Kansas",
    16: "Kentucky",
    17: "Louisiana",
    18: "Maine",
    19: "Maryland",
    20: "Massachusetts",
    21: "Michigan",
    22: "Minnesota",
    23: "Mississippi",
    24: "Missouri",
    25: "Montana",
    26: "Nebraska",
    27: "Nevada",
    28: "New Hampshire",
    29: "New Jersey",
    30: "New Mexico",
    31: "New York",
    32: "North Carolina",
    33: "North Dakota",
    34: "Ohio",
    35: "Oklahoma",
    36: "Oregon",
    37: "Pennsylvania",
    38: "Rhode Island",
    39: "South Carolina",
    40: "South Dakota",
    41: "Tennessee",
    42: "Texas",
    43: "Utah",
    44: "Vermont",
    45: "Virginia",
    46: "Washington",
    47: "West Virginia",
    48: "Wisconsin",
    49: "Wyoming",
    50: "Alaska",
    51: "Hawaii",
    52: "Canal Zone",
    53: "Puerto Rico",
    54: "American Samoa",
    55: "Guam",
    62: "Virgin Islands"
}

# Map the STATE column to the state names using the state_dict
grouped_data['State'] = grouped_data['STATE'].map(state_dict)

# Rename the column 'STATE' to 'STATECODE'
grouped_data.rename(columns={'STATE': 'STATECODE'}, inplace=True)



# Create the output directory if it doesn't exist
os.makedirs(processed_output_directory, exist_ok=True)

# Define the output file path
output_file_path = os.path.join(processed_output_directory, '2012to2022_CrimeData-tidy-yearly.csv')

# Save the grouped dataframe to a new CSV file
grouped_data.to_csv(output_file_path, index=False)
print(f'Grouped data saved to {output_file_path}')
