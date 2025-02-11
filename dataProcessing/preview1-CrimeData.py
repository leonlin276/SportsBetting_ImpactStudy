import pandas as pd


# Load the TSV file into a DataFrame
file_path = 'toProcess\CrimeDataTsvs/2012CrimeData.tsv'
df = pd.read_csv(file_path, sep='\t')

# Display the first few rows of the DataFrame
print(df.head())

# Print the unique values of the 'month' column
print(df['MONTH'].unique())