# Sports Betting Impact Study

## Project Overview

This project aims to analyze the impact of sports betting on various metrics such as gaming revenue, crime data, and problem gambling spending across different states in the United States. The data spans multiple years and includes detailed information on monthly and quarterly revenues, crime rates, and other relevant statistics.


## Data Sources

### Processed Data

- **AllGamingRevenuebyStatebyQuarter**
  - [AllGamingRevenuebyStatebyQuarter-tidy-all.csv](dataProcessing/processed/AllGamingRevenuebyStatebyQuarter/AllGamingRevenuebyStatebyQuarter-tidy-all.csv)
  - [AllGamingRevenuebyStatebyQuarter-tidy-quarterly.csv](dataProcessing/processed/AllGamingRevenuebyStatebyQuarter/AllGamingRevenuebyStatebyQuarter-tidy-quarterly.csv)
  - [AllGamingRevenuebyStatebyQuarter-tidy-yearly.csv](dataProcessing/processed/AllGamingRevenuebyStatebyQuarter/AllGamingRevenuebyStatebyQuarter-tidy-yearly.csv)
  - [CodeBook.md](dataProcessing/processed/AllGamingRevenuebyStatebyQuarter/CodeBook.md)

- **MonthlyRevenueForEachState2012to2024**
  - [MonthlyRevenueForEachState2012to2024-tidy-all.csv](dataProcessing/processed/MonthlyRevenueForEachState2012to2024/MonthlyRevenueForEachState2012to2024-tidy-all.csv)
  - [MonthlyRevenueForEachState2012to2024-tidy-monthly.csv](dataProcessing/processed/MonthlyRevenueForEachState2012to2024/MonthlyRevenueForEachState2012to2024-tidy-monthly.csv)
  - [MonthlyRevenueForEachState2012to2024-tidy-yearly.csv](dataProcessing/processed/MonthlyRevenueForEachState2012to2024/MonthlyRevenueForEachState2012to2024-tidy-yearly.csv)
  - [CodeBook.md](dataProcessing/processed/MonthlyRevenueForEachState2012to2024/CodeBook.md)

- **OnlineSportsBettingRevenueByState**
  - [OnlineSportsBettingRevenueByState-tidy-historicalTotal.csv](dataProcessing/processed/OnlineSportsBettingRevenueByState/OnlineSportsBettingRevenueByState-tidy-historicalTotal.csv)
  - [OnlineSportsBettingRevenueByState-tidy-monthly.csv](dataProcessing/processed/OnlineSportsBettingRevenueByState/OnlineSportsBettingRevenueByState-tidy-monthly.csv)
  - [CodeBook.md](dataProcessing/processed/OnlineSportsBettingRevenueByState/CodeBook.md)

- **CrimeData**
  - [StatePopulation-tidy-yearly.csv](dataProcessing/processed/PopulationbyStatebyYear/StatePopulation-tidy-yearly.csv)
  - [2012to2022_CrimeData-tidy-yearly.csv](dataProcessing/processed/CrimeDataYearly/2012to2022_CrimeData-tidy-yearly.csv)


## Final Report

- **FinalReport-final.ipynb**
  - Jupyter notebook containing the final analysis and visualizations.
  - [Notebook](FinalReport-final.ipynb)


## Project Work

### Data Preprocessing Scripts

1. **processing-AllGamingRevenuebyStatebyQuartersince2020Q3-Untidy.py**:
   - Converts columns to numeric, scales data, and cleans column titles.
   - Melts the data and separate 'Quarter' and 'Year' columns.
   - Reorders and sorts the DataFrame.
   - Handles zero revenue values by setting them to NaN.
   - Saves the processed data to new CSV files for all data, yearly data, and quarterly data.

2. **processing-MonthlyRevenueForEachState2012to2024.py**:
    - Loads and processes data from an Excel file with multiple sheets (each sheet a year) containing monthly revenue for each state.
    - Melts the data to have 'State' and 'Revenue' columns, and adds 'Year' and 'Date' columns.
    - Standardizes the name and data type of value to align with other datasets. 
    - Handles zero values and sorts the data.
    - Saves the processed data to new CSV files for all data, yearly data, and monthly data.

3. **processing-OnlineSportsBettingRevenueByState.py**:
    - Loads and processes data from an Excel file with multiple sheets (each sheet a state) containing online sports betting revenue by state.
    - Cleans and formats the data, including handling zero values and correcting state names.
    - Saves the processed data to new CSV files for historical totals and monthly data.

4. **processing1-AgeSexRaceGender.py**:
   - Merges two CSV files containing population data by age, sex, race, and gender from two different time range.
   - Saves the merged data to a new CSV file.

5. **processing2-AgeSexRaceGender.py**:
   - Groups and sums population data by state name and year.
   - Standardizes the name of column titles to align with other datasets. 
   - Melts the data to have 'Year' and 'Population' columns.
   - Saves the processed data to a new CSV file.

6. **processing1-CrimeData.py**:
   - Extracts specific columns to use from large raw TSV files (5.63 GB in total), which are not included in this repository. See the [source data here](https://www.icpsr.umich.edu/web/ICPSR/series/57). 
   - Saves the data to new CSV files.

7. **processing2-CrimeData.py**:
   - Converts columns to integers and counts the number of cases per state and year.
   - Examines unexpected error values in datasets. 
   - Merges the data and reorders columns.
   - Saves the processed data to a new CSV file.

8. **processing3-CrimeData.py**:
   - Combines multiple CSV files containing yearly crime data into one.
   - Groups the data by state, division, year, and case number.
   - Maps state codes to state names and renames columns.
   - Saves the grouped data to a new CSV file.

9. **processing4-CrimeData.py**:
   - Merges crime data with population data by state and year.
   - Calculates crime rates by dividing the number of cases by the population.
   - Saves the merged and processed data to a new CSV file.

10. **processing1-ProblemGamblingSpending.py**:
   - Renames columns, converts data types, and replaces zero values with NaN, standardizing this datasets to align with other.
   - Sorts the data and saves it to a new CSV file.

11. **processing2-ProblemGamblingSpending.py**:
   - Updates error spending data of the year 2021 to the latest correct version handed over from data collector in this project. 
   - Replaces zero values with NaN.
   - Saves the updated data to a new CSV file.


### Data Analysis Report

1. **Data Preparation**
  - Imported processed datasets to pandas dataframe and clearly annotates them for collaborative use with team members. 

2. **Dataframes Initialization**
  - **State Revenue Data**: Initialized dataframes for yearly and monthly gambling revenue for each state.
  - **Sports Betting Revenue Data**: Initialized dataframes for monthly and yearly online sports betting revenue.
  - **Problem Gambling Spending Data**: Initialized dataframe for problem gambling spending.
  - **Crime Data**: Initialized dataframe for crime data by state and year.
  - **Demographic Data**: Initialized dataframe for population data by state and year.

3. **Data Processing**
  - **Legalization Dates**: Extracted the first date of revenue data for each state to determine the legalization date of online sports betting.
  - **Data Exclusion**: Removed rows where the state is 'United States' and excluded data for the years 2020 and 2024 due to anomalies caused by the pandemic.
  - **Merging Data**: Merged gambling revenue data with sports betting revenue data to calculate the percentage of sports betting revenue to total gambling revenue and the revenue excluding sports betting.

4. **Data Visualization**
  - **Trending Analysis**: Plotted longitudinal graphs to visualize the trends in gambling revenue and sports betting revenue for each state over time.
  - **Ranking Analysis**: Created bar charts to rank states by gambling revenue and sports betting revenue for specific years.
  - **Distribution Analysis**: Plotted histograms to analyze the distribution of gambling revenue and sports betting revenue across states.
  - **Average and Variance Analysis**: Calculated and plotted the average and variance of gambling revenue and sports betting revenue over time.

5. **Statistical Analysis**
  - **T-Test on Revenue Increase Rate**: Conducted a two-sample t-test to compare the monthly revenue increase rates before and after the legalization of online sports betting in 2018. The results indicated a significant increase in the revenue growth rate after 2018.
  - **Correlation Analysis**: Analyzed the relationship between crime rates and gambling revenue per capita. The results showed no significant correlation between the two.

6. **Ethical Considerations**
  - **Ethical Reporting**: Ensured that the findings were presented in a balanced and accessible manner, considering the potential social and economic impacts of gambling.


### Key Findings
- **Revenue Growth**: The analysis showed a significant increase in gambling revenue growth rates after the legalization of online sports betting in 2018.
- **Crime Rates**: There was no significant correlation between crime rates and gambling revenue per capita.
- **Problem Gambling**: States with higher gambling revenue did not necessarily spend more on problem gambling, indicating a potential gap in addressing gambling-related issues.


