import os
import pandas as pd

processed_output_directory = 'processed/PopulationbyStatebyYear/'

population_file_path = os.path.join('processed', 'AgeSexRaceGender', 'AgeSexRaceGender2010to2023-yearlyPopulationAsColumn.csv')
population_data = pd.read_csv(population_file_path)

population_columns = [
    'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013',
    'POPESTIMATE2014', 'POPESTIMATE2015', 'POPESTIMATE2016', 'POPESTIMATE2017',
    'POPESTIMATE2018', 'POPESTIMATE2019', 'POPESTIMATE2020', 'POPESTIMATE2021',
    'POPESTIMATE2022', 'POPESTIMATE2023'
]

# get all sex and all origin
population_data_sex_origin_0 = population_data[(population_data['SEX'] == 0) & (population_data['ORIGIN'] == 0)]

state_population = population_data_sex_origin_0.groupby('NAME')[population_columns].sum().reset_index()

state_population.columns = ['State'] + [int(col.replace('POPESTIMATE', '')) for col in state_population.columns[1:]]

melted_population = state_population.melt(id_vars=['State'], var_name='Year', value_name='Population')

melted_population['Year'] = melted_population['Year'].astype(int)

sorted_population = melted_population.sort_values(by=['State', 'Year'])

os.makedirs(processed_output_directory, exist_ok=True)
output_file_path = os.path.join(processed_output_directory, 'StatePopulation-tidy-yearly.csv')
sorted_population.to_csv(output_file_path, index=False)