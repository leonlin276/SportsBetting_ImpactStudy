
import pandas as pd

# Define the path to the file
file_path_1 = 'toProcess/AgeSexRaceGender2010to2019.csv'
file_path_2 = 'toProcess/AgeSexRaceGender2020to2023.csv'
output_directory = 'processed/AgeSexRaceGender/'

# Load the file
df_1 = pd.read_csv(file_path_1)
df_2 = pd.read_csv(file_path_2)


# Remove the columns 'CENSUS2010POP' and 'ESTIMATESBASE2010' from df_1
df_1.drop(columns=['CENSUS2010POP', 'ESTIMATESBASE2010'], inplace=True)

# Remove the column 'ESTIMATESBASE2020' from df_2
df_2.drop(columns=['ESTIMATESBASE2020'], inplace=True)


# Merge the dataframes on the specified columns
df_merged = pd.merge(df_1, df_2, on=['SUMLEV', 'REGION', 'DIVISION', 'STATE', 'NAME', 'SEX', 'ORIGIN', 'RACE', 'AGE'], how='outer')


# Check the unique values in the 'NAME' column
print(df_merged['NAME'].unique())


# # A tidy version of the data
# df_tidy = df_merged.copy()

# # Remove 'POPESTIMATE' from column titles
# df_tidy.columns = df_tidy.columns.str.replace('POPESTIMATE', '')


# # Melt the dataframe to have 'Year' and 'Population' columns
# df_tidy = df_tidy.melt(id_vars=['SUMLEV', 'REGION', 'DIVISION', 'STATE', 'NAME', 'SEX', 'ORIGIN', 'RACE', 'AGE'], 
#                        value_vars=['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'], 
#                        var_name='Year', 
#                        value_name='Population')

# # Save the data to a new CSV file
# # Create the directory if it doesn't exist
# import os
# os.makedirs(output_directory, exist_ok=True)
# df_tidy.to_csv(f'{output_directory}AgeSexRaceGender2010to2023-temp.csv', index=False)



# Save the data to a new CSV file
# Create the directory if it doesn't exist
import os
os.makedirs(output_directory, exist_ok=True)
df_merged.to_csv(f'{output_directory}AgeSexRaceGender2010to2023-yearlyPopulationAsColumn.csv', index=False)
