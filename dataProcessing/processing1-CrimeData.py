import pandas as pd
import os


def process1_crime_data(file_path):
    processed1_output_directory = 'toProcess/CrimeDataTsvsAir/'

    # Read the TSV file
    crime_data = pd.read_csv(file_path, sep='\t')

    # Select the specified columns
    crime_data = crime_data[['STATE', 'DIV', 'YEAR', 'COUNTY', 'POP', 'STNAME', 'MONTH', 'OFFENSE']]

    # Create the output directory if it doesn't exist
    os.makedirs(processed1_output_directory, exist_ok=True)

    # Define the output file path
    output_file_path = os.path.join(processed1_output_directory, os.path.basename(file_path).replace('.tsv', 'Air.csv'))

    # Save the dataframe to the new CSV file
    crime_data.to_csv(output_file_path, index=False)



# Process all CSV files in the directory
input_directory = 'toProcess/CrimeDataTsvs/'
for file_name in os.listdir(input_directory):
    if file_name.endswith('.tsv'):
        file_path = os.path.join(input_directory, file_name)
        process1_crime_data(file_path)
        print(f'Processed {file_path}')

