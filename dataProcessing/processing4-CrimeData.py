import os
import pandas as pd


input_directory1 = 'processed/CrimeDataYearly/'
input_directory2 = 'processed/PopulationbyStatebyYear/'
processed_output_directory = 'processed/State_Year_Population_CrimeRate/'

file_path1 = os.path.join(input_directory1, '2012to2022_CrimeData-tidy-yearly.csv')
crimedata_yearly = pd.read_csv(file_path1)
file_path2 = os.path.join(input_directory2, 'StatePopulation-tidy-yearly.csv')
population_data = pd.read_csv(file_path2)


merged_data = pd.merge(crimedata_yearly, population_data, left_on=['YEAR', 'State'], right_on=['Year', 'State'])
merged_data = merged_data.drop(columns=['YEAR'])

merged_data = merged_data[['STATECODE', 'DIV', 'State', 'Year', 'Population', 'StateCaseNumYearly']]

merged_data['CrimeRate'] = merged_data['StateCaseNumYearly'] / merged_data['Population']



os.makedirs(processed_output_directory, exist_ok=True)
output_file_path = os.path.join(processed_output_directory, 'StatePopulationCrimeRate-tidy-yearly.csv')
merged_data.to_csv(output_file_path, index=False)
print(f'Processed {output_file_path}')
